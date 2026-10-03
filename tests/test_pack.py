"""Mutation checks of structural validation, independent of live installation."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate_pack', ROOT / 'scripts/validate_pack.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class Pack(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')

    def edit(self, relative, transform):
        path = self.root / 'skills' / relative
        path.write_text(transform(path.read_text(encoding='utf-8')), encoding='utf-8')

    def test_valid_pack(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_sibling(self):
        shutil.rmtree(self.root / 'skills/ai-work-delivery')
        self.assertTrue(any('missing' in e for e in validator.validate(self.root)))

    def test_missing_reference(self):
        (self.root / 'skills/ai-work/references/routing.md').unlink()
        self.assertTrue(any('missing local link' in e for e in validator.validate(self.root)))

    def test_missing_route(self):
        self.edit('ai-work/SKILL.md', lambda t: t.replace('(../ai-work-delivery/SKILL.md)', '(references/routing.md)'))
        self.assertTrue(any('missing sibling route' in e for e in validator.validate(self.root)))

    def test_frontmatter_and_name(self):
        for transform in (lambda t: t.replace('name: ai-work\n', 'name: INVALID_NAME\n', 1),
                          lambda t: t.replace('---', '', 1)):
            with self.subTest(transform=transform):
                path = self.root / 'skills/ai-work/SKILL.md'
                original = path.read_text(encoding='utf-8')
                self.edit('ai-work/SKILL.md', transform)
                self.assertTrue(validator.validate(self.root))
                path.write_text(original, encoding='utf-8')

    def test_private_path_and_scaffold(self):
        self.edit('ai-work/SKILL.md', lambda t: t + '\n' + '/' + 'Users/example/private.txt\nTODO\n')
        errors = validator.validate(self.root)
        self.assertTrue(any('private absolute path' in e for e in errors))
        self.assertTrue(any('scaffold' in e for e in errors))

    def test_missing_helper_and_escape(self):
        (self.root / 'skills/ai-work-knowledge/scripts/check_sources.py').unlink()
        self.edit('ai-work/SKILL.md', lambda t: t + '\n[escape](../../../outside.md)\n')
        errors = validator.validate(self.root)
        self.assertTrue(any('missing required helper' in e for e in errors))
        self.assertTrue(any('escapes skills' in e for e in errors))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Validate pack structure only; this does not certify skill behavior or privacy."""
import argparse
import json
import re
from pathlib import Path

SKILLS = ('ai-work', 'ai-work-delivery', 'ai-work-distill',
          'ai-work-intelligence', 'ai-work-knowledge',
          'ai-work-orchestration', 'ai-work-workflow')
REQUIRED_SCRIPTS = ('ai-work-knowledge/scripts/check_sources.py',
                    'ai-work-orchestration/scripts/check_plan.py')
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
PRIVATE_PATH = re.compile(r'(?:/Users/[^/\s]+|/home/[^/\s]+|/private/var/|\.codex/artifacts/)')
SCAFFOLD = re.compile(r'\b(?:TODO|FIXME)\b|\[INSERT[^\]]*\]|<YOUR_[A-Z_]+>')


def validate(root):
    root = Path(root).resolve()
    skills = root / 'skills'
    errors = []
    found = {p.name for p in skills.iterdir() if p.is_dir()} if skills.is_dir() else set()
    if found != set(SKILLS):
        errors.append('skill directories differ: missing=%s unexpected=%s' %
                      (sorted(set(SKILLS) - found), sorted(found - set(SKILLS))))
    for name in SKILLS:
        path = skills / name / 'SKILL.md'
        if not path.is_file():
            errors.append('%s: missing SKILL.md' % name)
            continue
        text = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        fields = {}
        if not match:
            errors.append('%s: malformed frontmatter' % name)
        else:
            for line in match.group(1).splitlines():
                item = re.fullmatch(r'([a-z][a-z_-]*):\s*(.+)', line)
                if not item or item.group(1) in fields:
                    errors.append('%s: invalid or duplicate frontmatter field' % name)
                else:
                    fields[item.group(1)] = item.group(2).strip().strip('\"\'')
            if fields.get('name') != name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields.get('name', '')):
                errors.append('%s: frontmatter name must match directory' % name)
            if not fields.get('description'):
                errors.append('%s: missing description' % name)
    for path in sorted(skills.rglob('*')):
        if path.is_symlink():
            errors.append('%s: symlinks are unsupported' % path.relative_to(root))
            continue
        if not path.is_file() or path.suffix not in ('.md', '.py', '.yaml'):
            continue
        text = path.read_text(encoding='utf-8')
        label = str(path.relative_to(root))
        if PRIVATE_PATH.search(text):
            errors.append('%s: private absolute path or artifact locator' % label)
        if SCAFFOLD.search(text):
            errors.append('%s: unfinished scaffold marker' % label)
        if path.suffix == '.md':
            for raw in LINK.findall(text):
                target = raw.split()[0].strip('<>').split('#')[0]
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(skills.resolve())
                except ValueError:
                    errors.append('%s: local link escapes skills: %s' % (label, target))
                    continue
                if not resolved.exists():
                    errors.append('%s: missing local link: %s' % (label, target))
    entry = skills / 'ai-work/SKILL.md'
    if entry.is_file():
        targets = set(LINK.findall(entry.read_text(encoding='utf-8')))
        for name in SKILLS[1:]:
            if '../%s/SKILL.md' % name not in targets:
                errors.append('ai-work: missing sibling route to %s' % name)
    for relative in REQUIRED_SCRIPTS:
        if not (skills / relative).is_file():
            errors.append('missing required helper: %s' % relative)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    print(json.dumps({'scope': 'structure, local links, known private-path patterns',
                      'valid': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())

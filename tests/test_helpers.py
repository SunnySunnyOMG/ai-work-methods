"""Behavioral checks of plan/provenance contracts; standard library only."""
import hashlib, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'skills'

class Helpers(unittest.TestCase):
    def invoke(self, script, data, *args, directory=None):
        with tempfile.TemporaryDirectory() as d:
            root=Path(directory or d); path=root/'input.json'; path.write_text(json.dumps(data))
            run=subprocess.run([sys.executable,str(script),str(path),*args],text=True,capture_output=True,timeout=2)
            return run.returncode,json.loads(run.stdout)
    def assert_unreadable_source(self, root, path):
        data={'sources':[{'id':'s','path':path,'sha256':'0'*64}],'claims':[{'id':'a','source_ids':['s']},{'id':'b','depends_on':['a']}]}
        code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,directory=root)
        self.assertEqual(code,2); self.assertEqual(out['source_states']['s'],'unreadable')
        self.assertEqual(out['changed_sources'],['s']); self.assertEqual(out['affected_claims'],['a','b'])
        self.assertTrue(out['errors'])
    def assert_invalid_manifest(self, path, *args):
        run=subprocess.run([sys.executable,str(ROOT/'ai-work-knowledge/scripts/check_sources.py'),str(path),*args],text=True,capture_output=True,timeout=2)
        self.assertEqual(run.returncode,2); out=json.loads(run.stdout)
        self.assertTrue(out['errors']); self.assertEqual(out['affected_claims'],[])
        self.assertEqual(run.stderr,'')
    @unittest.skipUnless(hasattr(os,'symlink'),'symlinks unavailable')
    def test_source_symlink_loop_propagates_review(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'loop').symlink_to('loop')
            self.assert_unreadable_source(d,'loop')
    @unittest.skipUnless(hasattr(os,'symlink'),'symlinks unavailable')
    def test_regular_symlink_preserves_root_boundary(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            root=Path(d); source=root/'source.txt'; source.write_bytes(b'original')
            link=root/'link'; link.symlink_to(source)
            data={'sources':[{'id':'s','path':'link','sha256':hashlib.sha256(b'original').hexdigest()}],'claims':[]}
            code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,directory=d)
            self.assertEqual(code,0); self.assertEqual(out['source_states']['s'],'matches')
            link.unlink(); remote=Path(outside)/'source.txt'; remote.write_bytes(b'original'); link.symlink_to(remote)
            code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,directory=d)
            self.assertEqual(code,2); self.assertEqual(out['source_states']['s'],'invalid')
    @unittest.skipUnless(hasattr(os,'mkfifo'),'FIFO unavailable')
    def test_fifo_source_does_not_wait_for_writer(self):
        with tempfile.TemporaryDirectory() as d:
            os.mkfifo(Path(d)/'fifo')
            self.assert_unreadable_source(d,'fifo')
    @unittest.skipUnless(hasattr(os,'symlink'),'symlinks unavailable')
    def test_manifest_and_root_symlink_loops_return_json(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); loop=root/'loop'; loop.symlink_to('loop')
            self.assert_invalid_manifest(loop)
            manifest=root/'manifest.json'; manifest.write_text('{"sources":[],"claims":[]}')
            self.assert_invalid_manifest(manifest,'--root',str(loop))
    @unittest.skipUnless(hasattr(os,'mkfifo'),'FIFO unavailable')
    def test_fifo_manifest_does_not_wait_for_writer(self):
        with tempfile.TemporaryDirectory() as d:
            fifo=Path(d)/'fifo'; os.mkfifo(fifo)
            self.assert_invalid_manifest(fifo)
    def test_independent_and_ordered_writes(self):
        script=ROOT/'ai-work-orchestration/scripts/check_plan.py'
        data={'tasks':[{'id':'a','depends_on':[],'writes':['report']},{'id':'b','depends_on':['a'],'writes':[]},{'id':'c','depends_on':['b'],'writes':['report']},{'id':'d','depends_on':[],'writes':['index']}]}
        code,out=self.invoke(script,data); self.assertEqual(code,0); self.assertEqual(out['ready'],['a','d'])
    def test_unordered_write_conflict(self):
        code,out=self.invoke(ROOT/'ai-work-orchestration/scripts/check_plan.py',{'tasks':[{'id':'a','writes':['report']},{'id':'b','writes':['report']}]})
        self.assertEqual(code,2); self.assertEqual(len(out['write_conflicts']),1)
    def test_cycle_and_missing_dependency(self):
        script=ROOT/'ai-work-orchestration/scripts/check_plan.py'
        for tasks in [[{'id':'a','depends_on':['b']},{'id':'b','depends_on':['a']}],[{'id':'a','depends_on':['missing']}]]:
            code,out=self.invoke(script,{'tasks':tasks}); self.assertEqual(code,2); self.assertTrue(out['errors'])
    def test_duplicate_and_wrong_type(self):
        script=ROOT/'ai-work-orchestration/scripts/check_plan.py'
        for tasks in [[{'id':'a'},{'id':'a'}],[{'id':'a','depends_on':'b'}]]:
            code,out=self.invoke(script,{'tasks':tasks}); self.assertEqual(code,2)
    def test_hash_and_affected_closure(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'source.txt').write_bytes(b'original')
            data={'sources':[{'id':'s','path':'source.txt','sha256':hashlib.sha256(b'original').hexdigest()}],'claims':[{'id':'a','source_ids':['s']},{'id':'b','depends_on':['a']},{'id':'c','source_ids':[]}]}
            code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,'--changed','s',directory=d)
            self.assertEqual(code,0); self.assertEqual(out['affected_claims'],['a','b'])
            (root/'source.txt').write_bytes(b'changed')
            code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,directory=d)
            self.assertEqual(code,2); self.assertEqual(out['changed_sources'],['s']); self.assertEqual(out['affected_claims'],['a','b'])
            (root/'source.txt').unlink()
            code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',data,directory=d)
            self.assertEqual(code,2); self.assertEqual(out['affected_claims'],['a','b'])
    def test_missing_escape_and_unknown_claim_source(self):
        script=ROOT/'ai-work-knowledge/scripts/check_sources.py'
        for path in ['missing.txt','../outside.txt']:
            code,out=self.invoke(script,{'sources':[{'id':'s','path':path,'sha256':'0'*64}],'claims':[]}); self.assertEqual(code,2)
        code,out=self.invoke(script,{'sources':[],'claims':[{'id':'a','source_ids':['missing']}]}); self.assertEqual(code,2)
    def test_claim_cycle(self):
        code,out=self.invoke(ROOT/'ai-work-knowledge/scripts/check_sources.py',{'sources':[],'claims':[{'id':'a','depends_on':['b']},{'id':'b','depends_on':['a']}]})
        self.assertEqual(code,2)
if __name__=='__main__': unittest.main()

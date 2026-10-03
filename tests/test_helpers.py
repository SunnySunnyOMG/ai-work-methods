"""Behavioral checks of plan/provenance contracts; standard library only."""
import hashlib, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'skills'

class Helpers(unittest.TestCase):
    def invoke(self, script, data, *args, directory=None):
        with tempfile.TemporaryDirectory() as d:
            root=Path(directory or d); path=root/'input.json'; path.write_text(json.dumps(data))
            run=subprocess.run([sys.executable,str(script),str(path),*args],text=True,capture_output=True)
            return run.returncode,json.loads(run.stdout)
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

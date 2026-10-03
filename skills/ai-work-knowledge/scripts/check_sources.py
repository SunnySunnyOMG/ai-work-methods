"""Read-only local source integrity/dependency check; does not judge truth or semantics."""
import argparse, hashlib, json, re, sys
from pathlib import Path

def check(data,root,changed):
    errors=[]; sources={}; claims={}; states={}; mismatches=[]
    if not isinstance(data,dict) or any(not isinstance(data.get(k),list) for k in ['sources','claims']):
        return {'errors':['expected sources and claims arrays'],'changed_sources':[],'affected_claims':[],'source_states':{}}
    for kind,target in [('sources',sources),('claims',claims)]:
        for entry in data[kind]:
            if not isinstance(entry,dict) or not isinstance(entry.get('id'),str) or not entry['id'].strip(): errors.append(f'{kind}: missing string id'); continue
            ident=entry['id']
            if ident in target or ident in (claims if kind=='sources' else sources): errors.append(f'duplicate identity: {ident}'); continue
            target[ident]=entry
    for ident,source in sources.items():
        path=source.get('path'); expected=source.get('sha256')
        if not isinstance(path,str) or not path or not isinstance(expected,str) or not re.fullmatch(r'[0-9a-f]{64}',expected):
            errors.append(f'{ident}: relative path and lowercase sha256 required'); states[ident]='invalid'; continue
        local=Path(path)
        if local.is_absolute() or not (root/local).resolve().is_relative_to(root):
            errors.append(f'{ident}: path outside root'); states[ident]='invalid'; continue
        try:
            h=hashlib.sha256()
            with (root/local).open('rb') as f:
                for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
            if h.hexdigest()==expected: states[ident]='matches'
            else: states[ident]='changed'; mismatches.append(ident)
        except OSError: states[ident]='unreadable'; errors.append(f'{ident}: source unreadable'); mismatches.append(ident)
    for ident,claim in claims.items():
        for key,target in [('source_ids',sources),('depends_on',claims)]:
            value=claim.get(key,[])
            if not isinstance(value,list) or any(not isinstance(x,str) for x in value): errors.append(f'{ident}: {key} must be string array'); continue
            for item in value:
                if item not in target: errors.append(f'{ident}: unknown {key} identity {item}')
    # Iterative graph walk avoids recursion limits on large provenance chains.
    if not errors:
        degrees={ident:len(set(c.get('depends_on',[]))) for ident,c in claims.items()}; children={ident:[] for ident in claims}
        for ident,claim in claims.items():
            for dep in set(claim.get('depends_on',[])): children[dep].append(ident)
        ready=[i for i,d in degrees.items() if d==0]; visited=0
        while ready:
            ident=ready.pop(); visited+=1
            for child in children[ident]:
                degrees[child]-=1
                if degrees[child]==0: ready.append(child)
        if visited!=len(claims): errors.append('claim dependency cycle')
    unknown=set(changed)-set(sources)-set(claims)
    if unknown: errors.append('unknown changed identities: '+', '.join(sorted(unknown)))
    affected=set(changed)|set(mismatches)
    valid_claim_fields=all(isinstance(c.get(k,[]),list) and all(isinstance(v,str) for v in c.get(k,[])) for c in claims.values() for k in ['source_ids','depends_on'])
    if valid_claim_fields:
        # Even an unreadable source requires downstream review; no content claim is made.
        again=True
        while again:
            again=False
            for ident,claim in claims.items():
                if ident not in affected and (set(claim.get('source_ids',[]))|set(claim.get('depends_on',[])))&affected:
                    affected.add(ident); again=True
    return {'errors':errors,'source_states':states,'changed_sources':sorted(set(mismatches)),'affected_claims':sorted(set(claims)&affected),'scope':'Hashes and declared dependencies only; no truth, semantic support or completeness guarantee.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('manifest',type=Path); parser.add_argument('--root',type=Path); parser.add_argument('--changed',action='append',default=[]); args=parser.parse_args()
    root=(args.root or args.manifest.resolve().parent).resolve()
    try: result=check(json.loads(args.manifest.read_text()),root,args.changed)
    except (OSError,ValueError): result={'errors':['invalid or unreadable manifest'],'changed_sources':[],'affected_claims':[],'source_states':{}}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 2 if result['errors'] or result['changed_sources'] else 0
if __name__=='__main__': sys.exit(main())

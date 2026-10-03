"""Read-only local source integrity/dependency check; does not judge truth or semantics."""
import argparse, hashlib, json, os, re, stat, sys
from pathlib import Path

def open_regular(path):
    """Reject special files before opening, and recheck the opened descriptor."""
    if not stat.S_ISREG(path.stat().st_mode):
        raise OSError('regular file required')
    # Nonblocking open prevents a swapped-in FIFO waiting for a writer. Avoid
    # following a swapped-in final symlink where the platform supports it.
    fd=os.open(path,os.O_RDONLY|getattr(os,'O_NONBLOCK',0)|getattr(os,'O_NOFOLLOW',0))
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError('regular file required')
        return os.fdopen(fd,'rb')
    except BaseException:
        os.close(fd)
        raise

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
        if local.is_absolute():
            errors.append(f'{ident}: path outside root'); states[ident]='invalid'; continue
        try:
            resolved=(root/local).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f'{ident}: path outside root'); states[ident]='invalid'; continue
            h=hashlib.sha256()
            with open_regular(resolved) as f:
                for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
            if h.hexdigest()==expected: states[ident]='matches'
            else: states[ident]='changed'; mismatches.append(ident)
        except (OSError,ValueError,RuntimeError): states[ident]='unreadable'; errors.append(f'{ident}: source unreadable'); mismatches.append(ident)
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
    try:
        manifest=args.manifest.resolve(strict=True)
        root=(args.root or manifest.parent).resolve(strict=True)
        if not root.is_dir(): raise OSError('root directory required')
        with open_regular(manifest) as f: data=json.load(f)
        result=check(data,root,args.changed)
    except (OSError,ValueError,RuntimeError): result={'errors':['invalid or unreadable manifest or root'],'changed_sources':[],'affected_claims':[],'source_states':{}}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 2 if result['errors'] or result['changed_sources'] else 0
if __name__=='__main__': sys.exit(main())

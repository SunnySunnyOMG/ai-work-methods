"""Read-only DAG and exact-name shared-write checks; never executes a task."""
import argparse, json, sys
from collections import deque

def check(data):
    errors=[]; tasks={}
    if not isinstance(data,dict) or not isinstance(data.get('tasks'),list):
        return {'errors':['expected object with tasks array'],'write_conflicts':[],'ready':[],'order':[]}
    for task in data['tasks']:
        if not isinstance(task,dict) or not isinstance(task.get('id'),str) or not task['id'].strip():
            errors.append('task needs nonempty string id'); continue
        ident=task['id']
        if ident in tasks: errors.append(f'duplicate task id: {ident}'); continue
        valid=True
        for key in ['depends_on','writes']:
            value=task.get(key,[])
            if not isinstance(value,list) or any(not isinstance(v,str) or not v.strip() for v in value):
                errors.append(f'{ident}: {key} needs nonempty string array'); valid=False
            elif len(value)!=len(set(value)): errors.append(f'{ident}: duplicate {key}'); valid=False
        if valid: tasks[ident]=task
    for ident,task in tasks.items():
        for dep in task.get('depends_on',[]):
            if dep not in tasks: errors.append(f'{ident}: unknown dependency {dep}')
    if errors: return {'errors':errors,'write_conflicts':[],'ready':[],'order':[]}
    degrees={ident:len(task.get('depends_on',[])) for ident,task in tasks.items()}
    children={ident:[] for ident in tasks}
    for ident,task in tasks.items():
        for dep in task.get('depends_on',[]): children[dep].append(ident)
    ready=sorted(ident for ident,degree in degrees.items() if degree==0)
    queue=deque(ready); order=[]; ancestors={ident:set() for ident in tasks}
    while queue:
        ident=queue.popleft(); order.append(ident)
        for child in sorted(children[ident]):
            ancestors[child].update(ancestors[ident]|{ident}); degrees[child]-=1
            if degrees[child]==0: queue.append(child)
    if len(order)!=len(tasks): errors.append('dependency cycle; unresolved: '+', '.join(sorted(ident for ident in tasks if ident not in order)))
    conflicts=[]; resources={}
    for ident,task in tasks.items():
        for resource in task.get('writes',[]): resources.setdefault(resource,[]).append(ident)
    if not errors:
        for resource,writers in sorted(resources.items()):
            for i,a in enumerate(writers):
                for b in writers[i+1:]:
                    if a not in ancestors[b] and b not in ancestors[a]: conflicts.append({'resource':resource,'tasks':sorted([a,b])})
    return {'errors':errors,'write_conflicts':conflicts,'ready':ready,'order':order,'scope':'Structure and exact resource names only; not semantic independence, permissions or task success.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('plan'); args=parser.parse_args()
    try:
        with open(args.plan,encoding='utf-8') as f: result=check(json.load(f))
    except (OSError,ValueError) as e: result={'errors':[type(e).__name__+': invalid or unreadable plan'],'write_conflicts':[],'ready':[],'order':[]}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 2 if result['errors'] or result['write_conflicts'] else 0
if __name__=='__main__': sys.exit(main())

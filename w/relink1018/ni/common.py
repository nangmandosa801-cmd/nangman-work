import json,os
inv=json.load(open('/home/claude/w/relink1018/ni/inv.json')); idx=json.load(open('/home/claude/w/relink1018/ni/idx.json'))
R={r['slug']:r for r in json.load(open('/home/claude/sched/convert_res.json'))}
def pick(s,a):
    c=idx.get(a,[])
    for p in c:
        if p.startswith(f'/mnt/user-data/outputs/int/{s}/'): return p
    for p in c:
        if p.startswith('/mnt/user-data/uploads/블로그/interior/'+R[s]['top']+'/'): return p
    for p in c:
        if '/mnt/user-data/uploads' in p: return p
    return c[0] if c else None

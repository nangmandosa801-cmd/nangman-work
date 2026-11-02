import json,re,time,difflib,html,os
from tailparse import fetch,paras
exec(open('tailbuild.py').read().split("A='style")[0])  # T,G,DESC,Lk
PUB={no:t for no,t in T.items()}
def norm(s): return re.sub(r'[\s|,·()]','',s)
def match(txt):
    best=None;bs=0
    for no,t in PUB.items():
        r=difflib.SequenceMatcher(None,norm(txt),norm(t)).ratio()
        if r>bs: bs,best=r,no
    return best if bs>=0.72 else None
res={}
for tgt in G:
    P=paras(fetch(tgt)); time.sleep(3)
    ks=[i for i,p in enumerate(P) if '함께 보면' in p['t']]
    items=[]
    if ks:
        seg=P[ks[-1]+1:]
        for i,p in enumerate(seg):
            if p['c']=='#2e5c8a' and p['fs']=='16' and 'NANGMAN' in p['t']: break
            if p['c']=='#2e5c8a' and p['fs']=='19' and p['t']:
                no=p['l'][0] if p['l'] else match(p['t'])
                d=''
                if i+1<len(seg) and seg[i+1]['c']=='#7a8590': d=re.sub(r'\s*\(발행 예정\)','',seg[i+1]['t'])
                items.append((no,d,p['t']))
    res[tgt]=dict(found=bool(ks),items=items)
    print(tgt,bool(ks),len(items),sum(1 for x in items if x[0]),flush=True)
json.dump(res,open('/tmp/claude-0/tailexist.json','w'),ensure_ascii=False)

import json,re,time,html,os
from tailparse import fetch,paras
exec(open('tailfull.py').read().split("res={}")[0])
res=json.load(open('/tmp/claude-0/tailexist.json'))
for tgt in ['224383649942','224401854235','224381460159']:
    P=paras(fetch(tgt)); time.sleep(3)
    end=next((i for i,p in enumerate(P) if '답이 아니라 방법' in p['t']),len(P))
    heads=[i for i,p in enumerate(P[:end]) if p['fs']=='24' and p['t']]
    items=[]
    if heads:
        h=heads[-1]
        for i in range(h+1,end):
            p=P[i]
            if p['c']=='#2e5c8a' and p['fs']=='19' and p['l']:
                d=P[i+1]['t'] if i+1<end and P[i+1]['c']=='#7a8590' else ''
                items.append((p['l'][0],d,p['t']))
    res[tgt]=dict(found=True,items=items); print(tgt,len(items))
json.dump(res,open('/tmp/claude-0/tailexist.json','w'),ensure_ascii=False)

import re,sys,pickle,time
sys.argv=['x']
src=open('/home/claude/w/expand/scan.py').read().split('REG=')[0].replace('datetime.datetime(2026,10,8','datetime.datetime(2026,10,20')
exec(src)
import json
Q=json.loads(open('qs.json').read())
from concurrent.futures import ThreadPoolExecutor
_,P=pickle.load(open('scan3.pkl','rb'))
for q in Q:
    r=ranks(q); bs=[b for b,_ in sorted(r.items(),key=lambda x:x[1])][:15]
    new=[b for b in bs if b not in P]
    with ThreadPoolExecutor(8) as ex:
        for b,p in zip(new,ex.map(rss,new)): P[b]=p
    print('#',q)
    for b in bs:
        p=P[b]; ts=p['titles']
        if not ts: continue
        mv=sum(1 for t in ts if re.search('이사|포장|이삿짐',t))/len(ts)
        if mv<0.6 or p['n30']>30 or p['n30']<1: continue
        print('  ',p['n30'],b,'|',p['name'][:30],p['ph'][:1],'|',p['desc'][:60].replace('\n',' '),'|',ts[0][:40])
    time.sleep(1)
pickle.dump((_,P),open('scan3.pkl','wb'))

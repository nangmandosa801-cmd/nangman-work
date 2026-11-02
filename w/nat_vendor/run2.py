import sys,json,re,pickle,time
sys.path.insert(0,'/home/claude/w/expand')
from scan import ranks,rss
from concurrent.futures import ThreadPoolExecutor
exec(open('run.py').read().split('qs=')[0].split('from concurrent.futures import ThreadPoolExecutor')[1])
done=pickle.load(open('raw.pkl','rb'))
hits,P=done
need=['부산','대전','세종','충북','충남','강원','제주']
qs=[(rg,c,q.format(city)) for rg,cs in REG.items() if rg in need for city in cs for c,(qq,_) in CAT.items() for q in qq]
def slow(t):
    time.sleep(0.8); r=ranks(t[2])
    if not r: time.sleep(3); r=ranks(t[2])
    return (t,r)
with ThreadPoolExecutor(3) as ex: res=list(ex.map(slow,qs))
print(sum(1 for _,r in res if r),'/',len(qs),'nonempty',flush=True)
for (rg,c,q),r in res:
    for b,rk in r.items(): hits.setdefault((rg,c,b),[]).append(rk)
nb=sorted({b for (_,_,b) in hits if b not in P})
with ThreadPoolExecutor(6) as ex: P.update(dict(zip(nb,ex.map(rss,nb))))
pickle.dump((hits,P),open('raw.pkl','wb'))

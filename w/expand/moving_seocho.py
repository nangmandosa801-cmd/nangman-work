import re,json,time,pickle,sys
sys.argv=['x']
src=open('scan.py').read().split('REG=')[0]
exec(src)
Q=[]
for r in ['서초','방배','반포','강남','송파','잠실','동작','사당','관악','강동','성남 분당','과천']:
    for k in ['포장이사','포장이사 후기','아파트 포장이사','이사업체','이사 직영']:
        Q.append(f'{r} {k}')
from concurrent.futures import ThreadPoolExecutor
hits={}
for i in range(0,len(Q),4):
    with ThreadPoolExecutor(4) as ex:
        for q,r in zip(Q[i:i+4],ex.map(ranks,Q[i:i+4])):
            for b,rk in r.items(): hits.setdefault(b,[]).append((q,rk))
    time.sleep(1.3)
print('blogs',len(hits))
with ThreadPoolExecutor(8) as ex: P=dict(zip(hits,ex.map(rss,hits)))
pickle.dump((hits,P),open('moving_seocho.pkl','wb'))
out=[]
for b,p in P.items():
    ts=p['titles'];
    if not ts: continue
    mv=sum(1 for t in ts if re.search('이사|용달|포장',t))
    if mv/len(ts)<0.5 or not(1<=p['n30']<=25): continue
    out.append(dict(b=b,name=p['name'],n30=p['n30'],ph=p['ph'],nq=len(hits[b]),desc=p['desc'][:120],t=ts[:6]))
out.sort(key=lambda x:-x['nq'])
json.dump(out,open('moving_seocho.json','w'),ensure_ascii=False,indent=0)
for o in out[:45]: print(o['nq'],o['n30'],o['b'],o['name'][:20],o['ph'],'|',' / '.join(o['t'][:3])[:150])

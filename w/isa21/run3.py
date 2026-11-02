import re,json,time,pickle,sys,collections
sys.argv=['x']
src=open('/home/claude/w/expand/scan.py').read().split('REG=')[0].replace('datetime.datetime(2026,10,8','datetime.datetime(2026,10,20')
exec(src)
REG={'서울동북':['노원구','도봉구','중랑구','성북구','강북구','동대문구','월계동','장위동','길음','창동'],
'서울서북':['은평구','마포구','서대문구','종로','용산','불광동','수색','아현','홍제'],
'경기북부':['일산서구','일산동구','덕양구','파주','운정','의정부','옥정','동두천','포천','고양 지축'],
'경기동부':['하남','미사','남양주','구리','별내','다산','진접','감일','위례']}
Q=[]
for g,rs in REG.items():
    for r in rs:
        for k in ['포장이사','포장이사 아파트','이삿짐센터 후기']:
            Q.append((g,f'{r} {k}'))
from concurrent.futures import ThreadPoolExecutor
hits={}
for i in range(0,len(Q),4):
    ch=Q[i:i+4]
    with ThreadPoolExecutor(4) as ex:
        for (g,q),r in zip(ch,ex.map(lambda x:ranks(x[1]),ch)):
            for b,rk in r.items(): hits.setdefault(b,[]).append((g,q,rk))
    time.sleep(1.2)
_,P0=pickle.load(open('scan2.pkl','rb'))
new=[b for b in hits if b not in P0]
with ThreadPoolExecutor(8) as ex: P=dict(zip(new,ex.map(rss,new)))
P.update({b:P0[b] for b in hits if b in P0})
pickle.dump((hits,P),open('scan3.pkl','wb'))
for b,p in P.items():
    ts=p['titles']
    if not ts or len(ts)<5: continue
    mv=sum(1 for t in ts if re.search('이사|포장|이삿짐',t))
    if mv/len(ts)<0.6 or p['n30']<2 or p['n30']>40: continue
    co=re.search('이사|익스프레스|이삿짐|무빙|로지스|통운|express|moving|물류|트랜스',p['name'],re.I) or p['ph']
    if not co: continue
    if re.search('통인|영구|이사방|KGB|짐싸|다방|로젠|용달|원룸|소형|GS이사|다해주는|박스가드|슈퍼맨|무빙코리아|살구',p['name']+p['desc'][:60]): continue
    regs=collections.Counter(g for g,q,r in hits[b]).most_common(2)
    print(len(hits[b]),p['n30'],b,'|',p['name'][:34],p['ph'][:2],[r[0] for r in regs],'|',p['desc'][:70].replace('\n',' '),'|',ts[0][:45])

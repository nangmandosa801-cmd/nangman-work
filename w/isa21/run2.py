import re,json,time,pickle,sys,collections
sys.argv=['x']
src=open('/home/claude/w/expand/scan.py').read().split('REG=')[0].replace('datetime.datetime(2026,10,8','datetime.datetime(2026,10,20')
exec(src)
REG={'서울동남':['송파','강동','강남','광진'],'서울서남':['강서','양천','영등포','관악','금천'],
'서울동북':['노원','도봉','중랑','성북','동대문','상계동','중계동'],'서울서북':['은평','마포','서대문','상암'],
'경기남부':['수원','용인 수지','분당','동탄','안양 평촌','광명'],'경기동부':['하남','남양주','구리','별내','다산','미사','위례','감일'],
'경기북부':['일산','고양 삼송','파주','의정부','양주','김포'],'인천':['송도','청라','부천','인천 남동구','부평','검단']}
Q=[]
for g,rs in REG.items():
    for r in rs:
        for k in ['포장이사 현장','보관이사','이사 익스프레스','포장이사 전문업체']:
            Q.append((g,f'{r} {k}'))
from concurrent.futures import ThreadPoolExecutor
hits={}
for i in range(0,len(Q),4):
    ch=Q[i:i+4]
    with ThreadPoolExecutor(4) as ex:
        for (g,q),r in zip(ch,ex.map(lambda x:ranks(x[1]),ch)):
            for b,rk in r.items(): hits.setdefault(b,[]).append((g,q,rk))
    time.sleep(1.2)
old,P0=pickle.load(open('scan.pkl','rb'))
new=[b for b in hits if b not in P0]
print('blogs',len(hits),'new',len(new),flush=True)
with ThreadPoolExecutor(8) as ex: P=dict(zip(new,ex.map(rss,new)))
P.update({b:P0[b] for b in hits if b in P0})
pickle.dump((hits,P),open('scan2.pkl','wb'))
for b,p in P.items():
    ts=p['titles']
    if not ts or len(ts)<5: continue
    mv=sum(1 for t in ts if re.search('이사|포장|이삿짐',t))
    if mv/len(ts)<0.6 or p['n30']<2 or p['n30']>40: continue
    co=re.search('이사|익스프레스|이삿짐|무빙|로지스|통운|express|moving|물류|트랜스',p['name'],re.I) or p['ph']
    if not co: continue
    if re.search('통인|영구|이사방|KGB|짐싸|다방|로젠|용달|원룸|소형|GS이사|다해주는|박스가드|슈퍼맨',p['name']+p['desc'][:60]): continue
    regs=collections.Counter(g for g,q,r in hits[b]).most_common(2)
    print(len(hits[b]),p['n30'],b,'|',p['name'][:34],p['ph'][:2],[r[0] for r in regs],'|',p['desc'][:70].replace('\n',' '),'|',ts[0][:45])

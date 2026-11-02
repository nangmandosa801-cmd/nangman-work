import re,json,time,pickle,sys,datetime
sys.argv=['x']
src=open('/home/claude/w/expand/scan.py').read().split('REG=')[0]
src=src.replace('datetime.datetime(2026,10,8','datetime.datetime(2026,10,19')
exec(src)
REG={'서울동남':['송파','강동','강남','서초','광진'],'서울서남':['강서','양천','영등포','구로','관악','동작'],
'서울동북':['노원','도봉','중랑','성북','강북'],'서울서북':['은평','마포','서대문'],
'경기남부':['수원','용인','성남 분당','화성 동탄','안양','광교'],'경기동부':['하남','남양주','구리','미사','다산'],
'경기북부':['일산','고양','파주 운정','의정부','양주 옥정'],'인천':['인천 송도','인천 청라','부천','인천 검단','인천 서구']}
Q=[]
for g,rs in REG.items():
    for r in rs:
        for k in ['포장이사','포장이사 후기','이삿짐센터','포장이사 업체 추천']:
            Q.append((g,f'{r} {k}'))
from concurrent.futures import ThreadPoolExecutor
hits={}
for i in range(0,len(Q),4):
    ch=Q[i:i+4]
    with ThreadPoolExecutor(4) as ex:
        for (g,q),r in zip(ch,ex.map(lambda x:ranks(x[1]),ch)):
            for b,rk in r.items(): hits.setdefault(b,[]).append((g,q,rk))
    time.sleep(1.2)
print('blogs',len(hits),flush=True)
with ThreadPoolExecutor(8) as ex: P=dict(zip(hits,ex.map(rss,hits)))
pickle.dump((hits,P),open('scan.pkl','wb'))

from ac import many
import json,collections
REG=['서울','은평','강서','관악','중랑','강북','도봉','노원','마포','송파','광진','구로','양천','동작','성북','영등포','강동',
     '경기','수원','부천','인천','고양','일산','성남','분당','안양','의정부','남양주','화성','용인','평택','김포','하남','구리','광명','시흥','안산',
     '부산','대구','대전','광주','울산','청주','천안','전주','창원','김해','포항','강릉','원주','춘천','제주','세종','충주','목포','여수','구미','경주','군산','익산']
KW=['누수','누수탐지','옥상 방수','빌라 누수','주택 누수','지붕 공사','빌라 리모델링','주택 리모델링','단독주택 리모델링','원룸 입주청소','상가 인테리어','상가 원상복구','외벽 페인트','보일러 교체','샷시 교체','중문','인테리어','입주청소','줄눈','동파']
qs=[f'{r} {k}' for r in REG for k in KW]
R=many(qs,10)
tab={}
for q,v in R.items():
    if not v: continue
    r,k=q.split(' ',1)
    hit=any(x.replace(' ','').startswith(q.replace(' ','')) for x in v)
    tab.setdefault(k,{})[r]=(hit,len(v))
json.dump({k:{r:list(x) for r,x in d.items()} for k,d in tab.items()},open('step3.json','w'),ensure_ascii=False)
for k in KW:
    d=tab.get(k,{}); live=[r for r in REG if d.get(r,(0,0))[0]]
    print(f'{k} ({len(live)}/{len(REG)}): '+' '.join(live))

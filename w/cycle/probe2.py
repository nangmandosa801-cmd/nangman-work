import sys,json
exec(open('/home/claude/ac2.py').read().split('rows=')[0])
from concurrent.futures import ThreadPoolExecutor
seeds={
'동네+인테리어(구축 거래 많은 곳)':['영통 인테리어','산본 인테리어','평촌 인테리어','중계동 인테리어','목동 인테리어','분당 인테리어','일산 인테리어','상계동 인테리어','동탄 인테리어','송도 인테리어','광명 인테리어','수지 인테리어'],
'단지+인테리어/샷시':['헬리오시티 인테리어','파크리오 인테리어','은마 인테리어','잠실엘스 인테리어','올림픽훼밀리 인테리어','중계 그린 인테리어','산본 샷시','평촌 샷시','분당 샷시교체','일산 샷시','목동 샷시','상계동 샷시'],
'동네+공정':['수원 샷시','용인 샷시','안양 샷시','군포 샷시','부천 샷시','수원 탄성코트','인천 줄눈','수원 입주청소','인천 입주청소','분당 입주청소','송도 줄눈','동탄 매트시공'],
'지역+지원금':['수원시 샷시 지원','경기도 노후주택','인천 집수리 지원','서울 창호 지원','경기도 에너지','용인시 집수리'],
'지역+사전점검업체':['검단 사전점검','송도 사전점검','동탄 사전점검','평택 사전점검','파주 사전점검','인천 사전점검'],
'하자':['아파트 하자보수','신축 하자','하자 점검','결로 하자보수','아파트 결로','타일 들뜸'],
}
qs=[q for v in seeds.values() for q in v]
with ThreadPoolExecutor(max_workers=10) as ex: out=dict(ex.map(ac,qs))
json.dump({'seeds':seeds,'out':out},open('/home/claude/w/cycle/probe2.json','w'),ensure_ascii=False,indent=0)
for g,v in seeds.items():
    print('##',g)
    for q in v:
        r=out[q]; print(f'  {q} [{len(r) if r is not None else "x"}] ', ' / '.join((r or [])[:7]))

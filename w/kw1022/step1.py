from ac import many
import json,re
TYPES=['아파트','빌라','다세대','단독주택','주택','오피스텔','원룸','상가','사무실','지식산업센터','전원주택','농막','구축아파트','오래된 아파트','다가구']
ITEMS=['누수','옥상 방수','외벽 방수','동파','보일러 교체','샷시 교체','단열','결로','곰팡이','외풍','중문','도배','리모델링','올수리','욕실 리모델링','원상복구','인테리어','입주청소','이사청소','줄눈','탄성코트','방충망','필름','지붕','외벽 페인트','배관','수리']
qs=[f'{t} {i}' for t in TYPES for i in ITEMS]
R=many(qs)
COM=re.compile(r'비용|가격|업체|견적|시공|공사|교체|수리|추천|후기')
rows=[]
for q,v in R.items():
    if v is None: continue
    sq=q.replace(' ','')
    has=any(x.replace(' ','')==sq for x in v)
    com=sum(1 for x in v if COM.search(x[len(q):] if x.startswith(q) else x))
    rows.append(dict(q=q,n=len(v),self=has,com=com,sug=v[:10]))
json.dump(rows,open('step1.json','w'),ensure_ascii=False,indent=1)
# 유형별 요약
import collections
for t in TYPES:
    r=[x for x in rows if x['q'].startswith(t+' ')]
    top=sorted(r,key=lambda x:(-x['n'],-x['com']))[:8]
    print(f"{t}: 살아있는 조합 {sum(1 for x in r if x['n']>0)}/{len(r)} | "+' · '.join(f"{x['q'][len(t)+1:]}({x['n']}/{x['com']})" for x in top if x['n']>0))

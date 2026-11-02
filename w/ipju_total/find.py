import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['수원','용인','성남','화성','동탄','안양','부천','인천','송도','검단','고양','파주','김포','남양주','구리','하남','의정부','양주','서울','평택','안산','시흥','광명','오산','대전','청주','세종','천안','부산','창원','김해','대구','광주','울산']
QS=['입주 토탈케어','입주케어 업체','입주 케어 패키지','입주 패키지 시공','입주 토탈 시공','줄눈 탄성코트 새집증후군','줄눈 탄성코트 패키지','입주청소 줄눈 탄성코트','줄눈 탄성코트 나노코팅','입주 시공 패키지 가격','신축 아파트 입주 시공 업체','입주 올인원 시공','입주 박람회 줄눈 탄성코트','새집증후군 줄눈 탄성 패키지','입주케어 후기','홈케어 줄눈 탄성코트','입주 전 시공 한번에','입주 시공 순서 업체']+[r+' 입주케어' for r in REG]+[r+' 줄눈 탄성코트' for r in REG]
hits=collections.defaultdict(list)
for q in QS:
    try: s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    except Exception as e: print('ERR',q,e); continue
    its=list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))
    print(q,len(its),flush=True)
    for b,n in its: hits[b].append((q,n))
    time.sleep(0.9)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
print(len(hits),'곳', sum(1 for b,v in c if len(set(q for q,_ in v))>=2),'곳이 2개 넘게')

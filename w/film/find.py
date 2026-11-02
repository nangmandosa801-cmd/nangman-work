import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','고양','일산','파주','김포','남양주','구리','하남','의정부','서울','강남','송파','노원','마포','평택','안산','시흥','광명','대전','청주','세종','천안','부산','창원','김해','대구','광주','울산']
QS=[r+' 인테리어 필름' for r in REG]+[r+' 필름 시공' for r in ['수원','용인','성남','화성','인천','고양','남양주','서울','대전','부산']]+['인테리어 필름 시공 후기','싱크대 필름 시공','방문 필름 시공','샷시 필름 시공','현관문 필름 시공','몰딩 필름 시공','붙박이장 필름 시공','입주 필름 시공','구축 아파트 필름 시공','인테리어 필름 업체']
hits=collections.defaultdict(list)
for q in QS:
    s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    its=list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))
    print(q,len(its),flush=True)
    for b,n in its: hits[b].append((q,n))
    time.sleep(1.0)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
print(len(hits),'곳')
for b,v in c[:90]: print(b,'글',len(set(n for _,n in v)),'검색어',len(set(q for q,_ in v)),'|',' · '.join(sorted(set(q.split()[0] for q,_ in v)))[:80])

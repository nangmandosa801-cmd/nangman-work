import sys,re,json,time,urllib.parse,html,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
QS=['무타공 중문 시공','무타공 중문 설치','무타공 중문 업체','무타공 3연동 중문','무타공 중문 전세','무타공 원슬라이딩 중문','무타공 중문 설치 비용','무타공 중문 가격','전세집 무타공 중문 시공','무타공 중문 후기','무타공 슬라이딩 중문 시공','무타공 중문 서울','무타공 중문 경기','무타공 중문 부산','무타공 중문 인천','무타공 초슬림 중문','무타공 파티션 중문 시공','무타공 스윙도어 중문']
hits=collections.defaultdict(list)
for q in QS:
    for start in (1,):
        s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
        its=re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)
        its=list(dict.fromkeys(its))
        print(q,len(s),len(its),flush=True)
        for b,n in its: hits[b].append((q,n))
    time.sleep(1.2)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
c=sorted(hits.items(),key=lambda x:-len(set(n for _,n in x[1])))
for b,v in c[:60]: print(b,len(set(n for _,n in v)),len(set(q for q,_ in v)))

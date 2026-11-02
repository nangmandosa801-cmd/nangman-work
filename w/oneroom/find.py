import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['서울','강남','관악','신림','마포','성북','동대문','수원','인천','부천','고양','성남','용인','안산','의정부']
QS=[r+' 원룸 리모델링' for r in REG]+['원룸 리모델링','원룸 인테리어 시공','원룸 리모델링 업체','다가구 리모델링','원룸 도배 장판','임대 원룸 리모델링','원룸 올수리','오피스텔 인테리어 시공','원룸 리모델링 비용','다세대 원룸 리모델링']
hits=collections.defaultdict(list)
for q in QS:
    s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    its=list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))
    for b,n in its: hits[b].append((q,n))
    time.sleep(1.0)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
print(len(hits),'곳')
for b,v in c[:50]: print(b,'글',len(set(n for _,n in v)),'검색어',len(set(q for q,_ in v)),'|',' · '.join(sorted(set(q for q,_ in v)))[:110])

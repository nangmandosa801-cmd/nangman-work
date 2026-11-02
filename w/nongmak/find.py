import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['김포','강화','파주','양주','포천','가평','남양주','양평','여주','이천','용인','화성','평택','안성','춘천','홍천','횡성','원주','평창','충주','제천','천안','아산','당진','서산','청주','세종','공주','논산','전주','김해','양산','경주','대구']
QS=['농막 제작','농막 제작 업체','농막 가격','농막 설치 비용','체류형 쉼터 제작','체류형 쉼터 가격','농촌체류형 쉼터 제작','농촌체류형 쉼터 업체','이동식주택 제작','이동식주택 가격','6평 농막','10평 체류형 쉼터','컨테이너 농막','목조 농막','농막 출고','체류형쉼터 출고','이동식주택 전시장','농막 전시장','체류형 쉼터 10평 가격','농막 주문제작','세컨하우스 이동식주택','농막 후기','체류형 쉼터 후기']+[r+' 농막' for r in REG]+[r+' 체류형쉼터' for r in REG[:20]]+[r+' 이동식주택' for r in REG[:14]]
hits=collections.defaultdict(list)
for q in QS:
    try: s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    except Exception as e: print('ERR',q,e); continue
    its=list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))
    for b,n in its: hits[b].append((q,n))
    time.sleep(0.8)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
print(len(QS),'검색어',len(hits),'곳', sum(1 for b,v in c if len(set(q for q,_ in v))>=3),'곳이 3개 넘게')

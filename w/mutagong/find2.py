import sys,re,json,time,urllib.parse,collections,requests
from bs4 import BeautifulSoup
sys.path.insert(0,'/home/claude/blogkit'); import seo
old=json.load(open('hits.json'))
QS=['무타공 3연동 시공사례','전세집 중문 못자국 없이 시공','간이 중문 시공사례 무타공','무타공 가벽 중문 시공','압착식 중문 시공','무타공 중문 시공 전세 3연동 알루미늄','월세집 중문 무타공 시공','무타공 중문 실측 시공 업체','무타공 ㄱ자 중문','무타공 간살 중문 시공','원상복구 중문 시공 무타공','오피스텔 무타공 중문 시공']
hits=collections.defaultdict(list)
for q in QS:
    s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    its=list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))
    print(q,len(its),flush=True)
    for b,n in its: hits[b].append((q,n))
    time.sleep(1.2)
json.dump(hits,open('hits2.json','w'),ensure_ascii=False)
skip=set(old)|{'champion_chart'}
new={b:v for b,v in hits.items() if b not in skip}
print('새 블로그',len(new),'/ 전체',len(hits))
out={}
for b,v in sorted(hits.items(),key=lambda x:-len(set(n for _,n in x[1]))):
    if b in ('champion_chart','lyt777'): continue
    n=v[0][1]
    try: r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
    except Exception: continue
    so=BeautifulSoup(r.text,'html.parser'); tt=so.select_one('.se-title-text'); c=so.select_one('.se-main-container')
    title=tt.get_text(' ',strip=True) if tt else ''; body=c.get_text('\n',strip=True).replace('​','') if c else ''
    ph=sorted(set(re.findall(r'01\d[-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}-\d{3,4}-\d{4}|1\d{3}-\d{4}',body)))
    k=body.count('무타공'); sig=('시공' in body) and bool(ph)
    aff=bool(re.search(r'쿠팡|파트너스|￦|수수료를 제공',body))
    out[b]=dict(n=n,title=title,ph=ph,k=k,aff=aff,nq=len(set(q for q,_ in v)),body=body)
    if (k>=3 and not aff): print(f'{b:18}|{len(set(x for _,x in v))}글|무타공 {k}|전화 {ph[:2]}|{title[:60]}')
    time.sleep(0.6)
json.dump(out,open('posts2.json','w'),ensure_ascii=False)

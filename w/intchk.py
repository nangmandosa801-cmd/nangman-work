import urllib.request,urllib.parse,re,time,html
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def get(u):
    for _ in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
        except Exception as e: time.sleep(3)
    return ''
r=get('https://rss.blog.naver.com/champion_chart.xml')
items=re.findall(r'<item>.*?<title>(.*?)</title>.*?<link>(.*?)</link>.*?<pubDate>(.*?)</pubDate>',r,re.S)
print(len(items))
for t,l,p in items:
    t=html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',t)); kw=re.split(r'[,|]',t)[0].strip()
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(kw)); time.sleep(2)
    ids=[]
    for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
        if b not in ids: ids.append(b)
    h2=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(t)); time.sleep(2)
    idx='O' if 'champion_chart' in h2 else 'X'
    rank=ids.index('champion_chart')+1 if 'champion_chart' in ids else 0
    print(p[5:16],'|',kw,'| 경쟁',len(ids),'| 내순위',rank,'| 제목검색 노출',idx,'|',t[:50],flush=True)

import urllib.request,urllib.parse,re,time,html,sys
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def rank(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
    out=[]
    for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
        if (b,n) not in out: out.append((b,n))
    ids=[]
    for b,n in out:
        if b not in ids: ids.append(b)
    return ids,h

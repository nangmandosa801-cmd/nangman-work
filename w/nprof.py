import re, urllib.request, pickle, datetime
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
D=pickle.load(open('nation.pkl','rb'))
allb=sorted({x for b,a in D.values() if b for x in b})
def feed(b):
    try:
        with urllib.request.urlopen(urllib.request.Request(
            'https://rss.blog.naver.com/%s.xml'%b, headers={'User-Agent':UA}),timeout=12) as r:
            x=r.read().decode('utf-8','ignore')
    except Exception: return None
    def f(tag,s=x):
        m=re.search(r'<%s>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>'%(tag,tag), s, re.S)
        return re.sub(r'\s+',' ',re.sub('<[^>]+>','',m.group(1))).strip() if m else ''
    items=re.findall(r'<item>(.*?)</item>', x, re.S)
    posts=[]
    for it in items:
        t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        posts.append(re.sub(r'\s+',' ',re.sub('<[^>]+>','',t.group(1))) if t else '')
    pub=re.findall(r'<pubDate>(.*?)</pubDate>', x)
    return {'blog':f('title'),'desc':f('description'),'n':len(items),
            'last':pub[0] if pub else '','posts':posts}
print('조회', len(allb), flush=True)
out={}
with ThreadPoolExecutor(16) as ex:
    for i,(b,v) in enumerate(zip(allb, ex.map(feed,allb))):
        out[b]=v
        if i%60==0: print(i,flush=True); pickle.dump(out,open('nprof.pkl','wb'))
pickle.dump(out,open('nprof.pkl','wb'))
print('끝',sum(1 for v in out.values() if v),flush=True)

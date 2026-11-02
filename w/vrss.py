import urllib.request,re,time,pickle,collections,html,email.utils,datetime
out=pickle.load(open('vend.pkl','rb'))
cnt=collections.Counter(b for v in out.values() for b in v)
reg=collections.defaultdict(list)
for r,v in out.items():
    for b in v: reg[b].append(r)
kw=re.compile(r'door|moon|mun|doornarae|joa|gold',re.I)
cands=[b for b in cnt if kw.search(b) or b in ('hanbyul_housing','jbdr','dbswkdrms89','dbswkdrms82','soo8349','3sgogo','bardamoon')]
res={}
for b in cands:
    try:
        x=urllib.request.urlopen(urllib.request.Request('https://rss.blog.naver.com/%s.xml'%b,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf-8','ignore')
    except Exception as e: print(b,'ERR'); continue
    t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>',x).group(1)
    desc=re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>',x,re.S).group(1)[:80]
    ds=[email.utils.parsedate_to_datetime(d) for d in re.findall(r'<pubDate>(.*?)</pubDate>',x)]
    titles=[html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',m)) for m in re.findall(r'<item>\s*<title>(.*?)</title>',x,re.S)]
    if ds:
        span=(ds[0]-ds[-1]).days+1; last=ds[0].date()
    else: span=0; last=None
    res[b]=dict(t=t,desc=desc,n=len(ds),span=span,last=last,regions=reg[b],titles=titles[:8])
    print(f"{b:18} {t[:22]:22} 지역{len(reg[b]):2} 글{len(ds):2}/{span:4}일 최근 {last} | {' / '.join(titles[:3])[:120]}",flush=True)
    time.sleep(0.6)
pickle.dump(res,open('vrss.pkl','wb'))

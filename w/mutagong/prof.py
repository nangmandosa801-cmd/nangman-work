import json,re,time,html,email.utils,urllib.request,datetime
hits=json.load(open('hits.json'))
c=sorted(hits.items(),key=lambda x:(-len(set(n for _,n in x[1])),-len(set(q for q,_ in x[1]))))
cands=[b for b,v in c if b!='champion_chart' and (len(set(n for _,n in v))>=2 or len(set(q for q,_ in v))>=4)]
res={}
for b in cands:
    try: x=urllib.request.urlopen(urllib.request.Request('https://rss.blog.naver.com/%s.xml'%b,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf-8','ignore')
    except Exception as e: print(b,'ERR',e); continue
    t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>',x); t=html.unescape(t.group(1)) if t else ''
    desc=re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>',x,re.S); desc=html.unescape(desc.group(1))[:90] if desc else ''
    ds=[email.utils.parsedate_to_datetime(d) for d in re.findall(r'<pubDate>(.*?)</pubDate>',x)]
    titles=[html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',m)) for m in re.findall(r'<item>\s*<title>(.*?)</title>',x,re.S)]
    now=datetime.datetime.now(datetime.timezone.utc)
    n30=sum(1 for d in ds if (now-d).days<=30)
    mu=[tt for tt in titles if '무타공' in tt]; jm=[tt for tt in titles if '중문' in tt]
    res[b]=dict(t=t,desc=desc,n=len(ds),n30=n30,last=str(ds[0].date()) if ds else None,mu=len(mu),jm=len(jm),titles=titles[:6],mut=mu[:4])
    print(f"{b:16} | {t[:24]} | {desc[:50]} | 30일 {n30} · 최근 {res[b]['last']} · RSS {len(ds)}편 가운데 중문 {len(jm)} 무타공 {len(mu)}\n      "+' / '.join((mu or titles)[:3])[:200],flush=True)
    time.sleep(0.5)
json.dump(res,open('prof.json','w'),ensure_ascii=False)

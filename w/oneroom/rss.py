import sys,re,json,time,datetime,html,subprocess
sys.path.insert(0,'/home/claude/blogkit'); import seo
hits=json.load(open('hits.json'))
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))[:45]
now=datetime.datetime(2026,10,10)
out=[]
for b,v in c:
    s=seo._get(f'https://rss.blog.naver.com/{b}.xml') or ''
    t=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S).group(1)) if '<title>' in s else ''
    desc=html.unescape(re.search(r'<description>(.*?)</description>',s,re.S).group(1))[:80] if '<description>' in s else ''
    items=re.findall(r'<item>.*?<title>(.*?)</title>.*?<pubDate>(.*?)</pubDate>',s,re.S)
    n30=0; titles=[]
    for ti,pd in items:
        try:
            d=datetime.datetime.strptime(pd.strip()[:25],'%a, %d %b %Y %H:%M:%S')
            if (now-d).days<=30: n30+=1
        except: pass
        titles.append(html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',ti)).strip())
    rr=sum(1 for x in titles if re.search(r'원룸|리모델링|올수리|도배|장판|시공|인테리어',x))
    out.append((b,t,desc,n30,len(items),rr,titles[:4]))
    print(b,'|',re.sub(r'<!\[CDATA\[|\]\]>','',t)[:30],'| 30일',n30,'| 시공글',rr,'/',len(items),'|',' / '.join(titles[:3])[:120],flush=True)
    time.sleep(0.6)
json.dump(out,open('rss.json','w'),ensure_ascii=False)

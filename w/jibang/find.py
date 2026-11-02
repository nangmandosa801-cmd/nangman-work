import re,json,urllib.parse,subprocess,html,collections
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"
def get(u): return subprocess.run(["curl","-s","-m","15","-A",UA,u],capture_output=True,text=True).stdout
R={"부산":["부산","해운대","명지","에코델타","기장"],"울산":["울산"],"창원/김해":["창원","김해","양산"],"대구/경북":["대구","포항","구미","경산"],"대전/세종":["대전","세종"],"천안/아산":["천안","아산","탕정"],"청주":["청주","오송"],"광주":["광주"],"전주":["전주","익산","군산"],"원주/강원":["원주","춘천","강릉"],"제주":["제주"]}
qs=[]
for reg,places in R.items():
  for p in places:
    for k in ["새집증후군","입주청소 새집증후군","베이크아웃"]:
      qs.append((reg,p+" "+k))
def serp(x):
  reg,q=x;h=get("https://m.search.naver.com/search.naver?where=m_blog&query="+urllib.parse.quote(q))
  return reg,q,set(re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/\d+',h))
ids=collections.defaultdict(set)
with ThreadPoolExecutor(8) as ex:
  for reg,q,s in ex.map(serp,qs):
    for i in s: ids[i].add(reg)
SKIP={'champion_chart','dong_jin_kim','jisandream01'}
def rss(i):
  x=get(f"https://rss.blog.naver.com/{i}.xml")
  items=re.findall(r'<item>(.*?)</item>',x,re.S)
  cl=lambda s:html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<!\[CDATA\[|\]\]>','',s or '')))
  ts=[cl((re.search(r'<title>(.*?)</title>',it,re.S) or [None,''])[1]) for it in items]
  ds=[cl((re.search(r'<description>(.*?)</description>',it,re.S) or [None,''])[1]) for it in items]
  dt=[(re.search(r'<pubDate>(.*?)</pubDate>',it) or [None,''])[1] for it in items]
  nm=cl((re.search(r'<channel>.*?<title>(.*?)</title>',x,re.S) or [None,''])[1])
  desc=cl((re.search(r'<channel>.*?<description>(.*?)</description>',x,re.S) or [None,''])[1])
  return i,nm,desc,ts,ds,dt
import email.utils,datetime
now=datetime.datetime(2026,10,23,tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
res=[]
with ThreadPoolExecutor(10) as ex:
  for i,nm,desc,ts,ds,dt in ex.map(rss,[i for i in ids if i not in SKIP]):
    if not ts: continue
    d30=0
    for d in dt:
      try:
        if (now-email.utils.parsedate_to_datetime(d)).days<=30: d30+=1
      except: pass
    allt=' '.join(ts+ds)
    sj=sum(1 for t,dd in zip(ts,ds) if re.search('새집증후군|베이크아웃',t+dd))
    clean=sum(1 for t in ts if re.search('입주청소|이사청소',t))
    plat=bool(re.search('청소를부탁해|머씨|한스클린|청소연구소|숨고|영구크린|크린토피아|가맹|지사|본사|전국|체험단|협찬|원고료',nm+desc+allt[:4000]))
    ph=sorted(set(re.findall(r'01[016789][-\s.]?\d{3,4}[-\s.]?\d{4}',nm+desc+allt)))
    res.append(dict(id=i,name=nm,desc=desc[:120],reg=sorted(ids[i]),n=len(ts),d30=d30,sj=sj,clean=clean,plat=plat,ph=ph[:2],last=dt[0][:16] if dt else '',t=ts[:4]))
json.dump(res,open('raw.json','w'),ensure_ascii=False)
ok=[r for r in res if r['d30']>=2 and r['sj']>=3 and r['clean']>=2 and not r['plat']]
ok.sort(key=lambda r:(r['reg'][0],-(r['sj']+r['clean'])))
print(len(ids),len(res),len(ok))
for r in ok: print(r['reg'],r['id'],'|',r['name'][:30],'| 30일',r['d30'],'| 새집',r['sj'],'청소',r['clean'],'/',r['n'],'|',r['ph'],'|',r['last'])

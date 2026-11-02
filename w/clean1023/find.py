import re,json,urllib.parse,subprocess,html,collections
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"
def get(u):
  return subprocess.run(["curl","-s","-m","15","-A",UA,u],capture_output=True,text=True).stdout
regs=["서울","강남","송파","노원","마포","은평","인천","검단","송도","청라","부천","고양","일산","파주","김포","수원","용인","성남","분당","하남","남양주","구리","의정부","양주","화성","동탄","평택","안산","시흥","광명","안양","광주 경기","오산","이천"]
qs=[r+" 입주청소" for r in regs]
def serp(q):
  h=get("https://m.search.naver.com/search.naver?where=m_blog&query="+urllib.parse.quote(q))
  return q,set(re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/\d+',h))
ids=collections.Counter();where=collections.defaultdict(set)
with ThreadPoolExecutor(8) as ex:
  for q,s in ex.map(serp,qs):
    for i in s: ids[i]+=1; where[i].add(q.split()[0])
SKIP={'champion_chart','dong_jin_kim','jisandream01'}
def rss(i):
  x=get(f"https://rss.blog.naver.com/{i}.xml")
  items=re.findall(r'<item>(.*?)</item>',x,re.S)
  ts=[html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',(re.search(r'<title>(.*?)</title>',it,re.S) or [None,''])[1])) for it in items]
  ds=[html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<!\[CDATA\[|\]\]>','',(re.search(r'<description>(.*?)</description>',it,re.S) or [None,''])[1]))) for it in items]
  dt=[(re.search(r'<pubDate>(.*?)</pubDate>',it) or [None,''])[1] for it in items]
  nm=html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','',(re.search(r'<channel>.*?<title>(.*?)</title>',x,re.S) or [None,''])[1]))
  return i,nm,ts,ds,dt
res=[]
with ThreadPoolExecutor(10) as ex:
  for i,nm,ts,ds,dt in ex.map(rss,[i for i in ids if i not in SKIP]):
    if not ts: continue
    allt=' '.join(ts+ds)
    clean=sum(1 for t in ts if re.search('입주청소|이사청소|입주 청소|이사 청소',t))
    sj=len(re.findall('새집증후군|베이크아웃',allt))
    other=len(re.findall('줄눈|탄성|나노코팅|방충망|에어컨',allt))
    ph=sorted(set(re.findall(r'01[016789][-\s.]?\d{3,4}[-\s.]?\d{4}',allt)))
    plat=re.search('청소를부탁해|머씨|한스클린|청소연구소|미소|숨고|영구크린|크린토피아|가맹|지사|본사|전국',nm+allt[:3000])
    res.append(dict(id=i,name=nm,n=len(ts),clean=clean,sj=sj,other=other,ph=ph,reg=sorted(where[i]),hit=ids[i],last=dt[0][:16] if dt else '',plat=bool(plat),t=ts[:3]))
json.dump(res,open('find.json','w'),ensure_ascii=False)
ok=[r for r in res if r['clean']>=max(5,r['n']*0.4) and r['sj']==0 and not r['plat']]
ok.sort(key=lambda r:(-r['clean'],-r['hit']))
print(len(ids),len(res),len(ok))
for r in ok[:40]: print(r['id'],'|',r['name'],'|',r['clean'],'/',r['n'],'| 다른공정',r['other'],'|',r['ph'][:2],'|',','.join(r['reg'][:5]),'|',r['last'])

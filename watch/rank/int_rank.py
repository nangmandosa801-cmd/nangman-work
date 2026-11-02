# 10/16 사용자 「올린다고 다가 아냐 · 1번부터」 — 낭만 인테리어 발행 글이 네이버 블로그 탭에서 몇 위에 뜨는지
import sys,re,json,urllib.parse,time,datetime
sys.path.insert(0,'/home/claude/blogkit'); import seo
t=open('/tmp/claude-0/pl.txt').read()
rows=[]
for m in re.finditer(r'\{[^{}]*?"logNo":"(\d+)"[^{}]*?"title":"(.*?)"[^{}]*?"addDate":"(.*?)"',t):
    rows.append(dict(logNo=m.group(1),title=urllib.parse.unquote_plus(m.group(2)),date=urllib.parse.unquote_plus(m.group(3))))
if not rows:
    for m in re.finditer(r'"logNo":"(\d+)".*?"title":"(.*?)".*?"addDate":"(.*?)"',t):
        rows.append(dict(logNo=m.group(1),title=urllib.parse.unquote_plus(m.group(2)),date=urllib.parse.unquote_plus(m.group(3))))
print(len(rows),file=sys.stderr)
out=[]
for r in rows:
    q=r['title'].split(',')[0].strip()
    s=seo._get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q))
    us=[]
    for u in re.findall(r'https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if u not in us: us.append(u)
    pos=next((i for i,u in enumerate(us,1) if u==('champion_chart',r['logNo'])),None)
    other=[i for i,u in enumerate(us,1) if u[0]=='champion_chart' and u[1]!=r['logNo']]
    out.append(dict(r,q=q,pos=pos,other=other[:3],seen=len(us)))
    print(pos,q,file=sys.stderr); time.sleep(1.2)
json.dump(dict(day=str(datetime.date.today()),rows=out),open('/home/claude/watch/rank/int_rank_1016.json','w'),ensure_ascii=False,indent=1)

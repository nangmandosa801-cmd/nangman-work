import sys,re,json,urllib.parse,time,datetime
sys.path.insert(0,'/home/claude/blogkit'); import seo
rows=[];seen=set()
for p in range(1,12):
    t=seo._get(f'https://blog.naver.com/PostTitleListAsync.naver?blogId=champion_chart&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30','https://blog.naver.com/champion_chart')
    n=0
    for m in re.finditer(r'"logNo":"(\d+)".*?"title":"(.*?)".*?"addDate":"(.*?)"',t):
        if m.group(1) in seen: continue
        seen.add(m.group(1));n+=1
        rows.append(dict(logNo=m.group(1),title=urllib.parse.unquote_plus(m.group(2)),date=urllib.parse.unquote_plus(m.group(3))))
    if n==0: break
    time.sleep(0.8)
print('posts',len(rows),flush=True)
def ours(q):
    s=seo._get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q))
    us=[]
    for u in re.findall(r'https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if u not in us: us.append(u)
    return us
out=[]
for i,r in enumerate(rows):
    q=r['title'].split(',')[0].strip()
    us=ours(q); time.sleep(1.2)
    pos=next((k for k,u in enumerate(us,1) if u==('champion_chart',r['logNo'])),None)
    idx=None
    if pos is None:
        us2=ours(r['title']); time.sleep(1.2)
        idx=('champion_chart',r['logNo']) in us2
    out.append(dict(r,q=q,pos=pos,indexed=(True if pos else idx)))
    if i%20==0: print(i,flush=True)
json.dump(dict(day=str(datetime.date.today()),rows=out),open('/home/claude/watch/rank/r1031/int_rank_1031.json','w'),ensure_ascii=False,indent=1)
print('done')

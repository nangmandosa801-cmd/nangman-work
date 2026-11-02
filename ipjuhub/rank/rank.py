import sys,re,json,urllib.parse,time,datetime,pickle
sys.path.insert(0,'/home/claude/blogkit'); import seo
a,_=pickle.load(open('/home/claude/ipjuhub/data.pkl','rb'))
def ours(q):
    s=seo._get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q))
    us=[]
    for u in re.findall(r'https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if u not in us: us.append(u)
    return us
out={}
for r in a:
    for p in r['_p']:
        m=re.search(r'blog\.naver\.com/([A-Za-z0-9_]+)/(\d+)',p['u'])
        if not m or p['u'] in out: continue
        q=p['t'].split(',')[0].strip()
        us=ours(q); time.sleep(1.2)
        pos=next((k for k,u in enumerate(us,1) if u==(m.group(1),m.group(2))),None)
        out[p['u']]=dict(단지=r['단지'],b=p['b'],t=p['t'],q=q,pos=pos,n=len(us))
json.dump(dict(day=str(datetime.date.today()),rows=out),open('/home/claude/ipjuhub/rank/rank.json','w'),ensure_ascii=False,indent=1)
print('done',len(out),sum(1 for v in out.values() if v['pos']))

import subprocess,re,urllib.parse,pickle,time
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
MINE={'dong_jin_kim','jisandream01','give_me_travel'}
def fetch(args):
    q,where=args
    u=f'https://m.search.naver.com/search.naver?where={where}&query='+urllib.parse.quote(q)
    try:
        h=subprocess.run(['curl','-s','-A',UA,'--max-time','15',u],capture_output=True).stdout.decode('utf-8','replace')
    except Exception: return (q,where,None,None)
    ids=[]
    for b,p in re.findall(r'blog\.naver\.com/([A-Za-z0-9_]+)/(\d+)',h):
        if (b,p) not in ids: ids.append((b,p))
    pos=[i+1 for i,(b,p) in enumerate(ids) if b in MINE]
    return (q,where,len(ids),pos[0] if pos else None)
res=pickle.load(open('/home/claude/w/ac.pkl','rb'))
has=[k for b,k,n,s in res if n>0]
jobs=[(k,'m_blog') for k in has]+[(k,'m') for k in has]
with ThreadPoolExecutor(max_workers=6) as ex:
    out=list(ex.map(fetch,jobs))
d={}
for q,w,n,p in out: d.setdefault(q,{})[w]=(n,p)
print(f'{"키워드":28s} {"블로그탭":>10s} {"통합검색":>10s}')
top=mid=none=0; utop=unone=0
for k in has:
    b=d[k].get('m_blog',(None,None)); m=d[k].get('m',(None,None))
    bs = f'{b[1]}위/{b[0]}' if b[1] else f'없음/{b[0]}'
    ms = f'{m[1]}위/{m[0]}' if m[1] else f'없음/{m[0]}'
    print(f'{k:28s} {bs:>10s} {ms:>10s}')
    if b[1] and b[1]<=5: top+=1
    elif b[1]: mid+=1
    else: none+=1
    if m[1] and m[1]<=5: utop+=1
    elif not m[1]: unone+=1
print()
print(f'수요 있는 키워드 {len(has)}개 중')
print(f'  블로그탭 5위 이내 {top} / 6위이하 {mid} / 없음 {none}')
print(f'  통합검색 5위 이내 {utop} / 아예 없음 {unone}')

import csv,io,re,subprocess,urllib.parse,json,time,pickle,sys
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
def ac(q):
    u='https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
    try:
        o=subprocess.run(['curl','-s','-A',UA,'--max-time','10',u],capture_output=True).stdout.decode('utf-8','replace')
        return q,[i[0] for i in json.loads(o).get('items',[[]])[0]]
    except Exception:
        return q,None
rows=list(csv.DictReader(io.open('/home/claude/w/SEO목록_전체.csv',encoding='utf-8-sig')))
pub=[r for r in rows if r['상태']=='발행' and r['블로그'] in ('낭만','지산')]
def head(t): return re.split(r'[|,]',t)[0].strip()
ks=[]; seen=set()
for r in pub:
    k=head(r['제목'])
    if k not in seen: seen.add(k); ks.append((r['블로그'],k))
with ThreadPoolExecutor(max_workers=8) as ex:
    out=dict(ex.map(ac,[k for _,k in ks]))
res=[(b,k,(len(out[k]) if out[k] is not None else -1),(out[k] or [])[:3]) for b,k in ks]
pickle.dump(res,open('/home/claude/w/ac.pkl','wb'))
print('검사',len(res))

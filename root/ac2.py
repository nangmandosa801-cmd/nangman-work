import csv,io,re,subprocess,urllib.parse,json,pickle
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
def ac(q):
    u='https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
    try:
        o=subprocess.run(['curl','-s','-A',UA,'--max-time','10',u],capture_output=True).stdout.decode('utf-8','replace')
        return q,[i[0] for i in json.loads(o).get('items',[[]])[0]]
    except Exception: return q,None
rows=list(csv.DictReader(io.open('/home/claude/w/SEO목록_전체.csv',encoding='utf-8-sig')))
tgt=[r for r in rows if r['상태'] in ('미발행','예약')]
def head(t): return re.split(r'[|,]',t)[0].strip()
cands=set()
info=[]
for r in tgt:
    h=head(r['제목']); ws=h.split()
    vs=[' '.join(ws[:i]) for i in range(len(ws),0,-1)]
    vs=[v for v in vs if len(v)>=2][:5]
    info.append((r,h,vs)); cands.update(vs)
cands=sorted(cands)
with ThreadPoolExecutor(max_workers=10) as ex:
    out=dict(ex.map(ac,cands))
pickle.dump((info,out),open('/home/claude/w/ac2.pkl','wb'))
print('제목',len(info),'후보어',len(cands))

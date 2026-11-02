import json,re,subprocess,urllib.parse,pickle
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
def ac(q):
    u='https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
    try:
        o=subprocess.run(['curl','-s','-A',UA,'--max-time','10',u],capture_output=True).stdout.decode('utf-8','replace')
        return q,[i[0] for i in json.loads(o).get('items',[[]])[0]]
    except Exception: return q,None
M=json.load(open('/home/claude/w/newtitles.json'))
heads=sorted({re.split(r'[|,]',v)[0].strip() for v in M.values()})
with ThreadPoolExecutor(max_workers=10) as ex: out=dict(ex.map(ac,heads))
pickle.dump(out,open('/home/claude/w/verif.pkl','wb'))
bad=[h for h in heads if not out.get(h)]
print('새 앞머리',len(heads),'개 검증 / 자동완성 0개:',len(bad))
for h in bad: print('  X',h)

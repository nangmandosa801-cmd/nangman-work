import json,subprocess,urllib.parse,sys,os,time
from concurrent.futures import ThreadPoolExecutor
CACHE='ac_cache.json'; C=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def ac(q):
    if q in C: return C[q]
    u='https://ac.search.naver.com/nx/ac?'+urllib.parse.urlencode(dict(q=q,con=1,frm='nv',ans=2,r_format='json',r_enc='UTF-8',r_unicode=0,t_koreng=1,run=2,rev=4,q_enc='UTF-8',st=100))
    for _ in range(3):
        r=subprocess.run(['curl','-s','-m','10',u,'-A','Mozilla/5.0'],capture_output=True,text=True).stdout
        try: v=[i[0] for i in json.loads(r)['items'][0]]; C[q]=v; return v
        except Exception: time.sleep(1)
    C[q]=None; return None
def many(qs,n=8):
    with ThreadPoolExecutor(n) as ex: res=list(ex.map(ac,qs))
    json.dump(C,open(CACHE,'w'),ensure_ascii=False); return dict(zip(qs,res))

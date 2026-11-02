import json,re,os,requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('helper_old_data.json'))
jobs=[]
for x in d:
    if x['day']!='1일차': continue
    n=x['logNo']; os.makedirs(f'img/{n}',exist_ok=True)
    s=BeautifulSoup(open(f'src/{n}.html').read(),'html.parser'); c=s.select_one('.se-main-container')
    for i,im in enumerate(c.select('img')):
        u=im.get('data-lazy-src') or im.get('src'); u=re.sub(r'\?type=.*','',u)
        jobs.append((n,i,u))
def f(j):
    n,i,u=j; p=f'img/{n}/{i:02d}.png'
    if os.path.exists(p) and os.path.getsize(p)>500: return j,200
    r=requests.get(u,headers={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'},timeout=40)
    open(p,'wb').write(r.content); return j,r.status_code
with ThreadPoolExecutor(8) as ex: res=list(ex.map(f,jobs))
print(len(res),[ (j[0],j[1],s) for j,s in res if s!=200])

import json,re,subprocess,concurrent.futures as cf
from scan import NAMES,OUR,get
P=[p for p in json.load(open('posts.json')) if p['b'] in ('낭만 인테리어','낭만 부동산 분석 플랫폼')]
def chk(p):
    u=p['u'].replace('blog.naver.com','m.blog.naver.com')
    h=get(u)
    m=re.search(r'se-main-container(.*)',h,re.S);body=m.group(1) if m else ''
    body=body.split('post_footer')[0]
    links=sorted(set(x for x in re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)',body) if not re.match(OUR,x)))
    names=sorted(set(n for n in NAMES if n in body))
    return p['u'],p['t'][:30],links,names,len(body)
with cf.ThreadPoolExecutor(8) as ex: R=list(ex.map(chk,P))
bad=[r for r in R if r[2] or r[3]]
print('checked',len(R),'empty',sum(1 for r in R if r[4]<500),'flagged',len(bad))
for r in bad: print(r[0].split('/')[-2][:6],r[0].split('/')[-1],'|',r[1],'|',r[2][:4],'|',r[3][:5])
json.dump(bad,open('scan_naver.json','w'),ensure_ascii=False)

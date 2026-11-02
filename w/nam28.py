# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, time, pickle, os, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
live=pickle.load(open('nam_live.pkl','rb')); A=pickle.load(open('nam_ac.pkl','rb'))
C=pickle.load(open('nam28.pkl','rb')) if os.path.exists('nam28.pkl') else {}
def ba(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for _ in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=15) as x:
                h=x.read().decode('utf-8','ignore')
            b=[]
            for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
                if m.group(1) not in b: b.append(m.group(1))
            return len(b), len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
        except Exception: time.sleep(4)
    return -1,-1
for i,q in enumerate(live):
    if q in C and C[q][0]>=0: continue
    C[q]=ba(q); pickle.dump(C,open('nam28.pkl','wb'))
    print('%2d/%d %-22s %3d %3d' % (i+1,len(live),q,C[q][0],C[q][1])); sys.stdout.flush()
    time.sleep(2.3)
rows=[]
for q in live:
    b,ad=C.get(q,(-1,-1))
    if b<0: continue
    a=len(A[q]); rows.append((round(ad*2+a*1.5-b*0.8,1),q,a,b,ad))
rows.sort(reverse=True)
print('\n%5s %-22s %4s %4s %4s' % ('점수','앞머리','제안','블로그','광고'))
for s,q,a,b,ad in rows: print('%5.1f %-22s %4d %4d %4d' % (s,q,a,b,ad))
pickle.dump(rows,open('nam28_rows.pkl','wb'))

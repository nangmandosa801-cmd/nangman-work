# -*- coding: utf-8 -*-
import pickle, re, time, os, json, urllib.request, urllib.parse
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='dosarev.pkl'; C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def sv(): pickle.dump(C,open(CF,'wb'))
def ac(q):
    k=('a',q)
    if k in C: return C[k]
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    for _ in range(3):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf-8','ignore'))
            C[k]=len(j.get('items',[[]])[0]); sv(); return C[k]
        except Exception: time.sleep(3)
    C[k]=-1; sv(); return -1
def blog(q):
    k=('b',q)
    if k in C: return C[k]
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for _ in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
            ids=[]
            for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
                if b not in ids: ids.append(b)
            ads=len(set(re.findall(r'ader\.naver\.com/v1/\w{20}',h)))
            pos=ids.index('give_me_travel')+1 if 'give_me_travel' in ids else 0
            C[k]=(len(ids),ads,pos); sv(); return C[k]
        except Exception: time.sleep(4)
    C[k]=(-1,-1,0); sv(); return C[k]

t,l=pickle.load(open('dosa_rss.pkl','rb'))
t=t[1:]
def head(x):
    m=re.split(r'\s*[,|—:?·]\s*', x, 1)[0]
    return m.strip()[:22]
rows=[]
for x in t:
    h=head(x)
    a=ac(h); time.sleep(0.9)
    b,ad,pos=blog(h); time.sleep(2.5)
    rows.append((h,a,b,ad,pos,x))
pickle.dump(rows,open('dosarev_rows.pkl','wb'))
print('%-22s %4s %4s %4s %5s' % ('앞머리','제안','경쟁','광고','내순위'))
for h,a,b,ad,pos,x in rows:
    print('%-22s %4d %4d %4d %5s' % (h,a,b,ad, pos if pos else '-'))

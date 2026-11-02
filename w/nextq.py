# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, time, pickle, os, json
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='nextq.pkl'; C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def _sv(): pickle.dump(C,open(CF,'wb'))
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
            C[k]=(len(ids),len(set(re.findall(r'ader\.naver\.com/v1/\w{20}',h)))); _sv(); return C[k]
        except Exception: time.sleep(4)
    C[k]=(-1,-1); _sv(); return C[k]
def ac(q):
    k=('a',q)
    if k in C: return C[k]
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    for _ in range(3):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf-8','ignore'))
            C[k]=len(j.get('items',[[]])[0]); _sv(); return C[k]
        except Exception: time.sleep(3)
    C[k]=-1; _sv(); return C[k]

ROWS=[('중문 교체','replace'),('중문 사이즈','size'),('현관 풍수','pungsu'),
 ('LX하우시스 샷시','sash_brand'),('샷시 등급','sash_grade'),('3연동 중문','3yeondong'),
 ('스윙 중문','swing'),('자동 중문','auto'),('무타공 중문','mutagong'),
 ('중문 브랜드','brand'),('중문 색상','color'),('중문 손잡이','handle'),
 ('중문 설치 비용','cost'),('베란다 중문','veranda'),('현관 조명','light'),
 ('중문 잠금장치','lock')]
out=[]
for q,slug in ROWS:
    a=ac(q); time.sleep(1.2)
    b,ad=blog(q); time.sleep(2.7)
    out.append((q,slug,a,b,ad, ad*2 + a*1.5 - b*0.8))
out.sort(key=lambda r:-r[5])
print('%-16s %5s %5s %5s %7s' % ('앞머리','제안','경쟁','광고','점수'))
for q,s,a,b,ad,sc in out:
    print('%-16s %5d %5d %5d %7.1f' % (q,a,b,ad,sc))
pickle.dump(out,open('nextq_rank.pkl','wb'))

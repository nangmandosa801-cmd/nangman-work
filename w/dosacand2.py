# -*- coding: utf-8 -*-
import pickle, re, time, os, json, urllib.request, urllib.parse
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='dosarev.pkl'; C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def sv(): pickle.dump(C,open(CF,'wb'))
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
Q=['상관 사주','투자 사주','부동산 운','이직운','직장운','삼형살','신왕재왕','재물복','부자 사주',
   '겁재','비견 겁재','건록격','연예인 사주','사주 공망','공망','신금 일간','12운성','손 없는 날',
   '결혼 날짜','이사 날짜','관인상생','시험운','상관격','월지','편재','식신','식신격','공망 사주',
   '공망 뜻','진술축미','무토','오행']
ac=pickle.load(open('dosacand.pkl','rb'))
out=[]
for q in Q:
    b,ad,pos=blog(q); time.sleep(2.6)
    out.append((q,ac.get(q,0),b,ad,pos))
    print('%-12s 제안%3s 경쟁%3d 광고%3d 순위%3s'%(q,ac.get(q,'?'),b,ad,pos if pos else '-'))
pickle.dump(out,open('dosacand2.pkl','wb'))

# -*- coding: utf-8 -*-
import pickle, re, time, os, json, urllib.request, urllib.parse
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='grade.pkl'; C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def sv(): pickle.dump(C,open(CF,'wb'))
def ac(q):
    k=('a',q)
    if k in C: return C[k]
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    for _ in range(3):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf-8','ignore'))
            C[k]=[i[0] for i in j.get('items',[[]])[0]]; sv(); return C[k]
        except Exception: time.sleep(3)
    C[k]=[]; sv(); return []
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

G={1:['무토','사주 궁합','삼재','재물운 사주','도화살','사주 무료','연애운','공망','사주팔자','직업운 사주','정관','백호살'],
   2:['토정비결','사주 보는 법','십신','편관','역마살','신년운세','정재','사주 강약','편인','궁합 보는 법','만세력'],
   3:['용신','원진살','대운','갑목','일주 특징','결혼 시기 사주','비견','겁재'],
   9:['괴강살','오행','일간','병화','정인','식신','세운','상관','편재','임수','을목']}
SAJU=('사주','일간','일주','운세','궁합','명리','팔자','대운','세운','오행','천간','지지','신살','만세력',
      '토정','도화','역마','백호','괴강','원진','공망','삼재','재물운','연애운','직업운','용신','십신',
      '정관','편관','정인','편인','식신','상관','정재','편재','비견','겁재','무토','기토','갑목','을목',
      '병화','정화','경금','신금','임수','계수','격','운','살','띠','재성','관성','인성','식상','합')
def issaju(s):
    return any(w in s for w in SAJU)
rows=[]
for g,ks in G.items():
    for q in ks:
        it=ac(q); time.sleep(0.8)
        b,ad,p=blog(q); time.sleep(2.6)
        n=len(it); cl=sum(1 for x in it if issaju(x))
        rows.append((g,q,n,cl,b,ad,p,it))
        print('%d %-10s 제안%3d(사주%2d) 경쟁%3d 광고%3d 순위%3s | %s'%(g,q,n,cl,b,ad,p if p else '-',' / '.join(it[:6])))
pickle.dump(rows,open('grade_rows.pkl','wb'))

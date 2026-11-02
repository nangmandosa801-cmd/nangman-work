# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, json, time, pickle, os, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
C=pickle.load(open('dosa40.pkl','rb')) if os.path.exists('dosa40.pkl') else {}
def ac(q):
    try:
        with urllib.request.urlopen(urllib.request.Request(AC%urllib.parse.quote(q),headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        return [i[0] for i in d.get('items',[[]])[0]]
    except Exception: return None
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
Q=['사주 보는 법','사주팔자','일간','십신','오행','용신','대운','세운','만세력',
   '사주 궁합','궁합 보는 법','결혼 시기 사주','연애운','재물운 사주','직업운 사주',
   '삼재','신년운세','토정비결','도화살','역마살','백호살','괴강살','원진살','공망',
   '비견','겁재','식신','상관','편재','정재','편관','정관','편인','정인',
   '갑목','을목','병화','무토','임수','일주 특징','사주 무료','사주 강약']
for i,q in enumerate(Q):
    if q in C and C[q][1]>=0: continue
    a=ac(q); b,ad=ba(q); C[q]=(len(a) if a else 0, b, ad)
    pickle.dump(C,open('dosa40.pkl','wb'))
    print('%3d/%d %-12s %2d %3d %3d' % (i+1,len(Q),q,C[q][0],b,ad)); sys.stdout.flush()
    time.sleep(2.3)
print('완료')

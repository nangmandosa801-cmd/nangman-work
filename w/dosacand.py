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

CAND={
'경매 사주':['재물운 사주','상관 사주','투자 사주','돈 버는 사주','경매 운'],
'부동산 사는 시기':['집 사는 시기','부동산 운','이사 시기','매수 타이밍','재물운 시기'],
'직장이 자꾸 바뀌는 사주':['이직 사주','직장운','삼형살','직업운 사주','이직운'],
'사주 건강 신호 6가지':['건강 사주','사주 건강운','오행 건강','몸 약한 사주'],
'부자 사주 첫 번째 구조':['부자 사주','신왕재왕','재물복','돈 많은 사주','부자 되는 사주'],
'월주 겁재':['겁재','겁재 뜻','월주','비견 겁재','겁재 많은 사주'],
'임영웅 사주 풀이':['임영웅 사주','건록격','극신강','연예인 사주'],
'2026년 9월 개업':['개업 좋은 날','개업 날짜','오픈 좋은 날','개업 길일','사업자등록 좋은 날'],
'사주 공망이 정관에':['공망','공망 뜻','정관','공망 계산','사주 공망'],
'신금의 12운성':['12운성','신금','신금 일간','십이운성','신금 사주'],
'2026년 9월 결혼':['결혼 좋은 날','손 없는 날','이사 좋은 날','결혼 날짜','이사 날짜'],
'형(刑)과 관인':['관인상생','시험운','삼형','공부 잘하는 사주','시험운 사주'],
'상관이 사회에서는':['상관','상관 뜻','상관격','상관 사주','식상'],
'재성 월지':['재성','재성 뜻','월지','편재','정재','재성 많은 사주'],
'식신은 밥그릇입니다':['식신','식신 뜻','식신격','식신 사주'],
'빈 과일이 소리가 크다':['공망 뜻','공망 계산','공망 사주','천을귀인'],
'공망은 손이 한 번 더':['공망','공망 뜻','사주 공망','공망 보는 법'],
'없다던 오행이 사실은':['오행','오행 보는 법','진술축미','오행 없는 사주','무토'],
}
seen={}
for k,v in CAND.items():
    print('■',k)
    for q in v:
        if q in seen: n=seen[q]
        else:
            n=ac(q); seen[q]=n; time.sleep(0.8)
        print('   %-16s %3d' % (q,n))
pickle.dump(seen,open('dosacand.pkl','wb'))

# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, json, time, pickle, os, csv, io, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
A=pickle.load(open('dosa_ac.pkl','rb')) if os.path.exists('dosa_ac.pkl') else {}
def ac(q):
    if q in A: return A[q]
    try:
        with urllib.request.urlopen(urllib.request.Request(AC%urllib.parse.quote(q),headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        r=[i[0] for i in d.get('items',[[]])[0]]
    except Exception: r=[]
    A[q]=r; time.sleep(0.35); return r
rows=list(csv.DictReader(io.open('/mnt/user-data/outputs/SEO목록_전체.csv',encoding='utf-8-sig')))
D=[r for r in rows if (r.get('블로그')or'')=='도사']
def head(t):
    t=(t or '').strip()
    for sep in ['—','–','-','|',',']:
        if sep in t: return t.split(sep,1)[0].strip()
    return ' '.join(t.split()[:2])
ALT={
 '격각(隔角)':['격각살','격각','사주 격각'],
 '낭만도사 사주 판독기':['사주 무료','사주 보는 법'],
 '낭만도사 소개 ›':['사주 블로그'],
 '돈 글자가 하나도 없는데 그래미를 다섯 개':['재성 없는 사주','무재사주'],
 '배우자복 없는 사주':['배우자복','배우자운','배우자복 없는 사주'],
 '부동산 사주':['부동산 사주','재물운 사주'],
 '부모와 자식의 띠':['띠 궁합','부모 자식 띠','띠별 궁합'],
 '사주 건강 신호 6가지':['사주 건강','건강 사주'],
 '사주로 보는 건강 시기':['사주 건강','조후'],
 '식상생재':['식상생재','식신생재'],
 '십이운성 목욕':['십이운성','목욕 십이운성'],
 '재성 인성 균형':['재성','인성 사주','재다신약'],
 '조용필 사주':['조용필 사주','연예인 사주'],
 '직업 해석기':['직업운 사주','사주 직업'],
 '해공':['공망','공망 푸는 법'],
 '화 많은 사주':['화 많은 사주','화기 많은 사주','사주 화'],
 '송강 사주 여덟 글자에 불이 하나도 없는데':['송강 사주','연예인 사주'],
 '송강 사주 풀이 인성도 식상도 0인데 배우가 된 구조':['송강 사주','무인성'],
 '오행 상극 가위바위보는 셋':['오행 상극','오행'],
 '오행 상생 왜 하필 나무 다음이 불일까':['오행 상생','오행'],
 '일간 뜻 사주 여덟 글자 중 「나」는 딱 한 글자입니다':['일간','일간 뜻'],
 '전현무 사주 조선일보 1주일':['전현무 사주','연예인 사주'],
 '지장간 뜻 여덟 글자만 세면 절반을 놓칩니다':['지장간','지장간 뜻'],
}
out=[]
for r in D:
    t=(r.get('제목') or ''); h=head(t); cur=len(ac(h))
    best=('',0)
    for c in ALT.get(t.split('—')[0].strip(), ALT.get(h,[])) or []:
        n=len(ac(c))
        if n>best[1]: best=(c,n)
    out.append((r.get('상태'),t,h,cur,best[0],best[1]))
pickle.dump(A,open('dosa_ac.pkl','wb'))
w=io.open('/mnt/user-data/outputs/낭만도사_앞머리점검.csv','w',encoding='utf-8-sig',newline='')
cw=csv.writer(w); cw.writerow(['상태','제목','현재 앞머리','현재 제안어','바꿀 앞머리','대체 제안어','판정'])
print('%-6s %-30s %3s  %-14s %3s' % ('상태','현재 앞머리','제안','대체','제안'))
for s,t,h,cur,c,n in out:
    v='유지' if cur>0 else ('교체' if n>0 else '검토')
    cw.writerow([s,t,h,cur,c,n,v])
    print('%-6s %-30s %3d  %-14s %3d  %s' % (s,h[:30],cur,c[:14],n,v))
w.close()

# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, json, time, pickle, os, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
C=pickle.load(open('jm40.pkl','rb')) if os.path.exists('jm40.pkl') else {}
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
Q=['중문 시공','중문 교체','원슬라이딩 중문','거실 중문','2연동 중문','간살 중문','안방 중문',
   '포켓도어','폴딩 중문','프렌치 중문','중문 as','중문 셀프시공','중문 방음','중문 단열',
   '중문 결로','중문 수리','중문 수리 비용','중문 철거','중문 유리 종류','중문 방충망',
   '중문 레일','중문 하부레일','중문 없는 집','중문 후회','중문 단점','중문 필요성',
   '모루유리 중문','아쿠아유리 중문','중문 인테리어','중문 리모델링','전세 중문','원룸 중문',
   '중문 문턱','중문 추천','중문 설치 비용','중문 가격 비교','중문 시공비','중문 종류별 가격',
   '중문 도어락','중문 유리 교체']
for i,q in enumerate(Q):
    if q in C and C[q][1]>=0: continue
    a=ac(q); b,ad=ba(q); C[q]=(len(a) if a else 0, b, ad)
    pickle.dump(C,open('jm40.pkl','wb'))
    print('%3d/%d %-16s %2d %3d %3d' % (i+1,len(Q),q,C[q][0],b,ad)); sys.stdout.flush()
    time.sleep(2.4)
print('완료 %d/%d' % (sum(1 for q in Q if q in C and C[q][1]>=0), len(Q)))

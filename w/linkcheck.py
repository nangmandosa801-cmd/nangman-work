# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, time, pickle, os, json
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='linkcheck.pkl'
C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def get(q,tries=3):
    if q in C: return C[q]
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for k in range(tries):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
            ids=[]
            for bid,no in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
                if bid not in ids: ids.append(bid)
            ads=len(set(re.findall(r'ader\.naver\.com/v1/\w{20}',h)))
            C[q]=(ids,ads); pickle.dump(C,open(CF,'wb')); return C[q]
        except Exception as e:
            time.sleep(4)
    C[q]=([],-1); pickle.dump(C,open(CF,'wb')); return C[q]

QS=['하남 구도심 아파트','동탄 산척동 아파트','1기 신도시 재건축','은마아파트 재건축',
    '대치동 전세','미사 아파트 시세','하남 감일지구 아파트 시세','교산신도시 분양권',
    '하남 오피스텔 시세','하남 아파트 시세','위례 아파트 시세','동탄 아파트 시세',
    '경기도 아파트 시세 지도','하남 지하철 노선도','하남 미사 아파트 시세 비교',
    '동탄역 아파트 시세','창동 아파트 시세','망월동 아파트 시세']
print('%-24s %5s %5s %s' % ('검색어','경쟁','광고','내 순위'))
for q in QS:
    ids,ads=get(q)
    pos=ids.index('dong_jin_kim')+1 if 'dong_jin_kim' in ids else 0
    print('%-24s %5d %5d %s' % (q,len(ids),ads,pos if pos else '-'))
    time.sleep(2.7)

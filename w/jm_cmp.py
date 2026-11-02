import re, urllib.parse, urllib.request, pickle, json, os
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def blogads(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=14) as x:
            h=x.read().decode('utf-8','ignore')
    except Exception: return q,-1
    return q,len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
Q=['중문','중문 설치','중문 가격','중문 종류','3연동 중문','스윙 중문','자동 중문','중문 시공',
   '중문 브랜드','무타공 중문','중문 색상','중문 손잡이','거실 중문','중문 방충망','원슬라이딩 중문',
   '중문 견적','중문 수리','현관 중문']
with ThreadPoolExecutor(6) as ex: R=list(ex.map(blogads,Q))
for q,a in sorted(R,key=lambda r:-r[1]): print('%-18s %3d' % (q,a))
import statistics
v=[a for q,a in R if a>=0]
print('중문 평균 %.1f  합 %d  n=%d' % (statistics.mean(v), sum(v), len(v)))
S=pickle.load(open('sash.pkl','rb'))
sv=[ad for q,a,b,ad in S if ad>=0 and q not in ('창','새시','샤시','창호')]
print('샷시 평균 %.1f  합 %d  n=%d' % (statistics.mean(sv), sum(sv), len(sv)))

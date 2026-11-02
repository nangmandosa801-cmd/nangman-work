import re, urllib.parse, urllib.request, pickle
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
UA2='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
def ranks(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=12) as r:
            h=r.read().decode('utf-8','ignore')
    except Exception: return {}
    out={}
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in out: out[m.group(1)]=len(out)+1
    return out
AUTO=['자동 중문','자동중문 설치','현관 자동문','남양주 자동문','구리 자동문','별내 자동문',
      '다산 자동문','자동 중문 고장','아파트 자동문 설치','자동중문 가격']
REP=['중문수리','남양주 중문수리','구리 중문수리','별내 중문수리','다산 중문수리',
     '중문 as','중문 고장','3연동 중문 수리','중문 와이어 교체','중문 호차 교체']
def scan(QS,label):
    with ThreadPoolExecutor(5) as ex: R=dict(zip(QS, ex.map(ranks,QS)))
    agg={}
    for q,d in R.items():
        for b,r in d.items():
            agg.setdefault(b,{'q':{},'n':0})
            agg[b]['q'][q]=r; agg[b]['n']+=1
    return R, agg
RA,AA=scan(AUTO,'auto'); RR,AR=scan(REP,'rep')
pickle.dump((RA,AA,RR,AR),open('find2.pkl','wb'))
print('자동 후보 %d / 수리 후보 %d' % (len(AA),len(AR)))

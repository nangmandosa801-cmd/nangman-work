# 도배 · 장판 업체 후보 찾기 (2026.10.8 10:45 · 사용자 「도배 장판 업체 추가는 어때?」) — tk_run.py와 같은 방법
import re, urllib.parse, urllib.request, pickle, time, html, datetime, email.utils, json
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def get(u,ua=UA,t=6):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=t) as r: return r.read().decode('utf-8','ignore')
    except Exception as e: return ''
def ranks(q):
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)); out={}
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in out: out[m.group(1)]=len(out)+1
    return out
REG=['노원','도봉','은평','강서','구로','송파','강동','부천','인천','수원','영통','고양 일산','하남','구리','남양주','광명','안양','군포 산본','성남 분당','용인','의정부','안산','평택','화성 동탄','김포','시흥','대전','청주','부산','대구']
QS=['아파트 도배 장판','도배 장판 업체','도배 장판 비용 30평','실크 도배 시공','부분 도배 업체','장판 교체 시공','전세 도배 장판']+[r+' 도배 장판' for r in REG]+[r+' 도배 업체' for r in REG]
R={}
for i in range(0,len(QS),4):
    with ThreadPoolExecutor(4) as ex: R.update(dict(zip(QS[i:i+4],ex.map(ranks,QS[i:i+4]))))
    time.sleep(1.2)
agg={}
for q,d in R.items():
    for b,r in d.items(): agg.setdefault(b,{})[q]=r
print('검색어',len(QS),'· 결과 있는 검색어',sum(1 for v in R.values() if v),'· 블로그',len(agg),flush=True)
def rss(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',x); d=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S)
    dates=re.findall(r'<pubDate>(.*?)</pubDate>',x); n30=0; now=datetime.datetime(2026,10,8,tzinfo=datetime.timezone.utc)
    for s in dates:
        try:
            if (now-email.utils.parsedate_to_datetime(s)).days<=30: n30+=1
        except Exception: pass
    titles=re.findall(r'<item>.*?<title><!\[CDATA\[(.*?)\]\]>',x,re.S)[:50]
    ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-.]\d{3,4}[-.]\d{4}|1[5-8]\d{2}[-.]\d{4}',x)))[:3]
    return dict(name=(t.group(1) if t else ''),desc=(d.group(1)[:300] if d else ''),n30=n30,nitem=len(dates),titles=titles,ph=ph)
B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:260]
print('RSS 볼 블로그',len(B),flush=True)
INFO={}
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss,B[i:i+10]))))
    time.sleep(0.2)
pickle.dump((R,agg,INFO),open('scan.pkl','wb'))
print('done',len(INFO),flush=True)

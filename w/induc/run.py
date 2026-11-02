# 새 영역 업체 후보(10/14 09:56 사용자 「업체 추천 해줘」) — 욕실 덧방 · 현관 타일 · 베란다 확장 · w/dobae/run.py와 같은 방법
import re,urllib.parse,urllib.request,pickle,time,datetime,email.utils,json,sys
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
def get(u,ua=UA,t=8):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=t) as r: return r.read().decode('utf-8','ignore')
    except Exception: return ''
def ranks(q):
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)); out={}
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
        if m.group(1) not in out: out[m.group(1)]=len(out)+1
    return out
REG=['서울','송파','강서','노원','인천','수원','성남','부천','하남','남양주','고양','용인','안양','김포','화성 동탄']
CAT={'ind':['인덕션 설치','인덕션 설치 가스 철거','가스레인지 철거 인덕션','인덕션 전기공사','인덕션 단독배선','하이라이트 인덕션 교체','빌트인 인덕션 설치','인덕션 설치비용']+[r+' 인덕션 설치' for r in REG]}
KW={'ind':r'인덕션'}
res={}
for c,qs in CAT.items():
    R={}
    for i in range(0,len(qs),4):
        with ThreadPoolExecutor(4) as ex: R.update(dict(zip(qs[i:i+4],ex.map(ranks,qs[i:i+4]))))
        time.sleep(1.0)
    agg={}
    for q,d in R.items():
        for b,r in d.items(): agg.setdefault(b,{})[q]=r
    print(c,'검색어',len(qs),'결과',sum(1 for v in R.values() if v),'블로그',len(agg),flush=True)
    res[c]=(R,agg)
def rss(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',x); d=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S)
    dates=re.findall(r'<pubDate>(.*?)</pubDate>',x); n30=0; now=datetime.datetime(2026,10,14,tzinfo=datetime.timezone.utc)
    for s in dates:
        try:
            if (now-email.utils.parsedate_to_datetime(s)).days<=30: n30+=1
        except Exception: pass
    titles=re.findall(r'<item>.*?<title><!\[CDATA\[(.*?)\]\]>',x,re.S)[:50]
    ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-.]\d{3,4}[-.]\d{4}|1[5-8]\d{2}[-.]\d{4}',x)))[:3]
    return dict(name=(t.group(1) if t else ''),desc=(d.group(1)[:300] if d else ''),n30=n30,nitem=len(dates),titles=titles,ph=ph)
B=set()
for c,(R,agg) in res.items():
    B|=set([x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:150])
B=list(B); print('RSS',len(B),flush=True)
INFO={}
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss,B[i:i+10]))))
pickle.dump((res,INFO),open('induc/scan.pkl','wb')); print('done',len(INFO))

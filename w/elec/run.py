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
REG=['서울','노원','송파','강서','인천','수원','성남','부천','하남','남양주','구리','고양 일산','용인','안양','김포','의정부']
CAT={'el':['전기 수리 업체','전기 수리 기사','누전 차단기 수리','누전 수리','콘센트 교체','아파트 전기 수리','차단기 내려감','두꺼비집 교체','조명 전기 공사','전기 출장 수리']+[r+' 전기 수리' for r in REG]}
KW={'el':r'전기|누전|차단기|콘센트'}
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
pickle.dump((res,INFO),open('elec/scan.pkl','wb')); print('done',len(INFO))

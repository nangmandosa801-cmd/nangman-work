import re, urllib.parse, urllib.request, pickle, time, datetime, email.utils, json, sys
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def get(u,ua=UA,t=8):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=t) as r: return r.read().decode('utf-8','ignore')
    except Exception as e: return ''
def ranks(q):
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)); out={}
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in out: out[m.group(1)]=len(out)+1
    return out
def rss(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',x); d=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S)
    dates=re.findall(r'<item>.*?<pubDate>(.*?)</pubDate>',x,re.S); n30=0; now=datetime.datetime(2026,10,20,tzinfo=datetime.timezone.utc); last=None
    for s in dates:
        try:
            dt=email.utils.parsedate_to_datetime(s)
            if last is None or dt>last: last=dt
            if (now-dt).days<=30: n30+=1
        except Exception: pass
    items=re.findall(r'<item>(.*?)</item>',x,re.S)
    titles=[re.search(r'<title><!\[CDATA\[(.*?)\]\]>',i,re.S).group(1) for i in items[:50] if re.search(r'<title><!\[CDATA\[(.*?)\]\]>',i,re.S)]
    ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}',x)))[:4]
    return dict(name=(t.group(1) if t else ''),desc=(d.group(1)[:300] if d else ''),n30=n30,nitem=len(dates),last=(last.strftime('%Y-%m-%d') if last else ''),titles=titles,ph=ph)
REG=['송파','강동','강남','서초','강서','구로','금천','관악','양천','영등포','노원','도봉','중랑','광진','성북','은평','마포','서대문','하남','미사','남양주','구리','다산','별내','의정부','양주','고양 일산','파주','인천','부천','분당','성남','수원','용인','안양','화성 동탄','광명','김포']
P=['도어락 교체','현관문 교체','방화문 교체','열쇠 도어락']
QS=[r+' '+p for r in REG for p in P]
R={}
for i in range(0,len(QS),4):
    with ThreadPoolExecutor(4) as ex: R.update(dict(zip(QS[i:i+4],ex.map(ranks,QS[i:i+4]))))
    time.sleep(1.0)
agg={}
for q,d in R.items():
    for b,r in d.items(): agg.setdefault(b,{})[q]=r
B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:220]
INFO={}
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss,B[i:i+10]))))
pickle.dump((R,agg,INFO),open('dl.pkl','wb'))
print('검색어',len(QS),'결과있는',sum(1 for v in R.values() if v),'블로그',len(agg),'RSS',len(INFO))

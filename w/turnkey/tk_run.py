# 종합(턴키) 인테리어 업체 후보 찾기 (2026.10.8 08시 · 사용자 07:57 「둘다 가자」) — 네이버 블로그 검색 첫 화면에 나오는 블로그 아이디를 모으고 RSS로 이름 · 최근 글 수를 본다
import re, urllib.parse, urllib.request, pickle, time, html, datetime, email.utils
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
REG=['노원','도봉','강서','구로','송파','부천','인천','수원','고양 일산','하남','구리','남양주','광명','안양','성남 분당','용인','의정부','안산','평택','화성 동탄','김포','시흥']
QS=['구축 아파트 인테리어','구축 아파트 리모델링','아파트 부분 인테리어','아파트 올수리','부분 인테리어 업체','살면서 인테리어','30평대 아파트 인테리어 비용']+[r+' 아파트 인테리어' for r in REG]+[r+' 구축 아파트 인테리어' for r in REG]
R={}
for i in range(0,len(QS),4):
    with ThreadPoolExecutor(4) as ex: R.update(dict(zip(QS[i:i+4],ex.map(ranks,QS[i:i+4]))))
    time.sleep(1.2)
agg={}
for q,d in R.items():
    for b,r in d.items(): agg.setdefault(b,{})[q]=r
print('검색어',len(QS),'· 결과 있는 검색어',sum(1 for v in R.values() if v),'· 블로그',len(agg))
def rss(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',x); d=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S)
    dates=re.findall(r'<pubDate>(.*?)</pubDate>',x); n30=0; now=datetime.datetime(2026,10,8,tzinfo=datetime.timezone.utc)
    for s in dates:
        try:
            if (now-email.utils.parsedate_to_datetime(s)).days<=30: n30+=1
        except Exception: pass
    titles=re.findall(r'<item>.*?<title><!\[CDATA\[(.*?)\]\]>',x,re.S)[:12]
    return dict(name=(t.group(1) if t else ''),desc=(d.group(1)[:200] if d else ''),n30=n30,nitem=len(dates),titles=titles)
pickle.dump((R,agg),open('search.pkl','wb'))
B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:220]
print('RSS 볼 블로그',len(B),flush=True)
INFO={}
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss,B[i:i+10]))))
    time.sleep(0.2)
pickle.dump((R,agg,INFO),open('scan.pkl','wb'))
for b in B[:90]:
    i=INFO[b]; print(b,'|',i['name'][:28],'| 30일',i['n30'],'| 검색어',len(agg[b]),'|',' · '.join(list(agg[b])[:3]),'|',i['desc'][:60].replace('\n',' '))

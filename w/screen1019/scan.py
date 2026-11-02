# 방충망 제휴 후보 19차 (10/19 사용자 「방충망 업체 찾아봐」) — w/expand/scan.py ranks()/rss() 방식
import re, urllib.parse, urllib.request, pickle, time, datetime, email.utils, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'/home/claude/w/expand')
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def get(u,ua=UA,t=8):
    for k in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=t) as r: return r.read().decode('utf-8','ignore')
        except Exception as e: time.sleep(2)
    return ''
def ranks(q):
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)); out={}
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in out: out[m.group(1)]=len(out)+1
    return out
NOW=datetime.datetime(2026,10,19,tzinfo=datetime.timezone.utc)
def rss(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',x); d=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S)
    items=re.findall(r'<item>(.*?)</item>',x,re.S); its=[]
    for it in items:
        tt=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',it,re.S); pd=re.search(r'<pubDate>(.*?)</pubDate>',it); lk=re.search(r'<link><!\[CDATA\[(.*?)\]\]>|<link>(.*?)</link>',it)
        try: days=(NOW-email.utils.parsedate_to_datetime(pd.group(1))).days
        except Exception: days=9999
        its.append(dict(t=tt.group(1) if tt else '',days=days,link=(lk.group(1) or lk.group(2)) if lk else '',body=it[:4000]))
    ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-.]\d{3,4}[-.]\d{4}|1[5-8]\d{2}[-.]\d{4}',x)))
    return dict(name=(t.group(1) if t else ''),desc=(d.group(1)[:400] if d else ''),items=its,ph=ph,raw=len(x))
REG=['서울 강남','서울 송파','서울 노원','서울 은평','서울 마포','남양주','하남','구리','수원','용인','성남','고양','파주','김포','인천','부천','시흥','안양','화성','평택','대전','청주','부산','경남','대구']
GEN=['방충망 교체','방충망 수리','미세방충망','촘촘망','롤방충망','현관 방충망','방묘창','스텐 방충망','방충망 시공 업체']
QS=GEN+[r+' '+p for r in REG for p in ['방충망 교체','방충망 수리','미세방충망']]
if __name__=='__main__':
    R={}
    for i in range(0,len(QS),3):
        with ThreadPoolExecutor(3) as ex: R.update(dict(zip(QS[i:i+3],ex.map(ranks,QS[i:i+3]))))
        time.sleep(2.0)
        if i%30==0: print(i,sum(1 for v in R.values() if v),flush=True)
    agg={}
    for q,d in R.items():
        for b,r in d.items(): agg.setdefault(b,{})[q]=r
    B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:170]
    for extra in ['bbjch7294','shhg4632','hjyh0921','thrcara-jeju']:
        if extra not in B: B.append(extra)
    INFO={}
    for i in range(0,len(B),3):
        with ThreadPoolExecutor(3) as ex: INFO.update(dict(zip(B[i:i+3],ex.map(rss,B[i:i+3]))))
        time.sleep(0.8)
    pickle.dump((R,agg,INFO),open('/home/claude/w/screen1019/screen.pkl','wb'))
    print('검색어',len(QS),'결과 있는',sum(1 for v in R.values() if v),'블로그',len(agg),'RSS',len(INFO),'ALL DONE',flush=True)

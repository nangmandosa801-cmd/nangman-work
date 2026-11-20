#!/usr/bin/env python3
"""하남 검색어 순위 재기 (모바일 블로그 탭). python3 hanam_rank.py [--save]
3번 재서 나쁜 쪽 순위를 적고 맨 끝에 [좋은 쪽 지산, 낭만]. 결과: 검색어마다 지산드림 / 낭만 부동산 / hanam-curator 순위(0 = 첫 쪽에 없음) + 1위 블로그. --save 면 rank_log.json 에 날짜별로 쌓음."""
import urllib.request,urllib.parse,re,json,sys,datetime,os
KW=['하남 토지','하남 땅값','하남 토지거래허가','하남 토지거래허가구역 해제','하남 땅 사는법','하남 토지 매매','그린벨트 땅값','토지 매도 방법','하남 그린벨트 해제','하남 그린벨트 해제 지역','비사업용토지 양도세','하남 초이동','하남 감북동','하남 초일동','하남 상산곡동','하남 춘궁동',
'하남 집값','하남 부동산','하남 부동산 전망','하남 아파트 시세','미사 아파트 시세','감일 아파트','하남 교산신도시','교산신도시 분양가']
ME=['jisandream01','dong_jin_kim','hanam-curator']
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile Safari/604.1'
def _one(k):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(k)
    h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=12).read().decode('utf8','ignore')
    ids=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h):
        if m.group(0) not in ids: ids.append(m.group(0))
    b=[i.split('/')[1] for i in ids]
    return [ (b.index(x)+1) if x in b else 0 for x in ME ]+[b[0] if b else '']
def one(k):
    # 네이버가 같은 검색어에 두 가지 결과를 번갈아 보여 준다(11/21 「하남 토지」 2위 ↔ 26위). 3번 재서 나쁜 쪽을 적는다.
    import time
    rs=[]
    for _ in range(3):
        rs.append(_one(k)); time.sleep(1)
    w=lambda i:max((r[i] or 99) for r in rs)
    b=lambda i:min((r[i] or 99) for r in rs)
    f=lambda x:0 if x==99 else x
    return [f(w(0)),f(w(1)),f(w(2)),rs[0][3],[f(b(0)),f(b(1))]]
out={}
for k in KW:
    try: out[k]=one(k)
    except Exception as e: out[k]=[-1,-1,-1,str(e)[:30]]
top=lambda i:sum(1 for v in out.values() if 1<=v[i]<=3)
first=lambda i:sum(1 for v in out.values() if v[i]==1)
summ={'n':len(KW),'jisan_top3':top(0),'nangman_top3':top(1),'rival_top3':top(2),'jisan_1':first(0),'nangman_1':first(1),'either_top3':sum(1 for v in out.values() if 1<=v[0]<=3 or 1<=v[1]<=3)}
if '--save' in sys.argv:
    p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'rank_log.json')
    L=json.load(open(p)) if os.path.exists(p) else {}
    L[datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d')]={'sum':summ,'kw':out}
    json.dump(L,open(p,'w'),ensure_ascii=False,indent=0)
for k,v in out.items(): print(k,v)
print(json.dumps(summ,ensure_ascii=False))

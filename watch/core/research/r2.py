import subprocess,urllib.parse,re,json,html,datetime as dt
from concurrent.futures import ThreadPoolExecutor
T=dt.date(2026,10,22)
Q=['인테리어 견적서 보는법','인테리어 견적 비교','입주청소 견적 비교','인테리어 사기 안당하는법','샷시 교체 비용','아파트 샷시 교체 비용 32평','샷시 교체 지원금','30평 아파트 도배 비용','실크벽지 합지벽지 금액차이','도배 평당단가','입주청소 평당 가격','입주청소 견적 공급면적','입주청소 업체 추천']
def serp(q):
    u='https://m.search.naver.com/search.naver?'+urllib.parse.urlencode(dict(where='m_blog',query=q))
    h=subprocess.run(['curl','-s','-m','15',u,'-A','Mozilla/5.0 (iPhone)'],capture_output=True,text=True).stdout
    # 제목: title 링크 텍스트
    ts=[]
    for m in re.finditer(r'<a[^>]+href="https?://(?:m\.)?blog\.naver\.com/([^/"]+)/(\d{9,})"[^>]*>(.*?)</a>',h,re.S):
        t=html.unescape(re.sub('<[^>]+>','',m.group(3))).strip()
        if 8<len(t)<120 and (m.group(1),t) not in [(a,b) for a,b in ts]: ts.append((m.group(1),t))
    ds=re.findall(r'(\d{4})\.(\d{1,2})\.(\d{1,2})\.|(\d+)(일|주|시간|분) 전',h)[:10]
    age=[]
    for y,mo,d,n,u_ in ds:
        age.append((T-dt.date(int(y),int(mo),int(d))).days if y else {'일':1,'주':7,'시간':0,'분':0}[u_]*int(n))
    return dict(titles=ts[:10],age=age)
with ThreadPoolExecutor(5) as ex: R=dict(zip(Q,ex.map(serp,Q)))
json.dump(R,open('serp.json','w'),ensure_ascii=False,indent=1)
for q,v in R.items():
    print(f"\n## {q} · 나이(일) {v['age']}")
    for b,t in v['titles'][:8]: print('  -',t[:70],'|',b)

import sys,re,json,time,collections,datetime,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
hits=json.load(open('hits.json'))
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
SKIP={'champion_chart','lsh_house','wgtung','dong_jin_kim','jisandream01'}
B=[b for b,v in c if len(set(q for q,_ in v))>=3 and b not in SKIP][:170]
print(len(B),flush=True)
today=datetime.date(2026,10,7)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d)
    return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else today
KW={'농막':r'농막','체류형':r'체류형','이동식':r'이동식 ?주택|모듈러|소형 ?주택|세컨하우스','컨테이너':r'컨테이너','목조':r'목조|목구조|통나무','출고':r'출고|납품|설치 ?완료|제작 ?현장|제작기|시공'}
out={}
for b in B:
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception: L=[]
    ds=[pd(d) for _,_,d in L]
    cov={k:sum(1 for _,t,_ in L if re.search(p,t)) for k,p in KW.items()}
    out[b]=dict(n=len(L),n30=sum(1 for d in ds if (today-d).days<=30),last=str(max(ds)) if ds else '',cov=cov,nq=len(set(q for q,_ in hits[b])),t5=[t for _,t,_ in L[:5]],first=hits[b][0][1])
    time.sleep(0.3)
json.dump(out,open('prof.json','w'),ensure_ascii=False)
r=sorted(out.items(),key=lambda x:(-(x[1]['cov']['농막']+x[1]['cov']['체류형']+x[1]['cov']['이동식']),-x[1]['n30']))
for b,o in r[:80]:
    print(f"{b} | 검색어 {o['nq']} | 30일 {o['n30']}편 · 마지막 {o['last']} | "+' '.join(f'{k}{v}' for k,v in o['cov'].items() if v)+' | '+(o['t5'][0][:40] if o['t5'] else ''))

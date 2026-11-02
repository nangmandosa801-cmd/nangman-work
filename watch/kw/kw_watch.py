# 자동완성 키워드 관찰 — python3 kw_watch.py daily|weekly
# 원칙: 전략 doc 「키워드 추출 원칙」. 매일 = 계절 · 날씨 품목 + 이번 주 쓸 글 씨앗 / 매주 = 전체 매트릭스(주거 유형 × 품목 · 지역 × 품목)
import json,subprocess,urllib.parse,sys,os,re,glob,datetime as dt
from concurrent.futures import ThreadPoolExecutor
K='/home/claude/watch/kw'; T=dt.date.today(); MODE=sys.argv[1] if len(sys.argv)>1 else 'daily'
def ac(q):
    u='https://ac.search.naver.com/nx/ac?'+urllib.parse.urlencode(dict(q=q,con=1,frm='nv',ans=2,r_format='json',r_enc='UTF-8',r_unicode=0,t_koreng=1,run=2,rev=4,q_enc='UTF-8',st=100))
    for _ in range(3):
        try: return [i[0] for i in json.loads(subprocess.run(['curl','-s','-m','10',u,'-A','Mozilla/5.0'],capture_output=True,text=True).stdout)['items'][0]]
        except Exception: pass
    return None
TYPES=['아파트','구축아파트','빌라','단독주택','주택','오피스텔','원룸','상가','사무실','전원주택','농막','다가구']
ITEMS=['누수','누수탐지','옥상 방수','외벽 방수','동파','보일러 교체','샷시 교체','단열','결로','곰팡이','외풍','중문','도배','리모델링','올수리','욕실 리모델링','원상복구','인테리어','입주청소','이사청소','줄눈','탄성코트','방충망','필름','지붕','외벽 페인트','배관','수리','에어컨 설치','현관문']
REG=['서울','은평','강서','관악','중랑','강북','도봉','노원','마포','송파','광진','구로','양천','동작','성북','영등포','강동','수원','부천','인천','고양','일산','성남','분당','안양','의정부','남양주','화성','용인','평택','김포','하남','구리','광명','시흥','안산','부산','대구','대전','광주','울산','청주','천안','전주','창원','김해','포항','강릉','원주','춘천','제주','세종']
RITEMS=['누수','누수탐지','옥상 방수','지붕 공사','보일러 교체','샷시 교체','중문','인테리어','입주청소','줄눈','동파','상가 인테리어','주택 리모델링','원룸 입주청소']
SEASON={1:'동파 보일러 결로 곰팡이 도배',2:'이사 입주청소 도배',3:'이사 도배 필름 방충망',4:'탄성코트 외벽 방수 샷시 교체 리모델링',5:'방충망 에어컨 설치',6:'누수 외벽 방수 에어컨 설치',7:'누수 곰팡이 결로 단열',8:'샷시 교체 방충망 누수',9:'이사 입주청소 도배',10:'외풍 중문 보일러 교체 단열',11:'단열 결로 보일러 교체 외풍',12:'동파 보일러 교체 결로 외풍'}
seeds=set()
season=(SEASON[T.month]+' '+SEASON[T.month%12+1]).split()
for s in season: seeds|={s}|{f'{t} {s}' for t in TYPES}
# 이번 주 쓸 글 씨앗: 일정표 「[쓸 글]」 · 미발행 제목 앞머리(쉼표 앞)
try:
    ms=json.load(open('/home/claude/watch/mix_schedule_1017c.json'))
    for r in ms:
        d=r.get('_d') or ''
        if d and T.isoformat()<=d<=(T+dt.timedelta(14)).isoformat() and not (r.get('상태') or '').startswith('발행'):
            h=re.sub(r'^\[쓸 글\]\s*','',r['제목']).split(',')[0].split('(')[0].strip()
            if 2<len(h)<30: seeds.add(h)
except Exception: pass
if MODE=='weekly':
    seeds|={f'{t} {i}' for t in TYPES for i in ITEMS}|{f'{r} {i}' for r in REG for i in RITEMS}|set(ITEMS)
seeds=sorted(seeds)
if len(sys.argv)>2 and sys.argv[2]=='rescore':
    res={q:v['sug'] for q,v in json.load(open(sorted(glob.glob(f'{K}/snap_{MODE}_*.json'))[-1])).items()}
else:
    with ThreadPoolExecutor(10) as ex: res=dict(zip(seeds,ex.map(ac,seeds)))
BUY=re.compile(r'비용|가격|업체|견적|시공|공사|교체|추천|후기|설치|잘하는')
DISP=re.compile(r'책임|보험|분쟁|소송|내용증명|누가|집주인|세입자|건물주|기준|범위')
SELF=re.compile(r'셀프|DIY|diy|하는법|만들기')
NOISE=re.compile(r'타이어|엔진오일|자동차|차량|핸드폰|휴대폰|아이폰|갤럭시|배터리|액정|필터|와이퍼|브레이크|상가집|소파|게임|노래|가사|영화|드라마|주식|뜻|영어로|학원|교육|자격증|창업|술집|알바|구인|동파육|동판|캐리어|탕수육|교회|덮밥|세면대|파스타|파전|파리바게|파히타|파인빌|파크골프|맛집|호텔|펜션')
snap={}
for q,v in res.items():
    if v is None: continue
    v=[x for x in v if not NOISE.search(x)]
    tail=[x[len(q):].strip() if x.replace(' ','').startswith(q.replace(' ','')) else x for x in v]
    snap[q]=dict(sug=v,live=any(x.replace(' ','')==q.replace(' ','') for x in v) or bool(v),
        buy=sum(1 for x in tail if BUY.search(x)),disp=sum(1 for x in tail if DISP.search(x)),self=sum(1 for x in tail if SELF.search(x)))
p=f'{K}/snap_{MODE}_{T:%Y%m%d}.json'; json.dump(snap,open(p,'w'),ensure_ascii=False)
# 바뀐 것: 같은 모드 바로 앞 스냅샷과 비교
prev=sorted(glob.glob(f'{K}/snap_{MODE}_*.json'))
old=json.load(open(prev[-2])) if len(prev)>1 else {}
new_words=[];gone=[]
for q,s in snap.items():
    o=set(old.get(q,{}).get('sug',[])); n=set(s['sug'])
    if old and q in old:
        new_words+= [(q,x) for x in n-o]; gone+=[(q,x) for x in o-n]
score=lambda s: s['buy']*2+s['disp']*2+len(s['sug'])-s['self']*2
top=sorted(((score(s),q,s) for q,s in snap.items() if s['sug'] and ' ' in q),reverse=True)
json.dump([dict(kw=q,score=sc,buy=s['buy'],disp=s['disp'],sug=s['sug'][:10]) for sc,q,s in top],open(f'{K}/kw_ledger_{MODE}.json','w'),ensure_ascii=False)
out=[f'# 키워드 관찰 {MODE} {T}','',f'- 씨앗 {len(seeds)} · 살아 있는 말 {sum(1 for s in snap.values() if s["sug"])} · 앞 스냅샷 {os.path.basename(prev[-2]) if len(prev)>1 else "없음"}','',
 '## 점수 상위 40 (구매 · 책임 말 ×2 + 제안 수 − 셀프 ×2)','','| 키워드 | 점수 | 구매 | 책임 · 분쟁 | 셀프 | 자동완성(앞 6) |','|---|---|---|---|---|---|']
out+=[f"| {q} | {sc} | {s['buy']} | {s['disp']} | {s['self']} | {' · '.join(s['sug'][:6])} |" for sc,q,s in top[:40]]
out+=['','## 새로 뜬 말 (기회)','']+([f'- {q} → {x}' for q,x in new_words[:60]] or ['- 없음(첫 스냅샷이거나 변화 없음)'])
out+=['','## 사라진 말 (철 지남 · 일정 뒤로)','']+([f'- {q} → {x}' for q,x in gone[:60]] or ['- 없음'])
open(f'{K}/kw_{MODE}_latest.md','w').write('\n'.join(out)); print('\n'.join(out[:12])); print('...',len(new_words),'new',len(gone),'gone')

# ── 빈자리 검사 (매주만): 점수 상위 + 롱테일(구매 말 붙은 자동완성) 40개의 블로그 탭 상위 10
OURS={'champion_chart':'인테리어','dong_jin_kim':'부동산'}
def serp(q):
    u='https://m.search.naver.com/search.naver?'+urllib.parse.urlencode(dict(where='m_blog',query=q))
    h=subprocess.run(['curl','-s','-m','15',u,'-A','Mozilla/5.0 (iPhone)'],capture_output=True,text=True).stdout
    ids=[];[ids.append(b) for b,_ in re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h) if b not in ids]
    ds=re.findall(r'(\d{4})\.(\d{1,2})\.(\d{1,2})\.|(\d+)(일|주|시간|분) 전',h)[:10]
    age=[]
    for y,m,d,n,u_ in ds:
        if y: age.append((T-dt.date(int(y),int(m),int(d))).days)
        else: age.append({'일':1,'주':7,'시간':0,'분':0}[u_]*int(n))
    old=sum(1 for a in age if a>365); rank={OURS[b]:i+1 for i,b in enumerate(ids[:10]) if b in OURS}
    return dict(old=old,n=len(age),fresh=sum(1 for a in age if a<=60),ours=rank)
if MODE=='weekly':
    pick=[q for _,q,_ in top[:20]]
    for _,q,s in top[:60]:
        for x in s['sug']:
            if x!=q and BUY.search(x) and x not in pick: pick.append(x); break
    pick=pick[:40]
    with ThreadPoolExecutor(5) as ex: sp=dict(zip(pick,ex.map(serp,pick)))
    json.dump(sp,open(f'{K}/serp_{T:%Y%m%d}.json','w'),ensure_ascii=False)
    rows=sorted(sp.items(),key=lambda kv:(-kv[1]['old'],kv[1]['fresh']))
    add=['','## 빈자리 (블로그 탭 상위 10 · 1년 넘은 글이 많을수록 들어갈 틈)','','| 키워드 | 1년+ 글 | 60일 안 글 | 우리 순위 |','|---|---|---|---|']
    add+=[f"| {q} | {v['old']}/{v['n']} | {v['fresh']} | {' · '.join(f'{k} {r}위' for k,r in v['ours'].items()) or '-'} |" for q,v in rows]
    open(f'{K}/kw_{MODE}_latest.md','a').write('\n'.join(add)+'\n'); print('\n'.join(add[:25]))

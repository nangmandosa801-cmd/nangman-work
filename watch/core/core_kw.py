# 근본 콘텐츠 검색어 다시 고르기 — python3 core_kw.py   (매주 월 · 주간 점검 A2)
# 원칙 = core_rules.json(무게) · 결과 = results.json(조회 · 문의 · 계약) · 출력 = core_rank.json · core_rank_latest.md · core_plan.json 순서 갱신
import json,re,subprocess,urllib.parse,glob,datetime as dt,os,html
from concurrent.futures import ThreadPoolExecutor
C='/home/claude/watch/core'; T=dt.date.today(); R=json.load(open(C+'/core_rules.json'))
plan=json.load(open(C+'/core_plan.json'))
res=json.load(open(C+'/results.json')) if os.path.exists(C+'/results.json') else {'글':[]}
def ac(q):
    u='https://ac.search.naver.com/nx/ac?'+urllib.parse.urlencode(dict(q=q,con=1,frm='nv',ans=2,r_format='json',r_enc='UTF-8',r_unicode=0,t_koreng=1,run=2,rev=4,q_enc='UTF-8',st=100))
    try: return [i[0] for i in json.loads(subprocess.run(['curl','-s','-m','10',u,'-A','Mozilla/5.0'],capture_output=True,text=True).stdout)['items'][0]]
    except Exception: return []
def serp(q):
    u='https://m.search.naver.com/search.naver?'+urllib.parse.urlencode(dict(where='m_blog',query=q))
    h=subprocess.run(['curl','-s','-m','15',u,'-A','Mozilla/5.0 (iPhone)'],capture_output=True,text=True).stdout
    ages=[]
    for y,m,d,n,un in re.findall(r'(\d{4})\.(\d{1,2})\.(\d{1,2})\.|(\d+)(일|주|시간|분) 전',h)[:10]:
        ages.append((T-dt.date(int(y),int(m),int(d))).days if y else {'일':1,'주':7,'시간':0,'분':0}[un]*int(n))
    ours=[i+1 for i,b in enumerate(dict.fromkeys(re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/\d{9,}',h))) if b=='champion_chart']
    return dict(ages=ages,ours=ours[0] if ours else None)
# 1) 씨앗 = 목록의 키워드 + 꼬리 → 두 단계 자동완성
items=plan['글']; seeds={it['키워드']:it for it in items}
for it in items:
    for t in it.get('꼬리',[]): seeds.setdefault(t,it)
with ThreadPoolExecutor(8) as ex: L1=dict(zip(seeds,ex.map(ac,seeds)))
l2=sorted({x for v in L1.values() for x in v}-set(seeds))
with ThreadPoolExecutor(8) as ex: L2=dict(zip(l2,ex.map(ac,l2)))
MIX=re.compile(R['섞인말'])
def intents(w): return [k for k,v in R['의도'].items() if re.search(v['말'],w)]
def iscore(w): return sum(R['의도'][k]['무게'] for k in intents(w))
cand={}
for s,v in list(L1.items())+list(L2.items()):
    for w in v:
        if MIX.search(w) or re.search(r'울산|대구|부산|광주|대전|천안|청주|포항|창원|전주|원주|제주|김해|강릉|춘천|세종|진주|구미|순천|\d{4}',w): continue
        c=cand.setdefault(w,dict(kw=w,부모=s,깊이=0,의도=intents(w),뜸=0)); c['뜸']+=1
for w,c in cand.items(): c['자식']=len(L2.get(w,[])) ; c['깊이']=c['뜸']+c['자식']
# 2) 상위 40(의도 점수 + 깊이)만 빈자리 검사
pre=sorted(cand.values(),key=lambda c:-(iscore(c['kw'])+0.3*c['깊이']))[:40]
with ThreadPoolExecutor(5) as ex: S=dict(zip([c['kw'] for c in pre],ex.map(serp,[c['kw'] for c in pre])))
G=R['빈자리']; can=R['할수있음']
# 3) 결과(이미 발행한 근본 글 성적)를 같은 품목 · 같은 의도에 더함
def result_bonus(c):
    b=0
    for g in res.get('글',[]):
        if g.get('품목') and g['품목'] in c['부모'] or (g.get('의도') and set(g['의도'])&set(c['의도'])):
            b+=g.get('조회',0)/100*R['결과']['조회_1백당']+g.get('문의',0)*R['결과']['문의_1건']+g.get('계약',0)*R['결과']['계약_1건']
    return b
for c in pre:
    s=S[c['kw']]; ages=s['ages']
    gap=sum(G['오래된글_무게'] for a in ages if a>G['오래된글_일수'])-sum(G['새글_벌점'] for a in ages if a<=G['새글_일수'])
    it=seeds.get(c['부모'],{}); ok=can.get(it.get('제휴','없음'),0)
    c.update(빈자리=round(gap,2),우리순위=s['ours'],할수있음=ok,결과=round(result_bonus(c),2),
             점수=round(iscore(c['kw'])+0.3*c['깊이']+gap+ok*can['무게']+result_bonus(c),2),품목=it.get('키워드'))
pre.sort(key=lambda c:-c['점수'])
prev=sorted(glob.glob(C+'/core_rank_2*.json')); old={x['kw']:x for x in json.load(open(prev[-1]))} if prev else {}
json.dump(pre,open(C+f'/core_rank_{T:%Y%m%d}.json','w'),ensure_ascii=False,indent=1)
# 4) 품목 순서 다시 매김: 품목별 상위 3개 점수 합
agg={}
for c in pre: agg.setdefault(c['품목'],[]).append(c['점수'])
order=sorted(agg,key=lambda k:-sum(sorted(agg[k],reverse=True)[:3]))
for it in items:
    if it['키워드'] in agg:
        best=[c for c in pre if c['품목']==it['키워드'] and '셀프형' not in c['의도']][:4]
        it['고른말']=[c['kw'] for c in best]; it['점수']=round(sum(sorted(agg[it['키워드']],reverse=True)[:3]),2)
pending=[it for it in items if it.get('상태')=='쓸 글']
pending.sort(key=lambda it:(-(it.get('점수') or 0)))
plan['다음_순서']=[it['키워드'] for it in pending]; plan['갱신']=str(T); plan['원칙판']=R['판']
json.dump(plan,open(C+'/core_plan.json','w'),ensure_ascii=False,indent=1)
o=[f'# 근본 콘텐츠 검색어 판정 {T} · 원칙 {R["판"]}','',f'- 후보 {len(cand)} → 빈자리 검사 {len(pre)} · 결과 반영 글 {len(res.get("글",[]))}편','',
   '| 검색어 | 점수 | 의도 | 깊이 | 빈자리 | 할 수 있음 | 결과 | 우리 순위 | 지난주 |','|---|---|---|---|---|---|---|---|---|']
for c in pre[:30]:
    p=old.get(c['kw']); o.append(f"| {c['kw']} | {c['점수']} | {' · '.join(c['의도'])} | {c['깊이']} | {c['빈자리']} | {c['할수있음']} | {c['결과']} | {c['우리순위'] or '-'} | {(str(p['점수'])) if p else '새로'} |")
o+=['','## 다음에 쓸 근본 글 순서','']+[f"{i+1}. {k} — 고른 말: {' · '.join(next((it.get('고른말',[]) for it in items if it['키워드']==k),[]))}" for i,k in enumerate(plan['다음_순서'][:8])]
open(C+'/core_rank_latest.md','w').write('\n'.join(o)); print('\n'.join(o))

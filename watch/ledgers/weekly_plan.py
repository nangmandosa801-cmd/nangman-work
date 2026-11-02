# 주간 운영표 — 일정 마스터(mix_schedule · 장부) × 전략 마스터(전략 doc 목표 비율)를 한 장으로
# python3 weekly_plan.py [YYYY-MM-DD(그 주 월요일)] → /home/claude/watch/ledgers/weekly/W<주>.md 와 stdout
import json,sys,re,datetime as dt,os
W='/home/claude/watch'
today=dt.date.today()
mon=dt.date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else today-dt.timedelta(days=today.weekday())
days=[mon+dt.timedelta(i) for i in range(7)]
ms=json.load(open(W+'/mix_schedule_1017c.json'))
ipju=[re.sub(r'\(.*?\)','',x['단지']).strip() for x in json.load(open(W+'/ipju_master.json'))['단지목록']]
# 전략 목표 비율(가설 · 전략 doc 「시험 중인 가설」과 함께 고친다)
TARGET={'근본(가격표 · 견적 비교 · 패키지 · 문제 허브 · 믿음)':0.06,'계절 · 날씨':0.38,'입주 사이클':0.28,'15년 이상 리모델링 · 수리':0.14,'2년차':0.05,'재정비':0.04,'기타':0.05}
CORE='근본(가격표 · 견적 비교 · 패키지 · 문제 허브 · 믿음)'
def kind(t):
    if re.search(r'\[근본\]|가격표|견적 비교|견적비교|패키지|이렇게 일합니다|시공 기록|증상 · 원인',t): return CORE
    if re.search(r'재건축|재개발|이주|관리처분|정비구역',t): return '재정비'
    if re.search(r'하자보수|2년 ?차|전세 만기|입주 2년',t): return '2년차'
    if re.search(r'리모델링|올수리|구축|욕실 공사|주방 공사|샷시 교체',t): return '15년 이상 리모델링 · 수리'
    if re.search(r'입주|사전점검|신혼희망타운',t) or any(n.replace(' ','') in t.replace(' ','') for n in ipju if len(n)>4): return '입주 사이클'
    # 계절 · 날씨: 전략 doc 표 3 — 그달 · 다음 달 품목(달마다 바뀜)
    SEASON={1:'동파|보일러|결로|곰팡이|아이방|도배|청소',2:'이사|입주청소|아이방|신혼',3:'이사|도배|필름|창호|틈새|환기|방충망',4:'탄성|외벽|코킹|샷시|리모델링',5:'방충망|에어컨|안전손잡이',6:'코킹|누수|에어컨|단열 ?필름',7:'누수|곰팡이|결로|단열 ?필름|에어컨',8:'샷시|방충망|코킹',9:'이사|청소|도배',10:'외풍|문풍지|중문|보일러|방풍|모헤어|틈새',11:'단열|결로|보일러|외풍|방풍|뽁뽁이|창문',12:'동파|보일러|결로|곰팡이|외풍|단열'}
    m=mon.month; pat=SEASON[m]+'|'+SEASON[m%12+1]
    if re.search(pat,t): return '계절 · 날씨'
    return '기타'
rows=[r for r in ms if r.get('_d') and dt.date.fromisoformat(r['_d']) in days]
rows.sort(key=lambda r:(r['_d'],r.get('시각','')))
cnt={k:0 for k in TARGET}
for r in rows: r['_k']=kind(r['제목']); cnt[r['_k']]+=1
n=len(rows) or 1
wk=mon.isocalendar()[1]
o=[f'# 주간 운영표 W{wk} ({mon:%m/%d}~{days[-1]:%m/%d})','',f'만든 때 {dt.datetime.now():%Y-%m-%d %H:%M} · 일정 {len(rows)}칸','',
'## 전략 비율과 이번 주','','| 갈래 | 목표 | 이번 주 | 차이 |','|---|---|---|---|']
for k,v in TARGET.items():
    c=cnt[k]; o.append(f'| {k} | {round(v*100)}% ({round(v*n)}칸) | {c}칸 | {c-round(v*n):+d} |')
o+=['','## 칸','','| 날 | 시각 | 갈래 | 글 | 상태 |','|---|---|---|---|---|']
for r in rows: o.append(f"| {r['_d'][5:]} | {r.get('시각','')} | {r['_k']} | {r['제목'][:60]} | {(r.get('상태') or '쓸 글')[:22]} |")
gap=[k for k in TARGET if cnt[k]<round(TARGET[k]*n)]
o+=['','## 이번 주에 고칠 것',f'- 모자란 갈래: {" · ".join(gap) or "없음"} → 비어 있는 「[쓸 글]」 칸이나 예약 안 된 칸을 이 갈래 글로 바꾼다(「예약…」 줄은 옮기지 않음).',
'- 남는 갈래는 다음 주로 미룰 수 있는지 본다.']
import subprocess
o+=['']+subprocess.run(['python3',W+'/ledgers/candidates.py',mon.isoformat()],capture_output=True,text=True).stdout.splitlines()
# ④ 키워드: 이번 주 빈 칸을 채울 후보 (kw_watch.py weekly 결과)
try:
    L=json.load(open(W+'/kw/kw_ledger_weekly.json')); SP={}
    import glob as _g
    sp=sorted(_g.glob(W+'/kw/serp_*.json')); SP=json.load(open(sp[-1])) if sp else {}
    o+=['','## ④ 키워드 후보 (자동완성 점수 · 빈자리)','','| 키워드 | 점수 | 붙일 말(자동완성) | 빈자리 |','|---|---|---|---|']
    for r in L[:25]:
        tails=[x for x in r['sug'] if x!=r['kw']][:3]; g=SP.get(r['kw'])
        o.append(f"| {r['kw']} | {r['score']} | {' · '.join(tails)} | {(str(g['old'])+'/10 낡음') if g else '-'} |")
    o+=['- 제목 맨 앞에 키워드, 붙일 말 하나를 뒤에(예: 「주택 누수 비용, …」). 같은 키워드 4주 안 두 번 쓰지 않음.']
except Exception as e: o+=['',f'(키워드 장부 없음: {e})']
os.makedirs(W+'/ledgers/weekly',exist_ok=True)
p=W+f'/ledgers/weekly/W{wk}.md'; open(p,'w').write('\n'.join(o)); print('\n'.join(o))

# 통합 일정표 — python3 master.py [check|apply]
# 원천(고치는 곳): 인테리어 = watch/mix_schedule_1017c.json · 부동산 = bd/month_1021_1119.tsv + bd/bd_schedule.json + master/b_override.json
# 짝 · 앞뒤 · 같이 쓸 내용 = master/pairs.json. 규칙 = 전략 doc 「부동산 글 ↔ 인테리어 글 앞뒤 순서」 · 「내용으로 잇는 법」
import json,re,sys,os,shutil,datetime as dt
W='/home/claude/watch'; M=W+'/master'; MODE=sys.argv[1] if len(sys.argv)>1 else 'check'
T=dt.date.today(); Y=2026
def d_of(s):
    m=re.match(r'(\d+)/(\d+)',s); y=Y if int(m.group(1))>=10 else Y+1; return dt.date(y,int(m.group(1)),int(m.group(2)))
pub=open('/home/claude/proj/발행글_목록_부동산_인테리어.md').read()
bd_pub,int_pub=pub.split('## 낭만 인테리어')[0],pub.split('## 낭만 인테리어',1)[1] if '## 낭만 인테리어' in pub else ''
def pub_rows(txt):
    out=[]
    for l in txt.splitlines():
        m=re.match(r'\|[^|]*\|\s*(\d{12})\s*\|\s*(.*?)\s*\|',l)
        if m: out.append((m.group(1),m.group(2)))
    return out
BP,IP=pub_rows(bd_pub),pub_rows(int_pub)
def head(t): return re.sub(r'\s','',re.sub(r'^\[.*?\]\s*','',t).split(',')[0])[:14]
def bd_status(t):
    h=head(t); hit=next((n for n,x in BP if head(x)==h),None); return ('발행 '+hit) if hit else ''
# ── 인테리어 줄
MS=W+'/mix_schedule_1017c.json'; ms=json.load(open(MS)); I=[]
for i,r in enumerate(ms):
    if '_d' not in r: continue
    st=r.get('상태') or ''
    I.append(dict(id=f'I{i}',blog='인테리어',date=dt.date.fromisoformat(r['_d']),time=r.get('시각',''),title=r['제목'],status=st or ('쓸 글' if r['제목'].startswith('[') else '미발행 원고'),
        fixed=st.startswith(('예약','발행')),fill=(not st.startswith(('예약','발행'))) and r['제목'].startswith(('[쓸 글]','[새 시공]')) and '짝 ' not in r['제목'],idx=i))
# ── 부동산 줄
B=[]; ov=json.load(open(M+'/b_override.json')) if os.path.exists(M+'/b_override.json') else {}
bs=json.load(open(W+'/bd/bd_schedule.json'))
swaps={r['slot']:r for r in bs if r.get('swap') and r['slot']}
pushed=[]
for l in open(W+'/bd/month_1021_1119.tsv'):
    p=l.rstrip('\n').split('\t')
    if len(p)<4: continue
    d=d_of(p[0]); row=dict(id=f'BM{p[0]}{p[1]}',blog='부동산',date=d,time=p[1],title=p[3],kind=p[2],src='한달계획',links=p[4].split() if len(p)>4 else [])
    if p[1]=='19:00' and str(d) in swaps: pushed.append(row); continue
    B.append(row)
for r in bs:
    if not r['slot']: continue
    B.append(dict(id='BC'+r['slot']+r['title'][:6],blog='부동산',date=dt.date.fromisoformat(r['slot']),time='19:00',title=r['title'],kind=r['kind'],src='사이클',links=r['link'],why=r['why'],end=r['end']))
d0=dt.date(2026,11,20)
for k,r in enumerate(pushed): r['date']=d0+dt.timedelta(k); r['time']='07:00'; r['src']='한달계획(밀림)'; B.append(r)
for a in ov.get('_add',[]):  # 새로 더한 부동산 줄 (한달계획 · 사이클 밖)
    B.append(dict(id=a['id'],blog='부동산',date=dt.date.fromisoformat(a['date']),time=a['time'],title=a['title'],kind=a.get('kind','추가'),src='추가',links=a.get('links',[])))
for r in B:
    o=ov.get(r['id'])
    if isinstance(o,str): r['date']=dt.date.fromisoformat(o)
    elif isinstance(o,dict):
        if o.get('date'): r['date']=dt.date.fromisoformat(o['date'])
        if o.get('time'): r['time']=o['time']
        if o.get('title'): r['old_title']=r['title']; r['title']=o['title']
    r['status']=bd_status(r['title']) or '미발행'; r['fixed']=r['status'].startswith('발행')
# ── 짝 만들기 (사이클 글만)
NEED={'① 입주 · 분양가':r'중문','① 입주 · 잔금':r'사전점검','① 입주 · 전세':r'입주청소|줄눈|청소','② 2년차 · 전세 만기':r'하자|도배|실리콘|줄눈|2년',
      '③ 생활 · 수능':r'가벽|공부방|방 나누','③ 계절 · 겨울':r'단열|외풍|샷시 교체','③ 계절 · 이사철':r'입주청소|이사청소|도배','③ 생활 · 실거주':r'부분 인테리어|도배|필름',
      '③ 생활 · 신학기':r'가벽|방 나누|공부방','④ 15년+ 생활권':r'올수리|리모델링|배관 교체|구축','⑤ 주거 유형 · 임대차':r'원상복구|도배 비용|곰팡이|퇴실','⑥ 재정비 · 이주':r'이사|이주'}
SHARED={ # 같은 질문 · 같은 숫자 표 · 부동산이 맡는 것 · 인테리어가 맡는 것 · 넘기는 문장
 '① 입주 · 분양가':('옵션까지 넣으면 이 집은 실제로 얼마인가','옵션 포함 분양가 표(분양가 · 발코니 확장 · 옵션 중문 · 사제 중문)','분양가 · 같은 평형 실거래 · 옵션 포함 실제 금액','옵션 중문과 사제 중문 금액 차이 · 언제 다나','「옵션 중문 ○만원이 이 집 실제 분양가에 들어 있다 → 사제로 하면 얼마가 남나」'),
 '① 입주 · 잔금':('잔금 날 통장에 얼마가 있어야 하나','입주 준비 계산서(잔금 현금 + 청소 · 줄눈 · 중문 · 이사)','대출 · 취득세 · 현금 줄','사전점검 뒤 고칠 것과 입주 준비 품목 금액(제휴 공개 금액만)','「계산서 마지막 줄 입주 준비비 → 사전점검 날 무엇을 재 두나」'),
 '① 입주 · 전세':('세를 놓을까, 들어가 살까','두 갈래 표(세놓는 집 = 청소 · 줄눈 / 사는 집 = + 중문 · 탄성 · 매트)','입주 물량 · 첫 석 달 전세 · 옆 단지 선례','갈래마다 시공 범위 · 순서','「전세가 낮은 첫 석 달, 세놓는 집은 청소 · 줄눈만 → 사는 집은 이 순서」'),
 '② 2년차 · 전세 만기':('갱신할까, 새로 놓을까, 들어갈까','세 갈래 표(갱신 5% · 새 시세 · 실거주) × 손볼 것','갱신 상한 · 지금 전세 · 실거주 요건','하자보수 마감 전 점검 · 다시 세놓기 전 손볼 것 · 실거주 부분 인테리어','「새로 놓으면 ○억 → 그 전에 2년 하자 접수부터」'),
 '③ 생활 · 수능':('학군지로 옮기면 방을 어떻게 쓰나','학군지 84㎡ 전세 표 + 방 구성','학군지 전세 · 갱신','공부방 · 가벽 · 방 나누기 금액','「84㎡ 방 셋에 아이 둘 → 거실 가벽으로 방 하나 더」'),
 '③ 계절 · 겨울':('오래된 집 겨울 관리비, 고치면 몇 해 만에 돌아오나','관리비 차이 표 + 단열 공사 회수 햇수','연식별 겨울 관리비','단열 · 외풍 · 샷시 공사 금액','「한 해 ○만원 더 낸다 → 샷시는 ○년, 단열 필름은 ○년」'),
 '③ 계절 · 이사철':('1~2월 이사, 언제 무엇을 잡나','이사 달력(계약 · 대출 · 청소 · 이사)','이사철 전세 · 갱신','청소 · 도배 예약 시점','「잔금 날 2주 전 → 청소 · 도배 날짜 잡기」'),
 '③ 생활 · 실거주':('집주인이 들어갈 때 무엇부터','실거주 순서표(통보 · 갱신 거절 · 수리)','갱신 거절 요건 · 시점','들어가기 전 부분 인테리어 범위','「세입자 나간 날부터 입주까지 ○주 → 그 안에 끝낼 공사」'),
 '③ 생활 · 신학기':('3월 전에 이사하려면','신학기 이사 달력','학군지 전세 · 매매','방 나누기 · 중문','「1월 계약 → 2월 공사 → 3월 입학」'),
 '④ 15년+ 생활권':('구축을 사서 고치면 신축보다 얼마 싼가','구축 + 올수리 vs 같은 동네 신축 표','동네 구축 84㎡ 실거래 · 신축 실거래','평수별 올수리 · 배관 · 샷시 금액','「구축 ○억 + 올수리 ○천 = ○억 → 신축과 ○억 차이」'),
 '⑤ 주거 유형 · 임대차':('나갈 때 누가 내나','책임 표(통상 손모 · 세입자 몫 · 집주인 몫) × 실제 금액','계약 · 법 쪽 책임','도배 · 곰팡이 · 청소 실제 금액','「세입자 몫이면 공제 → 실제 공사 금액은 이 정도」'),
 '⑥ 재정비 · 이주':('이주 날짜에 맞춰 어디로, 언제 옮기나','이주 달력 + 근처 전세','이주 일정 · 이주비 · 근처 전세','이사 · 보관이사 · 이사청소','「이주 마감 ○월 → 이사 예약은 ○주 전」')}
ALIAS={'고양장항제일풍':['한강풍경채어바','장항제일풍경채','장항풍경채'],'한강풍경채어바':['고양장항제일풍','장항제일풍경채']}  # 이름 바뀐 같은 단지 (10/23 EBN · 고양 장항 제일풍경채 → 한강풍경채어바니티)
def dkey(t):
    m=re.match(r'(.+?)\s(분양가|잔금|전세|전세 만기|구축|학군지|1월|신학기|빌라|상가|오피스텔)',t); n=m.group(1) if m else t.split(',')[0]
    return re.sub(r'\(.*?\)|\s','',n)[:7]
pairs=[]; moves=[]; alerts=[]; IEND=max(r['date'] for r in I); later=[]
for b in [x for x in B if x.get('src')=='사이클']:
    pat=NEED.get(b['kind'],'.'); k=dkey(b['title']); per_dong=b['kind'][0] in '①②'
    def hit(t):
        t=t.split('(')[0]
        if not per_dong: t=re.sub(r'^\[.*?\]\s*','',t).split(',')[0]
        ks=[k]+ALIAS.get(k,[]); tt=re.sub(r'\s','',t)
        return re.search(pat,t) and not re.search(r'모집|제휴',t) and (not per_dong or any(x in tt for x in ks))
    pubhit=[(n,t) for n,t in IP if hit(t)]
    pid='P'+b['id'][2:]
    sched=[r for r in I if hit(r['title']) or f'(짝 {pid}' in r['title']]   # 이미 채운 짝 칸은 다시 채우지 않음
    due=b['date']-dt.timedelta(2)
    P=dict(id=pid,부동산=b['id'],부동산_날=str(b['date']),부동산_제목=b['title'],갈래=b['kind'])
    sh=SHARED.get(b['kind']); 
    if sh: P.update(같은질문=sh[0],같은표=sh[1],부동산몫=sh[2],인테리어몫=sh[3],넘기는문장=sh[4],공유숫자={})
    if per_dong and pubhit or (not per_dong and pubhit):
        P.update(인테리어='발행 '+pubhit[0][0],인테리어_제목=pubhit[0][1],판정='OK · 앞 글 발행됨')
    elif sched:
        r=min(sched,key=lambda r:r['date'])
        P.update(인테리어=r['id'],인테리어_날=str(r['date']),인테리어_제목=r['title'])
        if r['date']<=due: P['판정']='OK · 앞에 잡혀 있음'
        elif not r['fixed']:
            tgt=next((x for x in sorted(I,key=lambda x:-x['date'].toordinal()) if x['fill'] and b['date']-dt.timedelta(7)<=x['date']<=due),None)
            if tgt: moves.append(('swap',r['idx'],tgt['idx'])); tgt['fill']=False; P['판정']=f"옮김 · {r['date']} → {tgt['date']}"
            else: alerts.append(f"{b['title'][:30]}: 짝 인테리어가 {r['date']}로 늦음 · 옮길 빈 칸 없음"); P['판정']='늦음'
        else:
            alerts.append(f"{b['title'][:30]}: 짝 인테리어 {r['date']} 예약이라 못 옮김 → 부동산 글을 {r['date']+dt.timedelta(2)} 뒤로"); P['판정']='부동산 미룸 필요'
    else:
        tgt=next((x for x in sorted(I,key=lambda x:-x['date'].toordinal()) if x['fill'] and b['date']-dt.timedelta(7)<=x['date']<=due and x['date']>=T+dt.timedelta(2)),None)
        what=f"{k if per_dong else ''} {sh[3] if sh else b['kind']}".strip()
        if tgt:
            moves.append(('fill',tgt['idx'],f"[쓸 글] {what} (짝 {P['id']} · 부동산 {b['date']:%m/%d} 앞)")); tgt['fill']=False
            P.update(인테리어=tgt['id'],인테리어_날=str(tgt['date']),판정=f"새 칸 {tgt['date']}")
        else:
            gen=next((t for n,t in IP if re.search(pat,t)),None)
            P['판정']=('인테리어 일정 밖 → 주간 점검이 칸을 만들 때 짝부터' if b['date']-dt.timedelta(2)>IEND else '새 칸 없음 → 그 품목 기존 글로 잇기'+(f" ({gen[:24]})" if gen else ''))
            if b['date']-dt.timedelta(2)>IEND: later.append(b); continue
            alerts.append(f"{b['date']:%m/%d} {b['title'][:28]}: 앞에 낼 인테리어 칸 없음")
    pairs.append(P)
json.dump(pairs,open(M+'/pairs.json','w'),ensure_ascii=False,indent=1)
if MODE=='apply' and moves:
    shutil.copy(MS,MS+f'.bak{dt.datetime.now():%m%d_%H%M}_master')
    ms=json.load(open(MS))
    for m in moves:
        if m[0]=='swap':
            a,b_=ms[m[1]],ms[m[2]]
            for f in ('제목','메모','상태','성격','갈래'): a[f],b_[f]=b_.get(f,''),a.get(f,'')
        else: ms[m[1]]['제목']=m[2]; ms[m[1]]['메모']=(ms[m[1]].get('메모','')+' · 통합 일정 짝 칸').strip(' ·')
    json.dump(ms,open(MS,'w'),ensure_ascii=False,indent=1)
# ── 보기: 날마다 두 블로그 + 스레드
rows=[r for r in I+B if T<=r['date']<=T+dt.timedelta(days=42)]
pm={}; [pm.setdefault(p.get('인테리어'),p['id']) or pm.setdefault(p['부동산'],p['id']) for p in pairs]
for p in pairs: pm[p['부동산']]=p['id']; pm[p.get('인테리어')]=p['id']
o=[f'# 통합 일정표 ({T:%m/%d}~{T+dt.timedelta(42):%m/%d})','',f'만든 때 {dt.datetime.now():%Y-%m-%d %H:%M} · master.py {MODE}','',
 '- 원천은 그대로: 인테리어 = mix_schedule_1017c.json · 부동산 = 한달계획 + 사이클 일정(bd_plan.py). 이 표는 둘을 합쳐 보고 짝 · 앞뒤를 맞춘다.',
 '- 짝 칸(P…): 같은 질문 · 같은 표를 두 글이 나눠 쓴다(pairs.json). 인테리어 글이 부동산 글보다 2일 넘게 먼저 뜬다. 부동산 발행 다음 날 스레드 12:20.',
 '- 「예약…」 · 발행 칸은 움직이지 않는다.','']
if alerts or later: o+=['## 손볼 것','']+[f'- {a}' for a in alerts]+([f'- 인테리어 일정({IEND:%m/%d}까지) 밖 부동산 짝 {len(later)}편 — 주간 점검이 인테리어 칸을 늘릴 때 짝 칸을 먼저 넣는다.'] if later else [])+['']
o+=['## 짝 판정','','| 짝 | 부동산(날) | 같은 질문 | 인테리어 | 판정 |','|---|---|---|---|---|']
o+=[f"| {p['id'][:12]} | {p['부동산_날'][5:]} {p['부동산_제목'][:28]} | {p.get('같은질문','')} | {(p.get('인테리어_날','')[5:]+' '+p.get('인테리어_제목','')[:26]) if p.get('인테리어') else '-'} | {p['판정']} |" for p in pairs if dt.date.fromisoformat(p['부동산_날'])<=T+dt.timedelta(42)]
o+=['','## 날마다','','| 날 | 시각 | 블로그 | 글 | 상태 | 짝 |','|---|---|---|---|---|---|']
for r in sorted(rows,key=lambda r:(r['date'],r['time'],r['blog'])):
    o.append(f"| {r['date']:%m/%d} | {r['time']} | {r['blog']} | {r['title'][:52]} | {r['status'][:18]} | {pm.get(r['id'],'')[:12]} |")
    if r['blog']=='부동산' and r['id'] in pm: o.append(f"| {(r['date']+dt.timedelta(1)):%m/%d} | 12:20 | 스레드 | ↳ {r['title'].split(',')[0]} 숫자 한 줄 + 인테리어 | 대기열 | {pm[r['id']][:12]} |")
open(M+'/master_latest.md','w').write('\n'.join(o))
print(f'{MODE}: 인테리어 {len(I)} · 부동산 {len(B)} · 짝 {len(pairs)} · 옮김/채움 {len(moves)} · 손볼 것 {len(alerts)}'); print('\n'.join(o[:40]))

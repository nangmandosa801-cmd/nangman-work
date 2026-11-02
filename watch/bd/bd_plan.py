# 낭만 부동산 분석 플랫폼 · 사이클 글 일정 — python3 bd_plan.py [시작일] [주수]
# 규칙: 전략 doc 「부동산 블로그 연동」 절. 19시 칸 = 사이클 글(우선순위 ①~⑥), 07시 칸 = 미발행 원고.
import json,re,sys,datetime as dt,collections
W='/home/claude/watch'; T=dt.date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else dt.date.today()
WEEKS=int(sys.argv[2]) if len(sys.argv)>2 else 10; END=T+dt.timedelta(weeks=WEEKS)
SUDO=('서울','경기','인천')
GG='수원 성남 고양 용인 부천 안산 안양 남양주 화성 평택 의정부 시흥 파주 김포 광명 광주시 군포 하남 오산 이천 안성 의왕 양주 구리 포천 동두천 과천 여주 양평 가평 연천 동탄 운정 검단 위례 미사 감일 회천 옥정 산본 분당 일산 평촌 송도 청라 계양 부평 영종 지제 고덕 브레인시티'.split()
def sudo(x): s=(x.get('지역') or '')+' '+x['단지']; return s.split()[0] in SUDO or any(g in s for g in GG)
pub=open('/home/claude/proj/발행글_목록_부동산_인테리어.md').read()
bd_pub=pub.split('## 낭만 인테리어')[0]; int_pub=pub[len(bd_pub):]
def key(n): return re.sub(r'\(.*?\)|\s','',n)[:7]
def published(n,txt): return key(n) in re.sub(r'\s','',txt)
def int_link(n):
    k=key(n); out=[]
    for l in int_pub.splitlines():
        m=re.match(r'\|[^|]*\|\s*(\d{12})\s*\|\s*(.*?)\s*\|',l)
        if m and k in m.group(2).replace(' ',''): out.append(m.group(1))
    return out[:2]
# 한달계획(10/21~11/19)에 이미 잡힌 단지 — 겹쳐 잡지 않음
PLANNED={'신검단중앙역센트레빌':'10/26 · 10/31','풍경채어바니티':'10/27 · 10/30','등촌역':'11/1','회천중앙역':'11/11','올림픽파크포레온':'10/23','트리우스광명':'11/2','안양역푸르지오':'11/12','부평역해링턴':'11/17','디에이치방배':'11/10 · 11/14','래미안레벤투스':'11/15'}
def planned(n): nn=n.replace(' ',''); return next((v for k,v in PLANNED.items() if k[:5] in nn),None)
rows=[]
def add(d0,d1,pri,kind,title,link,why):
    if d1<T or d0>END: return
    rows.append(dict(start=max(d0,T),end=d1,pri=pri,kind=kind,title=title,link=link,why=why))
M=json.load(open(W+'/ipju_master.json'))['단지목록']
for x in M:
    if not x.get('입주시작') or not sudo(x): continue
    D=dt.date.fromisoformat(x['입주시작']); n=x['단지']; s=x.get('세대') or 0
    if planned(n) or re.search(r'임대|청년안심|행복주택',n): continue
    if x['구분']=='입주예정' and s>=500:
        L=int_link(n)
        for a,b,kind,t in [(-90,-75,'① 입주 · 분양가',f'{n} 분양가, ○○㎡ 분양가와 옆 단지 같은 평형 실거래 ○억'),
                           (-60,-45,'① 입주 · 잔금',f'{n} 잔금, 입주 {D.month}월 {D.day}일 시작이고 대출을 빼면 현금 ○억'),
                           (-45,-14,'① 입주 · 전세',f'{n} 전세, 입주 {s:,}세대가 한꺼번에 나오면 첫 석 달 전세 ○억')]:
            if published(n+kind[-2:],bd_pub): continue
            add(D+dt.timedelta(a),D+dt.timedelta(b),1,kind,t,L,f'D={D} · {s:,}세대')
    if x['구분']=='2년차' and s>=1000:
        y2=(x.get('시점') or {}).get('2년차') or {}
        if y2.get('시작'):
            add(dt.date.fromisoformat(y2['시작']),dt.date.fromisoformat(y2['끝']),2,'② 2년차 · 전세 만기',
                f'{n} 전세 만기, {D:%Y년 %-m월} 입주 {s:,}세대의 2년 계약이 몰리고 지금 전세 ○억',int_link(n),f'입주 {D} · {s:,}세대')
# ③ 계절 · 생활 고정점 (해마다 손봄)
FIX=[('2026-11-21','2026-11-27',3,'③ 생활 · 이사','손 없는 날(11/27 · 11/28) 이사, 주말 이사 몰리는 단지에서 이사비 ○만원 차이','이사 · 입주청소','손 없는 날 11/27 · 11/28 · 입동(11/7) 지난 첫 영하'),
     ('2026-11-16','2026-11-22',3,'③ 생활 · 수능','학군지 전세, 수능(11/19) 끝나고 움직이는 집 · 대치 · 목동 · 중계 84㎡ 전세 ○억','가벽 · 공부방 · 중문','수능 11/19 뒤 이사 문의'),
     ('2026-11-23','2026-11-30',3,'③ 계절 · 겨울','구축 아파트 난방비, 20년 넘은 단지와 새 아파트의 겨울 관리비 ○만원 차이','단열 · 외풍 · 샷시','첫 한파 · 관리비 고지'),
     ('2026-12-07','2026-12-13',3,'③ 계절 · 이사철','1월 이사 전세, 1~2월 이사철 앞 수도권 전세 갱신 · 신규 ○억','입주청소 · 도배','1~2월 이사 정점 3~4주 전'),
     ('2026-12-14','2026-12-20',3,'③ 생활 · 실거주','전세 만기 실거주, 집주인이 들어갈 때 갱신 거절 · 수리 순서','2년차 부분 인테리어','연말 만기'),
     ('2026-12-28','2027-01-03',3,'③ 생활 · 신학기','신학기 이사, 3월 입학 전 학군지 전세 · 매매 ○억','방 나누기 · 중문','1~2월 학군 이사')]
for a,b,p,k,t,l,w in FIX: add(dt.date.fromisoformat(a),dt.date.fromisoformat(b),p,k,t,[l],w)
# ④ 15년 이상 생활권 묶음 (사이클 장부 · 동 단위 · 최근 12개월 거래 많은 순)
C=json.load(open(W+'/cycle/apt_cycle.json'))['단지']; g=collections.defaultdict(lambda:[0,0,[]])
for c in C:
    if c['연차']>=15 and c.get('최근12개월매매'):
        tk=c['주소'].split(); i=next((j for j,t in enumerate(tk) if re.search(r'(동|읍|면|가)$',t) and j>=2),len(tk)-1); k=' '.join(tk[:i+1]); g[k][0]+=c['최근12개월매매']; g[k][1]+=1; g[k][2].append(c['단지'])
top=[k for k,v in sorted(g.items(),key=lambda kv:-kv[1][0]) if v[1]>=4 and not published(k.split()[-1],bd_pub)][:WEEKS]
wk=T+dt.timedelta(days=(3-T.weekday())%7)  # 목요일
for i,k in enumerate(top):
    d=wk+dt.timedelta(weeks=i); dong=k.split()[-1]; v=g[k]
    add(d,d+dt.timedelta(6),4,'④ 15년+ 생활권',f'{dong} 구축 아파트 시세, 15년 넘은 {v[1]}개 단지 84㎡ 실거래와 올수리 뒤 값 차이',['올수리 비용 · 배관 · 샷시'],f'{k} · 최근 12개월 {v[0]}건')
# ⑤ 다른 주거 유형 (임대차 책임 — 부동산 독자와 겹치는 말)
for a,t,l in [('2026-11-24','빌라 전세 원상복구, 나갈 때 도배 · 곰팡이는 누가 내나 — 보증금에서 빼는 범위','원룸 도배 비용 청구 · 곰팡이 책임'),
              ('2026-12-21','상가 원상복구 범위, 임대차 끝날 때 철거 · 바닥 · 간판은 누가','상가 원상복구'),
              ('2027-01-18','오피스텔 월세 퇴실 청소비, 계약서에 없으면 누가 내나','퇴실 청소 · 입주청소')]:
    d=dt.date.fromisoformat(a); add(d,d+dt.timedelta(6),5,'⑤ 주거 유형 · 임대차',t,[l],'자동완성 책임 말')
# ⑥ 재정비 (정비사업 장부 · 관리처분인가 → 이주 3개월 전)
J=json.load(open(W+'/jeongbi/jeongbi.json')).get('구역') or []
for z in J:
    if z.get('이주 시작'):
        d=dt.date.fromisoformat(z['이주 시작'][:10]); add(d-dt.timedelta(100),d-dt.timedelta(60),6,'⑥ 재정비 · 이주',f"{z['구역']} 이주, {d:%Y년 %-m월} 시작 · 근처 전세 ○억",['낭만 이사 · 이사청소'],z.get('확인정도',''))
# 칸 배정 — 19시 한 주 7칸 몫: ① 입주 3 · ② 2년차 1 · ③ 계절 · 생활 1 · ④ 15년+ 1 · ⑤⑥ 1 (모자라면 ① → ④ 순으로 채움)
# 11/19까지는 한달계획이 차 있으므로 창이 11/20 전에 닫히는 급한 글만, 한 주 2편까지 「바꿀 칸」(한달계획의 「같은 돈이면 어디 · 산 사람 손익표」 날)
MONTH_END=dt.date(2026,11,19)
SWAP=[dt.date(2026,m,d) for m,d in [(10,28),(10,29),(11,3),(11,5),(11,8),(11,10),(11,13),(11,15),(11,18)]]
QUOTA={1:3,2:1,3:1,4:1,5:1}
pool=sorted(rows,key=lambda r:(r['end'],r['pri'])); out=[]; used=set()
for r in sorted([r for r in pool if r['end']<=MONTH_END and r['pri']<=2],key=lambda r:(not r['link'],r['end'])):
    ok=lambda x: x not in used and r['start']<=x<=r['end'] and x>=T and sum(1 for u in used if u.isocalendar()[1]==x.isocalendar()[1])<2
    d=next((x for x in SWAP if ok(x)),None)
    if d: used.add(d); r['slot']=d; r['swap']=True; out.append(r); pool.remove(r)
day=max(T,MONTH_END+dt.timedelta(1))
while day<=END:
    wk=[day+dt.timedelta(i) for i in range(7) if day+dt.timedelta(i)<=END]; left=dict(QUOTA)
    for d in wk:
        cand=[r for r in pool if r['start']<=d<=r['end']]
        if not cand: continue
        def rank(r): p=r['pri'] if r['pri']<5 else 5; return (0 if left.get(p,0)>0 else 1, r['end'], r['pri'])
        r=min(cand,key=rank); p=r['pri'] if r['pri']<5 else 5; left[p]=left.get(p,0)-1
        r['slot']=d; out.append(r); pool.remove(r)
    day+=dt.timedelta(7)
for r in pool: r['slot']=None; out.append(r)
out.sort(key=lambda r:(r['slot'] or dt.date(2100,1,1)))

o=[f'# 낭만 부동산 사이클 글 일정 ({T:%m/%d}~{END:%m/%d})','',f'만든 때 {dt.datetime.now():%Y-%m-%d %H:%M} · bd_plan.py · 매주 월 08:40 점검이 다시 만든다.','',
 '- 19시 칸 = 사이클 글(우선 ① 입주 → ② 2년차 → ③ 계절 · 생활 → ④ 15년+ → ⑤ 임대차 → ⑥ 재정비). 07시 칸 = 미발행 원고 그대로.',
 f'- {MONTH_END:%m/%d}까지는 한달계획 19시 칸이 차 있다. 그 안에 든 줄은 「바꿀 칸」 — 같은 날 한달계획 19시 글을 뒤(11/20 뒤 빈 날)로 민다.',
 '- 앞뒤 규칙: 인테리어 글이 먼저 뜨고 2~5일 뒤 부동산 글이 그 글을 문단 안에서 건다. 다음 인테리어 글이 부동산 글을 건다(발행 글은 고치지 않으므로 늦게 내는 글이 앞 글을 건다).',
 '- 쓰는 날 = 발행 이틀 전. ○ 숫자는 쓸 때 실거래로 채운다. 매물 · 중개보수 말 없음. 인테리어 링크는 그 이야기 문단 바로 뒤 1~2개.','',
 '| 발행(19시) | 쓰는 날 | 갈래 | 제목(안) | 앞에 떠 있어야 할 인테리어 글 | 근거 |','|---|---|---|---|---|---|']
for r in [r for r in out if r['slot']]+[r for r in out if not r['slot']][:0]:
    s=r['slot']; mark=' · 바꿀 칸' if r.get('swap') else ''
    PART={'① 입주 · 분양가':'1편 중문','① 입주 · 잔금':'2편 사전점검','① 입주 · 전세':'3편 입주청소 · 줄눈','② 2년차 · 전세 만기':'6편 하자보수 · 도배'}
    if r['link'] and re.match(r'\d{12}',r['link'][0]): ln='발행 글 '+' · '.join(r['link'])
    else: ln=f"먼저 인테리어 「{PART.get(r['kind'], ' · '.join(r['link']))}」 글 {(s-dt.timedelta(3)).strftime('%m/%d') if s else ''} 발행(없으면 그 품목 기존 글)"
    o.append(f"| {(s.strftime('%m/%d')+mark) if s else '칸 없음'} | {(s-dt.timedelta(2)).strftime('%m/%d') if s else '-'} | {r['kind']} | {r['title']} | {ln} | {r['why']} |")
p='/home/claude/watch/bd/bd_schedule_latest.md'; open(p,'w').write('\n'.join(o))
json.dump([{**r,'start':str(r['start']),'end':str(r['end']),'slot':str(r['slot']) if r['slot'] else None} for r in out],open('/home/claude/watch/bd/bd_schedule.json','w'),ensure_ascii=False,indent=1)
miss=[r for r in out if not r['slot'] and r['end']>=T]
o+=['',f'칸이 모자라 이번 판에 못 넣은 글 {len(miss)}편 — 창이 닫힌 입주 글은 버리고, ③ · ④ · ⑤는 다음 판으로 넘어간다.']
open(p,'w').write('\n'.join(o)); print('\n'.join(o)); print(len(out),'rows')

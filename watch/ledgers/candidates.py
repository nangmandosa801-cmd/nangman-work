# 이번 주 글 후보 — 수요로만 고름(제휴 업체 유무는 보지 않음 · 사용자 10/22)
# 세 단위: ① 단지(입주 · 2년차 · 이주) ② 생활권 묶음(3년 이상 · 같은 동 단지 여럿) ③ 지역 + 문제(겨울 급한 문제)
import json,datetime as dt,re,subprocess,sys
from collections import defaultdict
W='/home/claude/watch'; T=dt.date.today()
mon=dt.date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else T
cyc=json.load(open(W+'/cycle/apt_cycle.json'))['단지']
ipju=json.load(open(W+'/ipju_master.json'))['단지목록']
out=['## 이번 주 글 후보 (수요 점수 · 제휴 유무는 보지 않음)','']
# ① 단지 — 입주 칸이 열린 곳(인테리어 6편 · 부동산 4편 표) · 세대수 큰 순
WIN=[('1편 중문',-90,-75),('2편 사전점검',-75,-62),('3편 청소 · 줄눈',-35,-30),('4편 직전',-7,0),('5편 직후',0,14)]
rows=[]
for x in ipju:
    if x.get('구분')!='입주예정' or not x.get('입주시작'): continue
    d=dt.date.fromisoformat(x['입주시작'])
    for nm,a,b in WIN:
        if d+dt.timedelta(a)<=mon+dt.timedelta(13) and mon<=d+dt.timedelta(b):
            rows.append((x.get('세대') or 0,x['단지'],x.get('지역') or '',x['입주시작'],nm))
rows.sort(reverse=True)
out+=['**① 단지 (입주 칸이 열린 곳 · 세대수 큰 순 · 2주)**','','| 단지 | 지역 | 세대 | 입주 | 칸 |','|---|---|---|---|---|']+[f'| {n} | {r} | {s} | {d} | {k} |' for s,n,r,d,k in rows[:15]]
# ② 생활권 묶음 — 15년 이상 · 같은 동 단지들의 최근 12개월 매매 합
g=defaultdict(list)
for x in cyc:
    if x['연차'] and x['연차']>=15: g[x['주소']].append(x)
grp=sorted(g.items(),key=lambda kv:-sum(y['최근12개월매매'] for y in kv[1]))
out+=['','**② 생활권 묶음 (15년 이상 · 동 단위 매매 합 큰 순)**','','| 동 | 매매 12개월 합 | 묶을 단지(거래 많은 셋) |','|---|---|---|']
for k,v in grp[:12]:
    v=sorted(v,key=lambda y:-y['최근12개월매매'])
    out.append(f"| {k} | {sum(y['최근12개월매매'] for y in v)} | {' · '.join(y['단지']+'('+str(y['건축'])+')' for y in v[:3])} |")
# ③ 지역 + 문제 — 10년 이상 매매가 많은 시군구(겨울: 보일러 · 동파 · 외풍 · 결로 · 샷시)
s=defaultdict(int)
for x in cyc:
    if x['연차'] and x['연차']>=10:
        a=x['주소'].split(); s[' '.join(a[:-1])]+=x['최근12개월매매']
top=sorted(s.items(),key=lambda kv:-kv[1])[:10]
out+=['','**③ 지역 + 문제 (10년 이상 · 시군구 매매 합 큰 순 · 겨울엔 보일러 · 동파 · 외풍 · 결로 · 샷시)**','','| 지역 | 매매 12개월 합 |','|---|---|']+[f'| {k} | {v} |' for k,v in top]
out+=['','- 빈자리 확인: 고른 후보는 쓰기 전에 「단지명(또는 동네) + 품목」 네이버 블로그 탭 상위 10을 보고, 오래된 글 · 작은 블로그만 있으면 쓰고 아니면 한 단계 좁은 말로 바꾼다.']
print('\n'.join(out))

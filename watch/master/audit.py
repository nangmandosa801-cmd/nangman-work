#!/usr/bin/env python3
"""스케줄 마스터 실행 점검: python3 audit.py [일수=3]
- 지난 칸인데 발행/예약 아님 → 밀림
- 앞으로 N일 칸: 도우미 링크 없음 · 원고 없음 · [쓸 글] 빈칸 · 금지어 · 제목 앞머리 자동완성(snap) 미확인
결과: audit_latest.md"""
import json, re, sys, datetime as dt, glob, os
W='/home/claude/watch'
N=int(sys.argv[1]) if len(sys.argv)>1 else 3
now=dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).replace(tzinfo=None)
rows=json.load(open(f'{W}/mix_schedule_1017c.json'))
BAN=['자리','어요','예요','고요','최고','프리미엄','가능성','헷갈','놓습니다','가정','까닭','견줘','%p','나갈','1위','값','기준','차례로','갈렸','갈라','갈린']
snaps=sorted(glob.glob(f'{W}/kw/snap_daily_*.json'))
sug=set()
for s in snaps[-3:]:
    for k,v in json.load(open(s)).items(): sug.update(x.lower() for x in v.get('sug',[])); sug.add(k.lower())
def when(r):
    d=r.get('날',''); t=r.get('시각','00:00') or '00:00'
    m=re.match(r'(\d+)/(\d+)',d)
    if not m: return None
    try: return dt.datetime(2026,int(m[1]),int(m[2]),*map(int,t.split(':')))
    except: return None
out={'밀림':[],'빈칸':[],'도우미없음':[],'금지어':[],'앞머리확인':[]}
for r in rows:
    w=when(r); st=r.get('상태',''); ti=r.get('제목',''); me=r.get('메모','')
    if not w or st.startswith(('발행','예약')) or '보류' in st: continue
    if w<now-dt.timedelta(days=7): continue
    tag=f"{r['날']} {r.get('시각','')} {ti[:45]}"
    if w<now: out['밀림'].append(tag); continue
    if w>now+dt.timedelta(days=N): continue
    if ti.startswith('[쓸 글]'): out['빈칸'].append(tag); continue
    if 'claude.ai/artifact' not in me: out['도우미없음'].append(tag)
    b=[x for x in BAN if x in ti]
    if b: out['금지어'].append(tag+' → '+','.join(b))
    head=ti.split(',')[0].strip().lower()
    if head not in sug: out['앞머리확인'].append(tag+f' (앞머리 「{head}」 최근 자동완성 기록에 없음)')
L=[f'# 스케줄 마스터 점검 {now:%m/%d %H:%M} · 앞으로 {N}일']
for k,v in out.items():
    L.append(f'\n## {k} ({len(v)})'); L+=['- '+x for x in v] or ['- 없음']
open(f'{W}/master/audit_latest.md','w').write('\n'.join(L)+'\n'); print('\n'.join(L))

# --apply: 밀린 칸을 모레부터 빈 시각으로 옮긴다(예약 · 발행 · 보류 칸은 안 건드림)
if '--apply' in sys.argv and out['밀림']:
    import shutil; shutil.copy(f'{W}/mix_schedule_1017c.json', f'{W}/mix_schedule_1017c.bak_audit{now:%m%d%H%M}')
    used={(when(r).date(),r.get('시각')) for r in rows if when(r)}
    HOURS=['08:00','12:00','14:00','16:00','18:00','20:00','22:00']
    moved=[]
    for r in rows:
        w=when(r); st=r.get('상태','')
        if not w or st.startswith(('발행','예약')) or '보류' in st or w>=now or w<now-dt.timedelta(days=7): continue
        if r.get('제목','').startswith('[새 시공]') or r.get('제목','').startswith('[쓸 글]'): continue
        d=(now+dt.timedelta(days=2)).date()
        while True:
            free=[h for h in HOURS if (d,h) not in used]
            if free: break
            d+=dt.timedelta(days=1)
        h=free[0]; used.add((d,h)); old=f"{r['날']} {r.get('시각')}"
        r['날']=f'{d.month}/{d.day}'; r['시각']=h; r['_d']=d.isoformat()
        r['메모']=r.get('메모','')+f' · {now:%m/%d} 점검: 밀림 {old} → {r["날"]} {h}'
        moved.append(f"{old} → {r['날']} {h} {r['제목'][:40]}")
    json.dump(rows,open(f'{W}/mix_schedule_1017c.json','w'),ensure_ascii=False,indent=1)
    print('\n## 옮김'); [print('- '+m) for m in moved]
    open(f'{W}/master/audit_latest.md','a').write('\n## 옮김\n'+'\n'.join('- '+m for m in moved)+'\n')

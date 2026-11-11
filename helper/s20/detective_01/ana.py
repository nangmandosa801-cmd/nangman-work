#!/usr/bin/env python3
"""실거래 탐정 1화 · 하남 창우동 부영 59㎡ — 숫자 재기. 후보는 /home/claude/tools/postkit/odd_deals.py 가 뽑은 odd.json.
다시 돌리기: python3 /home/claude/tools/postkit/odd_deals.py --from 202608 --to 202610 --out odd.json && python3 ana.py"""
import sys, glob, json, pandas as pd
sys.path.insert(0, '/home/claude/tools/postkit')
import odd_deals as o
R = '/home/claude/rtn/'
cur = o.prep(pd.concat([o.load_csv(f) for f in sorted(glob.glob(R + 'rawO/M_*_0801_1112.csv'))], ignore_index=True))
h = pd.concat([pd.read_pickle(R + 'M2025.pkl'), pd.read_pickle(R + 'M2026.pkl')], ignore_index=True)
h = o.prep(h[h['시군구'].astype(str).str.startswith(('서울특별시', '경기도', '인천광역시'))])
hist = pd.concat([h[h['계약년월'] < '202608'], cur], ignore_index=True)
d = cur[(cur['계약년월'] >= '202608') & (cur['계약년월'] <= '202610')]
J = {}
# 1. 부영 59.97
isb = lambda x: (x['시군구'] == '경기도 하남시 창우동') & (x['단지명'] == '부영') & (x['면k'] == 60)
b = hist[isb(hist)].sort_values('일')
J['buyoung_recent'] = [o.rec(r) for _, r in b[b['일'] >= '20260801'].iterrows()]
pv = b[(~b['해제']) & (b['일'] < '20260919')]
J['buyoung_prev'] = {'n': int(len(pv)), 'max': int(pv['금'].max()), 'max_day': pv.loc[pv['금'].idxmax(), '일'], 'from': pv['일'].min(),
                     'n_direct': int(pv['직'].sum())}
for nm, a, z in [('2025', '202501', '202512'), ('2026_1_7', '202601', '202607'), ('2026_8_10', '202608', '202610')]:
    x = b[(~b['해제']) & (~b['직']) & (b['계약년월'] >= a) & (b['계약년월'] <= z)]
    J['buyoung_' + nm] = {'n': int(len(x)), 'med': float(x['금'].median()), 'min': int(x['금'].min()), 'max': int(x['금'].max())}
x = b[(b['계약년월'] >= '202608') & (b['계약년월'] <= '202610')]
J['buyoung_810_all'] = {'n': int(len(x)), 'mean_all': float(x['금'].mean()), 'med_all': float(x['금'].median()),
                        'mean_clean': float(x[(~x['해제']) & (~x['직'])]['금'].mean()), 'med_clean': float(x[(~x['해제']) & (~x['직'])]['금'].median())}
x9 = b[b['계약년월'] == '202609']; J['buyoung_sep'] = [o.rec(r) for _, r in x9.iterrows()]
ba = hist[(hist['시군구'] == '경기도 하남시 창우동') & (hist['단지명'] == '부영')]
J['buyoung_all_areas'] = {str(k): int(v) for k, v in ba[ba['계약년월'] >= '202601']['면k'].value_counts().items()}
J['buyoung_build'] = str(b['건축년도'].iloc[0])
# 2. 하남 8~10월
hn = d[d['시군구'].str.startswith('경기도 하남시')]
c = hn[hn['해제']].copy()
c['간격'] = (pd.to_datetime(c['해제사유발생일']) - pd.to_datetime(c['일'])).dt.days
J['hanam'] = {'n': int(len(hn)), 'cancel': int(len(c)), 'direct': int((hn['직'] & ~hn['해제']).sum()), 'cancel_days_med': float(c['간격'].median()),
              'cancel_days': sorted(c['간격'].tolist()), 'cancel_list': [dict(o.rec(r), 단지=r['단지명'], 동=r['시군구'].split()[-1], 간격=int(r['간격'])) for _, r in c.sort_values('일').iterrows()]}
# 3. 수도권 8~10월
cc = d[d['해제']].copy(); cc['간격'] = (pd.to_datetime(cc['해제사유발생일']) - pd.to_datetime(cc['일'])).dt.days
J['sudo'] = {'n': int(len(d)), 'cancel': int(len(cc)), 'cancel_pct': round(len(cc) / len(d) * 100, 2), 'direct': int((d['직'] & ~d['해제']).sum()),
             'direct_pct': round((d['직'] & ~d['해제']).sum() / (~d['해제']).sum() * 100, 2), 'cancel_days_med': float(cc['간격'].median()),
             'cancel_over30': int((cc['간격'] > 30).sum()), 'cancel_le7': int((cc['간격'] <= 7).sum())}
# 직거래 vs 같은 단지 · 같은 면적 · 앞뒤 한 달 중개거래 중앙값(3층 넘는 것끼리 · 2건 넘게)
v = d[~d['해제']].copy(); v['mi'] = v['계약년월'].str[:4].astype(int) * 12 + v['계약년월'].str[4:].astype(int)
br = v[(~v['직']) & (v['층n'] > 2)]
grp = {k: g for k, g in br.groupby(['key', '면k'])}
ratios = []
for _, r in v[v['직'] & (v['층n'] > 2)].iterrows():
    g = grp.get((r['key'], r['면k']))
    if g is None: continue
    g = g[(g['mi'] - r['mi']).abs() <= 1]
    if len(g) < 2: continue
    ratios.append(r['금'] / g['금'].median() - 1)
s = pd.Series(ratios)
J['direct_cmp'] = {'n': int(len(s)), 'med': round(float(s.median()) * 100, 1), 'lt10': int((s <= -0.10).sum()), 'lt20': int((s <= -0.20).sum()), 'lt30': int((s <= -0.30).sum()),
                   'gt10': int((s >= 0.10).sum()), 'within5': int((s.abs() < 0.05).sum())}
# 같은 방법으로 중개거래끼리(자기 빼고) — 견줄 기준
ratios = []
for (k, mk), g in br.groupby(['key', '면k']):
    if len(g) < 3: continue
    for i, r in g.iterrows():
        gg = g.drop(i); gg = gg[(gg['mi'] - r['mi']).abs() <= 1]
        if len(gg) < 2: continue
        ratios.append(r['금'] / gg['금'].median() - 1)
s = pd.Series(ratios)
J['broker_cmp'] = {'n': int(len(s)), 'med': round(float(s.median()) * 100, 1), 'lt10': int((s <= -0.10).sum()), 'lt20': int((s <= -0.20).sum()), 'lt30': int((s <= -0.30).sum())}
O = json.load(open('odd.json'))
J['odd_meta'] = O['meta']
J['hanam_A'] = [x for x in O['A'] if x['시군구'].startswith('경기도 하남시')]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(J, ensure_ascii=False, indent=1))

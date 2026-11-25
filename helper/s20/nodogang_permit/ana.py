#!/usr/bin/env python3
"""보도 숫자 뒤집어 보기 3호 · 노도강 아파트 매매 — 보도(서울경제 2026-11-24)는 토지거래허가 신청 건수를 셌다. 같은 달을 실거래 신고(계약일)로 다시 센다.
자료: python3 /home/claude/tools/postkit/rt_refresh.py (2026-11-26 05시 국토부에서 받음 · 수도권 아파트 매매 · 2026년 8월 1일~11월 25일 계약) → /home/claude/rtn/keep/M_latest_1126.pkl(저장소 밖)
건수 = 해제사유발생일이 없는 거래(직거래 포함 · 허가 신청과 견주려고). 값 견줌 = 중개거래만.
ana.json 은 받은 날 값 그대로 둔다(다시 받으면 11월 숫자가 늘어남)."""
import json, pandas as pd, numpy as np
m = pd.read_pickle('/home/claude/rtn/keep/M_latest_1126.pkl').reset_index(drop=True)
m['p'] = m['거래금액(만원)'].str.replace(',', '').astype(int); m['a'] = m['전용면적(㎡)'].astype(float)
m['d'] = pd.to_datetime(m['계약년월'] + m['계약일'].str.zfill(2), format='%Y%m%d'); m['x'] = m['해제사유발생일'] != '-'; m['ym'] = m['계약년월']
s = m[m['시군구'].str.startswith('서울')].copy(); s['gu'] = s['시군구'].str.split().str[1]
live = s[~s.x]
NDG = ['노원구', '도봉구', '강북구']; G3 = ['강남구', '서초구', '송파구']
n = live[live.gu.isin(NDG)]; g = live[live.gu.isin(G3)]
cnt = lambda df: {k: int(v) for k, v in df.groupby('ym').size().items()}
pct = lambda a, b: round((a / b - 1) * 100, 1)
J = {'meta': {'src': 'M_latest_1126.pkl', 'first': str(m.d.min().date()), 'last': str(m.d.max().date()), 'n_seoul_live': int(len(live)),
              'ndg_cancel': cnt(s[s.x & s.gu.isin(NDG)]), 'ndg_direct': cnt(n[n['거래유형'] == '직거래'])}}
J['news'] = {'ndg_apply': {'202608': 790, '202609': 904, '202611_est': 610}, 'seoul_apply_1_23': {'202610': 3569, '202611': 2763}, 'seoul_apply_aug': 3570,
             'g3_apply': {'202608': 368, '202609': 517, '202610': 629}, 'nowon_apply_1_23': {'202610': 389, '202611': 280}}
J['ndg'] = cnt(n); J['g3'] = cnt(g); J['seoul'] = cnt(live)
J['ndg_gu'] = {k: cnt(n[n.gu == k]) for k in NDG}
J['chg'] = {'apply_9': pct(904, 790), 'deal_9': pct(J['ndg']['202609'], J['ndg']['202608']), 'deal_10': pct(J['ndg']['202610'], J['ndg']['202609']),
            'deal_10_vs_8': pct(J['ndg']['202610'], J['ndg']['202608']), 'apply_11_vs_9': pct(610, 904), 'apply_11_vs_8': pct(610, 790),
            'g3_apply_9': pct(517, 368), 'g3_deal_9': pct(J['g3']['202609'], J['g3']['202608']), 'g3_apply_10': pct(629, 517), 'g3_deal_10': pct(J['g3']['202610'], J['g3']['202609'])}
# 11월: 열흘 단위(신고 기한 30일)
nn = n.assign(dec=(n.d.dt.day.clip(upper=30) - 1) // 10)
J['ndg_dec'] = {ym: {str(int(k)): int(v) for k, v in nn[nn.ym == ym].groupby('dec').size().items()} for ym in ['202610', '202611']}
# 15억 이하 · 초과(서울)
J['band'] = {b: cnt(live[(live.p <= 150000) == (b == 'le15')]) for b in ['le15', 'gt15']}
# 값: 10월 · 11월 중개거래를 같은 단지 · 같은 면적(㎡ 반올림)의 8~9월 중개거래(2건 이상) 가운데 값 · 최고값과 견줌
b = n[n['거래유형'] == '중개거래'].copy(); b['k'] = b['시군구'] + '|' + b['번지'] + '|' + b['단지명'] + '|' + b.a.round().astype(int).astype(str)
e = b[b.ym.isin(['202608', '202609'])].groupby('k').p.agg(['max', 'median', 'size'])
J['price'] = {}
for ym in ['202610', '202611']:
    l = b[b.ym == ym].join(e, on='k', how='inner'); l = l[l['size'] >= 2]
    J['price'][ym] = {'n': int(len(l)), 'ge_max': round((l.p >= l['max']).mean() * 100, 1), 'ge_max_n': int((l.p >= l['max']).sum()), 'gt_med': round((l.p > l['median']).mean() * 100, 1),
                      'gt_med_n': int((l.p > l['median']).sum()), 'lt_med_n': int((l.p < l['median']).sum()), 'med_diff': float((l.p - l['median']).median())}
J['ndg_med'] = {k: float(v) for k, v in b.groupby('ym').p.median().items()}
h = m[m['시군구'].str.contains('하남시') & ~m.x]; J['hanam'] = cnt(h)
# 한 건: 10월 노도강 중개거래 가운데 8~9월 같은 단지 · 면적 거래가 가장 많은 묶음
l = b[b.ym == '202610'].join(e, on='k', how='inner'); top = l.groupby('k').size().sort_values(ascending=False).head(5)
J['case'] = []
for k in top.index:
    q = b[b.k == k].sort_values('d')
    J['case'].append({'k': k, 'n': cnt(q), 'med': {a: float(v) for a, v in q.groupby('ym').p.median().items()}, 'max': {a: int(v) for a, v in q.groupby('ym').p.max().items()},
                      'min': {a: int(v) for a, v in q.groupby('ym').p.min().items()}, 'area': sorted(set(q['전용면적(㎡)'])), 'yr': q['건축년도'].iloc[0]})
json.dump(J, open('ana.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(json.dumps({k: J[k] for k in ['ndg', 'g3', 'seoul', 'chg', 'ndg_dec', 'band', 'price', 'ndg_med', 'hanam', 'ndg_gu']}, ensure_ascii=False))
for c in J['case']: print(c)

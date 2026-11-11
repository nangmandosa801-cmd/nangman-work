#!/usr/bin/env python3
"""하남 이번 주 · 전세 재계약 인상률 — 갱신요구권 쓴 계약 vs 안 쓴 계약.
다시 돌리기: cd /home/claude/rtn && python3 dl_hanam_rent26.py && python3 -c "from load import load;import glob;load(sorted(glob.glob('rawH/RH2026_*.csv'))[-1]).to_pickle('RH2026_hanam.pkl')" ; python3 ana.py"""
import json, pandas as pd, numpy as np
d = pd.read_pickle('/home/claude/rtn/RH2026_hanam.pkl')
for c in ['보증금(만원)', '월세금(만원)', '종전계약 보증금(만원)', '종전계약 월세(만원)']:
    d[c] = pd.to_numeric(d[c].astype(str).str.replace(',', '').str.strip().replace('-', np.nan), errors='coerce')
d['면'] = d['전용면적(㎡)'].astype(float); d['일'] = d['계약년월'].astype(str) + d['계약일'].astype(str).str.zfill(2)
d['동'] = d['시군구'].str.split().str[-1]
J = {'n': int(len(d)), 'last': d['일'].max(), 'renew': int((d['계약구분'] == '갱신').sum()), 'new': int((d['계약구분'] == '신규').sum()),
     'none': int((d['계약구분'] == '-').sum()), 'use': int((d['갱신요구권 사용'] == '사용').sum())}
g = d[d['계약구분'] == '갱신'].copy()
J['renew_by_type'] = {k: int(v) for k, v in g['전월세구분'].value_counts().items()}
J['renew_use_by_type'] = {f'{a}|{b}': int(v) for (a, b), v in g.groupby(['전월세구분', '갱신요구권 사용']).size().items()}
# 순수 전세 → 순수 전세 (지금 · 예전 둘 다 월세 0) · 예전 보증금 있음
j = g[(g['월세금(만원)'].fillna(0) == 0) & (g['종전계약 월세(만원)'].fillna(0) == 0) & (g['종전계약 보증금(만원)'] > 0)].copy()
j['율'] = j['보증금(만원)'] / j['종전계약 보증금(만원)'] - 1; j['차'] = j['보증금(만원)'] - j['종전계약 보증금(만원)']
j['쓴'] = j['갱신요구권 사용'] == '사용'
J['jeonse_n'] = int(len(j))
def st(x):
    return {'n': int(len(x)), 'med_pct': round(float(x['율'].median()) * 100, 2), 'mean_pct': round(float(x['율'].mean()) * 100, 2),
            'med_won': int(x['차'].median()), 'up': int((x['율'] > 0.0001).sum()), 'same': int((x['율'].abs() <= 0.0001).sum()),
            'down': int((x['율'] < -0.0001).sum()), 'over5': int((x['율'] > 0.0501).sum()), 'eq5': int(((x['율'] > 0.0001) & (x['율'] <= 0.0501)).sum()),
            'over10': int((x['율'] > 0.1001).sum()), 'over20': int((x['율'] > 0.2001).sum()),
            'up_pct': round((x['율'] > 0.0001).mean() * 100, 1), 'same_pct': round((x['율'].abs() <= 0.0001).mean() * 100, 1),
            'down_pct': round((x['율'] < -0.0001).mean() * 100, 1), 'over5_pct': round((x['율'] > 0.0501).mean() * 100, 1),
            'med_old': int(x['종전계약 보증금(만원)'].median()), 'med_new': int(x['보증금(만원)'].median())}
J['use'] = st(j[j['쓴']]); J['nouse'] = st(j[~j['쓴']]); J['all'] = st(j)
# 올린 계약만의 중앙 인상률
J['use_upmed'] = round(float(j[j['쓴'] & (j['율'] > 0.0001)]['율'].median()) * 100, 2)
J['nouse_upmed'] = round(float(j[~j['쓴'] & (j['율'] > 0.0001)]['율'].median()) * 100, 2)
# 면적대
j['면대'] = pd.cut(j['면'], [0, 50, 65, 90, 300], labels=['50㎡ 아래', '59㎡ 안팎', '84㎡ 안팎', '90㎡ 넘게'])
J['by_area'] = {str(k): {'use': st(x[x['쓴']]) if x['쓴'].sum() else None, 'nouse': st(x[~x['쓴']]) if (~x['쓴']).sum() else None} for k, x in j.groupby('면대', observed=True)}
# 동별(30건 넘는 곳)
J['by_dong'] = {k: st(x) for k, x in j.groupby('동') if len(x) >= 30}
# 월별 중앙값
J['by_month'] = {k: {'use': round(float(x[x['쓴']]['율'].median()) * 100, 2) if x['쓴'].sum() else None,
                     'nouse': round(float(x[~x['쓴']]['율'].median()) * 100, 2) if (~x['쓴']).sum() else None, 'n': int(len(x))} for k, x in j.groupby('계약년월')}
# 같은 단지 · 같은 면적 신규 전세 중앙값과 비교(같은 달 앞뒤 한 달)
n = d[(d['계약구분'] == '신규') & (d['월세금(만원)'].fillna(0) == 0)].copy()
n['mi'] = n['계약년월'].astype(str).str[:4].astype(int) * 12 + n['계약년월'].astype(str).str[4:].astype(int)
j['mi'] = j['계약년월'].astype(str).str[:4].astype(int) * 12 + j['계약년월'].astype(str).str[4:].astype(int)
n['k'] = n['시군구'] + '|' + n['단지명'] + '|' + n['면'].round(0).astype(int).astype(str)
j['k'] = j['시군구'] + '|' + j['단지명'] + '|' + j['면'].round(0).astype(int).astype(str)
gn = {k: x for k, x in n.groupby('k')}
gaps = []
for i, r in j.iterrows():
    x = gn.get(r['k'])
    if x is None: continue
    x = x[(x['mi'] - r['mi']).abs() <= 1]
    if len(x) < 2: continue
    gaps.append((i, float(x['보증금(만원)'].median()), int(len(x))))
gp = pd.DataFrame(gaps, columns=['i', 'newmed', 'nn']).set_index('i'); jj = j.join(gp, how='inner')
jj['싸게'] = jj['newmed'] - jj['보증금(만원)']; jj['싸게율'] = jj['보증금(만원)'] / jj['newmed'] - 1
J['vs_new'] = {lab: {'n': int(len(x)), 'med_gap': int(x['싸게'].median()), 'med_gap_pct': round(float(x['싸게율'].median()) * 100, 1),
                     'med_new': int(x['newmed'].median()), 'med_renew': int(x['보증금(만원)'].median())}
               for lab, x in (('use', jj[jj['쓴']]), ('nouse', jj[~jj['쓴']]), ('all', jj))}
# 계기판 4칸(2026 1~10월 · 이번 주 전 기준): 전세 갱신 건수 · 갱신 중 5% 넘게 올린 비율 · 내린 비율 · 갱신요구권 사용 비율
J['dash'] = {'renew_jeonse': J['jeonse_n'], 'use_share': round(j['쓴'].mean() * 100, 1), 'over5_nouse_pct': J['nouse']['over5_pct'], 'down_all_pct': J['all']['down_pct']}
# 이야기용: 84㎡ 안팎 · 같은 단지에서 쓴 계약과 안 쓴 계약이 둘 다 많은 단지
cand = []
for (k), x in j[(j['면'] >= 83) & (j['면'] <= 86)].groupby('k'):
    a, b = x[x['쓴']], x[~x['쓴']]
    if len(a) >= 5 and len(b) >= 5:
        cand.append({'k': k, 'n_use': len(a), 'n_no': len(b), 'use_med': round(float(a['율'].median()) * 100, 2), 'no_med': round(float(b['율'].median()) * 100, 2),
                     'use_old': int(a['종전계약 보증금(만원)'].median()), 'use_new': int(a['보증금(만원)'].median()), 'no_old': int(b['종전계약 보증금(만원)'].median()), 'no_new': int(b['보증금(만원)'].median()),
                     'new_med': int(n[n['k'] == k]['보증금(만원)'].median()) if (n['k'] == k).any() else None, 'new_n': int((n['k'] == k).sum())})
J['cand'] = sorted(cand, key=lambda c: -(c['n_use'] + c['n_no']))[:12]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1, default=str)
print(json.dumps({k: v for k, v in J.items() if k not in ('cand', 'by_dong', 'by_area')}, ensure_ascii=False))
for c in J['cand']: print(c)
print(json.dumps(J['by_area'], ensure_ascii=False)[:1500])
# 상반기 · 하반기 안 쓴 계약 · 쓴 계약 비율
for lab, a, z in (('m1_4', '202601', '202604'), ('m5_11', '202605', '202611')):
    x = j[(j['계약년월'].astype(str) >= a) & (j['계약년월'].astype(str) <= z)]
    J[lab] = {'n': int(len(x)), 'use_share': round(x['쓴'].mean() * 100, 1), 'nouse': st(x[~x['쓴']])}
# 위례롯데캐슬 84.98 2026 전체
w = j[j['k'] == '경기도 하남시 학암동|위례롯데캐슬|85']; wn = n[n['k'] == '경기도 하남시 학암동|위례롯데캐슬|85']
J['wirye'] = {'use': st(w[w['쓴']]), 'nouse': st(w[~w['쓴']]), 'new_n': int(len(wn)), 'new_med': int(wn['보증금(만원)'].median()),
              'new_oct_med': int(wn[wn['계약년월'].astype(str) == '202610']['보증금(만원)'].median()), 'new_oct_n': int((wn['계약년월'].astype(str) == '202610').sum())}
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1, default=str)
print(J['m1_4']['n'], J['m1_4']['use_share'], J['m1_4']['nouse']['med_pct'], J['m1_4']['nouse']['over5_pct'])
print(J['m5_11']['n'], J['m5_11']['use_share'], J['m5_11']['nouse']['med_pct'], J['m5_11']['nouse']['over5_pct'])
print(json.dumps(J['wirye'], ensure_ascii=False))
print(json.dumps(J['by_area']['84㎡ 안팎']['nouse'], ensure_ascii=False))

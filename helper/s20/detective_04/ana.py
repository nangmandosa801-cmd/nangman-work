#!/usr/bin/env python3
"""실거래 탐정 4화 · 아파트 직거래 가격 — 직거래는 같은 단지 중개거래보다 얼마나 싸게 신고됐나.
자료: python3 /home/claude/tools/postkit/odd_deals.py --from 202609 --to 202611 --fetch (2026-11-18 05시 받음 · 파일 이름은 _1117 · 마지막 계약일 11월 17일)
개인 직거래 = 거래유형 직거래 · 매수자와 매도자가 모두 개인 · 해제 뺌 · 묶음(같은 날 한 단지 직거래 10건 이상) 뺌.
견줌 = 같은 단지 · 같은 면적(㎡ 반올림) · 계약일 앞뒤 30일 · 3층 이상 · 개인끼리 중개거래 2건 이상의 가운데 값. 견줄 거래 자신은 뺀다.
ana.json 은 받은 날 값 그대로 둔다(다시 받으면 숫자가 바뀜)."""
import sys, glob, json, pandas as pd, numpy as np
sys.path.insert(0, '/home/claude/tools/postkit')
import odd_deals as o
fs = sorted(glob.glob('/home/claude/rtn/rawO/M_*_202609_202611_1117.csv'))
cur = o.prep(pd.concat([o.load_csv(f) for f in fs], ignore_index=True))
v = cur[~cur['해제']].copy().reset_index(drop=True)
g = v[v['직']].groupby(['key', '일']).size(); bk = set(g[g >= 10].index)
v['묶음'] = pd.Series([(k, d) in bk for k, d in zip(v['key'], v['일'])], index=v.index) & v['직']
v['개인끼리'] = (v['매수자'] == '개인') & (v['매도자'] == '개인')
v['dt'] = pd.to_datetime(v['일'])
v['m2'] = v['면'].round().astype(int)
J = {'meta': {'files': [f.split('/')[-1] for f in fs], 'n_all': int(len(cur)), 'n_valid': int(len(v)), 'last': cur['일'].max()}}
J['direct'] = {'n': int(v['직'].sum()), '묶음': int(v['묶음'].sum()), '개인': int((v['직'] & v['개인끼리'] & ~v['묶음']).sum()),
               '그밖': int((v['직'] & ~v['개인끼리'] & ~v['묶음']).sum()), '중개개인': int((~v['직'] & v['개인끼리']).sum())}
base = v[v['개인끼리'] & ~v['묶음'] & (v['층n'] >= 3)].copy()
comp = base[~base['직']]
grp = {k: x for k, x in comp.groupby(['key', 'm2'])}
def cmpr(r):
    x = grp.get((r['key'], r['m2']))
    if x is None: return (np.nan, 0)
    x = x[(x.index != r.name) & ((x['dt'] - r['dt']).abs() <= pd.Timedelta(days=30))]
    return (float(x['금'].median()), len(x)) if len(x) >= 2 else (np.nan, len(x))
t = base.apply(cmpr, axis=1, result_type='expand'); base['med'] = t[0]; base['nc'] = t[1]
c = base[base['med'].notna()].copy(); c['gap'] = c['금'] - c['med']; c['rate'] = (c['gap'] / c['med'] * 100).round(1)
def dist(x):
    n = len(x); f = lambda m: int(m.sum())
    tax = (x['rate'] <= -30) | (x['gap'] <= -30000)
    return {'n': n, '비쌈': f(x['rate'] > 0), '같음': f(x['rate'] == 0), '0~5': f((x['rate'] < 0) & (x['rate'] > -5)), '5~15': f((x['rate'] <= -5) & (x['rate'] > -15)), '15~30': f((x['rate'] <= -15) & (x['rate'] > -30)), '30이상': f(x['rate'] <= -30),
            '싼': f(x['rate'] < 0), '5%넘게싼': f(x['rate'] <= -5), '15%넘게싼': f(x['rate'] <= -15), '3억넘게싼': f(x['gap'] <= -30000), '30%또는3억': f(tax), '5%또는3억': f((x['rate'] <= -5) | (x['gap'] <= -30000)),
            'med_rate': float(x['rate'].median()), 'med_gap': float(x['gap'].median())}
D = c[c['직']]; M = c[~c['직']]
J['dist'] = {'직': dist(D), '중개': dist(M)}
J['cover'] = {'직_3층이상': int(base['직'].sum()), '직_견줌': int(len(D)), '중개_견줌': int(len(M))}
top = D.sort_values('gap').head(12)
J['top'] = [{'시군구': r['시군구'], '단지': r['단지명'], '면': float(r['면']), '층': int(r['층n']), '일': r['일'], '금': int(r['금']), 'med': int(r['med']), 'nc': int(r['nc']), 'gap': int(r['gap']), 'rate': float(r['rate']), '등기': r['등기일자']} for _, r in top.iterrows()]
top2 = D.sort_values('rate').head(8)
J['top_rate'] = [{'시군구': r['시군구'], '단지': r['단지명'], '면': float(r['면']), '층': int(r['층n']), '일': r['일'], '금': int(r['금']), 'med': int(r['med']), 'nc': int(r['nc']), 'gap': int(r['gap']), 'rate': float(r['rate'])} for _, r in top2.iterrows()]
# 세법 기준을 넘는 직거래의 시도 · 금액대
tx = D[(D['rate'] <= -30) | (D['gap'] <= -30000)]
J['tax'] = {'n': int(len(tx)), '시도': tx['시군구'].str.split().str[0].value_counts().to_dict(), 'med가운데': float(tx['med'].median()), 'gap가운데': float(tx['gap'].median()), 'gap합억': round(float(-tx['gap'].sum()) / 10000, 1)}
# 분당 매화마을공무원2 59㎡ 견준 거래
r0 = D[(D['단지명'] == '매화마을공무원2')].sort_values('gap').iloc[0]
x = grp[(r0['key'], r0['m2'])]; x = x[(x['dt'] - r0['dt']).abs() <= pd.Timedelta(days=30)].sort_values('일')
J['case'] = {'일': r0['일'], '면': float(r0['면']), '층': int(r0['층n']), '금': int(r0['금']), 'med': int(r0['med']), 'gap': int(r0['gap']), 'rate': float(r0['rate']), '등기': r0['등기일자'], '건축': str(r0['건축년도']),
             'comps': [{'일': a['일'], '면': float(a['면']), '층': int(a['층n']), '금': int(a['금'])} for _, a in x.iterrows()]}
# 시도별 개인 직거래 비중
pp = v[v['개인끼리'] & ~v['묶음']]; pp = pp.assign(시도=pp['시군구'].str.split().str[0])
J['sido'] = {k: {'n': int(len(x)), '직': int(x['직'].sum()), 'share': round(x['직'].mean() * 100, 1)} for k, x in pp.groupby('시도')}
J['all_share'] = round(pp['직'].mean() * 100, 1); J['pp_n'] = int(len(pp))
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(J, ensure_ascii=False))

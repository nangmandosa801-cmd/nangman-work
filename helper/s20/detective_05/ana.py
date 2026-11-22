#!/usr/bin/env python3
"""실거래 탐정 5화 · 실거래가 취소 재등록 — 해제된 거래 가운데 같은 단지 · 같은 면적 · 같은 층이 다시 신고된 건을 센다.
자료: python3 /home/claude/tools/postkit/rt_refresh.py (2026-11-23 05시 국토부에서 받음 · 수도권 아파트 매매 · 2026년 8월 1일~11월 계약) → /home/claude/rtn/keep/M_latest_1123.pkl(저장소 밖)
해제 = 해제사유발생일이 있는 거래. 짝 = 시군구 · 번지 · 단지명 · 전용면적 · 층이 같고 해제되지 않은 거래(해제 기록에는 동이 없어 같은 집이라고 못박을 수는 없다 → 글에서는 「같은 단지 · 같은 면적 · 같은 층」).
한 해제 건에 짝 하나(1:1) · 먼저 계약일과 금액이 모두 같은 짝(A) → 남은 것 가운데 계약일이 같거나 뒤인 가장 가까운 짝(B) → 없으면 C.
ana.json 은 받은 날 값 그대로 둔다(다시 받으면 숫자가 바뀜)."""
import json, pandas as pd, numpy as np
m = pd.read_pickle('/home/claude/rtn/keep/M_latest_1123.pkl').reset_index(drop=True)
m['p'] = m['거래금액(만원)'].str.replace(',', '').astype(int)
m['a'] = m['전용면적(㎡)'].astype(float)
m['d'] = pd.to_datetime(m['계약년월'] + m['계약일'].str.zfill(2), format='%Y%m%d')
m['x'] = m['해제사유발생일'] != '-'
m['xd'] = pd.to_datetime(m['해제사유발생일'].where(m['x']), format='%Y%m%d', errors='coerce')
m['시도'] = m['시군구'].str.split().str[0]
KEY = ['시군구', '번지', '단지명', '전용면적(㎡)', '층']
m['k'] = m[KEY].agg('|'.join, axis=1)
c = m[m.x].sort_values('d'); live = m[~m.x]
lg = {k: g for k, g in live.groupby('k')}
used = set(); res = {}
for i, r in c.iterrows():                      # A: 같은 계약일 · 같은 값
    g = lg.get(r.k)
    if g is None: continue
    t = g[(g.d == r.d) & (g.p == r.p) & (~g.index.isin(used))]
    if len(t): used.add(t.index[0]); res[i] = ('A', t.index[0])
for i, r in c.iterrows():                      # B: 계약일이 같거나 뒤 · 가장 가까운 짝
    if i in res: continue
    g = lg.get(r.k)
    if g is None: continue
    t = g[(g.d >= r.d) & (~g.index.isin(used))].sort_values('d')
    if len(t): used.add(t.index[0]); res[i] = ('B', t.index[0])
c = c.assign(cat=[res.get(i, ('C', None))[0] for i in c.index], mate=[res.get(i, ('C', None))[1] for i in c.index])
c['wait'] = (c.xd - c.d).dt.days
B = c[c.cat == 'B'].copy(); B['p2'] = live.loc[B.mate, 'p'].values; B['d2'] = live.loc[B.mate, 'd'].values
B['dp'] = B.p2 - B.p; B['gap'] = (B.d2 - B.d).dt.days
n = len(c); f = lambda x: int(x)
J = {'meta': {'src': 'M_latest_1123.pkl', 'n_all': f(len(m)), 'n_live': f(len(live)), 'n_cancel': n, 'share': round(n / len(m) * 100, 1),
              'first': str(m.d.min().date()), 'last': str(m.d.max().date()), 'ym_all': m['계약년월'].value_counts().sort_index().to_dict(),
              'ym_cancel': c['계약년월'].value_counts().sort_index().to_dict()}}
J['cat'] = {k: f((c.cat == k).sum()) for k in 'ABC'}
J['cat_pct'] = {k: round((c.cat == k).mean() * 100, 1) for k in 'ABC'}
J['re'] = f((c.cat != 'C').sum()); J['re_pct'] = round((c.cat != 'C').mean() * 100, 1)
J['B'] = {'n': f(len(B)), '같은값': f((B.dp == 0).sum()), '오름': f((B.dp > 0).sum()), '내림': f((B.dp < 0).sum()),
          '같은날_값만다름': f(((B.gap == 0) & (B.dp != 0)).sum()), '날만다름_값같음': f(((B.gap > 0) & (B.dp == 0)).sum()), '둘다다름': f(((B.gap > 0) & (B.dp != 0)).sum()),
          'gap_med': float(B.gap.median()), 'up_med': float(B[B.dp > 0].dp.median()), 'dn_med': float(B[B.dp < 0].dp.median()),
          'up_1억넘게': f((B.dp >= 10000).sum()), 'dn_1억넘게': f((B.dp <= -10000).sum())}
J['wait'] = {k: {'med': float(c[c.cat == k].wait.median()), 'd7': round((c[c.cat == k].wait <= 7).mean() * 100, 1), 'd30넘게': round((c[c.cat == k].wait > 30).mean() * 100, 1)} for k in 'ABC'}
J['wait_all_med'] = float(c.wait.median())
C = c[c.cat == 'C'].copy()
# 사라진 거래: 같은 단지 · 같은 면적(㎡ 반올림) · 앞뒤 30일 · 살아 있는 중개거래 2건 이상의 가운데 값과 견줌
live2 = live[live['거래유형'] == '중개거래'].assign(m2=live.a.round().astype(int)); live2['ck'] = live2[['시군구', '번지', '단지명']].agg('|'.join, axis=1)
gg = {k: g for k, g in live2.groupby(['ck', 'm2'])}
def cmpr(r):
    g = gg.get(('|'.join([r['시군구'], r['번지'], r['단지명']]), int(round(r.a))))
    if g is None: return np.nan
    t = g[(g.d - r.d).abs() <= pd.Timedelta(days=30)]
    return float(t.p.median()) if len(t) >= 2 else np.nan
for nm, X in (('C', C), ('A', c[c.cat == 'A'])):
    X = X.copy(); X['med'] = X.apply(cmpr, axis=1); Y = X[X.med.notna()]; rate = (Y.p / Y.med - 1) * 100
    J['cmp_' + nm] = {'n': f(len(Y)), 'med_rate': round(float(rate.median()), 1), '높음': f((rate > 0).sum()), '5%넘게높음': f((rate >= 5).sum()), '낮음': f((rate < 0).sum()), '같음': f((rate == 0).sum())}
J['C'] = {'n': f(len(C)), '시도': C['시도'].value_counts().to_dict(), '직거래': f((C['거래유형'] == '직거래').sum()), 'p_med': float(C.p.median()),
          '10억넘게': f((C.p >= 100000).sum()), 'ym': C['계약년월'].value_counts().sort_index().to_dict()}
J['sido'] = {k: {'cancel': f(len(x)), 'C': f((x.cat == 'C').sum()), 're_pct': round((x.cat != 'C').mean() * 100, 1), 'all': f((m['시도'] == k).sum())} for k, x in c.groupby('시도')}
J['direct'] = {'cancel': f((c['거래유형'] == '직거래').sum()), 'all': f((m['거래유형'] == '직거래').sum())}
h = c[c['시군구'].str.contains('하남시')]
J['hanam'] = {'all': f(m['시군구'].str.contains('하남시').sum()), 'cancel': f(len(h)), 'cat': {k: f((h.cat == k).sum()) for k in 'ABC'}}
# 한 건의 이야기: 대치동 선경1차 136.68㎡ 10층
s = m[(m['단지명'].str.startswith('선경1차')) & (m['시군구'].str.contains('대치동')) & (m['전용면적(㎡)'].str.startswith('136.68')) & (m['층'] == '10')].sort_values(['d', 'x'], ascending=[True, False])
J['case'] = [{'계약': str(r.d.date()), '금': f(r.p), '유형': r['거래유형'], '해제': (str(r.xd.date()) if r.x else None), '등기': r['등기일자']} for _, r in s.iterrows()]
# 값이 바뀐 재신고 예(같은 계약일 · 값만 다름)에서 금액 차가 큰 것
t = B.assign(adp=B.dp.abs()).sort_values('adp', ascending=False).head(10)
J['B_top'] = [{'시군구': r['시군구'], '단지': r['단지명'], '면': float(r.a), '층': r['층'], '계약': str(r.d.date()), '금': f(r.p), '해제': str(r.xd.date()), '계약2': str(pd.Timestamp(r.d2).date()), '금2': f(r.p2), '유형': r['거래유형']} for _, r in t.iterrows()]

# 덧붙임: 계약 월별 해제 비율 · 마포 한 건 · 살아 있는 거래의 바탕 비율 · 값 그대로 재신고 합계
J['ym_rate'] = {k: round(J['meta']['ym_cancel'][k] / J['meta']['ym_all'][k] * 100, 1) for k in J['meta']['ym_all']}
q = m[(m['단지명'] == '마포프레스티지자이') & (m['전용면적(㎡)'].str.startswith('84.9422')) & (m['층'] == '11')].sort_values(['d', 'x'], ascending=[True, False])
J['case_mapo'] = [{'계약': str(r.d.date()), '금': f(r.p), '유형': r['거래유형'], '해제': (str(r.xd.date()) if r.x else None), '등기': r['등기일자'], '동': r['동'], '면': r['전용면적(㎡)']} for _, r in q.iterrows()]
gl = live.groupby('k'); mx = gl['d'].transform('max'); cnt = gl['d'].transform('size'); nmax = gl['d'].transform(lambda s: (s == s.max()).sum())
J['base'] = {'later_pct': round(float(((cnt > 1) & ((live.d < mx) | (nmax > 1))).mean() * 100), 1), 'dup_pct': round(float(live.duplicated(['k', 'd', 'p'], keep=False).mean() * 100), 2)}
J['same_price'] = J['cat']['A'] + J['B']['같은값']; J['same_price_pct'] = round(J['same_price'] / n * 100, 1)
J['changed'] = J['B']['오름'] + J['B']['내림']; J['changed_pct'] = round(J['changed'] / n * 100, 1)
J['notA'] = n - J['cat']['A']; J['B_of_notA'] = round(J['cat']['B'] / (n - J['cat']['A']) * 100, 1)
J['wait_all'] = {'d7': round(float((c.wait <= 7).mean() * 100), 1), 'd30넘게': round(float((c.wait > 30).mean() * 100), 1), 'd60넘게': round(float((c.wait > 60).mean() * 100), 1), 'max': int(c.wait.max())}
J['C']['wait_d30넘게_n'] = f((C.wait > 30).sum())
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k:J[k] for k in ['ym_rate','case_mapo','base','same_price','same_price_pct','changed','changed_pct','notA','B_of_notA','wait_all','C']}, ensure_ascii=False))

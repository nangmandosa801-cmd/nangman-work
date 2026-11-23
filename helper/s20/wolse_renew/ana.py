# 보도 뒤집기 · 월세 상승률 — 서울 아파트 월세 갱신 계약을 실거래로 다시 센다(2026-11-24 받은 R_latest 그대로 · 다시 계산하지 않는다)
import pandas as pd, numpy as np, json, os
SRC = '/home/claude/rtn/keep/R_latest_1124.pkl'
R = pd.read_pickle(SRC)
n = lambda s: pd.to_numeric(s.astype(str).str.replace(',', '').str.strip(), errors='coerce')
R['dep'] = n(R['보증금(만원)']); R['mon'] = n(R['월세금(만원)']).fillna(0)
R['pd'] = n(R['종전계약 보증금(만원)']); R['pm'] = n(R['종전계약 월세(만원)']).fillna(0); R['a'] = n(R['전용면적(㎡)'])
R['date'] = pd.to_datetime(R['계약년월'].astype(str) + R['계약일'].astype(str).str.zfill(2), format='%Y%m%d')
R['gu'] = R['시군구'].str.split().str[1]; R['use'] = R['갱신요구권 사용'].astype(str).str.strip() == '사용'
S = R[R['시군구'].str.startswith('서울특별시')].copy()
pct = lambda x: round(float(x) * 100, 1)
J = {'meta': {'n_rent': int(len(S)), 'first': str(S.date.min().date()), 'last': str(S.date.max().date()),
              'n_wol': int((S.mon > 0).sum()), 'wol_share': pct((S.mon > 0).mean()),
              'ym_share': {k: pct((d.mon > 0).mean()) for k, d in S.groupby('계약년월')},
              'ym_n': {k: int(len(d)) for k, d in S.groupby('계약년월')},
              'new_share': pct((S[S['계약구분'] == '신규'].mon > 0).mean()), 'renew_share': pct((S[S['계약구분'] == '갱신'].mon > 0).mean()),
              'n_new': int((S['계약구분'] == '신규').sum()), 'n_renew': int((S['계약구분'] == '갱신').sum())}}
# 월세 → 월세 갱신(종전 값이 적힌 계약)
A = S[(S['계약구분'] == '갱신') & (S.pd > 0) & (S.mon > 0) & (S.pm > 0)].copy()
E = A[A.dep == A.pd].copy(); E['r'] = (E.mon / E.pm - 1) * 100; E['d'] = E.mon - E.pm
def stat(d):
    return {'n': int(len(d)), 'med_r': round(float(d.r.median()), 2), 'med_won': float(d.d.median()), 'same': pct((d.r == 0).mean()), 'down': pct((d.r < 0).mean()),
            'le5': pct(((d.r > 0) & (d.r <= 5.0001)).mean()), 'gt5': pct((d.r > 5.0001).mean()), 'gt5_n': int((d.r > 5.0001).sum()), 'gt10': pct((d.r > 10.0001).mean()), 'gt20': pct((d.r > 20.0001).mean())}
J['same_dep'] = {'all': stat(E), 'use': stat(E[E.use]), 'nouse': stat(E[~E.use])}
J['renew_wol'] = {'n': int(len(A)), 'use': int(A.use.sum()), 'same_dep': int(len(E))}
# 보증금까지 월세로 바꿔 합친 값(연 4.5% · 5%)으로 다시 잰 인상률 — 갱신권을 쓴 계약 전부(보증금이 바뀐 것 포함)
U = A[A.use]
def conv(d, rate):
    x = ((d.dep + d.mon * 12 / rate) / (d.pd + d.pm * 12 / rate) - 1) * 100
    return {'n': int(len(d)), 'le5': pct((x <= 5.1).mean()), 'med': round(float(x.median()), 2)}
J['conv_use'] = {'r45': conv(U, 0.045), 'r50': conv(U, 0.05)}
J['conv_use_same'] = {'r45': conv(E[E.use], 0.045), 'r50': conv(E[E.use], 0.05)}
# 전세 → 전세 갱신
T = S[(S['계약구분'] == '갱신') & (S.mon == 0) & (S.pm == 0) & (S.pd > 0)].copy(); T['r'] = (T.dep / T.pd - 1) * 100
J['jeonse'] = {k: {'n': int(len(d)), 'gt5': pct((d.r > 5.0001).mean()), 'gt5_n': int((d.r > 5.0001).sum()), 'med_r': round(float(d.r.median()), 2)} for k, d in (('use', T[T.use]), ('nouse', T[~T.use]))}
# 같은 단지 · 같은 면적 · 같은 보증금에서 새 계약 월세와 갱신 월세
W = S[(S.mon > 0) & S['계약구분'].isin(['신규', '갱신'])].copy(); W['ar'] = W.a.round()
g = W.groupby(['시군구', '번지', '단지명', 'ar', 'dep', '계약구분']).mon.median().unstack()
g = g.dropna(); g['diff'] = g['신규'] - g['갱신']
J['pair'] = {'n': int(len(g)), 'med_new': float(g['신규'].median()), 'med_renew': float(g['갱신'].median()), 'med_diff': float(g['diff'].median()), 'new_higher': pct((g['diff'] > 0).mean()), 'med_rate': round(float((g['신규'] / g['갱신'] - 1).median() * 100), 1)}
# 구별(갱신 월세 · 보증금 그대로)
gu = E.groupby('gu').apply(lambda d: pd.Series({'n': len(d), 'med_r': round(d.r.median(), 2), 'gt5': pct((d.r > 5.0001).mean()), 'med_won': d.d.median()}))
J['gu'] = {k: {'n': int(v.n), 'med_r': float(v.med_r), 'gt5': float(v.gt5), 'med_won': float(v.med_won)} for k, v in gu.iterrows()}
J['gu_wol_share'] = {k: pct((d.mon > 0).mean()) for k, d in S.groupby('gu')}
# 보도에 나온 사례 · 본문 사례
def rows(d): return [{'단지': r['단지명'], '면적': float(r.a), '층': str(r['층']).strip(), '계약': str(r.date.date()), '보증금': float(r.dep), '월세': float(r.mon), '구분': r['계약구분'], '갱신권': bool(r.use), '종전보증금': None if pd.isna(r.pd) else float(r.pd), '종전월세': float(r.pm)} for _, r in d.sort_values('date').iterrows()]
J['case_junggye'] = rows(S[S['단지명'].str.contains('중계그린1단지') & S.a.between(49, 50) & (S['층'].astype(str).str.strip() == '12') & (S.mon > 0)])
J['case_sanggye'] = rows(S[S['단지명'].str.contains('상계주공6') & S.a.between(58, 58.1) & (S['층'].astype(str).str.strip() == '11') & (S.mon > 0)])
J['case_mapo'] = rows(E[E.use & E['단지명'].str.contains('래미안밤섬리베뉴') & (E.dep == 50000) & (E.pm == 150)])
# 하남
H = R[R['시군구'].str.contains('하남시')]; HA = H[(H['계약구분'] == '갱신') & (H.pd > 0) & (H.mon > 0) & (H.pm > 0)]; HE = HA[HA.dep == HA.pd].copy(); HE['r'] = (HE.mon / HE.pm - 1) * 100; HE['d'] = HE.mon - HE.pm
J['hanam'] = {'n_rent': int(len(H)), 'wol_share': pct((H.mon > 0).mean()), 'same_dep': stat(HE) if len(HE) else None, 'use': stat(HE[HE.use]) if HE.use.sum() else None}
json.dump(J, open('ana.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(json.dumps({k: J[k] for k in J if k not in ('gu', 'gu_wol_share')}, ensure_ascii=False, indent=0))
print({k: J['gu'][k] for k in ('노원구', '성북구', '송파구', '강남구', '마포구', '강동구')}); print({k: J['gu_wol_share'][k] for k in ('노원구', '성북구', '송파구', '강남구')})

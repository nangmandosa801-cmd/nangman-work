#!/usr/bin/env python3
"""실거래 탐정 3화 · 동대문구 휘경동 하루 313건 — 숫자 재기.
자료: python3 /home/claude/tools/postkit/odd_deals.py --from 202609 --to 202611 --fetch --out odd.json (2026-11-16 05시 받음 · 파일 이름은 _1115)
묶음 = 같은 날 · 같은 단지에서 직거래가 10건 이상 계약된 것(해제 뺌). ana.json 은 받은 날 값 그대로 둔다(다시 받으면 숫자가 바뀜)."""
import sys, glob, json, pandas as pd
sys.path.insert(0, '/home/claude/tools/postkit')
import odd_deals as o
fs = sorted(glob.glob('/home/claude/rtn/rawO/M_*_202609_202611_1115.csv'))
cur = o.prep(pd.concat([o.load_csv(f) for f in fs], ignore_index=True))
v = cur[~cur['해제']].copy()
v['시도'] = v['시군구'].str.split().str[0]
v['구'] = v['시군구'].apply(lambda s: ' '.join(s.split()[:3]) if (len(s.split()) > 3 and s.split()[2].endswith('구')) else ' '.join(s.split()[:2]))
g = v[v['직']].groupby(['key', '일']).size()
bk = set(g[g >= 10].index)
v['묶음'] = pd.Series([(k, d) in bk for k, d in zip(v['key'], v['일'])], index=v.index) & v['직']
J = {'meta': {'files': [f.split('/')[-1] for f in fs], 'n_all': int(len(cur)), 'n_valid': int(len(v)), 'last': cur['일'].max()}}
# 1. 묶음 목록
B = []
for (k, d), x in v[v['묶음']].groupby(['key', '일']):
    B.append({'시군구': x['시군구'].iloc[0], '단지': x['단지명'].iloc[0], '일': d, '채': int(len(x)), '면적min': float(x['면'].min()), '면적max': float(x['면'].max()),
              '금min': int(x['금'].min()), '금max': int(x['금'].max()), '합계억': round(x['금'].sum() / 10000, 1), '매수': x['매수자'].value_counts().to_dict(), '매도': x['매도자'].value_counts().to_dict(),
              '건축': str(x['건축년도'].iloc[0]), '등기': x['등기일자'].value_counts().to_dict(), '층min': int(x['층n'].min()), '층max': int(x['층n'].max())})
B.sort(key=lambda r: -r['채']); J['bundles'] = B
J['bundle_sum'] = {'n': len(B), '채': sum(b['채'] for b in B), '서울n': sum(b['시군구'].startswith('서울') for b in B), '서울채': sum(b['채'] for b in B if b['시군구'].startswith('서울')),
                   '60이하': int((v[v['묶음']]['면'] <= 60).sum()), '40이하': int((v[v['묶음']]['면'] <= 40).sum()),
                   '매수': v[v['묶음']]['매수자'].value_counts().to_dict(), '매도': v[v['묶음']]['매도자'].value_counts().to_dict(),
                   '신축': int(v[v['묶음']]['건축년도'].astype(int).ge(2025).sum())}
# 2. 동대문구 · 송파구
def gu(name):
    x = v[v['구'] == name]; r = {}
    for ym in ['202609', '202610']:
        m = x[x['계약년월'] == ym]; c = m[~m['묶음']]
        r[ym] = {'n': int(len(m)), '묶음': int(m['묶음'].sum()), '뺀': int(len(c)), '직': int(m['직'].sum()), '뺀직': int(c['직'].sum()),
                 'med': float(m['금'].median()), 'med뺀': float(c['금'].median()), '면med': float(m['면'].median()), '면med뺀': float(c['면'].median()),
                 '매수': m['매수자'].value_counts().to_dict()}
    return r
J['ddm'] = gu('서울특별시 동대문구'); J['songpa'] = gu('서울특별시 송파구')
# 3. 서울 구별 순위(9월 · 10월) 묶음 넣고 · 빼고
J['rank'] = {}
s = v[v['시도'] == '서울특별시']
for ym in ['202609', '202610']:
    m = s[s['계약년월'] == ym]
    a = m.groupby('구').size().sort_values(ascending=False); c = m[~m['묶음']].groupby('구').size().sort_values(ascending=False)
    J['rank'][ym] = {'넣고': [(k.split()[-1], int(n)) for k, n in a.head(6).items()], '빼고': [(k.split()[-1], int(n)) for k, n in c.head(6).items()],
                     '서울': int(len(m)), '서울묶음': int(m['묶음'].sum()), '서울뺀': int((~m['묶음']).sum()),
                     '순위넣고': {k.split()[-1]: i + 1 for i, k in enumerate(a.index)}, '순위빼고': {k.split()[-1]: i + 1 for i, k in enumerate(c.index)}}
# 4. 에드가휘경 · 송파해링턴타워 값 묶음
def grp(sgg, dj):
    x = v[(v['시군구'] == sgg) & (v['단지명'] == dj)]
    t = x.groupby([x['면'].round(2), '금']).agg(채=('금', 'size'), 층min=('층n', 'min'), 층max=('층n', 'max')).reset_index().sort_values('채', ascending=False)
    return [{'면': float(r['면']), '금': int(r['금']), '채': int(r['채']), '층': f"{int(r['층min'])}~{int(r['층max'])}"} for _, r in t.iterrows()]
J['edgar'] = grp('서울특별시 동대문구 휘경동', '에드가휘경'); J['harr'] = grp('서울특별시 송파구 장지동', '송파해링턴타워')
# 5. 수도권 매수자 · 매도자 종류(해제 뺌)
J['who'] = {'매수': v['매수자'].value_counts().to_dict(), '매도': v['매도자'].value_counts().to_dict(),
            '개인끼리': int(((v['매수자'] == '개인') & (v['매도자'] == '개인')).sum())}
# 6. 묶음이 그 달 거래의 20%를 넘는 시군구(월별)
t = v[v['계약년월'].isin(['202609', '202610'])].groupby(['구', '계약년월']).agg(n=('금', 'size'), b=('묶음', 'sum')).reset_index()
t['share'] = (t['b'] / t['n'] * 100).round(1)
J['share'] = [{'구': r['구'], '월': r['계약년월'], 'n': int(r['n']), 'b': int(r['b']), 'share': float(r['share'])} for _, r in t[t['b'] > 0].sort_values('share', ascending=False).iterrows()]
# 동대문구 10월 묶음 뺀 거래에서 60㎡ 아래 비중 / 넣었을 때
m = v[(v['구'] == '서울특별시 동대문구') & (v['계약년월'] == '202610')]
J['ddm_small'] = {'40이하_넣고': int((m['면'] <= 40).sum()), '40이하_빼고': int(((m['면'] <= 40) & ~m['묶음']).sum())}
J['direct'] = {'n': int(v['직'].sum()), '묶음': int(v['묶음'].sum()), 'share': round(v['묶음'].sum() / v['직'].sum() * 100, 1)}
J['seoul_gu_n'] = int(v[v['시도'] == '서울특별시']['구'].nunique())
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(J, ensure_ascii=False)[:6000])

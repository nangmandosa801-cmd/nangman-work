#!/usr/bin/env python3
"""이 돈이면 어디 · 월상환액 200만원으로 하남에서 닿는 아파트.
조건: 월 200만원 · 30년 · 원리금균등 · 금리 4.6/5.6/6.6%(노컷뉴스 11/3 · 5대 은행 5년 고정 4.55~6.868%) · 떼는 돈 1,500만원 · 생애최초 LTV 70% / 하남(규제지역) 일반 40% · 한도 6억.
다시 돌리기: python3 ana.py (자료 /home/claude/rtn/M_gg2026_1112.pkl · 경기 2026 매매 11/12 내려받음)"""
import sys, json, subprocess, argparse, pandas as pd
sys.path.insert(0, '/home/claude/tools/postkit'); import budget_map as bm
DATA = '/home/claude/rtn/M_gg2026_1112.pkl'; M = 200; Y = 30; RES = 1500
J = {'rates': {}}
for r in (4.6, 5.6, 6.6):
    L = bm.annuity_loan(M, r, Y)
    L = int(L // 10 * 10)
    p70 = int((L / 0.7) // 100 * 100); eq70 = p70 - L + RES
    p40 = int((L / 0.4) // 100 * 100); eq40 = p40 - L + RES
    srate = r + 3.0; spay = bm.annuity_pay(L, srate, Y)
    J['rates'][str(r)] = dict(loan=L, p70=p70, eq70=eq70, p40=p40, eq40=eq40, income=round(spay * 12 / 0.4), interest=round(M * Y * 12 - L))
# 하남 · 2026년 8~10월 · 84㎡ · 59㎡ (해제 · 직거래 뺌)
def run(price, out):
    cmd = f'python3 /home/claude/tools/postkit/budget_map.py --data {DATA} --price {price} --monthly {M} --rate 4.6 --years {Y} --ym-from 202608 --ym-to 202610 --base-year 2026 --out {out}'
    subprocess.run(cmd.split(), check=True, capture_output=True); return json.load(open(out))
R = J['rates']['4.6']
A = run(R['p70'], '/tmp/m200_a.json'); B = run(R['p40'], '/tmp/m200_b.json')
J['A'] = {'price': R['p70'], 'hanam': A['hanam'], 'deals84': A['hanam_deals_84'], 'deals59': A['hanam_deals_59']}
J['B'] = {'price': R['p40'], 'hanam': B['hanam'], 'deals84': B['hanam_deals_84'], 'deals59': B['hanam_deals_59']}
# 동별 84㎡ 중앙값 · 9억 8천 아래 비율 (거래 10건 넘는 동)
d, _, _ = bm.load_data(argparse.Namespace(data=DATA, rebuild=False, ym_from='202608', ym_to='202610'))
h = d[d.area == '경기 하남시']
J['hanam_n'] = int(len(h)); J['hanam_n84'] = int((h['size'] == '84').sum()); J['hanam_n59'] = int((h['size'] == '59').sum())
J['dong84'] = []
for dn, g in h[h['size'] == '84'].groupby('dong'):
    J['dong84'].append(dict(dong=dn, n=int(len(g)), med=int(g.amt.median()), kB=int((g.amt <= R['p40']).sum()), kA=int((g.amt <= R['p70']).sum())))
J['dong84'].sort(key=lambda x: -x['n'])
J['dong59'] = []
for dn, g in h[h['size'] == '59'].groupby('dong'):
    J['dong59'].append(dict(dong=dn, n=int(len(g)), med=int(g.amt.median()), kB=int((g.amt <= R['p40']).sum()), kA=int((g.amt <= R['p70']).sum())))
J['dong59'].sort(key=lambda x: -x['n'])
# 9억 8천 아래 84㎡ 단지(2012년 이후) 많이 팔린 곳
x = h[(h['size'] == '84') & (h.amt <= R['p40'])]
v = x.groupby(['dong', '단지명']).agg(k=('amt', 'size'), med=('amt', 'median'), lo=('amt', 'min'), hi=('amt', 'max'), yr=('yr', 'first')).reset_index().sort_values('k', ascending=False)
J['B_apts84'] = [dict(dong=r.dong, apt=r.단지명, k=int(r.k), med=int(r.med), lo=int(r.lo), hi=int(r.hi), yr=int(r.yr)) for r in v.head(10).itertuples()]
x = h[(h.amt <= R['p70'])]
v = x.groupby(['dong', '단지명', 'size']).agg(k=('amt', 'size'), med=('amt', 'median'), lo=('amt', 'min'), hi=('amt', 'max'), yr=('yr', 'first')).reset_index().sort_values('k', ascending=False)
J['A_apts'] = [dict(dong=r.dong, apt=r.단지명, size=r.size, k=int(r.k), med=int(r.med), lo=int(r.lo), hi=int(r.hi), yr=int(r.yr)) for r in v.head(12).itertuples()]
# 같은 돈 59㎡ 새 아파트(2012년 이후) 9억 8천 아래
x = h[(h['size'] == '59') & (h.yr >= 2012) & (h.amt <= R['p40'])]
v = x.groupby(['dong', '단지명']).agg(k=('amt', 'size'), med=('amt', 'median'), yr=('yr', 'first')).reset_index().sort_values('k', ascending=False)
J['B_apts59new'] = [dict(dong=r.dong, apt=r.단지명, k=int(r.k), med=int(r.med), yr=int(r.yr)) for r in v.head(8).itertuples()]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1, default=int)
print(json.dumps(J['rates'], ensure_ascii=False)); print('n', J['hanam_n'], J['hanam_n84'], J['hanam_n59'])
print('A', J['A']['price'], json.dumps(J['A']['hanam']['total'], ensure_ascii=False)); print('B', J['B']['price'], json.dumps(J['B']['hanam']['total'], ensure_ascii=False))
for k in ('dong84', 'dong59', 'B_apts84', 'A_apts', 'B_apts59new'):
    print(k); [print(' ', r) for r in J[k]]
# 모은 돈별 닿는 집값(4.6%) · 하남 84㎡ · 59㎡ 거래 중 그 값 아래
L = J['rates']['4.6']['loan']; J['by_eq'] = []
for eq in (20000, 30000, 40000, J['rates']['4.6']['eq40']):
    own = eq - RES
    pf = int(min(own / 0.3, own + L) // 100 * 100); pg = int(min(own / 0.6, own + L) // 100 * 100)
    J['by_eq'].append(dict(eq=eq, first=pf, gen=pg, loan_first=pf - own, loan_gen=pg - own,
                           k_first=int((h.amt <= pf).sum()), k_gen=int((h.amt <= pg).sum()),
                           k84_first=int(((h['size'] == '84') & (h.amt <= pf)).sum()), k84_gen=int(((h['size'] == '84') & (h.amt <= pg)).sum())))
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1, default=int)
for r in J['by_eq']: print(r)
# 모은 돈 3억 · 생애최초(6억 7,500만) 아래 거래 보기
p3 = [r for r in J['by_eq'] if r['eq'] == 30000][0]['first']
x = h[h.amt <= p3].sort_values('amt', ascending=False)
J['eq3_deals'] = [dict(dong=r.dong, apt=r.단지명, size=r.size, ar=round(r.ar, 2), fl=r.층, ym=r.계약년월, amt=int(r.amt), yr=int(r.yr)) for r in x.itertuples()]
J['eq3_apts'] = x.groupby(['dong', '단지명', 'size']).size().sort_values(ascending=False).reset_index().values.tolist()
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1, default=int)
for r in J['eq3_deals']: print(r)

# 연봉 5천 편 — 계산 · 실거래 집계 (가정은 허브 글 salary_map 과 같다: 연 4.5% · 30년 · 다른 대출 없음 · 은행 DSR 40% · 수도권 스트레스 금리 3.0%p)
# 자료: /home/claude/rtn/M_budget_sudo.pkl (없으면 python3 /home/claude/tools/postkit/rtdata.py --from 202608 --to 202610 로 받는다)
import pandas as pd, json, math
BASE, YEARS, DSR, STRESS, CAP, INC = 4.5, 30, 0.40, 3.0, 60000, 5000
N = YEARS * 12
def pv(pm, rate): r = rate / 100 / 12; return pm * (1 - (1 + r) ** -N) / r
def pay(loan, rate): r = rate / 100 / 12; return loan * r / (1 - (1 + r) ** -N)
def loan(inc, ratio, base=BASE, burden=0): return min(math.floor(pv((inc * DSR - burden) / 12, base + STRESS * ratio) / 10) * 10, CAP)
REG = {'과천시', '광명시', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '안양시 동안구', '용인시 수지구', '의왕시', '하남시', '화성시 동탄구', '용인시 기흥구', '구리시'}
d = pd.read_pickle('/home/claude/rtn/M_budget_sudo.pkl')
d = d[(d['해제사유발생일'] == '-') & (d['거래유형'] != '직거래')].copy()
d['amt'] = d['거래금액(만원)'].astype(str).str.replace(',', '').astype(int); d['a'] = d['전용면적(㎡)'].astype(float); d['ym'] = d['계약년월'].astype(int)
d = d[d.ym.between(202608, 202610)]
def sgg(x):
    t = x.split()
    if t[0].startswith(('서울', '인천')): return t[0][:2] + ' ' + t[1]
    return t[1] + ' ' + t[2] if len(t) >= 3 and t[2].endswith('구') else t[1]
d['sgg'] = d['시군구'].map(sgg); d['sido'] = d['시군구'].str[:2]; d['yr'] = pd.to_numeric(d['건축년도'], errors='coerce')
d['reg'] = d.apply(lambda r: r.sido == '서울' or r.sgg in REG, axis=1)
m84 = d[d.a.between(83, 86)]; m59 = d[d.a.between(58, 60)]
L = {'변동형': loan(INC, 1.0), '혼합형': loan(INC, 0.8), '주기형': loan(INC, 0.4)}
best = L['주기형']; price = math.floor(best / 0.7 / 100) * 100; own = price - best
J = dict(inc=INC, loan=L, gap=L['주기형'] - L['변동형'], price=price, own=own, pay=round(pay(best, BASE), 1), pay_share=round(pay(best, BASE) / (INC / 12) * 100, 1),
         month_gross=round(INC / 12, 1), n84=len(m84), n59=len(m59))
def reach(m, p): return int((m.amt <= p).sum()), round(float((m.amt <= p).mean()) * 100, 1)
J['k84'], J['s84'] = reach(m84, price); J['k59'], J['s59'] = reach(m59, price)
r84 = m84[m84.amt <= price]; r59 = m59[m59.amt <= price]
J['sido84'] = r84.sido.value_counts().to_dict(); J['sido59'] = r59.sido.value_counts().to_dict()
J['new84'] = int((r84.yr >= 2016).sum()); J['new84_share'] = round(J['new84'] / J['k84'] * 100, 1)
J['nonreg84_share'] = round(float((~r84.reg).mean()) * 100, 1)
def top(r, m, n=8):
    g = r.groupby('sgg').size().sort_values(ascending=False); tot = m.groupby('sgg').size()
    return [dict(sgg=k, k=int(v), n=int(tot[k]), share=round(v / tot[k] * 100, 1)) for k, v in g.head(n).items()]
J['top84'] = top(r84, m84); J['top59'] = top(r59, m59)
# 내 돈이 모자랄 때: 집값 = 내 돈 ÷ 0.3 (대출은 집값의 70% · 한도 안)
own_rows = []
for o in (6000, 8000, 10000, own):
    p = price if o == own else min(math.floor(o / 0.3 / 100) * 100, price); k, s = reach(m84, p); k5, s5 = reach(m59, p)
    own_rows.append(dict(own=o, price=p, loan=p - o if p < price else best, k84=k, s84=s, k59=k5, s59=s5))
J['own_rows'] = own_rows
# 신용대출 3,000만원(연 6% · DSR 은 5년에 나눠 갚는 것으로 봄)
b = 3000 / 5 + 3000 * 0.06; J['credit'] = dict(amount=3000, burden=b, loan=loan(INC, 0.4, burden=b)); J['credit']['cut'] = best - J['credit']['loan']
J['alt55'] = loan(INC, 0.4, 5.5); J['int_total'] = round(pay(best, BASE) * N - best)
c = m84[(m84.amt <= price) & (m84.amt >= price - 2500) & (m84.yr >= 2016)].sort_values(['amt', 'ym'], ascending=[False, False])
J['ex84'] = [dict(sgg=x.sgg, dong=x['시군구'].split()[-1], apt=x['단지명'], fl=str(x['층']), ym=int(x.ym), amt=int(x.amt), yr=int(x.yr)) for _, x in c.head(14).iterrows()]
c = m59[(m59.amt <= price) & (m59.amt >= price - 2000) & (m59.yr >= 2016)].sort_values(['amt', 'ym'], ascending=[False, False])
J['ex59'] = [dict(sgg=x.sgg, dong=x['시군구'].split()[-1], apt=x['단지명'], fl=str(x['층']), ym=int(x.ym), amt=int(x.amt), yr=int(x.yr)) for _, x in c.head(14).iterrows()]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print({k: v for k, v in J.items() if k not in ('top84', 'top59', 'ex84', 'ex59', 'own_rows')})
print('top84', [(t['sgg'], t['k'], t['share']) for t in J['top84']]); print('top59', [(t['sgg'], t['k'], t['share']) for t in J['top59']])
for r in own_rows: print(r)
for e in J['ex84'][:10]: print('84', e)
for e in J['ex59'][:10]: print('59', e)

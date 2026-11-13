# 연봉별 대출한도 · 연봉별 아파트 구매 — 계산 · 실거래 집계 (2026-11-13)
# 가정: 연 4.5% · 30년 · 원리금균등 · 다른 대출 없음 · 은행 DSR 40% · 수도권 스트레스 금리 3.0%p(변동형 100% · 혼합형 80% · 주기형 40%)
#       수도권 · 규제지역 주택담보대출 한도 6억원(집값 15억원 이하) · 닿는 집값은 LTV 70%(생애최초 · 비규제지역 무주택)를 꽉 채운 값
import pandas as pd, json, math
BASE, YEARS, DSR, STRESS, CAP = 4.5, 30, 0.40, 3.0, 60000
TYPES = [('변동형', 1.0), ('혼합형', 0.8), ('주기형', 0.4)]
N = YEARS * 12
def pv(pm, rate):
    r = rate / 100 / 12; return pm * (1 - (1 + r) ** -N) / r
def pay(loan, rate):
    r = rate / 100 / 12; return loan * r / (1 - (1 + r) ** -N)
def loan(inc, ratio, base=BASE):
    return min(math.floor(pv(inc * DSR / 12, base + STRESS * ratio) / 10) * 10, CAP)
REG = {'과천시', '광명시', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '안양시 동안구',
       '용인시 수지구', '의왕시', '하남시', '화성시 동탄구', '용인시 기흥구', '구리시'}   # 경기 15곳(2025-10-16 12곳 + 2026-07-01 3곳) · 서울은 전체
d = pd.read_pickle('/home/claude/rtn/M_budget_sudo.pkl')
d = d[(d['해제사유발생일'] == '-') & (d['거래유형'] != '직거래')].copy()
d['amt'] = d['거래금액(만원)'].astype(str).str.replace(',', '').astype(int)
d['a'] = d['전용면적(㎡)'].astype(float); d['ym'] = d['계약년월'].astype(int)
d = d[d.ym.between(202608, 202610)]
def sgg(x):
    t = x.split()
    if t[0].startswith(('서울', '인천')): return t[0][:2] + ' ' + t[1]
    return t[1] + ' ' + t[2] if len(t) >= 3 and t[2].endswith('구') else t[1]
d['sgg'] = d['시군구'].map(sgg); d['sido'] = d['시군구'].str[:2]
d['reg'] = d.apply(lambda r: r.sido == '서울' or r.sgg in REG, axis=1)
d['yr'] = pd.to_numeric(d['건축년도'], errors='coerce')
m84 = d[d.a.between(83, 86)]; m59 = d[d.a.between(58, 60)]
J = dict(base=BASE, years=YEARS, dsr=DSR, stress=STRESS, cap=CAP, n_all=len(d), n84=len(m84), n59=len(m59),
         sido84=m84.sido.value_counts().to_dict(), sido59=m59.sido.value_counts().to_dict(),
         med84=int(m84.amt.median()), med59=int(m59.amt.median()),
         med84_sido={k: int(v) for k, v in m84.groupby('sido').amt.median().items()})
J['mult'] = {n: round(pv(DSR / 12, BASE + STRESS * r), 3) for n, r in TYPES}
J['rate_dsr'] = {n: round(BASE + STRESS * r, 2) for n, r in TYPES}
J['cap_income'] = {n: math.ceil(CAP / pv(DSR / 12, BASE + STRESS * r) / 10) * 10 for n, r in TYPES}
rows = []
for inc in (3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 13000):
    L = {n: loan(inc, r) for n, r in TYPES}
    best = L['주기형']; p70 = math.floor(best / 0.7 / 100) * 100
    pm = pay(best, BASE)
    r = dict(inc=inc, **L, gap=L['주기형'] - L['변동형'], price=p70, own=p70 - best, pay=round(pm, 1), pay_share=round(pm / (inc / 12) * 100, 1),
             k84=int((m84.amt <= p70).sum()), k59=int((m59.amt <= p70).sum()))
    r['s84'] = round(r['k84'] / len(m84) * 100, 1); r['s59'] = round(r['k59'] / len(m59) * 100, 1)
    r['sido84'] = m84[m84.amt <= p70].sido.value_counts().to_dict()
    r['reg84'] = int((m84[m84.amt <= p70].reg).sum())
    r['new84'] = int(((m84.amt <= p70) & (m84.yr >= 2016)).sum())
    g = m84[m84.amt <= p70].groupby('sgg').size().sort_values(ascending=False)
    tot = m84.groupby('sgg').size()
    r['top84'] = [dict(sgg=k, k=int(v), n=int(tot[k]), share=round(v / tot[k] * 100, 1)) for k, v in g.head(8).items()]
    rows.append(r)
J['rows'] = rows
# 금리가 1%p 높을 때(연 5.5%) 주기형 한도 — 본문 한 줄
J['alt55'] = {inc: loan(inc, 0.4, 5.5) for inc in (5000, 6000, 8000, 10000)}
# 변동형 6억 → 월 상환액 등 본문용
J['pay_6eok'] = round(pay(60000, BASE), 1)
# 연봉 6천(주기형) 값 아래로 팔린 84㎡ 가운데 2016년 이후 지은 단지 — 이야기 한 건 후보
r6 = next(r for r in rows if r['inc'] == 6000)
c = m84[(m84.amt <= r6['price']) & (m84.amt >= r6['price'] - 3000) & (m84.yr >= 2016)]
c = c.sort_values(['amt', 'ym'], ascending=[False, False])
J['ex6'] = [dict(sgg=x.sgg, dong=x['시군구'].split()[-1], apt=x['단지명'], a=x.a, fl=str(x['층']), ym=int(x.ym), amt=int(x.amt), yr=int(x.yr)) for _, x in c.head(25).iterrows()]
# 시군구별 84㎡ 가운데 값 (구글 표 페이지 · 본문 표)
g = m84.groupby('sgg').agg(n=('amt', 'size'), med=('amt', 'median')).reset_index()
g['sido'] = g.sgg.map(lambda s: s[:2] if s.startswith(('서울', '인천')) else '경기')
J['sgg84'] = [dict(sgg=x.sgg, sido=x.sido, n=int(x.n), med=int(x.med), reg=bool(x.sgg in REG or x.sido == '서울')) for _, x in g.sort_values('med').iterrows() if x.n >= 20]

# ── 본문용 덧셈 ──
X = {}
X['lo441_1eok'] = min(math.floor(pv(10000 * DSR / 12, 4.41 + STRESS * 0.4) / 10) * 10, CAP)     # 가장 낮은 금리 4.41% · 주기형 · 연봉 1억
X['pure_fix_1eok'] = math.floor(pv(10000 * DSR / 12, BASE) / 10) * 10                              # 스트레스 0%(만기까지 고정)일 때 계산값(한도 6억 적용 전)
# 신용대출 5,000만원(연 6% · DSR 계산은 5년에 나눠 갚는 것으로 봄) 이 있을 때 연봉 6천 주기형 한도
burden = 5000 / 5 + 5000 * 0.06
left = 6000 * DSR - burden
X['credit'] = dict(burden=burden, left=left, loan=math.floor(pv(left / 12, BASE + STRESS * 0.4) / 10) * 10)
X['credit']['cut'] = next(r for r in rows if r['inc'] == 6000)['주기형'] - X['credit']['loan']
# 수도권 84㎡ 가운데 값 집(LTV 70%)에 필요한 연봉
need = J['med84'] * 0.7
X['med_need'] = dict(loan=int(need), own=int(J['med84'] - need), inc_p=math.ceil(need / pv(DSR / 12, BASE + STRESS * 0.4) / 10) * 10, inc_v=math.ceil(need / pv(DSR / 12, BASE + STRESS * 1.0) / 10) * 10)
# 규제지역 예: 연봉 1억 · 8억 집 · LTV 40%
X['reg_ex'] = dict(price=80000, loan40=32000, own40=48000, loan70=56000, own70=24000)
r6 = next(r for r in rows if r['inc'] == 6000); r10 = next(r for r in rows if r['inc'] == 10000)
X['r6_nonreg_share'] = round((r6['k84'] - r6['reg84']) / r6['k84'] * 100, 1)
X['r6_new_share'] = round(r6['new84'] / r6['k84'] * 100, 1)
X['seoul84'] = J['sido84']['서울']; X['r6_seoul'] = r6['sido84'].get('서울', 0); X['r10_seoul'] = r10['sido84'].get('서울', 0)
X['r10_seoul_share'] = round(X['r10_seoul'] / X['seoul84'] * 100, 1)
X['gap_ratio_1eok'] = round(r10['gap'] / 10000 * 100, 1)
X['pay10'] = r10['pay']; X['pay6'] = r6['pay']
X['int_total_6'] = round(r6['pay'] * N - r6['주기형'])
J['x'] = X
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(X)

print('n84', J['n84'], 'n59', J['n59'], 'med84', J['med84'], J['med84_sido'], 'mult', J['mult'], 'cap_income', J['cap_income'])
for r in rows: print(r['inc'], r['변동형'], r['혼합형'], r['주기형'], 'gap', r['gap'], 'price', r['price'], 'own', r['own'], 'pay', r['pay'], r['pay_share'], '84:', r['k84'], r['s84'], '59:', r['k59'], r['s59'], 'reg', r['reg84'], 'new', r['new84'], r['sido84'])
print(J['alt55'], J['pay_6eok'])

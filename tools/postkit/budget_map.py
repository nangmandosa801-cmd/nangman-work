#!/usr/bin/env python3
"""「사람에서 출발」 글 계산기 — 내 조건으로 살 수 있는 집값 상한 → 그 값 아래 실거래가 많은 수도권 동네.

쓰기 (돈 단위는 전부 만원):
  python3 /home/claude/tools/postkit/budget_map.py --equity 20000 --monthly 250 --rate 4.5 --years 30 --out ana.json
  조건만 바꿔 다시 돌리면 다음 주 글 자료가 나온다(예: --equity 30000 --monthly 300, --ltv 40, --areas 59).

인자
  --equity   모은 돈                         --monthly  한 달에 갚을 수 있는 돈(원리금)
  --rate     대출 금리 연 %                  --years    만기(년 · 수도권 주담대는 30년까지)
  --ltv      집값 대비 대출 비율 %(생애최초 70 · 규제지역 일반 40 · 그 밖 수도권 무주택 70)
  --cap      대출 한도(수도권 · 규제지역 주담대 60000 = 6억)
  --reserve  세금 · 중개보수 · 이사비로 따로 떼는 돈
  --stress / --stress-ratio / --dsr   스트레스 금리 % · 적용 비율 %(주기형 40 · 혼합형 80 · 변동형 100) · DSR % → 필요한 연소득
  --ym-from / --ym-to   계약년월 범위(202608 202610)   --new-years  「지은 지 N년 안쪽」(15)
  --data     실거래 pkl(없으면 /home/claude/rtn/M_budget_sudo.pkl → 없으면 M2026.pkl 의 서울 · 경기 · 인천)
             새로 받기: cd /home/claude/rtn && python3 dl_budget.py 2026-08-01 <오늘>  뒤  --rebuild
  --price    집값 상한을 직접 줄 때(계산을 건너뜀)

계산(쉬운 말)
  ① 갚는 돈으로 빌릴 수 있는 돈 = 월 상환액 × (1 − (1+월금리)^−개월) ÷ 월금리      (원리금균등)
  ② 모은 돈으로 정해지는 집값 = (모은 돈 − 떼는 돈) ÷ (1 − LTV)
  ③ 집값 상한 = min( ②, (모은 돈 − 떼는 돈) + min(①, 대출 한도) )   → 100만원 아래 버림
거르기: 해제사유발생일 '-' · 직거래 뺌 · 전용 84㎡(83~86) · 59㎡(58~60).
출력: JSON(조건 · 계산 · 시도별 · 시군구별 · 동별 · 하남 · 개별 거래 보기). 표준 출력에는 요약 몇 줄만.
"""
import argparse, json, os, sys, glob, datetime
import pandas as pd

RTN = '/home/claude/rtn'


def annuity_loan(monthly, rate, years):
    r = rate / 100 / 12; n = years * 12
    return monthly * (1 - (1 + r) ** -n) / r if r else monthly * n


def annuity_pay(loan, rate, years):
    r = rate / 100 / 12; n = years * 12
    return loan * r / (1 - (1 + r) ** -n) if r else loan / n


def calc(a):
    own = a.equity - a.reserve
    by_pay = annuity_loan(a.monthly, a.rate, a.years)
    loan_room = min(by_pay, a.cap)
    p_ltv = own / (1 - a.ltv / 100)
    p_pay = own + loan_room
    price = min(p_ltv, p_pay)
    price = int(price // 100 * 100)
    loan = price - own
    pay = annuity_pay(loan, a.rate, a.years)
    srate = a.rate + a.stress * a.stress_ratio / 100
    spay = annuity_pay(loan, srate, a.years)
    return dict(own=own, loan_by_pay=round(by_pay), price_by_ltv=round(p_ltv), price_by_pay=round(p_pay),
                bind='모은 돈(LTV)' if p_ltv <= p_pay else ('대출 한도' if by_pay > a.cap else '월 상환액'),
                price=price, loan=loan, pay=round(pay, 1), total_interest=round(pay * a.years * 12 - loan),
                dsr_rate=round(srate, 2), dsr_pay=round(spay, 1), income_need=round(spay * 12 / (a.dsr / 100)))


def load_data(a):
    p = a.data
    if not p:
        p = f'{RTN}/M_budget_sudo.pkl'
        if a.rebuild or not os.path.exists(p):
            fs = sorted(glob.glob(f'{RTN}/rawBud/M_*.csv'))
            if fs:
                sys.path.insert(0, RTN)
                from load import load
                # 같은 시도 파일이 여러 번 받은 것이면 가장 늦게 받은 것만
                last = {}
                for f in fs: last[os.path.basename(f).split('_')[1]] = f
                pd.concat([load(f) for f in last.values()], ignore_index=True).to_pickle(p)
            else:
                p = f'{RTN}/M2026.pkl'
    d = pd.read_pickle(p)
    d = d[d['시군구'].str.split().str[0].isin(['서울특별시', '경기도', '인천광역시'])]
    d = d[(d['계약년월'] >= a.ym_from) & (d['계약년월'] <= a.ym_to)]
    raw = len(d)
    d = d[(d['해제사유발생일'] == '-') & (d['거래유형'] != '직거래')].copy()
    d['amt'] = d['거래금액(만원)'].str.replace(',', '').astype(int)
    d['ar'] = d['전용면적(㎡)'].astype(float)
    d['yr'] = pd.to_numeric(d['건축년도'], errors='coerce')
    d['size'] = None
    d.loc[(d.ar >= 83) & (d.ar < 86), 'size'] = '84'
    d.loc[(d.ar >= 58) & (d.ar < 60), 'size'] = '59'
    d = d[d['size'].notna()]
    t = d['시군구'].str.split()
    d['sido'] = t.str[0].map({'서울특별시': '서울', '경기도': '경기', '인천광역시': '인천'})
    d['sgg'] = t.apply(lambda x: x[1] + ' ' + x[2] if len(x) > 3 and x[1].endswith('시') and x[2].endswith('구') else x[1])
    d['dong'] = t.apply(lambda x: ' '.join(x[3:] if len(x) > 3 and x[1].endswith('시') and x[2].endswith('구') else x[2:]))
    d['area'] = d['sido'] + ' ' + d['sgg']
    return d, p, raw


def agg(g, price):
    n = len(g); k = int((g.amt <= price).sum())
    return dict(n=n, k=k, pct=round(k / n * 100, 1) if n else None, med=int(g.amt.median()) if n else None)


def table(d, key, price, new_from):
    out = {}
    for name, g in d.groupby(key):
        r = {}
        for s in ('84', '59'):
            gs = g[g['size'] == s]
            r[s] = agg(gs, price); r[s + 'new'] = agg(gs[gs.yr >= new_from], price)
        r['all'] = agg(g, price); r['allnew'] = agg(g[g.yr >= new_from], price)
        out[name] = r
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--equity', type=float, default=20000); ap.add_argument('--monthly', type=float, default=250)
    ap.add_argument('--rate', type=float, default=4.5); ap.add_argument('--years', type=int, default=30)
    ap.add_argument('--ltv', type=float, default=70); ap.add_argument('--cap', type=float, default=60000)
    ap.add_argument('--reserve', type=float, default=1500)
    ap.add_argument('--stress', type=float, default=3.0); ap.add_argument('--stress-ratio', dest='stress_ratio', type=float, default=40)
    ap.add_argument('--dsr', type=float, default=40)
    ap.add_argument('--ym-from', dest='ym_from', default='202608'); ap.add_argument('--ym-to', dest='ym_to', default='202610')
    ap.add_argument('--new-years', dest='new_years', type=int, default=15)
    ap.add_argument('--base-year', dest='base_year', type=int, default=datetime.date.today().year)
    ap.add_argument('--data', default=''); ap.add_argument('--rebuild', action='store_true')
    ap.add_argument('--price', type=float, default=0); ap.add_argument('--out', default='ana.json')
    ap.add_argument('--top', type=int, default=10); ap.add_argument('--min-n', dest='min_n', type=int, default=30)
    a = ap.parse_args()
    c = calc(a)
    if a.price: c['price'] = int(a.price)
    price = c['price']; new_from = a.base_year - a.new_years + 1     # 2026 · 15년 → 2012년부터
    d, src, raw = load_data(a)
    J = dict(cond={k: getattr(a, k) for k in ('equity', 'monthly', 'rate', 'years', 'ltv', 'cap', 'reserve', 'stress', 'stress_ratio', 'dsr', 'ym_from', 'ym_to', 'new_years')},
             calc=c, new_from=new_from, src=src, rows_raw=raw, rows=len(d),
             by_month=d.groupby('계약년월').size().to_dict(),
             total=table(d.assign(z='수도권'), 'z', price, new_from)['수도권'],
             sido=table(d, 'sido', price, new_from), sgg=table(d, 'area', price, new_from))
    # 금리가 달라질 때 (같은 조건) — 표로 쓰기 좋게
    J['rate_alt'] = {}
    for r in (4.0, 4.5, 5.0, 5.5, 6.0):
        b = argparse.Namespace(**vars(a)); b.rate = r; J['rate_alt'][str(r)] = calc(b)
    # LTV 40%(규제지역 · 생애최초 아님)일 때
    b = argparse.Namespace(**vars(a)); b.ltv = 40; J['ltv40'] = calc(b)
    # 순위: 지은 지 N년 안쪽 84㎡ 를 상한 아래로 산 거래 건수
    S = J['sgg']
    rk = sorted(S.items(), key=lambda kv: -kv[1]['84new']['k'])
    J['top_84new'] = [(k, v['84new'], v['59new'], v['84'], v['59']) for k, v in rk[:a.top]]
    rk59 = sorted(S.items(), key=lambda kv: -kv[1]['59new']['k'])
    J['top_59new'] = [(k, v['59new'], v['84new']) for k, v in rk59[:a.top]]
    # 비율 순위(거래 min_n건 이상인 곳만)
    J['top_84new_pct'] = [(k, v['84new']) for k, v in sorted(S.items(), key=lambda kv: -(kv[1]['84new']['pct'] or 0)) if v['84new']['n'] >= a.min_n][:a.top]
    J['zero_84new'] = sorted(k for k, v in S.items() if v['84new']['n'] >= a.min_n and v['84new']['k'] == 0)
    # 동별(지은 지 N년 안쪽 84㎡ 상한 아래 건수)
    dn = d[(d['size'] == '84') & (d.yr >= new_from)]
    g = dn.assign(ok=dn.amt <= price).groupby(['area', 'dong']).agg(n=('ok', 'size'), k=('ok', 'sum'), med=('amt', 'median')).reset_index()
    g = g.sort_values('k', ascending=False).head(20)
    J['dong_84new'] = [dict(area=r.area, dong=r.dong, n=int(r.n), k=int(r.k), pct=round(r.k / r.n * 100, 1), med=int(r.med)) for r in g.itertuples()]
    # 서울 구별
    J['seoul'] = {k: v for k, v in S.items() if k.startswith('서울')}
    # 하남 동별
    h = d[d.area == '경기 하남시']
    J['hanam'] = dict(total=table(h.assign(z='h'), 'z', price, new_from)['h'], dong=table(h, 'dong', price, new_from))
    # 하남에서 상한 아래로 팔린 지은 지 N년 안쪽 거래 보기(단지 · 면적 · 층 · 계약 월 · 금액까지만)
    def deals(x, n=12):
        x = x.sort_values('amt', ascending=False).head(n)
        return [dict(dong=r.dong, apt=r.단지명, ar=round(r.ar, 2), fl=r.층, ym=r.계약년월, amt=int(r.amt), yr=int(r.yr)) for r in x.itertuples()]
    hx = h[(h.amt <= price) & (h.yr >= new_from)]
    J['hanam_deals_84'] = deals(hx[hx['size'] == '84']); J['hanam_deals_59'] = deals(hx[hx['size'] == '59'])
    # 순위 상위 시군구에서 많이 팔린 단지(상한 아래 · 지은 지 N년 안쪽 84㎡)
    J['top_apts'] = {}
    for k, *_ in J['top_84new']:
        x = dn[(dn.area == k) & (dn.amt <= price)]
        v = x.groupby(['dong', '단지명']).agg(k=('amt', 'size'), med=('amt', 'median'), yr=('yr', 'first')).reset_index().sort_values('k', ascending=False).head(4)
        J['top_apts'][k] = [dict(dong=r.dong, apt=r.단지명, k=int(r.k), med=int(r.med), yr=int(r.yr)) for r in v.itertuples()]
    json.dump(J, open(a.out, 'w'), ensure_ascii=False, indent=1, default=int)
    print(json.dumps(dict(price=price, loan=c['loan'], pay=c['pay'], bind=c['bind'], loan_by_pay=c['loan_by_pay'], income_need=c['income_need'],
                          rows=len(d), total=J['total'], top3=[(k, v['k'], v['pct']) for k, v, *_ in J['top_84new'][:3]], out=a.out), ensure_ascii=False))


if __name__ == '__main__':
    main()

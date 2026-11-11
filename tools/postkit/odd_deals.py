#!/usr/bin/env python3
"""실거래 탐정 · 「이상한 거래」 후보 뽑기 (낭만 부동산 월요일 고정 코너용 · 11/12)

사용:
  python3 odd_deals.py --from 202608 --to 202610                       # 수도권(서울 · 경기 · 인천) 전체
  python3 odd_deals.py --from 202608 --to 202610 --region "경기도 하남시,서울특별시 송파구,서울특별시 강동구"
  python3 odd_deals.py --from 202609 --to 202611 --fetch --out /tmp/odd.json   # 국토부에서 그 기간을 새로 받아서
  인자:
    --from / --to   계약년월(YYYYMM) 범위
    --region        시군구 앞머리(쉼표로 여러 개). 기본 「서울특별시,경기도,인천광역시」
    --prefer        이 앞머리로 시작하는 곳을 같은 유형 안에서 위로(쉼표). 기본 하남 · 서울 동남권 · 경기 동부
    --fetch         rt.molit.go.kr 에서 그 기간 매매를 새로 받아 /home/claude/rtn/rawO/ 에 둔다(시 · 도 단위)
    --src           csv(국토부 내려받은 꼴) 또는 pkl 경로(쉼표). 없으면 rawO 의 가장 새 파일들 → 없으면 M2026.pkl
    --hist          신고가 판정용 과거 자료 pkl(쉼표). 기본 /home/claude/rtn/M2025.pkl,/home/claude/rtn/M2026.pkl
    --top           유형별 후보 수(기본 20)
    --out           결과 JSON 파일(없으면 화면에)
유형:
  A 같은 단지 · 같은 면적 · 같은 달 · 층 차이 3층 안인데 다른 거래들 중앙값보다 2억 넘게(그리고 15% 넘게) 싼 거래
    → 직거래 여부 · 해제 여부 · 층 · 견준 거래 수를 함께 적는다. 1~2층은 뺀다(저층 값 차이와 섞이지 않게).
  B 같은 날 · 같은 단지 · 같은 금액으로 3채 넘게 신고된 거래(해제 안 된 것)
  C 그때까지 그 단지 · 그 면적에서 가장 높은 값(신고가)으로 신고됐다가 해제된 거래가 몰린 단지
결과: {"meta":{...}, "A":[...], "B":[...], "C":[...]} — 사람 · 동 · 호수는 없다(단지 · 면적 · 층 · 계약일 · 금액 · 거래유형 · 해제일까지만).
"""
import argparse, glob, io, json, os, sys
import pandas as pd

RTN = '/home/claude/rtn/'
SIDO = {'서울특별시': '11000', '경기도': '41000', '인천광역시': '28000', '부산광역시': '26000', '대구광역시': '27000',
        '대전광역시': '30000', '울산광역시': '31000', '세종특별자치시': '36000'}
PREFER = '경기도 하남시,서울특별시 송파구,서울특별시 강동구,서울특별시 강남구,서울특별시 서초구,경기도 남양주시,경기도 구리시,경기도 광주시,경기도 성남시'


def load_csv(path):
    raw = open(path, 'rb').read().decode('cp949', errors='replace')
    lines = raw.splitlines()
    i = [k for k, l in enumerate(lines) if l.startswith('"NO"')][0]
    return pd.read_csv(io.StringIO('\n'.join(lines[i:])), dtype=str)


def load_any(path):
    return pd.read_pickle(path) if path.endswith('.pkl') else load_csv(path)


def fetch(regions, ym_from, ym_to):
    """국토부 실거래 공개시스템에서 시 · 도 단위로 매매를 받는다."""
    import datetime, calendar, requests
    S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
    ca = os.path.expanduser('~/.ccr/ca-bundle.crt')
    if os.path.exists(ca): S.verify = ca
    B = 'https://rt.molit.go.kr'
    S.get(B + '/pt/xls/xls.do?mobileAt=')
    fr = f'{ym_from[:4]}-{ym_from[4:]}-01'
    last = datetime.date(int(ym_to[:4]), int(ym_to[4:]), calendar.monthrange(int(ym_to[:4]), int(ym_to[4:]))[1])
    to = min(last, datetime.date.today()).isoformat()
    os.makedirs(RTN + 'rawO', exist_ok=True)
    outs = []
    for nm in sorted({r.split()[0] for r in regions}):
        if nm not in SIDO: continue
        out = f'{RTN}rawO/M_{SIDO[nm]}_{ym_from}_{ym_to}_{datetime.date.today():%m%d}.csv'
        if not (os.path.exists(out) and os.path.getsize(out) > 1000):
            d = dict(srhThingNo='A', srhDelngSecd='1', srhAddrGbn='1', srhLfstsSecd='1', sidoNm=nm, sggNm='전체', emdNm='전체',
                     loadNm='전체', areaNm='전체', hsmpNm='전체', mobileAt='', srhFromDt=fr, srhToDt=to, srhSidoCd=SIDO[nm],
                     srhSggCd='', srhEmdCd='', srhRoadNm='', srhLoadCd='', srhHsmpCd='', srhArea='', srhLrArea='',
                     srhFromAmount='', srhToAmount='', srhNewRonSecd='')
            h = {'Referer': B + '/pt/xls/xls.do?mobileAt='}
            S.post(B + '/pt/xls/ptXlsDownDataCheck.do', data=d, headers=h)
            r = S.post(B + '/pt/xls/ptXlsCSVDown.do', data=d, headers=h, timeout=600)
            open(out, 'wb').write(r.content)
        outs.append(out)
    return outs


def prep(d):
    d = d.copy()
    for c in ['시군구', '단지명', '번지', '해제사유발생일', '거래유형', '계약년월', '계약일', '층']:
        d[c] = d[c].astype(str).str.strip()
    d['면'] = d['전용면적(㎡)'].astype(float)
    d['금'] = d['거래금액(만원)'].astype(str).str.replace(',', '').astype(int)
    d['층n'] = pd.to_numeric(d['층'], errors='coerce')
    d['일'] = d['계약년월'] + d['계약일'].str.zfill(2)
    d['해제'] = d['해제사유발생일'] != '-'
    d['직'] = d['거래유형'] == '직거래'
    d['면k'] = d['면'].round(0).astype(int)          # 84.92 · 84.99 같은 타입 차이는 한 면적으로 묶음
    d['key'] = d['시군구'] + '|' + d['번지'] + '|' + d['단지명']
    return d


def rec(r):
    return {'계약일': r['일'], '면적': round(float(r['면']), 2), '층': r['층'], '금액': int(r['금']), '거래유형': r['거래유형'],
            '해제일': None if r['해제사유발생일'] == '-' else r['해제사유발생일']}


def pref_rank(sgg, prefer):
    return 0 if any(sgg.startswith(p) for p in prefer) else 1


def type_a(d, top, prefer, gap_min=20000, pct_min=0.15, floor_gap=3):
    out = []
    v = d[~d['해제']]
    for (key, mk, ym), g in v.groupby(['key', '면k', '계약년월']):
        if len(g) < 3: continue
        for i, r in g.iterrows():
            if pd.isna(r['층n']) or r['층n'] <= 2: continue
            o = g.drop(i)
            o = o[(~o['직']) & ((o['층n'] - r['층n']).abs() <= floor_gap) & (o['층n'] > 2)]
            if len(o) < 2: continue
            med = float(o['금'].median()); gap = med - r['금']
            if gap >= gap_min and gap / med >= pct_min:
                out.append({'시군구': r['시군구'], '단지': r['단지명'], '면적': mk, '계약월': ym, '싼거래': rec(r),
                            '견준거래수': int(len(o)), '견준중앙값': int(med), '견준최저': int(o['금'].min()), '견준층': sorted(o['층'].tolist(), key=int),
                            '차이': int(gap), '차이율': round(gap / med * 100, 1), '직거래': bool(r['직'])})
    out.sort(key=lambda x: (pref_rank(x['시군구'], prefer), -x['차이율']))
    return out[:top], len(out), sum(1 for x in out if x['직거래'])


def type_b(d, top, prefer, n_min=3):
    out = []
    v = d[~d['해제']]
    for (key, day, amt), g in v.groupby(['key', '일', '금']):
        if len(g) < n_min: continue
        r = g.iloc[0]
        out.append({'시군구': r['시군구'], '단지': r['단지명'], '계약일': day, '금액': int(amt), '채': int(len(g)),
                    '면적': sorted({round(float(a), 2) for a in g['면']}), '층': sorted(g['층'].tolist(), key=lambda s: int(s) if s.lstrip('-').isdigit() else 0),
                    '직거래': int(g['직'].sum()), '건축년도': str(r.get('건축년도', ''))})
    out.sort(key=lambda x: (pref_rank(x['시군구'], prefer), -x['채'], -x['금액']))
    return out[:top], len(out)


def type_c(d, hist, top, prefer):
    """기간 안 해제 거래 가운데, 그 계약일 전까지 같은 단지 · 같은 면적(해제 안 된 거래)의 가장 높은 값 이상이던 것."""
    c = d[d['해제']]
    hv = hist[~hist['해제']]
    hmax = {k: g[['일', '금']].sort_values('일').values.tolist() for k, g in hv[hv['key'].isin(set(c['key']))].groupby(['key', '면k'])}
    rows = []
    for _, r in c.iterrows():
        prev = [a for dday, a in hmax.get((r['key'], r['면k']), []) if dday < r['일']]
        if len(prev) < 3: continue
        if r['금'] >= max(prev):
            x = rec(r); x.update({'key': r['key'], '시군구': r['시군구'], '단지': r['단지명'], '면k': int(r['면k']), '직전최고': int(max(prev)), '앞선거래수': len(prev)})
            # 같은 값으로 다시 신고된 거래(해제 뒤 재신고)가 있는지
            again = hv[(hv['key'] == r['key']) & (hv['면k'] == r['면k']) & (hv['금'] == r['금']) & (hv['층'] == r['층']) & (hv['일'] >= r['일'])]
            x['같은층같은값재신고'] = int(len(again))
            rows.append(x)
    out = []
    for key, g in pd.DataFrame(rows).groupby('key') if rows else []:
        tot = d[d['key'] == key]
        out.append({'시군구': g['시군구'].iloc[0], '단지': g['단지'].iloc[0], '신고가해제': int(len(g)), '재신고없는것': int((g['같은층같은값재신고'] == 0).sum()),
                    '기간거래': int(len(tot)), '기간해제': int(tot['해제'].sum()),
                    '거래': [{k: v for k, v in x.items() if k not in ('key', '시군구', '단지')} for x in g.sort_values('계약일').to_dict('records')]})
    out.sort(key=lambda x: (pref_rank(x['시군구'], prefer), -x['재신고없는것'], -x['신고가해제']))
    return out[:top], len(out), len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='fr', required=True); ap.add_argument('--to', required=True)
    ap.add_argument('--region', default='서울특별시,경기도,인천광역시'); ap.add_argument('--prefer', default=PREFER)
    ap.add_argument('--fetch', action='store_true'); ap.add_argument('--src', default='')
    ap.add_argument('--hist', default=RTN + 'M2025.pkl,' + RTN + 'M2026.pkl')
    ap.add_argument('--top', type=int, default=20); ap.add_argument('--out', default='')
    a = ap.parse_args()
    regions = [x.strip() for x in a.region.split(',') if x.strip()]; prefer = [x.strip() for x in a.prefer.split(',') if x.strip()]
    if a.fetch: srcs = fetch(regions, a.fr, a.to)
    elif a.src: srcs = [s for s in a.src.split(',') if s]
    else:
        srcs = []
        for nm in sorted({r.split()[0] for r in regions}):
            fs = sorted(glob.glob(f'{RTN}rawO/M_{SIDO.get(nm, "x")}_*.csv'), key=os.path.getmtime)
            if fs: srcs.append(fs[-1])
        if not srcs: srcs = [RTN + 'M2026.pkl']
    inreg = lambda s: s.str.startswith(tuple(regions))
    cur = pd.concat([load_any(s) for s in srcs], ignore_index=True)
    cur = cur[inreg(cur['시군구'].astype(str))]
    cur = prep(cur)
    d = cur[(cur['계약년월'] >= a.fr) & (cur['계약년월'] <= a.to)]
    # 신고가 판정용: 과거 자료 + 이번 자료(겹치는 달은 이번 자료가 이김)
    hs = []
    for h in a.hist.split(','):
        if h and os.path.exists(h):
            x = pd.read_pickle(h); x = x[inreg(x['시군구'].astype(str))]; hs.append(x)
    if hs:
        h = prep(pd.concat(hs, ignore_index=True)); lo = cur['계약년월'].min()
        hist = pd.concat([h[h['계약년월'] < lo], cur], ignore_index=True)
    else: hist = cur
    A, na, na_dir = type_a(d, a.top, prefer)
    B, nb = type_b(d, a.top, prefer)
    C, nc, nc_deals = type_c(d, hist, a.top, prefer)
    meta = {'기간': [a.fr, a.to], '지역': regions, '자료': [os.path.basename(s) for s in srcs], '거래수': int(len(d)), '해제': int(d['해제'].sum()),
            '직거래': int((d['직'] & ~d['해제']).sum()), '마지막계약일': str(d['일'].max()),
            'A_전체': na, 'A_그중직거래': na_dir, 'B_전체': nb, 'C_단지': nc, 'C_신고가해제건': nc_deals}
    res = {'meta': meta, 'A': A, 'B': B, 'C': C}
    s = json.dumps(res, ensure_ascii=False, indent=1)
    if a.out:
        open(a.out, 'w').write(s); print(json.dumps(meta, ensure_ascii=False))
    else: print(s)


if __name__ == '__main__':
    main()

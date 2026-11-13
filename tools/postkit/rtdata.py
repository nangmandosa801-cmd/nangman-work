#!/usr/bin/env python3
"""국토부 실거래 공개시스템(rt.molit.go.kr)에서 아파트 매매 · 전월세를 받아 pkl 로 만든다(새 창 · 정기 작업용 · 11/14).
사용:
  python3 rtdata.py --from 202609 --to 202611                      # 수도권(서울 · 경기 · 인천) 매매 → /home/claude/rtn/M_budget_sudo.pkl
  python3 rtdata.py --from 202609 --to 202611 --sido 경기도 --sgg 하남시 --out /home/claude/rtn/M_hanam_recent.pkl
  python3 rtdata.py --from 202609 --to 202611 --rent --sido 경기도 --sgg 하남시 --out /home/claude/rtn/R_hanam_recent.pkl
결과 pkl 은 국토부 csv 열 그대로(글자) — 시군구 · 단지명 · 전용면적(㎡) · 계약년월 · 계약일 · 거래금액(만원) · 층 · 건축년도 · 해제사유발생일 · 거래유형 …
  · budget_map.py · odd_deals.py(--src) · helper/s20/*/ana.py 가 이 꼴을 읽는다. 해제 · 직거래는 빼지 않고 그대로 둔다(쓰는 쪽에서 뺀다).
주의: 하루 내려받기 100건 제한(사이트 안내) → 한 번에 시 · 도 × 기간 하나씩만 받는다. 기간은 1년까지. 받은 csv 는 /home/claude/rtn/rawR/ 에 두고 같은 날 다시 받지 않는다.
      사이트가 막혀 있거나 빈 파일이 오면 돌아가는 방법을 쓰지 않고 {"ok": false} 를 찍는다(그 실행은 자료 없이 못 쓰는 글을 건너뜀)."""
import argparse, calendar, datetime, io, json, os, sys
import pandas as pd

RTN = '/home/claude/rtn/'
SIDO = {'서울특별시': '11000', '경기도': '41000', '인천광역시': '28000', '부산광역시': '26000', '대구광역시': '27000',
        '대전광역시': '30000', '광주광역시': '29000', '울산광역시': '31000', '세종특별자치시': '36000'}


def load_csv(path):
    raw = open(path, 'rb').read().decode('cp949', errors='replace'); lines = raw.splitlines()
    i = [k for k, l in enumerate(lines) if l.startswith('"NO"')]
    if not i: return None
    return pd.read_csv(io.StringIO('\n'.join(lines[i[0]:])), dtype=str)


def fetch(sido, sgg, ym_from, ym_to, rent=False):
    import requests
    S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
    ca = os.path.expanduser('~/.ccr/ca-bundle.crt')
    if os.path.exists(ca): S.verify = ca
    B = 'https://rt.molit.go.kr'
    fr = f'{ym_from[:4]}-{ym_from[4:]}-01'
    last = datetime.date(int(ym_to[:4]), int(ym_to[4:]), calendar.monthrange(int(ym_to[:4]), int(ym_to[4:]))[1])
    to = min(last, datetime.date.today()).isoformat()
    os.makedirs(RTN + 'rawR', exist_ok=True)
    out = f"{RTN}rawR/{'R' if rent else 'M'}_{SIDO[sido]}_{sgg or 'all'}_{ym_from}_{ym_to}_{datetime.date.today():%m%d}.csv"
    if os.path.exists(out) and os.path.getsize(out) > 1000: return out
    S.get(B + '/pt/xls/xls.do?mobileAt=', timeout=60)
    d = dict(srhThingNo='A', srhDelngSecd='2' if rent else '1', srhAddrGbn='1', srhLfstsSecd='1', sidoNm=sido, sggNm=sgg or '전체', emdNm='전체',
             loadNm='전체', areaNm='전체', hsmpNm='전체', mobileAt='', srhFromDt=fr, srhToDt=to, srhSidoCd=SIDO[sido],
             srhSggCd='', srhEmdCd='', srhRoadNm='', srhLoadCd='', srhHsmpCd='', srhArea='', srhLrArea='',
             srhFromAmount='', srhToAmount='', srhNewRonSecd='')
    h = {'Referer': B + '/pt/xls/xls.do?mobileAt='}
    S.post(B + '/pt/xls/ptXlsDownDataCheck.do', data=d, headers=h, timeout=120)
    r = S.post(B + '/pt/xls/ptXlsCSVDown.do', data=d, headers=h, timeout=600)
    if r.status_code != 200 or b'"NO"' not in r.content[:20000]: return None
    open(out, 'wb').write(r.content); return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='fr', required=True); ap.add_argument('--to', required=True)
    ap.add_argument('--sido', default='서울특별시,경기도,인천광역시'); ap.add_argument('--sgg', default='')
    ap.add_argument('--rent', action='store_true'); ap.add_argument('--out', default='')
    a = ap.parse_args()
    frames = []; got = []
    for s in [x.strip() for x in a.sido.split(',') if x.strip()]:
        if s not in SIDO: print(json.dumps({'ok': False, 'why': '모르는 시 · 도: ' + s}, ensure_ascii=False)); sys.exit(2)
        p = None
        for k in range(3):                      # 끊기면 30초 쉬고 두 번 더
            try: p = fetch(s, a.sgg, a.fr, a.to, a.rent)
            except Exception as e: p = None; err = str(e)[:120]
            if p: break
            import time; time.sleep(30)
        if not p:
            print(json.dumps({'ok': False, 'why': f'{s} 받기 실패(사이트 막힘 · 제한 · 빈 응답)', 'err': locals().get('err', '')}, ensure_ascii=False)); sys.exit(1)
        df = load_csv(p)
        if df is None: print(json.dumps({'ok': False, 'why': f'{s} 응답에 표가 없음'}, ensure_ascii=False)); sys.exit(1)
        if a.sgg: df = df[df['시군구'].astype(str).str.contains(a.sgg)]     # 사이트는 이름으로 걸러 주지 않는다 → 받은 뒤 거른다
        frames.append(df); got.append((s, len(df)))
    d = pd.concat(frames, ignore_index=True)
    out = a.out or (RTN + ('R_recent.pkl' if a.rent else 'M_budget_sudo.pkl'))
    os.makedirs(os.path.dirname(out), exist_ok=True); d.to_pickle(out)
    ym = d['계약년월'].value_counts().sort_index().to_dict() if '계약년월' in d else {}
    print(json.dumps({'ok': True, 'out': out, 'rows': len(d), 'by_sido': got, 'by_month': ym, 'cols': list(d.columns)[:22]}, ensure_ascii=False))


if __name__ == '__main__':
    main()

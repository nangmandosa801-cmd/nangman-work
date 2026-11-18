#!/usr/bin/env python3
"""실거래 자료 늘 최신으로 (11/18 사용자 「실거래가 데이타는 네가 계속 업데이트 해」)
  python3 rt_refresh.py            # 오늘 것이 드라이브에 있으면 받아 오고, 없으면 국토부에서 새로 받아 드라이브에 올린다
  python3 rt_refresh.py --force    # 드라이브에 있어도 국토부에서 다시
결과(이 창): /home/claude/rtn/M_latest.pkl(수도권 아파트 매매) · R_latest.pkl(수도권 아파트 전월세) — 최근 4개월 계약(이번 달 포함)
       + /home/claude/rtn/latest.json(받은 날 · 줄 수 · 달별 건수 · 하남 요약)
드라이브: 「블로그/데이터/실거래/」에 M_latest.pkl.gz · R_latest.pkl.gz · latest.json (덮어쓰기 · 다른 창 · 정기 작업이 받아 씀)
국토부 하루 내려받기 제한(100건)이 있어 하루 한 번만 새로 받는다. 실패하면 어제 드라이브 것을 그대로 쓰고 {"fresh": false}."""
import datetime, gzip, json, os, shutil, subprocess, sys
import pandas as pd

RTN = '/home/claude/rtn/'; GAS = '/home/claude/helper/gas.py'; DRV = '블로그/데이터/실거래'
RT = '/home/claude/tools/postkit/rtdata.py'
os.makedirs(RTN, exist_ok=True)
today = datetime.date.today()


def sh(*a):
    r = subprocess.run(list(a), capture_output=True, text=True)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def drive_get():
    ok = True
    for f in ['latest.json', 'M_latest.pkl.gz', 'R_latest.pkl.gz']:
        rc, _ = sh('python3', GAS, 'fget', DRV, f, RTN + f)
        ok = ok and rc == 0 and os.path.exists(RTN + f)
    if not ok: return None
    for k in 'MR':
        with gzip.open(RTN + f'{k}_latest.pkl.gz', 'rb') as s, open(RTN + f'{k}_latest.pkl', 'wb') as d: shutil.copyfileobj(s, d)
    return json.load(open(RTN + 'latest.json', encoding='utf8'))


def num(s): return pd.to_numeric(s.astype(str).str.replace(',', ''), errors='coerce')


def summary(M, R):
    out = {'date': today.isoformat(), 'M_rows': len(M), 'R_rows': len(R),
           'M_by_month': M['계약년월'].value_counts().sort_index().to_dict(),
           'R_by_month': R['계약년월'].value_counts().sort_index().to_dict()}
    h = M[M['시군구'].str.contains('하남') & (M['해제사유발생일'].fillna('-').astype(str).str.strip().isin(['-', '']))]
    h = h[h['거래유형'].astype(str) != '직거래']
    out['hanam_M'] = {'rows': len(h), 'med84': int(num(h[num(h['전용면적(㎡)']).between(83, 86)]['거래금액(만원)']).median() or 0)}
    return out


def fresh():
    months = []; d = today.replace(day=1)
    for _ in range(4):
        months.append(d.strftime('%Y%m')); d = (d - datetime.timedelta(days=1)).replace(day=1)
    months = months[::-1]; fr, to = months[0], months[-1]
    for k, extra in [('M', []), ('R', ['--rent'])]:
        parts = []
        for ym in months:      # 달 하나씩(긴 기간은 사이트가 깨진 파일을 준다)
            rc, o = sh('python3', RT, '--from', ym, '--to', ym, *extra, '--out', RTN + f'{k}_{ym}.pkl')
            if rc != 0 or '"ok": true' not in o: return None, f'{k} {ym}: ' + o[-300:]
            parts.append(pd.read_pickle(RTN + f'{k}_{ym}.pkl'))
        pd.concat(parts, ignore_index=True).to_pickle(RTN + f'{k}_latest.pkl')
    M = pd.read_pickle(RTN + 'M_latest.pkl'); R = pd.read_pickle(RTN + 'R_latest.pkl')
    s = summary(M, R); s['from'] = fr; s['to'] = to
    json.dump(s, open(RTN + 'latest.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    for k in 'MR':
        with open(RTN + f'{k}_latest.pkl', 'rb') as a, gzip.open(RTN + f'{k}_latest.pkl.gz', 'wb') as b: shutil.copyfileobj(a, b)
    up = [sh('python3', GAS, 'fput', DRV, RTN + f)[0] == 0 for f in ['M_latest.pkl.gz', 'R_latest.pkl.gz', 'latest.json']]
    s['uploaded'] = all(up)
    return s, ''


def main():
    force = '--force' in sys.argv
    if not force:
        d = drive_get()
        if d and d.get('date') == today.isoformat():
            print(json.dumps({'ok': True, 'fresh': True, 'src': 'drive', 'date': d['date'], 'M_rows': d['M_rows'], 'R_rows': d['R_rows']}, ensure_ascii=False)); return
    s, err = fresh()
    if s:
        print(json.dumps({'ok': True, 'fresh': True, 'src': 'molit', **{k: s[k] for k in ['date', 'from', 'to', 'M_rows', 'R_rows', 'uploaded']}}, ensure_ascii=False)); return
    d = drive_get()
    if d:
        print(json.dumps({'ok': True, 'fresh': False, 'src': 'drive', 'date': d['date'], 'why': err}, ensure_ascii=False)); return
    print(json.dumps({'ok': False, 'why': err}, ensure_ascii=False)); sys.exit(1)


if __name__ == '__main__':
    main()

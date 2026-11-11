#!/usr/bin/env python3
"""실거래 탐정 · 하남 2026 매매 해제 62건 중 신고가였던 것 다시 세기.
다시 돌리기: (rawO 에 경기 2026 새 파일) python3 ana.py"""
import sys, glob, os, json, pandas as pd
sys.path.insert(0, '/home/claude/tools/postkit'); import odd_deals as o
R = '/home/claude/rtn/'
src = sorted(glob.glob(R + 'rawO/M_41000_202601_*.csv'), key=os.path.getmtime)[-1]
cur = o.prep(o.load_csv(src)); h26 = cur[cur['시군구'].str.startswith('경기도 하남시')].copy()
old = pd.read_pickle(R + 'M_hanam_2014_2026.pkl'); old = old[old['계약년월'].astype(str) < '202601']
old = o.prep(old)
hist = pd.concat([old, h26], ignore_index=True)
hv = hist[~hist['해제']]
c = h26[h26['해제']].copy()
c['간격'] = (pd.to_datetime(c['해제사유발생일']) - pd.to_datetime(c['일'])).dt.days
rows = []
for i, r in c.iterrows():
    g = hv[(hv['key'] == r['key']) & (hv['면k'] == r['면k'])]
    prev = g[g['일'] < r['일']]
    p25 = prev[prev['일'] >= '20250101']
    after = g[g['일'] > r['일']].sort_values('일')
    x = dict(o.rec(r)); x.update(단지=r['단지명'], 동=r['시군구'].split()[-1], 면k=int(r['면k']), 간격=int(r['간격']), 건축=str(r['건축년도']),
             앞선=int(len(prev)), 직전최고=int(prev['금'].max()) if len(prev) else None,
             직전최고일=prev.loc[prev['금'].idxmax(), '일'] if len(prev) else None,
             앞선25=int(len(p25)), 최고25=int(p25['금'].max()) if len(p25) else None,
             뒤거래=[o.rec(a) for _, a in after.iterrows()][:12], 뒤거래수=int(len(after)),
             등기=r['등기일자'])
    x['신고가'] = bool(len(prev) >= 1 and r['금'] >= x['직전최고'])
    x['신고가3'] = bool(len(prev) >= 3 and r['금'] >= x['직전최고'])
    rows.append(x)
J = {'src': os.path.basename(src), 'n': int(len(h26)), 'cancel': int(len(c)), 'direct': int((h26['직'] & ~h26['해제']).sum()),
     'last_day': h26['일'].max(), 'cancel_by_month': {k: int(v) for k, v in c['계약년월'].value_counts().sort_index().items()},
     'gap_med': float(c['간격'].median()), 'gap_over30': int((c['간격'] > 30).sum()), 'gap_le7': int((c['간격'] <= 7).sum()),
     'gap_max': int(c['간격'].max()),
     'new_high': sum(x['신고가'] for x in rows), 'new_high3': sum(x['신고가3'] for x in rows),
     'no_prev': sum(1 for x in rows if x['앞선'] == 0), 'direct_cancel': int(c['직'].sum()),
     'cancel_dong': {k: int(v) for k, v in c['시군구'].str.split().str[-1].value_counts().items()},
     'rows': sorted(rows, key=lambda x: x['계약일'])}
# 해제 안 된 거래 중 신고가 비율(견줄 기준)
nh = 0; nn = 0
for (k, mk), g in h26[~h26['해제']].groupby(['key', '면k']):
    pv = hv[(hv['key'] == k) & (hv['면k'] == mk)]
    for _, r in g.iterrows():
        p = pv[pv['일'] < r['일']]
        if len(p) >= 3:
            nn += 1; nh += int(r['금'] >= p['금'].max())
J['normal_newhigh'] = {'n': nn, 'k': nh, 'pct': round(nh / nn * 100, 1)}
cc = [x for x in rows if x['앞선'] >= 3]
J['cancel_newhigh_base'] = {'n': len(cc), 'k': sum(x['신고가3'] for x in rows), 'pct': round(sum(x['신고가3'] for x in rows) / len(cc) * 100, 1)}
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in J.items() if k != 'rows'}, ensure_ascii=False))
for x in J['rows']:
    if x['신고가']: print(x['계약일'], x['동'], x['단지'], x['면k'], x['층'], x['금액'], x['거래유형'], '해제', x['해제일'], x['간격'], '직전최고', x['직전최고'], x['직전최고일'], '앞선', x['앞선'], '뒤', x['뒤거래수'])
# ── 해제 뒤 같은 날 · 같은 층 · 같은 값으로 다시 신고된 줄(해제 안 됨)이 있는지 = 다시 신고
hv26 = h26[~h26['해제']]
for x in J['rows']:
    m = hv26[(hv26['단지명'] == x['단지']) & (hv26['시군구'].str.endswith(x['동'])) & (hv26['면k'] == x['면k']) & (hv26['일'] == x['계약일']) & (hv26['층'] == x['층']) & (hv26['금'] == x['금액'])]
    x['다시신고'] = int(len(m)); x['다시신고등기'] = m['등기일자'].iloc[0] if len(m) else None
    # 진짜 해제: 뒤 거래 중 그 값 이상이 나온 첫 날
    up = [a for a in x['뒤거래'] if a['금액'] >= x['금액']]
    x['뒤에그값이상'] = up[0] if up else None
    x['뒤첫거래'] = x['뒤거래'][0] if x['뒤거래'] else None
R_ = J['rows']; NH = [x for x in R_ if x['신고가']]
J['re_all'] = sum(1 for x in R_ if x['다시신고']); J['re_newhigh'] = sum(1 for x in NH if x['다시신고'])
J['true_all'] = len(R_) - J['re_all']; J['true_newhigh'] = len(NH) - J['re_newhigh']
J['re_newhigh_reg'] = sum(1 for x in NH if x['다시신고'] and x['다시신고등기'] not in (None, '-'))
J['true_newhigh_list'] = [{k: x[k] for k in ('계약일', '동', '단지', '면k', '층', '금액', '해제일', '간격', '직전최고', '뒤첫거래', '뒤에그값이상', '뒤거래수')} for x in NH if not x['다시신고']]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print({k: J[k] for k in ('re_all', 're_newhigh', 'true_all', 'true_newhigh', 're_newhigh_reg')})
for x in J['true_newhigh_list']: print(x)
# ── 그 값 이상 해제 안 된 거래가 같은 날이나 뒤에 있었나(같은 단지 · 같은 면적)
for x in J['rows']:
    g = hv26[(hv26['단지명'] == x['단지']) & (hv26['시군구'].str.endswith(x['동'])) & (hv26['면k'] == x['면k']) & (hv26['일'] >= x['계약일']) & (hv26['금'] >= x['금액'])]
    x['그값이상'] = int(len(g)); x['그값이상첫'] = g.sort_values('일')['일'].iloc[0] if len(g) else None
    later = hv26[(hv26['단지명'] == x['단지']) & (hv26['시군구'].str.endswith(x['동'])) & (hv26['면k'] == x['면k']) & (hv26['일'] > x['계약일'])]
    x['뒤최고'] = int(later['금'].max()) if len(later) else None
NH = [x for x in J['rows'] if x['신고가']]
J['nh_reached'] = sum(1 for x in NH if x['그값이상']); J['nh_not_reached'] = [(x['단지'], x['면k'], x['금액'], x['뒤최고']) for x in NH if not x['그값이상']]
J['re_newhigh_noreg'] = [(x['단지'], x['계약일'], x['다시신고등기']) for x in NH if x['다시신고'] and x['다시신고등기'] in (None, '-')]
J['nh_gap'] = {'le7': sum(1 for x in NH if x['간격'] <= 7), 'mid': sum(1 for x in NH if 7 < x['간격'] <= 30), 'over30': sum(1 for x in NH if x['간격'] > 30), 'med': float(pd.Series([x['간격'] for x in NH]).median())}
J['all_gap'] = {'le7': J['gap_le7'], 'mid': J['cancel'] - J['gap_le7'] - J['gap_over30'], 'over30': J['gap_over30']}
J['re_gap_med'] = float(pd.Series([x['간격'] for x in J['rows'] if x['다시신고']]).median()); J['true_gap_med'] = float(pd.Series([x['간격'] for x in J['rows'] if not x['다시신고']]).median())
J['nh_jump'] = sorted([(x['단지'], x['면k'], x['금액'] - x['직전최고']) for x in NH], key=lambda t: -t[2])[:6]
json.dump(J, open('ana.json', 'w'), ensure_ascii=False, indent=1)
print({k: J[k] for k in ('nh_reached', 'nh_not_reached', 're_newhigh_noreg', 'nh_gap', 'all_gap', 're_gap_med', 'true_gap_med', 'nh_jump')})

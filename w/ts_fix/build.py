import json, re, os, sys, subprocess, html as H
sys.path.insert(0, '/home/claude/tools/tistory'); sys.path.insert(0, '/home/claude/w/ts_fix')
import viz2d as V
from spec import S, T
tabs = json.load(open('/tmp/ts_tables.json')); meta = {o['no']: o for o in json.load(open('/tmp/ts.json'))}
OUT = '/home/claude/w/ts_fix/out'; os.makedirs(OUT, exist_ok=True)
def num(s):
    s = s.replace(',', '').replace(' ', '')
    m = re.match(r'^[+]?(\d+(?:\.\d+)?)억(?:(\d+)만)?', s)
    if m: return float(m.group(1)) * 10000 + float(m.group(2) or 0)
    m = re.match(r'^[+]?(\d+(?:\.\d+)?)(만원|만|%|건|세대|곳|배|ha|㎡)?$', s.replace('원', '') if s.endswith('만원') else s)
    return float(m.group(1)) if m else None
def table_png(rows, path, head):
    h = '<table style="width:100%;border-collapse:collapse;font-size:30px;font-family:\'Noto Sans CJK KR\',sans-serif">'
    for i, r in enumerate(rows):
        tg = 'th' if i == 0 else 'td'; st = 'background:#191F28;color:#fff;' if i == 0 else ('background:#F4F6F8;' if i % 2 == 0 else '')
        h += '<tr>' + ''.join(f'<{tg} style="{st}padding:16px 14px;border:1px solid #D1D6DB;text-align:left;line-height:1.45">{H.escape(c)}</{tg}>' for c in r) + '</tr>'
    page = f'<html><head><meta charset="utf-8"></head><body style="margin:0;padding:36px;background:#fff;width:1128px"><div style="font:900 44px \'Noto Sans CJK KR\';color:#191F28;margin-bottom:24px">{H.escape(head)}</div>{h}</table></body></html>'
    open('/tmp/_t.html', 'w').write(page)
    subprocess.run(['wkhtmltoimage', '-q', '--width', '1200', '/tmp/_t.html', path], check=True)
words = lambda t: set(w for w in re.split(r'[\s,·]+', t) if len(w) >= 2 and not re.match(r'\d', w))
res = []
for no, (title, cat, tags) in S.items():
    rows = T.get(no) or (tabs.get(no) or [[]])[0]
    rows = [r for r in rows if any(r)][:7]
    core = title.split(',')[0]
    d = f'{OUT}/{no}'; os.makedirs(d, exist_ok=True)
    V.thumb(f'{d}/01.jpg')
    table_png(rows, f'{d}/02.png', core + ' 비교표')
    body = rows[1:]; kind = 'cards'
    def unit(x):
        x = x.replace(' ', '')
        return 'money' if re.search(r'억|만원', x) else 'pct' if '%' in x else 'cnt' if re.search(r'건|세대|곳|가구|호', x) else 'num'
    PREF = r'분양가|전세|매매|시세|평당|중앙값|금액|값|가격|평균|상승률|보증금'
    cols = sorted(range(1, max(len(r) for r in rows)), key=lambda c: (0 if re.search(PREF, rows[0][c] if len(rows[0]) > c else '') else 1, c))
    for c in cols:
        cells = [r[c] if len(r) > c else '' for r in body[:5]]
        vals = [num(x) for x in cells]
        if len(body) >= 2 and all(v is not None for v in vals) and len(set(vals)) > 1 and len(set(unit(x) for x in cells)) == 1 and max(len(x) for x in cells) <= 11:
            names = [r[0][:12] for r in body[:5]]; hi = vals.index(max(vals))
            labs = {i: r[c] for i, r in enumerate(body[:5])}
            try:
                V.bars(core + ' · ' + rows[0][c], names, vals, hi, f'{d}/03.png', fmt=lambda v, _l=labs, _v=vals: _l[_v.index(v)])
                kind = 'bars'; break
            except Exception: pass
    if kind == 'cards':
        short = all(len(r) > 1 and len(r[1]) <= 9 for r in body[:3])
        if short:
            V.cards3(core, [(r[0][:14], r[1], (r[2] if len(r) > 2 else '')[:22]) for r in body[:3]], f'{d}/03.png')
        else:
            kind = 'steps'
            V.steps(core + ' 한눈에', [(r[0][:14], ' · '.join(r[1:])[:40]) for r in body[:5]], f'{d}/03.png')
    # 함께 보면 좋은 글
    w0 = words(title + ' ' + meta[no]['title'])
    cands = sorted([(len(w0 & words(t2 + ' ' + meta[n2]['title'])), -abs(int(n2) - int(no)), n2) for n2, (t2, c2, _) in S.items() if n2 != no and c2 == cat], reverse=True)[:3]
    rel = [(S[c[2]][0], f'https://talk7921.tistory.com/{c[2]}') for c in cands]
    lead = re.sub(r'\s+', ' ', meta[no]['title']).strip().rstrip('.') + '.'
    th = ''.join('<tr>' + ''.join(f'<{"th" if i == 0 else "td"} style="border:1px solid #ccc;padding:6px">{H.escape(c)}</{"th" if i == 0 else "td"}>' for c in r) + '</tr>' for i, r in enumerate(rows))
    alt = [f'{core} 대표 그림', f'{core} 비교표', f'{core} ' + {'bars':'그래프','cards':'숫자 카드','steps':'한눈에 보기'}[kind]]
    top = (f'<p><b>{H.escape(lead)}</b></p>\n<table style="width:100%;border-collapse:collapse">{th}</table>\n')
    rel_html = '<h3>함께 보면 좋은 글</h3>\n' + '\n'.join(f'<p>· <a href="{u}">{H.escape(t)}</a></p>' for t, u in rel)
    page = (f'<!doctype html><html><head><meta charset="utf-8"><title>{H.escape(title)}</title></head><body style="max-width:760px;margin:20px auto;font-size:17px;line-height:1.8">'
            f'<p style="color:#c00;font-weight:700">새 제목: {H.escape(title)}<br>카테고리: {cat}<br>태그: {H.escape(tags)}</p><hr>'
            f'<p style="color:#c00;font-weight:700">▼ [맨 위에 넣기] 아래 굵은 한 줄 + 표 (글자 그대로 붙여 넣기)</p>{top}'
            f'<p style="color:#c00;font-weight:700">▼ 01.jpg (대표 지정) · 대체텍스트: {alt[0]}</p><img src="01.jpg" width="380">'
            f'<p style="color:#c00;font-weight:700">▼ 02.png · 대체텍스트: {alt[1]} — 첫 소제목 바로 위</p><img src="02.png" width="380">'
            f'<p style="color:#c00;font-weight:700">▼ 03.png · 대체텍스트: {alt[2]} — 둘째 소제목 바로 위</p><img src="03.png" width="380">'
            f'<hr><p style="color:#c00;font-weight:700">▼ [글 맨 끝 · 원래 끝 문단 아래에 넣기]</p>{rel_html}</body></html>')
    open(f'{d}/보완_{no}.html', 'w').write(page)
    res.append(dict(no=no, title=title, cat=cat, tags=tags, kind=kind, rel=[r[1][-2:] for r in rel], alt=alt))
json.dump(res, open('/home/claude/w/ts_fix/res.json', 'w'), ensure_ascii=False, indent=0)
print(len(res), sum(1 for r in res if r['kind'] == 'bars'))

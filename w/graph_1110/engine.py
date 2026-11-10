#!/usr/bin/env python3
"""그래프 교체(11/10) 엔진: specs.py 의 지정대로 옛 그림 데이터에서 5개 이하 막대/카드 3개를 뽑아 fig2d 코드로 만든다.
  python3 engine.py gen            → 모든 spec 의 v2 그림 생성 + fig.py 끝에 v2 블록 붙임(/tmp/insp/*.json 필요)
"""
import json, os, re, sys
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
H = '/home/claude/helper/'
MARK = '# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ===='

def near(a, b):
    best = None
    for t in a.get('tx', []):
        if not any(c.isdigit() for c in t[0]): continue
        p = t[2] if a['horiz'] else t[1]
        dd = abs(p - b[3])
        if best is None or dd < best[0]: best = (dd, t[0])
    return best[1] if best and best[0] < 0.45 else ''

def clean_txt(t):
    t = re.sub(r'\s{2,}\(.*?\)\s*$', '', t)      # '144.2  (401건)' → '144.2'
    t = re.sub(r'\s+\(\d[\d,]*건.*?\)\s*$', '', t)
    t = re.sub(r'\s{2,}', ' ', t).strip()
    return t

def clean_lab(l):
    l = l.strip()
    m = re.match(r'^(.*?)\s*\((.*)\)\s*(.*)$', l)
    if m and '|' not in l:
        return (m.group(1) + (' ' + m.group(3) if m.group(3) else '')).strip() + '|' + m.group(2)
    m = re.match(r'^(.*\S)\s+(\S+동 · \d{4})$', l)
    if m: return m.group(1) + '|' + m.group(2)
    return l

def resolve(folder, fname, sp):
    j = json.load(open('/tmp/insp/' + folder.replace('/', '_') + '.json'))
    g = [x for x in j['figs'] if x['file'] == fname]
    head = sp.get('head'); note = sp.get('note')
    if g:
        ft = sorted(g[0]['figtexts'], key=lambda x: -x[1])
        head = head or ft[0][0]
        if note is None and len(ft) > 1: note = ft[1][0]
    if note:
        parts = note.replace('\n', ' ').split(' · ')
        while len(parts) > 1 and len(' · '.join(parts)) > 50: parts.pop()
        note = ' · '.join(parts)[:60]
    if sp['k'] == 'c':
        return dict(k='c', head=head, cards=sp['cards'], note=note)
    if 'items' in sp:
        items = [tuple(i) for i in sp['items']]
    else:
        a = g[0]['axes'][sp.get('ax', 0)]; bl = a['bl']
        idx = sp.get('idx') or list(range(len(bl)))
        items = []
        for i in idx:
            b = bl[i]
            lab = sp.get('lab', {}).get(i) or clean_lab(b[0])
            txt = sp.get('txt', {}).get(i) or (clean_txt(near(a, b)) + sp.get('suf', ''))
            items.append((lab, abs(b[1]) if not sp.get('zero', {}).get(i) else 0, txt, i == sp.get('hi')))
    return dict(k='b', head=head, items=items, note=note)

def code(out, r):
    if r['k'] == 'c':
        return f"cards3({out!r}, {r['head']!r}, {r['cards']!r}, note={r['note']!r})"
    return f"bars({out!r}, {r['head']!r}, {r['items']!r}, note={r['note']!r})"

def gen(only=None):
    from specs import SPEC
    import fig2d
    res = {}
    for key, sp in SPEC.items():
        folder, fname = key.rsplit('/', 1)
        if only and folder not in only: continue
        r = resolve(folder, fname, sp)
        out = 'img/' + fname.replace('.png', '_v2.png')
        d = H + folder; os.makedirs(d + '/img', exist_ok=True)
        cwd = os.getcwd(); os.chdir(d)
        try:
            (fig2d.cards3 if r['k'] == 'c' else fig2d.bars)(out, r['head'], r['cards'] if r['k'] == 'c' else r['items'], note=r['note'])
        finally: os.chdir(cwd)
        res.setdefault(folder, []).append((fname, code(out, r), r))
    for folder, lst in res.items():
        fp = H + folder + '/fig.py'
        if os.path.exists(fp):
            s = open(fp).read().split('\n' + MARK)[0].rstrip('\n')
            blk = ['', MARK, "import sys; sys.path.insert(0, '/home/claude/helper/pg')", 'from fig2d import bars, cards3'] + [c for _, c, _ in lst] + ["print('v2 ok')", '']
            open(fp, 'w').write(s + '\n' + '\n'.join(blk))
    json.dump({f: [(a, r) for a, _, r in l] for f, l in res.items()}, open(os.path.dirname(os.path.abspath(__file__)) + '/resolved.json', 'w'), ensure_ascii=False, indent=0)
    return res

if __name__ == '__main__':
    r = gen(set(sys.argv[2:]) or None)
    print(json.dumps({'folders': len(r), 'figs': sum(len(v) for v in r.values())}))

#!/usr/bin/env python3
"""낭만 부동산 helper 폴더(post.html · urls.json · img/) → 어사이드용 txt + 사진 (11/5 발행 방식 변경)
사용: python3 html2aside.py <폴더> <글이름> [--up]
  → /home/claude/w/aside_out/<글이름>.txt, /home/claude/w/aside_out/<글이름>/01.jpg …(01 = 썸네일 · 대표 사진)
  --up: 드라이브 「블로그/협업/4_어사이드/원고」(txt) · 「…/원고/<글이름>」(사진) 에 올림
표시: [사진 NN] · [소제목] · [표] 칸 | 칸 … [/표] · 링크는 「글자 (주소)」 · 맨 아래 「태그:」
"""
import sys, os, re, json, glob, subprocess
from bs4 import BeautifulSoup, NavigableString
from PIL import Image

d, name = os.path.abspath(sys.argv[1]), sys.argv[2]
O = f'/home/claude/w/aside_out/{name}'; os.makedirs(O, exist_ok=True)
for f in glob.glob(O + '/*.jpg'): os.remove(f)
urls = json.load(open(f'{d}/urls.json'))
u2f = {}
for k, u in urls.items():
    m = glob.glob(f'{d}/img/*_{k}.png')
    if m: u2f[u] = m[0]
soup = BeautifulSoup(open(f'{d}/post.html', encoding='utf8').read(), 'html.parser')
TITLE = re.search(r"TITLE\s*=\s*['\"](.+?)['\"]", open(f'{d}/mk.py', encoding='utf8').read()).group(1)
k = 0
def photo(path):
    global k; k += 1
    Image.open(path).convert('RGB').save(f'{O}/{k:02d}.jpg', quality=92)
    return f'[사진 {k:02d}]'
def text(el):
    out = []
    for c in el.descendants:
        if isinstance(c, NavigableString):
            if c.parent.name == 'a': continue
            out.append(str(c))
        elif c.name == 'a':
            h = c.get('href', ''); t = c.get_text()
            out.append(f'{t} ({h})' if h.startswith('http') and h != t else t)
        elif c.name == 'br': out.append('\n')
        elif c.name in ('p', 'tr') and out and not out[-1].endswith('\n'): out.append('\n')
    lines = [re.sub(r'\s+', ' ', l).strip() for l in ''.join(out).split('\n')]
    return '\n'.join(l for l in lines if l)

out = [f'제목: {TITLE}', '']
thumb = glob.glob(f'{d}/img/*_thumb.png')
if thumb: out += [photo(thumb[0]) + '  ← 대표 사진', '']
tags = ''
def walk(nodes):
    global tags
    for el in nodes:
        if isinstance(el, NavigableString) or el.name is None: continue
        if el.name == 'img':
            f = u2f.get(el.get('src'));
            if f: out.append(photo(f))
            continue
        imgs = el.find_all('img') if el.name in ('p', 'span') else []
        if imgs:
            for im in imgs:
                f = u2f.get(im.get('src'))
                if f: out.append(photo(f))
            cap = text(el)
            if cap: out.append(cap)
            continue
        if el.name == 'table':
            trs = [[text(td) for td in tr.find_all('td', recursive=False)] for tr in el.find_all('tr', recursive=False) or el.find_all('tr')]
            trs = [r for r in trs if any(r)]
            if not trs: continue
            flat = '\n'.join(c for r in trs for c in r if c)
            if flat.count('#') >= 5: tags = re.sub(r'^태그\s*', '', flat.replace('\n', ' ')); continue
            if all(len([c for c in r if c]) <= 1 for r in trs) or len(trs) == 1:
                out.append('')
                for r in trs:
                    for c in r:
                        if c: out.append(c.replace('\n', ' · ') if len(trs) == 1 and len(r) > 1 else c)
                out.append(''); continue
            out.extend(['[표]'] + [' | '.join(c.replace('\n', ' ') for c in r) for r in trs] + ['[/표]'])
            continue
        if el.name == 'p':
            t = text(el)
            if not t: continue
            st = el.get('style', '')
            if 'font-size:34px' in st and t == TITLE: continue
            if re.search(r'font-size:2[3-7]px', st) and 'font-weight:700' in st: out.extend(['', f'[소제목] {t}', '']); continue
            if t.startswith('#') and t.count('#') >= 5: tags = t; continue
            out.extend([t.replace('\n', ' '), '']); continue
        walk(el.children)
walk(soup.children)
if tags: out += ['', f'태그: {tags}']
s = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip() + '\n'
# 11/12 같이 보면 좋은 글: [같이 보면 좋은 글] 표식 · 「▶ 제목 | 주소」 · 태그보다 뒤(글 맨 끝)
m = re.search(r'\[소제목\] 같이 보면 좋은 글\n(.*?)(?=\n\n태그:|\Z)', s, re.S)
if m:
    lines = [f'▶ {a.strip()} | {b}' for a, b in re.findall(r'▶ (.+?) \((https?://[^)]+)\)', m.group(1))]
    s = s.replace(m.group(0), '').rstrip() + '\n\n[같이 보면 좋은 글]\n' + '\n'.join(lines) + '\n'
    s = re.sub(r'\n{3,}', '\n\n', s)
open(f'{O}.txt', 'w', encoding='utf8').write(s)
bad = re.findall(r'##|\*\*|<div|<p|\[CALL\]', s)
print(json.dumps({'name': name, 'photos': k, 'chars': len(s), 'bad': bad}, ensure_ascii=False))
if '--up' in sys.argv:
    G = '/home/claude/helper/gas.py'; base = '블로그/협업/4_어사이드/원고'
    subprocess.run(['python3', G, 'fput', base, f'{O}.txt'], check=True, capture_output=True)
    for f in sorted(glob.glob(O + '/*.jpg')):
        subprocess.run(['python3', G, 'fput', f'{base}/{name}', f], check=True, capture_output=True)
    print('uploaded', name)

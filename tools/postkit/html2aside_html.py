#!/usr/bin/env python3
"""helper 폴더 post.html → 어사이드가 보고 쓸 원고 html (모양 그대로 · 그림마다 「사진 NN」 표시 · 01 = 대표)
사용: python3 html2aside_html.py <폴더> nangman_<이름> [--up]  → /home/claude/w/aside_out/nangman_<이름>.html"""
import sys, re, json, glob, subprocess, html as H
d, name = sys.argv[1], sys.argv[2]
sys.path.insert(0, '/home/claude/tools/postkit'); from vis2img import prep
s, vm = prep(d)
urls = json.load(open(f'{d}/urls.json'))
T = re.search(r"TITLE\s*=\s*['\"](.+?)['\"]", open(f'{d}/mk.py', encoding='utf8').read()).group(1)
k = [1]
KW = T.split(',')[0].strip()   # 11/18 사용자: 사진 설명 칸 = 사진 제목 · 검색 단어, 썸네일 = 핵심 검색어
CAP = lambda c: f'<p style="font-size:14px;color:#0a58ca;font-weight:700;">사진 설명 칸: {H.escape(c[:60])}</p>'
def lab(m):
    g = m.group(0)
    if 'lh3.googleusercontent' not in g and 'vis://' not in g: return g
    if 'vis://' in g:
        import base64; u = re.search(r'src="([^"]+)"', g).group(1)
        g = g.replace(u, 'data:image/png;base64,' + base64.b64encode(open(vm[u], 'rb').read()).decode())
    k[0] += 1
    alt = (re.search(r'alt="([^"]*)"', g) or [None, ''])[1].strip()
    if not alt or re.fullmatch(r'(시각화|그림|image|img)\s*\d*', alt):   # 이름 없는 그림은 바로 위 소제목으로
        hs = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', SRC[:m.start()], re.S)
        alt = re.sub(r'<[^>]+>|[?？]', '', hs[-1]).strip() if hs else '핵심 숫자 요약'
    cap = alt if alt and KW.split()[0] in alt else ' '.join(x for x in [KW, alt] if x)
    return f'<p style="font-size:14px;color:#c00;font-weight:700;">▼ 사진 {k[0]:02d}.jpg</p>' + CAP(cap) + g
SRC = s
s = re.sub(r'<img[^>]+>', lab, s)
th = urls.get('thumb', '')
top = (f'<p style="font-size:14px;color:#c00;font-weight:700;">제목 칸: {H.escape(T)}</p>'
       f'<p style="font-size:14px;color:#c00;font-weight:700;">▼ 사진 01.jpg (대표 사진)</p>' + CAP(KW) + f'<img src="{th}" width="400"><hr>') if th else ''
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{H.escape(T)}</title></head><body style="max-width:760px;margin:20px auto;padding:0 16px;">{top}{s}</body></html>'
out = f'/home/claude/w/aside_out/{name}.html'; open(out, 'w', encoding='utf8').write(doc)
print(name, 'photos', k[0])
if '--up' in sys.argv:
    subprocess.run(['python3', '/home/claude/helper/gas.py', 'fput', '블로그/협업/4_어사이드/원고', out], check=True, capture_output=True); print('uploaded')

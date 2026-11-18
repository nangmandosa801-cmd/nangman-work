#!/usr/bin/env python3
"""helper 폴더 post.html → 어사이드가 보고 쓸 원고 html (모양 그대로 · 그림마다 「사진 NN」 표시 · 01 = 대표)
사용: python3 html2aside_html.py <폴더> nangman_<이름> [--up]  → /home/claude/w/aside_out/nangman_<이름>.html"""
import sys, re, json, glob, subprocess, html as H
d, name = sys.argv[1], sys.argv[2]
sys.path.insert(0, '/home/claude/tools/postkit'); from vis2img import prep
s, vm = prep(d)
urls = json.load(open(f'{d}/urls.json'))
T = re.search(r"TITLE\s*=\s*['\"](.+?)['\"]", open(f'{d}/mk.py', encoding='utf8').read()).group(1)
k = [1]; KW = re.split(r'[,，|]', T)[0].strip(); CAP = [f'01.jpg\t{KW}']
CS = 'font-size:13px;color:#0a6;font-weight:700;'
def lab(m):
    g = m.group(0)
    if 'lh3.googleusercontent' not in g and 'vis://' not in g: return g
    if 'vis://' in g:
        import base64; u = re.search(r'src="([^"]+)"', g).group(1)
        g = g.replace(u, 'data:image/png;base64,' + base64.b64encode(open(vm[u], 'rb').read()).decode())
    k[0] += 1; a = re.search(r'alt="([^"]*)"', g); cap = (a.group(1).strip() if a and a.group(1).strip() else '')
    cap = cap if KW in cap else (f'{KW} {cap}'.strip()); CAP.append(f'{k[0]:02d}.jpg\t{cap}')
    return f'<p style="font-size:14px;color:#c00;font-weight:700;">▼ 사진 {k[0]:02d}.jpg</p><p style="{CS}">└ 사진 설명 칸: {H.escape(cap)}</p>' + g
s = re.sub(r'<img[^>]+>', lab, s)
th = urls.get('thumb', '')
top = (f'<p style="font-size:14px;color:#c00;font-weight:700;">제목 칸: {H.escape(T)}</p>'
       f'<p style="font-size:14px;color:#c00;font-weight:700;">▼ 사진 01.jpg (대표 사진)</p><p style="{CS}">└ 사진 설명 칸: {H.escape(KW)}</p><img src="{th}" width="400"><hr>') if th else ''
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{H.escape(T)}</title></head><body style="max-width:760px;margin:20px auto;padding:0 16px;">{top}{s}</body></html>'
out = f'/home/claude/w/aside_out/{name}.html'; open(out, 'w', encoding='utf8').write(doc)
s_cap = '파일\t사진 설명 칸에 넣을 말(01 = 썸네일 · 핵심 검색어)\n' + '\n'.join(CAP) + '\n'
cap_out = f'/home/claude/w/aside_out/{name}_사진설명.txt'; open(cap_out, 'w', encoding='utf8').write(s_cap)
print(name, 'photos', k[0])
if '--up' in sys.argv:
    for f in (out, cap_out): subprocess.run(['python3', '/home/claude/helper/gas.py', 'fput', '블로그/협업/4_어사이드/원고', f], check=True, capture_output=True)
    print('uploaded')

#!/usr/bin/env python3
"""발행된 네이버 글 점검: 대표 사진이 썸네일 카드인지 · 문의 배너가 있는지 · 기호 찌꺼기.
사용: python3 postcheck.py <blogId> <logNo> [logNo ...]   → JSON 줄
판정: thumb_ok(대표 = 글자 카드: 위 띠가 진한 초록/남색) · banners(가로로 긴 흰 바탕 문의 그림 수) · junk(##, **, [CALL], <div 글자)"""
import sys, re, json, subprocess, io, html as H
from PIL import Image
def get(u, ref):
    return subprocess.run(['curl', '-s', '-L', '-A', 'Mozilla/5.0', '-e', ref, u], capture_output=True, timeout=40).stdout
def img(u, ref):
    try: return Image.open(io.BytesIO(get(u, ref))).convert('RGB')
    except Exception: return None
def is_card(im):
    w, h = im.size; px = [im.getpixel((int(w * x), int(h * 0.03))) for x in (0.05, 0.5, 0.95)]
    return all(sum(p) < 220 for p in px)          # 맨 위 띠가 어두움(카드 머리띠)
def is_banner(im):
    w, h = im.size
    if not (2.0 < w / h < 4.0): return False
    s = im.resize((100, max(1, int(100 * h / w)))); px = list(s.getdata())
    btn = sum(1 for p in px if abs(p[0] - 31) < 35 and abs(p[1] - 111) < 35 and abs(p[2] - 209) < 35) / len(px)
    return btn > 0.02                              # 파란 「문자 · 전화」 단추
def check(blog, no):
    ref = f'https://blog.naver.com/{blog}'
    t = get(f'https://blog.naver.com/PostView.naver?blogId={blog}&logNo={no}&redirect=Dlog&widgetTypeCall=true&directAccess=false', ref).decode('utf-8', 'replace')
    og = re.search(r'property="og:image" content="([^"]+)"', t)
    srcs = [H.unescape(s) for s in re.findall(r'data-lazy-src="([^"]+)"', t)] or [H.unescape(s) for s in re.findall(r'<img[^>]+src="(https://postfiles[^"]+)"', t)]
    srcs = [s.split('?')[0] + '?type=w773' for s in srcs]
    thumb = None
    if og:
        im = img(H.unescape(og.group(1)), ref); thumb = bool(im and is_card(im))
    elif srcs:
        im = img(srcs[0], ref); thumb = bool(im and is_card(im))
    nb = 0
    for s in srcs:
        im = img(s, ref)
        if im and is_banner(im): nb += 1
    m = t.split('se-main-container', 1)[-1] if 'se-main-container' in t else ''
    m = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', m, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', m)
    junk = [k for k in ['##', '**', '[CALL]', '&lt;div'] if k in txt]
    return {'logNo': no, 'imgs': len(srcs), 'thumb_ok': thumb, 'banners': nb, 'junk': junk,
            'ok': bool(thumb) and nb >= 1 and not junk}
if __name__ == '__main__':
    for no in sys.argv[2:]: print(json.dumps(check(sys.argv[1], no), ensure_ascii=False))

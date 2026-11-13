#!/usr/bin/env python3
"""사례 사진 깔끔하게 보정(11/13 15:06 사장님 「최신본 · 잘 나온 시공 사진 · 방향 · 색감 조정 · 지저분한 것 없애고 깔끔하게」).
python3 enhance.py <사례폴더>... | --all
- 방향: 휴대폰 회전 정보(EXIF)대로 바로 세움.
- 색감: 회색 기준 화이트밸런스(누런 · 푸른 끼 살짝 빼기) → 밝기 · 대비 자동(양끝 1% 자름) → 채도 +6% → 아주 약한 선명.
- 지저분함: 가장자리 4% 잘라 냄(벽 끝 · 바닥 물건 · 업체 표시 줄임). 물건을 지우는 그림 합성은 하지 않음(실제 시공 사진이 바뀌면 안 됨).
- 원본은 _원본/ (처음 한 번), 결과는 「보정본/」. 이미 보정본이 있는 사례(눈으로 고른 것)는 그 안 사진을 같은 방법으로 다듬음. 「보정: … 색 · 방향 다듬음」 표시.
"""
import os, sys, glob, re, shutil
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
def tidy_img(src, dst):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    a = np.asarray(im).astype(np.float32)
    m = a.reshape(-1, 3).mean(0); g = m.mean()
    gain = np.clip(g / np.maximum(m, 1), 0.94, 1.06)          # 화이트밸런스는 아주 약하게(따뜻한 대리석 · 나무색 살림)
    a = np.clip(a * (0.75 + 0.25 * gain), 0, 255).astype(np.uint8)
    im = Image.fromarray(a)
    im = ImageOps.autocontrast(im, cutoff=0.5, preserve_tone=True)   # 밝기만 · 색 틀어지지 않게
    im = ImageEnhance.Color(im).enhance(1.05)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=40, threshold=3))
    w, h = im.size; c = int(min(w, h) * 0.04)
    im = im.crop((c, c, w - c, h - c))
    if max(im.size) > 1600: im.thumbnail((1600, 1600))
    im.save(dst, quality=92)
def run(d):
    d = d.rstrip('/'); t = open(f'{d}/사례.txt', encoding='utf8').read()
    if '색 · 방향 다듬음' in t: return 0
    has = os.path.isdir(f'{d}/보정본')
    srcs = sorted(glob.glob(f'{d}/보정본/[0-9][0-9].jpg')) if has else sorted(glob.glob(f'{d}/[0-9][0-9].jpg'))
    os.makedirs(f'{d}/보정본', exist_ok=True); os.makedirs(f'{d}/_원본', exist_ok=True)
    for s in srcs:
        b = os.path.basename(s); keep = f'{d}/_원본/보정전_{b}' if has else f'{d}/_원본/{b}'
        if not os.path.exists(keep): shutil.copy(s, keep)
        tidy_img(keep, f'{d}/보정본/{b}')
    # 보정본 sheet
    from PIL import ImageDraw
    fs = sorted(glob.glob(f'{d}/보정본/[0-9][0-9].jpg')); c = 6; S = 220; r = max(1, (len(fs) + c - 1) // c)
    sh = Image.new('RGB', (c * S, r * S), 'white'); dr = ImageDraw.Draw(sh)
    for n, f in enumerate(fs):
        im = Image.open(f); im.thumbnail((S - 6, S - 20)); sh.paste(im, ((n % c) * S, (n // c) * S + 16)); dr.text(((n % c) * S + 3, (n // c) * S + 2), os.path.basename(f), fill='red')
    sh.save(f'{d}/보정본/sheet.jpg', quality=85)
    if '\n보정: ' in t: t = re.sub(r'(\n보정: [^\n]*)', r'\1 · 색 · 방향 다듬음(11/13)', t, count=1)
    else: t = t.replace('\n전후 짝:', f'\n보정: 11/13 색 · 방향 다듬음(화이트밸런스 · 밝기 · 가장자리 4% 정리) → 「보정본/」 {len(fs)}장을 쓴다(사례 폴더 바로 아래 01~ 은 다듬기 전)\n전후 짝:', 1)
    open(f'{d}/사례.txt', 'w', encoding='utf8').write(t); return len(fs)
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from bank import OUT, ok_case
    ds = [d.rstrip('/') for d in glob.glob(f'{OUT}/*/*/') if ok_case(d.rstrip('/'))] if sys.argv[1:] == ['--all'] else sys.argv[1:]
    n = sum(run(d) for d in ds); print({'cases': len(ds), 'photos': n})

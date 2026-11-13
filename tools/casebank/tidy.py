#!/usr/bin/env python3
"""사례 은행 사진 보정 — 인테리어가 보이는 분야(중문 설치 · 욕실 리모델링 등)만 (11/13 사장님 「기울어진 사진 빼고 지저분한 거 빼고 · 인테리어적 요소가 필요한 항목, 중문이라던가」).
python3 tidy.py <사례폴더>...            → 세로선 기울기 재서 0.7~6° 는 바로 세우고 잘라 냄, 6° 넘으면 제외/ 로
python3 tidy.py --drop <사례폴더> 03 07 → 지저분한 사진(눈으로 보고 고른 것) 제외/ 로
원본은 _원본/ 에 남김. 끝나면 남은 사진을 01부터 다시 번호 · sheet.jpg 다시 · 사례.txt 「보정」 줄.
"""
import cv2, numpy as np, os, sys, glob, shutil, math, re
from PIL import Image, ImageDraw
def tilt(path):
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE); h, w = im.shape
    e = cv2.Canny(cv2.GaussianBlur(im, (5, 5), 0), 60, 160)
    L = cv2.HoughLinesP(e, 1, np.pi / 720, 80, minLineLength=int(h * 0.18), maxLineGap=8)
    if L is None: return None
    a = []
    for x1, y1, x2, y2 in L.reshape(-1, 4):
        ang = math.degrees(math.atan2(x2 - x1, y2 - y1))
        if ang > 90: ang -= 180
        if ang < -90: ang += 180
        if abs(ang) < 12: a += [ang] * int(math.hypot(x2 - x1, y2 - y1) // 20 + 1)   # 긴 선에 무게
    return float(np.median(a)) if len(a) >= 6 else None
def straighten(path, deg):
    im = Image.open(path).convert('RGB'); w, h = im.size
    r = im.rotate(-deg, resample=Image.BICUBIC, expand=False)
    t = math.radians(abs(deg)); cw = int(w * math.cos(t) - h * math.sin(t)); ch = int(h * math.cos(t) - w * math.sin(t))
    cw, ch = max(cw, int(w * 0.8)), max(ch, int(h * 0.8))
    r.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2)).save(path, quality=93)
def renumber(d, note):
    fs = sorted(glob.glob(f'{d}/[0-9][0-9].jpg'))
    for i, f in enumerate(fs, 1): os.rename(f, f'{d}/_tmp{i:02d}.jpg')
    fs = sorted(glob.glob(f'{d}/_tmp*.jpg'))
    for f in fs: os.rename(f, f'{d}/{os.path.basename(f)[4:]}')
    fs = sorted(glob.glob(f'{d}/[0-9][0-9].jpg'))
    c = 6; S = 220; rows = max(1, (len(fs) + c - 1) // c); sh = Image.new('RGB', (c * S, rows * S), 'white'); dr = ImageDraw.Draw(sh)
    for n, f in enumerate(fs):
        im = Image.open(f).convert('RGB'); im.thumbnail((S - 6, S - 20)); sh.paste(im, ((n % c) * S, (n // c) * S + 16)); dr.text(((n % c) * S + 3, (n // c) * S + 2), os.path.basename(f), fill='red')
    sh.save(f'{d}/sheet.jpg', quality=85)
    p = f'{d}/사례.txt'; t = open(p, encoding='utf8').read()
    t = re.sub(r'^사진: \d+장', f'사진: {len(fs)}장', t, count=1, flags=re.M)
    t = re.sub(r'\n보정: .*', '', t); t = t.replace('\n전후 짝:', f'\n보정: {note}\n전후 짝:', 1)
    open(p, 'w', encoding='utf8').write(t); return len(fs)
def run(d):
    os.makedirs(f'{d}/_원본', exist_ok=True); os.makedirs(f'{d}/제외', exist_ok=True); fixed = []; out = []
    for f in sorted(glob.glob(f'{d}/[0-9][0-9].jpg')):
        b = os.path.basename(f)
        if not os.path.exists(f'{d}/_원본/{b}'): shutil.copy(f, f'{d}/_원본/{b}')
        a = tilt(f)
        if a is None or abs(a) < 0.7: continue
        if abs(a) <= 6: straighten(f, a); fixed.append(f'{b} {a:+.1f}°')
        else: shutil.move(f, f'{d}/제외/기울어짐_{b}'); out.append(b)
    n = renumber(d, f"기울기 바로 세움 {len(fixed)}장 · 기울어 뺌 {len(out)}장 (원본 _원본/)")
    return {'case': os.path.basename(d)[:30], 'fixed': fixed, 'out': out, 'left': n}
if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--drop':
        d = a[1]; os.makedirs(f'{d}/제외', exist_ok=True)
        for k in a[2:]:
            f = f'{d}/{int(k):02d}.jpg'
            if os.path.exists(f): shutil.move(f, f'{d}/제외/지저분_{os.path.basename(d)[:12]}_{int(k):02d}.jpg')
        t = open(f'{d}/사례.txt', encoding='utf8').read(); m = re.search(r'보정: (.*)', t)
        print(renumber(d, (m.group(1) if m else '') + f' · 지저분해 뺌 {len(a) - 2}장'))
    else:
        import json
        for d in a: print(json.dumps(run(d.rstrip('/')), ensure_ascii=False))

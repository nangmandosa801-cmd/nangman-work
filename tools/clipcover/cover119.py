#!/usr/bin/env python3
"""낭만 인테리어 클립 · 릴스 커버 (11/9 원칙) — 실제 현장 사진 배경 + 위: 상황 한 줄(흰) → 질문형 훅(노랑 · 크게) → 키워드 3개 · 아래: 「○○ 실제 사례」 노란 배지 + 낭만 인테리어.
python3 cover119.py --photo p.jpg --situ "아랫집 천장에 물이 샌다면" --hook "수리비, 누가 낼까?" --kw "윗집,보험,관리사무소" --badge "등촌대림 실제 사례" --out c.jpg"""
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
K = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; B = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
W, H = 1080, 1920; YEL = (255, 214, 0); WHITE = (255, 255, 255)
def F(p, s): return ImageFont.truetype(p, s)
def wrap(d, t, ft, maxw):
    lines, cur = [], ''
    for ch in t:
        if d.textlength(cur + ch, font=ft) > maxw and cur:
            sp = cur.rfind(' ')
            if sp > 0: lines.append(cur[:sp]); cur = cur[sp + 1:] + ch
            else: lines.append(cur); cur = ch
        else: cur += ch
    if cur: lines.append(cur)
    return lines
def make(photo, situ, hook, kw, badge, out, crop_bottom=0.12):
    im = Image.open(photo).convert('RGB')
    if crop_bottom: im = im.crop((0, 0, im.width, int(im.height * (1 - crop_bottom))))
    bg = ImageOps.fit(im, (W, H), centering=(0.5, 0.5))
    shade = Image.new('L', (1, H))
    for y in range(H):
        a = 200 if y < 820 else (90 if y < 1500 else 170)
        if 700 <= y < 900: a = int(200 - (y - 700) / 200 * 110)
        if 1400 <= y < 1500: a = int(90 + (y - 1400) / 100 * 80)
        shade.putpixel((0, y), a)
    bg = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), bg, shade.resize((W, H)))
    d = ImageDraw.Draw(bg); x = 70; y = 150
    for ln in wrap(d, situ, F(B, 58), W - 140)[:2]:
        d.text((x, y), ln, font=F(B, 58), fill=WHITE); y += 80
    y += 30; size = 132
    while size > 90:
        ls = wrap(d, hook, F(K, size), W - 140)
        if len(ls) <= 3: break
        size -= 8
    for ln in ls[:3]:
        d.text((x, y), ln, font=F(K, size), fill=YEL, stroke_width=3, stroke_fill=(0, 0, 0)); y += int(size * 1.22)
    y += 30; cx = x
    for k in [k.strip() for k in kw.split(',') if k.strip()][:3]:
        ft = F(B, 46); w = d.textlength(k, font=ft) + 50
        if cx + w > W - 60: break
        d.rounded_rectangle((cx, y, cx + w, y + 78), 39, outline=WHITE, width=4); d.text((cx + 25, y + 10), k, font=ft, fill=WHITE); cx += w + 20
    ft = F(K, 56); bw = d.textlength(badge, font=ft) + 70
    d.rounded_rectangle((x, 1560, x + bw, 1660), 24, fill=YEL); d.text((x + 35, 1572), badge, font=ft, fill=(20, 20, 20))
    d.text((x, 1700), '낭만 인테리어', font=F(K, 64), fill=WHITE)
    bg.save(out, quality=92)
if __name__ == '__main__':
    a = argparse.ArgumentParser()
    for k in ['photo', 'situ', 'hook', 'kw', 'badge', 'out']: a.add_argument('--' + k, required=True)
    a.add_argument('--crop', type=float, default=0.12); v = a.parse_args()
    make(v.photo, v.situ, v.hook, v.kw, v.badge, v.out, v.crop)

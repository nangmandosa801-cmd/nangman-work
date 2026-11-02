# 스레드 카드 묶음(캐러셀) 생성기 · 10/29 사용자 「이렇게 만들어 스레드 · 앞으로 링크는 답글에」
# 크림 바탕 · 남색 윗선 · 「낭만 인테리어 | 오늘의 집 상식」 머리 · 큰 제목 · 상자 3개 · 아래 꼬리말
# 사용: from thread_cards import make; make(out_dir, slug, cards) → png 경로 목록
#   cards = [{'kind':'cover','kicker':..,'title':[..],'sub':..},
#            {'kind':'point','label':'첫 번째','title':..,'sub':..,'boxes':[(제목, 설명), ...]},
#            {'kind':'end','title':..,'rows':[..],'line':..}]
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1080, 1350
BG = (247, 245, 240); CARD = (255, 255, 255); BOX = (241, 238, 231)
NAVY = (27, 45, 79); INK = (28, 33, 44); MUTE = (110, 116, 128); GOLD = (185, 138, 46); LINE = (226, 222, 214)
B = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; BD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
R = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
def F(s, w='b'): return ImageFont.truetype({'k': B, 'b': BD, 'r': R}[w], s, index=1)
HEAD = '낭만 인테리어  |  오늘의 집 상식'

def frame(foot):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    d.rounded_rectangle((40, 40, W - 40, H - 40), 44, fill=CARD, outline=LINE, width=2)
    d.rounded_rectangle((40, 40, W - 40, 60), 10, fill=NAVY); d.rectangle((40, 50, W - 40, 60), fill=NAVY)
    d.text((100, 110), HEAD, font=F(32), fill=INK)
    d.line((100, 175, W - 100, 175), fill=LINE, width=2)
    d.line((100, H - 150, W - 100, H - 150), fill=LINE, width=2)
    d.text((100, H - 118), foot, font=F(28, 'r'), fill=MUTE)
    t = '낭만 인테리어'; d.text((W - 100 - d.textlength(t, font=F(30)), H - 120), t, font=F(30), fill=INK)
    return im, d

def wrap(d, text, font, maxw):
    out, cur = [], ''
    for ch in text:
        if d.textlength(cur + ch, font=font) > maxw and cur:
            sp = cur.rfind(' ')
            if sp > 0: out.append(cur[:sp]); cur = cur[sp + 1:] + ch
            else: out.append(cur); cur = ch
        else: cur += ch
    if cur: out.append(cur)
    return out

def cover(c, foot):
    im, d = frame(foot); y = 330
    d.text((100, y), c['kicker'], font=F(44), fill=GOLD); y += 90
    for t in c['title']:
        d.text((100, y), t, font=F(96, 'k'), fill=NAVY); y += 125
    y += 30
    for t in wrap(d, c['sub'], F(44, 'r'), W - 200):
        d.text((100, y), t, font=F(44, 'r'), fill=INK); y += 64
    if c.get('tag'):
        y += 40; f = F(34); w = d.textlength(c['tag'], font=f)
        d.rounded_rectangle((100, y, 100 + w + 56, y + 70), 35, fill=NAVY); d.text((128, y + 12), c['tag'], font=f, fill=CARD)
    return im

def point(c, foot):
    im, d = frame(foot); y = 225
    d.text((100, y), c['label'], font=F(32, 'r'), fill=MUTE); y += 58
    for t in wrap(d, c['title'], F(70, 'k'), W - 200):
        d.text((100, y), t, font=F(70, 'k'), fill=NAVY); y += 92
    if c.get('sub'):
        d.text((100, y + 6), c['sub'], font=F(34, 'r'), fill=MUTE); y += 70
    y += 30
    n = len(c['boxes']); bh = min(230, (H - 200 - y - 20 * (n - 1)) // n)
    for bt, bdsc in c['boxes']:
        d.rounded_rectangle((100, y, W - 100, y + bh), 24, fill=BOX)
        d.text((136, y + 30), bt, font=F(44), fill=INK)
        yy = y + 98
        for t in wrap(d, bdsc, F(34, 'r'), W - 272)[:2]:
            d.text((136, yy), t, font=F(34, 'r'), fill=MUTE); yy += 48
        y += bh + 20
    return im

def end(c, foot, contact):
    im, d = frame(foot); y = 225
    d.text((100, y), '오늘의 한 줄 정리', font=F(32, 'r'), fill=MUTE); y += 58
    for t in wrap(d, c['title'], F(66, 'k'), W - 200):
        d.text((100, y), t, font=F(66, 'k'), fill=NAVY); y += 88
    y += 30
    for r in c['rows']:
        d.rounded_rectangle((100, y, W - 100, y + 92), 20, fill=BOX); d.text((136, y + 22), r, font=F(40), fill=INK); y += 110
    y += 20
    bh = H - 190 - y
    d.rounded_rectangle((100, y, W - 100, y + bh), 26, fill=NAVY)
    yy = y + 34
    for i, t in enumerate(contact):
        f = F(46, 'k') if i == 0 else (F(56, 'k') if t.startswith('문의') else F(34, 'r'))
        col = (232, 200, 120) if t.startswith('문의') else CARD
        d.text((136, yy), t, font=f, fill=col); yy += int(f.size * 1.5)
    return im

CONTACT = ['낭만 인테리어  |  전국 지원', '받은 견적서 한 장, 같은 공사인지 무료로 봐 드립니다', '문의 010-2882-8165', '사진 · 지역 · 평수를 문자로 보내 주세요']

def make(out_dir, slug, cards, foot='견적은 같은 공사끼리 비교하세요', contact=CONTACT):
    os.makedirs(out_dir, exist_ok=True); paths = []
    for i, c in enumerate(cards):
        im = cover(c, foot) if c['kind'] == 'cover' else point(c, foot) if c['kind'] == 'point' else end(c, foot, contact)
        p = f'{out_dir}/{slug}_th{i+1:02d}.jpg'; im.save(p, quality=92); paths.append(p)
    return paths

# 낭만 부동산 숫자 클립 · 큰 글자판 (11/10 사용자 「잘 보이게 폰트 작아지지 않게」)
# clipgen2(캐릭터 없음) 위에 덮어씀: 어떤 글자도 64px(휴대폰에서 약 21px) 아래로 줄지 않는다.
# 길면 줄이지 않고 두 줄로 나눈다. 회색 작은 글씨 없음 · 바닥 이름표도 크게.
import sys; sys.path.insert(0, '/home/claude')
import clipgen as G
import clipgen2  # noqa: 캐릭터 끄기 등
from clipgen import *

MIN = 64
SUBC = NAVY          # 보조 글자도 진한 남색(옛 SAND 회색은 폰에서 안 보임)

def lines_of(d, t, size, maxw):
    """size 를 지키며 maxw 안에 들도록 어절 단위로 줄바꿈(최대 2줄). 그래도 넘치면 MIN 까지만 줄임."""
    if d.textlength(t, font=F(size)) <= maxw: return [t], size
    ws = t.split(' ')
    for cut in range(len(ws) - 1, 0, -1):
        a, b = ' '.join(ws[:cut]), ' '.join(ws[cut:])
        if d.textlength(a, font=F(size)) <= maxw and d.textlength(b, font=F(size)) <= maxw: return [a, b], size
    s = size
    while s > MIN and d.textlength(t, font=F(s)) > maxw: s -= 4
    return [t], s

def say(d, y, t, size, c, x=W // 2, maxw=980):
    """가운데 정렬로 쓰고 다음 y 를 돌려준다."""
    ls, s = lines_of(d, t, size, maxw)
    for i, l in enumerate(ls): ctext(d, y + i * int(s * 1.22), l, F(s), c, x)
    return y + len(ls) * int(s * 1.22)

def head(d, lines, c=NAVY, size=104, y=200):
    for l in lines: y = say(d, y, l, size, c)
    return y

def S_hook(d, b, lines, bub, c=NAVY, **k):
    head(d, lines, c, 108)
    d.rounded_rectangle((50, 700, 1030, 1400), 56, fill=CREAM, outline=NAVY, width=10)
    y = 1050 - len(bub) * 75
    for t in bub: y = say(d, y, t, 112, NAVY, maxw=900)
    say(d, 1520, '실거래로 확인했습니다', 76, SUBC)

def S_big(d, b, lines, num, sub1='', sub2='', c=WARN, nsize=280, **k):
    y = head(d, lines, NAVY, 100)
    s = nsize
    while s > 160 and d.textlength(num, font=F(s)) > 1020: s -= 8
    ctext(d, max(y + 80, 640), num, F(s), c, W // 2)
    y = max(y + 80, 640) + int(s * 1.3) + 40
    if sub1: y = say(d, y, sub1, 80, NAVY) + 20
    if sub2: say(d, y, sub2, 72, SUBC)

def S_vs(d, b, lines, L, R, bottom='', c=NAVY, bc=WARN, **k):
    head(d, lines, c, 100)
    d.rectangle((40, 560, 1040, 1360), fill=WH, outline=(210, 205, 195), width=6); d.line((540, 560, 540, 1360), fill=(210, 205, 195), width=6)
    for (lab, val, sub), x, cc in ((L, 290, NAVY), (R, 790, WARN)):
        yy = say(d, 620, lab, 74, cc, x=x, maxw=460)
        s = 170
        while s > 110 and d.textlength(val, font=F(s)) > 470: s -= 8
        ctext(d, max(yy + 40, 820), val, F(s), cc, x)
        if sub: say(d, 1200, sub, 64, SUBC, x=x, maxw=460)
    if bottom:
        y = 1450
        for t in (bottom if isinstance(bottom, list) else [bottom]): y = say(d, y, t, 92, bc) + 10

def S_bars(d, b, lines, items, unit='', c=NAVY, **k):
    items = items[:4]                         # 4개까지(글자를 키우려고)
    y = head(d, lines, c, 100)
    n = len(items); mx = max(abs(it[1]) for it in items) or 1
    y0 = max(y + 40, 560); h = min(290, 1060 // n)
    for i, it in enumerate(items):
        lab, v = it[0], it[1]; cc = it[2] if len(it) > 2 else NAVY
        yy = y0 + i * h
        ls, s = lines_of(d, lab, 72, 960); d.text((60, yy), ls[0], font=F(s), fill=NAVY)
        bh = min(120, h - 110); w = int(560 * abs(v) / mx)
        d.rounded_rectangle((60, yy + 96, 60 + max(w, 16), yy + 96 + bh), 20, fill=cc)
        txt = it[3] if len(it) > 3 else f'{v}{unit}'
        s = 84
        while s > MIN and 90 + max(w, 16) + d.textlength(txt, font=F(s)) > 1040: s -= 4
        d.text((84 + max(w, 16), yy + 96 + bh // 2 - int(s * 0.62)), txt, font=F(s), fill=cc)
    if k.get('note'): say(d, y0 + n * h + 50, k['note'], 80, WARN)

def S_end(d, b, lines, sub, sub2='자세한 숫자는'):
    head(d, lines, WH, 100, y=260)
    y = 600
    for t in sub: y = say(d, y, t, 120, Y) + 10
    y = max(y + 80, 1180)
    y = say(d, y, sub2, 76, PALE); y = say(d, y, '블로그에 정리했습니다', 76, PALE)
    say(d, y + 70, '낭만 부동산 분석 플랫폼', 84, Y)

def foot(d, b, c=SAND):
    ctext(d, 1800, BRAND[b][0], F(56), c)

G.foot = foot
G.TYPES.update(hook=S_hook, big=S_big, vs=S_vs, bars=S_bars, end=S_end)

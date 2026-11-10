#!/usr/bin/env python3
"""평평한 2D 그림 도구 (11/10 사용자 기준: 3D · 겹침 · 장식 금지 · 3초 안에 읽히게)
규칙
  · 그림 맨 위에 결론 한 줄을 크게 굵게.  · 막대는 최대 5개, 막대 위에 숫자를 바로.  · 강조는 1개만 파랑 #3182F6, 나머지 회색 #D1D6DB.
  · 격자 · 그림자 · 그라데이션 · 입체 없음.  · 폭 1200px.  · 항목이 5개(카드는 3개)를 넘으면 ValueError — 그럴 때는 표로.
함수
  bars(head, names, values, hi, path, fmt=None, subs=None, note=None)   세로 막대 ≤5 (값 ≥ 0)
  cards3(head, cards, path, hi=0, note=None)                            숫자 카드 ≤3  cards=[(이름, 큰 숫자, 작은 설명)]
  steps(head, steps, path, hi=None, pending=None, note=None)            단계 ≤5  steps=[(이름, 설명)]  pending=아직 안 된 단계 번호들
  thumb(path, values=None, hi=-1)                                       대표 그림 1200×630 · 글자 없음 · 막대 도형만
  eok(v, d=1)                                                           만원 → '11.2억'
글꼴: Pretendard(fonts/ · 없으면 Noto Sans CJK KR). 색: 먹색 #191F28 · 회색 #6B7684 · 강조 #3182F6 하나.
스타일(11/10 사용자): 흰 바탕 · 그라데이션 · 그림자 · 볼록 효과 없음 · 카드는 옅은 회색 면에 모서리 살짝 둥글게 · 여백 넉넉히.
"""
from PIL import Image, ImageDraw, ImageFont

import os
_PRE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts', 'Pretendard-%s.otf')
_TTC = '/usr/share/fonts/opentype/noto/NotoSansCJK-%s.ttc'
# 색은 셋만: 먹색 글자 · 회색 보조 · 강조 파랑 하나. (NAVY 는 예전 이름 — 강조색을 가리킨다)
ACC, GRAY, INK, SUB, LINE, BG = '#3182F6', '#D1D6DB', '#191F28', '#6B7684', '#E5E8EB', '#FFFFFF'
NAVY = ACC
CARD = '#F4F6F8'
W, S = 1200, 2          # 폭 · 내부 확대 배율(끝에 줄여서 가장자리를 매끈하게)
MAXBAR, MAXCARD, MAXSTEP = 5, 3, 5
_fc = {}


def _f(size, bold=True):
    k = (int(size), bold)
    if k not in _fc:
        w = {True: 'Bold', False: 'Medium', 'x': 'ExtraBold'}[bold]
        try: _fc[k] = ImageFont.truetype(_PRE % w, int(size) * S)
        except OSError: _fc[k] = ImageFont.truetype(_TTC % ('Bold' if bold else 'Medium'), int(size) * S, index=1)   # index 1 = KR
    return _fc[k]


def eok(v, d=1):
    if v is None or v != v: return '-'
    return f'{v / 10000:.{d}f}억'


def _tw(dr, t, f): return dr.textlength(t, font=f) / S


def _wrap(dr, t, f, maxw):
    """낱말(띄어쓰기) 먼저, 안 되면 글자 단위로 줄을 나눈다."""
    out = []
    for para in str(t).split('\n'):
        cur = ''
        for word in para.split(' '):
            cand = (cur + ' ' + word).strip()
            if _tw(dr, cand, f) <= maxw: cur = cand; continue
            if cur: out.append(cur); cur = ''
            while _tw(dr, word, f) > maxw:
                n = len(word)
                while n > 1 and _tw(dr, word[:n], f) > maxw: n -= 1
                out.append(word[:n]); word = word[n:]
            cur = word
        out.append(cur)
    return out


def _fit(dr, t, maxw, sizes, bold=True, maxlines=1):
    """큰 글자부터 시도해서 maxlines 줄 안에 들어가는 첫 크기. 돌려줌: (font, lines, size)"""
    for sz in sizes:
        f = _f(sz, bold); ls = _wrap(dr, t, f, maxw)
        if len(ls) <= maxlines: return f, ls, sz
    f = _f(sizes[-1], bold); ls = _wrap(dr, t, f, maxw)[:maxlines]
    ls[-1] = ls[-1][:-1] + '…'
    return f, ls, sizes[-1]


def _text(dr, x, y, t, f, fill, anchor='mt'):
    dr.text((x * S, y * S), t, font=f, fill=fill, anchor=anchor)


def _lines(dr, x, y, ls, f, sz, fill, gap=1.28, anchor='mt'):
    for i, l in enumerate(ls): _text(dr, x, y + i * sz * gap, l, f, fill, anchor)
    return y + len(ls) * sz * gap


def _canvas(h):
    im = Image.new('RGB', (W * S, int(h) * S), BG)
    return im, ImageDraw.Draw(im)


def _head(dr, head):
    """결론 한 줄(길면 두 줄까지). 돌려줌: 아래 끝 y"""
    f, ls, sz = _fit(dr, head, W - 120, [56, 52, 48, 44], 'x', 1)
    if ls[0].endswith('…') and not head.endswith('…'):
        f, ls, sz = _fit(dr, head, W - 120, [48, 44, 40, 36], 'x', 2)
    return _lines(dr, W / 2, 64, ls, f, sz, INK, 1.3)


def _note(dr, note, y):
    if note: _text(dr, W / 2, y, note, _f(20, False), SUB, 'mt')


def _save(im, path):
    im = im.resize((W, im.height // S), Image.LANCZOS)
    im.save(path, quality=93) if path.lower().endswith(('.jpg', '.jpeg')) else im.save(path)
    return path


def _hi(hi, names):
    if hi is None: return None
    if isinstance(hi, (list, tuple)): raise ValueError('강조는 1개만')
    return names.index(hi) if isinstance(hi, str) else int(hi) % len(names)


# ------------------------------------------------------------------ 막대
def _bar(dr, x0, y0, x1, y1, fill, r=10):
    """평평한 단색 막대 · 윗모서리만 살짝 둥글게"""
    r = min(r, (y1 - y0) / 2)
    dr.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S], radius=r * S, fill=fill, corners=(True, True, False, False))


def bars(head, names, values, hi, path, fmt=None, subs=None, note=None):
    n = len(names)
    if n > MAXBAR: raise ValueError(f'막대는 {MAXBAR}개까지입니다({n}개). 표나 숫자 카드로 바꾸세요.')
    if n < 1 or n != len(values): raise ValueError('names 와 values 개수가 다릅니다')
    vals = [None if (v is None or v != v) else float(v) for v in values]
    if any(v is not None and v < 0 for v in vals): raise ValueError('bars 는 0 이상만. 음수는 cards3 로.')
    fmt = fmt or (lambda v: f'{v:,.0f}')
    hi = _hi(hi, names)
    im, dr = _canvas(10); top = _head(dr, head)                       # 머리 높이를 먼저 잰다
    slot = min(250, (W - 120) / n); bw = slot * 0.62; x0 = (W - slot * n) / 2
    nsz = next((z for z in (25, 23, 21) if all(len(_wrap(dr, nm, _f(z, False), slot - 16)) <= 2 for nm in names)), 21)
    fn = _f(nsz, False); name_ls = [_wrap(dr, nm, fn, slot - 16)[:3] for nm in names]
    fs = _f(20, False); sub_ls = [_wrap(dr, s, fs, slot - 10)[:2] if s else [] for s in (subs or [''] * n)]
    lab_h = max(len(l) for l in name_ls) * nsz * 1.25 + (max(len(l) for l in sub_ls) * 20 * 1.3 + 6 if subs else 0)
    y_top = top + 120; base = y_top + 320; H = base + 22 + lab_h + (84 if note else 44)
    im, dr = _canvas(H); _head(dr, head)
    vmax = max([v for v in vals if v is not None] or [1]) or 1
    fv, _, vsz = _fit(dr, max((fmt(v) for v in vals if v is not None), key=len, default='-'), slot - 8, [50, 46, 42, 38, 34, 30], 'x', 1)
    for i, v in enumerate(vals):
        cx = x0 + slot * (i + 0.5); on = (i == hi)
        if v is None:
            _text(dr, cx, base - 14, '거래 없음', _f(24, False), SUB, 'mb')
        else:
            h = max(8, 320 * v / vmax)
            _bar(dr, cx - bw / 2, base - h, cx + bw / 2, base, ACC if on else GRAY)
            _text(dr, cx, base - h - 14, fmt(v), fv, ACC if on else INK, 'mb')
        _lines(dr, cx, base + 18, name_ls[i], fn, nsz, INK, 1.25)
        y = base + 18 + max(len(l) for l in name_ls) * nsz * 1.25      # 작은 설명은 모두 같은 높이에
        if sub_ls[i]: _lines(dr, cx, y + 6, sub_ls[i], fs, 20, SUB, 1.3)
    dr.line([(x0 - 10) * S, base * S, (x0 + slot * n + 10) * S, base * S], fill=GRAY, width=2 * S)
    _note(dr, note, H - 56)
    return _save(im, path)


# ------------------------------------------------------------------ 숫자 카드
def cards3(head, cards, path, hi=0, note=None):
    n = len(cards)
    if n > MAXCARD: raise ValueError(f'숫자 카드는 {MAXCARD}개까지입니다({n}개).')
    if n < 1: raise ValueError('카드가 없습니다')
    im, dr = _canvas(10); top = _head(dr, head)
    gap = 24; cw = (W - 120 - gap * 2) / 3; ch = 300
    x0 = (W - (cw * n + gap * (n - 1))) / 2; y0 = top + 56; H = y0 + ch + (96 if note else 60)
    im, dr = _canvas(H); _head(dr, head)
    for i, c in enumerate(cards):
        name, big, desc = (list(c) + ['', ''])[:3]
        on = (hi is not None and i == hi); x = x0 + i * (cw + gap); cx = x + cw / 2
        dr.rounded_rectangle([x * S, y0 * S, (x + cw) * S, (y0 + ch) * S], radius=20 * S, fill=CARD)
        f1, l1, s1 = _fit(dr, name, cw - 44, [24, 22, 20], False, 2)                    # 라벨: 숫자 위에 작게 회색
        _lines(dr, cx, y0 + 40 + (0 if len(l1) > 1 else 14), l1, f1, s1, SUB, 1.28)
        f2, l2, s2 = _fit(dr, str(big), cw - 44, [88, 80, 72, 64, 56, 48, 42], 'x', 1)  # 숫자: 아주 크고 굵게
        _text(dr, cx, y0 + 162, l2[0], f2, ACC if on else INK, 'mm')
        if desc:
            f3, l3, s3 = _fit(dr, desc, cw - 40, [22, 20, 18], False, 2)                # 설명: 아래 작게 회색
            _lines(dr, cx, y0 + 226 + (0 if len(l3) > 1 else 12), l3, f3, s3, SUB, 1.3)
    _note(dr, note, H - 64)
    return _save(im, path)


# ------------------------------------------------------------------ 단계
def steps(head, steps, path, hi=None, pending=None, note=None):
    n = len(steps)
    if n > MAXSTEP: raise ValueError(f'단계는 {MAXSTEP}개까지입니다({n}개).')
    if n < 2: raise ValueError('단계는 2개 이상')
    pending = set(pending or []); hi = None if hi is None else int(hi) % n
    im, dr = _canvas(10); top = _head(dr, head)
    aw = 40; bw = (W - 100 - aw * (n - 1)) / n; bh = 250; x0 = 50; y0 = top + 56; H = y0 + bh + (96 if note else 60)
    im, dr = _canvas(H); _head(dr, head)
    for i, s in enumerate(steps):
        name, desc = (list(s) + [''])[:2]
        x = x0 + i * (bw + aw); cx = x + bw / 2; on = (i == hi); pend = i in pending
        box = [x * S, y0 * S, (x + bw) * S, (y0 + bh) * S]
        if pend: dr.rounded_rectangle(box, radius=18 * S, fill=BG, outline=LINE, width=2 * S)   # 아직 안 된 단계: 빈 상자
        else: dr.rounded_rectangle(box, radius=18 * S, fill=CARD)
        c1 = ACC if on else (SUB if pend else INK)
        _text(dr, cx, y0 + 26, str(i + 1), _f(22, True), ACC if on else SUB, 'mt')
        f1, l1, s1 = _fit(dr, name, bw - 24, [32, 29, 26, 23], 'x', 2)
        _lines(dr, cx, y0 + 74 + (0 if len(l1) > 1 else 18), l1, f1, s1, c1, 1.22)
        if desc:
            f2, l2, s2 = _fit(dr, desc, bw - 22, [21, 19, 18], False, 3)
            _lines(dr, cx, y0 + 162, l2, f2, s2, SUB, 1.34)
        if i < n - 1:                                                   # 평평한 화살표
            ax = x + bw + 8; ay = y0 + bh / 2
            dr.line([ax * S, ay * S, (ax + 16) * S, ay * S], fill=GRAY, width=4 * S)
            dr.polygon([((ax + 13) * S, (ay - 10) * S), ((ax + 26) * S, ay * S), ((ax + 13) * S, (ay + 10) * S)], fill=GRAY)
    _note(dr, note, H - 64)
    return _save(im, path)


# ------------------------------------------------------------------ 대표 그림
def thumb(path, values=None, hi=-1):
    """1200×630 · 글자 없음 · 평평한 막대 5개(값이 많으면 5구간 평균). 강조 1개만 남색."""
    v = [float(x) for x in (values if values is not None else [3, 4, 5, 6.5, 8]) if x == x] or [3, 4, 5, 6.5, 8]
    if len(v) > 5:
        k = len(v) / 5.0; v = [sum(v[int(i * k):max(int((i + 1) * k), int(i * k) + 1)]) / len(v[int(i * k):max(int((i + 1) * k), int(i * k) + 1)]) for i in range(5)]
    lo, hi_v = min(v), max(v); n = len(v); hi = hi % n
    hs = [0.35 + 0.65 * ((x - lo) / (hi_v - lo) if hi_v > lo else 0.5) for x in v]     # 모양만 보이게 0.35~1 로
    Ht = 630; im = Image.new('RGB', (W * S, Ht * S), BG); dr = ImageDraw.Draw(im)
    slot = 170; bw = 108; x0 = (W - slot * n) / 2; base = 515
    for i, h in enumerate(hs):
        cx = x0 + slot * (i + 0.5)
        _bar(dr, cx - bw / 2, base - 400 * h, cx + bw / 2, base, ACC if i == hi else GRAY, 14)
    im = im.resize((W, Ht), Image.LANCZOS)
    im.save(path, quality=93) if path.lower().endswith(('.jpg', '.jpeg')) else im.save(path)
    return path


if __name__ == '__main__':
    import os
    d = '/tmp/viz2d_test'; os.makedirs(d, exist_ok=True)
    bars('84㎡ 1년 새 2억 3천 올랐습니다', ['2021년 하반기', '1년 전', '6개월 전', '지금'], [98000, 89000, 101000, 112000], 3, f'{d}/bars.png',
         fmt=lambda v: eok(v), subs=['21.7~12월', '24.12~25.5월', '25.6~11월', '25.12~26.5월'], note='국토교통부 실거래 · 84㎡ 가운데 값')
    cards3('미사 84㎡ 가운데 값은 11억 2,000만입니다', [('84㎡ 매매 · 최근 6개월', '11.2억', '312건'), ('2021년 하반기 대비', '+8.4%', '10.3억 → 11.2억'), ('전세가율', '56%', '새 전세 6.3억 · 120건')], f'{d}/cards.png')
    steps('환지처분이 끝나야 땅 등기가 나옵니다', [('구역 지정', '개발할 땅의 범위를 정함'), ('환지 계획', '누가 어느 땅을 받을지 정함'), ('공사 · 준공', '도로 · 공원 · 택지 준공검사'), ('환지처분', '공고 다음 날 새 땅이 내 땅'), ('등기', '시행자가 14일 안에 신청')], f'{d}/steps.png', hi=3)
    thumb(f'{d}/thumb.png', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    try: bars('x', list('abcdef'), [1] * 6, 0, f'{d}/x.png')
    except ValueError as e: print('OK', e)
    print(d)

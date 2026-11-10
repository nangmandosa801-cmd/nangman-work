#!/usr/bin/env python3
"""입체 그림 도구 (티스토리 talk7921 실거래가 페이지용 · 11/10)
함수
  ribbon_line(labels, values, path, title)            입체 리본 꺾은선 (월별 중앙값)
  iso_bars(names, values, path, title, hi=None)       가로 등축 입체 막대 · 그림자 · 그라데이션
  card_row(cards, path)                               숫자 카드 입체 · 그림자  cards=[(이름, 큰 숫자, 작은 설명)]
  bar3d_months(rows, cols, Z, path, title)            (동/단지 × 기간) 3D 막대  Z[row][col] (없으면 nan)
  thumb(values, path, seed)                           대표 이미지 1200×630 · 글자 없음
색: 남색 #1F3864 · #2E5C8A 계열 + 강조 #E8833A. 폭 1200px.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Polygon, FancyBboxPatch, Rectangle
from matplotlib.colors import to_rgb, LinearSegmentedColormap

for f in ['/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
          '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc']:
    try: fm.fontManager.addfont(f)
    except Exception: pass
_fam = [f.name for f in fm.fontManager.ttflist if 'Noto Sans CJK' in f.name or 'Nanum' in f.name]
FONT = 'Noto Sans CJK JP' if 'Noto Sans CJK JP' in _fam else (_fam[0] if _fam else 'DejaVu Sans')
plt.rcParams.update({'font.family': FONT, 'axes.unicode_minus': False})

NAVY, BLUE, LIGHT, ACC = '#1F3864', '#2E5C8A', '#8FB0D6', '#E8833A'
INK, GRID, BG = '#22324A', '#D9E1EC', '#FFFFFF'
DPI = 100

def _shade(c, k):
    """k<1 어둡게, k>1 밝게"""
    r = np.array(to_rgb(c))
    return tuple(np.clip(r * k, 0, 1)) if k <= 1 else tuple(r + (1 - r) * (k - 1))

def eok(v, d=1):
    """만원 → '11.2억' (d=2 이면 끝 0 지움: 12.40 → 12.4)"""
    t = f'{v/10000:.{d}f}'
    if '.' in t: t = t.rstrip('0').rstrip('.')
    return t + '억'

def _title(fig, title, sub=None):
    if title: fig.text(0.04, 0.955, title, fontsize=30, fontweight='bold', color=NAVY, va='top')
    if sub: fig.text(0.04, 0.955 - 52 / (fig.get_figheight() * DPI), sub, fontsize=19, color='#5A6B85', va='top')

def _grad_rect(ax, x0, y0, w, h, c1, c2, horiz=True, z=3):
    g = np.linspace(0, 1, 64)
    g = g[None, :] if horiz else g[:, None]
    cm = LinearSegmentedColormap.from_list('g', [c1, c2])
    ax.imshow(g, extent=[x0, x0 + w, y0, y0 + h], cmap=cm, aspect='auto', zorder=z, interpolation='bicubic', origin='lower')

# ---------------------------------------------------------------- 입체 리본 꺾은선
def ribbon_line(labels, values, path, title='', sub='', unit_fn=eok, depth=(0.35, None)):
    v = np.array(values, float); n = len(v); x = np.arange(n)
    fig = plt.figure(figsize=(12, 7.2), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0.07, 0.15, 0.89, 0.62]); ax.set_facecolor(BG)
    ok = ~np.isnan(v)
    lo, hi = np.nanmin(v), np.nanmax(v); span = hi - lo if hi > lo else hi * 0.1
    ymin = lo - span * 0.55; ymax = hi + span * 0.45
    dx, dy = depth[0], span * 0.09
    xs, ys = x[ok], v[ok]
    # 바닥 그림자 (리본 뒤로 살짝)
    # 면 아래 그라데이션 (위 진하게 → 아래 옅게)
    for i in range(1, 25):
        ax.fill_between(xs, ys - (ys - ymin) * (i / 24), ymin, color=BLUE, alpha=0.018, lw=0, zorder=1.5)
    # 리본 윗면 (평행사변형)
    for i in range(len(xs) - 1):
        x1, x2, y1, y2 = xs[i], xs[i + 1], ys[i], ys[i + 1]
        k = 1.25 if y2 >= y1 else 0.95
        ax.add_patch(Polygon([(x1, y1), (x2, y2), (x2 + dx, y2 + dy), (x1 + dx, y1 + dy)], closed=True,
                             fc=_shade(BLUE, k + 0.25), ec='none', zorder=4))
        # 앞면 띠 (두께)
        ax.add_patch(Polygon([(x1, y1), (x2, y2), (x2, y2 - dy * 0.9), (x1, y1 - dy * 0.9)], closed=True,
                             fc=_shade(NAVY, 0.95 if y2 >= y1 else 0.8), ec='none', zorder=5))
    ax.plot(xs, ys, color=NAVY, lw=2.2, zorder=6)
    ax.plot(xs + dx, ys + dy, color='white', lw=1.4, alpha=0.9, zorder=6)
    # 점 · 강조
    imax = int(np.nanargmax(v)); imin = int(np.nanargmin(v)); il = int(xs[-1])
    for i, c in [(imax, NAVY), (imin, BLUE), (il, ACC)]:
        ax.scatter([i], [v[i]], s=190, color=c, edgecolor='white', lw=2.5, zorder=8)
    lab = {imax: ('가장 높음', NAVY), imin: ('가장 낮음', BLUE), il: ('최근', ACC)}
    for i, (t, c) in lab.items():
        up = i != imin
        yy = v[i] + (dy * 2.6 if up else -dy * 3.6)
        if i == il and imax != il and abs(imax - il) <= 5: yy = max(v[il], v[imax]) + dy * 6.2   # 겹침 피해 위로
        ha = 'right' if i > n - 3 else ('left' if i < 2 else 'center')
        if i == imax and imax != il and abs(imax - il) <= 5: ha = 'right'
        if i == imin and imin != il and abs(imin - il) <= 2: yy = v[i] - dy * 7
        ax.annotate(f'{t} {unit_fn(v[i])}', (i, v[i]), (i, yy), fontsize=20, fontweight='bold', color=c, ha=ha,
                    va='bottom' if up else 'top', zorder=9,
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=c, lw=1.5, alpha=0.95))
    ax.set_ylim(ymin, ymax + span * 0.55); ax.set_xlim(-0.6, n - 0.2)
    step = max(1, n // 8)
    ticks = [i for i in range(n) if (n - 1 - i) % step == 0]
    ax.set_xticks(ticks); ax.set_xticklabels([labels[i] for i in ticks], fontsize=17, color=INK)
    yt = ax.get_yticks(); ax.set_yticks(yt[1:-1]); ax.set_yticklabels([unit_fn(t) for t in yt[1:-1]], fontsize=17, color=INK)
    ax.grid(axis='y', color=GRID, lw=1); ax.set_axisbelow(True)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    _title(fig, title, sub)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    return path

# ---------------------------------------------------------------- 가로 등축 입체 막대
def iso_bars(names, values, path, title='', sub='', hi=None, unit_fn=eok, note=None):
    """names/values 위에서부터 순서대로. hi: 강조할 이름(들)."""
    hi = set([hi] if isinstance(hi, str) else (hi or []))
    n = len(names); v = np.array(values, float)
    rowh = 0.78
    H = 2.6 + n * rowh
    fig = plt.figure(figsize=(12, H), dpi=DPI, facecolor=BG)
    top = 1 - 1.75 / H; bot = 0.45 / H
    ax = fig.add_axes([0.31, bot, 0.66, top - bot]); ax.axis('off')
    vmax = np.nanmax(v); vmin0 = 0
    L = vmax * 1.22
    ax.set_xlim(0, L); ax.set_ylim(-0.7, n - 0.2)
    bh = 0.56; dx = L * 0.018; dy = 0.17
    for i, (nm, val) in enumerate(zip(names, v)):
        y = n - 1 - i - bh / 2
        if np.isnan(val): continue
        base = ACC if nm in hi else (NAVY if i % 2 == 0 else BLUE)
        w = val
        # 그림자
        ax.add_patch(Polygon([(dx * 1.5, y - 0.09), (w + dx * 2.8, y - 0.09), (w + dx * 2.8 + dx, y + bh * 0.25), (dx * 2.5, y + bh * 0.25)],
                             fc='black', alpha=0.07, ec='none', zorder=1))
        # 앞면 그라데이션
        _grad_rect(ax, 0, y, w, bh, _shade(base, 0.85), _shade(base, 1.35), horiz=True, z=3)
        # 윗면
        ax.add_patch(Polygon([(0, y + bh), (w, y + bh), (w + dx, y + bh + dy), (dx, y + bh + dy)], fc=_shade(base, 1.6), ec='none', zorder=4))
        # 옆면
        ax.add_patch(Polygon([(w, y), (w + dx, y + dy), (w + dx, y + bh + dy), (w, y + bh)], fc=_shade(base, 0.6), ec='none', zorder=4))
        ax.text(w + dx * 2.2, y + bh / 2, unit_fn(val), fontsize=21, fontweight='bold', color=ACC if nm in hi else INK, va='center', zorder=6)
        fig.text(0.295, bot + (top - bot) * ((y + bh / 2 + 0.7) / (n - 0.2 + 0.7)), nm, fontsize=19 if len(nm) < 13 else 16,
                 color=INK, ha='right', va='center', fontweight='bold' if nm in hi else 'normal')
    if note: fig.text(0.97, 0.15 / H * 2, note, fontsize=15, color='#6B7A90', ha='right')
    _title(fig, title, sub)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    return path

# ---------------------------------------------------------------- 숫자 카드
def card_row(cards, path, title=''):
    n = len(cards)
    H = 3.4 if not title else 4.3
    fig = plt.figure(figsize=(12, H), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 12); ax.set_ylim(0, H)
    gap = 0.28; W = (12 - 0.5 - gap * (n - 1)) / n; ch = 2.55; y0 = 0.38
    for i, c in enumerate(cards):
        lab, big, small = (list(c) + [''])[:3]
        x0 = 0.25 + i * (W + gap)
        hl = i == n - 1 and len(c) > 3 and c[3]
        base = ACC if (len(c) > 3 and c[3]) else (NAVY if i % 2 == 0 else BLUE)
        # 그림자 · 두께
        ax.add_patch(FancyBboxPatch((x0 + 0.1, y0 - 0.16), W, ch, boxstyle='round,pad=0,rounding_size=0.22', fc='black', alpha=0.10, ec='none', zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0 - 0.1), W, ch, boxstyle='round,pad=0,rounding_size=0.22', fc=_shade(base, 0.62), ec='none', zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0), W, ch, boxstyle='round,pad=0,rounding_size=0.22', fc=base, ec='none', zorder=3))
        # 위에서 비추는 빛 (세로 그라데이션)
        for j in range(12):
            ax.add_patch(Rectangle((x0 + 0.04, y0 + ch * (0.5 + j * 0.04)), W - 0.08, ch * 0.04, fc='white', alpha=0.012 * j, ec='none', zorder=4))
        ax.plot([x0 + 0.25, x0 + W - 0.25], [y0 + ch - 0.05, y0 + ch - 0.05], color='white', alpha=0.35, lw=2, zorder=5)
        cx = x0 + W / 2
        ax.text(cx, y0 + ch - 0.42, lab, fontsize=18, color='white', ha='center', va='center', alpha=0.92, zorder=5)
        fs = 38 if len(big) <= 7 else (32 if len(big) <= 9 else 26)
        ax.text(cx, y0 + ch / 2 - 0.05, big, fontsize=fs, fontweight='bold', color='white', ha='center', va='center', zorder=5)
        ax.text(cx, y0 + 0.38, small, fontsize=15, color='white', ha='center', va='center', alpha=0.85, zorder=5)
    if title: ax.text(0.3, H - 0.45, title, fontsize=28, fontweight='bold', color=NAVY, va='center')
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    return path

# ---------------------------------------------------------------- 3D 막대 (행 × 기간)
def bar3d_months(rows, cols, Z, path, title='', sub='', unit_fn=eok):
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    Z = np.array(Z, float); nr, nc = Z.shape
    fig = plt.figure(figsize=(12, 9.6), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([-0.06, -0.05, 1.12, 0.98], projection='3d'); ax.set_facecolor(BG)
    zmin = np.nanmin(Z) * 0.82; zmax = np.nanmax(Z)
    cm = LinearSegmentedColormap.from_list('n', ['#B9CDE6', '#5F88B8', BLUE])
    for r in range(nr):
        for c in range(nc):
            z = Z[r, c]
            if np.isnan(z): continue
            t = (z - zmin) / (zmax - zmin + 1e-9)
            col = ACC if (c == nc - 1 and r == int(np.nanargmax(Z[:, -1])) and not np.isnan(Z[r, -1])) else cm(0.25 + 0.75 * t)
            ax.bar3d(c, r, zmin, 0.62, 0.55, z - zmin, color=col, shade=True, edgecolor=(1, 1, 1, 0.25), lw=0.4)
    ax.set_xticks(np.arange(nc) + 0.31); ax.set_xticklabels(cols, fontsize=13, color=INK, rotation=0)
    ax.set_yticks(np.arange(nr) + 0.27); ax.set_yticklabels([s if len(s) <= 9 else s[:9] + '…' for s in rows], fontsize=14, color=INK, ha='left')
    zt = np.linspace(zmin, zmax, 4); ax.set_zticks(zt); ax.set_zticklabels([unit_fn(t) for t in zt], fontsize=13, color=INK)
    ax.set_zlim(zmin, zmax * 1.02)
    ax.view_init(elev=24, azim=-58)
    ax.set_box_aspect((nc * 0.9, nr * 1.0, max(nr, nc) * 0.55))
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.95, 0.96, 0.98, 1)); a.pane.set_edgecolor(GRID)
        a._axinfo['grid'].update(color=GRID, linewidth=0.8)
    ax.tick_params(axis='y', pad=2); ax.tick_params(axis='x', pad=0); ax.tick_params(axis='z', pad=6)
    _title(fig, title, sub)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    return path

# ---------------------------------------------------------------- 대표 이미지 (글자 없음)
def thumb(values, path, seed=0):
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    rng = np.random.default_rng(seed)
    v = np.array([x for x in values if not np.isnan(x)], float)
    if len(v) < 6: v = np.concatenate([v, rng.uniform(v.min() if len(v) else 1, v.max() if len(v) else 2, 6 - len(v))])
    v = v[-12:]; v = (v - v.min()) / (v.max() - v.min() + 1e-9) * 0.7 + 0.3
    nc = len(v); nr = 4
    fig = plt.figure(figsize=(12, 6.3), dpi=DPI)
    bg = fig.add_axes([0, 0, 1, 1]); bg.axis('off')
    bg.imshow(np.linspace(0, 1, 256)[:, None], extent=[0, 1, 0, 1], cmap=LinearSegmentedColormap.from_list('b', ['#0F1E3A', NAVY, BLUE]), aspect='auto', origin='upper')
    ax = fig.add_axes([-0.02, 0.02, 1.04, 1.1], projection='3d'); ax.set_facecolor((0, 0, 0, 0)); ax.axis('off')
    cm = LinearSegmentedColormap.from_list('n', ['#4F78A8', LIGHT, '#E6EEF8'])
    for r in range(nr):
        for c in range(nc):
            h = v[c] * (0.55 + 0.45 * (r + 1) / nr) * rng.uniform(0.85, 1.0)
            col = ACC if (c == nc - 1 and r == nr - 1) else cm(0.2 + 0.8 * (h / 1.0) * (0.6 + 0.4 * r / nr))
            ax.bar3d(c, r * 1.1, 0, 0.66, 0.7, h, color=col, shade=True, edgecolor=(1, 1, 1, 0.15), lw=0.3)
    ax.set_xlim(-1, nc + 0.5); ax.set_ylim(-0.5, nr * 1.1 + 0.5); ax.set_zlim(0, 1.0)
    ax.view_init(elev=24, azim=-60); ax.set_box_aspect((nc, nr * 1.4, 4.6), zoom=1.2)
    fig.savefig(path, dpi=DPI); plt.close(fig)
    return path

if __name__ == '__main__':
    import os; os.makedirs('/tmp/v3', exist_ok=True)
    lab = [f'{(24+i)%12+1}월' for i in range(24)]; val = 100000 + np.cumsum(np.random.default_rng(1).normal(800, 2500, 24))
    ribbon_line(lab, val, '/tmp/v3/r.png', '84㎡ 매매 중앙값 · 최근 24개월', '하남 미사 · 국토교통부 실거래')
    iso_bars(['미사강변센트럴자이', '미사역파라곤', 'B', 'C단지이름이긴단지'], [125000, 140000, 98000, 103000], '/tmp/v3/i.png', '단지별 84㎡ 중앙값', '최근 6개월', hi='미사역파라곤')
    card_row([('최근 6개월 중앙값', '11.2억', '84㎡ · 312건'), ('2021 하반기 대비', '+3.1%', '10.9억 → 11.2억'), ('새 전세 중앙값', '5.6억', '84㎡ · 120건'), ('전세가율', '50%', '전세 ÷ 매매', 1)], '/tmp/v3/c.png')
    bar3d_months(['가단지', '나단지', '다단지', '라단지', '마단지'], ['25.1Q', '25.2Q', '25.3Q', '25.4Q', '26.1Q', '26.2Q', '26.3Q', '26.4Q'],
                 np.random.default_rng(2).uniform(90000, 140000, (5, 8)), '/tmp/v3/b.png', '단지별 분기 중앙값', '84㎡')
    thumb(val, '/tmp/v3/t.png', 3)
    print('ok', FONT)

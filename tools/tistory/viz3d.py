#!/usr/bin/env python3
"""입체 그림 도구 (티스토리 talk7921 실거래가 페이지용 · 11/10)
함수
  ribbon_line(labels, values, path, title)            입체 리본 꺾은선 (월별 중앙값)
  iso_bars(names, values, path, title, hi=None)       가로 등축 입체 막대 · 그림자 · 그라데이션
  card_row(cards, path)                               숫자 카드 입체 · 그림자  cards=[(이름, 큰 숫자, 작은 설명)]
  bar3d_months(rows, cols, Z, path, title)            (동/단지 × 기간) 3D 막대  Z[row][col] (없으면 nan)
  step3d(steps, path, title, hi, pending)             입체 계단 단계 그림  steps=[(이름, 아래 설명)]
  iso_cols(labels, panels, path, title)               세로 입체 막대 · 패널 여러 줄 · 0에서 시작  panels=[(이름, 값들, 강조 번호들, {번호: 글})]
  thumb(values, path, seed)                           대표 이미지 1200×630 · 글자 없음
  twin_bars(names, A, B, path, title, sub, la, lb)    이름마다 막대 두 개(입체) · 「눈에 띄는 점」 그림 · 음수 가능
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
        ax.text(cx, y0 + ch - 0.42, lab, fontsize=18 if len(lab) <= 13 else 15, color='white', ha='center', va='center', alpha=0.92, zorder=5)
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

# ---------------------------------------------------------------- 입체 계단 단계 그림
def step3d(steps, path, title='', sub='', hi=None, pending=None, note=None):
    """steps=[(이름, 아래 설명)] 왼쪽→오른쪽 계단. hi: 강조할 번호(0부터)들, pending: 아직 안 끝난 번호들(옅게)."""
    hi = set([hi] if isinstance(hi, int) else (hi or [])); pending = set(pending or [])
    n = len(steps); H = 7.4
    fig = plt.figure(figsize=(12, H), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 12); ax.set_ylim(0, H)
    gap = 0.16; dx, dy = 0.30, 0.22
    W = (12 - 0.7 - dx - gap * (n - 1)) / n
    y0 = 1.75; h0 = 1.25 if all('\n' not in st[0] for st in steps) else 1.95; hstep = (H - 1.9 - y0 - h0 - dy) / max(n - 1, 1)
    for i, st in enumerate(steps):
        nm, cap = (list(st) + [''])[:2]
        x0 = 0.35 + i * (W + gap); h = h0 + hstep * i
        base = ACC if i in hi else (NAVY if i % 2 == 0 else BLUE)
        if i in pending and i not in hi: base = '#A9B8CC'
        ax.add_patch(Polygon([(x0 + 0.12, y0 - 0.13), (x0 + W + dx + 0.18, y0 - 0.13), (x0 + W + dx + 0.18, y0 + 0.12), (x0 + 0.12, y0 + 0.12)], fc='black', alpha=0.08, ec='none', zorder=1))
        _grad_rect(ax, x0, y0, W, h, _shade(base, 0.82), _shade(base, 1.22), horiz=False, z=3)
        ax.add_patch(Polygon([(x0, y0 + h), (x0 + W, y0 + h), (x0 + W + dx, y0 + h + dy), (x0 + dx, y0 + h + dy)], fc=_shade(base, 1.6), ec='none', zorder=4))
        ax.add_patch(Polygon([(x0 + W, y0), (x0 + W + dx, y0 + dy), (x0 + W + dx, y0 + h + dy), (x0 + W, y0 + h)], fc=_shade(base, 0.58), ec='none', zorder=4))
        cx = x0 + W / 2
        ax.text(cx, y0 + h - 0.42, str(i + 1), fontsize=30, fontweight='bold', color='white', ha='center', va='center', alpha=0.95, zorder=6)
        lines = nm.split('\n'); fs = 21 if max(len(l) for l in lines) <= 6 else (18 if max(len(l) for l in lines) <= 8 else 15)
        ax.text(cx, y0 + (h - 0.75) / 2 + 0.02, nm, fontsize=fs, fontweight='bold', color='white', ha='center', va='center', linespacing=1.25, zorder=6)
        ax.text(cx, y0 - 0.32, cap, fontsize=14.5, color=ACC if i in hi else INK, ha='center', va='top', linespacing=1.35, fontweight='bold' if i in hi else 'normal', zorder=6)
    if note: fig.text(0.97, 0.03, note, fontsize=14, color='#6B7A90', ha='right')
    _title(fig, title, sub)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    return path

# ---------------------------------------------------------------- 세로 입체 막대 (여러 줄 패널)
def iso_cols(labels, panels, path, title='', sub='', unit_fn=lambda v: f'{int(v):,}', note=None):
    """panels=[(이름, 값들, 강조 번호들(0부터), {번호: 표시 글})] 위에서 아래로. 0에서 시작하는 세로 입체 막대."""
    n = len(labels); k = len(panels); ph = 3.9
    H = 1.75 + k * ph + 0.45
    fig = plt.figure(figsize=(12, H), dpi=DPI, facecolor=BG)
    for pi, pn in enumerate(panels):
        nm, vals, his, marks = (list(pn) + [[], {}])[:4]; his = set(his or []); marks = marks or {}
        v = np.array(vals, float); vmax = np.nanmax(v)
        b0 = (0.45 + (k - 1 - pi) * ph + 0.75) / H; hh = (ph - 1.75) / H
        ax = fig.add_axes([0.05, b0, 0.92, hh]); ax.axis('off')
        ax.set_xlim(-0.4, n + 0.3); ax.set_ylim(-vmax * 0.02, vmax * 1.42)
        bw = 0.62; dx = 0.2; dy = vmax * 0.045
        ax.add_patch(Polygon([(-0.4, 0), (n + 0.1, 0), (n + 0.1 + dx, dy), (-0.4 + dx, dy)], fc='#EEF2F7', ec='none', zorder=1))
        for i, val in enumerate(v):
            base = ACC if i in his else (NAVY if pi % 2 == 0 else BLUE)
            _grad_rect(ax, i, 0, bw, val, _shade(base, 0.85), _shade(base, 1.3), horiz=False, z=3)
            ax.add_patch(Polygon([(i, val), (i + bw, val), (i + bw + dx, val + dy), (i + dx, val + dy)], fc=_shade(base, 1.6), ec='none', zorder=4))
            ax.add_patch(Polygon([(i + bw, 0), (i + bw + dx, dy), (i + bw + dx, val + dy), (i + bw, val)], fc=_shade(base, 0.58), ec='none', zorder=4))
            ax.text(i + bw / 2 + dx / 2, val + dy + vmax * 0.04, unit_fn(val), fontsize=12.5 if n > 14 else 15, color=ACC if i in his else INK,
                    fontweight='bold' if i in his else 'normal', ha='center', va='bottom', zorder=6)
            if i in marks:
                ax.text(i + bw / 2, val + dy + vmax * 0.2, marks[i], fontsize=15, color=ACC, fontweight='bold', ha='center', va='bottom', zorder=7)
            fig.text(0.05 + 0.92 * ((i + bw / 2 + 0.4) / (n + 0.7)), b0 - 0.30 / H, labels[i], fontsize=12.5 if n > 14 else 15, color=INK, ha='center', va='top')
        fig.text(0.05, b0 + hh + 0.42 / H, nm, fontsize=20, fontweight='bold', color=NAVY, va='center')
    if note: fig.text(0.97, 0.12 / H, note, fontsize=14, color='#6B7A90', ha='right')
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

# ---------------------------------------------------------------- 두 막대 짝 (눈에 띄는 점)
def _wrap(s, w=7):
    s = s.replace('미사강변', '').strip() or s
    out = [s[i:i + w] for i in range(0, len(s), w)]
    return '\n'.join(out[:3])

def twin_bars(names, A, B, path, title='', sub='', la='', lb='', fmt=None, tags=None, hi=None):
    """이름마다 A(남색) · B(주황) 막대 한 짝. 음수도 그린다. tags: 이름 아래 덧붙일 글자. hi: 강조할 이름들(바탕 띠)."""
    fmt = fmt or eok; hi = set(hi or [])
    A = np.array(A, float); B = np.array(B, float); n = len(names)
    fig = plt.figure(figsize=(12, 8.2), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0.05, 0.25, 0.92, 0.50]); ax.axis('off')
    allv = np.concatenate([A, B]); vmax = max(np.nanmax(allv), 0); vmin = min(np.nanmin(allv), 0)
    span = (vmax - vmin) or 1.0
    ax.set_xlim(-0.6, n - 0.4); ax.set_ylim(vmin - span * 0.16, vmax + span * 0.20)
    bw = 0.27; dx = 0.06; dy = span * 0.03
    for i, nm in enumerate(names):
        if nm in hi:
            ax.add_patch(Rectangle((i - 0.47, vmin - span * 0.14), 0.94, span * 1.32, fc='#FFF3E8', ec='none', zorder=0))
    ax.plot([-0.6, n - 0.4], [0, 0], color='#8796AD', lw=1.6, zorder=2)
    for i in range(n):
        for k, (v, base) in enumerate([(A[i], NAVY), (B[i], ACC)]):
            if np.isnan(v): continue
            x0 = i - bw - 0.07 + k * (bw + 0.13)
            y0, h = (0, v) if v >= 0 else (v, -v)
            if h < span * 0.004: h = span * 0.004
            _grad_rect(ax, x0, y0, bw, h, _shade(base, 0.82), _shade(base, 1.25), horiz=False, z=3)
            ax.add_patch(Polygon([(x0, y0 + h), (x0 + bw, y0 + h), (x0 + bw + dx, y0 + h + dy), (x0 + dx, y0 + h + dy)], fc=_shade(base, 1.55), ec='none', zorder=4))
            ax.add_patch(Polygon([(x0 + bw, y0), (x0 + bw + dx, y0 + dy), (x0 + bw + dx, y0 + h + dy), (x0 + bw, y0 + h)], fc=_shade(base, 0.6), ec='none', zorder=4))
            fs = 17 if n <= 6 else 13
            lift = span * 0.075 if (k == 1 and A[i] == A[i] and A[i] >= 0 and v >= 0 and abs(v - A[i]) < span * 0.09 and v >= A[i]) else 0
            if k == 0 and B[i] == B[i] and B[i] >= 0 and v >= 0 and abs(v - B[i]) < span * 0.09 and v > B[i]: lift = span * 0.075
            if v >= 0: ax.text(x0 + bw / 2 + dx / 2, v + dy + span * 0.015 + lift, fmt(v), fontsize=fs, fontweight='bold', color=base, ha='center', va='bottom', zorder=6)
            else: ax.text(x0 + bw / 2, v - span * 0.02, fmt(v), fontsize=fs, fontweight='bold', color=base, ha='center', va='top', zorder=6)
    for i, nm in enumerate(names):
        xf = 0.05 + 0.92 * ((i + 0.6) / n)
        fig.text(xf, 0.225, _wrap(nm), fontsize=18 if n <= 6 else 14, color=INK, ha='center', va='top', fontweight='bold' if nm in hi else 'normal', linespacing=1.25)
        if tags is not None and tags[i]:
            fig.text(xf, 0.062, tags[i], fontsize=17 if n <= 6 else 14, color=ACC if nm in hi else '#4A5A72', ha='center', va='center', fontweight='bold')
    # 범례
    lx = fig.add_axes([0.04, 0.775, 0.92, 0.05]); lx.axis('off'); lx.set_xlim(0, 12); lx.set_ylim(0, 1)
    lx.add_patch(Rectangle((0.0, 0.2), 0.32, 0.6, fc=NAVY, ec='none')); lx.text(0.45, 0.5, la, fontsize=18, color=INK, va='center')
    off = 0.45 + len(la) * 0.27 + 0.6
    lx.add_patch(Rectangle((off, 0.2), 0.32, 0.6, fc=ACC, ec='none')); lx.text(off + 0.45, 0.5, lb, fontsize=18, color=INK, va='center')
    _title(fig, title, sub)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
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

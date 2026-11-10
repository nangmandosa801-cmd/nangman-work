#!/usr/bin/env python3
"""티스토리 talk7921 실거래가 페이지 생성기 (11/10)
사용: python3 pricepage.py <지역키> [--up]      지역키: misa gamil wirye deokpung sinjang pungsan hanam (all = 전부)
  → /home/claude/w/ts_pages/<slug>/index.html (그림 주소판) · local.html (01.jpg 상대경로판) · 01.jpg(대표) · 02.jpg~ · meta.json
  --up : 그림을 블로그 우체통 image 로 올려 주소를 index.html 에 넣고,
         드라이브 「블로그/협업/4_어사이드/티스토리/원고/<slug>」 에 index.html · 01.jpg · 02.jpg~ 를 덮어쓴다.
자료: /home/claude/rtn  (매매 M_hanam_2014_2026 <2021 · MH2021_2024 · M2025 · M2026 / 전월세 R2026, 하남 행만)
필터: 해제사유발생일 '-' · 직거래 제외 · 84㎡ = 전용 83~86 · 59㎡ = 전용 58~61 · 중앙값.
문장은 숫자를 끼우는 틀이다. 매달 같은 명령이면 숫자만 바뀐다.
"""
import sys, os, json, re, base64, html as H, datetime
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import viz3d as V

RTN = '/home/claude/rtn'
OUT = '/home/claude/w/ts_pages'
DRIVE = '블로그/협업/4_어사이드/티스토리/원고'

REG = {
    'misa': dict(slug='misa-apt-price', kw='미사 아파트 실거래가', name='미사', dongs=['망월동', '풍산동', '선동'],
                 define='미사 = 미사강변도시. 하남시 망월동 · 풍산동 · 선동 법정동의 아파트만 셉니다. 덕풍동 · 창우동 단지는 넣지 않았습니다.'),
    'gamil': dict(slug='gamil-apt-price', kw='감일 아파트 실거래가', name='감일', dongs=['감이동', '감일동'],
                  define='감일 = 하남 감일지구. 하남시 감이동 · 감일동 법정동의 아파트만 셉니다.'),
    'wirye': dict(slug='hanam-wirye-apt-price', kw='하남 위례 아파트 실거래가', name='하남 위례', dongs=['학암동'],
                  define='하남 위례 = 위례신도시 중 하남시 학암동 법정동의 아파트입니다. 송파구 · 성남시 위례는 넣지 않았습니다.'),
    'deokpung': dict(slug='hanam-deokpung-apt-price', kw='하남 덕풍동 아파트 실거래가', name='덕풍동', dongs=['덕풍동'],
                     define='덕풍동 = 하남시 덕풍동 법정동의 아파트입니다. 풍산 아이파크 단지도 주소가 덕풍동이라 여기에 들어갑니다.'),
    'sinjang': dict(slug='hanam-sinjang-apt-price', kw='하남 신장동 아파트 실거래가', name='신장동', dongs=['신장동'],
                    define='신장동 = 하남시 신장동 법정동의 아파트입니다.'),
    'pungsan': dict(slug='hanam-pungsan-apt-price', kw='하남 풍산동 아파트 실거래가', name='풍산동', dongs=['풍산동'],
                    define='풍산동 = 하남시 풍산동 법정동의 아파트입니다. 모두 미사강변도시 단지입니다. 풍산 아이파크는 주소가 덕풍동이라 빠집니다.'),
    'hanam': dict(slug='hanam-apt-price', kw='하남 아파트 실거래가', name='하남', dongs=None,
                  define='하남 = 하남시 전체 아파트. 동별 비교는 미사(망월 · 풍산 · 선동) · 감일(감이 · 감일동) · 위례(학암동) · 덕풍동 · 신장동 · 창우동으로 묶었습니다.'),
}
GROUP = {'망월동': '미사', '풍산동': '미사', '선동': '미사', '감이동': '감일', '감일동': '감일', '학암동': '위례',
         '덕풍동': '덕풍동', '신장동': '신장동', '창우동': '창우동'}

# ------------------------------------------------------------------ 자료
def _num(s): return pd.to_numeric(s.astype(str).str.replace(',', '').str.strip(), errors='coerce')

def load():
    cache = '/tmp/_ts_hanam.pkl'
    srcs = [f'{RTN}/{f}.pkl' for f in ['M_hanam_2014_2026', 'MH2021_2024', 'M2025', 'M2026', 'R2026']]
    if os.path.exists(cache) and os.path.getmtime(cache) > max(os.path.getmtime(f) for f in srcs):
        return pd.read_pickle(cache)
    parts = []
    h = pd.read_pickle(srcs[0]); parts.append(h[pd.to_numeric(h['계약년월']) < 202101])
    for f in srcs[1:4]:
        d = pd.read_pickle(f); parts.append(d[d['시군구'].str.contains('하남시')])
    m = pd.concat(parts, ignore_index=True)
    m = m[(m['해제사유발생일'].astype(str).str.strip() == '-') & (m['거래유형'].astype(str).str.strip() != '직거래')].copy()
    m = pd.DataFrame({'dong': m['시군구'].str.split().str[-1], 'apt': m['단지명'].str.strip(), 'a': _num(m['전용면적(㎡)']),
                      'ym': _num(m['계약년월']).astype(int), 'p': _num(m['거래금액(만원)']), 'by': _num(m['건축년도'])})
    r = pd.read_pickle(srcs[4]); r = r[r['시군구'].str.contains('하남시')]
    r = r[(r['전월세구분'] == '전세') & (r['계약구분'].astype(str).str.strip() == '신규')]
    r = pd.DataFrame({'dong': r['시군구'].str.split().str[-1], 'apt': r['단지명'].str.strip(), 'a': _num(r['전용면적(㎡)']),
                      'ym': _num(r['계약년월']).astype(int), 'p': _num(r['보증금(만원)'])})
    out = {'m': m, 'r': r}
    pd.to_pickle(out, cache)
    return out

def size(df, k):
    return df[(df.a >= 83) & (df.a <= 86)] if k == 84 else df[(df.a >= 58) & (df.a <= 61)]

def months_back(end, n):
    y, mo = divmod(end, 100); out = []
    for _ in range(n):
        out.append(y * 100 + mo); mo -= 1
        if mo == 0: y -= 1; mo = 12
    return out[::-1]

# ------------------------------------------------------------------ 글자 모양
def won(v):
    """만원 → '11억 2,000만' (천만 단위 반올림)"""
    if v is None or (isinstance(v, float) and np.isnan(v)): return '-'
    v = int(round(v / 100.0) * 100); e, r = divmod(v, 10000)
    if e == 0: return f'{r:,}만'
    return f'{e}억' + (f' {r:,}만' if r else '')
def pct(v, sign=True):
    if v is None or np.isnan(v): return '-'
    return (f'{v:+.1f}%' if sign else f'{v:.0f}%')
def ymlab(ym): return f'{ym // 100}년 {ym % 100}월'

TD = 'border:1px solid #D5DDE8;padding:9px 6px;text-align:center;font-size:15px'
TH = 'border:1px solid #1F3864;padding:10px 6px;background:#1F3864;color:#fff;font-size:15px;text-align:center'
def table(head, rows, first_left=True):
    h = ''.join(f'<th style="{TH}">{H.escape(x)}</th>' for x in head)
    body = ''
    for i, row in enumerate(rows):
        bg = '#F4F7FB' if i % 2 else '#FFFFFF'
        tds = ''.join(f'<td style="{TD};background:{bg}' + (';text-align:left;font-weight:bold' if j == 0 and first_left else '') + f'">{H.escape(str(c))}</td>'
                      for j, c in enumerate(row))
        body += f'<tr>{tds}</tr>'
    return f'<table style="width:100%;border-collapse:collapse;table-layout:auto;margin:14px 0"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'
def P(t): return f'<p style="font-size:17px;line-height:1.85;color:#22324A;margin:10px 0">{t}</p>'
def H2(t): return f'<h2 style="font-size:24px;color:#1F3864;border-left:6px solid #2E5C8A;padding-left:12px;margin:38px 0 12px">{H.escape(t)}</h2>'
def H3(t): return f'<h3 style="font-size:19px;color:#1F3864;margin:24px 0 6px">{H.escape(t)}</h3>'
def IMG(n, alt): return f'<p style="margin:16px 0;text-align:center"><img src="{{IMG{n:02d}}}" alt="{H.escape(alt)}" style="width:100%;max-width:1200px;height:auto"></p>'
def NOTE(t): return f'<div style="background:#F4F7FB;border:1px solid #D5DDE8;border-radius:8px;padding:14px 16px;margin:26px 0;font-size:14px;line-height:1.8;color:#4A5A72">{t}</div>'

# ------------------------------------------------------------------ 계산
def build(key, up=False):
    R = REG[key]; D = load(); m, r = D['m'], D['r']
    if R['dongs']: m = m[m.dong.isin(R['dongs'])]; r = r[r.dong.isin(R['dongs'])]
    m84, r84, m59, r59 = size(m, 84), size(r, 84), size(m, 59), size(r, 59)
    end = int(D['m']['ym'].max()); end = min(end, int(D['m'][D['m'].ym <= 209912].ym.max()))
    L6 = months_back(end, 6); L24 = months_back(end, 24); H21 = list(range(202107, 202113))
    today = datetime.date.today()
    title = f"{R['kw']} · 시세, 84㎡ 단지별 정리 ({today.year}년 {today.month}월 갱신)"
    if key == 'hanam': title = f"{R['kw']} · 시세, 동별 84㎡ 비교 ({today.year}년 {today.month}월 갱신)"
    d = os.path.join(OUT, R['slug']); os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith(('.jpg', '.png')): os.remove(os.path.join(d, f))

    s6 = m84[m84.ym.isin(L6)]; s21 = m84[m84.ym.isin(H21)]; j6 = r84[r84.ym.isin(L6)]
    med6, n6 = s6.p.median(), len(s6); med21 = s21.p.median(); jm6, jn6 = j6.p.median(), len(j6)
    chg = (med6 / med21 - 1) * 100 if med21 and n6 else np.nan
    jr = jm6 / med6 * 100 if n6 and jn6 else np.nan
    prev6 = m84[m84.ym.isin(months_back(L6[0] - 1 if L6[0] % 100 != 1 else L6[0] - 89, 6))]
    pmed = prev6.p.median(); chg6 = (med6 / pmed - 1) * 100 if len(prev6) and n6 else np.nan

    # 월별 (24개월, 3건 미만은 비움)
    g = m84[m84.ym.isin(L24)].groupby('ym').p.agg(['median', 'size'])
    mon = [g.loc[x, 'median'] if x in g.index and g.loc[x, 'size'] >= 3 else np.nan for x in L24]
    mlab = [f"{str(x // 100)[2:]}.{x % 100:02d}" for x in L24]
    monv = np.array(mon, float); okm = ~np.isnan(monv)
    mhi = L24[int(np.nanargmax(monv))]; mlo = L24[int(np.nanargmin(monv))]

    # 단지 표 (84) — 최근 6개월 2건 이상
    key_cols = ['dong', 'apt'] if not R['dongs'] or len(R['dongs']) > 1 else ['apt']
    def by_apt(df, L):
        x = df[df.ym.isin(L)].groupby(['dong', 'apt']).p.agg(['median', 'size']); return x
    a6 = by_apt(m84, L6); a21 = by_apt(m84, H21); aj = by_apt(r84, L6)
    yr = m.groupby(['dong', 'apt']).by.agg(lambda s: s.mode().iloc[0] if len(s.mode()) else np.nan)
    rows = []
    for (dg, ap), (md, n) in a6.iterrows():
        if n < 2: continue
        p21 = a21.loc[(dg, ap)] if (dg, ap) in a21.index else None
        c21 = (md / p21['median'] - 1) * 100 if p21 is not None and p21['size'] >= 2 else np.nan
        jj = aj.loc[(dg, ap)] if (dg, ap) in aj.index else None
        jmed = jj['median'] if jj is not None else np.nan
        rows.append(dict(dong=dg, apt=ap, yr=yr.get((dg, ap), np.nan), med=md, n=int(n), c21=c21,
                         j=jmed, jn=int(jj['size']) if jj is not None else 0, jr=jmed / md * 100 if jj is not None else np.nan,
                         grp=GROUP.get(dg, dg)))
    T = pd.DataFrame(rows).sort_values('med', ascending=False) if rows else pd.DataFrame()

    # 59
    b6 = by_apt(m59, L6); bj = by_apt(r59, L6); rows59 = []
    for (dg, ap), (md, n) in b6.iterrows():
        if n < 2: continue
        jj = bj.loc[(dg, ap)] if (dg, ap) in bj.index else None
        rows59.append(dict(apt=ap, dong=dg, med=md, n=int(n), j=jj['median'] if jj is not None else np.nan,
                           jn=int(jj['size']) if jj is not None else 0))
    T59 = pd.DataFrame(rows59).sort_values('med', ascending=False) if rows59 else pd.DataFrame()
    s59 = m59[m59.ym.isin(L6)]; med59, n59 = s59.p.median(), len(s59)

    # ------------------------------------------------------------ 그림
    imgs = []  # (파일, alt)
    def fig(name, alt): p = os.path.join(d, name); imgs.append((p, alt)); return p
    V.thumb(monv[okm] if okm.sum() >= 6 else np.linspace(1, 2, 12), fig('t.png', f"{R['name']} 아파트 실거래가 대표 그림"), seed=len(key))
    V.card_row([('최근 6개월 84㎡ 매매', V.eok(med6, 2) if n6 else '-', f'중앙값 · {n6}건'),
                ('2021년 하반기 대비', pct(chg), f'{V.eok(med21, 2)} → {V.eok(med6, 2)}' if n6 and med21 == med21 else ''),
                ('새 세입자 전세', V.eok(jm6, 2) if jn6 else '-', f'84㎡ 중앙값 · {jn6}건'),
                ('전세가율', pct(jr, False), '전세 ÷ 매매', 1)],
               fig('c.png', f"{R['name']} 아파트 84㎡ 실거래 요약 숫자"))
    V.ribbon_line(mlab, monv, fig('r.png', f"{R['name']} 84㎡ 월별 실거래 중앙값"),
                  f"{R['name']} 84㎡ 매매 중앙값 · 최근 24개월", f'{ymlab(L24[0])} ~ {ymlab(L24[-1])} · 한 달 3건 미만은 비움')
    if key == 'hanam':
        G = m84.assign(grp=m84.dong.map(GROUP)).dropna(subset=['grp'])
        gg = G[G.ym.isin(L6)].groupby('grp').p.agg(['median', 'size']).sort_values('median', ascending=False)
        V.iso_bars([f'{i} ({int(n)}건)' for i, n in gg['size'].items()], gg['median'].values, fig('i.png', '하남 동별 84㎡ 실거래 중앙값'),
                   '하남 동별 84㎡ 매매 중앙값', f'최근 6개월 ({ymlab(L6[0])} ~ {ymlab(L6[-1])})', hi=f"{gg.index[0]} ({int(gg['size'].iloc[0])}건)")
        rowsB = list(gg.index)
        q = G.assign(q=(G.ym // 100) * 10 + ((G.ym % 100) - 1) // 3 + 1)
    else:
        top = T.sort_values('n', ascending=False).head(12).sort_values('med', ascending=False) if len(T) else T
        if len(top):
            V.iso_bars([a for a in top.apt], top.med.values, fig('i.png', f"{R['name']} 단지별 84㎡ 실거래 중앙값"),
                       f"{R['name']} 단지별 84㎡ 매매 중앙값", f'최근 6개월 · 거래 많은 {len(top)}개 단지', hi=top.apt.iloc[0])
        rowsB = list(T.sort_values('n', ascending=False).head(6).sort_values('med').apt) if len(T) else []
        q = m84[m84.apt.isin(rowsB)].assign(grp=lambda x: x.apt, q=lambda x: (x.ym // 100) * 10 + ((x.ym % 100) - 1) // 3 + 1)
    endq = (end // 100) * 10 + ((end % 100) - 1) // 3 + 1
    Q = []; y_, k_ = divmod(endq, 10)
    for _ in range(8):
        Q.append(y_ * 10 + k_); k_ -= 1
        if k_ == 0: y_ -= 1; k_ = 4
    Q = Q[::-1]
    if rowsB:
        qq = q[q.q.isin(Q)].groupby(['grp', 'q']).p.median()
        Z = [[qq.get((rw, x), np.nan) for x in Q] for rw in rowsB]
        V.bar3d_months(rowsB, [f"{str(x // 10)[2:]}년{x % 10}Q" for x in Q], Z, fig('b.png', f"{R['name']} 84㎡ 분기별 실거래 중앙값 입체 막대"),
                       f"{R['name']} {'동별' if key == 'hanam' else '단지별'} 84㎡ 분기 중앙값", f'최근 8개 분기 · 마지막 분기는 {ymlab(end)}까지 · 빈 칸은 거래 없음')
    # 번호 붙이기: 01 = 대표, 이후 본문 순서
    from PIL import Image
    files = []
    for i, (p, alt) in enumerate(imgs, 1):
        j = os.path.join(d, f'{i:02d}.jpg'); Image.open(p).convert('RGB').save(j, quality=93); os.remove(p); files.append((j, alt))

    # ------------------------------------------------------------ 본문
    nm = R['name']; B = []
    B.append(f'<p style="font-size:14px;color:#6B7A90;margin:0 0 6px">갱신 {today.year}.{today.month:02d}.{today.day:02d} · 자료 {ymlab(L6[0])} ~ {ymlab(end)} 계약분 · 국토교통부 실거래</p>')
    B.append(P(f'{nm} 아파트 84㎡(34평) 실거래가를 단지별로 모았습니다. 숫자는 매달 새로 바꿉니다.'))
    B.append(P(f'최근 6개월 {nm} 84㎡ 매매는 {n6}건입니다. 가운데 값은 <b>{won(med6)}</b>입니다.'
               + (f' 바로 앞 6개월은 {won(pmed)}였습니다({pct(chg6)}).' if chg6 == chg6 else '')))
    B.append(IMG(2, files[1][1]))
    B.append(H2(f'{nm} 아파트 실거래가 · 월별 흐름'))
    B.append(IMG(3, files[2][1]))
    B.append(P(f'24개월 동안 한 달 가운데 값이 가장 높았던 때는 {ymlab(mhi)}({won(g.loc[mhi, "median"])})입니다. '
               f'가장 낮았던 때는 {ymlab(mlo)}({won(g.loc[mlo, "median"])})입니다.'))
    lastok = [x for x in L24 if x in g.index and g.loc[x, 'size'] >= 3][-1]
    B.append(P(f'마지막 칸 {ymlab(lastok)}은 {int(g.loc[lastok, "size"])}건, {won(g.loc[lastok, "median"])}입니다.'
               + (f' {ymlab(end)} 계약은 신고 기한(30일)이 남아 건수가 더 늘 수 있습니다.' if end == L24[-1] else '')))
    if key == 'hanam':
        B.append(H2('하남 아파트 시세 · 동별 84㎡ 비교'))
        B.append(IMG(4, files[3][1]))
        G6 = m84.assign(grp=m84.dong.map(GROUP))
        rowsG = []
        for gname in gg.index:
            x6 = G6[(G6.grp == gname) & G6.ym.isin(L6)]; x21 = G6[(G6.grp == gname) & G6.ym.isin(H21)]
            rj = r84.assign(grp=r84.dong.map(GROUP)); xj = rj[(rj.grp == gname) & rj.ym.isin(L6)]
            c = (x6.p.median() / x21.p.median() - 1) * 100 if len(x21) else np.nan
            rowsG.append([gname, won(x6.p.median()), f'{len(x6)}건', pct(c), won(xj.p.median()) if len(xj) else '-',
                          pct(xj.p.median() / x6.p.median() * 100, False) if len(xj) else '-'])
        B.append(table(['동', '84㎡ 매매 중앙값', '건수', '2021 하반기 대비', '새 전세 중앙값', '전세가율'], rowsG))
        g0, g1 = gg.index[0], gg.index[-1]
        B.append(P(f'6개월 가운데 값은 {g0}가 {won(gg.loc[g0, "median"])}로 가장 높습니다. {g1}는 {won(gg.loc[g1, "median"])}입니다. '
                   f'두 곳 차이는 {won(gg.loc[g0, "median"] - gg.loc[g1, "median"])}입니다.'))
        B.append(H2('하남 아파트 시세 · 분기별 입체 그림'))
        B.append(IMG(5, files[4][1]))
        B.append(P('막대 하나가 한 분기(3개월)의 가운데 값입니다. 주황 막대는 마지막 분기에서 가장 높은 곳입니다. 마지막 분기는 아직 다 채워지지 않은 달이 들어 있습니다.'))
    B.append(H2(f'{nm} 아파트 84㎡ 단지별 시세표'))
    B.append(P(f'최근 6개월({ymlab(L6[0])} ~ {ymlab(L6[-1])}) 84㎡ 매매가 2건 이상인 단지만 넣었습니다. 비싼 순서입니다.'))
    if len(T):
        show_dong = (R['dongs'] is None) or len(R['dongs']) > 1
        head = ['단지'] + (['동'] if show_dong else []) + ['입주', '84㎡ 매매 중앙값', '건수', '2021 하반기 대비', '새 전세 중앙값', '전세가율']
        rr = []
        for _, x in T.iterrows():
            rr.append([x.apt] + ([x.dong] if show_dong else []) + [f'{int(x.yr)}' if x.yr == x.yr else '-', won(x.med), f'{x.n}건',
                       pct(x.c21), won(x.j) if x.jn else '-', pct(x.jr, False) if x.jn else '-'])
        B.append(table(head, rr))
        t0, t1 = T.iloc[0], T.iloc[-1]
        B.append(P(f'가장 높은 단지는 {t0.apt}({won(t0.med)})입니다. 표의 마지막은 {t1.apt}({won(t1.med)})입니다. '
                   f'두 단지 차이는 {won(t0.med - t1.med)}입니다.'))
        busy = T.sort_values('n', ascending=False).iloc[0]
        B.append(P(f'거래가 가장 많았던 단지는 {busy.apt}로 {busy.n}건입니다.'))
        if key != 'hanam':
            B.append(IMG(4, files[3][1]))
            if len(files) > 4:
                B.append(H3(f'{nm} 거래 많은 단지 · 분기별 입체 그림'))
                B.append(IMG(5, files[4][1]))
                B.append(P('막대 하나가 한 분기(3개월)의 가운데 값입니다. 뒤쪽 줄일수록 값이 높은 단지입니다. 막대가 없으면 그 분기에 84㎡ 거래가 없었습니다.'))
    B.append(H2(f'{nm} 아파트 59㎡ 시세표'))
    if len(T59):
        B.append(P(f'59㎡(25평)는 최근 6개월 {n59}건, 가운데 값 {won(med59)}입니다.'))
        B.append(table(['단지', '59㎡ 매매 중앙값', '건수', '새 전세 중앙값'],
                       [[x.apt, won(x.med), f'{x.n}건', won(x.j) if x.jn else '-'] for _, x in T59.iterrows()]))
    else:
        B.append(P(f'최근 6개월 59㎡ 매매가 2건 넘는 단지가 없습니다. 전체 {n59}건입니다.'))
    B.append(H2('이 표 읽는 법'))
    B.append(P('<b>중앙값</b>은 거래를 값 순서로 줄 세웠을 때 한가운데 값입니다. 한두 건 튀는 거래에 덜 흔들립니다.'))
    B.append(P('<b>건수</b>가 2~3건이면 층 · 향에 따라 숫자가 크게 움직입니다. 건수를 같이 보세요.'))
    B.append(P('<b>2021 하반기 대비</b>는 2021년 7~12월 같은 단지 84㎡ 가운데 값과 비교한 것입니다. 그때 거래가 2건 미만이면 비워 뒀습니다.'))
    B.append(P('<b>새 전세</b>는 새로 들어온 세입자 계약만 셉니다. 기존 세입자의 갱신 계약은 뺐습니다. 전세가율은 새 전세 ÷ 매매 가운데 값입니다.'))
    B.append(H2(f'{nm} 아파트 실거래가 · 자주 묻는 질문'))
    B.append(H3(f'{nm} 84㎡ 지금 얼마에 거래되나요?'))
    B.append(P(f'최근 6개월 {n6}건의 가운데 값은 {won(med6)}입니다.' + (f' 단지별로는 {won(T.med.min())} ~ {won(T.med.max())}입니다.' if len(T) else '')))
    B.append(H3('2021년 하반기보다 올랐나요?'))
    if chg == chg:
        B.append(P(f'2021년 7~12월 {nm} 84㎡ 가운데 값은 {won(med21)}였습니다. 지금은 {won(med6)}입니다. '
                   + (f'{pct(chg)} 높습니다.' if chg >= 0 else f'{pct(chg)}, 아직 그때보다 낮습니다.')))
        if len(T) and T.c21.notna().sum():
            n_up = int((T.c21 >= 0).sum()); tot = int(T.c21.notna().sum())
            B.append(P(f'비교할 수 있는 {tot}개 단지 중 {n_up}개가 그때 값 이상입니다.'))
    else:
        B.append(P('2021년 하반기 84㎡ 거래가 적어 비교하지 않았습니다.'))
    B.append(H3(f'{nm} 84㎡ 전세는 얼마인가요?'))
    B.append(P(f'최근 6개월 새 세입자 전세 {jn6}건의 가운데 값은 {won(jm6)}입니다. 매매 가운데 값의 {pct(jr, False)}입니다.' if jn6 else '최근 6개월 새 전세 계약이 없습니다.'))
    B.append(H3(f'{nm} 59㎡는 얼마인가요?'))
    B.append(P(f'최근 6개월 59㎡ {n59}건, 가운데 값은 {won(med59)}입니다. 84㎡와 차이는 {won(med6 - med59)}입니다.' if n59 and n6 else '최근 6개월 59㎡ 거래가 적습니다.'))
    B.append(NOTE('<b>NOTE</b><br>'
                  f'· 출처: 국토교통부 아파트 매매 · 전월세 실거래가 공개 자료. {ymlab(end)} 계약분까지 반영했습니다.<br>'
                  f'· 지역: {H.escape(R["define"])}<br>'
                  '· 뺀 거래: 계약이 취소된 거래(해제), 중개사 없이 한 직거래.<br>'
                  '· 84㎡ = 전용면적 83~86㎡, 59㎡ = 전용면적 58~61㎡. 값은 모두 중앙값입니다.<br>'
                  '· 전세: 신규 계약만. 갱신 계약 · 월세는 넣지 않았습니다. 전세 자료는 2026년 1월 계약분부터 씁니다.<br>'
                  '· 단지 표는 최근 6개월 2건 이상인 단지만 넣었습니다. 단지 이름은 국토교통부 표기 그대로입니다.'))
    body = '\n'.join(B)
    tags = [R['kw'], f"{R['name']} 아파트 시세", f"{R['name']} 아파트 매매", f"{R['name']} 아파트 전세", '하남 아파트 실거래가', '84㎡ 시세']
    tags = list(dict.fromkeys(tags))[:6]

    def render(srcmap):
        b = body
        for i in range(2, len(files) + 1): b = b.replace('{IMG%02d}' % i, srcmap[i])
        return (f'<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8"><title>{H.escape(title)}</title>'
                f'<meta name="description" content="{H.escape(strip(B[1])[:150])}"></head>\n<body style="max-width:1000px;margin:0 auto;font-family:sans-serif">\n'
                f'<!-- 제목: {H.escape(title)} -->\n<!-- 태그: {", ".join(tags)} -->\n<!-- 대표 이미지: 01.jpg -->\n{b}\n</body></html>\n')
    local = {i: f'{i:02d}.jpg' for i in range(1, len(files) + 1)}
    open(os.path.join(d, 'local.html'), 'w').write(render(local))
    urls = local
    if up:
        sys.path.insert(0, '/home/claude/helper'); from gas import call
        urls = {}
        stamp = today.strftime('%Y%m')
        for i, (p, _) in enumerate(files, 1):
            res = call('image', name=f"ts_{R['slug']}_{stamp}_{i:02d}.jpg", b64=base64.b64encode(open(p, 'rb').read()).decode())
            urls[i] = res['url']
    html_out = render(urls)
    open(os.path.join(d, 'index.html'), 'w').write(html_out)
    text = strip(body)
    ban = [w for w in ['고요', '갈렸', '갈랐', '갈라', '최고', '분양', '매물', '인테리어', '010-'] if w in text]
    meta = dict(key=key, slug=R['slug'], title=title, tags=tags, chars=len(text.replace(' ', '')), chars_sp=len(text),
                images=len(files), drive=f"{DRIVE}/{R['slug']}" if up else None, ban=ban,
                core=dict(end=end, med84_6m=med6, n84_6m=n6, med84_2021h2=med21, chg_vs_2021h2=round(chg, 1) if chg == chg else None,
                          prev6=pmed, jeonse_new=jm6, jeonse_n=jn6, jeonse_ratio=round(jr, 1) if jr == jr else None,
                          med59_6m=med59, n59=n59, apts=len(T),
                          top=(T.iloc[0].apt, T.iloc[0].med) if len(T) else None))
    json.dump(meta, open(os.path.join(d, 'meta.json'), 'w'), ensure_ascii=False, indent=1, default=float)
    if up:
        for p in [os.path.join(d, 'index.html')] + [f for f, _ in files]:
            mime = 'text/html' if p.endswith('.html') else 'image/jpeg'
            call('fput', path=f"{DRIVE}/{R['slug']}", name=os.path.basename(p), mime=mime,
                 b64=base64.b64encode(open(p, 'rb').read()).decode())
    return meta

def strip(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = H.unescape(s); return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]; up = '--up' in sys.argv
    keys = list(REG) if not a or a[0] == 'all' else a
    for k in keys:
        mt = build(k, up)
        print(json.dumps({x: mt[x] for x in ['key', 'title', 'chars', 'images', 'drive', 'ban']}, ensure_ascii=False))

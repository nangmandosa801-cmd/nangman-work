#!/usr/bin/env python3
"""티스토리 talk7921 실거래가 페이지 생성기 (11/10)
사용: python3 pricepage.py <지역키> [--up]      지역키: misa gamil wirye deokpung sinjang pungsan hanam (all = 전부)
  → /home/claude/w/ts_pages/<slug>/index.html (그림 주소판) · local.html (01.jpg 상대경로판) · 01.jpg(대표) · 02.jpg~ · meta.json
  --up : 그림을 블로그 우체통 image 로 올려 주소를 index.html 에 넣고,
         드라이브 「블로그/협업/4_어사이드/티스토리/원고/<slug>」 에 index.html · 01.jpg · 02.jpg~ 를 덮어쓴다.
자료: /home/claude/rtn  (매매 M_hanam_2014_2026 <2021 · MH2021_2024 · M2025 · M2026 / 전월세 R2026, 하남 행만)
필터: 해제사유발생일 '-' · 직거래 제외 · 84㎡ = 전용 83~86 · 59㎡ = 전용 58~61 · 중앙값.
문장은 숫자를 끼우는 틀이다. 매달 같은 명령이면 숫자만 바뀐다.
  --gblog : 구글 블로그(낭만 부동산 budongsan)용 gblog.html 도 만든다. 그림은 우체통 image 로 올린다(드라이브 원고는 건드리지 않음).
            맨 위에 「이번 달 눈에 띄는 점 3가지」(insights() 가 다섯 후보 중 점수 높은 셋을 고름) + 그림 1장(마지막 번호),
            맨 아래 「이 동네 분석 글」(gblog_links.json — 발행된 네이버 글만). 올리기 · 매달 고치기는 gblog_pub.py.
"""
import sys, os, json, re, base64, html as H, datetime
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import viz2d as V   # 11/10: 평평한 2D만(3D · 겹침 금지 · 막대 ≤5 · 결론 한 줄)

RTN = '/home/claude/rtn'
OUT = '/home/claude/w/ts_pages'
DRIVE = '블로그/협업/4_어사이드/티스토리/원고'

REG = {
    'misa': dict(slug='misa-apt-price', kw='미사 아파트 실거래가', name='미사', dongs=['망월동', '풍산동', '선동'],
                 define='미사 = 미사강변도시. 하남시 망월동 · 풍산동 · 선동 법정동의 아파트만 셉니다. 덕풍동 · 창우동 단지는 넣지 않았습니다.'),
    'gamil': dict(slug='gamil-apt-price', kw='감일 아파트 실거래가', name='감일', dongs=['감이동', '감일동'],
                  define='감일 = 하남 감일지구. 하남시 감이동 · 감일동 법정동의 아파트만 셉니다.'),
    'wirye': dict(slug='hanam-wirye-apt-price', kw='하남 위례 아파트 실거래가', name='하남 위례', dongs=['학암동'],
                  define='하남 위례 = 위례신도시 중 하남시 학암동 법정동의 아파트입니다. 송파구 · 성남시 위례는 넣지 않았습니다. 이곳은 거래 대부분이 전용 95~105㎡라서 이 크기를 먼저 셉니다.',
                  S1=('95~105㎡', 95, 105, ''), S2=('84㎡', 83, 86, '(34평)')),
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

S84, S59 = ('84㎡', 83, 86, '(34평)'), ('59㎡', 58, 61, '(25평)')
def size(df, S):
    if isinstance(S, int): S = S84 if S == 84 else S59
    return df[(df.a >= S[1]) & (df.a <= S[2])]

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
def josa(w, a, b):
    """받침 있으면 a, 없으면 b. 으로/로는 ㄹ받침도 b."""
    c = (w.strip().rstrip(')] ') or w.strip())[-1]
    if not ('가' <= c <= '힣'):
        return b if c.isdigit() and c in '2459' else (a if c.isalnum() else b)
    jong = (ord(c) - 0xAC00) % 28
    if a == '으로' and jong == 8: return b
    return a if jong else b
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

# ------------------------------------------------------------------ 이번 달 눈에 띄는 점 (구글 블로그용)
def _span(L):
    a, b = L[0], L[-1]
    return f'{a // 100}년 {a % 100}~{b % 100}월' if a // 100 == b // 100 else f'{ymlab(a)} ~ {ymlab(b)}'
def _eun(w): return w + josa(w, '은', '는')
def _i(w): return w + josa(w, '이', '가')

def insights(key, m84, r84, end, W, L6, PREV, H21, SA, T, pick=3):
    """후보 다섯(오른 폭 차이 · 전세가율 · 매매와 전세 엇갈림 · 2021 하반기 대비/순서 · 거래 건수)을 만들고 점수 높은 순으로 pick 개.
    묶음: hanam 은 동 묶음(GROUP), 나머지는 단지. 건수 문턱: 동 10건 · 단지 5건(전세 3건). 돌려줌: [dict(kind, score, title, body, fig)]"""
    grp = key == 'hanam'
    if grp:
        m = m84.assign(u=m84.dong.map(GROUP)).dropna(subset=['u']); r = r84.assign(u=r84.dong.map(GROUP)).dropna(subset=['u'])
        NM, NJ, word = 10, 10, '곳'
    else:
        m = m84.assign(u=m84.apt); r = r84.assign(u=r84.apt); NM, NJ, word = 5, 3, '단지'
    def ag(df, L): return df[df.ym.isin(L)].groupby('u').p.agg(['median', 'size'])
    a6, ap, a21, aj = ag(m, L6), ag(m, PREV), ag(m, H21), ag(r, L6)
    pc = lambda v: f'{v:+.1f}%'
    out = []
    # ① 오른 폭 1위와 꼴찌
    x = a6.join(ap, rsuffix='_p', how='inner'); x = x[(x['size'] >= NM) & (x['size_p'] >= NM)]
    if len(x) >= 3:
        x = x.assign(c=(x['median'] / x['median_p'] - 1) * 100).sort_values('c', ascending=False)
        t, b = x.index[0], x.index[-1]; gap = x.c.iloc[0] - x.c.iloc[-1]
        body = (f'앞 {W}개월({_span(PREV)})과 최근 {W}개월({_span(L6)})의 {SA} 매매 가운데 값을 비교했습니다. '
                f'{_eun(t)} {won(x.loc[t, "median_p"])} → {won(x.loc[t, "median"])}입니다({pc(x.c.iloc[0])}, 최근 {int(x.loc[t, "size"])}건). '
                f'{_eun(b)} {won(x.loc[b, "median_p"])} → {won(x.loc[b, "median"])}입니다({pc(x.c.iloc[-1])}, 최근 {int(x.loc[b, "size"])}건). '
                f'두 {word} 차이는 {gap:.1f}%p입니다.')
        if b == x['median'].idxmax(): body += f' 값이 가장 높은 {_i(b)} 가장 적게 올랐습니다.' if x.c.iloc[-1] >= 0 else f' 값이 가장 높은 {_i(b)} 내렸습니다.'
        show = x if len(x) <= 8 else pd.concat([x.head(4), x.tail(4)])
        out.append(dict(kind='rise', score=gap / 5, title=f'최근 {W}개월 {t} {pc(x.c.iloc[0])}, {b} {pc(x.c.iloc[-1])}',
                        body=body, fig=dict(type='cards', title=f'{SA} 매매 가운데 값 · 앞 {W}개월과 최근 {W}개월',
                                            cards=[(t, pc(x.c.iloc[0]), f'{V.eok(x.loc[t, "median_p"])} → {V.eok(x.loc[t, "median"])}'),
                                                   (b, pc(x.c.iloc[-1]), f'{V.eok(x.loc[b, "median_p"])} → {V.eok(x.loc[b, "median"])}'),
                                                   (f'두 {word} 차이', f'{gap:.1f}%p', f'최근 {W}개월에 오른 폭')],
                                            note=f'{SA} 매매 가운데 값 · {_span(PREV)} → {_span(L6)}')))
    # ② 전세가율이 가장 높은 곳 · 낮은 곳
    x = a6.join(aj, rsuffix='_j', how='inner'); x = x[(x['size'] >= NM) & (x['size_j'] >= NJ)]
    if len(x) >= 3:
        x = x.assign(jr=x['median_j'] / x['median'] * 100).sort_values('jr', ascending=False)
        h, l = x.index[0], x.index[-1]; gap = x.jr.iloc[0] - x.jr.iloc[-1]
        body = (f'최근 {W}개월 {SA} 기준입니다. {_eun(h)} 매매 {won(x.loc[h, "median"])}에 새 전세 {won(x.loc[h, "median_j"])}입니다. '
                f'둘의 차이는 {won(x.loc[h, "median"] - x.loc[h, "median_j"])}입니다. '
                f'{_eun(l)} 매매 {won(x.loc[l, "median"])}에 새 전세 {won(x.loc[l, "median_j"])}입니다. '
                f'차이는 {won(x.loc[l, "median"] - x.loc[l, "median_j"])}입니다. '
                + (f'두 {word}의 전세 값은 {won(abs(x.loc[l, "median_j"] - x.loc[h, "median_j"]))} 차이인데, 매매 값은 {won(abs(x.loc[l, "median"] - x.loc[h, "median"]))} 차이입니다.'
                   if abs(x.loc[l, "median_j"] - x.loc[h, "median_j"]) >= 100 else f'두 {word}의 전세 값은 같은데, 매매 값은 {won(abs(x.loc[l, "median"] - x.loc[h, "median"]))} 차이입니다.'))
        show = x if len(x) <= 8 else pd.concat([x.head(4), x.tail(4)])
        out.append(dict(kind='jr', score=gap / 10, title=f'전세가율은 {h} {x.jr.iloc[0]:.0f}%, {l} {x.jr.iloc[-1]:.0f}%',
                        body=body, fig=dict(type='bars', title=f'{SA} 전세가율이 가장 높은 곳과 낮은 곳', names=[h, l], values=[x.jr.iloc[0], x.jr.iloc[-1]], hi=0,
                                            fmt=lambda v: f'{v:.0f}%', subs=[f'매매 {V.eok(x.loc[u, "median"])} · 전세 {V.eok(x.loc[u, "median_j"])}' for u in (h, l)],
                                            note=f'{SA} 새 전세 ÷ 매매 가운데 값 · 최근 {W}개월({_span(L6)})')))
    # ③ 매매와 전세가 다르게 움직인 곳 (전세 자료가 있는 달을 앞 · 뒤 절반으로)
    JM = [y for y in months_back(end, 24) if y >= int(r84.ym.min())] if len(r84) else []
    if len(JM) >= 6:
        hf = len(JM) // 2; A_, B_ = JM[:hf], JM[-hf:]
        x = ag(m, A_).join(ag(m, B_), rsuffix='_b', how='inner').join(ag(r, A_).add_prefix('j_'), how='inner').join(ag(r, B_).add_prefix('jb_'), how='inner')
        x = x[(x['size'] >= NM) & (x['size_b'] >= NM) & (x['j_size'] >= max(NJ, 5)) & (x['jb_size'] >= max(NJ, 5))]
        if len(x) >= 3:
            x = x.assign(cm=(x['median_b'] / x['median'] - 1) * 100, cj=(x['jb_median'] / x['j_median'] - 1) * 100)
            x = x.assign(d=x.cj - x.cm).sort_values('d', ascending=False)
            u1, u2 = x.index[0], x.index[-1]; d1, d2 = x.d.iloc[0], x.d.iloc[-1]
            if d1 > 0 and d2 < 0:
                sa, sb = _span(A_), _span(B_); sb = sb.split('년 ')[-1] if A_[0] // 100 == B_[-1] // 100 else sb
                body = (f'{sa}과 {sb} 두 기간의 {SA} 가운데 값을 비교했습니다. '
                        f'{u1}의 새 전세는 {won(x.loc[u1, "j_median"])} → {won(x.loc[u1, "jb_median"])}입니다({pc(x.loc[u1, "cj"])}). '
                        f'같은 기간 매매는 {won(x.loc[u1, "median"])} → {won(x.loc[u1, "median_b"])}입니다({pc(x.loc[u1, "cm"])}). '
                        f'{_eun(u2)} 반대입니다. 매매가 {won(x.loc[u2, "median"])} → {won(x.loc[u2, "median_b"])}입니다({pc(x.loc[u2, "cm"])}). '
                        f'새 전세는 {won(x.loc[u2, "j_median"])} → {won(x.loc[u2, "jb_median"])}입니다({pc(x.loc[u2, "cj"])}).')
                show = x if len(x) <= 8 else pd.concat([x.head(4), x.tail(4)])
                out.append(dict(kind='cross', score=(d1 - d2) / 5,
                                title=f'{_eun(u1)} 전세 {pc(x.loc[u1, "cj"])} · 매매 {pc(x.loc[u1, "cm"])}, {_eun(u2)} 반대',
                                body=body, fig=dict(type='cards', title=f'{SA} · 매매와 새 전세가 오른 폭',
                                                    cards=[(f'{u1} · 새 전세', pc(x.loc[u1, "cj"]), f'같은 기간 매매 {pc(x.loc[u1, "cm"])}'),
                                                           (f'{u2} · 새 전세', pc(x.loc[u2, "cj"]), f'같은 기간 매매 {pc(x.loc[u2, "cm"])}')],
                                                    note=f'{SA} 가운데 값 · {sa} → {sb}')))
    # ④ 2021년 하반기 대비 (동 묶음: 넘은 폭 차이 · 단지: 값 순서가 바뀐 곳)
    x = a6.join(a21, rsuffix='_o', how='inner'); x = x[(x['size'] >= (NM if grp else 3)) & (x['size_o'] >= (NM if grp else 3))]
    if len(x) >= 3:
        x = x.assign(c=(x['median'] / x['median_o'] - 1) * 100)
        below = int((x.c < 0).sum())
        tc = T[T.c21.notna()] if len(T) else T
        tail = ''
        if grp and len(tc):
            k = int((tc.c21 < 0).sum())
            tail = f' 단지로 보면 비교할 수 있는 {len(tc)}개 단지 중 {k}개가 아직 그때 값 아래입니다.' if k else f' 단지로 봐도 비교할 수 있는 {len(tc)}개 단지가 모두 그때 값 이상입니다.'
        if grp:
            x = x.sort_values('c', ascending=False); t, b = x.index[0], x.index[-1]
            head = (f'{len(x)}곳 모두 2021년 7~12월 가운데 값을 넘었습니다. 넘은 폭은 다릅니다. ' if not below
                    else f'{len(x)}곳 중 {below}곳이 아직 2021년 7~12월 가운데 값 아래입니다. ')
            body = (head + f'{_eun(t)} {won(x.loc[t, "median_o"])} → {won(x.loc[t, "median"])}입니다({pc(x.c.iloc[0])}). '
                    f'{_eun(b)} {won(x.loc[b, "median_o"])} → {won(x.loc[b, "median"])}입니다({pc(x.c.iloc[-1])}).' + tail)
            out.append(dict(kind='h21', score=(x.c.iloc[0] - x.c.iloc[-1]) / 8 + (1 if below else 0),
                            title=(f'{below}곳이 아직 2021년 하반기 값 아래' if below else f'2021년 하반기보다 {t} {pc(x.c.iloc[0])}, {b} {pc(x.c.iloc[-1])}'),
                            body=body, fig=dict(type='cards', title=f'{SA} 매매 가운데 값 · 2021년 하반기와 지금',
                                                cards=[(t, pc(x.c.iloc[0]), f'{V.eok(x.loc[t, "median_o"])} → {V.eok(x.loc[t, "median"])}'),
                                                       (b, pc(x.c.iloc[-1]), f'{V.eok(x.loc[b, "median_o"])} → {V.eok(x.loc[b, "median"])}'),
                                                       ('두 곳 차이', f'{x.c.iloc[0] - x.c.iloc[-1]:.1f}%p', '2021년 하반기보다 오른 폭')],
                                                note=f'{SA} 매매 가운데 값 · 2021년 7~12월 → {_span(L6)}')))
        else:
            x = x.assign(r0=x['median_o'].rank(ascending=False, method='min').astype(int), r1=x['median'].rank(ascending=False, method='min').astype(int))
            x = x.assign(j=x.r0 - x.r1).sort_values('j', ascending=False); u, dn = x.index[0], x.index[-1]
            if x.j.iloc[0] >= 2:
                body = (f'2021년 7~12월과 최근 {W}개월 모두 {SA} 매매가 3건 이상인 {len(x)}개 단지를 값이 높은 순서로 세웠습니다. '
                        f'{_eun(u)} {x.loc[u, "r0"]}번째 → {x.loc[u, "r1"]}번째입니다({won(x.loc[u, "median_o"])} → {won(x.loc[u, "median"])}, {pc(x.loc[u, "c"])}).')
                if x.j.iloc[-1] <= -2:
                    body += f' {_eun(dn)} {x.loc[dn, "r0"]}번째 → {x.loc[dn, "r1"]}번째입니다({won(x.loc[dn, "median_o"])} → {won(x.loc[dn, "median"])}, {pc(x.loc[dn, "c"])}).'
                body += (f' {len(x)}개 단지 중 {below}개는 아직 2021년 하반기 값 아래입니다.' if below else f' {len(x)}개 단지 모두 2021년 하반기 값보다는 높습니다.')
                show = x.sort_values('r1'); show = show if len(show) <= 8 else pd.concat([show[show.index.isin([u, dn])], show[~show.index.isin([u, dn])].head(6)]).sort_values('r1')
                out.append(dict(kind='rank', score=(x.j.iloc[0] - min(x.j.iloc[-1], 0)) / 4,
                                title=f'2021년 하반기 {x.loc[u, "r0"]}번째였던 {_i(u)} 지금은 {x.loc[u, "r1"]}번째',
                                body=body, fig=dict(type='cards', title=f'{SA} 매매 가운데 값 · 2021년 하반기와 지금',
                                                    cards=[(z_, f'{x.loc[z_, "r0"]}번째 → {x.loc[z_, "r1"]}번째', f'{V.eok(x.loc[z_, "median_o"])} → {V.eok(x.loc[z_, "median"])} · {pc(x.loc[z_, "c"])}')
                                                           for z_ in ([u, dn] if x.j.iloc[-1] <= -2 else [u])],
                                                    note=f'{SA} 값이 높은 순서 · {len(x)}개 단지 · 2021년 7~12월 → {_span(L6)}')))
    # ⑤ 거래 건수 (마지막 달은 신고가 덜 끝나 뺀다)
    full = months_back(end, 7)[:-1]; q0, q1 = full[:3], full[3:]
    n0, n1 = int(m84.ym.isin(q0).sum()), int(m84.ym.isin(q1).sum())
    if n0 >= 20 and n1 >= 10:
        ch = (n1 / n0 - 1) * 100; p0, p1 = m84[m84.ym.isin(q0)].p.median(), m84[m84.ym.isin(q1)].p.median(); cp = (p1 / p0 - 1) * 100
        body = (f'{ymlab(end)} 계약은 신고 기한이 남아 빼고 세었습니다. {SA} 매매는 {_span(q0)} {n0}건, {_span(q1).split("년 ")[-1]} {n1}건입니다({pc(ch)}). '
                f'같은 기간 가운데 값은 {won(p0)} → {won(p1)}입니다({pc(cp)}).')
        if ch < 0 and cp > 0: body += ' 거래는 줄었는데 값은 올랐습니다.'
        elif ch > 0 and cp < 0: body += ' 거래는 늘었는데 값은 내렸습니다.'
        out.append(dict(kind='vol', score=abs(ch) / 15, title=f'{SA} 거래 {n0}건 → {n1}건({pc(ch)}), 값은 {pc(cp)}', body=body, fig=None))
    out.sort(key=lambda z: -z['score'])
    return out[:pick]

# ------------------------------------------------------------------ 계산
def build(key, up=False, gblog=False):
    R = REG[key]; D = load(); m, r = D['m'], D['r']
    if R['dongs']: m = m[m.dong.isin(R['dongs'])]; r = r[r.dong.isin(R['dongs'])]
    S1, S2 = R.get('S1', S84), R.get('S2', S59); SA, SAP, SB, SBP = S1[0], S1[3], S2[0], S2[3]
    m84, r84, m59, r59 = size(m, S1), size(r, S1), size(m, S2), size(r, S2)
    endm = int(D['m'].ym.max())
    def clean_r(rr, mm):
        ref = mm[mm.ym.isin(months_back(endm, 12))].groupby(['dong', 'apt']).p.median()
        k = list(zip(rr.dong, rr.apt)); base = np.array([ref.get(x, np.nan) for x in k])
        keep = ~(base == base) | (rr.p.values >= 0.3 * np.nan_to_num(base))
        return rr[keep]
    r84, r59 = clean_r(r84, m84), clean_r(r59, m59)
    end = int(D['m']['ym'].max()); end = min(end, int(D['m'][D['m'].ym <= 209912].ym.max()))
    W = 6 if size(m, S1).ym.isin(months_back(end, 6)).sum() >= 60 else 12   # 거래 적은 곳은 12개월
    L6 = months_back(end, W); L24 = months_back(end, 24); H21 = list(range(202107, 202113))
    today = datetime.date.today()
    title = f"{R['kw']} · 시세, {SA}{(' · ' + SB) if SA != '84㎡' else ''} 단지별 정리 ({today.year}년 {today.month}월 갱신)"
    if key == 'hanam': title = f"{R['kw']} · 시세, 동별 {SA} 비교 ({today.year}년 {today.month}월 갱신)"
    d = os.path.join(OUT, R['slug']); os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith(('.jpg', '.png')): os.remove(os.path.join(d, f))

    s6 = m84[m84.ym.isin(L6)]; s21 = m84[m84.ym.isin(H21)]; j6 = r84[r84.ym.isin(L6)]
    med6, n6 = s6.p.median(), len(s6); med21 = s21.p.median(); jm6, jn6 = j6.p.median(), len(j6)
    chg = (med6 / med21 - 1) * 100 if med21 and n6 else np.nan
    jr = jm6 / med6 * 100 if n6 and jn6 else np.nan
    prev6 = m84[m84.ym.isin(months_back(L6[0] - 1 if L6[0] % 100 != 1 else L6[0] - 89, W))]
    pmed = prev6.p.median(); chg6 = (med6 / pmed - 1) * 100 if len(prev6) and n6 else np.nan

    # 월별 (24개월, 3건 미만은 비움)
    MMIN = 3 if W == 6 else 2
    g = m84[m84.ym.isin(L24)].groupby('ym').p.agg(['median', 'size'])
    mon = [g.loc[x, 'median'] if x in g.index and g.loc[x, 'size'] >= MMIN else np.nan for x in L24]
    mlab = [f"{str(x // 100)[2:]}.{x % 100:02d}" for x in L24]
    monv = np.array(mon, float); okm = ~np.isnan(monv)
    mhi = L24[int(np.nanargmax(monv))]; mlo = L24[int(np.nanargmin(monv))]

    # 단지 표 (84) — 최근 {W}개월 2건 이상
    key_cols = ['dong', 'apt'] if not R['dongs'] or len(R['dongs']) > 1 else ['apt']
    def by_apt(df, L):
        x = df[df.ym.isin(L)].groupby(['dong', 'apt']).p.agg(['median', 'size']); return x
    a6 = by_apt(m84, L6); a21 = by_apt(m84, H21); aj = by_apt(r84, L6)
    yr = m.groupby(['dong', 'apt']).by.agg(lambda s: s.mode().iloc[0] if len(s.mode()) else np.nan)
    rows = []
    nmin = 3 if key == 'hanam' else 2
    for (dg, ap), (md, n) in a6.iterrows():
        if n < nmin: continue
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
    # 01 대표 · 02 숫자 카드 3개 · 03 「1년 전 · 6개월 전 · 지금」 막대 · 04 위 3 · 아래 2 막대 · (구글 블로그) 05 눈에 띄는 점
    V.thumb(fig('t.png', f"{R['name']} 아파트 실거래가 대표 그림"), monv[okm] if okm.sum() >= 6 else None)
    V.cards3(f"{R['name']} {SA} 가운데 값은 {won(med6)}입니다" if n6 else f"{R['name']} {SA} 최근 거래가 없습니다",
             [(f'{SA} 매매 · 최근 {W}개월', V.eok(med6, 1) if n6 else '-', f'{n6}건'),
              ('2021년 하반기 대비', pct(chg), f'{V.eok(med21, 1)} → {V.eok(med6, 1)}' if n6 and med21 == med21 else ''),
              ('전세가율', pct(jr, False), f'새 전세 {V.eok(jm6, 1)} · {jn6}건' if jn6 else '새 전세 계약 없음')],
             fig('c.png', f"{R['name']} 아파트 {SA} 실거래 요약 숫자"), note=f'국토교통부 실거래 · {_span(L6)} 계약 · 가운데 값')
    # 기간 막대: W=6 → 1년 전 · 6개월 전 · 지금 / W=12 → 1년 전 · 지금. 맨 앞에 2021년 하반기. 3건 미만 기간은 뺀다.
    PREVW = months_back(L6[0] - 1 if L6[0] % 100 != 1 else L6[0] - 89, W)
    wins = [('2021년 하반기', H21)]
    if W == 6: wins += [('1년 전', months_back(PREVW[0] - 1 if PREVW[0] % 100 != 1 else PREVW[0] - 89, W)), ('6개월 전', PREVW)]
    else: wins += [('1년 전', PREVW)]
    wins += [('지금', L6)]
    TB = []
    for nm_, L_ in wins:
        x_ = m84[m84.ym.isin(L_)]
        if len(x_) >= 3: TB.append((nm_, float(x_.p.median()), len(x_), L_))
    yago = next((t_ for t_ in TB if t_[0] == '1년 전'), None)
    if yago and n6:
        dy = med6 - yago[1]
        thead = (f"{R['name']} {SA}, 1년 새 {won(abs(dy))} {'올랐습니다' if dy > 0 else '내렸습니다'}" if abs(dy) >= 100 else f"{R['name']} {SA}, 1년 전과 같은 {won(med6)}입니다")
    else:
        dy = None; thead = f"{R['name']} {SA} 가운데 값은 {won(med6)}입니다"
    def _sp(L_): return f"{str(L_[0] // 100)[2:]}.{L_[0] % 100}~{str(L_[-1] // 100)[2:]}.{L_[-1] % 100}월"
    V.bars(thead, [t_[0] for t_ in TB], [t_[1] for t_ in TB], len(TB) - 1, fig('r.png', f"{R['name']} {SA} 실거래 가운데 값 · 1년 전과 지금"),
           fmt=lambda v: V.eok(v, 1), subs=[f'{_sp(t_[3])} · {t_[2]}건' for t_ in TB], note=f'국토교통부 실거래 · {SA} 매매 가운데 값')
    if key == 'hanam':
        G = m84.assign(grp=m84.dong.map(GROUP)).dropna(subset=['grp'])
        gg = G[G.ym.isin(L6)].groupby('grp').p.agg(['median', 'size']).sort_values('median', ascending=False)
        five = gg if len(gg) <= 5 else pd.concat([gg.head(3), gg.tail(2)])
        g0_, g1_ = gg.index[0], gg.index[-1]
        V.bars(f"{g0_}{josa(g0_, '이', '가')} {g1_}보다 {won(gg['median'].iloc[0] - gg['median'].iloc[-1])} 비쌉니다",
               list(five.index), five['median'].values, 0, fig('i.png', f'하남 동별 {SA} 실거래 중앙값'),
               fmt=lambda v: V.eok(v, 1), subs=[f'{int(n)}건' for n in five['size']],
               note=f'하남 {SA} 매매 가운데 값 · 최근 {W}개월' + (f' · {len(gg)}곳 중 위 3곳 · 아래 2곳' if len(gg) > 5 else ''))
    elif len(T):
        five = T if len(T) <= 5 else pd.concat([T.head(3), T.tail(2)])
        V.bars(f"{R['name']} {SA}, 단지에 따라 {won(T.med.iloc[0] - T.med.iloc[-1])} 차이 납니다" if len(T) > 1 else f"{T.apt.iloc[0]} {SA} {won(T.med.iloc[0])}",
               list(five.apt), five.med.values, 0, fig('i.png', f"{R['name']} 단지별 {SA} 실거래 중앙값"),
               fmt=lambda v: V.eok(v, 1), subs=[f'{int(n)}건' for n in five.n],
               note=f"{R['name']} {SA} 매매 가운데 값 · 최근 {W}개월" + (f' · {len(T)}개 단지 중 위 3곳 · 아래 2곳' if len(T) > 5 else ''))
    INS = []
    if gblog:
        INS = insights(key, m84, r84, end, W, L6, PREVW, H21, SA, T)
        fi = next((z for z in INS if z['fig']), None)
        if fi:
            f_ = fi['fig']; px = fig('x.png', f"{R['name']} {f_['title']}")
            if f_['type'] == 'bars': V.bars(fi['title'], f_['names'], f_['values'], f_['hi'], px, fmt=f_['fmt'], subs=f_.get('subs'), note=f_['note'])
            else: V.cards3(fi['title'], f_['cards'], px, hi=0, note=f_['note'])
    n_base = len(imgs) - (1 if gblog and INS and any(z['fig'] for z in INS) else 0)
    # 번호 붙이기: 01 = 대표, 이후 본문 순서 (눈에 띄는 점 그림은 마지막 번호)
    from PIL import Image
    files = []
    for i, (p, alt) in enumerate(imgs, 1):
        j = os.path.join(d, f'{i:02d}.jpg'); Image.open(p).convert('RGB').save(j, quality=93); os.remove(p); files.append((j, alt))

    # ------------------------------------------------------------ 본문
    nm = R['name']; B = []
    B.append(f'<p style="font-size:14px;color:#6B7A90;margin:0 0 6px">갱신 {today.year}.{today.month:02d}.{today.day:02d} · 자료 {ymlab(L6[0])} ~ {ymlab(end)} 계약분 · 국토교통부 실거래</p>')
    B.append(P(f'{nm} 아파트 {SA}{SAP} 실거래가를 단지별로 모았습니다. 숫자는 매달 새로 바꿉니다.'))
    B.append(P(f'최근 {W}개월 {nm} {SA} 매매는 {n6}건입니다. 가운데 값은 <b>{won(med6)}</b>입니다.'
               + (f' 바로 앞 {W}개월은 {won(pmed)}이었습니다({pct(chg6)}).' if chg6 == chg6 else '')))
    B.append(IMG(2, files[1][1]))
    B.append(H2(f'{nm} 아파트 실거래가 · 월별 흐름'))
    B.append(IMG(3, files[2][1]))
    B.append(P(' '.join(f'{t_[0]}({_span(t_[3])}) 가운데 값은 {won(t_[1])}입니다.' if t_[0] != '지금' else f'최근 {W}개월은 {won(t_[1])}입니다.' for t_ in TB)
               + (f' 1년 전보다 {won(abs(dy))} {"높습니다" if dy > 0 else "낮습니다"}.' if dy is not None and abs(dy) >= 100 else '')))
    B.append(P(f'24개월 동안 한 달 가운데 값이 가장 높았던 때는 {ymlab(mhi)}({won(g.loc[mhi, "median"])})입니다. '
               f'가장 낮았던 때는 {ymlab(mlo)}({won(g.loc[mlo, "median"])})입니다.'))
    lastok = [x for x in L24 if x in g.index and g.loc[x, 'size'] >= MMIN][-1]
    B.append(P(f'가장 최근 달인 {ymlab(lastok)}은 {int(g.loc[lastok, "size"])}건, {won(g.loc[lastok, "median"])}입니다.'
               + (f' {ymlab(end)} 계약은 신고 기한(30일)이 남아 건수가 더 늘 수 있습니다.' if end == L24[-1] else '')))
    if key == 'hanam':
        B.append(H2(f'하남 아파트 시세 · 동별 {SA} 비교'))
        B.append(IMG(4, files[3][1]))
        G6 = m84.assign(grp=m84.dong.map(GROUP))
        rowsG = []
        for gname in gg.index:
            x6 = G6[(G6.grp == gname) & G6.ym.isin(L6)]; x21 = G6[(G6.grp == gname) & G6.ym.isin(H21)]
            rj = r84.assign(grp=r84.dong.map(GROUP)); xj = rj[(rj.grp == gname) & rj.ym.isin(L6)]
            c = (x6.p.median() / x21.p.median() - 1) * 100 if len(x21) else np.nan
            rowsG.append([gname, won(x6.p.median()), f'{len(x6)}건', pct(c), won(xj.p.median()) if len(xj) else '-',
                          pct(xj.p.median() / x6.p.median() * 100, False) if len(xj) else '-'])
        B.append(table(['동', f'{SA} 매매 중앙값', '건수', '2021 하반기 대비', '새 전세 중앙값', '전세가율'], rowsG))
        g0, g1 = gg.index[0], gg.index[-1]
        B.append(P(f'최근 {W}개월 가운데 값은 {g0}{josa(g0, '이', '가')} {won(gg.loc[g0, "median"])}으로 가장 높습니다. {g1}{josa(g1, '은', '는')} {won(gg.loc[g1, "median"])}입니다. '
                   f'두 곳 차이는 {won(gg.loc[g0, "median"] - gg.loc[g1, "median"])}입니다.'))
    B.append(H2(f'{nm} 아파트 {SA} 단지별 시세표'))
    B.append(P(f'최근 {W}개월({ymlab(L6[0])} ~ {ymlab(L6[-1])}) {SA} 매매가 {nmin}건 이상인 단지만 넣었습니다. 비싼 순서입니다.'))
    if len(T):
        show_dong = (R['dongs'] is None) or len(R['dongs']) > 1
        head = ['단지'] + (['동'] if show_dong else []) + ['입주', f'{SA} 매매 중앙값', '건수', '2021 하반기 대비', '새 전세 중앙값', '전세가율']
        rr = []
        for _, x in T.iterrows():
            rr.append([x.apt] + ([x.dong] if show_dong else []) + [f'{int(x.yr)}' if x.yr == x.yr else '-', won(x.med), f'{x.n}건',
                       pct(x.c21), won(x.j) if x.jn else '-', pct(x.jr, False) if x.jn else '-'])
        B.append(table(head, rr))
        t0, t1 = T.iloc[0], T.iloc[-1]
        B.append(P(f'가장 높은 단지는 {t0.apt}({won(t0.med)})입니다. 표의 마지막은 {t1.apt}({won(t1.med)})입니다. '
                   f'두 단지 차이는 {won(t0.med - t1.med)}입니다.'))
        busy = T.sort_values('n', ascending=False).iloc[0]
        B.append(P(f'거래가 가장 많았던 단지는 {busy.apt}{josa(busy.apt, '으로', '로')} {busy.n}건입니다.'))
        if key != 'hanam':
            B.append(IMG(4, files[3][1]))
            if len(T) > 5: B.append(P(f'그림에는 값이 높은 3개 단지와 낮은 2개 단지만 넣었습니다. 나머지는 위 표에 있습니다.'))
    B.append(H2(f'{nm} 아파트 {SB} 시세표'))
    if len(T59):
        B.append(P(f'{SB}{SBP}는 최근 {W}개월 {n59}건, 가운데 값 {won(med59)}입니다.'))
        B.append(table(['단지', f'{SB} 매매 중앙값', '건수', '새 전세 중앙값'],
                       [[x.apt, won(x.med), f'{x.n}건', won(x.j) if x.jn else '-'] for _, x in T59.iterrows()]))
    else:
        B.append(P(f'최근 {W}개월 {SB} 매매가 2건 이상인 단지가 없습니다. 전체 {n59}건입니다.'))
    B.append(H2('이 표 읽는 법'))
    B.append(P('<b>중앙값</b>은 거래를 값 순서로 줄 세웠을 때 한가운데 값입니다. 한두 건 튀는 거래에 덜 흔들립니다.'))
    B.append(P('<b>건수</b>가 2~3건이면 층 · 향에 따라 숫자가 크게 움직입니다. 건수를 같이 보세요.'))
    B.append(P(f'<b>2021 하반기 대비</b>는 2021년 7~12월 같은 단지 {SA} 가운데 값과 비교한 것입니다. 그때 거래가 2건 미만이면 비워 뒀습니다.'))
    B.append(P('<b>새 전세</b>는 새로 들어온 세입자 계약만 셉니다. 기존 세입자의 갱신 계약은 뺐습니다. 전세가율은 새 전세 ÷ 매매 가운데 값입니다.'))
    B.append(H2(f'{nm} 아파트 실거래가 · 자주 묻는 질문'))
    B.append(H3(f'{nm} {SA} 지금 얼마에 거래되나요?'))
    B.append(P(f'최근 {W}개월 {n6}건의 가운데 값은 {won(med6)}입니다.' + (f' 단지별로는 {won(T.med.min())} ~ {won(T.med.max())}입니다.' if len(T) else '')))
    B.append(H3('2021년 하반기보다 올랐나요?'))
    if chg == chg:
        B.append(P(f'2021년 7~12월 {nm} {SA} 가운데 값은 {won(med21)}이었습니다. 지금은 {won(med6)}입니다. '
                   + (f'{abs(chg):.1f}% 높습니다.' if chg >= 0 else f'{abs(chg):.1f}% 낮습니다. 아직 그때 값에 못 미칩니다.')))
        if len(T) and T.c21.notna().sum():
            n_up = int((T.c21 >= 0).sum()); tot = int(T.c21.notna().sum())
            B.append(P(f'비교할 수 있는 {tot}개 단지 중 {n_up}개가 그때 값 이상입니다.'))
    else:
        B.append(P(f'2021년 하반기 {SA} 거래가 적어 비교하지 않았습니다.'))
    B.append(H3(f'{nm} {SA} 전세는 얼마인가요?'))
    B.append(P(f'최근 {W}개월 새 세입자 전세 {jn6}건의 가운데 값은 {won(jm6)}입니다. 매매 가운데 값의 {pct(jr, False)}입니다.' if jn6 else f'최근 {W}개월 새 전세 계약이 없습니다.'))
    B.append(H3(f'{nm} {SB}는 얼마인가요?'))
    B.append(P(f'최근 {W}개월 {SB} {n59}건, 가운데 값은 {won(med59)}입니다. {SA}와 차이는 {won(med6 - med59)}입니다.' if n59 and n6 else f'최근 {W}개월 {SB} 거래가 적습니다.'))
    B.append(NOTE('<b>NOTE</b><br>'
                  f'· 출처: 국토교통부 아파트 매매 · 전월세 실거래가 공개 자료. {ymlab(end)} 계약분까지 반영했습니다.<br>'
                  f'· 지역: {H.escape(R["define"])}<br>'
                  '· 뺀 거래: 계약이 취소된 거래(해제), 중개사 없이 한 직거래.<br>'
                  f'· {SA} = 전용면적 {S1[1]}~{S1[2]}㎡, {SB} = 전용면적 {S2[1]}~{S2[2]}㎡. 값은 모두 중앙값입니다.<br>'
                  '· 전세: 신규 계약만. 갱신 계약 · 월세는 넣지 않았습니다. 같은 단지 매매 가운데 값의 30%가 안 되는 보증금(임대 단지 등)도 뺐습니다. 전세 자료는 2026년 1월 계약분부터 씁니다.<br>'
                  + (f'· 이 지역은 거래가 적어 최근 12개월로 셉니다. 전세는 2026년 1월 이후만 들어갑니다.<br>' if W == 12 else '')
                  + f'· 단지 표는 최근 {W}개월 {nmin}건 이상인 단지만 넣었습니다({SB} 표는 2건 이상). 단지 이름은 국토교통부 표기 그대로입니다.'))
    body = '\n'.join(B)
    tags = [R['kw'], f"{R['name']} 아파트 시세", f"{R['name']} 아파트 매매", f"{R['name']} 아파트 전세", '하남 아파트 실거래가', f'{SA} 시세']
    tags = list(dict.fromkeys(tags))[:6]

    def fill(b, srcmap):
        for i in range(2, len(files) + 1): b = b.replace('{IMG%02d}' % i, srcmap[i])
        return b
    def render(srcmap):
        b = fill(body, srcmap)
        return (f'<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8"><title>{H.escape(title)}</title>'
                f'<meta name="description" content="{H.escape(strip(B[1])[:150])}"></head>\n<body style="max-width:1000px;margin:0 auto;font-family:sans-serif">\n'
                f'<!-- 제목: {H.escape(title)} -->\n<!-- 태그: {", ".join(tags)} -->\n<!-- 대표 이미지: 01.jpg -->\n{b}\n</body></html>\n')
    local = {i: f'{i:02d}.jpg' for i in range(1, len(files) + 1)}
    open(os.path.join(d, 'local.html'), 'w').write(render(local))
    urls = local
    if up or gblog:
        sys.path.insert(0, '/home/claude/helper'); from gas import call
        urls = {}
        stamp = today.strftime('%Y%m')
        for i, (p, _) in enumerate(files, 1):
            res = call('image', name=f"ts_{R['slug']}_{stamp}_{i:02d}.jpg", b64=base64.b64encode(open(p, 'rb').read()).decode())
            urls[i] = res['url']
    html_out = render(urls)
    open(os.path.join(d, 'index.html'), 'w').write(html_out)
    gmeta = None
    if gblog:
        G = B[:3]
        if INS:
            G.append(H2(f'{nm} 아파트 실거래가 · 이번 달 눈에 띄는 점 {len(INS)}가지'))
            shown = False
            for no, z in zip('①②③④', INS):
                G.append(H3(f'{no} {z["title"]}'))
                ss = re.split(r'(?<=[다\)]\.) ', z['body'])          # 한 문단 = 한 문장(숫자 한 짝). 세는 방법 문장은 맨 뒤로.
                if len(ss) > 1 and ss[0].endswith(('비교했습니다.', '기준입니다.', '세웠습니다.', '세었습니다.')): ss = ss[1:] + [ss[0]]
                for t_ in ss[:1]: G.append(P(t_))
                if z['fig'] and not shown: G.append(IMG(len(files), files[-1][1])); shown = True
                for t_ in ss[1:]: G.append(P(t_))
            G.append(P(f'{"동 묶음은 거래 10건 이상" if key == "hanam" else "단지는 매매 5건 이상"}인 곳만 비교했습니다. 건수가 적은 곳은 층 · 향에 따라 가운데 값이 움직입니다.'))
        G += B[3:]
        lk = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gblog_links.json'))).get(key, [])
        if lk:
            G.append(H2(f'{nm} · 이 동네 분석 글'))
            G.append(P('낭만 부동산 분석 플랫폼이 네이버 블로그에 쓴 글입니다.'))
            G.append('<ul style="font-size:17px;line-height:2;color:#22324A;padding-left:20px">' + ''.join(
                f'<li><a href="https://blog.naver.com/dong_jin_kim/{no}">{H.escape(t)}</a></li>' for no, t in lk) + '</ul>')
        gb = fill('\n'.join(G), urls)
        open(os.path.join(d, 'gblog.html'), 'w').write(gb)
        gt = strip(gb)
        gmeta = dict(file=os.path.join(d, 'gblog.html'), chars=len(gt.replace(' ', '')), links=len(lk),
                     insights=[dict(kind=z['kind'], score=round(float(z['score']), 2), title=z['title'], body=z['body']) for z in INS],
                     ban=[w for w in ['고요', '갈렸', '갈랐', '갈라', '가른', '최고', '분양', '매물', '인테리어', '010-'] if w in gt])
    text = strip(body)
    ban = [w for w in ['고요', '갈렸', '갈랐', '갈라', '최고', '분양', '매물', '인테리어', '010-'] if w in text]
    meta = dict(key=key, slug=R['slug'], title=title, tags=tags, chars=len(text.replace(' ', '')), chars_sp=len(text),
                images=n_base, drive=f"{DRIVE}/{R['slug']}" if up else None, ban=ban, gblog=gmeta,
                core=dict(end=end, med84_6m=med6, n84_6m=n6, med84_2021h2=med21, chg_vs_2021h2=round(chg, 1) if chg == chg else None,
                          prev6=pmed, jeonse_new=jm6, jeonse_n=jn6, jeonse_ratio=round(jr, 1) if jr == jr else None,
                          med59_6m=med59, n59=n59, apts=len(T),
                          top=(T.iloc[0].apt, T.iloc[0].med) if len(T) else None))
    json.dump(meta, open(os.path.join(d, 'meta.json'), 'w'), ensure_ascii=False, indent=1, default=float)
    if up:
        for p in [os.path.join(d, 'index.html')] + [f for f, _ in files[:n_base]]:
            mime = 'text/html' if p.endswith('.html') else 'image/jpeg'
            call('fput', path=f"{DRIVE}/{R['slug']}", name=os.path.basename(p), mime=mime,
                 b64=base64.b64encode(open(p, 'rb').read()).decode())
    return meta

def strip(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = H.unescape(s); return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]; up = '--up' in sys.argv; gb = '--gblog' in sys.argv
    keys = list(REG) if not a or a[0] == 'all' else a
    for k in keys:
        mt = build(k, up, gb)
        print(json.dumps({x: mt[x] for x in ['key', 'title', 'chars', 'images', 'drive', 'ban']}, ensure_ascii=False))
        if gb and mt.get('gblog'): print(json.dumps({'gblog': {x: mt['gblog'][x] for x in ['file', 'chars', 'links', 'ban']}, 'insights': [z['title'] for z in mt['gblog']['insights']]}, ensure_ascii=False))

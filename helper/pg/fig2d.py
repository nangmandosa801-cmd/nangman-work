#!/usr/bin/env python3
"""낭만 부동산(네이버 dong_jin_kim) 그래프 공통 함수 (11/10 기준) — 2D · 3초 안에 읽히는 그림.
그리는 일은 /home/claude/tools/tistory/viz2d.py 가 한다(티스토리 · 구글 블로그와 같은 모양).
규칙: 흰 바탕 · 그라데이션/그림자/입체 없음 · 먹색 #191F28 + 회색 #6B7684 + 강조 1색 #3182F6 · Pretendard.
  막대는 5개까지, 막대 위에 숫자를 굵게, 강조 막대 1개만 파랑(나머지 #D1D6DB).
  그림 맨 위에 결론 한 줄을 크게. 5개를 넘는 비교는 표(본문)나 cards3(숫자 카드 3개).
쓰기:
  from fig2d import bars, cards3        (sys.path 에 /home/claude/helper/pg 추가)
  bars('img/x_v2.png', '84㎡ 1년 새 2억 3천 올랐습니다',
       [('2025년', 11.8, '11억 8천', False), ('2026년', 14.1, '14억 1천', True)], note='감일동 84㎡ 매매 중앙값')
       items = (이름, 값(0 이상), 막대 위 글자, 강조?) 5개까지 · 이름 뒤에 '|작은 설명' 을 붙이면 이름 아래 회색 줄
  cards3('img/y_v2.png', '결론 한 줄', [('144.2', '강남구 84㎡', True), ('4곳', '못 넘긴 구', False), ('5.0배', '강남 · 도봉 차이', False)])
       cards = (큰 숫자, 이름, 강조?[, 아래 작은 설명]) 3개까지
폭 1200px. sub 는 예전 인자(그림 아래 작은 줄로 note 앞에 붙는다).
"""
import sys
sys.path.insert(0, '/home/claude/tools/tistory')
import viz2d as _v

INK, SUB, ACC, BAR = _v.INK, _v.SUB, _v.ACC, _v.GRAY


def _nt(sub, note):
    t = ' · '.join(x for x in (sub, note) if x)
    return t or None


def bars(out, headline, items, sub=None, note=None):
    if len(items) > 5: raise ValueError('막대는 5개까지')
    if sum(1 for i in items if i[3]) > 1: raise ValueError('강조 막대는 1개만')
    names = [str(i[0]).split('|')[0] for i in items]
    subs = [(str(i[0]).split('|') + [''])[1] for i in items]
    vals = [float(i[1]) + k * 1e-9 for k, i in enumerate(items)]      # 같은 값이어도 글자를 따로 찾게
    txt = {v: str(i[2]) for v, i in zip(vals, items)}
    hi = next((k for k, i in enumerate(items) if i[3]), None)
    return _v.bars(headline, names, vals, hi, out, fmt=lambda v: txt.get(v, f'{v:,.0f}'),
                   subs=subs if any(subs) else None, note=_nt(sub, note))


def cards3(out, headline, cards, sub=None, note=None):
    if len(cards) > 3: raise ValueError('숫자 카드는 3개까지')
    if sum(1 for c in cards if c[2]) > 1: raise ValueError('강조 카드는 1개만')
    cs = [(str(c[1]).replace('\n', ' '), str(c[0]), c[3] if len(c) > 3 else '') for c in cards]
    hi = next((k for k, c in enumerate(cards) if c[2]), None)
    return _v.cards3(headline, cs, out, hi=hi, note=_nt(sub, note))


if __name__ == '__main__':
    bars('/tmp/fig2d_bars.png', '84㎡ 1년 새 2억 3천 올랐습니다',
         [('2024년', 11.2, '11억 2천', False), ('2025년', 11.8, '11억 8천', False), ('2026년', 14.1, '14억 1천', True)],
         note='감일동 84㎡ 매매 중앙값 · 국토교통부 실거래')
    cards3('/tmp/fig2d_cards.png', '2021년 고점 넘긴 구 21곳, 못 넘긴 구 4곳',
           [('144.2', '강남구 84㎡', True, '2021년 = 100'), ('4곳', '2021년 고점 못 넘긴 구', False), ('5.0배', '강남 · 도봉 84㎡ 차이', False)],
           note='서울 25개 구 · 84㎡ 매매 중앙값')
    print('ok')

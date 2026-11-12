# 「같이 보면 좋은 글」 규칙 (11/12 사용자): 글 맨 끝 블록 하나 · 링크 딱 3개(11/12 18:17 사용자 「앞으로 링크는 딱 세개만」) · 「▶ 제목」 한 줄씩 · 줄 사이 빈 줄 · 번호 · 표 · 카드 금지
import re
def short(t, n=30):
    t = re.sub(r'\s+', ' ', t).strip()
    head = t.split(',')[0].strip()
    if len(head) <= n: return head
    cut = head[:n]; sp = cut.rfind(' ')
    return cut[:sp] if sp > 10 else cut
def pick(items, lo=3, hi=3):
    items = [x for x in items if x]
    if len(items) < lo: raise SystemExit(f'같이 보면 좋은 글 {len(items)}개 — 3개 이상 필요(같은 단지 · 지역 · 주제)')
    items = items[:hi]
    if any('champion_chart' in str(x) or 'nangmaninterior' in str(x) for x in items): raise SystemExit('낭만 인테리어로 가는 링크 금지')
    return items
def txt_block(items):
    return '[같이 보면 좋은 글]\n' + '\n'.join(f'▶ {short(t)} | {u}' for t, u in pick(items))

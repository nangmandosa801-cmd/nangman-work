# 「같이 보면 좋은 글」 규칙 (11/12 사용자): 글 맨 끝 블록 하나 · 링크 3~5개 · 「▶ 제목」 한 줄씩 · 줄 사이 빈 줄 · 번호 · 표 · 카드 금지
import re
def short(t, n=30):
    t = re.sub(r'\s+', ' ', t).strip()
    head = t.split(',')[0].strip()
    if len(head) <= n: return head
    cut = head[:n]; sp = cut.rfind(' ')
    return cut[:sp] if sp > 10 else cut
def pick(items, lo=3, hi=5):
    items = [x for x in items if x]
    if len(items) < lo: raise SystemExit(f'같이 보면 좋은 글 {len(items)}개 — 3개 이상 필요(같은 단지 · 지역 · 주제)')
    return items[:hi]
def txt_block(items):
    return '[같이 보면 좋은 글]\n' + '\n'.join(f'▶ {short(t)} | {u}' for t, u in pick(items))

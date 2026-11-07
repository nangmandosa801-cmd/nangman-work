#!/usr/bin/env python3
"""제휴 업체 글 → 인테리어툰 이야깃거리 카드 (11/7 사용자 「제휴 업체 블로그 스토리를 모아 두면 ChatGPT가 만화로」)
사용: python3 cards.py [--up] [--max N]
  pool.json(crawl.py 결과) 중 아직 카드가 없는 글만 gpt-4o-mini(블로그 우체통 gpt)로 카드화.
  카드: 주제(왜지금 · 꼼꼼함 · 가격 · 서비스) · 손님 상황 · 원인 · 한 일 · 꼼꼼한 장면 · 가격(원글에 있을 때만) · 계절 · 만화 재해석 장면
  + 이어 줄 낭만 인테리어 네이버 글(제목 낱말 겹침으로 고름 · 없으면 「새 글 필요」)
결과: /home/claude/w/partners/cards.json · cards.md  --up 이면 드라이브 「블로그/협업/인테리어툰/재료」에 올림
"""
import sys, os, json, re, urllib.request, urllib.parse
sys.path.insert(0, '/home/claude/helper'); from gas import call
POOL = '/home/claude/w/partners/pool.json'; OUT = '/home/claude/w/partners/cards.json'; MD = '/home/claude/w/partners/cards.md'
SKIP = ('후기 이벤트', '휴무', '공지', '채용', '모집')
SYS = """너는 인테리어 시공 블로그 글을 읽고 만화 재료 카드를 만든다. 글에 있는 사실만 쓴다. 없는 숫자 · 가격 · 효과는 만들지 않는다.
업체 이름(상호) · 전화번호 · 블로그 주소는 절대 쓰지 않는다(업체는 「제휴 ○○팀」으로). price에는 시공 금액만 쓰고 혜택 · 할인 · 사은품 · 「○만원 상당」은 쓰지 않는다.
JSON 하나로 답한다:
{"usable": true/false(시공 · 수리 이야기가 아니면 false),
 "pillar": "왜지금"(지금 안 고치면 커지는 문제 · 계절 · 입주 시기) | "꼼꼼함"(팀의 작업 방식이 핵심) | "가격"(금액 · 범위 이야기가 있음) | "서비스"(견적 비교 · 일정 · 손님 응대) 중 이 글에 가장 맞는 하나. 꼼꼼함만 고르지 말고 글의 중심으로 고른다,
 "trade": "중문" | "설비" | "줄눈" | "청소" | "코킹" | "단열 · 곰팡이" | "사전점검" | "기타",
 "place": "지역 · 단지 · 공간(글에 있는 대로, 없으면 빈칸)",
 "problem": "손님이 겪던 일 한두 문장(장면처럼)",
 "cause": "원인(글에 있을 때만)",
 "work": ["팀이 한 일 순서대로 3~6개, 짧게"],
 "careful": "이 팀이 꼼꼼했던 구체적 장면 한 문장(글에 있는 것)",
 "price": "글에 적힌 금액만, 없으면 빈칸",
 "season": "겨울 · 입주철 등 시기 연결(없으면 빈칸)",
 "comic": "만화로 재해석할 장면 아이디어 2문장(인물 · 상황 · 반전, 사실은 글 그대로)",
 "keywords": ["검색어가 될 말 3~5개"]}"""
def naver_titles():
    try:
        s = urllib.request.urlopen(urllib.request.Request('https://rss.blog.naver.com/champion_chart.xml', headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read().decode('utf8', 'ignore')
        rss = {l.split('?')[0].rsplit('/', 1)[-1]: t for t, l in re.findall(r'<item>.*?<title><!\[CDATA\[(.*?)\]\]></title>.*?<link><!\[CDATA\[(.*?)\]\]>', s, re.S)}
    except Exception: rss = {}
    t = json.load(open('/home/claude/w/ts_expand/naver_titles.json')); t.update(rss); return t
def toks(s): return set(w for w in re.findall(r'[가-힣A-Za-z0-9]{2,}', s))
def match(card, titles):
    q = toks(' '.join(card.get('keywords', [])) + ' ' + card.get('trade', '')); pl = toks(card.get('place', ''))
    best = sorted(((len(q & toks(v)) + 3 * len(pl & toks(v)), k, v) for k, v in titles.items()), reverse=True)[:2]
    return [{'logNo': k, 'title': v, 'url': f'https://blog.naver.com/champion_chart/{k}'} for sc, k, v in best if sc >= 2]
def main():
    import time
    for _ in range(10):
        try: pool = json.load(open(POOL)); break
        except Exception: time.sleep(3)
    cards = json.load(open(OUT)) if os.path.exists(OUT) else {}
    mx = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 9999
    titles = naver_titles(); n = 0
    from itertools import zip_longest
    byb = {}
    for k, x in pool.items(): byb.setdefault(x['blog'], []).append((k, x))
    order = [kx for grp in zip_longest(*byb.values()) for kx in grp if kx]   # 업체를 돌아가며
    for k, x in order:
        if k in cards or n >= mx: continue
        if any(w in x['title'] for w in SKIP) or len(x.get('text', '')) < 300: cards[k] = {'usable': False, 'title': x['title']}; continue
        try: r = call('gpt', system=SYS, user=f"제목: {x['title']}\n종목: {x['kind']}\n본문:\n{x['text'][:3800]}")
        except Exception as e: print(k, 'gpt_err', str(e)[:80]); continue
        try: c = r if isinstance(r, dict) else json.loads(r)
        except Exception: print(k, 'bad_json'); continue
        NAMES = r'드림하우스|메가줄눈|펠리체|플로우홈케어|플로우|스페셜코킹|패브릭클리닝|패브릭|단디홈케어|단디|문수리'
        for f in ('problem', 'cause', 'careful', 'comic'): c[f] = re.sub(NAMES, '제휴팀', str(c.get(f, '')))
        c['work'] = [re.sub(NAMES, '제휴팀', w) for w in c.get('work', [])]
        if re.search('상당|혜택|할인|사은', c.get('price', '')): c['price'] = ''
        c.update({'src': k, 'partner': x['abbr'], 'title': x['title'], 'date': x['date'], 'imgs': len(x.get('imgs', []))})
        if c.get('usable'): c['naver'] = match(c, titles); c['naver_need'] = not c['naver']
        cards[k] = c; n += 1
        json.dump(cards, open(OUT, 'w'), ensure_ascii=False, indent=0)
    ok = [c for c in cards.values() if c.get('usable')]
    L = ['# 인테리어툰 이야깃거리 카드', f'카드 {len(ok)}장 · 원글 {len(cards)}편', '']
    for i, c in enumerate(sorted(ok, key=lambda c: (c['pillar'], c['trade'])), 1):
        L += [f"## C{i:03d} [{c['pillar']} · {c['trade']}] {c.get('place','')}", f"- 원글: {c['partner']} · {c['title']} ({c['src']} · {c['date']} · 사진 {c['imgs']}장)",
              f"- 상황: {c.get('problem','')}", f"- 원인: {c.get('cause','')}", '- 한 일: ' + ' → '.join(c.get('work', [])),
              f"- 꼼꼼한 장면: {c.get('careful','')}", f"- 가격: {c.get('price','') or '원글에 없음'}", f"- 시기: {c.get('season','')}",
              f"- 만화 아이디어: {c.get('comic','')}",
              '- 이어 줄 네이버 글: ' + (' / '.join(f"{n['title']} {n['url']}" for n in c.get('naver', [])) or '새 글 필요'), '']
    open(MD, 'w').write('\n'.join(L))
    res = {'new': n, 'cards': len(ok), 'need_naver': sum(1 for c in ok if c.get('naver_need'))}
    if '--up' in sys.argv:
        for f in (OUT, MD): call('fput', path='블로그/협업/인테리어툰/재료', name=os.path.basename(f).replace('cards', '이야깃거리_카드'), text=open(f).read())
        res['up'] = True
    print(json.dumps(res, ensure_ascii=False))
if __name__ == '__main__': main()

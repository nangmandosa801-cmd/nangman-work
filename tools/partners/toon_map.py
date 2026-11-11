#!/usr/bin/env python3
"""인테리어툰 ↔ 네이버 글 매핑 장부 (11/7 사용자 「만화와 블로그를 매핑 · 인스타 → 네이버 한 방향 · 네가 관리」)
원칙: 네이버 글에는 인스타 링크를 넣지 않는다. 인스타 · 스레드에서 네이버로만 보낸다.
  인스타 캡션: 링크 대신 「네이버에서 ○○○ 검색」(검색 유입도 늘어남) · 스레드: 첫 댓글에 네이버 주소.
사용:
  python3 toon_map.py scan              드라이브 「블로그/협업/인테리어툰/발행대기 · 발행완료」 회차 폴더 → 장부에 줄 추가(memo.txt 읽음)
  python3 toon_map.py pub IT001 <인스타job> [스레드job] [YYYY-MM-DD]   발행 · 예약 기록
  python3 toon_map.py link              champion_chart 새 글 중 「새 글 필요」 회차와 맞는 글을 찾아 이어 줌(naver_new)
  python3 toon_map.py need              네이버 새 글이 필요한 회차 · 카드 목록(블로그 글감으로)
  python3 toon_map.py up                장부를 드라이브 「블로그/장부/인테리어툰_매핑.json · .md」로
장부: /home/claude/w/partners/toon_map.json  (회차 → card · src · 검색어 · naver(지금 이어 준 글) · naver_need · naver_new · insta · threads · date)
"""
import sys, os, json, re
sys.path.insert(0, '/home/claude/helper'); sys.path.insert(0, '/home/claude/tools/partners')
from gas import call
MAP = '/home/claude/w/partners/toon_map.json'; CARDS = '/home/claude/w/partners/cards.json'
WEB = '/home/claude/w/partners/web_stories.json'
def load(p, d):
    try: return json.load(open(p))
    except Exception: return d
def save(m): json.dump(m, open(MAP, 'w'), ensure_ascii=False, indent=1)
def ls(path):
    try: r = call('ls', path=path)
    except Exception: return []
    return r if isinstance(r, list) else r.get('files', [])
def scan(m):
    cards = load(CARDS, {}); add = []
    for st in ('발행대기', '발행완료'):
        for f in ls(f'블로그/협업/인테리어툰/{st}'):
            name = f.get('name', ''); ep = name.split('_')[0]
            if not re.match(r'IT\d{3}$', ep): continue
            row = m.get(ep, {'ep': ep}); row.update({'folder': name, 'state': st})
            if 'src' not in row:
                try: memo = call('fget', path=f'블로그/협업/인테리어툰/{st}/{name}', name='memo.txt')
                except Exception: memo = ''
                memo = memo if isinstance(memo, str) else memo.get('text', '')
                src = re.search(r'[a-z0-9_-]+/\d{9,}', memo); cid = re.search(r'C\d{3}', memo)
                kw = re.search(r'검색어\s*[:：]\s*(.+)', memo); wid = re.search(r'\bW\d{2}\b', memo)
                row.update({'card': cid.group(0) if cid else '', 'src': src.group(0) if src else '', 'search': kw.group(1).strip() if kw else ''})
                c = cards.get(row['src'], {})
                if wid:  # 11/11 인터넷 소재(web_stories.json W01~) — 네이버 글이 아직 없어도 검색어로 추적, 나중에 link 가 이어 줌
                    w = load(WEB, {}).get(wid.group(0), {}); row['web'] = wid.group(0)
                    c = {'naver': w.get('naver', []), 'naver_need': w.get('naver_need', True)}
                    if not row['search']: row['search'] = (w.get('keywords') or [''])[0]
                row['naver'] = c.get('naver', []); row['naver_need'] = bool(c.get('naver_need', not c.get('naver')))
                add.append(ep)
            m[ep] = row
    save(m); return {'added': add, 'total': len(m)}
def link(m):
    from cards import naver_titles, toks
    t = naver_titles(); got = []
    for ep, r in m.items():
        if not r.get('naver_need') or r.get('naver_new'): continue
        q = toks(r.get('search', '') + ' ' + r.get('folder', '').replace('_', ' '))
        best = max(((len(q & toks(v)), k, v) for k, v in t.items()), default=(0, '', ''))
        if best[0] >= 2:
            r['naver_new'] = {'logNo': best[1], 'title': best[2], 'url': f'https://blog.naver.com/champion_chart/{best[1]}'}; got.append(ep)
    save(m); return {'linked': got}
def md(m):
    L = ['# 인테리어툰 ↔ 네이버 글 매핑', '인스타 · 스레드 → 네이버 한 방향(네이버 글엔 인스타 링크 없음)', '',
         '| 회차 | 상태 | 카드 | 원글 | 검색어 | 이어 준 네이버 글 | 새 글 | 인스타 | 스레드 | 날짜 |', '|---|---|---|---|---|---|---|---|---|---|']
    for ep in sorted(m):
        r = m[ep]; nv = (r.get('naver') or [{}])[0]
        L.append(f"| {ep} | {r.get('state','')} | {r.get('card','')} | {r.get('src','')} | {r.get('search','')} | {nv.get('title','')} | "
                 f"{(r.get('naver_new') or {}).get('title', '필요' if r.get('naver_need') else '')} | {r.get('insta','')} | {r.get('threads','')} | {r.get('date','')} |")
    return '\n'.join(L)
if __name__ == '__main__':
    m = load(MAP, {}); a = sys.argv[1] if len(sys.argv) > 1 else 'need'
    if a == 'scan': print(json.dumps(scan(m), ensure_ascii=False))
    elif a == 'pub':
        ep = sys.argv[2]; r = m.setdefault(ep, {'ep': ep}); r['insta'] = sys.argv[3]
        if len(sys.argv) > 4: r['threads'] = sys.argv[4]
        if len(sys.argv) > 5: r['date'] = sys.argv[5]
        r['state'] = '발행완료'; save(m); print(json.dumps(r, ensure_ascii=False))
    elif a == 'link': print(json.dumps(link(m), ensure_ascii=False))
    elif a == 'need':
        cards = load(CARDS, {})
        print(json.dumps({'eps': [ep for ep, r in m.items() if r.get('naver_need') and not r.get('naver_new')],
                          'cards': [f"{c['trade']} · {c.get('place','')} · {c['title']}" for c in cards.values() if c.get('usable') and c.get('naver_need')][:30]}, ensure_ascii=False, indent=0))
    elif a == 'up':
        call('fput', path='블로그/장부', name='인테리어툰_매핑.json', text=json.dumps(m, ensure_ascii=False, indent=1))
        call('fput', path='블로그/장부', name='인테리어툰_매핑.md', text=md(m)); print('up', len(m))

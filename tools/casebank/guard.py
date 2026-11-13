#!/usr/bin/env python3
"""사례 은행 중복 관리 — Claude가 맡음(11/13 사장님 「중복 발행하지 않게 관리는 네가 해」).
python3 guard.py check            → champion_chart RSS 50편과 사례 지역 · 단지 이름 대조 → 목록에 「겹침」 표시
python3 guard.py mark <사례ID앞자리> <글주소>  → 사용함 기록(같은 사례 두 번 금지)
python3 guard.py queue [n]        → 안 쓴 · 안 겹친 사례로 배정표 n칸(분야 돌려 가며 · 같은 분야 연속 금지) → 배정표.txt
결과는 bank.py index/upload 가 같이 올림(목록.txt 「사용」 열 · 배정표.txt)."""
import json, os, re, sys, glob, subprocess, html
B = '/home/claude/w/casebank'; U = f'{B}/used.json'
used = json.load(open(U)) if os.path.exists(U) else {}
def cases(): return [(f.split('/')[-3], f.split('/')[-2]) for f in sorted(glob.glob(f'{B}/*/*/사례.txt'))]
STOP = set('아파트 시공 중문 수리 후기 단열 단열공사 단열시공 곰팡이 결로 줄눈시공 입주청소 사전점검 안내 업체 서울 인천 경기 베란다 창틀 누수 코킹 욕실 리모델링 변기 교체 공동구매 혜택 오래된'.split())
def keys(cid):
    t = cid.split('_', 1)[1]; ws = [w for w in t.split('_') if len(w) >= 2 and w not in STOP and not re.match(r'^\d', w)]
    return ws[:2]
def check():
    x = subprocess.run(['curl', '-s', 'https://rss.blog.naver.com/champion_chart.xml'], capture_output=True, text=True).stdout
    titles = [html.unescape(re.sub(r'<!\[CDATA\[|\]\]>', '', t)) for t in re.findall(r'<item>.*?<title>(.*?)</title>', x, re.S)]
    links = [re.sub(r'<!\[CDATA\[|\]\]>', '', l) for l in re.findall(r'<item>.*?<link>(.*?)</link>', x, re.S)]; hit = 0
    for fld, cid in cases():
        k = keys(cid); m = [(t, l) for t, l in zip(titles, links) if k and all(w in t.replace(' ', '') for w in k)]
        no = cid.split('_')[0]
        if m and no not in used: used[no] = {'상태': '블로그에 있음(인스타 사용 가능)', '글': m[0][1].split('?')[0], '제목': m[0][0][:40]}; hit += 1
    json.dump(used, open(U, 'w'), ensure_ascii=False, indent=1); return hit
def top(f, c): return '줄눈' if '줄눈' in c else f.split('_')[0]
def queue(n=7):
    good = lambda f, c: os.path.exists(f'{B}/{f}/{c}/이야기.txt') or '상태: 좋음' in open(f'{B}/{f}/{c}/사례.txt', encoding='utf8').read()
    free = [(f, c) for f, c in cases() if good(f, c) and used.get(c.split('_')[0], {}).get('상태') != '인스타 사용함' and not re.search(r'공동|혜택|예약하기|안내', c)]   # 홍보 · 안내 글은 이야기가 약해 뺌
    by = {}
    for f, c in sorted(free, key=lambda x: not os.path.exists(f'{B}/{x[0]}/{x[1]}/이야기.txt')): by.setdefault(f, []).append(c)
    order = []
    while len(order) < n:
        recent = {top(f, c) for f, c in order[-2:]}   # 인스타 하루 3편 → 연속 3칸 안에 같은 주제 없게   # 같은 주제(중문 설치 · 수리 = 중문) 7칸 안에 한 번
        cand = [f for f in by if by[f] and top(f, by[f][0]) not in recent]
        if not cand: break
        f = sorted(cand, key=lambda f: (not os.path.exists(f'{B}/{f}/{by[f][0]}/이야기.txt'), -len(by[f])))[0]
        order.append((f, by[f].pop(0)))
    txt = ['[배정표] 낭만 인테리어 인스타 시공 스토리 · Claude가 중복 관리 · ChatGPT는 이 순서대로 1번부터 씀',
           '규칙: 여기 없는 사례는 쓰지 않는다 · 한 사례 한 글 · 쓰면 교신에 「사용함 <사례ID> → <글 주소 또는 예약 시각>」 · 인스타 하루 3편(사장님 11/13) · 같은 날 같은 주제 2편 금지. 「블로그에 있음」 사례도 인스타에는 써도 됨(블로그 글 주소를 캡션 링크로). 네이버 블로그 홀딩(하루 1편)과는 별개.', '']
    for i, (f, c) in enumerate(order, 1):
        st = '이야기.txt 있음' if os.path.exists(f'{B}/{f}/{c}/이야기.txt') else '뼈대만 · 쓰기 전 원문 확인'
        txt.append(f'{i}. {f} | {c} | {st}')
    open(f'{B}/배정표.txt', 'w', encoding='utf8').write('\n'.join(txt)); return order
if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'check': print({'겹침_새로': check()})
    elif a[0] == 'mark':
        no = a[1].split('_')[0]; used[no] = {'상태': '인스타 사용함', '글': a[2], '전': used.get(no, {}).get('상태', '')}; json.dump(used, open(U, 'w'), ensure_ascii=False, indent=1); print('ok', no)
    elif a[0] == 'queue': print(queue(int(a[1]) if len(a) > 1 else 7))

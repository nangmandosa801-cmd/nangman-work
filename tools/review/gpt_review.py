#!/usr/bin/env python3
"""인테리어 원고 ChatGPT 검수 — 배치 (11/4 사용자 「도우미 만들기 전에 내용만 챗지피트 검수 · 자동화 · 배치로」)
사용:
  python3 gpt_review.py <원고.md> [<원고.md> ...]     지정한 원고만
  python3 gpt_review.py --inbox                         /home/claude/w/review/inbox/*.md 전부(검수 안 된 것만)
  python3 gpt_review.py --setup     드라이브 「블로그/협업」 폴더 · 10분 검수 · 0_지시/검수_점검표.txt 올림(11/4 23시)
  python3 gpt_review.py --push      inbox 원고(글자만)를 드라이브 1_검수대기에 넣음 → Apps Script가 10분마다 검수
  python3 gpt_review.py --pull      드라이브 2_검수결과/*.gpt.json 을 out/ 으로 받아 옴(로컬 금지어 합침)
하는 일(원고마다, 동시에 4개):
  1) 사진 줄(!=) · 머리말 빼고 글자만 추림
  2) 로컬 금지어 검사(돈 안 듦)
  3) 블로그 우체통 gas.py 'gpt' 동작으로 ChatGPT에 점검표와 함께 보냄(키는 Apps Script 속성 OPENAI_KEY · 여기엔 없음)
  4) 결과 /home/claude/w/review/out/<파일이름>.gpt.json — verdict(통과|수정 필요) · fixes · local
출력: 원고마다 한 줄 요약. mkhelper.py auto 는 이 결과가 「통과」여야 돈다(--force 로 건너뛰기).
"""
import sys, os, re, json, glob
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, '/home/claude/helper')
OUT = '/home/claude/w/review/out'; INBOX = '/home/claude/w/review/inbox'
BANNED = ['갈렸', '갈랐', '갈라 ', '갈라보', '고요.', '최고', '프리미엄', '가능성', '헷갈', '놓치면 손해', '이번 달만', '%p',
          '업체가', '업체는', '010-', '어요.', '예요.', '자리', '놓습니다']
SYSTEM = """너는 한국어 블로그 원고 검수자다. 낭만 인테리어(제휴 시공팀을 손님께 이어 주는 블로그) 원고를 본다.
고쳐 쓰지 말고 문제만 짚어라. 손님이 읽다가 멈추거나 믿음을 잃을 만한 것만. 취향 · 문체 다듬기는 넣지 마라.
점검표:
1 장황함: 같은 말 되풀이 · 주제와 상관없는 일반론 문단. 너무 짧아 뜻이 빠진 곳.
2 추상적인 말: 무슨 일이 일어나는지 장면이나 숫자가 없는 문장.
3 글 쓰는 과정을 말하는 문장(예: 「이 글에서는 ~를 정리합니다」「여기까지 보셨다면」).
4 손님이 모를 전문용어를 풀이 없이 쓴 곳.
5 「~고」로 세 번 넘게 이은 문장 · 「~고요」로 끝나는 문장이 두 번 넘음.
6 출처 없이 단정한 큰 숫자 · 손님 후기 · 과장(최고 · 프리미엄 · 1위).
7 할인율 숫자 · 기한 압박(이번 달만 · 놓치면 손해).
8 업체 상호 · 업체 전화번호 · 업체 블로그 주소가 본문에 있음(있으면 빼라고 짚기. 업체 이름을 넣으라고 하지 마라).
9 제목(첫 줄 #): 검색어가 맨 앞이 아니거나 35자를 넘음.
10 시공 사례에 평수 · 공간 · 범위 · 자재 중 둘 이상이 빠짐.
규칙:
- quote는 원고에 실제로 있는 문장을 한 글자도 바꾸지 말고 복사(30자 이내). 원고에 없는 문장 · 이 점검표의 예시 문장을 quote로 쓰지 마라.
- fixes는 많아야 5개. 심각한 것부터.
- how는 구체적으로(무엇을 무엇으로). 「구체적인 예시 추가」「간결하게」 같은 막연한 말 금지.
- [CALL]로 시작하는 줄은 문의 상자라 검수하지 마라.
JSON으로만 답하라: {"verdict":"통과" 또는 "수정 필요","fixes":[{"no":점검표번호,"quote":"…","why":"짧게","how":"구체적으로"}],"good":"잘 된 점 한 줄"}
fixes가 없으면 verdict는 통과."""
def text_of(md):
    L = []
    for l in open(md, encoding='utf8'):
        if l.startswith('!=') or re.match(r'^(kicker|tags|thumb|links|nodef):', l): continue
        L.append(l.rstrip())
    return '\n'.join(L).strip()
def local(t):
    return [w for w in BANNED if w in t]
def review(md):
    name = os.path.basename(md).rsplit('.', 1)[0]; out = f'{OUT}/{name}.gpt.json'
    t = text_of(md); res = {'file': md, 'local': local(t)}
    try:
        from gas import call
        r = call('gpt', system=SYSTEM, user='원고:\n' + t[:12000])
        j = json.loads(r); res.update(j)
    except Exception as e:
        res.update({'verdict': '오류', 'error': str(e)[:200]})
    if res.get('verdict') == '통과' and res['local']: res['verdict'] = '수정 필요'
    os.makedirs(OUT, exist_ok=True); json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
    return f"{name}: {res.get('verdict')} · 고칠 곳 {len(res.get('fixes', []))} · 금지어 {res['local']}" + (f" · {res['error']}" if res.get('error') else '')
def passed(md):
    p = f"{OUT}/{os.path.basename(md).rsplit('.', 1)[0]}.gpt.json"
    try: return json.load(open(p)).get('verdict') == '통과'
    except Exception: return False
def _b64(t): import base64; return base64.b64encode(t.encode('utf8')).decode()
def setup():
    from gas import call
    call('collab'); return call('fput', path='블로그/협업/0_지시', name='검수_점검표.txt', b64=_b64(SYSTEM))
def push():
    from gas import call
    n = 0
    for f in sorted(glob.glob(f'{INBOX}/*.md')):
        name = os.path.basename(f)[:-3]
        if os.path.exists(f'{OUT}/{name}.gpt.json'): continue
        call('fput', path='블로그/협업/1_검수대기', name=name + '.txt', b64=_b64(text_of(f))); n += 1
    return n
def pull():
    from gas import call
    os.makedirs(OUT, exist_ok=True); got = []
    for x in call('ls', path='블로그/협업/2_검수결과'):
        if not x['name'].endswith('.gpt.json'): continue
        name = x['name'][:-9]; md = f'{INBOX}/{name}.md'
        try: import base64; j = json.loads(base64.b64decode(call('fget', id=x['id'])['b64']).decode('utf8'))
        except Exception: continue
        if os.path.exists(md):
            _n = lambda x: re.sub(r'[\s「」\'"“”]', '', x); _t = _n(text_of(md))
            j['fixes'] = [x for x in j.get('fixes', []) if _n(x.get('quote', ''))[:25] and _n(x['quote'])[:25] in _t]
            if not j['fixes'] and j.get('verdict') == '수정 필요': j['verdict'] = '통과'
        j['file'] = md; j['local'] = local(text_of(md)) if os.path.exists(md) else []
        if j['local'] and j.get('verdict') == '통과': j['verdict'] = '수정 필요'
        json.dump(j, open(f'{OUT}/{name}.gpt.json', 'w'), ensure_ascii=False, indent=1); got.append((name, j.get('verdict'), len(j.get('fixes', []))))
    return got
if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] in ('--setup', '--push', '--pull'):
        print(json.dumps({'--setup': setup, '--push': push, '--pull': pull}[a[0]](), ensure_ascii=False)); sys.exit()
    if a == ['--inbox']:
        a = [f for f in sorted(glob.glob(f'{INBOX}/*.md')) if not os.path.exists(f"{OUT}/{os.path.basename(f)[:-3]}.gpt.json")]
    if not a: sys.exit('검수할 원고 없음')
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(review, a): print(line)

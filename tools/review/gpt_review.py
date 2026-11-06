#!/usr/bin/env python3
"""인테리어 원고 ChatGPT 검수 — 배치 (11/4 사용자 「도우미 만들기 전에 내용만 챗지피트 검수 · 자동화 · 배치로」)
사용:
  python3 gpt_review.py <원고.md> [<원고.md> ...]     지정한 원고만
  python3 gpt_review.py --inbox                         /home/claude/w/review/inbox/*.md 전부(검수 안 된 것만)
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
SYSTEM = """너는 한국어 블로그 원고 검수자다. 낭만 인테리어(시공팀을 손님께 이어 주는 블로그) 원고를 아래 점검표로 본다.
고쳐 쓰지 말고, 문제만 짚어라. 사실은 원고 안에서만 판단하고 새 정보를 지어내지 마라.
점검표:
1 장황함: 배경 설명 · 같은 말 되풀이 · 일반론 문단(줄일 곳을 문장으로 짚기). 다만 너무 짧아 뜻이 빠진 곳도 짚기.
2 추상적인 말: 실제 장면이나 숫자 없이 뜬구름 잡는 문장.
3 글 쓰는 과정을 말하는 문장(「먼저 바로잡고 시작하겠습니다」 류).
4 어려운 말: 일상어로 바꿀 단어.
5 문장 길이: 「~고」로 길게 이은 문장 · 「~고요」 반복.
6 지어낸 것으로 보이는 것: 손님 말 · 후기 · 출처 없는 숫자 · 과장(최고 · 프리미엄 · 1위).
7 판매 문구 남용: 할인율 숫자 · 기한 압박(이번 달만 · 놓치면 손해) · 「견적」 반복.
8 업체 이름 · 전화번호 글자 · 업체 블로그 주소가 본문에 있는지.
9 제목: 검색어가 맨 앞에 있는지 · 30자 안팎인지.
10 시공 사례: 사례마다 평수 · 공간 · 범위 · 자재 · 전후 사진 설명이 있는지.
JSON으로만 답하라: {"verdict":"통과" 또는 "수정 필요","fixes":[{"no":점검표번호,"quote":"문제 문장 그대로(30자 이내)","why":"짧게","how":"고칠 방향 짧게"}],"good":"잘 된 점 한 줄"}
심각하지 않은 것(취향)은 넣지 마라. fixes가 없으면 verdict는 통과."""
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
if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--inbox']:
        a = [f for f in sorted(glob.glob(f'{INBOX}/*.md')) if not os.path.exists(f"{OUT}/{os.path.basename(f)[:-3]}.gpt.json")]
    if not a: sys.exit('검수할 원고 없음')
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(review, a): print(line)

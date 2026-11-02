import json,re,sys
J='/root/.claude/projects/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588.jsonl'
doc=None
def walk(o):
    global doc
    if isinstance(o,dict):
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
    elif isinstance(o,str):
        if o.startswith('{"method":"project_read","path":"claude/낭만인테리어_제휴후보.md"'):
            try: doc=json.loads(o)['content']
            except Exception as e: pass
for line in open(J,encoding='utf-8'):
    try: walk(json.loads(line))
    except Exception: pass
assert doc, 'not found'
n0=len(doc)
a=doc.count('**10/8 낮에 사용자가 문자를 보낼 예정')
doc=doc.replace('**10/8 낮에 사용자가 문자를 보낼 예정','**10/8 09:15 사용자가 문자를 보냄 · 답 기다림')
for s in [' · 사용자가 부르면 업체 이름 · 번호 · 문안을 알려 줌',' · 사용자가 부르면 업체 이름과 번호를 알려 줌']:
    doc=doc.replace(s,'')
b=doc.count('| **10/8 낮에 문자 보낼 곳** |')
doc=doc.replace('| **10/8 낮에 문자 보낼 곳** |','| 답 기다림(10/8 09:15 문자 보냄) |')
doc=doc.replace('| 사용자가 문자로 제안할 예정 |','| 문자로 제안함 |')
doc=doc.replace('같은 대구의 「청소의 실력」은 낮에 문자 예정','같은 대구의 「청소의 실력」에는 10/8 09:15 문자를 보냄')
old='**10/8 00:56 사용자: 「이 글도 업체별로 네가 알려줘 내일」**'
assert old in doc
doc=doc.replace(old,'**10/8 09:03 일곱 곳의 이름 · 번호 · 업체별 문안을 대화창에 줌 → 09:15 사용자 「문자로는 다 보냄」. 일곱 곳 모두 답 기다림. 종합 인테리어 후보 여덟 곳은 사용자가 전화하기로 함(아직 결과 없음).**\n\n'+old,1)
open('w/partner_1008.md','w',encoding='utf-8').write(doc)
print(n0,len(doc),a,b,doc.count('보낼 예정'),doc.count('사용자가 부르면'))

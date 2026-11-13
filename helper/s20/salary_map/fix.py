#!/usr/bin/env python3
"""ChatGPT 자연스러움 검수 결과(.gpt.json)를 mk.py 문장에 반영한다.
사용: python3 fix.py <nangman_salary_map.gpt.json>   → 바꾼 것 · 못 바꾼 것을 JSON 으로. 그다음 bash rebuild.sh
규칙: quote 가 mk.py 에 꼭 한 번 나올 때만 바꾼다 · 숫자가 달라지는 고침은 하지 않는다(사실 · 숫자는 그대로) · 제목 · 소제목 · 표 · 근거 줄은 건드리지 않는다."""
import sys, json, re
j = json.load(open(sys.argv[1], encoding='utf8'))
if j.get('checklist') != '자연스러움_1112': print(json.dumps({'ok': False, 'why': '다른 점검표 결과 — 쓰지 않음'}, ensure_ascii=False)); sys.exit(2)
s = open('mk.py', encoding='utf8').read()
nums = lambda t: sorted(re.findall(r'\d[\d,.]*', t))
done, skip = [], []
for f in j.get('fixes', []):
    q, to = (f.get('quote') or '').strip(), (f.get('to') or '').strip()
    if not q: continue
    if s.count(q) != 1: skip.append({'quote': q, 'why': 'mk.py 에 없거나 여러 번 — 손으로'}); continue
    line = next(l for l in s.split('\n') if q in l)
    if line.startswith(('o.append(H(', 'o.append(NOTE(', 'TITLE', ' (', 'o.append(related', 'o.append(tags')): skip.append({'quote': q, 'why': '제목 · 소제목 · 근거 줄 — 그대로'}); continue
    if to and nums(q) != nums(to): skip.append({'quote': q, 'why': '숫자가 달라짐 — 그대로'}); continue
    if not to and nums(q): skip.append({'quote': q, 'why': '숫자가 든 문장은 지우지 않음'}); continue
    if any(w in to for w in ('까닭', '갈라', '갈렸', '갈랐', '고요', '가능성')): skip.append({'quote': q, 'why': '금지어가 든 고침'}); continue
    s = s.replace(q + ' ', (to + ' ') if to else '') if (q + ' ') in s and not to else s.replace(q, to)
    done.append({'no': f.get('no'), 'quote': q, 'to': to})
open('mk.py', 'w', encoding='utf8').write(s)
print(json.dumps({'ok': True, 'verdict': j.get('verdict'), 'done': len(done), 'skip': skip, 'tone': j.get('tone')}, ensure_ascii=False, indent=1))

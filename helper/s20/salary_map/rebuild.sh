#!/bin/bash
# 「연봉별 대출한도」 원고 다시 만들기 — 문장을 고친 뒤(python3 fix.py <결과.gpt.json> 또는 mk.py 직접) 이 한 줄.
# 그림은 fig.py 가 ana.json 으로 다시 그린다(그림 파일은 저장소에 없음). 숫자가 계산과 어긋나면 mk.py 의 assert 가 멈춘다.
set -e
cd /home/claude/helper/s20/salary_map
[ -f /home/claude/rtn/M_budget_sudo.pkl ] && python3 ana.py > /dev/null
[ -f img/nangman_salary_map_thumb.png ] || python3 fig.py
python3 mk.py
python3 ../_ban_check.py .
[ -f /home/claude/kit_dasi/selfqa.py ] && python3 /home/claude/kit_dasi/selfqa.py post.txt 2>/dev/null | python3 -c "import json,sys; j=json.load(sys.stdin); print('selfqa fail', [f for f in j['fail'] if '생일' not in f])" || true
python3 /home/claude/tools/postkit/html2aside.py . nangman_salary_map
python3 /home/claude/tools/postkit/html2aside_html.py . nangman_salary_map
python3 up.py "$@"

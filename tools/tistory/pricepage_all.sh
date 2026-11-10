#!/bin/bash
# 티스토리 talk7921 하남 실거래가 7개 페이지를 다시 만들고 드라이브에 덮어쓴다 (매달 · 자료 /home/claude/rtn 갱신 뒤)
# 결과: /home/claude/w/ts_pages/<slug>/ · 드라이브 「블로그/협업/4_어사이드/티스토리/원고/<slug>/」 index.html · 01.jpg(대표) · 02.jpg~
# 끝 줄 JSON = 페이지별 제목 · 글자 수 · 그림 수 · 드라이브 경로
cd /home/claude/tools/tistory || exit 1
UP=--up; [ "$1" = "--local" ] && UP=
for k in misa gamil wirye deokpung sinjang pungsan hanam; do
  python3 pricepage.py $k $UP 2>&1 | grep '^{' || echo "{\"key\":\"$k\",\"error\":true}"
done

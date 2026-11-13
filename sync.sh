#!/bin/bash
# 이 창이 실제로 고친 파일만 저장소에 올린다(11/13 고침 — 옛 파일로 덮어쓰기 방지). 규칙 전문은 sync.py 맨 위.
# 새 대화에서 쓰기: git clone --depth 1 https://github.com/nangmandosa801-cmd/nangman-work /home/claude/nangman-work && bash /home/claude/nangman-work/restore.sh
exec python3 /home/claude/nangman-work/sync.py sync "$@"

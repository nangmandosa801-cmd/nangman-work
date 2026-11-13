#!/bin/bash
# 저장소 파일을 이 창(/home/claude)으로. 없는 파일은 가져오고, 이 창이 안 고친 낡은 파일은 새것으로 바꾼다(옛 파일은 /home/claude/.stale_bak).
# 이 창이 고친 파일은 건드리지 않는다. 규칙 전문은 sync.py 맨 위.
python3 /home/claude/nangman-work/sync.py restore "$@" && echo restored

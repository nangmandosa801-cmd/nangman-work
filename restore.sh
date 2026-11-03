#!/bin/bash
# 새 대화(빈 /home/claude)에서 저장소 파일을 원래 자리로 되돌린다. 이미 있는 파일은 덮어쓰지 않는다.
R=/home/claude/nangman-work
for d in tools ipjuhub watch int/mp4_1015 w helper gcontacts kit spread gas coffee 텍스트; do
  [ -d $R/$d ] || continue; mkdir -p /home/claude/$d; cp -rn $R/$d/. /home/claude/$d/
done
cp -n $R/root/* /home/claude/ 2>/dev/null
echo restored

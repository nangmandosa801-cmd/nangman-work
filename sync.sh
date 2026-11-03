#!/bin/bash
# /home/claude 작업 파일(코드 · 원고 · 장부)을 이 저장소로 모아 올린다.
# 그림 · 영상 · 데이터 덩어리(pkl) · 로그인 파일(token/client.json)은 .gitignore로 뺀다. 2MB 넘는 파일도 뺀다.
# 새 대화에서 쓰기: git clone https://github.com/nangmandosa801-cmd/nangman-work /home/claude/nangman-work && bash /home/claude/nangman-work/restore.sh
R=/home/claude/nangman-work; cd $R
for d in tools ipjuhub watch int/mp4_1015 w helper gcontacts kit spread gas coffee 텍스트; do
  [ -d /home/claude/$d ] || continue
  mkdir -p "$R/$d"
  (cd /home/claude/$d && find . -type f -size -2M \
     ! -name '*.jpg' ! -name '*.jpeg' ! -name '*.png' ! -name '*.gif' ! -name '*.webp' \
     ! -name '*.mp4' ! -name '*.mp3' ! -name '*.wav' ! -name '*.pkl' ! -name '*.pdf' ! -name '*.zip' \
     ! -path "./kin*" ! -name "token.json" ! -name 'client.json' ! -path '*/__pycache__/*' ! -name '*.bak*' ! -path '*/bak*/*' -print0 \
   | tar --null -cf - -T - ) | (cd $R/$d && tar -xf -)
done
mkdir -p root && find /home/claude -maxdepth 1 -type f \( -name "*.py" -o -name "*.sh" -o -name "*.md" \) -size -2M -exec cp -p {} root/ \;
git add -A >/dev/null
git -c user.name=nangman -c user.email=nangmandosa801@users.noreply.github.com commit -qm "작업 파일 동기화 $(TZ=Asia/Seoul date +%m%d_%H%M)" && git pull -q --rebase -X ours origin main && git push -q origin HEAD:main && echo pushed || echo nochange

# 낭만 그룹 작업 저장소 — 모든 대화창 공통 규칙

## 시작할 때 (새 대화 · 정기 작업)
1. `git clone --depth 1 https://github.com/nangmandosa801-cmd/nangman-work /home/claude/nangman-work` (이미 있으면 `git -C /home/claude/nangman-work pull -q`)
2. `bash /home/claude/nangman-work/restore.sh` → /home/claude/tools · ipjuhub · watch · w · int/mp4_1015 등이 제자리로 돌아온다.
3. 프로젝트 문서 claude/토큰절감_공통원칙_1031.md 를 지킨다.

## 끝낼 때
- 파일을 고쳤으면 `bash /home/claude/nangman-work/sync.sh` 한 번 (커밋 · 올리기까지 한다).

## 저장소에 없는 것
- 사진 · 영상 · pkl · 2MB 넘는 파일 · 로그인 파일(token.json · client.json). 사진은 낭만 창고(블로거), 영상은 PC C:\블로그.

## 토큰 원칙 (요약)
- 한 대화를 길게 끌지 않는다. 일 덩어리마다 새 대화 + 이어 갈 내용은 프로젝트 문서에.
- 이 대화로 돌아오는 send_later 알림을 걸지 않는다. 반복 일은 새 대화로 도는 정기 작업으로.
- fork 서브에이전트 금지. 반복 일은 스크립트 한 번, 결과는 JSON 몇 줄.
- 큰 출력(Upload-Post list_scheduled · list_triggers 전문)은 파일로 받아 jq/python으로 필요한 줄만.
- 원고는 큰 모델, 올리기 · 검사 · 숫자 모으기는 작은 모델.


## ★ 11/03 추가 — 모든 창 공통 (사용자 11/3 08:36 「다 적용해 지트허브에 저장해」 · 08:41 「다른 창도 개선해줘」)
- **작업 파일은 GitHub 비공개 저장소 nangmandosa801-cmd/nangman-work 에 있다.** 새 대화 · 정기 작업은 시작할 때 `git clone --depth 1 https://github.com/nangmandosa801-cmd/nangman-work /home/claude/nangman-work && bash /home/claude/nangman-work/restore.sh` 로 /home/claude 작업 폴더를 되살린다(빈 폴더 문제 해결). 끝낼 때 파일을 고쳤으면 `bash /home/claude/nangman-work/sync.sh`.
- 저장소 맨 위 CLAUDE.md 가 공통 규칙이다. 사진 · 영상 · pkl · 로그인 파일은 저장소에 없다.
- 이 대화로 돌아오는 send_later 알림을 새로 걸지 않는다. 발행 뒤 후속은 주말에 몰아서 한다(claude/주말작업_1107.md).
- 큰 출력(Upload-Post list_scheduled 24만 자 · list_triggers 전문)은 파일로 받아 python으로 필요한 줄만 본다.

## ★ 11/03 09:52 추가 — PC 없이 올리기 (사용자 「PC가 연결 안되어도 작동하게」 · 「둘다 해 다른 채팅창도 적용해줘」)
- **스레드 kimdongjin24는 크롬을 쓰지 않는다.** Upload-Post upload_text / upload_video / upload_photos (user "default" = 인스타 · 스레드 kimdongjin24 · platforms ["threads"] · confirmed true). 블로그 주소는 본문에 넣지 않고 platformOptions.threadsFirstComment 로. 주제는 threadsTopicTag. 피크(07:00~08:50 · 21:00~23:30 KST) 밖이면 scheduledDate + timezone "Asia/Seoul" 로 예약하고 다른 스레드 예약과 20분 넘게 띄운다.
- **구글 블로그(낭만 부동산 7361591188244782195 · 낭만 창고 3521924271702627135 · 입주 노트)는 「블로그 우체통」(nangmandosa801 계정 Apps Script 웹 앱)으로 쓴다.** /home/claude/gas/conf.json 이 있으면 `python3 /home/claude/helper/gas.py post|append|get|list|image …`. conf.json 이 아직 없으면(사용자 설정 전) 예전처럼 크롬, 크롬도 없으면 원고만 남기고 건너뛴다. 설정 페이지: https://claude.ai/artifact/6Q9PUosF9n3JCDdpNdGuuw
- **PC 폴더 C:\블로그**: 사용자가 Google Drive 데스크톱으로 동기화하면 `gas.py ls|fget|fput|flink "블로그/…"` 로 PC 없이 읽고 쓴다. 영상은 flink 주소를 Upload-Post videoPathOrUrl 로 넘긴다.
- 네이버 · 티스토리는 그대로 Aside(사용자 브라우저)가 발행한다.

## ★ 11/03 10:04 추가 — 산출물은 PC가 아니라 구글 드라이브 (사용자 「산출물도 피씨에 저장 안하고 구글 드라이브에 저장하는 방식으로」 · 인테리어 창에도 적용)
- **결과 파일은 PC(C:\블로그)에 쓰지 않는다.** 영상 · 커버 · info → 드라이브 「블로그/shorts」, 원고 txt → 「블로그/텍스트/<블로그>」, 그 밖의 결과 → 「블로그/<블로그>」. `python3 /home/claude/helper/gas.py fput "블로그/<폴더>" <파일>`.
- 낭만 인테리어 도구도 같은 길로 바꿈: 발행 뒤 후속 `post_followup.py` 가 클립 · 커버 · info 를 「블로그/shorts」에 올림 · 발행 도우미 `mkhelper.py auto <md> <tag> '<when>'` 가 그림을 우체통(gas.py image)으로 낭만 창고에 올려 브라우저 없이 도우미까지 만듦.
- conf.json 이 없으면 브라우저 방식으로 하고 보고에 「드라이브 미저장」을 적는다.

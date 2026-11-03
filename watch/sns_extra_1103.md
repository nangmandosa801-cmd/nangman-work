# 「네이버 발행 → 전 채널」이 함께 하는 일 — 릴스 2편 · 부동산 스레드 홍보 (11/3)
사용자 11/3 10:21 「Upload-Post 연결 추가 니가 해」 → 커넥터가 없는 두 예약 작업(낭만 인테리어 릴스 2편 · 입주 글 스레드 홍보)을 끄고, Upload-Post가 붙은 「네이버 발행 → 전 채널」(08:17 · 13:17 · 20:17)이 대신 한다. 크롬 · 화면 캡처 쓰지 않음.

## A. 08:17 실행에서만 — 낭만 인테리어 릴스 2편
1. 프로젝트 문서 claude/낭만인테리어_인스타_릴스_큐_1027.md 의 「게시 기록」 · 「대기 큐」. 큐 맨 앞 2개 slug(게시 기록에 있는 것 · 셀프/DIY 제외). nangman.group에는 올리지 않음. 네이버 클립 · 유튜브는 안 함.
2. 영상: /home/claude/gas/conf.json 이 있으면 `python3 /home/claude/helper/gas.py ls "블로그/shorts"` → nangman_interior_<slug>_short.mp4 는 flink 주소, _short_info.txt 는 fget. 없으면 A는 건너뛰고 보고에 「릴스: 드라이브 미설정」.
3. upload_video(user "default", platforms ["instagram","threads"], confirmed true). 캡션: 숫자 한 줄 · 「프로필 링크 블로그에」 · 「사진 한 장 보내 주시면 무료로 봐 드립니다 010-2882-8165」 · 해시태그 5개 · 이모지 없음. 블로그 주소는 캡션에 넣지 않고 platformOptions.threadsFirstComment 「자세한 금액 · 사진은 블로그에 → <info 「연결할 글」>」. 아침 피크(07:00~08:50)로 scheduledDate(timezone "Asia/Seoul") · 다른 default 예약과 20분 넘게.
4. 큐 문서 게시 기록에 날짜 · slug · 예약 시각, 대기 큐에서 뺌 → project_write.

## B. 20:17 실행에서만 — 낭만 부동산 입주 글 스레드 홍보
1. `GREP='224449575744|사무소 인터뷰를 받습니다' python3 /home/claude/watch/rss_new.py dong_jin_kim 24` — new 가 비면 B 끝.
2. claude/낭만부동산_글원칙_통합_1022.md 7번 기록표에 있는 글은 빼고, 모집 글 224449575744 자체도 뺌. 하루 최대 2편.
3. 본문: 그 단지 이야기 한두 줄(글의 결론 숫자 하나) + 「이 단지 앞 중개사무소 인터뷰를 받습니다. 현장 이야기를 들려주시면 블로그에 무료로 소개합니다.」 링크 · 광고 표기 · 할인 숫자 · 동호수 가격 · 맞팔 말 없음.
4. upload_text(user "nangman_budongsan", platforms ["threads"], confirmed true, platformOptions.threadsTopicTag "부동산", threadsFirstComment 「자세한 내용은 블로그에 → <네이버 글 주소>」) · 21:00~23:30 칸 scheduledDate · 다른 스레드 예약과 20분 넘게.
5. 7번 기록표에 「날 | 글 번호 | 단지 | 예약 시각 · job id」 → project_write.

A · B 를 한 뒤에 원래 순서(새 글 확인 → 없으면 끝)로 간다. A · B 결과는 보고 한 줄에 같이.

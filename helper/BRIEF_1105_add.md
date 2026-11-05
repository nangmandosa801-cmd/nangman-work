# 11/5 밤 추가 지시 (BRIEF_1103.md 위에 덮어씀)
- 실거래 파일: 매매 = /home/claude/rtn/M2026.pkl (M2025 도 있음), 전월세 = /home/claude/rtn/R2026.pkl. 해제 거래 뺌.
- urls.json 은 직접 만든다: 그림마다 `python3 /home/claude/helper/gas.py image <png>` → {"1_xxx": 주소, "thumb": 주소}. 금지어 0 확인(`python3 ../make_helper.py . --skip-fig`).
- aside.py 와 아티팩트 게시는 하지 않는다. 대신 마지막에:
  `python3 /home/claude/tools/postkit/html2aside.py <폴더> nangman_<슬러그> --up` 와
  `python3 /home/claude/tools/postkit/html2aside_html.py <폴더> nangman_<슬러그> --up` (둘 다 사진 수가 같아야 함), 그다음 `bash /home/claude/nangman-work/sync.sh`.
- 같은 폴더 이름이 이미 있으면 지우지 말고 <폴더>_old 로 옮긴다.
- 최근 만든 글과 겹치지 않기: /home/claude/helper/{jw,bc,hr,gd4,os,tj,jbs,bdr,gs,bun12}/mk.py 제목 확인 + 낭만 부동산 발행 목록 확인. 이어지는 지점이 있으면 링크로 잇는다.
- 보고: 폴더 · 제목 · 자동완성 실측 · 사진 수 · 확인 못 한 것 · 출처. 한국어로 짧게.

## 20편 시리즈 (11/5 21:46 · 전략 문서 claude/낭만부동산_1000클릭_전략_20편_1105.md)
- 폴더: /home/claude/helper/s20/<슬러그>/ (kit.py · tails.py 는 /home/claude/helper/pg/ 에서 복사 · ../make_helper.py 경로는 /home/claude/helper/make_helper.py 로 바꿔 부른다)
- 발행 순서상 앞 글(11/12~11/17 예약 글: jw bc hr gd4 os tj jbs bdr gs bun12 · 각 /home/claude/helper/<폴더>/mk.py TITLE)과 이번 20편끼리 링크를 건다. 아직 발행 전 글은 링크 없이 제목 글자만(나중에 링크 작업).
- 「갈-」 표현 · 글 쓰는 과정 서술 · 「~고요」 반복 · 추상 표현 금지. 쉬운 말, 짧은 문장. 지어낸 사실 금지 — 확인 못 한 건 쓰지 않거나 「확인되지 않음」.

## 하남 본진 시리즈 (11/5 23:25 사용자 「개업하면 하남 · 하남은 더 심도 있게 써서 검색 순위를 먹어 보자」)
- 하남 글은 「하남을 숫자로 가장 잘 아는 블로그」가 목표. 넓은 말(하남 아파트 시세) 말고 단지 · 동 · 역 · 구역 이름의 좁은 검색어.
- 기존 하남 글 목록: /home/claude/helper/hanam_posts.txt — 글마다 이 중 3개 이상을 본문 안에서 이어 쓰고(링크), 꼬리 링크 5개 이상은 하남 글 위주로.
- 자동완성 실측(11/5): /home/claude/helper/hanam_ac_1105.json 참고 후 다시 잼.
- 중개 광고 · 매물 소개 금지(무자격). 분석과 정보까지만. 인테리어 상자는 잔금 · 입주 이야기가 나올 때 1개만.

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

## 한 줄 도구 (11/3)
- 발행 뒤 후속: `python3 /home/claude/tools/followup/post_followup.py` (인자 없으면 champion_chart 새 글 전부) → 장부 기록 · 꼬리 링크 도우미 · 세로 클립 · info. SNS는 「네이버 발행 → 전 채널」 정기 작업이 올림.
- 발행 도우미: `python3 /home/claude/tools/postkit/mkhelper.py prep|put|js|build|queue …` (사용법은 파일 맨 위). 순서: prep → Upload-Post create → put → complete → 블로거 낭만 창고 새 초안에서 js 결과 실행 → 결과를 tokens.txt로 저장 → build → 도우미 publish → queue → 큐 publish.

## PC 없이 올리기 (11/3 · 사용자 「PC가 연결 안되어도 작동하게」 · 「다른 채팅창도 적용」)
- **스레드 kimdongjin24**: 크롬 대신 Upload-Post `upload_text`/`upload_video`/`upload_photos` (user "default" · platforms ["threads"] · confirmed true). 링크는 본문에 넣지 않고 `platformOptions.threadsFirstComment`. 주제는 `threadsTopicTag`. 피크(07:00~08:50 · 21:00~23:30) 밖이면 `scheduledDate` + timezone "Asia/Seoul"로 예약. 인스타 kimdongjin24도 같은 default 프로필.
- **구글 블로그(낭만 부동산 · 낭만 창고 · 입주 노트)**: 「블로그 우체통」(Apps Script 웹 앱). `/home/claude/gas/conf.json`({"url","key"})이 있으면 `python3 /home/claude/helper/gas.py post|append|get|list|image …` (사용법은 파일 맨 위). 없으면 예전처럼 크롬, 크롬도 없으면 원고만 남기고 건너뜀.
- **PC 폴더 C:\블로그**: 사용자가 Google Drive 데스크톱으로 동기화하면 `gas.py ls|fget|fput|flink "블로그/…"` 로 읽고 씀. 영상은 `flink` 주소를 Upload-Post videoPathOrUrl로.
- 설정 페이지: https://claude.ai/artifact/6Q9PUosF9n3JCDdpNdGuuw
- **11/3 10:53 설정 끝 · 작동 확인**(글 초안 · 그림 · 드라이브 폴더). Cloud 프로젝트는 nangman-contacts(87451722112, Blogger API 켬). gas.py 블로그 이름: budongsan · changgo · interior · dosa · bunyang · isa · study. **입주 노트(nangman-ipju)는 nangmandosa801 블로그 목록에 없음** → 다른 계정 블로그라 아직 크롬으로(사용자가 nangmandosa801을 작성자로 초대하면 우체통으로).

## PC 없이 · 산출물은 구글 드라이브 (11/3 10:04 사용자 「pc 연결 안되어도 워크플로우 타게」 · 「산출물도 피씨에 저장 안하고 구글 드라이브에」)
- PC(C:\블로그)에 저장하지 않는다. 결과 파일(영상 · 커버 · info · 원고 txt · 그림)은 구글 드라이브 「블로그/…」 폴더에 `python3 /home/claude/helper/gas.py fput "블로그/<폴더>" <파일>` 로 올린다. 영상: 「블로그/shorts」 · 원고: 「블로그/텍스트/<블로그>」.
- SNS 영상은 `gas.py flink <id>` 주소를 Upload-Post videoPathOrUrl 로 넘긴다(PC에서 받아 오지 않음).
- 낭만 창고 그림은 `gas.py image <파일>`(브라우저 없음). 발행 도우미는 `mkhelper.py auto <md> <tag> '<when>'` 한 번.
- 블로그 우체통 설정 파일 /home/claude/gas/conf.json 이 없으면(사용자 설정 전) 브라우저 방식으로 하고, 그것도 안 되면 결과를 대화로 보내고 「드라이브 미저장」을 보고에 적는다.
- 네이버 · 티스토리 발행은 그대로 Aside.

## 발행 도우미 파일은 드라이브에 (11/3 13:2x 사용자 「도우미 위치도 다 클라우드에 올려」)
- 도우미 html(그림 주소 박힌 큰 파일)은 저장소에 못 담으니 드라이브 「블로그/도우미」에 있다. 목록은 「블로그/장부/도우미_목록.json」 (제목 · 파일 이름 · 드라이브 id).
- 새 도우미를 만들면 `python3 /home/claude/tools/followup/helper_cloud.py up` 한 번(이미 올린 것은 건너뜀).
- 이 창에 파일이 없으면 `python3 /home/claude/tools/followup/helper_cloud.py get "<제목 일부>"` → 경로 출력. post_followup.py 는 로컬에 없으면 알아서 받아 온다.

## 지산드림 (jisandream01 · 11/3)
- 작업 폴더 /home/claude/jisan (원고 · 그림 스크립트 · master/ 겹침 검사 · 장부), /home/claude/jisan_move (발행 글 목록 fetch_list.py).
- 한 번에: `python3 /home/claude/jisan/make_jisan.py <글.py> <폴더> <slug> <예약일> --helper` → 빌드 · SEO · 금지어 · 겹침 · 원고 txt · 도우미 (JSON 한 줄).
- 하남 땅값 자료 hanam_land.pkl 은 저장소에 없음 — /mnt/attach/outputs/부동산DB.parquet 에서 다시 만든다(자료=='토지' · 시군구에 하남 · 해제사유발생일 '-').
- 방향: 하남 토지 집중 · 땅 팔 사람 · 살 사람 둘 다 (프로젝트 문서 claude/지산드림_하남토지_집중_1031.md · claude/지산드림_매물부스팅_마스터.md).

## 틱톡 중단 (11/3 22:43 사용자 「낭만도사만 빼고 틱톡 다 죽여」)
- 낭만 인테리어(Upload-Post default · champion_chart) · 낭만 부동산(nangman_budongsan · dong_jin_kim) 틱톡에는 올리지 않는다. 어떤 작업이든 platforms 에 "tiktok" 을 넣지 않는다.
- 낭만도사(nangman_dosa · hidjkim2000) 틱톡만 계속 쓴다.
- 계정 삭제는 사용자가 틱톡 앱에서 직접(Claude는 하지 않음).

## 블로그 우체통 열쇠는 저장소에 없음 (11/4 23시 · 저장소가 공개라 열쇠가 드러나 있었음)
- Code.gs 의 KEY 는 Apps Script 스크립트 속성 KEY 에서 읽는다. gas/conf.json · key.txt · setup.html 은 저장소에서 뺐다(.gitignore).
- 새 창에서 /home/claude/gas/conf.json 이 없으면 사용자에게 웹 앱 주소와 열쇠를 받아 {"url","key"} 로 만든다(공개 저장소 · 프로젝트 문서에 적지 않음).

## 네이버 발행 수 제한 (11/5 사용자 「블로그 정지 사유」 공유)
- 낭만 인테리어(champion_chart)는 하루 2편 이하, 4시간 이상 간격으로만 예약한다. 큐에 줄을 넣을 때 그날 이미 2편이면 다음 날로.
- 단지명만 바꾼 비슷한 입주 · 중문 글은 쓰지 않는다. 같은 단지 글은 그 단지만의 사실을 절반 이상.
- 어사이드 지시서에는 늘 「발행 뒤 본문에 ##, **, [CALL], <div 같은 기호가 글자로 보이면 지우기」를 넣는다.
- 댓글 돌리기 · 같은 글 반복 등록은 하지 않는다.

## 도우미 없이 어사이드가 사람처럼 발행 (11/5 14시 사용자 「앞으로 도우미 없이 네가 위치 알려 주면 어사이드가 인간처럼 올릴게」)
- 원고는 HTML(11/5 14:50 사용자 「txt는 그렇고 html 방식이어야지」): `mkhelper.py auto` 로 만든 HTML(서식 · 표 · 사진)을 Artifact로 publish(어사이드가 여는 「화면」 링크) + 드라이브 「블로그/협업/4_어사이드/원고/<글이름>.html」.
- 예비본으로 `python3 /home/claude/tools/postkit/md2txt.py <원고.md> <글이름>` → txt + 사진 폴더도 같은 「원고」에.
- 같은 4_어사이드에 「지시_…txt」(번호 · 날짜 시각 · 카테고리 · 제목 · 화면 링크 · 파일 이름)를 넣는다. 예약 큐 아티팩트는 쓰지 않는다.
- 어사이드 작성 규칙은 드라이브 「블로그/협업/0_지시/어사이드_발행방식_1105.txt」.

## 낭만 부동산 원고 → 어사이드 (11/5 발행 방식 변경 · 프로젝트 문서 claude/공지_발행방식변경_1105.md)
- helper 폴더(post.html · urls.json · img/)를 `python3 /home/claude/tools/postkit/html2aside.py <폴더> nangman_<이름> --up` + `html2aside_html.py <폴더> nangman_<이름> --up` → html 원고(모양 그대로 · 「▼ 사진 NN」 · 숫자 카드 · 막대 · 비교 상자는 vis2img.py가 그림으로 바꿈) + txt + 사진(01 = 대표)을 드라이브 「블로그/협업/4_어사이드/원고」에. 지시 파일만 「4_어사이드」에 따로. 도우미 · 예약 큐 아티팩트는 쓰지 않음.
- 네이버 하루 2편 · 4시간 넘게 간격(낭만 부동산은 11:00 · 17:00).

## 낭만 인테리어 원고 → 어사이드 폴더 (11/5 23시 사용자 「도우미 만들지 말고 html하고 썸네일 · 시각화 · 사진 중심으로 폴더에」 · 「사진도 그냥 올릴 거야 · 창고 이용 안 하고」)
- 도우미 · Artifact 화면 · 낭만 창고 주소 쓰지 않는다. 원고 md(머리말에 `thumb: 꼬리표 | 이름1 | 이름2 | 앞말 | 핵심 | 설명`) → `python3 /home/claude/tools/postkit/md2aside.py <원고.md> --up` 한 번.
- 결과: 드라이브 「블로그/협업/4_어사이드/원고/<이름>/」에 <이름>.html(「▼ 사진 NN.jpg」 표시) + 01.jpg 썸네일(대표) + 02.jpg~ 본문 사진 · 표 그림(본문 순서). 어사이드가 사진을 네이버에 직접 올린다.
- 지시 파일은 「4_어사이드/지시_…txt」(번호 · 시각 · 카테고리 · 제목 · 폴더). 본문은 2,000자 넘게(꼬리 링크 빼고), 사진 · 표 그림 중심.
- 진단: 「4_어사이드/지시_인테리어_진단_1106.txt」 → 5_보고 「인테리어_진단_1106_보고」.

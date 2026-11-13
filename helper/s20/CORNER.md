# 낭만 부동산 요일 코너 원고 · 정기 작업 운영 문서 (2026-11-14 만듦)

사용자 지시: 11/13 22:01 「블로그 활성화 전략과 구체적인 수행 과제 · 방향 · 제목」 → 11/14 04:41 「응 만들고 챗지피티 검수 받아」(월 · 수 · 금 원고를 쓰는 정기 작업) · 04:47 「더 가 보자」.
이 문서는 프로젝트 문서 claude/낭만부동산_코너_정기작업_1114.md 와 저장소 helper/s20/CORNER.md 에 같은 내용으로 있다. 고치면 둘 다 고친다. 프롬프트와 부딪히면 이 문서가 이긴다.

정기 작업: 「낭만 부동산 요일 코너 원고 (월·수·금 05:13)」(trig_01GnqmCkLWKzGzebgYwSMUs2) — 한 번 뜰 때 ① 검수 결과 반영 → 「대기」 ② 다음 코너 글 한 편 쓰기 → 검수에 넣기 ③ 장부 · 현황. 사용자에게 묻지 않고 스스로 정한다. 사람만 할 수 있는 일(로그인 · 인증 · 결제 · 삭제)만 「사용자_확인필요」에 한 줄.

## 0. 시작 (매 실행)
1. `git clone --depth 1 https://github.com/nangmandosa801-cmd/nangman-work /home/claude/nangman-work`(있으면 pull) → `bash /home/claude/nangman-work/restore.sh`.
2. /home/claude/gas/conf.json 이 없으면 Google_Drive search_files(query: title = '우체통_conf.json') → read_file_content → `python3 /home/claude/helper/conf_fix.py '<읽은 글자>'` (내용은 어디에도 적지 않는다).
3. 1차 QA 도구: `mkdir -p /home/claude/kit_dasi && cd /home/claude/kit_dasi && python3 /home/claude/helper/gas.py fget "블로그/dosa/_tools/dasi" dasi_kit.tgz dasi_kit.tgz && tar xzf dasi_kit.tgz` (selfqa.py · 저장소에는 넣지 않는다).
4. 읽기: 프로젝트 문서 claude/낭만부동산_활성화전략_킬러콘텐츠_1113.md(5번 GEO 점검표 · 4번 덩어리 · 8번 달력) · claude/낭만부동산_새틀_코너_1112.md · claude/낭만부동산_블로그3곳_역할_1112.md. /home/claude/CLAUDE.md 의 「낭만 부동산 …」 절들. 점검표 `gas.py fget "블로그/협업/0_지시" 검수_점검표_자연스러움_1112.txt c.txt`(14항목 · 처음부터 이 기준으로 쓴다).
5. `python3 /home/claude/helper/s20/corner.py status` — 장부(helper/s20/corner_plan.json).

## 1. 검수 반영 (state 가 「검수중」인 글 전부 · 매 실행 먼저)
- 글마다 `cd /home/claude/helper/s20 && python3 corner.py result <slug>`
  - 결과가 왔다(exit 0) → `corner.py fix <slug>` → 출력의 skip 을 읽는다: 「mk.py 에 없거나 여러 번」은 mk.py 에서 그 문장을 찾아 손으로 고친다(뜻이 같은 범위에서 · 숫자 · 제목 · 소제목 · 「근거:」「출처:」「자료:」「규칙:」 줄은 그대로 · 고침이 사실을 바꾸거나 금지어를 넣으면 반영하지 않는다) → `corner.py build <slug>` 가 ok:true 가 될 때까지(ban 비어 있음 · related 3 · selfqa_fail 없음) → 아래 「내보내기」.
  - 결과가 없다(exit 3) + 넣은 지(submitted) 24시간이 넘었다 → 고치지 않고 「내보내기」(현황에 「검수 없이 넘김」).
  - 결과가 없다 + 24시간 안 → 그대로 둔다. 6시간이 넘었으면 「교신_챗지피티_클로드_<YYYYMMDD-HHMM>_독촉-검수_nangman_<slug>.txt」 여섯 줄(같은 글 하루 한 번).
  - 결과의 checklist 가 「자연스러움_1112」가 아니다(fix 가 exit 2) → 쓰지 않고 「…_다시검수_nangman_<slug>.txt」 교신(하루 한 번).
- 내보내기
  - 장부 mode 가 reedit 인 글(11/12 에 이미 예약 지시가 나간 hanam_cancel · detective_01 · hanam_monthly200 · budget_01 · hanam_renewal): 고친 문장이 한 곳이라도 있을 때만 `corner.py reedit <slug>`(글자만 다시 올리고 어사이드에 「본문 다시 채우기」 교신). 고친 것이 없거나 예약 시각이 4시간 안 남았으면 장부 state 만 「대기」로 바꾼다. 이 다섯 편은 `up`(사진까지)을 쓰지 않는다 — 대표 사진이 옛 그림으로 바뀐다.
  - 그 밖의 글: `corner.py up <slug> --end` → `corner.py ready <slug>`(지시 블록 「상태: 대기」 + 어사이드 교신). 예약 시각이 6시간 안 남았거나 이미 지났으면 `ready <slug> --when "<다음 날 같은 시각>"`(하루 2편 · 3시간 간격을 지킨다 · 장부 date 도 고친다). 그다음 `corner.py clip <slug>`(ChatGPT 클립 재료 · 이미 올렸으면 건너뜀).
- 킬러 1호 salary_map: 11/14 08시 ChatGPT 사실검수(0025 · 0624)를 반영해 제목을 「연봉별 대출한도, 연봉 1억도 변동금리면 4억 7천」으로 바꾸고 다시 검수에 넣었다. 11/13 원본(「6억은 못 빌립니다」)은 어디에도 내보내지 않는다. 지시 파일 「지시_부동산_킬러_연봉별대출한도_1113.txt」의 「상태:」 줄을 먼저 본다(`gas.py fget "블로그/협업/4_어사이드" <이름> j.txt`). 매시 교신 확인 작업이 이미 「대기」 · 「완료」로 바꿨으면 장부만 맞춘다. 아직 「검수중」이면 위 순서대로(`ready salary_map --when "<다음 빈 21:00>"`).
- 구글 표 페이지 글자(nangman_salary_table_blogger.gpt.json): helper/s20/salary_map/gblog.py 의 문장을 고치고 `python3 gblog.py --pub`.
- 예약 4시간 전이 지난 글은 손대지 않는다(원래 글이 나간다).
- 이 작업이 맡는 결과 파일(nangman_<장부의 slug>.gpt.json)은 「글 검수 관제」(07:13 · 11:13 · 17:13) 작업이 건드리지 않는다(claude/낭만도사_지난글_쉽게고치기_1112.md 에 적어 둠). 반영이 끝난 결과 json 과 대기 txt 는 「검수_자연스러움/결과/반영완료」에 fput 으로 복사한 뒤 Google_Drive 커넥터로 원본을 휴지통에(안 되면 그대로 둔다).

## 2. 새 글 쓰기 (한 실행에 한 편)
- 고르기: 장부에서 state 가 todo 인 것 가운데 날짜가 가장 이른 글. 「하남 이번 주」는 발행 이틀 전부터만 쓴다. 14일 넘게 남은 글은 쓰지 않는다. 쓸 글이 없으면 쓰지 않는다.
- 쓰기 전에 확인
  - 제목 맨 앞 말: `cd /home/claude && python3 -c "import ac;print(ac.ac('<말>'))"` — 자동완성에 뜨는 말만 제목 맨 앞에 둔다. 장부 kw 가 안 뜨면 뜨는 말로 바꾼다.
  - 겹침: 네이버 dong_jin_kim 최근 글 제목(TinyFish fetch_content 로 https://rss.blog.naver.com/dong_jin_kim.xml · WebFetch 와 셸 curl 은 쓰지 않는다)과 주제가 같으면 각도를 바꾼다. 분양가 · 청약 글은 쓰지 않는다(주 2편 한도는 다른 원고가 이미 씀).
  - 제미나이 숙제: `gas.py ls "블로그/리서치/딥리서치_1112"` 에 그 글 R번호 결과가 있으면 먼저 읽는다(없어도 쓴다).
  - 같이 보면 좋은 글 3개: 장부의 url 이 있는 같은 덩어리 글 먼저 · 없으면 salary_5000/mk.py 의 세 주소 · 인테리어(champion_chart · nangmaninterior) 링크 금지.
- 자료(확인한 숫자만 쓴다)
  - 실거래: `python3 /home/claude/tools/postkit/rtdata.py --from <석 달 전 YYYYMM> --to <이번 달>`(수도권 매매 → /home/claude/rtn/M_budget_sudo.pkl) · 하남만 `--sido 경기도 --sgg 하남시 --out …`, 전월세는 `--rent`. 실거래 탐정은 `python3 /home/claude/tools/postkit/odd_deals.py --from … --to … --fetch --out /tmp/odd.json`. 받기가 막히면 돌아가는 방법을 쓰지 않고 자료가 필요 없는 다음 글을 쓴다.
  - 제도 · 금리 숫자: WebSearch · WebFetch 로 기관 발표문이나 기사 원문을 다시 열어 본 것만. 못 연 숫자는 쓰지 않는다. 금리 · 스트레스 금리가 바뀌었으면 연봉 계산의 BASE · STRESS 를 그 값으로(그리고 salary_map/gblog.py --pub 로 한도표도).
  - 하남 이번 주: 하남시 고시 · 공고, 교통 보도(9호선 · 3호선 · 위례선), 그 주 하남 실거래 · 신고가 · 해제 → 「이번 주 하남에서 바뀐 것 3가지 + 그래서 내 집은」. 남의 사진 · 기사 사진은 쓰지 않는다.
- 만들기: `python3 corner.py new <slug>` → ana.py(계산 · 집계 → ana.json) · fig.py(2D 그림 3~5장 · fig2d 의 bars 는 막대 5개까지 · cards3 · 위에 결론 한 줄) · mk.py(본문 · 숫자 assert). **helper/s20/salary_5000 을 그대로 본뜬다**(허브 글은 salary_map).
- 글 기준(전략 문서 5번 + 점검표 14항목): 제목 = 자동완성 말 + 쉼표 + 숫자 하나 · 맨 위 30초 요약 3줄(SUM) · 뜻밖의 사실이나 한 건의 거래로 시작 · 소제목은 사람들이 묻는 말, 바로 아래 첫 문장이 답 · 표는 글자(TABLE) · 자주 묻는 질문 3개 · 근거 줄(NOTE)에 기관과 날짜 · 끝은 써먹을 한 가지와 다음 편 한 줄 · 「같이 보면 좋은 글」 딱 3개 · 쉬운 말 · 한 문장 70자 안 · 문단 5문장 안 · 「~입니다」만 줄줄이 쓰지 않기 · 「갈-」 · 「까닭」 · 「~고요」 · 글 쓰는 과정 문장 · 「오른다 · 내린다」 단정 · 사라 · 팔아라 권유 · 전화번호 · 홍보 상자 금지 · 「낭만 부동산 분석 플랫폼」으로 표기. 개별 거래는 단지 · 면적 · 층 · 계약 월 · 금액까지만.
- `corner.py thumb <slug> "낭만 부동산 · <코너> · <편>" "<검색어>" "<둘째 줄>" "<숫자 하나>" "<아래 한 줄>"` → `corner.py build <slug>` 가 ok:true 가 될 때까지 → /home/claude/w/aside_out/nangman_<slug>.txt 를 처음부터 끝까지 읽어 모순 · 표와 본문이 다른 곳 · 기계 같은 문장을 고친다 → 그림은 Read 로 한 번 본다(글자 잘림).
- 넘기기: `corner.py up <slug>` → `corner.py submit <slug>` → `corner.py block <slug> --when "<장부 날짜(요일) 시각>"` → 장부에 slug · title 적기(`plan_set` 이 하는 것 말고 date 칸의 todo 줄을 그 slug 로 바꾼다).
- 한 번 기다리기: 넣은 뒤 ChatGPT 의 다음 :20 검수가 지나도록(최대 40분 · `sleep`) 기다렸다가 `corner.py result <slug>` 를 한 번 본다. 왔으면 1번대로 반영하고 `ready` · `clip` 까지. 안 왔으면 다음 실행이 한다.

## 3. 장부 · 현황 (매 실행 끝)
- 어사이드 보고: `gas.py fget "블로그/협업/5_보고" 부동산_코너_보고.txt r.txt` 와 「부동산_킬러_연봉별대출한도_보고」에 발행 주소가 있으면 장부 url · state 「완료」. 허브 글(salary_map) 주소가 처음 생기면 ① salary_map/gblog.py 의 NAVER · NAVER_T 를 채워 `python3 gblog.py --pub` ② 아직 「대기」 전인 연봉 시리즈 글의 mk.py HUB 를 채워 build.
- todo 가 6편 아래로 남으면 전략 문서 4번 덩어리(H1 연봉 · H2 2027 제도 · H3 순위 · H4 하남 · H5 순서와 방법) 순서로 4주 치(월 · 수 · 금)를 장부에 더한다. kw 는 자동완성에서 확인한 말만.
- 5_보고 「부동산_코너_현황.txt」 덮어쓰기: `corner.py status` 표 + 오늘 한 일 + 막힌 것 + 스스로 정한 것. 5_보고 「부동산_주간통계.txt」가 있으면 발행 14일 지난 글의 조회수를 현황에 적는다.
- `SYNC_TRAILER` 없이 `bash /home/claude/nangman-work/sync.sh`.
- 끝 메시지는 세 줄(반영한 글 · 쓴 글 · 막힌 것). 막힌 일이 없으면 SendUserMessage 를 보내지 않는다.

## 4. 금지
네이버 · 티스토리 · 인스타 · 스레드에 직접 올리기(어사이드 · ChatGPT 몫) · 이미 걸린 예약 지우기 · 발행된 글 고치기 · 주소 지어내기 · 확인 못 한 숫자 · 인테리어 링크 · 전화번호 글자 · 3D 그림 · 발행 도우미 · 비밀번호나 열쇠 값을 적기 · send_later · fork 서브에이전트 · 한 실행에 두 편 넘게 쓰기 · 새 정기 작업 만들기. 사용자가 「그만」이라고 하면 이 예약을 끈다.

## 5. 기록
- 11/14 04:50 만듦. 같은 날 「연봉5천 대출가능금액, 2억 8,710만원으로 닿는 집」(salary_5000 · 11/25 수 17:00)을 쓰고 검수에 넣음. 11/16~11/20 다섯 편도 검수 대기에 넣음(mode reedit).
- 킬러 1호(salary_map)는 11/13 22:42 검수에 넣음 · 반영은 교신 확인 작업에 부탁해 둠.
- 11/26 금통위 당일 해설은 목요일이라 이 작업이 못 쓴다 → 11/27 「하남 이번 주」의 한 칸으로 넣는다(당일 한 번 도는 작업은 사용자 결정 전).
- 11/14 08시: ChatGPT 사실검수 반영 — salary_map · salary_5000 · 구글 표 페이지에 순수 고정금리 예외, 규제지역 생애최초 70% · 서민 · 실수요자 60%(세 요건), 2027 소득 20%→2년 · 30%→3년, 근거 날짜 8월 13일. 제목 · 숫자 결정은 Claude 몫(사용자 결정 대기로 올리지 않는다). 사실 지적이 오면 금융위 · 한국은행 · 은행연합회 원문을 다시 열어 확인하고 그 문장만 고친다.
- 다음 주 다섯 편(hanam_monthly200 · budget_01 등)에도 「생애최초가 아니면 40%」 문장이 있다 — 검수 반영 때 하남 · 규제지역 문장에 서민 · 실수요자 60% 요건(부부 합산 9천만원 이하 · 8억 이하 · 무주택 세대주)을 한 줄 더하고 근거 날짜 「8월 14일」을 「8월 13일」로(reedit). 그 글 폴더는 helper/s20/<slug>/ (mk.py 가 없으면 txt · html 만 고쳐 reedit).
- corner.py result 는 「결과」에 없으면 「결과/반영완료」도 본다(다른 작업이 먼저 옮긴 경우).

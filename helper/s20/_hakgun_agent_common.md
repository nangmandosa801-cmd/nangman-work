# 학군지 연재 N화 · 에이전트 공통 지시 (11/6)
1. 먼저 읽기: /home/claude/helper/BRIEF_1103.md, /home/claude/helper/BRIEF_1105_add.md (「학군지 아파트 연재」 · 「추가 자료」 절), 원문 /home/claude/helper/s20/_hakgun_report.txt 에서 자기 화 부분만, 본보기 폴더 /home/claude/helper/s20/mokdong_school (kit.py · tails.py · fig.py · mk.py · 만화_콘티.md 구조를 그대로 따른다; kit.py · tails.py 는 /home/claude/helper/pg/ 에서 복사).
2. 자료: /home/claude/rtn/M2025.pkl · M2026.pkl(매매) · R2026.pkl(전월세) · rawK/MK_2021_2026.pkl · RK_2024_2026.pkl(강남 서초 양천 노원) · rawS/M2021_2024_seoul.pkl. 경기 2021~2024 매매 · 2024~2025 전월세가 필요하면 /home/claude/rtn/dl_hakgun.py 를 본떠(sidoNm '경기도' · srhSidoCd '41000' · sggNm 은 rt.molit 시군구 목록 그대로, 예 '성남분당구' 형식인지 먼저 확인) /home/claude/rtn/rawG/ 에 받고 /home/claude/rtn/load.py 의 load() 로 pkl(저장소 밖, 2MB 넘으면 .gitignore 확인). 필터: 해제사유발생일 '-' · 직거래 제외 · 전용 83~86(보고서가 다른 평형을 말하면 그 평형도) · 중앙값 · 단지명 정확히 일치(공백 제거). 보고서 숫자는 옮겨 적지 않고 우리 실거래로 다시 잰다. 학교 배정 · 학원가 사실은 웹 검색으로 확인하고 못 찾으면 「확인 안 됨」으로 쓴다. 보고서 오류는 따르지 않는다.
3. 제목: 자동완성 앞머리 실측 `cd /home/claude && python3 -c "import ac;print(ac.ac('○○ 아파트 시세'))"` + 숫자 하나. 머리줄 「낭만 부동산 분석 플랫폼 · 학군지 아파트 N화」.
4. 글 끝(인터뷰 상자 앞) 「연재 순서」 표 17화(자기 화 굵게, 지난 화는 제목 글자만: 1화 「학군지 아파트, 2021 고점 대비 덜 빠진 곳은 넷 중 둘」 · 2화 「대치동 아파트 시세, 84㎡ 매매 중앙값 37억」 · 3화 「목동 아파트 시세, 앞단지 뒷단지 차이 1억 8,500만」 · 4화 「반포 아파트 시세, 래미안원베일리 84㎡ 58억 7,500에 전세는 21억」, 그 뒤 화는 예정 글자) + 「다음 화는 12월 ○일, …」. 전체 순서와 날짜는 BRIEF_1105_add.md 의 17화 줄(12/12 1화 … 매일 11:00).
5. 만들기: fig.py → `python3 /home/claude/helper/gas.py image <png>` → urls.json → mk.py(TITLE=) → `python3 /home/claude/helper/make_helper.py . --skip-fig` 금지어 0 → `python3 /home/claude/tools/postkit/html2aside.py <폴더> nangman_<slug> --up` 와 `python3 /home/claude/tools/postkit/html2aside_html.py <폴더> nangman_<slug> --up` → 만화_콘티.md(6컷+7컷 링크 카드, 본보기 그대로) → `bash /home/claude/nangman-work/sync.sh`. 지시 파일은 만들지 않는다(주 대화가 만든다).
6. 쉬운 말 · 2,000자 넘게 · 지어내지 않기 · 매물 광고 없음 · 연락처는 kit 의 것만 · 본문 2,000자 넘게. 끝나면 JSON 몇 줄만: slug · 제목 · 금지어 · 드라이브(html txt 사진 수) · 못 한 것.

# 11/12 추가 규칙 (9~17화 · 위 내용보다 우선)
- 본보기 폴더는 /home/claude/helper/s20/gwanggyo_school (8화). tails.py 는 /home/claude/helper/pg/tails.py 최신판(낭만 인테리어 상자 · 링크 없음). mk.py 에 champion_chart 링크 · #낭만인테리어 태그를 쓰지 않는다.
- 그림: /home/claude/helper/pg/fig2d.py(bars · cards3 — /home/claude/tools/tistory/viz2d.py 를 부름)만 쓴다. 3D · 겹침 · 장식 금지, 2D 막대 최대 5개 + 막대 위 숫자 + 강조 1개만 파랑 + 그림 맨 위 결론 한 줄. 비교가 5개 넘으면 본문 표 + 숫자 카드 3개. 선 그래프 쓰지 않는다. 글마다 그림 2장 + thumb(썸네일은 본보기 fig.py 의 thumb 방식 그대로).
- 글: 첫 문장은 뜻밖의 사실 하나(숫자). 「그래서 집 사려는 · 전세 구하는 사람에게 무슨 일인가」를 먼저. 숫자는 한 문단에 하나, 비교는 둘만 짝으로. 끝은 요약 대신 써먹을 한 가지. 제도 · 학군 소개 나열 문단은 쓰지 않는다. 본문 2,000~3,000자. 제목은 「자동완성 검색어, 숫자 하나」 한 줄(괄호 · 가운뎃점 나열 없음).
- 지방 · 인천 · 경기 실거래: rt.molit 에서 받는다. 본보기 스크립트 /home/claude/rtn/dl_bundang.py · dl_gtx.py (sidoNm · srhSidoCd · sggNm · srhSggCd 는 rt.molit 시군구 목록에서 실측 확인). 매매 2021~2026(1~10월), 전월세 2024~2026 을 /home/claude/rtn/rawG/ 에 받고 pkl 은 /home/claude/rtn/ (저장소 밖). 2025 · 2026 이 /home/claude/rtn/M2025.pkl · M2026.pkl · R2026.pkl 에 그 지역 행으로 이미 있으면 그것을 쓴다(없으면 받는다).
- 연재 순서 표의 지난 화 제목: 5화 「중계동 아파트 시세, 을지초 배정 청구3차 84㎡ 13억 6,000만」 · 6화 「분당 아파트 시세, 소형 평당 1억 1,100만은 큰 평형의 2배」 · 7화 「평촌 학원가 아파트, 같은 현대홈타운인데 차이 6억 8,500만」 · 8화 「광교 자연앤힐스테이트, 84㎡ 18억 7천은 2021년보다 23% 위」. 9화 뒤 화는 「예정」 글자.
- 여러 에이전트가 동시에 돈다: 자기 폴더와 자기 지역 파일만 건드리고, sync.sh 가 충돌하면 30초 뒤 한 번 더.

# 11/12 00:43 추가 (사용자 「제목과 내용 SEO · GEO 최적화, 질문과 그에 대한 응답 스타일, 자동완성 제목으로」)
- 제목: 네이버 자동완성에 실제로 뜨는 검색어를 맨 앞에 그대로 + 쉼표 + 숫자 하나(실측 필수 · 안 뜨는 말은 앞머리로 쓰지 않음).
- 소제목은 전부 사람들이 실제로 묻는 질문 문장(자동완성 · 연관 검색어에서 고름, 예 「중계동 아파트 전세, 겨울에 더 비싼가요?」). 소제목 바로 아래 첫 문장이 그 질문의 답(숫자 포함 한두 문장, 그 문장만 떼어 읽어도 뜻이 통하게 주어 · 지역 · 시점을 다 적음 — AI 검색이 인용하기 좋게). 그 뒤에 근거 · 표.
- 글 맨 위 인사 다음 두 문장도 제목 질문에 대한 답. 글 끝쪽에 「자주 묻는 질문」 3개(질문 + 두 문장 답, 본문 반복이 아니라 본문에서 안 다룬 옆 질문). 태그도 실측 검색어.
- NOTE(출처 · 기준 시점 · 필터)는 그대로 둔다 — 출처와 날짜가 분명해야 인용된다.

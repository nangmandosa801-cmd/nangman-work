# 낭만 부동산 분석 플랫폼 새 글 · 공통 지시 (11/3)

목표: 네이버 blog.naver.com/dong_jin_kim 하루 조회 1,000 회복. 검색으로 들어오는 글 + 낭만 인테리어(champion_chart) 발행 글로 독자를 보내는 「인테리어 부스팅」.

## 만드는 것
- 폴더 /home/claude/helper/<폴더>/ 에 kit.py · tails.py 를 /home/claude/helper/pg/ 에서 복사하고, kit.py 의 'nangman_paragon3_' 를 'nangman_<슬러그>_' 로 바꾼다.
- fig.py: 그래프 1~2장(img/nangman_<슬러그>_1_xxx.png) + 썸네일(img/nangman_<슬러그>_thumb.png). /home/claude/helper/pg/fig.py 형식 그대로(남색 #1F3864 · 파랑 #2E5C8A · 회색 #A9B4C2만, 썸네일 1000×1000 남색 바탕 C형: 조건 하나 크게). 그래프 안 글자에도 금지어 쓰지 않는다.
- mk.py: /home/claude/helper/pg/mk.py 형식(TITLE · 머리줄 · 인사 · 결론 숫자 먼저 · FIGS · H 소제목 질문형 · TABLE · NOTE 자료 · interview(해당 지역 중개사무소 인터뷰) · related(낭만 부동산 글 5개 이상) · platform() · side(낭만 인테리어 글 3개) · tags).
- urls.json 은 만들지 않는다(그림 창고 올리기는 메인이 함). `python3 fig.py && python3 ../make_helper.py . --skip-fig` 로 금지어 0을 확인한다.

## 제목 · 키워드
- 제목 = 「네이버 자동완성 검색어, 숫자 하나」. 짧게(30자 안팎). `cd /home/claude && python3 -c "import ac;print(ac.ac('검색어'))"` 로 실측해 고른다.
- 같은 검색어를 첫 문단 첫 문장, 소제목 2~3개, 태그 10~13개(자동완성 문구 포함, 마지막 #낭만부동산)에 넣는다.

## 문장 규칙 (어기면 다시 씀)
- 아주 쉽게. 어려운 말 대신 일상어. 문장 짧게, 「~다」로 끊는다. 「~고」로 길게 잇지 않는다. 「~고요」 금지.
- 금지어: 자리 · 갈-(갈렸다 · 갈라 등) · 어요 · 예요 · 고요 · 최고 · 프리미엄 · 가능성 · 헷갈 · 놓습니다 · 가정 · 까닭 · 견줘 · %p · 나갈 · 1위 · 봤습니다 · 셌습니다. 「최고」 대신 「가장 높은」.
- 글 쓰는 과정 · 의식의 흐름 문장 금지(「먼저 하나를 바로잡고」 같은 말). 사실과 숫자만.
- 숫자는 실거래 데이터(/home/claude/rtn/M2026.pkl 매매 · R2026.pkl 전월세, 컬럼은 한글, 해제 거래 뺌)나 공식 공고 · 기사(WebSearch/WebFetch)로 확인한 것만. 지어내지 않는다. 출처는 NOTE에.
- 표기 「낭만 부동산 분석 플랫폼」. 전화 010-2882-8165만. 매수 · 매도 권유 금지. 할인 숫자 금지.
- 「본문을 반복하는 요약표」를 끝에 넣지 않는다.

## 링크
- 낭만 부동산 글 목록: `cd /home/claude/spread && python3 -c "from fetch import page; [print(p['logNo'],p['title']) for n in range(1,12) for p in page(n)]"`
- 낭만 인테리어 발행 글 목록: `curl -s -A Mozilla/5.0 "https://blog.naver.com/PostTitleListAsync.naver?blogId=champion_chart&currentPage=1&countPerPage=30"` (currentPage 1~6, 제목은 URL 인코딩 → urllib.parse.unquote_plus).
- 본문 중간에도 인테리어 글로 가는 상자 1개(pg/mk.py 의 「임대 10년 뒤까지…」 상자 형식) — 이 글 주제와 실제로 이어지는 인테리어 글로(입주 · 이사 · 수리 · 중문 · 청소 등).

## 끝나면
최종 답: 폴더 · 제목 · 그림 파일 이름 · 금지어 결과 · 쓴 데이터/출처 한 줄씩. 아티팩트 게시 · 블로거 업로드 · 발행은 하지 않는다.

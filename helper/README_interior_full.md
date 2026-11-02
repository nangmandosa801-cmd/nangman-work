# 낭만 인테리어 · 본문 전체 복사 도우미 (gen_full.py)

생성기: /tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad/h1024/gen_full.py
(gen.py 는 그대로 둔다. gen_full.py 는 같은 원고 · 같은 태그 규칙을 쓰는 별도 생성기.)

## 한 글에 적용하는 순서
1. 그림 목록: 원고 `/mnt/user-data/outputs/int/<slug>/nangman_interior_<slug>_post.html` 안의 그림 이름 중 `_thumb` 를 뺀 것.
2. 창고에 올리기: 낭만 창고 블로거(ID 3521924271702627135, nangmandosa801, Chrome)에서 새 글 「[창고] <slug> 그림」 → 파일 넣기 → 편집기 iframe 에 drop → `blogger.googleusercontent.com/…/s1600/<파일이름>` 주소 모음. 글은 발행하지 않고 임시 저장으로 둔다.
3. 주소 표 만들기: `{"<파일이름>": "<창고 주소>", ...}` JSON (예: h1024/changgo_<slug>.json).
4. 만들기:
   `python3 gen_full.py <slug> "<제목>" "<예약 시각>" "<짧은 이름>" h1024/changgo_<slug>.json`
   → `h1024/naver_paste_<slug>_full.html`. 주소가 빠진 그림이 있으면 멈춘다.
5. 확인: 창고 주소마다 `curl -sI` 200 + image/*; Playwright 로 「본문 전체 복사」 HTML 에 <img> 수 = 그림 수, `_thumb` 없음.
6. 게시: 그 글 도우미의 기존 artifact 주소에 `capabilities={"downloads": true}` 로 다시 게시 (먼저 read 해서 살아 있는 쪽 변경을 합친다).

## 바뀌는 점 (사용자 쪽)
- 본문은 「본문 전체 복사」 한 번 → 네이버에 Ctrl+V 한 번. 글 · 표 · 상자 · 그림이 같이 들어간다.
- 썸네일은 본문에 없다. 「썸네일 내려받기」(또는 PC 폴더 _thumb) 를 사진으로 올리고 대표로 지정.

## 처리 규칙
- 점선(`border:1px dashed`) 그림 자리 표만 바꾼다. 다른 표 · 상자는 그대로.
- `_thumb` 자리는 표와 바로 뒤 빈 줄까지 지운다.

## 파일럿 기록 (10/24)
- 창문 단열시트: 창고 임시글 「[창고] changmun_danyeol_sheet 그림」(글 ID 5021659978265295780), 그림 13장, 주소표 h1024/changgo_changmun_danyeol_sheet.json → 도우미 PVUwHifjXfqasgmovrVgxP 3판.
- 창고에 쓸 브라우저: Browser 3 (4dc8f8cb…). Browser 2 (71fb172a…)는 「This site is blocked.」
- file_upload 는 /mnt/user-data/outputs 경로를 거부함 → 작업 폴더(/home/claude/watch/…)에 잠깐 복사해 올리고 지움.
- Artifact 화면에서는 바깥 그림이 막혀 미리 보기에 빈칸으로 보임. 복사 HTML 에는 주소가 그대로 들어가니 정상.

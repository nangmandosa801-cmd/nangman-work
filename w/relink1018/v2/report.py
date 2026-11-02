import json,re,os,collections
sel=json.load(open('/home/claude/w/relink1018_files.json'))
L1={x['file']:x for x in json.load(open('/home/claude/w/relink1018/log.json'))}
L2={x['file']:x for x in json.load(open('/home/claude/w/relink1018/v2/log2.json'))}
CK={x['file']:x for x in json.load(open('/home/claude/w/relink1018/v2/check2.json'))}
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
CASE_NO_NI=set('busan_danggam donam_hansin daejeon_dure changwon_daewon cheongju_jiwell sejong_surubae arch_pocheon pocket_jinju busan_sasang changwon_gamgye living_suwon dress_cheonan suwon_narrow bronze_gimhae moru_yangsan six_seoul auto3_okjeong gabyeok_tongyeong jubang_jinhae anbang_saha wood3_daeyeon pocket_gimhae auto_okjeong slim3_onam asym_wolgye swing_onam house_macheon veranda_masan dress_gimhae villa_sash sash_live sink_film door_film room_film frame_film suwon_gansal incheon_gompangi'.split())
NOTE={
'bangchungmang_cat':['문의 문장 없음 — 방충망 시공을 어느 지역에 연결하는지 정해 주셔야 넣을 수 있음','끝 「정리」 단락이 본문을 되풀이함(뺄지 판단)','본문에 [썸네일] 칸이 남아 있음','발행 글 「방충망 교체, 같은 망으로 바꾸면 또 뜯습니다」(224426986850)와 주제가 거의 같음'],
'bangmyochang':['문의 문장 없음 — 방묘창 시공을 어느 지역에 연결하는지 정해 주셔야 넣을 수 있음','끝 「정리」 단락이 본문을 되풀이함(뺄지 판단)','본문에 [썸네일] 칸이 남아 있음','제목 앞머리 「방묘창 설치,」가 발행 글 224422997793과 같음'],
'jungmun_mutagong':['끝 「정리」 표가 본문 숫자를 되풀이함(뺄지 판단)','제목 앞머리 「무타공 중문,」이 발행 글 224424176442와 같음','숫자(시공 945건 · 수리 291건 · 38%)는 남양주·구리 업체 글 집계 — 다시 확인 못 함'],
'saejip_jeunghugun':['원본 글(post.html)에는 사진 번호 NI- 10개가 있는데 붙여넣기본에는 번호와 「이 사진처럼 하고 싶다면」 상자가 없음','문의 문장 「다른 지역도 가까운 업체를 연결해 드립니다」 — 어느 지역부터인지 빠져 있음(연결 지역 확인 필요)'],
'solar1':['표 「서울 관악구 … 10월 26일까지 서류 제출」 — 11-10 발행 때는 지난 마감','「서울시가 올해 다시 시작한 사업도 목표 500가구에 172가구만」 숫자 확인 필요','자료 줄 없음'],
'sash_grade':['태그에 낭만 부동산 시절 태그(#낭만부동산 · #인테리어견적 · #아파트인테리어)가 섞여 있음','제목 앞 <!-- 제목 --> 줄 없음'],
'hwajeong_interior':['본문 안 낭만 부동산 분석 플랫폼 링크 1개(dong_jin_kim/224422066734) — 살아 있는지 확인 못 함'],
'incheon_gompangi':['문의 지역에서 「부천」을 뺐음(금지어) — 실제로 부천도 연결하는지 확인 필요'],
'door_film':['자료 줄의 금액 출처 「인테리어 필름 시공 가격」 글은 지워진 글(224430339313) — 금액 출처 다시 확인 필요'],
'room_film':['자료 줄의 금액 출처 「인테리어 필름 시공 가격」 글은 지워진 글(224430339313) — 금액 출처 다시 확인 필요'],
'frame_film':['자료 줄의 금액 출처 「인테리어 필름 시공 가격」 글은 지워진 글(224430339313) — 금액 출처 다시 확인 필요'],
'jungmun_swing':['제목 앞머리 「스윙 중문,」이 11-21 16시 글과 같음'],
'swing_onam':['제목 앞머리 「스윙 중문,」이 11-10 16시 글과 같음'],
'upche':['제목을 바꿨음(「값이 다른 까닭이」→「가격이 다른 이유가」) — 네이버 제목 칸에도 새 제목으로 넣을 것 · PC 폴더 이름은 그대로'],
'gyeonjeok_bigyo':['제목 앞머리 「인테리어 견적 비교,」가 발행 글 「인테리어 견적 비교 사이트,」(224444906311)와 겹침'],
'jungmun_auto':['제목 앞머리 「자동 중문,」과 11-20 16시 「자동 중문 설치,」가 비슷함'],
}
def nobanner(s):
    p=O+s if os.path.exists(O+s) else B+s; return '[배너]' not in open(p).read()
def nosrc(s):
    p=O+s if os.path.exists(O+s) else B+s; return '>자료 ·' not in open(p).read()
def nomid(s):
    p=O+s if os.path.exists(O+s) else B+s; h=open(p).read(); k=h.find('같이 보면 좋은 글'); return not re.search(r'champion_chart/\d+',h[:k])
def short(c):
    if c.startswith('문장: '):
        a,_,b=c[4:].partition(' → '); return f'「{a.strip()}…」 고침'
    return c
cnt=collections.Counter(); rows=[]; listed=[]
for s in sel:
    sl=os.path.basename(s)[17:-11]; folder=s.split('/')[0][len('[미발행] '):len('[미발행] 11-01 08시')]
    c1=L1[s]['changes'] if L1[s]['changed'] else []; c2=L2[s]['changes']
    ASKS=('입주청소 시공팀을','사는 지역과 연락처를 비밀댓글로','로프를 타고','댓글이나 쪽지로')
    for c in c2:
        m=re.search(r'(\d+)(?:곳|편)',c); n=int(m.group(1)) if m and c.startswith(('꼬리 첫','「~십시오','문의 상자')) else 1
        if c.startswith('머리 수수료'): k='머리 수수료 고지 넣음'
        elif c.startswith('문장') and any(a in c for a in ASKS): k='문의 문장 고침'
        elif c.startswith('문장') and ('「방묘' in c or '「단열' in c): k='본문 「제목」에 링크 걸기'
        elif c.startswith('문장') and '낭만 부동산 분석 플랫폼 ·' in c: k='머리 꼬리표 고침'
        elif c.startswith('문의 상자'): k='「업체가 · 업체는」 주어 고침'
        elif c.startswith('문장') and re.search(r'업체[가는]',c.split('→')[0]): k='「업체가 · 업체는」 주어 고침'
        elif c.startswith('문장'): k='금지어 고침'
        elif c.startswith('「~십시오'): k='「~십시오」→「~세요」'
        elif c.startswith('링크 글자'): k='링크 글자를 발행 제목으로'
        elif c.startswith('꼬리 첫'): k='꼬리에 첫 화면 밖 글 더함'
        elif c.startswith('꼬리 묶음'): k='꼬리 묶음을 태그 앞으로'
        elif c.startswith('낭만 부동산'): k='다른 블로그 꼬리 목록 뺌'
        else: k='기타'
        cnt[k]+=n
    left=list(NOTE.get(sl,[]))
    if sl in CASE_NO_NI: left.append('사례 사진에 NI 번호 · 「이 사진처럼 하고 싶다면」 상자 없음(그림 작업)')
    if nobanner(s): left.append('끝 [배너] 칸(연락처 그림) 없음')
    if nosrc(s) and sl not in('solar1',): left.append('자료(출처) 줄 없음')
    if nomid(s): left.append('본문 중간 링크 0개(넣을 문장 판단 필요)')
    for x in left: listed.append((folder,sl,x))
    t1=collections.Counter(('발행 예정→발행 글' if x.startswith('예정') else '#→발행 글' if x.startswith('#') else x) for x in c1)
    d1=('1차: '+', '.join(f'{a} {b}곳' if b>1 else a for a,b in t1.items())) if c1 else ''
    d2='; '.join(short(x) for x in c2)
    rows.append((folder,sl,' / '.join(x for x in [d1,d2] if x) or '—',' · '.join(left) or '—'))
# ── 쓰기
o=[]
o.append('# 낭만 인테리어 미발행 75편 2차 현행화 (2026-10-18)\n')
o.append('원본: `/mnt/user-data/uploads/블로그/interior/` · 결과: `/mnt/user-data/outputs/relink1018/<같은 상대 경로>` (1차 30편 포함 58편) · 바뀐 파일 목록: `/home/claude/w/relink1018/changed2.json` · 스크립트: `/home/claude/w/relink1018/v2/fix2.py` · 점검: `/home/claude/w/relink1018/v2/check2.py`\n')
o.append('## ① 「지금 기준」 — 10/16 · 10/17 새 글(n1016 · n1017 · gyeonjeok_site · changmun_nusu_haegyeol)과 옛 글을 견준 차이\n')
STD=[('머리 수수료 고지','제목 위 「이 글은 낭만 인테리어가 씁니다. … 소개 수수료로 받습니다.」 한 줄(회색 띠). 옛 글 17편에 없었음','고침'),
('머리 꼬리표','「낭만 인테리어 · (검색어)」. 샷시 등급 글은 「낭만 부동산 분석 플랫폼 · 인테리어」로 남아 있었음','고침'),
('문의 상자','「(대상)을 알아보고 있다면」 + ▸ 세 줄 + 「사는 지역과 연락처를 비밀댓글로 남겨 주세요. (지역)은 (품목) 업체/시공팀을 연결해 드립니다.」 + 그 글만의 한 줄 · 입주청소는 지역 없이 · 「이어 드립니다」 쓰지 않음','고침(문의 문장 없는 2편은 목록)'),
('「업체가 · 업체는」 주어 금지','시공팀이 · 곳이 · 청소팀이로(머리 · 끝 수수료 고지만 예외)','고침'),
('금지어','자리 · 갈- · 어요 · 예요 · 고요 · 최고 · 프리미엄 · 가능성 · 헷갈 · 놓습니다 · 가정 · 까닭 · 견줘 · %p · 나갈 · 값 · 기준 · 부천 · 차례로 · 1위 (자료 줄 · 발행 글 제목 링크는 제외)','고침'),
('말투','「~세요 · ~습니다 · ~죠」. 옛 글의 「~십시오」 없음','고침'),
('마무리','본문을 되풀이하는 「정리」 단락 · 표 없이 질문 한 줄 → 문의 상자 → 자료 줄로 끝','목록(3편)'),
('사진 번호','사례 사진마다 NI- 번호 + 사례 뒤 「이 사진처럼 하고 싶다면」 상자(번호 · 견적서 대조 · 거절 대행 · 공동구매) + 묶음 할인 그림','목록(그림 작업)'),
('그림 칸','끝 [배너] 칸(010-7678-9967 연락처 그림) · 썸네일은 본문에 넣지 않고 따로','목록'),
('자료 줄','「자료 · …」 출처 한 줄(업체 이름 대신 「제휴 시공팀」 · 날짜)','목록(없는 글)'),
('본문 링크','본문 중간 「제목」 링크 1~2개 이상 · 링크 글자는 발행 제목 그대로','제목 맞춤 · 「제목」만 있던 3곳 링크 걸기 · 0개인 글은 목록'),
('꼬리 링크','「같이 보면 좋은 글」 5편 이상 · 2편은 tail_boost(검색 첫 화면 밖) 같은 품목 → 이웃 품목 · 같은 글은 이번 작업에서 3번까지 · 새 글은 카드형(links.section)','고침(옛 모양은 그대로 따름)'),
('꼬리 위치','꼬리 묶음 → 태그 순(꼬리가 태그 아래로 붙은 글 있었음) · 다른 블로그 꼬리 목록 없음','고침'),
('연락처','글 안 번호는 010-7678-9967만(배너 그림 · 010-2882-8165는 중개사 전용)','확인: 75편 본문에 전화번호 0개'),
('남은 표시','「발행 예정」 · 「(예정)」 · 「준비 중」 없음 · 지난 날짜를 앞날처럼 쓰지 않음','확인: 0 · 날짜 1건 목록'),
('제목 줄','맨 위 <!-- 제목: --> 줄 · 「검색어, 나머지 문장」','옛 글 일부 주석 줄 없음(붙여넣기에 영향 없음)')]
o.append('| 항목 | 지금 기준 | 이번 처리 |\n|---|---|---|')
for a,b,c in STD: o.append(f'| {a} | {b} | {c} |')
o.append('\n## ② 75편 표\n')
o.append('점검 결과(75편 모두): 죽은 링크 0 · 「발행 예정」 0 · 꼬리 5편 이상 75/75 · 첫 화면 밖 글 2편 이상 75/75 · 금지어 0 · 본문 전화번호 0(배너 그림은 010-7678-9967) · 문의 문장 73/75 · 「이어 드립니다」 0\n')
o.append('| 폴더 | 글(slug) | 꼬리 | 고친 것 | 남은 것 |\n|---|---|---|---|---|')
for (f,sl,d,l),s in zip(rows,sel):
    ck=CK[s]; o.append(f"| {f} | {sl} | {ck['tail']}편(밖 {ck['tb']}) | {d} | {l} |")
o.append('\n## ③ 목록에만 적은 것(고치지 않음)\n')
grp=collections.defaultdict(list)
for f,sl,x in listed: grp[x if x.startswith(('사례 사진에 NI','끝 [배너]','자료(출처)','본문 중간 링크')) else '__'].append((f,sl,x))
for f,sl,x in grp['__']: o.append(f'- {f} {sl} — {x}')
for k in ['사례 사진에 NI 번호 · 「이 사진처럼 하고 싶다면」 상자 없음(그림 작업)','끝 [배너] 칸(연락처 그림) 없음','자료(출처) 줄 없음','본문 중간 링크 0개(넣을 문장 판단 필요)']:
    if grp[k]: o.append(f'- {k} ({len(grp[k])}편): '+', '.join(f'{f[:5]} {sl}' for f,sl,_ in grp[k]))
o.append('\n## 건수(2차)\n')
for k,v in cnt.most_common(): o.append(f'- {k}: {v}')
o.append(f"\n- tail_boost 사용 기록: `/home/claude/watch/tailboost/tail_boost.json` used · used_by 「2026-10-18 미발행 75편 현행화」(백업 `/home/claude/w/relink1018/v2/tail_boost.bak1018.json`)")
open('/home/claude/w/relink1018/report2.md','w').write('\n'.join(o)+'\n')
print(cnt); print(len(listed))

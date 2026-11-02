import sys,json,re
sys.path.insert(0,'/home/claude/int/mp4_1015')
import clipinfo
D='/mnt/user-data/outputs/int/clip_sigong/'
T=json.load(open('/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad/int_pub.json'))
title={n:t for n,t,d in T}
BAN=['갈','값','자리','어요','예요','고요','최고','프리미엄','기준','헷갈']
J=[ # slug, spec, post no, 이름, caption, 자료
('mutagong_3yeondong','mutagong_3yeondong','224454664991','무타공 3연동 중문',
 '무타공 3연동 중문은 30평대 현관 75만~80만원, 나사 대신 실리콘으로 붙입니다 #무타공중문 #무타공3연동 #3연동중문가격 #전세중문 #낭만인테리어',
 '금액은 제휴 중문팀 안내 금액(30평대 아파트 현관 기준) · 시공 사진은 제휴 업체 사례(NI 번호)'),
('hyeongwan_mutagong','hyeongwan_mutagong','224454576114','현관 무타공 중문',
 '현관 무타공 중문, 셀프는 4만~7만원대 기둥식 시공은 폭 90cm에 25만~37만원 #현관무타공중문 #무타공중문가격 #무타공중문 #전세중문 #낭만인테리어',
 '금액은 10월 26일 확인한 공개 금액 · 시공 사진은 제휴 업체 사례(NI 번호)'),
('gucuk_sunseo','gucuk_sunseo','224453417329','구축 아파트 인테리어 순서',
 '구축 아파트 인테리어 순서, 안 뜯는 집은 누수부터 청소까지 일곱 단계 #구축아파트인테리어 #구축인테리어순서 #누수탐지 #입주청소 #낭만인테리어',
 '매매 숫자는 국토교통부 실거래가 2026년 8~9월 계약분 · 시공 사진은 제휴 업체 사례(NI 번호)'),
('bucheon_interior','bucheon_interior','224453424377','부천 인테리어',
 '부천 중동 · 상동 구축 593집, 30년 된 집은 배관부터 봅니다 #부천인테리어 #부천구축아파트 #중동인테리어 #상동인테리어 #낭만인테리어',
 '매매 숫자는 국토교통부 실거래가 2026년 8~9월 계약분 · 시공 사진은 제휴 업체 사례(NI 번호)'),
('doorlock_songpa','doorlock_songpa','224452931534','송파 도어락',
 '송파 다섯 집이 지문 · 번호 · 보조형 도어락을 고른 이유 #현관도어락 #도어락추천 #송파도어락 #지문도어락 #낭만인테리어',
 '시공 사진은 제휴 업체 사례(NI 번호)'),
('doorlock_uijeongbu','doorlock_uijeongbu','224452893456','도어락 교체',
 '도어락 교체는 이사 온 날 번호부터 바꾸고 옛 구멍은 보강판으로 덮습니다 #도어락교체 #현관도어락 #의정부도어락 #푸시풀도어락 #낭만인테리어',
 '시공 사진은 제휴 업체 사례(NI 번호)'),
('brain5bl_jungmun','brain5bl_jungmun','224453190862','브레인시티 사전점검',
 '브레인시티 대광로제비앙 사전점검 10월 30일~11월 1일, 중문은 줄자와 사진 두 장 #브레인시티 #평택입주 #사전점검 #중문 #낭만인테리어',
 '사전점검 날짜 · 세대수는 발행 글 기재 · 중문 사진은 제휴 업체 사례(NI 번호)'),
('geomdan_hoban3_jungmun','hoban3','224444950674','검단 호반써밋3차 중문',
 '검단 호반써밋3차 옵션 중문은 84B만 여닫이 160만원, 기본형은 중문 미설치 #검단호반써밋3차 #검단중문 #여닫이중문 #입주중문 #낭만인테리어',
 '입주 정보 · 옵션 가격은 입주자모집공고 · 시공 사진은 제휴 업체 사례(NI 번호)'),
('hwayang_dongmun_cheongso','hwayang_dongmun_cheongso','224448297578','평택 화양 입주청소',
 '평택화양동문디이스트 입주청소, 열쇠 받은 뒤 줄눈 다음 날에 잡습니다 #평택입주청소 #화양동문디이스트 #입주청소 #줄눈 #낭만인테리어',
 '입주 정보는 모집공고 · 시공 사진은 제휴 업체 사례(NI 번호)'),
('deungchon_ipju_bakeout','deungchon_ipju_bakeout','224448376944','힐스테이트 등촌역 입주',
 '힐스테이트 등촌역 입주, 청소 뒤 33도로 8시간 데우고 환기를 세 번 합니다 #힐스테이트등촌역 #등촌역입주 #입주청소 #베이크아웃 #낭만인테리어',
 '입주 정보는 모집공고 · 베이크아웃은 서울시보건환경연구원 2026년 2월 조사 · 시공 사진은 제휴 업체 사례(NI 번호)'),
]
only=sys.argv[1:]
for slug,sp,no,name,cap,src in J:
    if only and slug not in only: continue
    assert not any(w in re.sub(r'#\S+','',cap) or w in cap for w in BAN),(slug,[w for w in BAN if w in cap])
    s=json.load(open(f'/home/claude/int/mp4_1015/spec_{sp}_v.json'))
    sc=[x['kicker']+' · '+x['line'].replace('\n',' ') for x in s['vintro']]+[x['line'].replace('\n',' ') for x in s['slides']]
    sc.append('문의 010-2882-8165')
    clipinfo.make(slug,name,cap,f'https://blog.naver.com/champion_chart/{no}',title[no],s['what'],sc,src)
    # 맨 위에 블로그 원제목
    p=D+f'nangman_interior_{slug}_clip_info.txt'; t=open(p).read(); open(p,'w').write(f'블로그 원제목\n{title[no]}\n\n'+t)
    q=f'/tmp/claude-0/msg_{slug}.md'; m=open(q).read(); open(q,'w').write(f'**블로그 원제목**\n```\n{title[no]}\n```\n\n'+m)

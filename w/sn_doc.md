# 낭만 인테리어 시공 사진 일련번호 (사용자 10/9 00:07 「다음부터」)

망입유리 중문 글(10/9)부터 적용한다. 발행 · 예약 · 그 전에 만든 미발행 글(아쿠아유리 포함)은 고치지 않는다.

## 왜
- 손님이 「사진 NI-0010 같은 문으로」라고 남기면 맡을 업체 · 문 종류 · 유리 · 색을 바로 찾는다.

## 번호 모양
- `NI-0001`부터 낭만 인테리어 전체 공통으로 이어서 매긴다. 업체를 짐작할 수 있는 글자는 넣지 않는다.
- 공사 전 / 후를 붙인 한 장은 번호 하나.
- 그림(fig) · 썸네일 · 배너에는 넣지 않는다. 업체 시공 사진에만 넣는다.
- 만드는 곳: `int/serial.py` (code · stamp · table_md) · 번호표 원본 `int/serial.json`. 같은 글 · 같은 사진 이름이면 다시 돌려도 같은 번호.
- 이 표는 `int/serial.json`에서 그대로 뽑는다(10/9 입주 단지 글부터 · 10/11 07시 전체를 다시 뽑음 — NI-0228~0262 더함).

## 넣는 곳
- 사진 오른쪽 아래에 번호(사진을 폭 900으로 맞춘 뒤 30pt · 어두운 반투명 띠).
- 사진 설명 끝에 「(사진 NI-0010)」.
- 끝 문의 상자에 「마음에 드는 사진 번호도 같이 남겨 주세요」. 댓글 예시: 「부산 사하, 중문, 사진 NI-0001, 010-0000-0000」.
- 사진 아래 「이 사진처럼 하고 싶다면」 상자(LIKE)로 번호 → 같은 시공팀 연결을 알린다(10/9).

## 문의 문장 (10/8 23:54)
- 「찾아 드립니다」는 쓰지 않는다. 「다른 지역도 가까운 업체를 연결해 드립니다.」
- 「업체 말로는 · 업체 설명으로 · 업체에 따르면」은 쓰지 않는다. 사용자가 검증한 업체다. 사실로 바로 쓴다.

## 주의 (10/9)
- 썬중문은 재는 장면(레이저 · 천장 높이) 사진을 여러 글에 다시 쓴다. 같은 사진이 다른 지역 글에 나온다.
- 그래서 새 글에 넣기 전에 기존 사진과 겹치는지 본다. 겹치면 뺀다.
- 겹쳐서 뺀 사진: 서산 석림동 레이저(의왕 NI-0108과 같음) · 검암 천장 높이(서산 석림동과 같음) · 강아지 매트 가격 글의 파주 동패동 거실 전후(운정 NI-0151과 같음 → 같은 글의 다른 각도 사진으로 바꿈).
- 블라썸매트도 같은 시공 글을 여러 낭만 글에 나눠 쓴다. 같은 글 번호가 보이면 사진 번호(idx)까지 비교한다.

## 예약본과 다른 글
- 산본 인테리어(sanbon_interior · NI-0175~0186): 10/12 12:00 예약본은 번호 없이 올라갔다. 번호가 든 사진은 PC [미발행] 폴더에만 있다. 손님이 이 글 사진을 말하면 이 표의 설명으로 찾는다.

## 번호표

| 번호 | 업체 | 업체 블로그 · 글 번호 | 낭만 글(slug) | 지역 | 내용 |
|---|---|---|---|---|---|
| NI-0001 | 모던중문 | pjh20712 223161494511 | mangip_glass | 부산 사하 | 초슬림 3연동 · 딥블루 · 투명 망입 · 하부고시 · 닫음 |
| NI-0002 | 모던중문 | pjh20712 223161494511 | mangip_glass | 부산 사하 | 초슬림 3연동 · 공사 전 · 뒤 |
| NI-0003 | 모던중문 | pjh20712 223161494511 | mangip_glass | 부산 사하 | 초슬림 3연동 · 딥블루 · 옆 |
| NI-0004 | 모던중문 | pjh20712 223161494511 | mangip_glass | 부산 사하 | 초슬림 3연동 · 연 모습 · 망입 무늬 |
| NI-0005 | 크로바중문 | clovermc2644 221801531662 | mangip_glass | 대전 유성 온천1동 | 슬림 3연동 · 화이트 · 망입 · 닫음 |
| NI-0006 | 크로바중문 | clovermc2644 221801531662 | mangip_glass | 대전 유성 온천1동 | 슬림 3연동 · 공사 전 · 뒤(거실 쪽) |
| NI-0007 | 크로바중문 | clovermc2644 221801531662 | mangip_glass | 대전 유성 온천1동 | 슬림 3연동 · 레일 아래 실리콘 |
| NI-0008 | 크로바중문 | clovermc2644 221801531662 | mangip_glass | 대전 유성 온천1동 | 슬림 3연동 · 연 모습 |
| NI-0009 | 크로바중문 | clovermc2644 221801531662 | mangip_glass | 대전 유성 온천1동 | 슬림 3연동 · 망입 · 아래 판 · 가까이 |
| NI-0010 | 썬중문 | dbswkdrms89 222951204983 | mangip_glass | 평택 고덕 | 스윙 · 화이트 · 망입 · 골드 쫄대 · 공사 전 · 뒤 |
| NI-0011 | 썬중문 | dbswkdrms89 222951204983 | mangip_glass | 평택 고덕 | 스윙 · 레이저 레벨기 · 문틀 |
| NI-0012 | 썬중문 | dbswkdrms89 222951204983 | mangip_glass | 평택 고덕 | 스윙 · 댐퍼 부품 |
| NI-0013 | 썬중문 | dbswkdrms89 222951204983 | mangip_glass | 평택 고덕 | 스윙 · 연 모습 |
| NI-0014 | 썬중문 | dbswkdrms89 222951204983 | mangip_glass | 평택 고덕 | 스윙 · 망입 · 골드 쫄대 · 하부 1단 고시 · 닫음 |
| NI-0015 | 도하인테리어필름 | doha_film 224356352271 | butbagijang_film | 서울 구로 개봉동 | 붙박이장 문짝 전체 · 현대 S178 화이트 · 전 · 후 |
| NI-0016 | 도하인테리어필름 | doha_film 224356352271 | butbagijang_film | 서울 구로 개봉동 | 붙박이장 · 시공 전 금이 간 필름 |
| NI-0017 | 도하인테리어필름 | doha_film 224356352271 | butbagijang_film | 서울 구로 개봉동 | 붙박이장 · 시공 전 스테이플러 자국 |
| NI-0018 | 도하인테리어필름 | doha_film 224356352271 | butbagijang_film | 서울 구로 개봉동 | 붙박이장 · 뽑아낸 심 |
| NI-0019 | 도하인테리어필름 | doha_film 224356352271 | butbagijang_film | 서울 구로 개봉동 | 붙박이장 · 박리 뒤 MDF |
| NI-0020 | 더빅필름 | thebigfilm 224160422233 | butbagijang_film | 안양 미래엠피아 | 현관 신발장 · 하늘색 → 영림 PS100 화이트 |
| NI-0021 | 더빅필름 | thebigfilm 224160422233 | butbagijang_film | 안양 미래엠피아 | 안방 붙박이장 · 하늘색 → PS100 화이트 |
| NI-0022 | 더빅필름 | thebigfilm 224160422233 | butbagijang_film | 안양 미래엠피아 | 붙박이장 문 안쪽 면 · 양면 시공 · 전 · 후 |
| NI-0023 | 더빅필름 | thebigfilm 224160422233 | butbagijang_film | 안양 미래엠피아 | 현관 장 · PS100 화이트 · 시공 후 |
| NI-0024 | 더빅필름 | thebigfilm 224121740482 | butbagijang_film | 화성 동탄 센트럴푸르지오 | 화장대 · 상판 · 서랍 · 전 · 후 |
| NI-0025 | 더빅필름 | thebigfilm 224121740482 | butbagijang_film | 화성 동탄 센트럴푸르지오 | 붙박이장 서랍 · 시공 전 들뜸 |
| NI-0026 | 더빅필름 | thebigfilm 224121740482 | butbagijang_film | 화성 동탄 센트럴푸르지오 | 붙박이장 내부 · 화이트 · 시공 후 |
| NI-0027 | 더빅필름 | thebigfilm 224121740482 | butbagijang_film | 화성 동탄 센트럴푸르지오 | 오픈 수납장 · 전 · 후 |
| NI-0028 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 외부 아이보리 · 완성 |
| NI-0029 | 농막 업체(lsh_house) | lsh_house 224190649930 | container_nongmak | 인천 영종도 | 3×6m · 우레탄폼 시공 |
| NI-0030 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · XL 배관 · 보온재 |
| NI-0031 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 창 둘레 우레탄폼 |
| NI-0032 | 농막 업체(lsh_house) | lsh_house 224397355179 | container_nongmak | 김포 양촌 | 3×6m 알뜰형 · 외부 그레이 도장 |
| NI-0033 | 농막 업체(lsh_house) | lsh_house 224397355179 | container_nongmak | 김포 양촌 | 3×6m · 천장 단열 · 전선관 |
| NI-0034 | 농막 업체(lsh_house) | lsh_house 224397355179 | container_nongmak | 김포 양촌 | 3×6m · 내부 미장합판 |
| NI-0035 | 농막 업체(lsh_house) | lsh_house 224397355179 | container_nongmak | 김포 양촌 | 3×6m · 화장실 · 전기온수기 |
| NI-0036 | 농막 업체(lsh_house) | lsh_house 224291200753 | container_nongmak | 경기 안성 | 3×6m · SF관 · 배선 |
| NI-0037 | 농막 업체(lsh_house) | lsh_house 224291200753 | container_nongmak | 경기 안성 | 3×6m · 내부 편백루바 · 전기온돌판넬 |
| NI-0038 | 농막 업체(lsh_house) | lsh_house 224291200753 | container_nongmak | 경기 안성 | 3×6m · 전실 |
| NI-0039 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 하부 골조 · 장선 |
| NI-0040 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 석고보드 · 도배 |
| NI-0041 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 전실 · 안쪽 문 |
| NI-0042 | 농막 업체(lsh_house) | lsh_house 224428264784 | container_nongmak | 충남 서산 | 3×8m · 화장실 · 타일 · 배수구 |
| NI-0043 | 비치움종합클린 | lnr0724 224387566045 | saejip_jeunghugun | 서울 서초 반포 | 55평 · 편백수 연무 · 거실 |
| NI-0044 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | 신축 분진 · 수납장 |
| NI-0045 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | 수납장 탈거 청소 |
| NI-0046 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | 서랍 레일 · 청소 전 |
| NI-0047 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | 분진 집중케어 · 물필터 |
| NI-0048 | 비치움종합클린 | lnr0724 224387566045 | saejip_jeunghugun | 서울 서초 반포 | 주방 서랍 · 청소 후 |
| NI-0049 | 비치움종합클린 | lnr0724 224387566045 | saejip_jeunghugun | 서울 서초 반포 | UVC 조사 · 수납장 |
| NI-0050 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | UVC 조사 · 서랍장 |
| NI-0051 | 비치움종합클린 | lnr0724 224387566045 | saejip_jeunghugun | 서울 서초 반포 | 편백수 연무 · 드레스룸 |
| NI-0052 | 비치움종합클린 | lnr0724 224411188358 | saejip_jeunghugun | 서울 서초 방배 | 편백수 연무 · 방 |
| NI-0053 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 반려견 2 · 반려묘 3 · 거실 · 깐 뒤 |
| NI-0054 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 거실 · 전후 |
| NI-0055 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 주방 · 전후 |
| NI-0056 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 캣타워 방 |
| NI-0057 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 문턱 높이 차이 |
| NI-0058 | 블라썸매트 | blossommat_ 224306603733 | goyangi_mat | 충남 아산 배방 | 복도 |
| NI-0059 | 블라썸매트 | blossommat_ 224292555682 | goyangi_mat | 서울 구로 | 1살 반려묘 · 거실 · 전후 |
| NI-0060 | 블라썸매트 | blossommat_ 224292555682 | goyangi_mat | 서울 구로 | 주방 · 전후 |
| NI-0061 | 블라썸매트 | blossommat_ 224292555682 | goyangi_mat | 서울 구로 | 현관 턱 · 모양대로 자름 |
| NI-0062 | 블라썸매트 | blossommat_ 224292555682 | goyangi_mat | 서울 구로 | 현관 쪽 |
| NI-0063 | 블라썸매트 | blossommat_ 224164137108 | goyangi_mat | 경기 안양 | 반려묘 + 아이 · 거실 · 전후 |
| NI-0064 | 블라썸매트 | blossommat_ 224164137108 | goyangi_mat | 경기 안양 | 놀이 공간 |
| NI-0065 | 블라썸매트 | blossommat_ 224164137108 | goyangi_mat | 경기 안양 | 복도 |
| NI-0066 | 줄남청 · 줄눈 | ssu2058 224196205032 | sinchuk_ipju_sunseo | 경기 이천 | 신축 줄눈 · 전후 |
| NI-0067 | 줄남청 · 줄눈 | ssu2058 224196205032 | sinchuk_ipju_sunseo | 경기 이천 | 신축 줄눈 백화 |
| NI-0068 | 줄남청 · 줄눈 | ssu2058 224196205032 | sinchuk_ipju_sunseo | 경기 이천 | 신축 줄눈 · 뒤 |
| NI-0069 | 비치움종합클린 | lnr0724 224362185428 | sinchuk_ipju_sunseo | 경기 파주 운정 | 입주청소 · 욕실 선반 |
| NI-0070 | 비치움종합클린 | lnr0724 224362185428 | sinchuk_ipju_sunseo | 경기 파주 운정 | 입주청소 · 수납장 |
| NI-0071 | 비치움종합클린 | lnr0724 224362185428 | sinchuk_ipju_sunseo | 경기 파주 운정 | 입주청소 · 욕실 |
| NI-0072 | 비치움종합클린 | lnr0724 224362185428 | sinchuk_ipju_sunseo | 경기 파주 운정 | 입주청소 · 세면대 |
| NI-0073 | 블라썸매트 | blossommat_ 223969611685 | sinchuk_ipju_sunseo | 서울 영등포 | 매트 · 거실 |
| NI-0074 | 블라썸매트 | blossommat_ 223969611685 | sinchuk_ipju_sunseo | 서울 영등포 | 매트 · 주방 |
| NI-0075 | 블라썸매트 | blossommat_ 223969611685 | sinchuk_ipju_sunseo | 서울 영등포 | 매트 · 복도 |
| NI-0076 | 썬중문 | dbswkdrms89 223294414873 | geomdan_centreville_ipju | 인천 검단 원당동 | 슬라이딩 중문 · 전후 |
| NI-0077 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 실측 · 레이저 |
| NI-0078 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 실측 · 현관 턱 |
| NI-0079 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 실측 · 천장 |
| NI-0080 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 여닫이 · 전후 |
| NI-0081 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 여닫이 · 복도 |
| NI-0082 | 썬중문 | dbswkdrms89 223466377513 | geomdan_centreville_ipju | 인천 검단 당하동 | 실측 · 신발장 옆 |
| NI-0083 | 썬중문 | dbswkdrms89 223466377513 | geomdan_centreville_ipju | 인천 검단 당하동 | 블랙 3연동 · 과정 |
| NI-0084 | 썬중문 | dbswkdrms89 223466377513 | geomdan_centreville_ipju | 인천 검단 당하동 | 블랙 3연동 · 무늬 유리 |
| NI-0085 | 썬중문 | dbswkdrms89 223211717953 | geomdan_centreville_ipju | 인천 검단 원당동 | 여닫이 · 연 모습 |
| NI-0086 | 썬중문 | dbswkdrms89 223254020567 | songnae_centvien | 부천 송내동 새 아파트 | 중문 달기 전 현관 — 대리석 바닥과 빈 입구 |
| NI-0087 | 썬중문 | dbswkdrms89 223254020567 | songnae_centvien | 부천 송내동 새 아파트 | 거실 쪽에서 본 스윙 중문 — 한 짝을 연 모습 |
| NI-0088 | 썬중문 | dbswkdrms89 223254020567 | songnae_centvien | 부천 송내동 새 아파트 | 거실 쪽에서 본 스윙 중문 — 닫은 모습 |
| NI-0089 | 썬중문 | dbswkdrms89 224156058956 | songnae_centvien | 부천 송내동 다른 새 아파트 | 중문 달기 전 — 거실에서 현관문 쪽을 본 긴 복도 |
| NI-0090 | 썬중문 | dbswkdrms89 224156058956 | songnae_centvien | 부천 송내동 다른 새 아파트 | 현관 턱(검은 돌) 폭을 줄자로 재는 모습 |
| NI-0091 | 썬중문 | dbswkdrms89 224156058956 | songnae_centvien | 부천 송내동 다른 새 아파트 | 바닥에 레이저 선을 띄워 중문 자리를 잡는 모습 |
| NI-0092 | 썬중문 | dbswkdrms89 224156058956 | songnae_centvien | 부천 송내동 다른 새 아파트 | 틀을 먼저 세운 모습(보호 필름이 붙은 흰 틀) |
| NI-0093 | 썬중문 | dbswkdrms89 224156058956 | songnae_centvien | 부천 송내동 다른 새 아파트 | 현관 쪽에서 거실을 본 흰 3연동 — 바닥 보호지가 깔린 빈집 |
| NI-0094 | 썬중문 | dbswkdrms89 223314884448 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 | 중문 달기 전 현관 — 회색 우드 벽, 거울 붙박이, 흰 신발 정리함 |
| NI-0095 | 썬중문 | dbswkdrms89 223314884448 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 | 천장 모서리까지 줄자를 대어 높이를 재는 모습(손 안 보임) |
| NI-0096 | 썬중문 | dbswkdrms89 223314884448 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 | 거실 쪽에서 본 3연동 — 위는 벽과 같은 우드 판, 아래 칸만 무늬 유 |
| NI-0097 | 썬중문 | dbswkdrms89 223580266104 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 다른 집 | 중문 달기 전 — 현관에서 본 빈 입구 |
| NI-0098 | 썬중문 | dbswkdrms89 223580266104 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 다른 집 | 현관 턱에 레이저기를 놓고 선을 맞추는 모습 |
| NI-0099 | 썬중문 | dbswkdrms89 223580266104 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 다른 집 | 닫은 흰 3연동 — 투명 유리로 복도가 다 보임 |
| NI-0100 | 썬중문 | dbswkdrms89 223580266104 | pyeongchon_urbanvalley | 안양 호계동 새 아파트 다른 집 | 거실 쪽에서 본 흰 3연동 |
| NI-0101 | 썬중문 | dbswkdrms89 223255030127 | uiwang_centline | 의왕 오전동 새 아파트 | 중문 달기 전 — 긴 복도 끝 현관문, 바닥에 신발 몇 켤레 |
| NI-0102 | 썬중문 | dbswkdrms89 223255030127 | uiwang_centline | 의왕 오전동 새 아파트 | 같은 중문을 연 모습 |
| NI-0103 | 썬중문 | dbswkdrms89 223255030127 | uiwang_centline | 의왕 오전동 새 아파트 | 천장 쪽 레일과 틀 윗부분 가까이 |
| NI-0104 | 썬중문 | dbswkdrms89 223255030127 | uiwang_centline | 의왕 오전동 새 아파트 | 거실 쪽에서 본 골드 3연동 아래 칸 물결 무늬 유리(위쪽 비침 잘라냄) |
| NI-0105 | 썬중문 | dbswkdrms89 224233247704 | uiwang_centline | 의왕 고천동 새 아파트 | 중문 달기 전 — 현관에서 거실 쪽을 본 빈 입구 |
| NI-0106 | 썬중문 | dbswkdrms89 224233247704 | uiwang_centline | 의왕 고천동 새 아파트 | 현관 턱(테라조 무늬 돌)과 마루 사이를 줄자로 재는 모습(손 안 보임) |
| NI-0107 | 썬중문 | dbswkdrms89 224233247704 | uiwang_centline | 의왕 고천동 새 아파트 | 거실 쪽에서 본 간살 3연동 |
| NI-0108 | 썬중문 | dbswkdrms89 224388333436 | uiwang_centline | 의왕 내손동 새 아파트 | 현관 턱 위에 레이저기를 놓고 선을 띄운 모습 |
| NI-0109 | 줄남청 · 줄눈 | ssu2058 224205501356 | osan_geumgang_ipju | 경기광주 · 성남 입주 전 집 | 입주 전 베란다 바닥 타일 · 줄눈 넣기 전 |
| NI-0110 | 줄남청 · 줄눈 | ssu2058 224205501356 | osan_geumgang_ipju | 경기광주 · 성남 입주 전 집 | 줄눈 넣고 바닥에 하얀 자국이 남은 작업 중 모습 |
| NI-0111 | 줄남청 · 줄눈 | ssu2058 224205501356 | osan_geumgang_ipju | 경기광주 · 성남 입주 전 집 | 창 옆 베란다 바닥 · 줄눈 마친 뒤 |
| NI-0112 | 줄남청 · 줄눈 | ssu2058 224205501356 | osan_geumgang_ipju | 경기광주 · 성남 입주 전 집 | 거실 바닥 타일 전체 · 줄눈 마친 뒤 |
| NI-0113 | 블라썸매트 | blossommat_ 224039796881 | osan_geumgang_ipju | 수원 아파트 | 매트 깔기 전 거실 · 주방(회색 마루) |
| NI-0114 | 블라썸매트 | blossommat_ 224039796881 | osan_geumgang_ipju | 수원 아파트 | 복도와 현관 쪽까지 이어 깐 매트 |
| NI-0115 | 블라썸매트 | blossommat_ 224114325140 | osan_geumgang_ipju | 평택 아파트 | 주방 · 식탁 자리까지 깐 스톤화이트 매트 |
| NI-0116 | 블라썸매트 | blossommat_ 224114325140 | osan_geumgang_ipju | 평택 아파트 | 현관에서 본 복도 매트 |
| NI-0117 | 비치움종합클린 | lnr0724 224301923778 | deungchon_ipju | 서울 은평구 새 아파트 | 떼어 낸 서랍 자리 바닥에 공사 먼지가 쌓인 모습 |
| NI-0118 | 비치움종합클린 | lnr0724 224301923778 | deungchon_ipju | 서울 은평구 새 아파트 | 서랍을 모두 빼서 바닥에 늘어놓은 모습(떼어서 닦는 청소) |
| NI-0119 | 비치움종합클린 | lnr0724 224301923778 | deungchon_ipju | 서울 은평구 새 아파트 | 거실 창 유리에 세제 거품을 바른 모습 |
| NI-0120 | 비치움종합클린 | lnr0724 224301923778 | deungchon_ipju | 서울 은평구 새 아파트 | 욕실 샤워 유리에 세제 거품을 바른 모습 |
| NI-0121 | 비치움종합클린 | lnr0724 224293291254 | deungchon_ipju | 광명역 아파트(인테리어 끝난 집) | 욕조 안에 공사 가루와 얼룩이 남은 모습(청소 전) |
| NI-0122 | 비치움종합클린 | lnr0724 224293291254 | deungchon_ipju | 광명역 아파트(인테리어 끝난 집) | 창틀 레일 안에 먼지와 실리콘 찌꺼기가 낀 모습(청소 전) |
| NI-0123 | 비치움종합클린 | lnr0724 224293291254 | deungchon_ipju | 광명역 아파트(인테리어 끝난 집) | 현관 바닥 타일에 공사 먼지가 하얗게 앉은 모습(청소 전) |
| NI-0124 | 비치움종합클린 | lnr0724 224340806813 | reventus_ipju | 강남 청담동 새 아파트(1년 안 산 집) | 싱크대 배수구 거름망에 찌꺼기가 남은 모습(청소 전) |
| NI-0125 | 비치움종합클린 | lnr0724 224340806813 | reventus_ipju | 강남 청담동 새 아파트(1년 안 산 집) | 창틀 레일에 검은 먼지가 낀 모습(청소 전) |
| NI-0126 | 비치움종합클린 | lnr0724 224340806813 | reventus_ipju | 강남 청담동 새 아파트(1년 안 산 집) | 현관 신발장 아래 칸(청소 전) |
| NI-0127 | 비치움종합클린 | lnr0724 224340806813 | reventus_ipju | 강남 청담동 새 아파트(1년 안 산 집) | 높은 층 창 유리에 세제를 바르고 닦는 중 |
| NI-0128 | 비치움종합클린 | lnr0724 224340806813 | reventus_ipju | 강남 청담동 새 아파트(1년 안 산 집) | 청소 끝난 주방과 복도 |
| NI-0129 | 블라썸매트 | blossommat_ 224212509516 | reventus_ipju | 위례 아파트 | 매트 깔기 전 거실 마루 |
| NI-0130 | 크로바중문 | clovermc2644 222969708791 | seodaejeon_ipju | 대전 문화동 아파트 | 신발장 사이 빈 현관 — 중문 달기 전 |
| NI-0131 | 크로바중문 | clovermc2644 222969708791 | seodaejeon_ipju | 대전 문화동 아파트 | 옆에서 본 남색 3연동 — 문 세 짝이 겹친 두께 |
| NI-0132 | 크로바중문 | clovermc2644 222969708791 | seodaejeon_ipju | 대전 문화동 아파트 | 3연동 한쪽을 열어 둔 모습 — 드나드는 폭 |
| NI-0133 | 크로바중문 | clovermc2644 223891373372 | seodaejeon_ipju | 대전 도마동 아파트 | 중문 달기 전 현관 — 신발장과 거울장 사이 |
| NI-0134 | 크로바중문 | clovermc2644 223891373372 | seodaejeon_ipju | 대전 도마동 아파트 | 비대칭 스윙도어 큰 문을 연 모습 |
| NI-0135 | 크로바중문 | clovermc2644 223521990276 | seodaejeon_ipju | 대전 선화동 아파트 | 기존 문을 떼어 낸 현관 틀 — 거실 쪽에서 본 모습 |
| NI-0136 | 크로바중문 | clovermc2644 223962673329 | seodaejeon_ipju | 대전 대덕구 아파트 | 중문 달기 전 긴 현관 복도 |
| NI-0137 | 크로바중문 | clovermc2644 223958825851 | seodaejeon_ipju | 대전 중구 아파트 | 진회색 원슬라이딩 간살 중문 — 단 뒤(거울장 옆) |
| NI-0138 | 썬중문 | dbswkdrms89 224394198988 | seosan_ipark_ipju | 서산 석림동 아파트 | 현관 턱과 마루가 만나는 바닥 폭을 줄자로 재는 모습 |
| NI-0139 | 썬중문 | dbswkdrms89 224135096135 | seosan_ipark_ipju | 서산 성연면 새 아파트 | 현관 턱 대리석과 마루 경계를 줄자로 재는 모습 |
| NI-0140 | 썬중문 | dbswkdrms89 224135096135 | seosan_ipark_ipju | 서산 성연면 새 아파트 | 중문 틀 바로 옆 전등 스위치 — 스위치를 피해 틀을 세운 자리 |
| NI-0141 | 썬중문 | dbswkdrms89 224135096135 | seosan_ipark_ipju | 서산 성연면 새 아파트 | 샴페인색 얇은 틀 3연동 · 투명 강화유리 — 단 뒤 |
| NI-0142 | 썬중문 | dbswkdrms89 223940300456 | seosan_ipark_ipju | 서산테크노밸리 새 아파트 | 천장 몰딩까지 높이를 줄자로 재는 모습 |
| NI-0143 | 썬중문 | dbswkdrms89 223940300456 | seosan_ipark_ipju | 서산테크노밸리 새 아파트 | 흰 틀 3연동 — 거실 쪽 옆에서 본 모습 |
| NI-0144 | 썬중문 | dbswkdrms89 223346328835 | unjeong_jeil_ipju | 파주 운정 새 아파트 | 중문 달기 전 현관 — 신발장과 장식장 사이 빈 자리 |
| NI-0145 | 썬중문 | dbswkdrms89 223346328835 | unjeong_jeil_ipju | 파주 운정 새 아파트 | 현관 턱 대리석 모서리를 따라 줄자로 재는 모습 |
| NI-0146 | 썬중문 | dbswkdrms89 223798309897 | unjeong_jeil_ipju | 파주 다율동 새 아파트 | 중문 달기 전 현관 복도 |
| NI-0147 | 썬중문 | dbswkdrms89 223798309897 | unjeong_jeil_ipju | 파주 다율동 새 아파트 | 바닥 마루와 현관 턱 경계를 줄자로 재는 모습 |
| NI-0148 | 비치움종합클린 | lnr0724 224249859594 | unjeong_jeil_ipju | 파주 운정 다른 새 아파트 | 주방 수납장 안 — 공사 먼지와 나무 가루가 남은 청소 전 |
| NI-0149 | 비치움종합클린 | lnr0724 224249859594 | unjeong_jeil_ipju | 파주 운정 다른 새 아파트 | 세면대 — 이물질과 물방울 자국이 남은 청소 전 |
| NI-0150 | 비치움종합클린 | lnr0724 224249859594 | unjeong_jeil_ipju | 파주 운정 다른 새 아파트 | 창틀 레일 모서리 — 공사 먼지가 쌓인 청소 전 |
| NI-0151 | 블라썸매트 | blossommat_ 223863063343 | unjeong_jeil_ipju | 파주 동패동 아파트 | 매트 깔기 전 거실 — 카펫과 접은 매트를 여기저기 깐 모습 |
| NI-0152 | 썬중문 | dbswkdrms89 223387382930 | geomdan_jeil3_ipju | 인천 루원시티 아파트 | 중문 달기 전 현관 · 양쪽 거울 신발장, 바닥에 신발 몇 켤레 |
| NI-0153 | 썬중문 | dbswkdrms89 223387382930 | geomdan_jeil3_ipju | 인천 루원시티 아파트 | 집 안쪽 복도에서 본 연골드 3연동 옆모습(무늬 유리 칸이 보임) |
| NI-0154 | 썬중문 | dbswkdrms89 223387382930 | geomdan_jeil3_ipju | 인천 루원시티 아파트 | 집 안쪽에서 본 연골드 3연동 정면 · 간살과 무늬 유리 |
| NI-0155 | 썬중문 | dbswkdrms89 224281404676 | geomdan_jeil3_ipju | 인천 서구 검암 아파트 | 중문 달기 전 · 현관에서 거실 쪽으로 본 빈 입구(키 큰 신발장 옆) |
| NI-0156 | 썬중문 | dbswkdrms89 224281404676 | geomdan_jeil3_ipju | 인천 서구 검암 아파트 | 현관 바닥에 레이저 선을 띄워 수평을 맞추는 모습 |
| NI-0157 | 썬중문 | dbswkdrms89 224281404676 | geomdan_jeil3_ipju | 인천 서구 검암 아파트 | 바닥 레일 클로즈업 · 3줄 레일 |
| NI-0158 | 블라썸매트 | blossommat_ 223590377552 | geomdan_jeil3_ipju | 인천 송도 아파트 | 매트 깔기 전 주방 앞 마루 바닥 |
| NI-0159 | 썬중문 | dbswkdrms89 224120024434 | dongjak_signature_ipju | 영등포 대림동 아파트 | 화이트 틀 3연동 · 세로 줄무늬 유리 · 오른쪽 거울 신발장 |
| NI-0160 | 썬중문 | dbswkdrms89 224120024434 | dongjak_signature_ipju | 영등포 대림동 아파트 | 한 짝을 연 3연동 옆모습 · 현관문이 보임 |
| NI-0161 | 썬중문 | dbswkdrms89 223477864881 | dongjak_signature_ipju | 영등포 신길동 아파트 | 중문 달기 전 현관 · 신발장과 신발들 |
| NI-0162 | 썬중문 | dbswkdrms89 223477864881 | dongjak_signature_ipju | 영등포 신길동 아파트 | 천장과 신발장 위 모서리 · 틀 들어갈 자리 |
| NI-0163 | 썬중문 | dbswkdrms89 223477864881 | dongjak_signature_ipju | 영등포 신길동 아파트 | 복도에서 본 3연동 옆모습 · 모루(불투명) 유리 |
| NI-0164 | 썬중문 | dbswkdrms89 223257906674 | dongjak_signature_ipju | 영등포 신길동 다른 아파트 | 중문 달기 전 · 현관문까지 이어진 빈 복도 |
| NI-0165 | 썬중문 | dbswkdrms89 223257906674 | dongjak_signature_ipju | 영등포 신길동 다른 아파트 | 한 짝을 연 3연동 옆모습 |
| NI-0166 | 블라썸매트 | blossommat_ 223511609858 | dongjak_signature_ipju | 강서 우장산 아파트 | 매트 깔기 전 거실 마루 · 소파 |
| NI-0167 | 모던중문 | pjh20712 223327693878 | ecodelta_jungheung_ipju | 부산 강서구 명지 아파트 | 한 장에 전후 두 컷(화살표) · 왼쪽 달기 전 긴 복도 현관 · 오른쪽 |
| NI-0168 | 모던중문 | pjh20712 223327693878 | ecodelta_jungheung_ipju | 부산 강서구 명지 아파트 | 화이트 초슬림 비대칭 양개도어 정면 · 플루트(세로 줄무늬) 강화유리 · |
| NI-0169 | 모던중문 | pjh20712 223327693878 | ecodelta_jungheung_ipju | 부산 강서구 명지 아파트 | 세 컷 나란히 · 큰 문만 연 모습 · 둘 다 연 모습 · 접어 붙인 모 |
| NI-0170 | 모던중문 | pjh20712 223359616839 | ecodelta_jungheung_ipju | 김해 안동 아파트 | 한 장에 전후 · 왼쪽 달기 전 현관 · 오른쪽 화이트 원슬라이딩 투명  |
| NI-0171 | 모던중문 | pjh20712 223359616839 | ecodelta_jungheung_ipju | 김해 안동 아파트 | 한 장에 연 모습과 닫은 모습 · 원슬라이딩 한 짝 |
| NI-0172 | 모던중문 | pjh20712 223189382344 | ecodelta_jungheung_ipju | 김해 장유 아파트 | 한 장에 전후 · 왼쪽 신발장만 있는 현관 · 오른쪽 다크네이비 정대칭  |
| NI-0173 | 모던중문 | pjh20712 223074111191 | ecodelta_jungheung_ipju | 부산 사하구 아파트 | 한 장에 연 모습과 닫은 모습 · 샴페인골드 틀 원슬라이딩 · 브론즈 유 |
| NI-0174 | 블라썸매트 | blossommat_ 223475372754 | ecodelta_jungheung_ipju | 양산 아파트 | 매트 깔기 전 거실 원목 마루 |
| NI-0175 | 다온창호 | daonsash 224259371353 | sanbon_interior | 군포 산본동 | 알루미늄 발코니 창을 새 창으로 바꾼 모습 |
| NI-0176 | 다온창호 | daonsash 224259371353 | sanbon_interior | 군포 산본동 | 단창으로 바꾼 거실 분합문 |
| NI-0177 | 다온창호 | daonsash 224259371353 | sanbon_interior | 군포 산본동 | 복도 쪽 방 창을 이중창으로 바꾼 모습 |
| NI-0178 | 다온창호 | daonsash 224259371353 | sanbon_interior | 군포 산본동 | 복도 쪽 방 창 밖에 단 방범창 |
| NI-0179 | 다온창호 | daonsash 223675716790 | sanbon_interior | 군포 산본 | 공사 전 알루미늄 발코니 창 |
| NI-0180 | 다온창호 | daonsash 223675716790 | sanbon_interior | 군포 산본 | 살던 분이 침실 벽에 붙여 둔 단열재 |
| NI-0181 | 다온창호 | daonsash 223675716790 | sanbon_interior | 군포 산본 | 새로 바꾼 발코니 창 |
| NI-0182 | 다온창호 | daonsash 223675716790 | sanbon_interior | 군포 산본 | 거실 분합문 단창 |
| NI-0183 | 다온창호 | daonsash 223675716790 | sanbon_interior | 군포 산본 | 침실 이중창 |
| NI-0184 | 썬중문 | dbswkdrms89 224397501560 | sanbon_interior | 군포 산본동 | 바닥 레일 없이 접히며 열리는 스윙 중문 |
| NI-0185 | 썬중문 | dbswkdrms89 224381910125 | sanbon_interior | 군포 산본동 | 가벽을 세우고 ㄱ자로 둘러 단 3연동 중문 |
| NI-0186 | 썬중문 | dbswkdrms89 224381910125 | sanbon_interior | 군포 산본동 | 가벽 쪽 고정 유리와 문틀을 세운 모습 |
| NI-0187 | 블라썸매트 | blossommat_ 223863063343 | gangaji_mat_gagyeok | 경기 파주 | 카펫을 접어 쓰던 거실과 매트를 깐 거실 |
| NI-0188 | 블라썸매트 | blossommat_ 223863063343 | gangaji_mat_gagyeok | 경기 파주 | 현관 쪽 복도까지 이어 깐 매트 |
| NI-0189 | 블라썸매트 | blossommat_ 223863063343 | gangaji_mat_gagyeok | 경기 파주 | 주방 바닥까지 같은 매트 |
| NI-0190 | 블라썸매트 | blossommat_ 223853346593 | gangaji_mat_gagyeok | 경기 파주 | 흰 매트를 깐 거실 |
| NI-0191 | 블라썸매트 | blossommat_ 223853346593 | gangaji_mat_gagyeok | 경기 파주 | 거실 벽 끝까지 이어 깐 매트 |
| NI-0192 | 블라썸매트 | blossommat_ 223853346593 | gangaji_mat_gagyeok | 경기 파주 | 창가 끝선까지 잘라 맞춘 매트 |
| NI-0193 | 블라썸매트 | blossommat_ 224227979624 | gangaji_mat_gagyeok | 경기 안양 평촌 | 마루 거실에 브라운 매트를 깐 모습 |
| NI-0194 | 블라썸매트 | blossommat_ 224227979624 | gangaji_mat_gagyeok | 경기 안양 평촌 | 매트 위를 걷는 이탈리안 그레이하운드 |
| NI-0195 | 블라썸매트 | blossommat_ 224227979624 | gangaji_mat_gagyeok | 경기 안양 평촌 | 매트 위에 선 믹스견 |
| NI-0196 | 블라썸매트 | blossommat_ 223934576503 | gangaji_mat_gagyeok | 인천 부평 | 노후 마루 거실에 매트를 깐 모습 |
| NI-0197 | 블라썸매트 | blossommat_ 223934576503 | gangaji_mat_gagyeok | 인천 부평 | 현관 쪽까지 이어 깐 매트 |
| NI-0198 | 블라썸매트 | blossommat_ 223945765841 | seulgaegol_sulhu | 광주 서구 | 짙은 마루 거실과 밝은 매트를 깐 거실 |
| NI-0199 | 블라썸매트 | blossommat_ 223945765841 | seulgaegol_sulhu | 광주 서구 | 방문 앞 복도까지 이어 깐 매트 |
| NI-0200 | 블라썸매트 | blossommat_ 223945765841 | seulgaegol_sulhu | 광주 서구 | 주방 바닥까지 같은 매트 |
| NI-0201 | 블라썸매트 | blossommat_ 223926117447 | seulgaegol_sulhu | 경기 하남 미사 | 나무 마루 주방과 매트를 깐 주방 |
| NI-0202 | 블라썸매트 | blossommat_ 223926117447 | seulgaegol_sulhu | 경기 하남 미사 | 거실 벽 끝까지 맞춰 깐 매트 |
| NI-0203 | 블라썸매트 | blossommat_ 223926117447 | seulgaegol_sulhu | 경기 하남 미사 | 주방에서 현관 쪽 복도로 이어진 매트 |
| NI-0204 | 블라썸매트 | blossommat_ 223945765841 | seulgaegol_sulhu | 광주 서구 | 주방 쪽에서 본 매트 바닥 |
| NI-0205 | 블라썸매트 | blossommat_ 223945765841 | seulgaegol_sulhu | 광주 서구 | 방 안쪽 벽 끝까지 맞춘 매트 |
| NI-0206 | 블라썸매트 | blossommat_ 223926117447 | seulgaegol_sulhu | 경기 하남 미사 | 방문 앞까지 이어 깐 매트 |
| NI-0207 | 블라썸매트 | blossommat_ 223926117447 | seulgaegol_sulhu | 경기 하남 미사 | 식탁 아래까지 깐 매트 |
| NI-0208 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 대리석 거실과 매트를 깐 거실 |
| NI-0209 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 대리석 현관 쪽과 매트를 깐 모습 |
| NI-0210 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 식탁 아래까지 깐 매트 |
| NI-0211 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 긴 복도를 따라 이어 깐 매트 |
| NI-0212 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 주방 수납장 앞까지 깐 매트 |
| NI-0213 | 블라썸매트 | blossommat_ 224310355179 | nogyeon_mikkeureom | 서울 서초 | 방문 앞까지 이어진 매트 |
| NI-0214 | 블라썸매트 | blossommat_ 224064409231 | nogyeon_mikkeureom | 전남 순천 | 거실 전체에 깐 브라운 매트 |
| NI-0215 | 블라썸매트 | blossommat_ 224064409231 | nogyeon_mikkeureom | 전남 순천 | 현관으로 이어지는 복도 매트 |
| NI-0216 | 블라썸매트 | blossommat_ 224064409231 | nogyeon_mikkeureom | 전남 순천 | 좁은 주방 바닥까지 깐 매트 |
| NI-0217 | 블라썸매트 | blossommat_ 224064409231 | nogyeon_mikkeureom | 전남 순천 | 주방 옆 공간까지 이어진 매트 |
| NI-0218 | 블라썸매트 | blossommat_ 224279037782 | gangaji_badak_sigong | 경기 의정부 | 우드톤 마루와 매트를 깐 거실 |
| NI-0219 | 블라썸매트 | blossommat_ 224279037782 | gangaji_badak_sigong | 경기 의정부 | 주방까지 이어 깐 매트 |
| NI-0220 | 블라썸매트 | blossommat_ 224279037782 | gangaji_badak_sigong | 경기 의정부 | 방문 앞 벽 끝까지 맞춘 매트 |
| NI-0221 | 블라썸매트 | blossommat_ 224261346040 | gangaji_badak_sigong | 경기 광명 | 마루였던 거실과 주방 쪽에 깐 브라운 매트 |
| NI-0222 | 블라썸매트 | blossommat_ 224261346040 | gangaji_badak_sigong | 경기 광명 | 방문 앞 복도에 깐 매트 |
| NI-0223 | 블라썸매트 | blossommat_ 224261346040 | gangaji_badak_sigong | 경기 광명 | 소파 앞 거실 전체에 깐 매트 |
| NI-0224 | 블라썸매트 | blossommat_ 224212509516 | gangaji_badak_sigong | 위례 | 창가까지 깐 거실 매트 |
| NI-0225 | 블라썸매트 | blossommat_ 224212509516 | gangaji_badak_sigong | 위례 | 거실에서 주방으로 이어진 매트 |
| NI-0226 | 블라썸매트 | blossommat_ 224212509516 | gangaji_badak_sigong | 위례 | 방으로 가는 복도 입구까지 깐 매트 |
| NI-0227 | 블라썸매트 | blossommat_ 224212509516 | gangaji_badak_sigong | 위례 | 꺾인 벽 모양대로 자른 매트 끝 |
| NI-0228 | 블라썸매트 | blossommat_ 223590377552 | gangaji_mat_chucheon | 인천 송도 | 마루 거실과 스톤화이트 매트를 깐 거실 |
| NI-0229 | 블라썸매트 | blossommat_ 223590377552 | gangaji_mat_chucheon | 인천 송도 | 주방까지 이어 깐 매트 |
| NI-0230 | 블라썸매트 | blossommat_ 223590377552 | gangaji_mat_chucheon | 인천 송도 | 문틀 모양대로 잘라 맞춘 끝선 |
| NI-0231 | 블라썸매트 | blossommat_ 223590377552 | gangaji_mat_chucheon | 인천 송도 | 이음매가 한 줄로 맞은 매트 |
| NI-0232 | 블라썸매트 | blossommat_ 223577086207 | gangaji_mat_chucheon | 인천 송도 | 마블아이보리 매트 위를 걷는 고양이 |
| NI-0233 | 블라썸매트 | blossommat_ 223577086207 | gangaji_mat_chucheon | 인천 송도 | 마루 거실에 마블아이보리 매트를 깐 모습 |
| NI-0234 | 블라썸매트 | blossommat_ 223577086207 | gangaji_mat_chucheon | 인천 송도 | 매트 위에 선 고양이 |
| NI-0235 | 블라썸매트 | blossommat_ 224039796881 | gangaji_mat_chucheon | 경기 수원 | 복도까지 흰 논슬립 매트를 깐 모습 |
| NI-0236 | 블라썸매트 | blossommat_ 224039796881 | gangaji_mat_chucheon | 경기 수원 | 거실 전체에 깐 흰 논슬립 매트 |
| NI-0237 | 블라썸매트 | blossommat_ 224205475455 | gangaji_mat_chucheon | 서울 강북 번동 | 매트를 깐 거실과 강아지 |
| NI-0238 | 블라썸매트 | blossommat_ 224205475455 | gangaji_mat_chucheon | 서울 강북 번동 | 방 앞 복도까지 이어 깐 매트 |
| NI-0239 | 입주청소 제휴팀 | lnr0724 224408664526 | ipju_cheongso_upche | 서울 은평 | 가스레인지 받침과 부속을 모두 떼어 낸 주방 |
| NI-0240 | 입주청소 제휴팀 | lnr0724 224408664526 | ipju_cheongso_upche | 서울 은평 | 후드 필터와 수납장 선반을 꺼내 늘어놓은 모습 |
| NI-0241 | 입주청소 제휴팀 | lnr0724 224408664526 | ipju_cheongso_upche | 서울 은평 | 욕실 배수구 트랩과 부속을 떼어 낸 세면대 |
| NI-0242 | 입주청소 제휴팀 | lnr0724 224408664526 | ipju_cheongso_upche | 서울 은평 | 덮개를 떼어 안쪽까지 닦은 욕실 환풍구 |
| NI-0243 | 입주청소 제휴팀 | lnr0724 224408664526 | ipju_cheongso_upche | 서울 은평 | 창틀 레일 안쪽 |
| NI-0244 | 입주청소 제휴팀 | lnr0724 224293291254 | ipju_cheongso_upche | 경기 광명 | 서랍을 뺀 레일에 쌓인 공사 분진 |
| NI-0245 | 입주청소 제휴팀 | lnr0724 224293291254 | ipju_cheongso_upche | 경기 광명 | 서랍 칸막이를 꺼내 따로 닦는 모습 |
| NI-0246 | 입주청소 제휴팀 | lnr0724 224293291254 | ipju_cheongso_upche | 경기 광명 | 도배풀과 석고 가루가 굳어 있던 창틀 레일 |
| NI-0247 | 입주청소 제휴팀 | lnr0724 224293291254 | ipju_cheongso_upche | 경기 광명 | 인테리어 뒤 청소를 마친 거실 |
| NI-0248 | 입주청소 제휴팀 | lnr0724 224370400503 | ipju_cheongso_upche | 서울 강동 | 서랍 레일 사이까지 닦는 모습 |
| NI-0249 | 입주청소 제휴팀 | lnr0724 224370400503 | ipju_cheongso_upche | 서울 강동 | 선반 위 신축 분진을 걷어 낸 주방 수납장 |
| NI-0250 | 입주청소 제휴팀 | lnr0724 224370400503 | ipju_cheongso_upche | 서울 강동 | 공사 먼지가 쌓여 있던 창틀 모서리 |
| NI-0251 | 입주청소 제휴팀 | lnr0724 224370400503 | ipju_cheongso_upche | 서울 강동 | 덮개를 떼어 낸 욕실 환풍구 |
| NI-0252 | 입주청소 제휴팀 | lnr0724 224370400503 | ipju_cheongso_upche | 서울 강동 | 청소를 마친 거실 |
| NI-0253 | 블라썸매트 | blossommat_ 223978322599 | gangaji_rollmat | 인천 송도 | 주방 바닥에 롤매트를 펴 두었던 때와 시공 매트를 깐 뒤 |
| NI-0254 | 블라썸매트 | blossommat_ 223978322599 | gangaji_rollmat | 인천 송도 | 오래된 마루 거실과 매트를 깐 뒤 |
| NI-0255 | 블라썸매트 | blossommat_ 223978322599 | gangaji_rollmat | 인천 송도 | 현관에서 이어지는 긴 복도 |
| NI-0256 | 블라썸매트 | blossommat_ 223978322599 | gangaji_rollmat | 인천 송도 | 방문 앞까지 모양대로 자른 매트 |
| NI-0257 | 블라썸매트 | blossommat_ 224018717514 | gangaji_rollmat | 경기 고양 | 마루 주방과 매트를 깐 뒤 |
| NI-0258 | 블라썸매트 | blossommat_ 224018717514 | gangaji_rollmat | 경기 고양 | 방으로 가는 복도 |
| NI-0259 | 블라썸매트 | blossommat_ 224018717514 | gangaji_rollmat | 경기 고양 | ㄷ자 주방 안쪽까지 맞춘 매트 |
| NI-0260 | 블라썸매트 | blossommat_ 224317677881 | gangaji_rollmat | 경기 수원 | 큰 판 매트를 깐 거실 |
| NI-0261 | 블라썸매트 | blossommat_ 224317677881 | gangaji_rollmat | 경기 수원 | 문턱을 전용 마감재로 이은 곳 |
| NI-0262 | 블라썸매트 | blossommat_ 224317677881 | gangaji_rollmat | 경기 수원 | 거실에서 주방으로 이어진 매트 |

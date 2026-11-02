"""기본형(오렌지) · 고급형(드림하우스 준프리미엄) 두 코스 금액표 · 설명 (10/29 사용자 「금액 명확 · 서비스 정확 매칭 · 10% 남아야」)
기본형 = 오렌지 홈케어: 입주청소 평당 1만 1천 + 새집증후군 묶음 평당 1만 = 평당 2만 1천 (30평 63만 · 34평 71만 4천 · 오렌지 10/23 문자) · 수수료는 오렌지가 줌
고급형 = 비치움 3단계 평당 3만(청소+광촉매 저감 · 수수료 5% · 사용자 「제시는 하되 밀지 않음」)
프리미엄형 = 드림하우스 판매가: 준프리미엄 입주청소(59 55만 · 74 65만 · 84 73만 · 그 외 평×2.2만) + 새집증후군 청소와 같이 평×1.2만 · 판매가에 우리 몫(청소 10% · 새집 15%) 포함
부가세 별도."""
from html import escape as e
PREM={25:55,30:65,34:73}
def basic(py): return round(py*2.1,1)
def prem(py):
    c=PREM.get(py,round(py*2.2,1)); return round(c+py*1.2,1)
def bich(py): return round(py*3,1)
def won(m):
    man=int(m); chun=int(round((m-man)*10))
    return '%d만 %d천원'%(man,chun) if chun else '%d만원'%man
TD='padding:14px 8px;border:1px solid #D9DEE6;font-size:18px;text-align:center;'
def table(rows):
    """rows: [(라벨, 공급평수)]"""
    h='<table width="693" style="width:100%;border-collapse:collapse;table-layout:fixed;">'
    h+='<tr>'+''.join('<td style="%sbackground:#EEF2F7;font-weight:700;color:#1F3864;">%s</td>'%(TD,x) for x in ['평형','기본형','고급형','프리미엄형'])+'</tr>'
    for lab,py in rows:
        h+='<tr><td style="%s">%s</td><td style="%s">%s</td><td style="%s">%s</td><td style="%s">%s</td></tr>'%(TD,e(lab),TD,won(basic(py)),TD,won(bich(py)),TD,won(prem(py)))
    return h+'</table>\n\n'
BASIC_P='<b>기본형</b>은 한국인 부부 팀이 하루 한 집만 합니다. 입주청소(평당 1만 1천원)와 새집증후군을 묶은 금액입니다. 새집증후군은 자체 열 발생기로 실내를 40도 가까이 올리는 베이크아웃에 오존 · 가구 잘린 면 코팅까지 하고, 시공 전후 포름알데히드와 라돈을 재서 보여 드립니다. 같은 단지 30세대가 모이면 욕실 나노코팅은 돈을 받지 않습니다.'
BICH_P='<b>고급형</b>은 서울 · 경기 팀이 하루 한 집만 합니다. 평당 3만원 코스로, 청소와 새집 · 헌집증후군 저감 케어(광촉매)가 금액 안에 들어 있습니다. 바닥에 물부터 뿌리지 않고 마루 틈 분진을 건식으로 먼저 빼낸 뒤, 바닥재마다 장비와 세제를 바꿔 닦습니다. 수납장 · 신발장 선반 · 환풍구 · 배수구 트랩 · 주방 후드까지 떼어 닦고, UVC 살균과 편백수 연무로 마무리합니다. 현장 추가금은 없습니다.'
PREM_P='<b>프리미엄형</b>은 외주 없는 직영팀이 하루 한 집만 하고, 현장에서 붙는 추가금이 없습니다. 벽지 컬비 청소 · 바닥 기계 청소 · 에어컨 필터 청소가 금액 안에 들어 있습니다. 새집증후군은 가구 잘린 면 차폐 코팅 뒤 열풍기로 하는 베이크아웃입니다. 청소 전 하자 사진 · 영상과 실명 단톡방, 계약금 없는 후불은 이 팀의 기본입니다.'
NOTE='세 코스 모두 청소와 새집증후군이 같이 들어간 금액입니다. 부가세는 따로입니다. 위 금액은 공급평수 기준이고, 계약서의 공급평수를 문자로 주시면 코스별 금액을 바로 드립니다. 외창(바깥 유리) 청소는 두 코스 모두 따로입니다.'
PS='<p style="font-size:19px;color:#333;line-height:1.9;">%s</p>\n\n'
BR='<p><br></p>\n\n'
def block(rows):
    return table(rows)+PS%BASIC_P+BR+PS%BICH_P+BR+PS%PREM_P+BR+PS%e(NOTE)+BR
if __name__=='__main__':
    for py in (25,29,30,33,34,38,43,44): print(py,won(basic(py)),won(prem(py)))

# ---- 따로 맡길 때 (10/29 01:39 사용자 「청소와 새집증후군 별도로 하는 경우도」) ----
# 청소만: 일반(드림하우스 일반 평 1.2만 · 59 30 · 74 36 · 84 41 · 현장 추가금 있음 · 내 몫 10%) / 고급(비치움 01 평 2만 · 5%) / 프리미엄(드림 준프리미엄 평 2.2만 · 10%)
# 새집증후군만: 기본형(오렌지 평 1.1만 · 30평 33만) / 프리미엄(드림 단독 평 1.3만 · 59 32.5 · 74 39 · 84 44 · 10%)
DREAM_GEN={25:30,30:36,34:41}
DREAM_SJ={25:32.5,30:39,34:44}
def clean_gen(py): return DREAM_GEN.get(py,round(py*1.2,1))
def clean_std(py): return round(py*2,1)
def clean_prem(py): return PREM.get(py,round(py*2.2,1))
def sj_basic(py): return round(py*1.1,1)
def sj_prem(py): return DREAM_SJ.get(py,round(py*1.3,1))
def sep_rows(pys):
    return [(py,won(clean_gen(py)),won(clean_std(py)),won(clean_prem(py)),won(sj_basic(py)),won(sj_prem(py)),won(basic(py))) for py in pys]

# ---- 11/2 사용자 「청소도 묶음 풀고」 — 입주 글 제목 · 썸네일 · 첫 표는 청소 단독 금액, 새집증후군은 따로 더하는 칸 ----
# 11/2 12:14 사용자 「오렌지는 청소만 안 할 거야 · 자기는 청소가 아니거든」 → 청소만 = 드림하우스 일반(평 1.2만 · 59 30 · 74 36 · 84 41 · 현장 추가금 있음 · 내 몫 10%)
#   새집증후군만 = 오렌지 단독(평 1.1만 · 30평 33만 · 34평 37만 4천). 둘 다 하면 기존 기본형 묶음(평 2.1만 · 34평 71만 4천)이 더 쌈.
# 11/2 13:18 사용자 「머씨클린 10프로 11000원 홈페이지 사진 내용 사용 가능 이걸로 가자」 → 청소만 = 머씨클린(평 1.1만 · 25평 27.5 · 30평 33 · 34평 37.4 · 신축 분진 추가금 없음 · 7일 A/S · 내 몫 10%)
def clean_basic(py): return round(py*1.1,1)
def sj_basic(py): return round(py*1.1,1)
def split_table(rows):
    """rows: [(라벨, 공급평수)] → 평형 | 입주청소 | 새집증후군 더하면 | 같이 하면"""
    h='<table width="693" style="width:100%;border-collapse:collapse;table-layout:fixed;">'
    h+='<tr>'+''.join('<td style="%sbackground:#EEF2F7;font-weight:700;color:#1F3864;">%s</td>'%(TD,x) for x in ['평형','입주청소만','새집증후군만','둘 다 하면(묶음)'])+'</tr>'
    for lab,py in rows:
        h+='<tr><td style="%s">%s</td><td style="%s"><b>%s</b></td><td style="%s">%s</td><td style="%s">%s</td></tr>'%(TD,e(lab),TD,won(clean_basic(py)),TD,won(sj_basic(py)),TD,won(basic(py)))
    return h+'</table>\n\n'
SPLIT_NOTE='입주청소만 맡겨도 됩니다. 새집증후군만 따로 맡겨도 됩니다. 둘 다 하면 따로 맡길 때보다 묶음 금액이 낮습니다. 부가세는 따로이고 공급평수 기준입니다.'
def split_block(rows): return split_table(rows)+PS%e(SPLIT_NOTE)+BR

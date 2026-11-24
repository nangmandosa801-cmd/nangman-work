import sys, json, os
os.makedirs('img', exist_ok=True)   # 그림 폴더는 저장소에 없다(새 창에서 다시 그림)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_wolse_renew_'
J = json.load(open('ana.json'))
SRC = '국토교통부 아파트 전월세 실거래 · 2026년 11월 25일 내려받음'
u = J['same_dep']['use']; nu = J['same_dep']['nouse']; jz = J['jeonse']['use']; cv = J['conv_use_same']; p = J['pair']
cards3('img/' + S + '1_case.png', '갱신권을 쓴 계약인데 월세는 11.3% 올랐습니다',
       [('150만원', '종전 월세', False, '보증금 5억원'), ('167만원', '갱신한 월세', True, '보증금 5억원 그대로'), ('17만원', '한 달에 오른 돈', False, '150만원의 5%는 7만 5천원')],
       note=SRC + ' · 마포구 래미안밤섬리베뉴Ⅰ 전용 84.99㎡ 4층 · 10월 17일 계약')
bars('img/' + S + '2_gt5.png', f"갱신권을 쓴 월세 계약 {u['gt5']}%가 5%보다 더 올랐습니다",
     [('전세 갱신|갱신권 사용', jz['gt5'], f"{jz['gt5']}%", False), ('월세 갱신|갱신권 사용', u['gt5'], f"{u['gt5']}%", True), ('월세 갱신|갱신권 안 씀', nu['gt5'], f"{nu['gt5']}%", False)],
     note='국토교통부 전월세 실거래 · 서울 아파트 8월 1일~11월 24일 계약 · 5% 넘게 오른 비율')
cards3('img/' + S + '3_conv.png', '보증금까지 합쳐 보는 예시 계산',
       [(f"{u['gt5']}%", '월세만 보면 5% 초과', False, f"{u['n']:,}건 중 {u['gt5_n']:,}건"), (f"{cv['r50']['le50']}%", '합쳐서 재면 5% 이하', True, '보증금을 연 5%로 바꾼 예시'), (f"{cv['r45']['le50']}%", '연 4.5%로 바꾸면', False, '같은 계약 · 5% 이하 비율')],
       note='갱신권을 쓴 서울 월세 갱신 · 보증금 그대로 · 예시 계산이며 법 적용 판정이 아님')
cards3('img/' + S + '4_new.png', '새로 구한 월세가 갱신한 이웃보다 비쌉니다',
       [('15만원', '새 계약이 더 내는 월세', True, '한가운데 묶음 기준'), (f"{p['new_higher']}%", '새 계약이 더 비싼 묶음', False, f"{p['n']:,}묶음 가운데"), (f"{p['med_rate']}%", '갱신 월세보다 높은 폭', False, '한가운데 묶음 기준')],
       note='국토교통부 전월세 실거래 · 묶음 = 단지 · 면적 · 보증금이 같은 새 계약과 갱신')
print('fig ok')

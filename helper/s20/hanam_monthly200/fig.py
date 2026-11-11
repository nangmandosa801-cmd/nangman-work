import sys, json
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
import viz2d
S = 'nangman_hanam_monthly200_'
J = json.load(open('ana.json')); R = J['rates']; E = {r['eq']: r for r in J['by_eq']}
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
SRC = '하남 아파트 매매 실거래 · 2026년 8~10월 계약 · 해제 · 직거래 뺌'
r = R['4.6']; e3 = E[30000]
# 1. 숫자 카드 3개
cards3('img/' + S + '1_cards.png', f"월 200만원이면 대출 {uk(r['loan'])}, 모은 돈 3억이면 집값은?",
       [(uk(r['loan']), '갚을 수 있는 대출', True, '연 4.6% · 30년 · 매달 같은 돈'),
        (uk(e3['first']), '모은 돈 3억 · 생애최초', False, '집값의 70%까지 대출'),
        (uk(e3['gen']), '모은 돈 3억 · 생애최초 아님', False, '하남은 규제지역 · 40%까지')],
       note='떼어 두는 돈(세금 · 중개보수 · 이사비) 1,500만원 · 집값은 100만원 아래 버림 · 실제 한도는 은행 심사에서 정해짐')
# 2. 금리별 대출
bars('img/' + S + '2_rate.png', f"금리 2%포인트 오르면 빌릴 돈은 {uk(R['4.6']['loan'] - R['6.6']['loan'])} 줄어듭니다",
     [('연 4.6%', R['4.6']['loan'] / 1e4, uk(R['4.6']['loan']), True), ('연 5.6%', R['5.6']['loan'] / 1e4, uk(R['5.6']['loan']), False),
      ('연 6.6%', R['6.6']['loan'] / 1e4, uk(R['6.6']['loan']), False)],
     note='한 달 200만원 · 30년 · 원리금균등 · 5대 은행 5년 고정형 주담대 연 4.55~6.868%(11월 2일 · 노컷뉴스 11월 3일)')
# 3. 모은 돈별 닿는 거래(생애최초)
it = [(f"모은 돈 {uk(e['eq'])}|집값 {uk(e['first'])}까지", e['k_first'], f"{e['k_first']}건", e['eq'] == 30000) for e in J['by_eq']]
bars('img/' + S + '3_eq.png', f"모은 돈 3억, 하남 84㎡ · 59㎡ {J['hanam_n']}건 중 {e3['k_first']}건에 닿습니다", it,
     note='생애최초 · 월 200만원 · 연 4.6% · 30년 · ' + SRC)
# 4. 동별 84㎡ 가운데 값(거래 많은 5개 동)
dd = sorted(J['dong84'], key=lambda x: -x['n'])[:5]; dd.sort(key=lambda x: x['med'])
bars('img/' + S + '4_dong.png', f"하남 84㎡, 덕풍동 {uk(dd[0]['med'])}은 감이동의 절반",
     [(f"{x['dong']}|{x['n']}건", x['med'] / 1e4, uk(x['med']), x['dong'] == '덕풍동') for x in dd], note=SRC)
viz2d.thumb('img/' + S + 'thumb.png', [R['6.6']['loan'], R['5.6']['loan'], R['4.6']['loan'], e3['first'], E[40000]['first']], hi=3)
print('fig ok', [x['dong'] for x in dd])

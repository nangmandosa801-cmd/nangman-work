import sys, json, os
os.makedirs('img', exist_ok=True)   # 그림 폴더는 저장소에 없다(새 창에서 다시 그림)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_salary_5000_'
J = json.load(open('ana.json'))
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
COND = '연 4.5% · 30년 · 다른 대출 없음 · 은행 DSR 40% · 수도권 기준'
L = J['loan']
cards3('img/' + S + '1_loan.png', f"연봉 5천, 주택담보대출은 {uk(L['주기형'])}원까지 나옵니다",
       [(uk(L['변동형']), '변동형', False, '6개월마다 금리가 바뀜'), (uk(L['혼합형']), '혼합형', False, '5년 고정 뒤 변동'), (uk(L['주기형']), '5년 주기형', True, '5년마다 금리를 새로 정함')],
       note=COND + f" · 변동형은 {uk(J['gap'])}원이 적음")
cards3('img/' + S + '2_price.png', f"연봉 5천으로 닿는 집값은 {uk(J['price'])}원입니다",
       [(uk(L['주기형']), '빌리는 돈', False, '5년 주기형 한도'), (uk(J['price']), '닿는 집값', True, '집값의 70%를 빌릴 때'), (uk(J['own']), '필요한 내 돈', False, '세금 · 중개보수는 따로')],
       note=COND + f" · 한 달 갚는 돈 {J['pay']:.1f}만원".replace('.0만', '만'))
t = J['top84'][:5]
bars('img/' + S + '3_sgg.png', f"연봉 5천으로 닿는 84㎡, {t[0]['sgg']}에 가장 많습니다",
     [(f"{x['sgg']}|그 지역 84㎡의 {x['share']}%", x['k'], f"{x['k']}건", n == 0) for n, x in enumerate(t)],
     note=f"집값 {uk(J['price'])}원 아래로 팔린 수도권 84㎡ {J['k84']:,}건 가운데 · 2026년 8~10월 계약 · 서울은 {J['sido84'].get('서울', 0)}건")
o = J['own_rows']
bars('img/' + S + '4_own.png', f"내 돈이 {uk(o[1]['own'])}원이면 닿는 84㎡는 {o[1]['s84']}%로 줄어듭니다",
     [(f"내 돈 {uk(x['own'])}|집값 {uk(x['price'])}까지", x['s84'], f"{x['s84']}%", n == 3) for n, x in enumerate(o)],
     note=f"연봉 5천 · 집값의 70%까지 빌릴 때 · 수도권 84㎡ 실거래 {J['n84']:,}건 가운데 닿는 비율 · 2026년 8~10월 계약")
print('fig ok')

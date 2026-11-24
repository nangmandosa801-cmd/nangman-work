import sys, json, os
os.makedirs('img', exist_ok=True)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_salary_8000_'
J = json.load(open('ana.json'))
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
COND = '연 4.5% · 30년 · 다른 대출 없음 · 은행 DSR 40% · 수도권 기준'
L = J['loan']; R = J['reg']
cards3('img/' + S + '1_loan.png', f"연봉 8천, 주택담보대출은 {uk(L['주기형'])}원까지 나옵니다",
       [(uk(L['변동형']), '변동형', False, '6개월마다 금리가 바뀜'), (uk(L['혼합형']), '혼합형', False, '5년 고정 뒤 변동'), (uk(L['주기형']), '5년 주기형', True, '5년마다 금리를 새로 정함')],
       note=COND + f" · 변동형은 {uk(J['gap'])}원이 적음")
bars('img/' + S + '2_seoul.png', f"내 돈 {uk(J['own'])}원, 생애최초면 서울 84㎡ {R['first70']['seoul']}건",
     [(f"생애최초 70%|집값 {uk(R['first70']['price'])}까지", R['first70']['seoul'], f"{R['first70']['seoul']}건", True),
      (f"서민 · 실수요자 60%|집값 {uk(R['sm60']['price'])}까지", R['sm60']['seoul'], f"{R['sm60']['seoul']}건", False),
      (f"그 밖 무주택 40%|집값 {uk(R['base40']['price'])}까지", R['base40']['seoul'], f"{R['base40']['seoul']}건", False)],
     note=f"연봉 8천 · 서울 84㎡ 실거래 {R['n_seoul']:,}건 가운데 그 값 아래 · 2026년 8~10월 계약 · 서민 · 실수요자는 부부 합산 연소득 9천만원 이하 등 세 요건")
t = J['top84'][:5]
bars('img/' + S + '3_sgg.png', f"연봉 8천으로 닿는 84㎡, {t[0]['sgg']}에 가장 많습니다",
     [(f"{x['sgg']}|그 지역 84㎡의 {x['share']}%", x['k'], f"{x['k']}건", n == 0) for n, x in enumerate(t)],
     note=f"집값 {uk(J['price'])}원 아래로 팔린 수도권 84㎡ {J['k84']:,}건 가운데 · 2026년 8~10월 계약 · 규제지역 밖 {J['nonreg84_share']}%")
o = J['own_rows']
bars('img/' + S + '4_own.png', f"내 돈이 {uk(o[0]['own'])}원이면 닿는 84㎡는 {o[0]['s84']}%",
     [(f"내 돈 {uk(x['own'])}|집값 {uk(x['price'])}까지", x['s84'], f"{x['s84']}%", n == 3) for n, x in enumerate(o)],
     note=f"연봉 8천 · 집값의 70%까지 빌릴 때 · 수도권 84㎡ 실거래 {J['n84']:,}건 가운데 닿는 비율 · 2026년 8~10월 계약")
print('fig ok')

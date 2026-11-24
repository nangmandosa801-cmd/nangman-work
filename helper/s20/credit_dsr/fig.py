import sys, json, os
os.makedirs('img', exist_ok=True)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_credit_dsr_'
J = json.load(open('ana.json'))
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
COND = '연봉 6천 · 주담대 연 4.5% · 30년 · 5년 주기형 · 신용대출 연 6% · 은행 DSR 40% · 수도권'
r = J['rows']
cards3('img/' + S + '1_cut.png', f"신용대출 5천만원이 주담대 한도 {uk(r[3]['cut'])}원을 가져갑니다",
       [(uk(r[0]['loan']), '신용대출 없을 때', False, '주담대 한도'), (uk(r[3]['loan']), '신용대출 5천만원', True, '주담대 한도'), (uk(J['per1000']), '신용대출 1천만원마다', False, '줄어드는 한도')],
       note=COND)
bars('img/' + S + '2_rows.png', '신용대출이 늘수록 주담대 한도는 이렇게 줄어듭니다',
     [(f"신용대출 {uk(x['credit']) if x['credit'] else '0'}|한도가 집값 70%일 때 84㎡ {x['s84']}%", x['loan'], uk(x['loan']), n == 3) for n, x in enumerate(r)],
     note="연봉 6천 · 연 4.5% · 30년 · 주기형 · 84㎡ = 수도권 실거래 가운데 한도 ÷ 0.7 아래 비율")
c = J['choice']
bars('img/' + S + '3_choice.png', f"신용대출을 먼저 갚으면 닿는 84㎡가 {c['pay_k']:,}건으로 늘어납니다",
     [(f"5천을 남겨 둘 때|내 돈 2억 · 집값 {uk(c['keep_price'])}까지", c['keep_k'], f"{c['keep_k']:,}건", False),
      (f"5천을 먼저 갚을 때|내 돈 1억 5천 · 집값 {uk(c['pay_price'])}까지", c['pay_k'], f"{c['pay_k']:,}건", True)],
     note=f"연봉 6천 · 모은 돈 2억 · 집값 = 내 돈 + 주담대 한도 · 수도권 84㎡ {J['n84']:,}건")
print('fig ok')

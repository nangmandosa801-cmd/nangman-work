import sys, json, os
os.makedirs('img', exist_ok=True)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_apt4eok_'
J = json.load(open('ana.json')); C = J['cases']
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
bars('img/' + S + '1_cash.png', '4억 아파트, 현금은 1억 2천에서 2억 4천까지',
     [('생애최초 · 규제지역 밖 무주택|대출 70% · 2억 8,000만', C['70']['own'], uk(C['70']['own']), True),
      ('규제지역 서민 · 실수요자|대출 60% · 2억 4,000만', C['60']['own'], uk(C['60']['own']), False),
      ('규제지역 그 밖 무주택|대출 40% · 1억 6,000만', C['40']['own'], uk(C['40']['own']), False)],
     note=f"대출을 비율 한도까지 받을 때 집값에서 모자라는 돈 · 취득세 {J['tax']}만원 · 중개보수는 따로")
cards3('img/' + S + '2_inc.png', '2억 8천을 빌리려면 연봉이 이만큼 필요합니다',
       [(uk(C['70']['inc_주기형']), '5년 주기형', True, '스트레스 금리를 가장 적게 얹음'), (uk(C['70']['inc_혼합형']), '혼합형', False, '5년 고정 뒤 변동'), (uk(C['70']['inc_변동형']), '변동형', False, '6개월마다 금리가 바뀜')],
       note='세전 연봉 · 연 4.5% · 30년 · 다른 대출 없음 · 은행 DSR 40% · 수도권 스트레스 금리 기준')
t = J['top84'][:5]
bars('img/' + S + '3_sgg.png', f"4억 이하 84㎡, {t[0]['sgg']}에서 가장 많이 팔렸습니다",
     [(f"{x['sgg']}|그 지역 84㎡의 {x['share']}%", x['k'], f"{x['k']}건", n == 0) for n, x in enumerate(t)],
     note=f"4억원 아래로 팔린 수도권 84㎡ {J['k84']:,}건 가운데 · 2026년 8~10월 계약 · 서울은 {J['sido84'].get('서울', 0)}건")
print('fig ok')

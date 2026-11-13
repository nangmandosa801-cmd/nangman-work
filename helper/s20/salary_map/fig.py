import sys, json
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_salary_map_'
J = json.load(open('ana.json')); R = {r['inc']: r for r in J['rows']}; X = J['x']
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
COND = '연 4.5% · 30년 · 다른 대출 없음 · 은행 DSR 40% · 수도권 기준'
r10 = R[10000]; r6 = R[6000]
# 1. 연봉 1억 · 유형별 한도
cards3('img/' + S + '1_cards.png', f"연봉 1억, 고르는 금리에 따라 한도가 {uk(r10['gap'])}원 다릅니다",
       [(uk(r10['변동형']), '변동형', False, '6개월마다 금리가 바뀜'),
        (uk(r10['혼합형']), '혼합형', False, '5년 고정 뒤 변동'),
        (uk(r10['주기형']), '5년 주기형', True, '5년마다 금리를 새로 정함')],
       note=COND + ' · 셋 다 한도 6억원에 못 미침')
# 2. 6억을 다 빌리는 데 필요한 연봉
C = J['cap_income']
cards3('img/' + S + '2_cap.png', '6억을 다 빌리려면 연봉 1억 450만원부터입니다',
       [(uk(C['주기형']), '5년 주기형', True, '연봉의 5.7배까지'),
        (uk(C['혼합형']), '혼합형', False, '연봉의 5.1배까지'),
        (uk(C['변동형']), '변동형', False, '연봉의 4.8배까지')],
       note=COND + f" · 6억원이면 한 달 {J['pay_6eok']:.0f}만원")
# 3. 연봉별 주기형 한도 (막대 5)
it = [(f"연봉 {uk(i)}", R[i]['주기형'] / 1e4, uk(R[i]['주기형']), i == 6000) for i in (4000, 5000, 6000, 8000, 10000)]
bars('img/' + S + '3_loan.png', f"연봉 6천만원이면 {uk(r6['주기형'])}원까지 빌릴 수 있습니다", it,
     note='5년 주기형 · ' + COND + ' · 변동형은 17% 적음')
# 4. 연봉별 닿는 84㎡ 거래 비율 (막대 5)
it = [(f"연봉 {uk(i)}|집값 {uk(R[i]['price'])}까지", R[i]['s84'], f"{R[i]['s84']}%", i == 6000) for i in (4000, 5000, 6000, 8000, 10000)]
bars('img/' + S + '4_share.png', f"연봉 6천만원이면 수도권 84㎡ 거래의 {r6['s84']}%에 닿습니다", it,
     note=f"수도권 84㎡ 매매 실거래 {J['n84']:,}건 · 2026년 8~10월 계약 · 해제 · 직거래 뺌 · 닿는 집값 = 5년 주기형 한도 ÷ 0.7")
# 5. 연봉 6천으로 닿는 84㎡ 거래가 많은 다섯 곳
t = r6['top84'][:5]
bars('img/' + S + '5_sgg.png', f"연봉 6천으로 닿는 84㎡, {t[0]['sgg']}에 가장 많습니다",
     [(f"{x['sgg']}|그 지역 84㎡의 {x['share']}%", x['k'], f"{x['k']}건", n == 0) for n, x in enumerate(t)],
     note=f"집값 {uk(r6['price'])}원 아래로 팔린 84㎡ {r6['k84']:,}건 가운데 · 2026년 8~10월 계약 · 서울은 {X['r6_seoul']}건")
print('fig ok')

# 대표 사진(01) — C형 썸네일
from PIL import Image, ImageDraw, ImageFont
def kr(p, s):
    for i in range(10):
        f = ImageFont.truetype(p, s, index=i)
        if 'KR' in ' '.join(f.getname()): return f
SE='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; SA='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
def make(path, top, l1, l2, big, sub):
    W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
    d.text((70,95),top,font=kr(SA,28),fill='#AFC0D8',anchor='lm')
    d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
    d.text((W/2,360),l1,font=kr(SE,80),fill='#F4F1EA',anchor='mm')
    d.text((W/2,485),l2,font=kr(SE,60),fill='#F4F1EA',anchor='mm')
    d.text((W/2,605),big,font=kr(SE,100),fill='#D4B04C',anchor='mm')
    d.text((W/2,715),sub,font=kr(SA,32),fill='#AFC0D8',anchor='mm')
    im.save(path)
make('img/' + S + 'thumb.png', '낭만 부동산 · 이 돈이면 어디 · 연봉 편', '연봉별 대출한도', '연봉 1억이 빌리는 돈', uk(r10['주기형']), '가장 넉넉한 대출로도 한도 6억을 못 채웁니다')
print('thumb ok')

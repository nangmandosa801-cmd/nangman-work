import sys, json
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars
import viz2d
S = 'nangman_hanam_renewal_'
J = json.load(open('ana.json')); U, NU, V = J['use'], J['nouse'], J['vs_new']
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
SRC = '하남 아파트 전세 재계약 · 2026년 1월 1일~11월 11일 계약 · 국토교통부 실거래'
# 1. 5% 넘게 올린 비율
bars('img/' + S + '1_over5.png', f"갱신권 안 쓴 재계약, {NU['over5_pct']}%가 5% 넘게 올렸습니다",
     [(f"갱신권 씀|{U['n']:,}건 중 {U['over5']}건", U['over5_pct'], f"{U['over5_pct']}%", False),
      (f"갱신권 안 씀|{NU['n']:,}건 중 {NU['over5']}건", NU['over5_pct'], f"{NU['over5_pct']}%", True)],
     note='전세에서 전세로 재계약 · ' + SRC)
# 2. 위례롯데캐슬 10월
bars('img/' + S + '2_story.png', '같은 날 재계약, 한 집은 3,100만 올리고 한 집은 8,000만',
     [('14층 · 갱신권 씀|10월 17일 · 6억 2,000만에서', 6.51, '6억 5,100만', True),
      ('9층 · 갱신권 안 씀|10월 17일 · 6억 7,000만에서', 7.5, '7억 5,000만', False),
      ('14층 · 새 세입자|10월 14일', 8.0, '8억', False)],
     note='하남 학암동 위례롯데캐슬 전용 84.98㎡ 전세 · 국토교통부 실거래 · 11월 12일 내려받음')
# 3. 새 전세보다 낮은 폭
bars('img/' + S + '3_vsnew.png', f"갱신권 쓴 재계약, 새 전세보다 {uk(V['use']['med_gap'])} 낮습니다",
     [(f"갱신권 씀|{V['use']['n']:,}건", V['use']['med_gap'] / 1e4, uk(V['use']['med_gap']), True),
      (f"갱신권 안 씀|{V['nouse']['n']:,}건", V['nouse']['med_gap'] / 1e4, uk(V['nouse']['med_gap']), False)],
     note='같은 단지 · 같은 면적 · 앞뒤 한 달 새 전세 가운데 값과의 차이 · 하남 2026년 1~11월 계약')
viz2d.thumb('img/' + S + 'thumb.png', [U['med_pct'], NU['med_pct'], J['by_area']['84㎡ 안팎']['nouse']['med_pct']], hi=2)
print('fig ok')

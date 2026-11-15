import sys, json, os
os.makedirs('img', exist_ok=True)   # 그림 폴더는 저장소에 없다(새 창에서 다시 그림)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_detective_03_'
J = json.load(open('ana.json'))
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
SRC = '국토교통부 아파트 매매 실거래 · 2026년 11월 16일 내려받음 · 해제 거래 뺌'
d = J['ddm']['202610']; sp = J['songpa']['202609']; R = J['rank']['202610']
cards3('img/' + S + '1_ddm.png', f"동대문구 10월 {d['n']}건, {d['묶음']}건은 하루 한 건물입니다",
       [(f"{d['n']}건", '10월 동대문구 매매', False, '서울 25개 구 가운데 가장 많음'), (f"{d['묶음']}건", '10월 8일 한 건물', True, '전부 직거래 · 법인끼리'), (f"{d['뺀']}건", '나머지 거래', False, '25개 구 가운데 열째')],
       note=SRC + ' · 10월 계약은 신고 기한이 남아 더 늘 수 있음')
t = R['넣고'][:5]
bars('img/' + S + '2_rank.png', '10월 서울에서 거래가 가장 많은 동대문구, 한 건물을 빼면 열째입니다',
     [(f"{k}|{'한 건물 ' + str(d['묶음']) + '건 포함' if k == '동대문구' else '10월 계약'}", n, f'{n}건', k == '동대문구') for k, n in t],
     note=SRC + f" · 동대문구는 묶음을 빼면 {d['뺀']}건")
bars('img/' + S + '3_med.png', f"묶음 하나가 가운데 값을 {uk(d['med뺀'])}에서 {uk(d['med'])}으로 바꿉니다",
     [('동대문구 10월|전체', d['med'] / 10000, uk(d['med']), True), ('동대문구 10월|묶음 뺌', d['med뺀'] / 10000, uk(d['med뺀']), False),
      ('송파구 9월|전체', sp['med'] / 10000, uk(sp['med']), False), ('송파구 9월|묶음 뺌', sp['med뺀'] / 10000, uk(sp['med뺀']), False)],
     note='국토교통부 아파트 매매 실거래 · 2026년 11월 16일 내려받음 · 가운데 값 = 금액 순으로 세운 한가운데 값')
s = J['share'][:5]
bars('img/' + S + '4_share.png', f"묶음이 그 달 거래의 절반을 넘긴 구는 두 곳입니다",
     [(f"{x['구'].split()[-1]} {int(x['월'][4:])}월|{x['n']}건 중 {x['b']}건", x['share'], f"{x['share']}%", n == 0) for n, x in enumerate(s)],
     note='국토교통부 아파트 매매 실거래 · 2026년 11월 16일 내려받음 · 묶음 = 같은 날 한 단지 직거래 10건 이상')
print('fig ok')

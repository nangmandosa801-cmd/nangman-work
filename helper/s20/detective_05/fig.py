import sys, json, os
os.makedirs('img', exist_ok=True)   # 그림 폴더는 저장소에 없다(새 창에서 다시 그림)
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3
S = 'nangman_detective_05_'
J = json.load(open('ana.json'))
SRC = '국토교통부 아파트 매매 실거래 · 2026년 11월 23일 내려받음'
c = J['cat']; b = J['B']; n = J['meta']['n_cancel']
cards3('img/' + S + '1_case.png', '해제된 줄 바로 옆에 같은 날 · 같은 값 · 같은 층이 있습니다',
       [('27억 8,000만', '10월 12일 계약', False, '해제사유발생일 10월 30일'), ('27억 8,000만', '10월 12일 계약', True, '같은 층 · 11월 10일 등기'), ('0원', '두 줄의 값 차이', False, '날짜도 층도 같음')],
       note=SRC + ' · 마포구 염리동 마포프레스티지자이 전용 84.94㎡ 11층')
bars('img/' + S + '2_cat.png', f"해제 {n:,}건 가운데 짝이 없는 거래는 {c['C']}건입니다",
     [('날 · 값 · 층 같은|줄이 살아 있음', c['A'], f"{c['A']:,}건", False), ('같은 값 줄이|뒤 날짜로 있음', b['같은값'], f"{b['같은값']}건", False),
      ('값이 다른 줄이|같은 층에 있음', J['changed'], f"{J['changed']}건", False), ('살아 있는|줄 없음', c['C'], f"{c['C']}건", True)],
     note=SRC + ' · 짝 = 단지 · 면적 · 층이 같은 미해제 줄')
r = J['ym_rate']
bars('img/' + S + '3_ym.png', '오래된 계약일수록 해제 표시가 많습니다',
     [('8월 계약|', r['202608'], f"{r['202608']}%", True), ('9월 계약|', r['202609'], f"{r['202609']}%", False), ('10월 계약|', r['202610'], f"{r['202610']}%", False), ('11월 계약|21일까지', r['202611'], f"{r['202611']}%", False)],
     note=SRC + ' · 계약 월별 매매 신고 가운데 해제 표시가 붙은 비율')
cards3('img/' + S + '4_gone.png', f"짝이 없는 {c['C']}건, 값은 옆집과 비슷했습니다",
       [(f"{c['C']}건", '짝이 없는 해제 거래', True, f"해제 {n:,}건의 {J['cat_pct']['C']}%"), (f"{J['cmp_C']['med_rate']}%", '옆집 가운데 값과 차이', False, f"견줄 수 있는 {J['cmp_C']['n']}건 기준"), (f"{int(J['wait']['C']['med'])}일", '계약일 → 해제사유발생일', False, '한가운데 거래 기준')],
       note=SRC + ' · 옆집 = 같은 단지 같은 면적 · 계약일 앞뒤 30일 · 중개거래 2건 이상')
print('fig ok')

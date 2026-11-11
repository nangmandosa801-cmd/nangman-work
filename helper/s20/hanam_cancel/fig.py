import sys, json
sys.path.insert(0, '/home/claude/helper/pg'); sys.path.insert(0, '/home/claude/tools/tistory')
from fig2d import bars, cards3, one
import viz2d
S = 'nangman_hanam_cancel_'
J = json.load(open('ana.json'))
SRC = '국토교통부 아파트 매매 실거래 · 하남시 · 2026년 1월 1일~11월 9일 계약 · 11월 12일 내려받음'
# 1. 숫자 카드 3개
cards3('img/' + S + '1_cards.png', f"해제 표시 신고가 {J['new_high']}건 중 {J['re_newhigh']}건은 같은 줄이 또 있습니다",
       [(f"{J['cancel']}건", '하남 아파트 매매 해제', False, f"{J['n']:,}건 중"),
        (f"{J['new_high']}건", '그중 그때까지 가장 높은 값', True, '같은 단지 · 같은 면적 기준'),
        (f"{J['re_newhigh']}건", '같은 날 · 같은 층 · 같은 값 줄이 또 있음', False, f"{J['re_newhigh_reg']}건은 등기까지 끝남")],
       note=SRC)
# 2. 스타힐스 59㎡ 흐름
bars('img/' + S + '2_story.png', '해제 표시가 붙은 11억 6,500만원, 넉 달 뒤 12억 2,500만원',
     [('2025년 12월|9층 · 그 전 가장 높은 값', 9.95, '9억 9,500만', False),
      ('2026년 3월 13일|15층 · 4월 7일 해제 표시', 11.65, '11억 6,500만', True),
      ('2026년 5월 23일|11층 · 7월 21일 해제 표시', 11.76, '11억 7,600만', False),
      ('2026년 7월 14일|12층', 12.25, '12억 2,500만', False),
      ('2026년 9월 17일|12층', 12.45, '12억 4,500만', False)],
     note='하남 망월동 미사강변스타힐스 전용 59.79㎡ · 국토교통부 실거래 · 11월 12일 내려받음')
# 3. 계약에서 해제까지 걸린 날
g = J['all_gap']
bars('img/' + S + '3_gap.png', f"해제 62건 중 {g['over30']}건은 30일 넘게 조회 화면에 떠 있었습니다",
     [('7일 안', g['le7'], f"{g['le7']}건", False), ('8~30일', g['mid'], f"{g['mid']}건", False), ('31일 넘게', g['over30'], f"{g['over30']}건", True)],
     note=f"하남 아파트 매매 2026년 계약 · 계약일에서 해제사유발생일까지 · 가운데 값 {J['gap_med']:.0f}일")
# 4. 써먹을 한 가지
one('img/' + S + '4_one.png', '해제 표시를 봤을 때 할 일 하나', '같은 날 · 같은 층 · 같은 값 줄이 또 있는지 찾는다',
    note='있으면 등기일자 칸을 본다 · 날짜가 있으면 그 값에 실제로 소유권이 넘어간 거래')
# 썸네일 (viz2d thumb · 글자 없음)
viz2d.thumb('img/' + S + 'thumb.png', [9.95, 11.65, 11.76, 12.25, 12.45], hi=1)
print('fig ok')

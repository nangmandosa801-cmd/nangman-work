import sys, json
sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars
S = 'nangman_detective_01_'
J = json.load(open('ana.json'))
dc, bc = J['direct_cmp'], J['broker_cmp']
p_d = dc['lt10'] / dc['n'] * 100; p_b = bc['lt10'] / bc['n'] * 100
# 1. 부영 59㎡ 9월 신고 두 건과 8~10월 중개거래 중앙값
bars('img/' + S + '1_two.png', '9월 신고 두 건은 6억 1천과 9억, 남은 거래는 8억 3천',
     [('9월 9일 · 7층|직거래', 6.1, '6억 1,000만', False),
      ('8~10월 중개거래 6건|중앙값', 8.3, '8억 3,000만', True),
      ('9월 19일 · 14층|10월 28일 해제', 9.0, '9억', False)],
     note='하남 창우동 부영 전용 59.97㎡ · 2026년 8~10월 계약 · 국토교통부 실거래 11월 12일 내려받음')
# 2. 같은 단지 · 같은 면적 중앙값보다 10% 넘게 싼 거래 비율
bars('img/' + S + '2_direct.png', f'직거래 셋 중 하나는 10% 넘게 쌌습니다',
     [(f'중개거래|{bc["n"]:,}건 중 {bc["lt10"]:,}건', p_b, f'{p_b:.1f}%', False),
      (f'직거래|{dc["n"]:,}건 중 {dc["lt10"]:,}건', p_d, f'{p_d:.1f}%', True)],
     note='수도권 아파트 매매 · 2026년 8~10월 계약 · 같은 단지 같은 면적 앞뒤 한 달 중개거래 중앙값보다 10% 넘게 낮은 거래 비율')
from PIL import Image, ImageDraw, ImageFont
def kr(p, s):
    for i in range(10):
        f = ImageFont.truetype(p, s, index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_ = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W = 1000; im = Image.new('RGB', (W, W), '#203864'); d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill='#D4B04C'); d.rectangle([0, W - 14, W, W], fill='#D4B04C')
d.text((70, 95), '낭만 부동산 · 실거래 탐정 1화 · 하남 창우동', font=kr(san, 28), fill='#AFC0D8', anchor='lm')
d.line([70, 248, 930, 248], fill='#3A5A8A', width=3); d.line([70, 782, 930, 782], fill='#3A5A8A', width=3)
d.text((W / 2, 360), '하남 부영아파트 59㎡', font=kr(ser_, 80), fill='#F4F1EA', anchor='mm')
d.text((W / 2, 485), '9월 신고 두 건 차이', font=kr(ser_, 60), fill='#F4F1EA', anchor='mm')
d.text((W / 2, 605), '2억 9,000만', font=kr(ser_, 100), fill='#D4B04C', anchor='mm')
d.text((W / 2, 715), '6억 1,000만은 직거래 · 9억은 39일 뒤 해제', font=kr(san, 32), fill='#AFC0D8', anchor='mm')
im.save('img/' + S + 'thumb.png')
print('fig ok', round(p_b, 1), round(p_d, 1))

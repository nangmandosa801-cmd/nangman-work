import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_hakgun_ep1_'
# 그림 1: 대치동 84㎡ 새 세입자 전세 · 입주 달별 건수(605건 가운데 겨울~봄 다섯 달 · 열두 달 전체는 본문)
bars('img/'+S+'1_movein.png','대치동 전세 넷 중 하나는 2월에 입주했습니다',
     [('12월',64,'64건',False),('1월',58,'58건',False),('2월',140,'140건',True),('3월',46,'46건',False),('4월',20,'20건',False)],
     note='대치동 84㎡ 새 세입자 전세 605건 · 2024~2025년 계약 · 입주 달 = 계약 기간 시작 달 · 국토교통부 전월세 실거래')
# 그림 2: 2월 입주 몫 · 학군 동과 같은 구 비학군 동(목동 · 신월동은 본문 표)
cards3('img/'+S+'2_feb.png','2월 입주 몫, 학군 동이 같은 구 다른 동보다 높았습니다',
     [('23.1%','대치동',True,'세곡 · 자곡 · 율현동 8.8%'),('18.0%','중계동',False,'하계동 13.7%'),('16.4%','반포동',False,'방배동 12.7%')],
     note='84㎡ 새 세입자 전세 가운데 2월에 입주한 계약 · 2024~2025년 계약 · 국토교통부 전월세 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 1화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'학군지 아파트',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'2021 고점 대비 덜 빠진 곳',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'넷 중 둘',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'대치 · 반포는 버텼고 목동 · 중계는 15~19% 빠졌습니다',font=kr(san,31),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')

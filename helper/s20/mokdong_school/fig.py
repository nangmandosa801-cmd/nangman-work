import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_mokdong_school_'
# 그림 1: 앞단지 65㎡ · 뒷단지 71㎡ 매매 중앙값 2025 · 2026 (단지 14곳은 본문 표)
bars('img/'+S+'1_dan.png','앞단지와 뒷단지 차이, 3억 3,250만에서 1억 8,500만으로',
     [('앞단지 65㎡|2025년',21.925,'21억 9,250만',False),('뒷단지 71㎡|2025년',18.6,'18억 6,000만',False),('앞단지 65㎡|2026년',23.8,'23억 8,000만',True),('뒷단지 71㎡|2026년',21.95,'21억 9,500만',False)],
     note='목동 신시가지 매매 중앙값 · 앞단지 = 1~7단지 · 뒷단지 = 8~14단지 · 2026년은 1~10월 · 국토교통부 실거래')
# 그림 2: 2021 → 2023 변화 (해마다 값은 본문 표)
cards3('img/'+S+'2_year.png','2023년 목동은 9~10% 내렸고 신길동 우성2는 21% 내렸습니다',
     [('−9.0%','목동 앞단지 65㎡',True,'16억 7,500만 → 15억 2,500만'),('−9.8%','목동 뒷단지 71㎡',False,'15억 3,000만 → 13억 8,000만'),('−20.9%','신길동 우성2 64㎡',False,'11억 → 8억 7,000만')],
     note='매매 중앙값 2021년 → 2023년 · 우성2는 2021년 3건 · 2023년 6건 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 3화 · 양천구 목동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'목동 아파트 시세',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'앞단지 · 뒷단지 차이',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 8,500만',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'65㎡ 23억 8천 · 71㎡ 21억 9,500 · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_pyeongchon_school_'
# 그림 1: 같은 현대홈타운 짝 · 2021년과 2026년 (해마다 값 · 다른 단지는 본문 표)
bars('img/'+S+'1_pair.png','같은 현대홈타운 차이, 4억 5,500만에서 6억 8,500만으로',
     [('호계 현대홈타운 85㎡|2021년',6.9,'6억 9,000만',False),('귀인마을 현대홈타운 80㎡|2021년',11.45,'11억 4,500만',False),('호계 현대홈타운 85㎡|2026년',7.15,'7억 1,500만',False),('귀인마을 현대홈타운 80㎡|2026년',14,'14억',True)],
     note='안양 동안구 매매 중앙값 · 호계는 1 · 2차 합침 · 2026년은 1~10월 · 국토교통부 실거래')
# 그림 2: 전세가율 다섯 단지 (초원 · 관악마을은 본문 표)
bars('img/'+S+'2_rate.png','전세가율은 학원가 옆 54~57%, 먼 단지 61~66%',
     [('귀인마을 현대홈타운 80㎡|전세 8억',57,'57%',True),('향촌 롯데 · 현대 85㎡|전세 7억 5,000만',54,'54%',False),('호계 현대홈타운 85㎡|전세 4억 3,500만',61,'61%',False),('비산동 삼성래미안 85㎡|전세 5억 2,000만',61,'61%',False),('무궁화마을 85㎡|전세 5억 8,000만',66,'66%',False)],
     note='2026년 새 세입자 전세 중앙값 ÷ 매매 중앙값 · 앞의 둘이 평촌 학원가 옆 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 7화 · 안양 평촌',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'평촌 학원가 아파트',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'같은 현대홈타운인데 차이',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'6억 8,500만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'귀인마을 80㎡ 14억 · 호계동 85㎡ 7억 1,500 · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

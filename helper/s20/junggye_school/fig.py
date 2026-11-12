import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_junggye_school_'
# 그림 1: 을지초 배정 네 단지 2026년 매매 중앙값 · 이름 아래 새 세입자 전세
bars('img/'+S+'1_ladder.png','을지초 배정 네 단지, 7억부터 14억까지 네 칸입니다',
     [('주공10단지 58㎡|전세 5억 100만',7.15,'7억 1,500만',False),('건영3차 84㎡|전세 8억',12.58,'12억 5,800만',False),('청구3차 84㎡|전세 8억',13.6,'13억 6,000만',True),('롯데우성 115㎡|전세 8억',14.125,'14억 1,250만',False)],
     note='중계동 매매 중앙값 · 2026년 1~10월 · 이름 아래는 새 세입자 전세 중앙값 · 국토교통부 실거래')
# 그림 2: 2026 ÷ 2021 (해마다 값은 본문 표)
cards3('img/'+S+'2_year.png','2026년 을지초 배정 84㎡는 2021년의 99%, 하계동은 94%',
     [('99%','청구3차 84㎡',True,'13억 8,000만 → 13억 6,000만'),('99%','건영3차 84㎡',False,'12억 6,500만 → 12억 5,800만'),('94%','하계동 두 단지 84㎡',False,'하계1청구 · 하계2현대')],
     note='2026년 1~10월 매매 중앙값 ÷ 2021년 매매 중앙값 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 5화 · 노원구 중계동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'중계동 아파트 시세',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'을지초 배정 84㎡',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'13억 6,000만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'청구3차 · 2021년 고점의 99% · 새 세입자 전세 8억',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

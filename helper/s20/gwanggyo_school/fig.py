import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_gwanggyo_school_'
# 그림 1: 광교 84㎡ 다섯 단지 2026년 매매 중앙값 · 이름 아래 2021년 대비 (12곳 전체는 본문 표)
bars('img/'+S+'1_dan.png','2021년을 20% 넘게 넘은 광교 84㎡는 세 단지입니다',
     [('자연앤힐스테이트|2021년보다 +22.6%',18.7,'18억 7,000만',True),('센트럴뷰|+23.8%',15.95,'15억 9,500만',False),('더리브|+23.7%',14.1,'14억 1,000만',False),('호반써밋|+4.2%',12.4,'12억 4,000만',False),('e편한세상 2차|+2.8%',10.9,'10억 9,000만',False)],
     note='광교 2011~2013년 준공 단지 84㎡ 매매 중앙값 · 2026년 1~10월 · 이름 아래는 2021년 중앙값 대비 · 국토교통부 실거래')
# 그림 2: 자연앤힐스테이트 84㎡ 2021 · 2023 · 2026 (다른 단지는 본문 표)
bars('img/'+S+'2_year.png','자연앤힐스테이트 84㎡, 2023년 −13.1% 뒤 2026년 +22.6%',
     [('2021년',15.25,'15억 2,500만',False),('2023년|2021년보다 −13.1%',13.25,'13억 2,500만',False),('2026년 1~10월|2021년보다 +22.6%',18.7,'18억 7,000만',True)],
     note='광교 자연앤힐스테이트 전용 84㎡ 매매 중앙값 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 8화 · 수원 광교',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'광교 자연앤힐스테이트',font=kr(ser_,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'84㎡ 매매 중앙값',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'18억 7,000만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2021년보다 22.6% 위 · 2026년 1~10월 43건 · 새 전세 9억 6천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

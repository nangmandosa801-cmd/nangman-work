import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_mapo_school_'
J=json.load(open('ana.json'))
T=J['대흥동 대흥동태영아파트']; G=J['상암동 상암월드컵파크4단지']
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
# 1. 대흥동과 상암 84㎡ · 2021년과 2026년
bars('img/'+S+'1_pair.png','대흥동과 상암 84㎡ 차이, 9,500만에서 4억 7,400만으로',
     [('상암 4단지|2021년',G['2021'][0]/10000,uk(G['2021'][0]),False),('대흥동태영|2021년',T['2021'][0]/10000,uk(T['2021'][0]),False),
      ('상암 4단지|2026년',G['2026'][0]/10000,uk(G['2026'][0]),False),('대흥동태영|2026년',T['2026'][0]/10000,uk(T['2026'][0]),True)],
     note='전용 84㎡ 매매 중앙값 · 2026년은 1~10월(대흥동태영 18건 · 상암월드컵파크4단지 13건) · 국토교통부 실거래')
# 2. 1~2월 전세 계약 비율
a=J['_A']['j2425']; m=J['_mapo']['j2425']; g=J['대흥동 마포그랑자이']['j2425']
cards3('img/'+S+'2_winter.png','겨울 전세 몰림, 학원가 옆 17.5%는 마포 전체와 같습니다',
     [(f'{a[1]/a[0]*100:.1f}%','염리 · 대흥 · 용강동',True,f'전세 {a[0]:,}건 중 1~2월'),(f'{m[1]/m[0]*100:.1f}%','마포구 전체',False,f'전세 {m[0]:,}건 중 1~2월'),(f'{g[1]/g[0]*100:.1f}%','마포그랑자이 84㎡',False,'2020년 2월 입주 단지')],
     note='2024~2025년 전세 계약 가운데 1 · 2월 계약 비율 · 국토교통부 전월세 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 10화 · 마포 염리 대흥',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'마포 학군지',font=kr(ser_,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'대흥동과 상암 84㎡ 차이',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'4억 7,400만',font=kr(ser_,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2021년에는 9,500만 · 대흥동태영 20억 7,400만 · 2026년 1~10월',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

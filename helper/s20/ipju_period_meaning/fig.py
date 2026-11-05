from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 부동산 용어 한 장',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'입주지정기간 뜻',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'500세대 이상 단지는',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'60일 이상',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'지나면 잔금 연체료 · 다음 날부터 관리비',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_ipju_period_meaning_thumb.png'); print('ok')

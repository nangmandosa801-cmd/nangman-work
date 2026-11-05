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
d.text((W/2,370),'분양권 전매제한 뜻',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'수도권 공공택지는',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'3년',font=kr(ser,120),fill='#D4B04C',anchor='mm')
d.text((W/2,718),'당첨자 발표일부터 · 교산 A2는 2028년 4월',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_jeonmae_meaning_thumb.png')

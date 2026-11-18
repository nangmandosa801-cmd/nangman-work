# 2화 썸네일 (1화 fig.py 와 같은 꼴 · 남색 카드 · 숫자 하나)
from PIL import Image,ImageDraw,ImageFont
S='nangman_cheolsan13_ep2_'
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축 따라가기 2화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'철산주공 13단지',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,470),'시공사 입찰',font=kr(ser,66),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'현대건설 혼자 → 유찰',font=kr(ser,74),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'현장설명회 3곳 가운데 입찰은 1곳 · 2차 입찰 12월',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png'); print('thumb ok')

import sys
from PIL import Image, ImageDraw, ImageFont
def kr(p, s):
    for i in range(10):
        f = ImageFont.truetype(p, s, index=i)
        if 'KR' in ' '.join(f.getname()): return f
SE='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; SA='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
def make(path, top, l1, l2, big, sub):
    W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
    d.text((70,95),top,font=kr(SA,28),fill='#AFC0D8',anchor='lm')
    d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
    d.text((W/2,360),l1,font=kr(SE,80),fill='#F4F1EA',anchor='mm')
    d.text((W/2,485),l2,font=kr(SE,60),fill='#F4F1EA',anchor='mm')
    d.text((W/2,605),big,font=kr(SE,100),fill='#D4B04C',anchor='mm')
    d.text((W/2,715),sub,font=kr(SA,32),fill='#AFC0D8',anchor='mm')
    im.save(path); im.save(path.replace('.png','_01.jpg'),quality=92)
T={'hanam_cancel':('낭만 부동산 · 실거래 탐정 · 하남','하남 아파트 신고가','올해 해제된 거래','23건','22건은 그 값 넘는 거래가 다시 나옴'),
 'hanam_monthly200':('낭만 부동산 · 이 돈이면 어디 · 하남','월 상환 200만원','하남에서 닿는 아파트','19건','모은 돈 3억 · 생애최초 · 30년 기준'),
 'hanam_renewal':('낭만 부동산 · 하남 이번 주','하남 전세 재계약','갱신권 안 쓰면 인상률','7.1%','갱신권 쓴 1,586건은 5% 넘은 곳 0건')}
for s,v in T.items(): make(f'{s}/img/nangman_{s}_thumb.png',*v); print(s)

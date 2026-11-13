import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_banpo_school_'
# 그림 1: 네 단지 84㎡ 2026년 매매 중앙값 · 이름 아래 새 세입자 전세
bars('img/'+S+'1_price.png','원베일리 84㎡ 매매 58억 7,500만, 전세는 21억',
     [('래미안원베일리|전세 21억',58.75,'58억 7,500만',True),('아크로리버파크|전세 18억',55.5,'55억 5,000만',False),('래미안퍼스티지|전세 18억',50.75,'50억 7,500만',False),('반포자이|전세 16억 5,000만',48,'48억',False)],
     note='반포 84㎡ 매매 중앙값 · 2026년 1~10월 · 이름 아래는 새 세입자 전세 중앙값 · 국토교통부 실거래')
# 그림 2: 2021 → 2023 변화 (아크로리버파크 +2.4%와 해마다 값은 본문 표)
cards3('img/'+S+'2_year.png','2023년 반포는 2021년보다 높았고 잠실엘스는 6.7% 낮았습니다',
     [('+5.6%','래미안퍼스티지 84㎡',True,'32억 9,500만 → 34억 8,000만'),('+5.3%','반포자이 84㎡',False,'30억 → 31억 6,000만'),('−6.7%','잠실엘스 84㎡',False,'24억 2,000만 → 22억 5,750만')],
     note='매매 중앙값 2021년 → 2023년 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 4화 · 서초구 반포',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'반포 아파트 시세',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'래미안원베일리 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'58억 7,500',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'새 세입자 전세 21억 · 전세가율 36% · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

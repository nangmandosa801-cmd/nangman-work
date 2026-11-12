import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_daechi_price_'
# 그림 1: 단지별 84㎡ 2026년 새 세입자 전세 중앙값(막대) · 이름 아래 매매 중앙값 · 9곳 전체는 본문 표
bars('img/'+S+'1_pair.png','전세는 래미안대치팰리스 18억 5,500만, 은마 7억 8,250만',
     [('래미안대치팰리스|매매 42억 5,000만',18.55,'18억 5,500만',True),('대치르엘|매매 35억 8,000만',17.5,'17억 5,000만',False),('대치푸르지오써밋|매매 33억 2,500만',14.45,'14억 4,500만',False),('한보미도맨션1|매매 39억',10.5,'10억 5,000만',False),('은마 84㎡|매매 37억 9,000만',7.825,'7억 8,250만',False)],
     note='대치동 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월 · 이름 아래는 같은 해 매매 중앙값 · 국토교통부 실거래')
# 그림 2: 단지별 84㎡ 임대 계약 가운데 월세 몫(12곳 가운데 5곳 · 나머지는 본문 표)
bars('img/'+S+'2_rent.png','새 단지는 셋 중 둘, 은마는 둘 중 하나가 월세',
     [('대치르엘|21건 중',66.7,'66.7%',True),('래미안대치팰리스|48건 중',58.3,'58.3%',False),('은마 84㎡|195건 중',48.7,'48.7%',False),('쌍용대치1차|26건 중',38.5,'38.5%',False),('한보미도맨션2|22건 중',31.8,'31.8%',False)],
     note='대치동 84㎡ 임대 계약(신규 · 갱신) 가운데 월세가 있는 계약의 몫 · 2026년 1~10월 · 국토교통부 전월세 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 2화 · 대치동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'대치동 아파트 시세',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'84㎡ 매매 중앙값',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'37억',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2026년 1~10월 75건 · 2025년은 34억 7천',font=kr(san,33),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')

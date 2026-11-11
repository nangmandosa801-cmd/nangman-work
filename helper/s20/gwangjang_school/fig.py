import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars
S='img/nangman_gwangjang_school_'
N='국토교통부 아파트 실거래 · 서울 광진구 · 전용 83~86㎡ · 2026년 1~10월 계약 · 중앙값 · 해제 거래와 직거래 뺌'
# 1. 극동 1·2차 vs 현대파크빌 : 매매와 새 전세
bars(S+'1_pair.png','낡은 극동이 매매 3억 4천 높고 전세 2억 9,500 낮습니다',
     [('극동 1·2차 매매|1985 · 1989년 · 14건',24.9,'24억 9,000만',True),('현대파크빌 매매|2000년 · 11건',21.5,'21억 5,000만',False),
      ('극동 1·2차 전세|새 세입자 16건',7.65,'7억 6,500만',False),('현대파크빌 전세|새 세입자 16건',10.6,'10억 6,000만',False)],note='광장동 84㎡ 중앙값 · 2026년 1~10월 계약 · 국토교통부 실거래 · 해제 거래와 직거래 뺌')
# 2. 전세가율 다섯 묶음
bars(S+'2_ratio.png','오래된 광장동 넷은 전세가 매매의 33%입니다',
     [('광장동|1985~1990년 4곳',33.3,'33%',True),('자양동|1995~1999년 5곳',37.6,'38%',False),('구의동|1992~1997년 4곳',40.5,'40%',False),
      ('광장동|1995~2001년 6곳',43.6,'44%',False),('구의동|2017~2021년 3곳',51.5,'51%',False)],note='새 세입자 전세 중앙값 ÷ 매매 중앙값 · 광진구 84㎡ · 2026년 1~10월 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 11화 · 서울 광장동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'광장동 아파트 시세',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'낡은 극동 84㎡가',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'3억 4천 비쌉니다',font=kr(ser_,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'매매 24억 9,000만 · 새 전세 7억 6,500만 · 전세가율 31%',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save(S+'thumb.png'); print('fig ok')

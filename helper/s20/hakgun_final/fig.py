import sys
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_hakgun_final_'
# 1. 내신 5등급제 1등급 기준 10% 와 전 과목 1등급 비율(확인된 공식 · 보도 숫자만)
bars('img/'+S+'1_naesin.png','1등급 기준은 10%, 전 과목 1등급은 1.08%',
     [('1등급 기준|5등급제 한 과목',10.0,'10%',False),
      ('부산 고1|2025년 1학기',2.07,'2.07%',False),
      ('서울 고1|2025년 1학기',1.72,'1.72%',False),
      ('전국 고1|2025년 1 · 2학기',1.08,'1.08%',True)],
     note='교육부(뉴시스 2026년 7월 6일) · 서울시교육청 자료(뉴시스 2025년 10월 19일) · 부산진로진학지원센터(부산일보 2025년 8월 5일)')
# 2. 한국은행 2024년 8월 분석 숫자 카드 3개
cards3('img/'+S+'2_bok.png','강남 3구 졸업생은 4%, 서울대 진학생은 12%',
       [('12%','서울대 진학생 중 강남 3구',True,'고교 졸업생 중에서는 4%'),
        ('92%','서울 · 비서울 진학률 차이 중',False,'사는 곳 효과로 추정한 몫'),
        ('26.9%','서울대 입학생 중 재수생',False,'2013년 14.9% → 2024년')],
       note='한국은행 BOK 이슈노트 「입시경쟁 과열로 인한 사회문제와 대응방안」 2024년 8월 27일')

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 17화 · 마지막 화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'학군지 아파트',font=kr(ser_,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'내신 5등급제 전 과목 1등급',font=kr(ser_,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1.08%',font=kr(ser_,120),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'1등급 기준은 10% · 2025년 고1 전국 · 교육부',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

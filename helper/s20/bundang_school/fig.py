import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_bundang_school_'
J=json.load(open('ana.json'))
h=J['grp']['hak']
def py(v): return f'{int(round(v/100))*100:,}만' if v<10000 else f'{int(v//10000)}억 {int(round((v%10000)/100))*100:,}만'
# 그림 1: 학군 단지 넓이별 전용 3.3㎡당 매매 중앙값 2026 (101㎡와 야탑 · 구미는 본문 표)
B=[('S','28~49㎡'),('59','59㎡'),('84','84㎡'),('131','131~135㎡'),('164','164㎡ 이상')]
bars('img/'+S+'1_bin.png','소형 3.3㎡당 1억 900만, 164㎡ 이상의 2.1배입니다',
     [(lab,h[b]['2026']['py']/10000,py(h[b]['2026']['py']),b=='S') for b,lab in B],
     note='분당 수내 · 서현 학군 단지 16곳 · 전용 3.3㎡당 매매 중앙값 · 2026년 1~10월 · 101㎡는 본문 표 · 국토교통부 실거래')
# 그림 2: 소형 ÷ 164㎡ 이상 3.3㎡당 배수 (해마다 값은 본문 표)
bars('img/'+S+'2_year.png','소형 평당가는 2021년에도 큰 평형의 1.7배였습니다',
     [('2021년|6,200만 ÷ 3,600만',1.7,'1.7배',False),('2023년',1.8,'1.8배',False),('2025년',1.8,'1.8배',False),('2026년|1억 900만 ÷ 5,100만',2.1,'2.1배',True)],
     note='수내 · 서현 학군 단지 28~49㎡ 3.3㎡당 매매 중앙값 ÷ 164㎡ 이상 3.3㎡당 · 2026년은 1~10월 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 6화 · 분당 수내 · 서현',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'분당 아파트 시세',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'소형 평당 1억 1,100만',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'큰 평형의 2배',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'양지마을 35㎡ 11억 8천 · 194~198㎡ 31억 8,750 · 2026년',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='img/nangman_beomeo_school_'
J=json.load(open('ana.json'))
def up(k): return (J[k]['2026']['med']/J[k]['2023']['med']-1)*100
L=[('힐스테이트범어|범어동','힐스테이트범어',True),('만촌삼정그린코아|만촌동','만촌삼정그린코아에듀파크',False),('동대구이안센트럴D|동구 신암동','동대구이안센트럴D',False),('월배2차아이파크|달서구 유천동','대구월배2차아이파크',False),('시지3차서한이다음|수성구 사월동','시지3차서한이다음',False)]
bars(S+'1_up.png','범어동 84㎡ 3년 새 33% 올랐습니다, 시지는 0.1%',
     [(n,up(k),f'+{up(k):.1f}%',h) for n,k,h in L],
     note='84㎡ 매매 중앙값 · 2023년 → 2026년 1~10월 · 국토교통부 실거래')
def jr(k): return J[k]['jn26']['med']/J[k]['2026']['med']*100
L=[('범어센트럴푸르지오|범어동','범어센트럴푸르지오',False),('힐스테이트범어|범어동','힐스테이트범어',True),('월배2차아이파크|달서구','대구월배2차아이파크',False),('수성하늘채르레브|범물동','수성하늘채르레브',False),('시지3차서한이다음|사월동','시지3차서한이다음',False)]
bars(S+'2_jeonse.png','범어동 전세가율 40~50%, 시지 · 범물은 68~76%',
     [(n,jr(k),f'{jr(k):.1f}%',h) for n,k,h in L],
     note='84㎡ 새 세입자 전세 중앙값 ÷ 매매 중앙값 · 2026년 1~10월 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 14화 · 대구 범어 · 만촌',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'범어동 아파트 시세',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'힐스테이트범어 84㎡',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'16억 9,750만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2021년보다 13.7% 위 · 2026년 1~10월 24건 · 새 전세 8억 4천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save(S+'thumb.png')
print('fig ok', [round(up(k),1) for _,k,_ in [(0,'힐스테이트범어',0)]])

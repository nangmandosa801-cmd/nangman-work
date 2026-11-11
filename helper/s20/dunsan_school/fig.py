import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_dunsan_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
def M(k,y='2026'): return J[k][y]['med']
# 1. 둔산 1990년대 단지와 도안 2021년 단지 · 101~104㎡ 매매 중앙값
bars('img/'+S+'1_pair.png','1992년 크로바가 도안 새 아파트보다 2억 300만 비쌉니다',
     [('크로바 101㎡|1992년 · 둔산동',M('크로바101')/10000,uk(M('크로바101')),True),('목련 101㎡|1993년 · 둔산동',M('목련101')/10000,uk(M('목련101')),False),
      ('아이파크시티 2단지 104㎡|2021년 · 도안',M('아이파크시티2_104')/10000,uk(M('아이파크시티2_104')),False),('한마루 101㎡|1992년 · 둔산동',M('한마루101')/10000,uk(M('한마루101')),False),
      ('아이파크시티 1단지 104㎡|2021년 · 도안',M('아이파크시티1_104')/10000,uk(M('아이파크시티1_104')),False)],
     note='2026년 1~10월 매매 중앙값 · 크로바 11건 · 목련 14건 · 아이파크시티 2단지 25건 · 한마루 43건 · 1단지 8건 · 국토교통부 실거래')
# 2. 2021년 대비
def ch(k): return (M(k)/M(k,'2021')-1)*100
cards3('img/'+S+'2_2021.png','2021년보다 크로바는 5.5% 위, 도안 2014년 단지는 16.9% 아래',
     [(f'{ch("크로바101"):+.1f}%'.replace('-','−'),'크로바 101㎡',True,f'{uk(M("크로바101","2021"))} → {uk(M("크로바101"))}'),
      (f'{ch("한마루101"):+.1f}%'.replace('-','−'),'한마루 101㎡',False,f'{uk(M("한마루101","2021"))} → {uk(M("한마루101"))}'),
      (f'{ch("트리풀5_84"):+.1f}%'.replace('-','−'),'도안 트리풀시티 5단지 84㎡',False,f'{uk(M("트리풀5_84","2021"))} → {uk(M("트리풀5_84"))}')],
     note='2021년과 2026년 1~10월 매매 중앙값 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 13화 · 대전 둔산동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'둔산동 크로바아파트',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'도안 새 아파트보다',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'2억 300만 위',font=kr(ser_,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'1992년 크로바 101㎡ 12억 9,800만 · 2026년 1~10월',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

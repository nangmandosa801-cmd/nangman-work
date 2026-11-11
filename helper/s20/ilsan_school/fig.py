import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars
S='img/nangman_ilsan_school_'
J=json.load(open('ana.json')); IX=J['_ix']
def d(k): return round(100-IX[k]['2026'],1)
N=[('후곡|학원가 옆','후곡'),('백마|학원가 옆','백마'),('강촌|마두동 · 백마 옆','강촌'),('백송|학원가에서 멂','백송'),('성저 · 장성|학원가에서 멂','성저장성')]
bars(S+'1_drop.png','학원가 옆 후곡도, 먼 백송도 2021년보다 18~19% 아래',
     [(n,d(k),f'−{d(k)}%',k=='후곡') for n,k in N],
     note='일산 1992~1997년 준공 84㎡ 매매 · 2021년 대비 2026년 1~10월 · 같은 단지끼리 맞춘 값 · 국토교통부 실거래')
def uk(v):
    a,b=divmod(int(v),10000); return f'{a}억' if b==0 else f'{a}억 {b//1000}천'
bars(S+'2_jeonse.png','전세는 학원가 옆이 5,000만~8,000만원 더 비쌉니다',
     [(n,J[k]['jn2026']['med']/10000,uk(J[k]['jn2026']['med']),k=='후곡') for n,k in N],
     note='일산 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월 · 국토교통부 전월세 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); dr=ImageDraw.Draw(im)
dr.rectangle([0,0,W,14],fill='#D4B04C'); dr.rectangle([0,W-14,W,W],fill='#D4B04C')
dr.text((70,95),'낭만 부동산 · 학군지 아파트 12화 · 일산 후곡 · 백마',font=kr(san,28),fill='#AFC0D8',anchor='lm')
dr.line([70,248,930,248],fill='#3A5A8A',width=3); dr.line([70,782,930,782],fill='#3A5A8A',width=3)
dr.text((W/2,360),'일산 학원가 아파트',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
dr.text((W/2,485),'후곡 84㎡ 2021년보다',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
dr.text((W/2,605),'18% 아래',font=kr(ser_,110),fill='#D4B04C',anchor='mm')
dr.text((W/2,715),'먼 단지 백송도 19% 아래 · 전세는 5,000만 차이',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save(S+'thumb.png'); print('fig ok',[d(k) for _,k in N])

import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars
S='nangman_songdo_school_'
J=json.load(open('ana.json'))
a=J['1공구']['m']; b=J['8공구']['m_same']; b26=J['8공구']['m']['2026'][0]
def uk(v):
    v=int(round(v)); x,y=divmod(v,10000)
    return f'{x}억' if y==0 else f'{x}억 {y:,}만'
# 1. 2021년과 2026년, 1공구와 8공구 84㎡ 매매 중앙값
bars('img/'+S+'1_gap.png','2021년 2천만 차이가 2026년 1억 7천으로',
  [('1공구|2021년',a['2021'][0]/1e4,'8.5억',False),('8공구|2021년',b['2021'][0]/1e4,'8.3억',False),
   ('1공구|2026년 1~10월',a['2026'][0]/1e4,'8.2억',True),('8공구|2026년 1~10월',b26/1e4,'6.5억',False)],
  note='송도 84㎡ 매매 중앙값 · 1공구 13개 단지 · 8공구 6개 단지 · 국토교통부 실거래')
# 2. 2026년 84㎡ 전세 계약 중 갱신 비율
def rr(k): x=J[k]['j84']; return x['ren26n']/x['all26']*100
L=[('1공구',rr('1공구'),True),('2공구',rr('2공구'),False),('송도 전체',rr('_songdo_all'),False),('8공구',rr('8공구'),False)]
bars('img/'+S+'2_renew.png','1공구 전세 열 건 중 여섯 건은 갱신',
  [(n,v,f'{v:.0f}%',h) for n,v,h in L],
  note='2026년 1~10월 84㎡ 전세 계약 가운데 갱신 계약 비율 · 국토교통부 전월세 실거래 · 송도동')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 9화 · 인천 송도',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'송도 1공구 아파트',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'새 8공구보다',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 7천 비쌉니다',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'84㎡ 매매 중앙값 · 2021년에는 2천만 차이 · 2026년 1~10월',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok',uk(a['2026'][0]),uk(b26),[round(x[1],1) for x in L])

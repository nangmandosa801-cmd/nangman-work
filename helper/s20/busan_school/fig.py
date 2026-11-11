import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars
S='nangman_busan_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
def M(k): return J[k]['2026']['med']
def JN(k): return J[k]['j2026']['new_med']
# 1. 2026년 84㎡ 매매 중앙값 5곳
L=[('사직롯데캐슬|사직동 2017년','사직롯데캐슬더클래식',False),('더샵센텀파크1차|재송동 2005년','더샵센텀파크1차',False),('대우마리나 1·2차|우동 1991~92년','대우마리나1·2',False),('해운대자이 2차|우동 2018년','해운대자이2차1단지',False),('좌동 신시가지|1996~99년 30곳','좌동신시가지',True)]
bars('img/'+S+'1_mae.png','좌동 84㎡ 5억 5천, 대우마리나의 절반입니다',
     [(n,M(k)/10000,uk(M(k)),h) for n,k,h in L],
     note='부산 84㎡ 매매 중앙값 · 2026년 1~10월 · 국토교통부 실거래(전용 83~86㎡ · 해제 · 직거래 뺌)')
# 2. 전세가율 5곳
L=[('사직쌍용예가|사직동 2006년','사직쌍용예가',False),('좌동 신시가지|1996~99년','좌동신시가지',False),('사직롯데캐슬|사직동 2017년','사직롯데캐슬더클래식',False),('더샵센텀파크1차|재송동 2005년','더샵센텀파크1차',False),('대우마리나 1·2차|우동 1991~92년','대우마리나1·2',True)]
it=[]
for n,k,h in L:
    p=JN(k)/M(k)*100; it.append((n,p,f'{p:.0f}%',h))
bars('img/'+S+'2_rate.png','전세가율, 학원가는 56~73% 대우마리나는 33%',it,
     note='84㎡ 새 세입자 전세 중앙값 ÷ 매매 중앙값 · 2026년 1~10월 · 국토교통부 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 15화 · 부산 사직 · 좌동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'부산 학군지 아파트',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'바다 쪽 매매는 2배',font=kr(ser_,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'전세는 5,500만 차이',font=kr(ser_,88),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'좌동 84㎡ 5억 5,250만 · 대우마리나 11억 2,250만 · 2026년 1~10월',font=kr(san,30),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

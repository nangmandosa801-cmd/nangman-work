import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'

# 1. 12억 안팎(11억 5천~12억 5천) 84㎡ 거래 건수 · 단지별
R=[('미사레스티아 (2017)',31,NAVY),('미사강변 센텀팰리스 (2016)',24,NAVY),('이편한세상미사 (2018)',18,NAVY),('미사강변 하우스디 더 레이크 (2016)',16,NAVY),('미사강변동원로얄듀크 (2016)',11,NAVY),
   ('미사 나머지 16개 단지',74,GRAY),('감일센트레빌 (2020)',3,BLUE),('감일스윗시티10단지 (2020)',2,BLUE),('감일한라비발디 (2019)',1,BLUE),('감일금강펜테리움센트럴파크 (2021)',1,BLUE)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'미사 감일 비교 · 올해 12억 안팎(11억 5천~12억 5천)에 팔린 84㎡',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.915,'미사 21개 단지 174건, 감일 4개 단지 7건',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.1,0.6,0.72])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+0.8,y,f'{v}건',va='center',fontsize=15,color=NAVY if c!=BLUE else BLUE,fontweight='bold')
ax.set_xlim(0,84); ax.set_xticks([]); ax.set_ylim(-0.6,len(R)+0.4)
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.text(83,ys[0]+0.95,'■ 미사(망월 · 풍산 · 선동)',ha='right',fontsize=13,color=NAVY)
ax.text(83,ys[0]+0.45,'■ 감일(감일 · 감이동)',ha='right',fontsize=13,color=BLUE)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 83~86㎡ · 거래금액 11억 5천만~12억 5천만원 · 해제 · 직거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa_vs_gamil_1_band.png'); plt.close()

# 2. 여섯 항목 나란히 · 미사강변 센텀팰리스 vs 감일센트레빌
rows=[('84㎡ 올해 중앙값','12억 (38건)','13억 (11건)','12억은 가운데 값','12억은 아래쪽 3건'),
      ('새 세입자 전세 · 전세가율','7억 2,500만 · 60%','6억 5,000만 · 50%','16건','5건'),
      ('역까지 거리','미사역 885m','감일역 예정지 980m','5호선 · 2020년 개통','3호선 · 2032년 목표'),
      ('지은 해','2016년 7월','2020년 3월','10년차','6년차'),
      ('세대수','1,455세대','589세대','17개 동','6개 동'),
      ('1년 상승률','+22.4%','+24.4%','9억 8,000만 → 12억','10억 4,500만 → 13억')]
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'미사 감일 비교 · 같은 12억으로 보는 두 단지',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.92,'미사강변 센텀팰리스 vs 감일센트레빌, 여섯 항목',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.03,0.08,0.94,0.76]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
ax.text(31,96,'미사강변 센텀팰리스',ha='center',fontsize=18,color=NAVY,fontweight='bold')
ax.text(81,96,'감일센트레빌',ha='center',fontsize=18,color=BLUE,fontweight='bold')
ax.plot([0,100],[91,91],color='#C8D2DE',lw=2)
for i,(k,a,b,sa,sb) in enumerate(rows):
    y=84-i*15
    ax.text(0,y,k,fontsize=15,color='#555',va='center')
    ax.text(31,y+2.5,a,ha='center',fontsize=19,color=NAVY,fontweight='bold',va='center')
    ax.text(31,y-4.5,sa,ha='center',fontsize=13,color='#7A8590',va='center')
    ax.text(81,y+2.5,b,ha='center',fontsize=19,color=BLUE,fontweight='bold',va='center')
    ax.text(81,y-4.5,sb,ha='center',fontsize=13,color='#7A8590',va='center')
    ax.plot([0,100],[y-8.5,y-8.5],color='#E6EBF1',lw=1)
fig.text(0.045,0.03,'국토교통부 매매 · 전월세 실거래(2026년 1~10월 · 전용 83~86㎡ · 전세는 월세 없는 새 계약) · 거리는 지도 좌표 직선 · 세대수는 단지 정보 사이트 기준',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa_vs_gamil_2_six.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'미사 감일 비교',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'같은 12억이면',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'174건 vs 7건',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'12억 안팎에 팔린 84㎡ · 미사 · 감일',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa_vs_gamil_thumb.png')

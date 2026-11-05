import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 공구별 새 세입자 전세와 매매
R=[('1공구\n센트럴파크 · 커낼워크',52000,83000),('7공구\n연세대 캠퍼스',48000,77800),('3공구\n인천대입구역',47000,95250),('2·4공구\n초기 단지',39500,58700),('6·8공구\n랜드마크시티',39000,65000)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송도 전세 시세 · 공구별 84㎡ 새 세입자 전세와 매매 (2026년 1~10월 중앙값)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'3공구는 매매가 가장 높은데 전세는 매매의 49%',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=list(range(len(R)))[::-1]
for y,(lab,j,m) in zip(ys,R):
    ax.barh(y+0.19,m,height=0.36,color=GRAY); ax.barh(y-0.19,j,height=0.36,color=NAVY)
    ax.text(m+700,y+0.19,'매매 '+won(m),va='center',fontsize=14,color='#555')
    ax.text(j+700,y-0.19,'전세 '+won(j)+f'  ({j/m*100:.0f}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
ax.set_xlim(0,125000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 · 매매 실거래(인천 연수구 송도동 · 전용 83~86㎡ · 월세 없는 신규 계약 · 매매는 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_songdo_jeonse_1_gongu.png'); plt.close()
# 2 같은 해 지은 단지 짝
P=[('송도더샵파크애비뉴 (3공구 · 2018)',50500,131500),('e편한세상송도 (8공구 · 2018)',37000,64300),
   ('송도더샵퍼스트파크F15BL (3공구 · 2017)',50000,120000),('송도글로벌파크베르디움 (7공구 · 2017)',53000,94150),
   ('더샵송도프라임뷰20BL (3공구 · 2022)',50000,98800),('호반써밋송도 (8공구 · 2023)',40000,64000)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.957,'송도 전세 시세 · 비슷한 해에 지은 단지 짝 84㎡ (2026년 1~10월 중앙값)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.912,'2018년 짝: 매매는 6억 7천, 전세는 1억 3천 차이',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.10,0.6,0.71])
ys=[]; y=0
for i in range(len(P)):
    ys.append(y); y-=1 if i%2==0 else 1.6
for y,(lab,j,m) in zip(ys,P):
    ax.barh(y+0.17,m,height=0.32,color=GRAY); ax.barh(y-0.17,j,height=0.32,color=NAVY)
    ax.text(m+800,y+0.17,'매매 '+won(m),va='center',fontsize=13.5,color='#555')
    ax.text(j+800,y-0.17,'전세 '+won(j),va='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in P],fontsize=14,color='#333')
ax.set_xlim(0,165000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 · 매매 실거래(전용 83~86㎡ · 전세는 월세 없는 신규 계약 · 매매는 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_songdo_jeonse_2_pair.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 인천 송도 · 전세',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'송도 전세 시세',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 새 세입자',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'4억 1천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'매매 7억 3천의 56%',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_songdo_jeonse_thumb.png')

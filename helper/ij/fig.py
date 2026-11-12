import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'

# 1. 세 구역 근처 새 전세 중앙값과 이주비 한도 6억
R=[('노량진3구역 근처\n84㎡',79000,NAVY),('노량진3구역 근처\n59㎡',58000,GRAY),
   ('북아현2구역 근처\n84㎡',97000,NAVY),('북아현2구역 근처\n59㎡',77000,GRAY),
   ('방화3구역 근처\n84㎡',50000,NAVY),('방화3구역 근처\n59㎡',40000,GRAY)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'재개발 이주비대출 한도 6억 · 구역 근처 아파트 올해 새 전세 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'6억으로 84㎡를 구하는 곳은 방화3구역 근처뿐',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.22,0.11,0.71,0.68])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    ax.text(v+900,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold',zorder=5,bbox=dict(fc='white',ec='none',pad=2))
ax.axvline(60000,color=BLUE,lw=2.4,ls='--',zorder=1)
ax.text(60000,len(R)-0.35,'이주비대출 한도 6억',color=BLUE,fontsize=15,fontweight='bold',ha='center',va='bottom',bbox=dict(fc='white',ec='none',pad=2))
ax.set_xlim(0,112000); ax.set_ylim(-0.6,len(R)-0.1); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 전세 · 새로 맺은 계약 중앙값) · 근처 동은 본문 표 참고',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_ijubi_1_jeonse.png'); plt.close()

# 2. 84㎡ 새 전세 가운데 6억 이하 비율
R2=[('노량진3구역 근처',39,345),('북아현2구역 근처',15,176),('방화3구역 근처',57,63)]
fig=plt.figure(figsize=(11.55,6.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.95,'재개발 이주비 6억 · 근처 84㎡ 올해 새 전세 가운데 6억 이하 계약',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.89,'노량진 · 북아현은 10건 중 1건 정도',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.22,0.13,0.71,0.6])
ys=list(range(len(R2)))[::-1]
p=[a/b*100 for _,a,b in R2]
ax.barh(ys,[100]*3,color='#EEF1F5',height=0.56)
ax.barh(ys,p,color=[NAVY,NAVY,BLUE],height=0.56)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R2],fontsize=16,color='#333')
for y,(_,a,b),v in zip(ys,R2,p):
    ax.text(v+1.5,y,f'{v:.0f}%  ({a}건 / {b}건)',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,128); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.035,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 전용 80~90㎡ · 전세 · 새로 맺은 계약)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_ijubi_2_share.png'); plt.close()

# 썸네일 C형
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 재개발 · 이주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'재개발 이주비대출',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'한도',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'6억',font=kr(ser,120),fill='#D4B04C',anchor='mm')
d.text((W/2,720),'노량진 84㎡ 새 전세는 7억 9천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_ijubi_thumb.png')

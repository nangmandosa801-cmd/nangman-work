import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1) 단지별 84㎡ 올해 중앙값 (2026년 1~10월)
R=[('자연앤힐스테이트',187000,43),('광교센트럴뷰',159500,27),('광교푸르지오월드마크',150000,7),('광교에듀포레',149000,7),
   ('광교2차e편한세상',109000,30),('광교호반베르디움',96000,17),('광교한양수자인',93500,11),('광교 해모로',75000,16),('광교대광로제비앙',72750,12)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'수원 영통구 이의동 84㎡ 올해 매매 중앙값 · 단지별',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.915,'같은 이의동 84㎡, 단지 사이 11억 4천만원 차이',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.1,0.68,0.72])
ys=list(range(len(R)))[::-1]
cols=[NAVY if n==43 else GRAY for _,_,n in R]
ax.barh(ys,[v for _,v,_ in R],color=cols,height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,n) in zip(ys,R):
    ax.text(v+1500,y,f'{won(v)}  ({n}건)',va='center',fontsize=15,color=NAVY,fontweight='bold',bbox=dict(fc='white',ec='none',pad=1.5),zorder=5)
ax.axvline(94930,color=BLUE,ls='--',lw=2,zorder=1)
ax.text(94930,len(R)-0.35,' 광교 자연앤 센트레빌 84A 분양가 9억 4,930만',fontsize=13.5,color=BLUE,va='bottom')
ax.set_xlim(0,238000); ax.set_ylim(-0.6,len(R)-0.1); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 80~90㎡ · 해제 거래 뺌) · 분양가는 입주자모집공고(2026년 10월 30일)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_uidong_1_complex.png'); plt.close()

# 2) 분기별 흐름 (2025년 1분기~2026년 3분기)
Q=['25년\n1분기','2분기','3분기','4분기','26년\n1분기','2분기','3분기']
L=[('자연앤힐스테이트',[151000,158000,165000,174250,172500,186250,205000],NAVY,'o'),
   ('광교2차e편한세상',[92500,95000,98750,103000,105000,108500,110000],BLUE,'s'),
   ('광교 해모로',[69500,68500,70800,73000,74500,74650,79500],GRAY,'D')]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'이의동 84㎡ 매매 중앙값 · 분기별 (거래 많은 세 단지)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'자연앤힐스테이트 15억 1천 → 20억 5천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.72,0.66])
x=list(range(len(Q)))
for name,v,c,m in L:
    ax.plot(x,v,color=c,lw=3,marker=m,ms=8)
    ax.text(len(Q)-1+0.15,v[-1],f'{name}\n{won(v[-1])}',va='center',fontsize=14,color=c,fontweight='bold')
    ax.text(0,v[0]+5000,won(v[0]),ha='center',fontsize=13,color=c)
ax.set_xticks(x); ax.set_xticklabels(Q,fontsize=14,color='#333')
ax.set_ylim(50000,225000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 1월~2026년 9월 계약 · 전용 80~90㎡ · 해제 거래 뺌 · 분기별 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_uidong_2_quarter.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 수원 영통구 이의동 · 광교',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'이의동 아파트 매매',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'84㎡ 단지 사이',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'11억 차이',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'올해 중앙값 7억 2천 ~ 18억 7천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_uidong_thumb.png')

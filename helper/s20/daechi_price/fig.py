import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_daechi_price_'
def won(v):
    v=int(v); return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 그림 1: 단지별 84㎡ 2026년 매매 중앙값과 새 세입자 전세 중앙값
R=[('래미안대치팰리스 (2015)',425000,185500),('한보미도맨션1 (1983)',390000,105000),('개포우성1차 (1983)',389000,115500),('은마 (1979)',379000,78250),
   ('대치르엘 (2021)',358000,175000),('쌍용대치1차 (1983)',341500,76500),('대치우성1차 (1984)',339000,84000),('대치푸르지오써밋 (2023)',332500,144500),('대치현대 (1999)',302000,105500)]
fig=plt.figure(figsize=(11.55,9.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'대치동 단지별 84㎡ · 2026년 1~10월 매매 중앙값(남색)과 새 세입자 전세 중앙값(회색)',fontsize=15.5,color=BLUE,va='top')
fig.text(0.045,0.925,'매매는 30억~42억, 전세는 7억~18억',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.3,0.07,0.65,0.8])
n=len(R); ys=np.arange(n)[::-1]*1.0
ax.barh(ys+0.2,[m for _,m,_ in R],color=NAVY,height=0.38)
ax.barh(ys-0.2,[j for _,_,j in R],color=GRAY,height=0.38)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14,color='#333')
for y,(_,m,j) in zip(ys,R):
    ax.text(m+4000,y+0.2,won(m),va='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(j+4000,y-0.2,won(j),va='center',fontsize=13,color='#555')
ax.set_xlim(0,520000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.02,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1월~10월 24일 계약 · 전용 83~86㎡ · 해제 거래 뺌 · 매매 2건 · 새 세입자 전세 3건 이상 단지 · 괄호는 지은 해)',fontsize=11.5,color='#8A8578')
fig.savefig('img/'+S+'1_pair.png'); plt.close()

# 그림 2: 단지별 84㎡ 임대 계약 가운데 월세 몫
R2=[('대치르엘',66.7,21),('대치푸르지오써밋',66.7,24),('대치아이파크',62.1,29),('대치현대',59.3,27),('래미안대치팰리스',58.3,48),('은마 84㎡',48.7,195),('한보미도맨션1',45.9,37),('은마 76㎡',44.5,301),('대치삼성',42.1,38),('쌍용대치1차',38.5,26),('대치우성1차',36.4,22),('한보미도맨션2',31.8,22)]
fig=plt.figure(figsize=(11.55,9.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'대치동 단지별 84㎡ 임대 계약 가운데 월세가 있는 계약의 몫 · 2026년 1~10월',fontsize=15.5,color=BLUE,va='top')
fig.text(0.045,0.925,'새 단지는 셋 중 둘, 은마는 둘 중 하나가 월세',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.07,0.68,0.8])
ys=list(range(len(R2)))[::-1]
c=[NAVY if v>=55 else (BLUE if v>=45 else GRAY) for _,v,_ in R2]
ax.barh(ys,[v for _,v,_ in R2],color=c,height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R2],fontsize=14,color='#333')
for y,(_,v,k) in zip(ys,R2): ax.text(v+0.8,y,f'{v}%  ({k}건 중)',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_xlim(0,88); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.02,'국토교통부 아파트 전월세 실거래(2026년 1월~10월 24일 계약 · 전용 83~86㎡ · 은마 76㎡는 따로 · 신규 · 갱신 모두 포함 · 월세금이 0보다 큰 계약을 월세로 셈)',fontsize=11.5,color='#8A8578')
fig.savefig('img/'+S+'2_rent.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 2화 · 대치동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'대치동 아파트 시세',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'84㎡ 매매 중앙값',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'37억',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2026년 1~10월 75건 · 2025년은 34억 7천',font=kr(san,33),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')

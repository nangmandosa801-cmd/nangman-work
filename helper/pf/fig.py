import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_pyeongtaekcenterfine_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 힐스테이트평택화양 84㎡ 전세 달별 중앙값
M=[('4월',18000,5),('5월',17000,7),('6월',18000,10),('7월',17250,10),('8월',20000,9),('9월',21000,7)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평택 화양지구 힐스테이트평택화양 · 84㎡ 전세 달별 중앙값(2026년)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'첫 넉 달 1억 7천~1억 8천, 8월부터 2억 위로',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
xs=range(len(M)); cols=[GRAY]*4+[NAVY]*2
ax.bar(xs,[v for _,v,_ in M],color=cols,width=0.6)
for x,(m,v,n) in zip(xs,M):
    ax.text(x,v+300,won(v),ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(x,800,f'{n}건',ha='center',fontsize=13,color='white')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_,_ in M],fontsize=16,color='#333')
ax.set_ylim(0,24000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 4~9월 계약 · 전용 80~86㎡ · 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_hillstate.png'); plt.close()
# 2 84㎡ 전세 · 매매
R=[('평택 2019년 이후 아파트\n84㎡ 매매',53000,GRAY),('화양지구 새 아파트\n84㎡ 매매',39500,BLUE),('평택 2019년 이후 아파트\n84㎡ 전세',29000,GRAY),('화양지구 새 아파트\n84㎡ 전세',18250,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평택 푸르지오 센터파인 옆 화양지구 새 아파트 6곳 · 평택 전체와 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'화양지구 84㎡ 전세 1억 8천, 매매 3억 9천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.66,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+600,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,64000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1~10월 · 전용 80~86㎡ · 해제 거래 뺌 · 전세는 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}2_compare.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 화양지구 · 11월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'평택 푸르지오 센터파인',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'옆 단지 84㎡ 전세',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 8천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'화양지구 새 아파트 6곳 · 올해 144건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1. 방배동 84㎡ 새 세입자 전세 (실거래)
R=[('방배그랑자이 84㎡\n(2021년 · 8건)',141500,NAVY),('방배동 2018년 이후 아파트 84㎡\n(18건)',129500,BLUE),('방배 서리풀 그랑블 84㎡\n(2019년 · 8건)',109500,GRAY),('방배동 아파트 전체 84㎡\n(131건)',92000,GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'디에이치 방배 전세 · 옆 방배동 단지 84㎡ 새 세입자 전세 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'방배그랑자이 84㎡ 14억 1,500만원',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.33,0.12,0.6,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    ax.text(v+1500,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,185000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1월~11월 5일 계약 · 서초구 방배동 · 월세 없는 신규 계약 · 전용 80~86㎡)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_banbae_jeonse_1_near.png'); plt.close()

# 2. 방배동 84㎡ 새 세입자 전세 기간별 (입주 전후)
P=[('1~6월\n(73건)',94000,GRAY),('7~8월\n(29건)',90000,GRAY),('9월~11월 5일\n(29건)',100000,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'디에이치 방배 입주 시작(9월 1일) 앞뒤 · 방배동 아파트 84㎡ 새 세입자 전세 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'입주 뒤 석 달, 옆 단지 전세는 10억',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.1,0.14,0.84,0.62])
xs=range(len(P))
ax.bar(xs,[v for _,v,_ in P],color=[c for *_,c in P],width=0.55)
ax.set_xticks(list(xs)); ax.set_xticklabels([a for a,_,_ in P],fontsize=16,color='#333')
for x,(_,v,c) in zip(xs,P):
    ax.text(x,v+1500,won(v),ha='center',fontsize=18,color=NAVY,fontweight='bold')
ax.set_ylim(0,120000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 계약 · 서초구 방배동 모든 연식 · 월세 없는 신규 계약 · 전용 80~86㎡)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_banbae_jeonse_2_period.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 서초 방배동 · 입주장 전세',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'디에이치 방배 전세',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'옆 방배그랑자이 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'14억 1,500만',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'3,064세대 · 9월 1일 입주 시작',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_banbae_jeonse_thumb.png')

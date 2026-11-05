import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
SRC='국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 하남 망월동 미사강변도시13단지 신규 계약 · 같은 조합이 여러 건인 계약)'
# 1. 13단지 신규 계약: 같은 면적, 두 가지 조합
G=[('30㎡','보증금 1,879만',20,'보증금 3,779만',10),
   ('37㎡','보증금 2,317만',25,'보증금 4,817만',13),
   ('47㎡','보증금 4,988만',32,'보증금 8,188만',16)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'미사강변도시 13단지 임대 · 2026년 신규 계약의 보증금과 월세',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.918,'보증금을 더 내면 월세가 절반쯤 줄어듭니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.12,0.62,0.70])
labels=[];vals=[];cols=[];ys=[];y=0
for sz,a,ma,b,mb in G:
    for lab,v,c in [(a,ma,BLUE),(b,mb,NAVY)]:
        labels.append(f'{sz} · {lab}'); vals.append(v); cols.append(c); ys.append(y); y-=1
    y-=0.7
ax.barh(ys,vals,color=cols,height=0.78)
ax.set_yticks(ys); ax.set_yticklabels(labels,fontsize=15,color='#333')
for yy,v in zip(ys,vals): ax.text(v+0.5,yy,f'월 {v}만원',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,42); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.045,'파랑 = 보증금을 적게 낸 계약 · 남색 = 보증금을 더 낸 계약 · 면적은 전용면적',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.018,SRC,fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa13_1_combo.png'); plt.close()

# 2. 같은 2015년 단지와 한 달 월세 비교
R=[('미사강변도시 13단지 47㎡\n임대 · 보증금 4,988만원',32,NAVY),
   ('미사강변트래지안 52㎡\n보증금 2억원',110,BLUE),
   ('미사강변 파크뷰 75㎡\n보증금 4억원',87.5,GRAY)]
fig=plt.figure(figsize=(11.55,7.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'미사강변도시 13단지 · 2015년에 지은 옆 단지 월세 계약 중앙값(2026년 1~10월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.903,'13단지 47㎡ 월세는 옆 트래지안 52㎡의 3분의 1이 안 됩니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.14,0.56,0.62])
ys=[0,-1,-2]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.62)
ax.set_yticks(ys); ax.set_yticklabels([n for n,_,_ in R],fontsize=15,color='#333')
for yy,(_,v,_) in zip(ys,R): ax.text(v+1.5,yy,f'월 {v:g}만원',va='center',fontsize=17,color=NAVY,fontweight='bold')
ax.set_xlim(0,135); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.05,'13단지는 신규 계약 중 가장 많은 조합 · 트래지안 · 파크뷰는 그 면적 월세 계약의 보증금 · 월세 중앙값',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.022,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 하남 망월동)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa13_2_rent.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 미사 · 임대 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'미사강변도시 13단지',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'37㎡ 보증금 2,317만원에',font=kr(ser,56),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'월 25만원',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,722),'LH 임대 2,742세대 · 2026년 신규 계약',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa13_thumb.png')

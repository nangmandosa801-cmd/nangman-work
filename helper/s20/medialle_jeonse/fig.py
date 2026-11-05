import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
P='nangman_medialle_jeonse_'
def w(v):
    e,r=divmod(v,10000)
    return f'{e}억'+((f' {r//1000}천' if r%1000==0 else f' {r:,}') if r else '')

# 그림 1: 59㎡ 새 세입자 전세 중앙값 (2026년 1~10월) + 메디알레 보도 5억 중반대
G=['녹번역\ne편한세상캐슬\n(2021)','힐스테이트\n녹번역\n(2022)','힐스테이트\n녹번\n(2019)','DMC\n아트포레자이\n(2026)','DMC\n파인시티자이\n(2025)','DMC SK뷰\n아이파크포레\n(2025)']
V=[65000,65000,63500,64000,65000,63000]; N=[76,11,16,10,7,15]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'힐스테이트 메디알레 전세 · 은평구 새 아파트 59㎡ 새 세입자 전세 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'옆 새 아파트 6억 3천~6억 5천 · 메디알레 5억 중반',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.15,0.88,0.62])
x=np.arange(len(G))
ax.bar(x,V,0.58,color=[NAVY,NAVY,NAVY,BLUE,BLUE,BLUE],zorder=2)
for i,(v,n) in enumerate(zip(V,N)):
    ax.text(i,v+900,w(v),ha='center',fontsize=15.5,color=NAVY,fontweight='bold')
    ax.text(i,2500,f'{n}건',ha='center',fontsize=13,color='white',zorder=3)
ax.axhline(55000,color='#D4B04C',lw=3,ls='--',zorder=3)
ax.text(2.5,55000,'힐스테이트 메디알레 59㎡ 계약 사례 5억 중반대 (보도)',fontsize=15,color=NAVY,ha='center',va='center',fontweight='bold',zorder=4,bbox=dict(facecolor='white',edgecolor='#D4B04C',boxstyle='round,pad=0.4'))
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=13.5,color='#333')
ax.set_ylim(0,72000); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 전세 · 신규 계약 · 전용 58.4~60.6㎡) · 괄호는 지은 해 · 메디알레는 아주경제(2026년 10월 30일)',fontsize=12,color='#8A8578')
fig.savefig(f'img/{P}1_59.png'); plt.close()

# 그림 2: 84㎡ 새 세입자 전세 중앙값 + 메디알레 호가 7억~9억 띠
G=['녹번역\ne편한세상캐슬','힐스테이트\n녹번역','DMC\n파인시티자이','DMC\n아트포레자이','힐스테이트\n녹번','DMC SK뷰\n아이파크포레','센트레빌\n아스테리움\n시그니처']
V=[80000,79000,77000,76000,75500,70000,59500]; N=[27,9,12,3,8,13,6]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'힐스테이트 메디알레 전세 · 은평구 새 아파트 84㎡ 새 세입자 전세 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'메디알레 84㎡ 호가 7억~9억 · 옆 단지 계약 7억~8억',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.15,0.88,0.62])
x=np.arange(len(G))
ax.axhspan(70000,90000,color='#D4E6F7',zorder=0)
ax.text(-0.45,88600,'힐스테이트 메디알레 84㎡ 전세 호가 7억~9억 (보도)',fontsize=14.5,color=BLUE,fontweight='bold',va='top')
ax.bar(x,V,0.58,color=[NAVY]*6+[GRAY],zorder=2)
for i,(v,n) in enumerate(zip(V,N)):
    ax.text(i,v+900,w(v),ha='center',fontsize=15,color=NAVY,fontweight='bold',zorder=3)
    ax.text(i,v-4600,f'{n}건',ha='center',fontsize=13,color='white',zorder=3)
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=13.5,color='#333')
ax.set_ylim(45000,92000); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 전세 · 신규 계약 · 전용 83.4~85.6㎡) · 메디알레 호가는 아주경제(2026년 10월 30일)',fontsize=12,color='#8A8578')
fig.savefig(f'img/{P}2_84.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 은평 대조동 · 입주장 전세',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'힐스테이트 메디알레',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'59㎡ 전세',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'5억 중반',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'옆 새 아파트 59㎡ 새 세입자 6억 5천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save(f'img/{P}thumb.png')

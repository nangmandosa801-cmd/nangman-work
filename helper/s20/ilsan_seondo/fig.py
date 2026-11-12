import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 그림 1: 84㎡ 매매 중앙값 2025년 vs 2026년 1~10월 (국토교통부 실거래, 해제 뺌)
G=['백송 · 후곡\n선도지구 84㎡','선도지구 밖\n일산 구축 84㎡','일산 전체\n84㎡']
Y25=[57000,54000,44800]; Y26=[56850,54600,46000]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'일산 재건축 선도지구 84㎡ 매매 중앙값 · 2025년과 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'선도지구 84㎡ 5억 7,000 → 5억 6,850',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(G)); w=0.34
ax.bar(x-w/2,Y25,w,color=GRAY,label='2025년'); ax.bar(x+w/2,Y26,w,color=[NAVY,BLUE,BLUE],label='2026년 1~10월')
def s(v): return f'{v//10000}억 {v%10000:,}' if v%10000 else f'{v//10000}억'
for i,(a,b) in enumerate(zip(Y25,Y26)):
    ax.text(i-w/2,a+1000,s(a),ha='center',fontsize=14,color='#555')
    ax.text(i+w/2,b+1000,s(b),ha='center',fontsize=15.5,color=NAVY,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=15,color='#333')
ax.set_ylim(0,66000); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 80~86㎡ · 해제 거래 뺌 · 2026년은 10월 신고분까지) · 단위 만원',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_ilsan_seondo_1_price.png'); plt.close()

# 그림 2: 백송 · 후곡 선도지구 월별 매매 건수 (모든 크기)
M=['25.1','2','3','4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8','9','10']
BS=[1,5,4,5,7,4,6,4,4,9,11,7,6,6,13,6,11,19,9,5,6,2]
HG=[7,4,10,3,7,10,6,2,2,5,10,7,6,5,6,8,9,12,5,7,6,6]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'일산 재건축 선도지구 월별 매매 건수 · 백송마을과 후곡마을',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'2026년 6월 31건 · 2025년 이후 가장 많은 달',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.05,0.13,0.92,0.64])
x=np.arange(len(M))
ax.bar(x,BS,0.62,color=NAVY,label='백송마을 1 · 2 · 3 · 5단지')
ax.bar(x,HG,0.62,bottom=BS,color=GRAY,label='후곡마을 3 · 4 · 10 · 15단지')
for i,(a,b) in enumerate(zip(BS,HG)): ax.text(i,a+b+0.5,str(a+b),ha='center',fontsize=12.5,color=NAVY,fontweight='bold')
ax.axvline(15.5,color=BLUE,lw=2,ls='--'); ax.text(15.35,34.5,'2026년 5월 12~26일\n백송마을 주민공람',fontsize=13,color=BLUE,va='top',ha='right')
ax.set_xticks(x); ax.set_xticklabels(M,fontsize=12.5,color='#333'); ax.set_ylim(0,36); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=13.5,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(모든 크기 · 해제 거래 뺌) · 10월은 신고 기한이 남아 더 늘 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_ilsan_seondo_2_count.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 일산 · 1기 신도시 재건축',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'일산 선도지구',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'84㎡ 중앙값',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'5억 7천 그대로',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'백송 · 후곡마을 · 2025년과 2026년 10월까지',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_ilsan_seondo_thumb.png')

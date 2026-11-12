import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 그림 1: 84㎡ 매매 중앙값 2025년 vs 2026년 1~10월 (국토교통부 실거래, 해제 뺌)
G=['양지마을','시범 현대우성','샛별마을','선도지구 밖\n분당 구축']
Y25=[185000,168000,149500,139000]; Y26=[226500,199000,174500,180000]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'분당 재건축 선도지구 84㎡ 매매 중앙값 · 2025년과 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'양지마을 18억 5천 → 22억 6,500만',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(G)); w=0.36
ax.bar(x-w/2,Y25,w,color=GRAY,label='2025년'); ax.bar(x+w/2,Y26,w,color=[NAVY,NAVY,NAVY,BLUE],label='2026년 1~10월')
def s(v): return f'{v//10000}억 {v%10000:,}' if v%10000 else f'{v//10000}억'
for i,(a,b) in enumerate(zip(Y25,Y26)):
    ax.text(i-w/2,a+2500,s(a),ha='center',fontsize=13.5,color='#555')
    ax.text(i+w/2,b+2500,s(b),ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=15,color='#333')
ax.set_ylim(0,260000); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 80~86㎡ · 해제 거래 뺌 · 2026년은 10월 신고분까지) · 단위 만원',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_bundangrecon_1_price.png'); plt.close()

# 그림 2: 2026년 월별 84㎡ 거래 건수 (선도지구 3곳 합계)
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
SB=[11,8,4,17,10,7,1,0,2,1]   # 시범 현대우성 + 샛별마을
YJ=[2,2,1,5,2,2,5,1,1,0]      # 양지마을
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'분당 재건축 선도지구 84㎡ 월별 매매 건수 · 2026년',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'시범 · 샛별 4~6월 34건 → 7~10월 4건',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(M))
ax.bar(x,SB,0.6,color=NAVY,label='시범 현대우성 · 샛별마을')
ax.bar(x,YJ,0.6,bottom=SB,color=GRAY,label='양지마을')
for i,(a,b) in enumerate(zip(SB,YJ)): ax.text(i,a+b+0.4,str(a+b),ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.axvline(5.5,color=BLUE,lw=2,ls='--'); ax.text(5.6,20.5,'6월 26 · 29일\n시범 · 샛별 사업시행자 지정',fontsize=13.5,color=BLUE,va='top')
ax.set_xticks(x); ax.set_xticklabels(M,fontsize=15,color='#333'); ax.set_ylim(0,24); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 80~86㎡ · 해제 거래 뺌) · 10월은 신고 기한이 남아 더 늘 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_bundangrecon_2_count.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 분당 · 1기 신도시 재건축',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'분당 선도지구',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'시행자 지정 뒤 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'거래 7건',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'시범 · 샛별 · 양지마을 · 2026년 10월까지',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_bundangrecon_thumb.png')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1) 84㎡ 매매 · 새 세입자 전세 중앙값
A=[('위례 하남(학암동)',165000,76000),('감일(감이·감일동)',141000,72000),('미사(망월·선·풍산동)',120000,70000)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'교산신도시 청약일정을 기다리는 동안 · 하남 새 아파트 84㎡ 올해 실거래',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'옆 신축 84㎡ 매매 12억~16억 5천, 새 전세 7억~7억 6천',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
import numpy as np
ys=np.arange(len(A))[::-1]*1.0
ax.barh(ys+0.2,[a[1] for a in A],color=NAVY,height=0.36,label='매매 중앙값')
ax.barh(ys-0.2,[a[2] for a in A],color=GRAY,height=0.36,label='새 세입자 전세 중앙값')
for y,(_,m,j) in zip(ys,A):
    ax.text(m+1500,y+0.2,won(m),va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(j+1500,y-0.2,won(j),va='center',fontsize=15,color='#555')
ax.set_yticks(ys); ax.set_yticklabels([a[0] for a in A],fontsize=15,color='#333')
ax.set_xlim(0,200000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.legend(loc='lower right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1~10월 계약 · 전용 83~86㎡ · 해제 · 직거래 뺌 · 전세는 월세 없는 새 계약)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gyosan_1_price.png'); plt.close()
# 2) 블록별 착공~준공 목표
B=[('A2 · 1,115가구 (LH)',2025.25,2029.5,NAVY,'청약 끝 · 2029년 6월 입주'),
   ('A8 · 763가구 (GH)',2026.5,2029.5,BLUE,'2026 하반기 착공 목표'),
   ('A21 · 347가구 (GH)',2027,2030.5,BLUE,''),
   ('A17 · 398가구 (GH)',2028,2031.5,BLUE,''),
   ('A6 · 268가구 (GH)',2031,2034.5,GRAY,''),
   ('B1 · 693가구 (GH)',2031,2034.5,GRAY,''),
   ('송파하남선(3호선 연장)',2027,2032.5,'#7A8590','2027 착공 · 2032 개통 목표')]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'교산신도시 청약일정 · 블록별 착공에서 준공까지 목표',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'청약을 받은 곳은 A2 한 곳, 나머지는 목표만 있습니다',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.68,0.68])
ys=list(range(len(B)))[::-1]
for y,(lab,s,e,c,note) in zip(ys,B):
    ax.barh(y,e-s,left=s,color=c,height=0.55)
    if note: ax.text(e+0.1,y,note,va='center',fontsize=12.5,color='#555')
ax.set_yticks(ys); ax.set_yticklabels([b[0] for b in B],fontsize=14.5,color='#333')
ax.set_xlim(2025,2037.5); ax.set_xticks(range(2025,2036)); ax.set_xticklabels([str(x) for x in range(2025,2036)],fontsize=12,color='#555')
ax.axvline(2026.85,color='#B5533C',lw=1.5,ls='--'); ax.text(2026.9,len(B)-0.45,'지금(2026년 11월)',fontsize=12.5,color='#B5533C')
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE'); ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'막대 = 착공~준공 목표 · LH 공고, GH 설계공모 발표(2025년 5 · 6월, 하남일보), 하남시 발표 · 실제 일정은 바뀔 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gyosan_2_block.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 교산신도시 · 청약일정',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'교산신도시 청약일정',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'승인 26개 블록',font=kr(ser,66),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'공고는 1곳',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'A2 청약 뒤 18개월째 다음 공고 없음',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gyosan_thumb.png')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
fig=plt.figure(figsize=(11.55,9.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'줍줍 청약 일정 · 11월 2일 무순위 4곳 · 분양가와 옆 단지 실거래',fontsize=19,color=BLUE,va='top')
fig.text(0.045,0.905,'옆 새 아파트보다 싼 곳은 수원 한 곳',fontsize=31,color=NAVY,fontweight='bold',va='top')
R=[('엘리프 한신더휴 수원 84㎡','수원 금곡동',7.13,7.95,'호반써밋 수원 (2017)',9.425,True),
   ('화서역 호수공원 아너스빌 84㎡','수원 서둔동',8.32,8.98,'힐스테이트 수원파크포레 (2024)',8.725,False),
   ('숭의역 노르웨이숲 더 스카이 69㎡','인천 숭의동',4.87,5.79,'힐스테이트 숭의역 (2025)',4.693,False),
   ('더샵 분당하이스트 84㎡','성남 정자동',26.6,29.81,'파크뷰 (2004)',24.9,False)]
for i,(nm,loc,lo,hi,nb,nv,cheap) in enumerate(R):
    ax=fig.add_axes([0.32,0.70-i*0.18,0.62,0.10]); 
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#D5DCE6'); ax.tick_params(length=0); ax.set_yticks([])
    c=NAVY if cheap else '#7A8590'
    ax.plot([lo,hi],[0,0],color=c,lw=14,solid_capstyle='butt'); ax.scatter([nv],[0],s=260,marker='D',color=BLUE if cheap else GRAY,zorder=3,edgecolor='white',lw=2)
    span=max(hi,nv)-min(lo,nv); pad=span*0.35+0.3
    ax.set_xlim(min(lo,nv)-pad,max(hi,nv)+pad); ax.set_ylim(-1,1)
    f=lambda v:f'{v:.1f}억'.replace('.0억','억')
    ax.text((lo+hi)/2,0.45,f'분양가 {f(lo)}~{f(hi)}',ha='center',fontsize=16,color=c,fontweight='bold')
    ax.text(nv,-0.75,f'{nb} {f(nv)}',ha='center',fontsize=14,color='#555')
    ax.set_xticks([])
    fig.text(0.045,0.75-i*0.18,nm,fontsize=18,color=c,fontweight='bold',va='center')
    fig.text(0.045,0.72-i*0.18,loc+(' · 옆보다 쌈' if cheap else ''),fontsize=15,color=BLUE if cheap else '#7A8590',va='center')
fig.text(0.045,0.03,'막대 = 무순위 분양가 범위 · ◆ = 같은 동 비슷한 면적 2026년 매매 실거래 중앙값 · 국토교통부 실거래 · 각 모집공고',fontsize=14,color='#8A8578')
fig.savefig('img/nangman_jupjup1102_1_compare.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 11월 2일 무순위 4곳',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'줍줍 청약 일정',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'옆 단지보다 싼 곳은',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'수원 한 곳',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'분당 · 화서역 · 숭의역 · 수원 당수',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_jupjup1102_thumb.png')

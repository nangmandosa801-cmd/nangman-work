import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'

# 1. 미사강변도시 84㎡ 연도별 중앙값 2015~2026
Y=[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]
V=[39340,50500,56200,68000,70000,88000,107000,93250,85000,92000,101000,120000]
Nn=[12,328,371,492,501,621,371,112,416,584,817,433]
col=[GRAY]*6+[BLUE,GRAY,BLUE,GRAY,GRAY,NAVY]
fig=plt.figure(figsize=(11.55,7.8),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'하남 미사지구 개발 · 미사강변도시 84㎡ 매매 중앙값, 해마다',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.915,'3억 9천 → 10억 7천(2021) → 8억 5천(2023) → 12억(2026)',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.17,0.9,0.63])
xs=list(range(len(Y)))
ax.bar(xs,V,color=col,width=0.64)
for x,v,n in zip(xs,V,Nn):
    ax.text(x,v+2500,won(v) if v%10000 else won(v),ha='center',fontsize=12.5,color=NAVY,fontweight='bold')
    ax.text(x,-13500,f'{n}건',ha='center',fontsize=11,color='#7A8590')
ax.axhline(34700,color='#B5533C',lw=1.6,ls='--'); ax.text(11.45,37500,'2014년 LH 공공분양 84㎡ 3억 4,700만',ha='right',fontsize=12.5,color='#B5533C')
ax.set_xticks(xs); ax.set_xticklabels([str(y) for y in Y],fontsize=13,color='#333'); ax.tick_params(axis='x',length=0,pad=6)
ax.set_ylim(0,136000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(6,114000,'고점',ha='center',fontsize=13,color=BLUE,fontweight='bold'); ax.text(8,92000,'바닥',ha='center',fontsize=13,color=BLUE,fontweight='bold')
fig.text(0.045,0.03,'국토교통부 매매 실거래(망월 · 풍산 · 선동 2014년 이후 아파트 전용 83~86㎡ · 해제 · 직거래 뺌 · 2026년은 1~10월) · 분양가는 아주경제 2014.9.17 보도',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa_history_1_yearly.png'); plt.close()

# 2. 2009년 지정부터 2026년까지 한 줄 시간표
E=[('2009.5','시범지구\n선정',NAVY),('2013.10','첫 민영 분양\n푸르지오',BLUE),('2014.6','첫 입주',NAVY),('2014.9','LH 공공분양\n84㎡ 3억 4,700만',BLUE),('2018','입주\n거의 마무리',GRAY),('2020.8','5호선\n미사역 개통',NAVY),('2021','고점\n10억 7천',BLUE),('2023','바닥\n8억 5천',BLUE),('2026','12억\n(1~10월)',NAVY)]
fig=plt.figure(figsize=(11.55,6.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.95,'하남 미사지구 개발 · 2009년 지정에서 2026년까지',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.885,'분양가 3억 4,700만이 12년 만에 12억, 3.5배',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.03,0.1,0.94,0.64]); ax.set_xlim(-0.6,len(E)-0.4); ax.set_ylim(-1.3,1.3); ax.axis('off')
ax.plot([-0.4,len(E)-0.6],[0,0],color='#C8D2DE',lw=4,zorder=1)
for i,(d,t,c) in enumerate(E):
    ax.scatter([i],[0],s=260,color=c,zorder=3)
    up=(i%2==0)
    ax.text(i,0.42 if up else -0.42,d,ha='center',va='bottom' if up else 'top',fontsize=15,color=c,fontweight='bold')
    ax.text(i,0.78 if up else -0.78,t,ha='center',va='bottom' if up else 'top',fontsize=13,color='#333',linespacing=1.4)
fig.text(0.045,0.03,'머니투데이 2009.5.15 · 경기일보 2013.9.30 · 이투데이 2014.4.7 · 아주경제 2014.9.17 · 경기일보 2020.8.8 · 국토교통부 실거래',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa_history_2_timeline.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 미사강변도시 17년',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'하남 미사지구 개발',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'분양가 3억 4,700만이',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'12년 만에 12억',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'2009년 지정 · 2014년 입주 · 2026년 3.5배',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa_history_thumb.png')

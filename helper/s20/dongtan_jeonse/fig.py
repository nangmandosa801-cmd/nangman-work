import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 그림 1: 같은 이름 단지 짝 — 역 앞(시범길 · 동탄역로) vs 외곽 순환대로 84㎡ 새 세입자 전세
P=[('호반써밋\n시범 · 순환대로\n(둘 다 2015)','',64500,'',48000),
   ('반도유보라 아이비파크\n시범 1.0 · 순환대로 2.0\n(2015 · 2016)','',68500,'',45000),
   ('대원칸타빌\n시범 · 포레지움\n(둘 다 2015)','',65500,'',43000),
   ('동탄역롯데캐슬 (2021)\n한화 포레나 동탄호수\n(2020)','',82500,'',40000)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'동탄 아파트 전세 시세 · 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.912,'같은 이름 단지, 역 앞과 외곽은 1억 6,500만~2억 3,500만 차이',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.2,0.9,0.6])
import numpy as np
x=np.arange(len(P)); w=0.36
a=[p[2] for p in P]; b=[p[4] for p in P]
ax.bar(x-w/2,a,w,color=NAVY,label='동탄역 앞 (동탄역로 · 동탄대로시범길)')
ax.bar(x+w/2,b,w,color=GRAY,label='외곽 (동탄순환대로)')
for i,p in enumerate(P):
    ax.text(i-w/2,p[2]+1200,won(p[2]),ha='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(i+w/2,p[4]+1200,won(p[4]),ha='center',fontsize=13.5,color='#555',fontweight='bold')
    ax.text(i,-2500,p[0],ha='center',va='top',fontsize=13,color='#333',fontweight='bold')
ax.set_xticks([]); ax.set_ylim(0,100000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=13,frameon=False)
fig.text(0.045,0.025,'국토교통부 아파트 전월세 실거래(2026년 1~10월 · 화성시 동탄구 · 전용 83~86㎡ · 월세 없는 신규 계약) · 위치는 도로명 주소 기준',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_dongtan_jeonse_1_pair.png'); plt.close()

# 그림 2: 도로별 84㎡ 새 세입자 전세 · 매매 중앙값
R=[('동탄역 앞\n(동탄역로 · 시범길)',65000,125000),('남북 간선\n(동탄대로)',46500,76400),('외곽 순환\n(동탄순환대로)',43000,70800)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'동탄2 도로별 84㎡ 새 세입자 전세와 매매 · 2026년 1~10월 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'매매는 5억 4천 차이, 전세는 2억 2천 차이',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=np.arange(len(R))[::-1]*1.0; h=0.34
ax.barh(ys+h/2,[r[2] for r in R],h,color=GRAY,label='매매')
ax.barh(ys-h/2,[r[1] for r in R],h,color=NAVY,label='새 세입자 전세')
for y,r in zip(ys,R):
    ax.text(r[2]+1500,y+h/2,won(r[2]),va='center',fontsize=14.5,color='#555',fontweight='bold')
    ax.text(r[1]+1500,y-h/2,won(r[1])+f'  (매매의 {round(r[1]/r[2]*100)}%)',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in R],fontsize=15,color='#333')
ax.set_xlim(0,150000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.legend(loc='lower right',fontsize=13,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매(해제 거래 뺌) · 전월세(월세 없는 신규 계약) 실거래 · 화성시 동탄구 · 전용 83~86㎡',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_dongtan_jeonse_2_road.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 화성 동탄2 · 84㎡ 전세',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'동탄 아파트 전세',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'동탄역 앞 시범단지',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'6억 5천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'외곽 순환대로 쪽은 4억 3천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_dongtan_jeonse_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_dongtan_jeonse_1_pair_v2.png', '같은 이름 단지, 역 앞과 외곽은 1억 6,500만~2억 3,500만 차이', [('호반써밋|역 앞 · 시범', 64500.0, '6억 4,500만', False), ('호반써밋|외곽 · 순환대로', 48000.0, '4억 8,000만', False), ('반도유보라 아이비파크|역 앞 · 시범 1.0', 68500.0, '6억 8,500만', True), ('반도유보라 아이비파크|외곽 · 순환대로 2.0', 45000.0, '4억 5,000만', False)], note='동탄 아파트 전세 시세 · 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월')
bars('img/nangman_dongtan_jeonse_2_road_v2.png', '매매는 5억 4천 차이, 전세는 2억 2천 차이', [('동탄역 앞|매매', 125000.0, '12억 5,000만', False), ('외곽 순환|매매', 70800.0, '7억 800만', False), ('동탄역 앞|새 세입자 전세', 65000.0, '6억 5,000만', True), ('외곽 순환|새 세입자 전세', 43000.0, '4억 3,000만', False)], note='동탄2 도로별 84㎡ 새 세입자 전세와 매매 · 2026년 1~10월 중앙값')
print('v2 ok')

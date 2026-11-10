import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, csv
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1) 미사강변도시 84㎡ 월별 매매 중앙값 (해제 거래 뺌)
R=list(csv.DictReader(open('m84.csv')))
lab=[r['계약년월'] for r in R]; med=[float(r['median'])/10000 for r in R]; cnt=[int(r['count']) for r in R]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'미사섬 개발 발표 직전 · 미사강변도시 84㎡ 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1년 사이 10억 4,500만 → 12억 9,500만',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.36,0.88,0.44]); ax2=fig.add_axes([0.07,0.12,0.88,0.17])
x=list(range(len(R)))
ax.plot(x,med,color=NAVY,lw=3,marker='o',ms=6)
for i in [0,9,len(R)-1]:
    v=int(round(med[i]*10000)); dy=-0.6 if i==0 else 0.35; ax.text(i+(0.3 if i==0 else -0.2 if i==9 else 0),med[i]+dy,f'{v//10000}억 {v%10000:,}만',ha=('left' if i==0 else 'right' if i==9 else 'center'),fontsize=14,color=NAVY,fontweight='bold')
ax.axvline(9.6,color=GRAY,ls='--',lw=1.5); ax.text(9.75,9.7,'2025.10.20\n하남 아파트\n토지거래허가',fontsize=12.5,color=BLUE,va='bottom')
ax.set_ylim(9,14.6); ax.set_xlim(-0.6,len(R)-0.4); ax.set_xticks([])
ax.set_yticks([10,11,12,13,14]); ax.set_yticklabels([f'{v}억' for v in [10,11,12,13,14]],fontsize=13,color='#555')
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE'); ax.grid(axis='y',color='#EEF1F5')
ax2.bar(x,cnt,color=[BLUE if i==9 else GRAY for i in x],width=0.6)
for i,c in enumerate(cnt): ax2.text(i,c+3,str(c),ha='center',fontsize=11,color='#555')
ax2.set_xlim(-0.6,len(R)-0.4); ax2.set_ylim(0,150); ax2.set_yticks([])
ax2.set_xticks(x); ax2.set_xticklabels([f"{l[2:4]}.{int(l[4:])}" for l in lab],fontsize=11.5,color='#555')
for s in ['top','right','left']: ax2.spines[s].set_visible(False)
ax2.spines['bottom'].set_color('#C8D2DE')
fig.text(0.07,0.305,'월별 거래 건수',fontsize=13,color=BLUE)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 1월~2026년 11월 3일 신고분 · 망월 · 선동 · 풍산동 2014~2019년 준공 · 전용 83~86㎡ · 해제 거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misaseom_1_price.png'); plt.close()

# 2) 일정 그림
S=[('2026.10.29','후보지 발표','1만 2천 가구 · 131만㎡',NAVY),('2026.11.3 무렵','토지거래허가','후보지 · 영향권은 남기고\n나머지 그린벨트는 해제',NAVY),
   ('날짜 미정','주민공람 → 지구 지정','공람 공고일이 보상 기준',GRAY),('2030년 안','착공 목표','최단 37개월 절차',BLUE),('빠르면 2033년','첫 입주','정부 브리핑 예상',BLUE)]
fig=plt.figure(figsize=(11.55,7.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.95,'미사섬 개발 일정 · 국토교통부 10월 29일 발표 기준',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.895,'다음 순서는 주민공람과 지구 지정',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.03,0.1,0.94,0.68]); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
ax.plot([0.9,9.1],[6.2,6.2],color='#C8D2DE',lw=4,zorder=1)
for i,(d,t,s,c) in enumerate(S):
    xx=0.9+i*2.05
    ax.scatter([xx],[6.2],s=420,color=c,zorder=2,edgecolors='white',linewidths=3)
    ax.text(xx,7.6,d,ha='center',fontsize=14.5,color=c,fontweight='bold')
    ax.text(xx,4.7,t,ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(xx,3.9,s,ha='center',va='top',fontsize=12.5,color='#555',linespacing=1.5)
ax.text(0.2,0.6,'남색 = 지난 일 · 회색 = 날짜가 아직 안 나온 일 · 파랑 = 정부 목표',fontsize=12.5,color='#555')
fig.text(0.045,0.03,'국토교통부 10월 29일 발표 · 비즈워치 · 아이뉴스24 · 일문일답 보도(2026년 10월 29일)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misaseom_2_schedule.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 신규택지',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'미사섬 개발',font=kr(ser,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,530),'1만 2천 가구',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,680),'미사경정공원 옆 · 131만㎡',font=kr(san,38),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misaseom_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_misaseom_1_price_v2.png', '1년 사이 10억 4,500만 → 12억 9,500만', [('2025년 1월', 9.7, '9억 7,000만', False), ('2025년 10월', 10.45, '10억 4,500만', False), ('2026년 10월', 12.95, '12억 9,500만', True)], note='미사강변도시 84㎡ 월별 매매 중앙값')
print('v2 ok')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def clean(ax,keep='left'):
    for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
fig=plt.figure(figsize=(11.55,9.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'하남 신규택지 · 택지 발표 뒤 석 달 · 같은 단지 같은 면적 매매값',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.908,'2018년 교산 때는 미사가 가장 많이 내렸습니다',fontsize=29,color=NAVY,fontweight='bold',va='top')
P=[('2018년 12월 · 교산 3기 신도시 발표',[('하남 미사',-6.9,1),('하남 구도심',-2.2,1),('성남 · 구리 · 남양주',-0.6,0),('경기 전체',-1.1,0)]),
   ('2026년 8월 · 남양주 도심 · 광주역세권2 택지 발표',[('남양주 와부(덕소)',5.7,1),('광주역 주변',3.8,1),('남양주 다산 · 별내',5.8,0),('경기 전체',3.6,0)])]
for k,(t,R) in enumerate(P):
    ax=fig.add_axes([0.33,0.47-k*0.40,0.6,0.27])
    y=range(len(R))
    ax.barh(list(y),[v for _,v,_ in R],color=[NAVY if s else GRAY for _,_,s in R],height=0.6)
    ax.axvline(0,color='#888',lw=1)
    for i,(n,v,s) in enumerate(R): ax.text(v+(0.25 if v>=0 else -0.25),i,f'{v:+.1f}%',va='center',ha='left' if v>=0 else 'right',fontsize=16,color=NAVY,fontweight='bold')
    ax.set_yticks(list(y)); ax.set_yticklabels([n for n,_,_ in R],fontsize=15,color='#333'); ax.invert_yaxis(); ax.set_xlim(-9.5,9.5); ax.set_xticks([]); clean(ax)
    fig.text(0.045,0.77-k*0.40,t,fontsize=18,color=NAVY,fontweight='bold')
fig.text(0.045,0.022,'발표 전 석 달과 뒤 석 달(2026년은 10월 23일까지)의 같은 단지 같은 면적 중앙값 · 국토교통부 아파트 매매 실거래',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanamtaekji_1_3m.png'); plt.close()
# 2 hanam monthly trades 2018-2019
M=['18.7','8','9','10','11','12','19.1','2','3','4','5','6','7','8','9','10','11','12']
V=[195,498,353,137,55,67,63,59,79,93,144,193,276,278,213,456,557,368]
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 신규택지 · 하남 아파트 매매 거래 수 (2018년 7월 ~ 2019년 12월)',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'발표 앞뒤 넉 달은 한 달 60건 안팎',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.13,0.9,0.66])
ax.bar(range(len(V)),V,color=[NAVY if 4<=i<=7 else GRAY for i in range(len(V))],width=0.65)
for i,v in enumerate(V): ax.text(i,v+8,str(v),ha='center',fontsize=12.5,color=NAVY)
ax.set_xticks(range(len(V))); ax.set_xticklabels(M,fontsize=12.5,color='#444'); ax.set_yticks([]); clean(ax)
ax.annotate('12월 19일 교산 발표',xy=(5,67),xytext=(5,300),ha='center',fontsize=15,color=NAVY,arrowprops=dict(arrowstyle='->',color=NAVY))
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래 · 하남시 · 해제 거래 뺌 · 계약월 기준',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_hanamtaekji_2_count.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 미사 · 감일 1만 8,500가구',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'하남 신규택지',font=kr(ser,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'2018년 교산 때 미사는',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'석 달 6.9% 내렸다',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'택지 발표 두 번, 옆 아파트 실거래',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_hanamtaekji_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
cards3('img/nangman_hanamtaekji_1_3m_v2.png', '2018년 교산 때는 미사가 가장 많이 내렸습니다', [('-6.9%', '하남 미사', True, ''), ('-2.2%', '하남 구도심', False, ''), ('-1.1%', '경기 전체', False, '')], note='2018년 교산 발표 뒤 석 달 · 같은 단지 같은 면적 매매값')
bars('img/nangman_hanamtaekji_2_count_v2.png', '발표 앞뒤 넉 달은 한 달 60건 안팎', [('2018년 8월', 498.0, '498건', False), ('10월', 137.0, '137건', False), ('11월', 55.0, '55건', True), ('2019년 2월', 59.0, '59건', False), ('5월', 144.0, '144건', False)], note='하남 신규택지 · 하남 아파트 매매 거래 수 (2018년 7월 ~ 2019년 12월)')
print('v2 ok')

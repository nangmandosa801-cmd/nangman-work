import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 노점온도 vs 문 표면
H=[40,50,60,70]; D=[6.0,9.3,12.0,14.4]
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.08,0.14,0.86,0.62])
head(fig,'실내 20도 기준 · 노점온도는 마그누스 근사식 계산값','현관문 결로, 습도 60%면 문 표면 12도 아래에서 물이 맺힙니다')
x=np.arange(4)
ax.bar(x,D,0.55,color=[MID,MID,WARN,WARN])
for i in range(4):
    ax.text(x[i],D[i]+0.3,f'{D[i]}도',ha='center',va='bottom',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(x[i],-0.6,f'습도 {H[i]}%',ha='center',va='top',fontsize=14.5,color=NAVY,fontweight='bold')
ax.plot([-0.6,4.2],[11.8,11.8],color=NAVY,lw=2,ls='--'); ax.text(4.3,11.8,'설계기준 문짝\n표면 11.8도\n(중부2 조건)',ha='left',va='center',fontsize=12.5,color=NAVY,fontweight='bold',linespacing=1.4)
ax.set_xlim(-0.6,5.4); ax.set_ylim(-2.5,19); clean(ax)
ax.text(-0.55,18.5,'노점온도 (이 아래면 결로)',fontsize=13,color=MID,va='top')
finish(fig,O+'gyeollo_fig1.png','설계기준 문짝 TDR 0.33 적용 계산 · 2009년 열화상 연구에서 현관문은 거실 창보다 「매우 불량」',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 중문 닫았을 때
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.04,0.08,0.92,0.70])
head(fig,'측정 사례 2건 · 패시브건축협회 Q&A · 개인 측정 블로그','중문을 닫으면 현관은 더 춥고 습해집니다 · 틈을 먼저 막아야 하는 이유')
rows=[('현관 온도','열었을 때 18도','닫은 뒤 15도','현관이 3도 더 추워짐'),('거실 온도','21도','21.5도','거실은 지킴'),('현관 습도','실내 45%','현관 60%','습기가 현관에 갇힘'),('현관문 결로','—','심해질 수 있음','협회: 「지금은 달지 말라」')]
for xx,t in [(0.02,'항목'),(0.26,'중문 열었을 때'),(0.50,'중문 닫았을 때'),(0.74,'뜻')]:
    ax.text(xx,1.0,t,ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
for i,(a,b,c,d) in enumerate(rows):
    y=0.84-i*0.24; col=WARN if i in (0,2,3) else NAVY
    ax.plot([0.02,0.98],[y-0.12,y-0.12],color=LINE,lw=1)
    ax.text(0.02,y,a,ha='left',va='center',fontsize=15.5,color=NAVY,fontweight='bold')
    ax.text(0.26,y,b,ha='left',va='center',fontsize=15,color=NAVY)
    ax.text(0.50,y,c,ha='left',va='center',fontsize=15,color=col,fontweight='bold')
    ax.text(0.74,y,d,ha='left',va='center',fontsize=13.5,color=MID)
ax.set_xlim(0,1); ax.set_ylim(-0.15,1.12); clean(ax)
finish(fig,O+'gyeollo_fig2.png','순서: ① 현관문 문풍지로 틈 막기 → ② 습도 50% 아래 → ③ 중문 (하부 레일 모헤어까지) · 중문의 역할은 문 여닫을 때 거실 공기 지키기',brand='낭만 인테리어',allow_outside=True,strict=False)

render_interior('낭만 인테리어 · 겨울 준비',['현관문 결로 해결','중문만 달면 더 심해집니다'],'문 표면 12도 아래면 결로 · 방화문이라 하자 인정 어려움','문풍지 → 습도 50% → 그 다음 중문',O+'gyeollo_thumb.png')
print('ok')

import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

# fig1 유리별 추가금
R=[('투명 패브릭 이중 접합 강화',31,WARN),('투명 샤틴 · 브론즈 샤틴 강화',8,NAVY),('모루 강화',5,NAVY),('브론즈 강화',0,MID),('투명 강화 (기준 3만원)',0,MID)]
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.32,0.12,0.64,0.66])
head(fig,'부산 한 업체 원슬라이딩 견적(2026년 6월) · 투명 강화 3만원 기준 차액','중문 유리 종류별 가격, 모루 +5만원 샤틴 +8만원 패브릭 접합 +31만원입니다')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i
    if v>0: ax.barh(y,v,0.6,color=c); ax.text(v+0.5,y,f'+{v}만원',va='center',fontsize=16,color=c,fontweight='bold')
    else: ax.text(0.5,y,'+0 (기본)',va='center',fontsize=15,color=MID,fontweight='bold')
    ax.text(-0.8,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,40); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'glass_fig1.png','다른 업체: 모루 +2만(전주) · 브론즈샤틴 +5만(이천·여주) · 「모루 10~20만」은 근거 없는 추정치 · 크기·지역에 따라 다름',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 강화 여부·깨짐
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.04,0.08,0.92,0.70])
head(fig,'한국판유리창호협회 자료 · 허용 열응력(kg/㎠) 일반 180 · 망입 100 · 강화 500','망입유리는 강화가 안 되고, 안전이 목적이면 접합유리입니다')
rows=[('투명·모루·샤틴 강화','3~8배','콩알처럼 부서져 흩어짐','됨',NAVY),('망입 (철망)','일반 유리 수준','철망이 잡아 안 흩어짐','안 됨',WARN),('접합 (필름·패브릭)','강화 접합이면 강함','조각이 필름에 붙어 있음','됨 (강화 뒤 접합)',NAVY),('망입 인쇄 · 부식 망입','3~8배','콩알처럼','됨 (무늬만 망입)',NAVY)]
for x,t in [(0.02,'유리'),(0.30,'충격에'),(0.52,'깨지면'),(0.80,'강화')]:
    ax.text(x,1.0,t,ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
for i,(a,b,c,d,col) in enumerate(rows):
    y=0.84-i*0.24
    ax.plot([0.02,0.98],[y-0.12,y-0.12],color=LINE,lw=1)
    ax.text(0.02,y,a,ha='left',va='center',fontsize=15.5,color=col,fontweight='bold')
    ax.text(0.30,y,b,ha='left',va='center',fontsize=14,color=NAVY)
    ax.text(0.52,y,c,ha='left',va='center',fontsize=14,color=NAVY)
    ax.text(0.80,y,d,ha='left',va='center',fontsize=15,color=col,fontweight='bold')
ax.set_xlim(0,1); ax.set_ylim(-0.15,1.12); clean(ax)
finish(fig,O+'glass_fig2.png','강화유리 자파는 8,000kg당 1장(협회) · 중문 한 짝 5~6kg이면 1,300~1,600짝에 하나 · 비산방지 필름 권장',brand='낭만 인테리어',allow_outside=True,strict=False)

render_interior('낭만 인테리어 · 중문 고르기',['중문 유리 종류','5mm 강화가 기본입니다'],'모루 +5만 · 샤틴 +8만 · 패브릭 접합 +31만','망입만 강화 안 됨 · 유리 교체 한 짝 10~15만원',O+'glass_thumb.png')
print('ok')

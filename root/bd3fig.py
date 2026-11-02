import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_bd3_'
render('낭만 부동산 분석 플랫폼 · 분당 선도지구 3차',
       ['분당 선도지구 3차,','2030년까지 순서 절반을 미리 정합니다'],
       '2027년 약 1만 가구 + 예비구역 약 1만 5천 가구', O+'thumb.png')

# fig1 연도별 물량
yrs=['2024\n선도지구','2026\n2차','2027\n3차','2028','2029','2030']
done=[12055,13429,0,0,0,0]; y27=[0,0,10000,0,0,0]; pre=[0,0,0,5000,5000,5000]; sep=[0,0,0,5000,5000,5000]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.17,0.88,0.58])
fig.text(0.04,0.955,'분당 특별정비구역 연도별 물량 · 2027년 이후는 계획(내외)',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'2027년 한 번에 2만 5천 가구를 고릅니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x=range(6)
ax.bar(x,done,0.62,color=NAVY)
ax.bar(x,y27,0.62,color=MID)
ax.bar(x,pre,0.62,color=WARN)
ax.bar(x,sep,0.62,bottom=pre,color='#D9D3C7')
for i,v in [(0,'1만 2,055'),(1,'1만 3,429'),(2,'약 1만')]:
    ax.text(i,[12055,13429,10000][i]+400,v,ha='center',fontsize=15,color=NAVY,fontweight='bold')
for i in (3,4,5): ax.text(i,10400,'약 1만',ha='center',fontsize=15,color=NAVY,fontweight='bold')
fig.text(0.46,0.835,'■ 이미 선정',fontsize=14,color=NAVY,fontweight='bold'); fig.text(0.56,0.835,'■ 2027년 지정분',fontsize=14,color=MID,fontweight='bold')
fig.text(0.73,0.835,'■ 예비 약 5천',fontsize=14,color=WARN,fontweight='bold'); fig.text(0.87,0.835,'■ 별도 약 5천',fontsize=14,color='#A8A194',fontweight='bold')
for i,l in enumerate(yrs): ax.text(i,-900,l,ha='center',va='top',fontsize=14,color=NAVY,linespacing=1.4)
ax.plot([1.6,1.6,5.4,5.4],[12800,13300,13300,12800],color=WARN,lw=2)
ax.text(3.5,13600,'2027년 9월 한 번에 선정 · 약 2만 5천 가구',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.set_xlim(-0.6,5.6); ax.set_ylim(-3600,15500); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','성남시 2027년 지정계획 · 2027년 이후 물량은 모두 「내외」로 바뀔 수 있음',allow_outside=True,strict=False)

# fig2 예전 vs 이제
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.03,0.08,0.94,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
fig.text(0.04,0.955,'분당 예비 특별정비구역',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'떨어지면 다시 줄 서던 방식에서, 미리 예약하는 방식으로',fontsize=23,color=NAVY,fontweight='bold',va='center')
def box(x,y,w,h,t,c,fc='white',tc=None,fs=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.4',fc=fc,ec=c,lw=2))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=tc or c,fontweight='bold',linespacing=1.35)
ax.text(2,72,'지금까지',fontsize=19,color=SAND,fontweight='bold')
for i,t in enumerate(['2024 선도지구 신청','2026 2차 신청','떨어지면 다음 해 또 신청']):
    box(4+i*32,56,25,9,t,SAND)
    if i<2: ax.add_patch(FancyArrowPatch((29.8+i*32,60.5),(35.2+i*32,60.5),arrowstyle='-|>',mutation_scale=16,color=SAND,lw=2))
ax.text(50,50,'해마다 처음부터 다시 경쟁',ha='center',fontsize=15,color='#555555')
ax.text(2,40,'2027년부터',fontsize=19,color=NAVY,fontweight='bold')
box(4,8,22,26,'2027년\n한 번 선정\n약 2만 5천',NAVY,fc=NAVY,tc='white',fs=17)
for i,(t,c,fc,tc) in enumerate([('2027년 지정 · 약 1만',MID,'white',MID),('2028년 예비 · 약 5천',WARN,'white',WARN),('2029년 예비 · 약 5천',WARN,'white',WARN),('2030년 예비 · 약 5천',WARN,'white',WARN)]):
    y=29-i*7.4
    ax.add_patch(FancyArrowPatch((27.5,21),(39,y+2.6),arrowstyle='-|>',mutation_scale=14,color=SAND,lw=1.6))
    box(40,y,30,5.2,t,c,fs=15)
ax.text(73,21.5,'정해진 해에\n제안서를 다시 내고\n절차를 밟습니다',fontsize=14.5,color='#555555',va='center',linespacing=1.5)
finish(fig,O+'fig2.png','예비구역은 자동 지정이 아니며, 구역이 그해 물량을 넘으면 지정되지 않을 수 있음',allow_outside=True,strict=False)

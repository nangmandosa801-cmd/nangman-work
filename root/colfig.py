import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_colbern_'
render('낭만 부동산 분석 플랫폼 · 하남 캠프콜번',
       ['캠프콜번,','물류 11%·녹지 45%, 공사는 2029년'],
       '23만 4,132㎡ 땅 쓰임과 일정 · 옆 창우동 아파트 시세', O+'thumb.png')

# fig1 땅 쓰임 가로 누적 막대
u=[('기반시설·녹지',105991,45.1,'#D9D3C7'),('자족시설',49604,21.2,NAVY),('문화시설',33083,14.1,MID),('물류시설',26700,11.4,WARN),('업무시설',18754,8.0,SAND)]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.05,0.52,0.90,0.20])
fig.text(0.04,0.955,'캠프콜번 23만 4,132㎡ 땅 쓰임 · 우선협상대상자 제안',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'절반 가까이 도로·공원이고, 물류는 11.4%입니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
x=0
for n,a,r,c in u:
    ax.barh(0,r,left=x,color=c,height=0.8,edgecolor='white',lw=2)
    pass
    x+=r
ax.set_xlim(0,100); ax.set_ylim(-0.5,0.5); ax.axis('off')
for i,(n,a,r,c) in enumerate(u):
    y=0.43-i*0.065
    fig.text(0.08,y,'■',fontsize=20,color=c if c!='#D9D3C7' else '#B8B0A2',va='center')
    fig.text(0.12,y,n,fontsize=17,color=NAVY,fontweight='bold',va='center')
    fig.text(0.55,y,f'{a:,}㎡',fontsize=17,color=NAVY,va='center',ha='right')
    fig.text(0.70,y,f'{r}%',fontsize=17,color=WARN if n=='물류시설' else NAVY,fontweight='bold',va='center',ha='right')
fig.text(0.08,0.43-5*0.065,'주택은 없습니다',fontsize=16,color='#555555',va='center')
finish(fig,O+'fig1.png','하남시·사업자 자료 인용 보도(2026년 2월) · 계획은 사업협약·인허가에서 바뀔 수 있음',allow_outside=True,strict=False)

# fig2 동별 변화
g=['감이동 (감일)','망월동 (미사)','학암동 (위례)','풍산동','창우동','덕풍동','신장동']
a=[23.3,22.1,20.9,15.9,15.6,10.9,9.3]; b=[62.7,16.8,17.9,9.6,3.2,1.1,4.5]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.24,0.12,0.70,0.66])
fig.text(0.04,0.955,'하남 동별 같은 단지·같은 면적 가격 변화 중간값',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'캠프콜번 옆 창우동은 올해도 하남 중간입니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.24,0.825,'■ 2025년→2026년',fontsize=15,color=NAVY,fontweight='bold'); fig.text(0.46,0.825,'■ 2021년→2026년',fontsize=15,color=SAND,fontweight='bold')
for i in range(len(g)):
    y=len(g)-1-i; hl=g[i]=='창우동'
    ax.barh(y+0.19,a[i],0.36,color=WARN if hl else NAVY); ax.barh(y-0.19,b[i],0.36,color=SAND)
    ax.text(a[i]+0.8,y+0.19,f'+{a[i]}%',va='center',fontsize=14,color=WARN if hl else NAVY,fontweight='bold')
    ax.text(b[i]+0.8,y-0.19,f'+{b[i]}%',va='center',fontsize=14,color='#6E675C',fontweight='bold')
    fig.text(0.225,0.12+0.66*(y+0.5)/len(g),g[i],ha='right',va='center',fontsize=16,color=WARN if hl else NAVY,fontweight='bold')
ax.set_ylim(-0.6,len(g)-0.4); ax.set_xlim(0,72); ax.set_yticks([]); ax.set_xticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axvline(0,color=LINE,lw=1.5)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 2026년은 8월 계약분까지 · 두 해 모두 거래 있는 단지만',allow_outside=True,strict=False)

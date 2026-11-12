import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'; TXT='#444'; LINE='#D5DCE6'
def base(top,title,h=7.4):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.95,top,fontsize=19,color=BLUE,va='top')
    fig.text(0.045,0.885,title,fontsize=31,color=NAVY,fontweight='bold',va='top')
    return fig
def clean(ax):
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
M=['첫 달','둘째 달','셋째 달','넷째 달','다섯째 달','여섯째 달','일곱째 달']
# 1 big vs small
fig=base('입주장 전세 · 전국 새 아파트 50곳 · 첫 두 달 금액 = 100','계약이 많은 큰 단지일수록 넷째 달부터 더 올랐습니다',h=7.8)
ax=fig.add_axes([0.07,0.13,0.8,0.6]); clean(ax)
big=[101,100,101,105,107,110,112]; sm=[102,100,98,100,102,100,101]
ax.plot(range(7),big,color=NAVY,lw=5,marker='o',ms=12,zorder=3); ax.plot(range(7),sm,color=GRAY,lw=5,marker='o',ms=12)
for i,(b,s) in enumerate(zip(big,sm)):
    if i>=3: ax.text(i-0.05 if i==6 else i,b+0.9,str(b),ha='center',fontsize=21,fontweight='bold',color=NAVY)
ax.text(6.35,112,'큰 단지\n21곳',fontsize=20,color=NAVY,fontweight='bold',va='center')
ax.text(6.35,101,'작은 단지\n29곳',fontsize=20,color='#7A8590',fontweight='bold',va='center')
ax.set_ylim(95,115); ax.set_yticks([]); ax.set_xlim(-0.3,7.4)
ax.set_xticks(range(7)); ax.set_xticklabels(M,fontsize=18,color=TXT)
fig.text(0.045,0.035,'큰 단지 = 입주장 전월세 계약 100건 넘게 신고 · 같은 단지 같은 면적 전세 비교 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_geupmae_1_big.png'); plt.close()
# 2 geupmae concentration big
fig=base('입주장 전세급매 · 큰 단지 21곳','가장 싼 전세는 둘째 달에 1.6배 몰렸습니다',h=7.8)
ax=fig.add_axes([0.07,0.13,0.88,0.6]); clean(ax)
v=[0.68,1.58,0.95,1.35,0.95,0.70,0.10]
cols=[NAVY if x>=1.3 else GRAY for x in v]
ax.bar(range(7),v,0.6,color=cols); ax.axhline(1,color='#7A8590',lw=2,ls=(0,(4,4)))
ax.text(6.45,1.0,'평소',fontsize=17,color='#7A8590',va='center')
for i,x in enumerate(v): ax.text(i,x+0.04,f'{x:.1f}배' if x>=0.95 else f'{x:.1f}배',ha='center',fontsize=21,fontweight='bold',color=NAVY if x>=1.3 else '#7A8590',bbox=dict(fc='white',ec='none',pad=1))
ax.set_ylim(0,1.9); ax.set_yticks([]); ax.set_xticks(range(7)); ax.set_xticklabels(M,fontsize=18,color=TXT); ax.set_xlim(-0.5,6.9)
fig.text(0.045,0.035,'같은 단지 같은 면적 전세 가운데 가장 싸게 계약된 10%가 그달에 나온 비율 ÷ 그달 전체 계약 비율 · 국토교통부 전월세 실거래',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_geupmae_2_month.png'); plt.close()
print('ok')

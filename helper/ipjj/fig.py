import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
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
    ax.yaxis.grid(True,color='#EEF1F5'); ax.set_axisbelow(True)
M=['첫 달','둘째','셋째','넷째','다섯째','여섯째','일곱째']
# 1 index line
fig=base('입주장 전세 · 전국 새 아파트 50곳','첫 석 달은 그대로, 넷째 달부터 올랐습니다')
ax=fig.add_axes([0.07,0.13,0.88,0.6]); clean(ax)
v=[101,100,100,103,104,106,108]
ax.axvspan(-0.4,2.4,color='#F1F6FB'); ax.text(1,108.6,'첫 석 달',ha='center',fontsize=22,color=BLUE,fontweight='bold')
ax.plot(range(7),v,color=NAVY,lw=5,marker='o',ms=13)
for i,x in enumerate(v): ax.text(i,x+0.75,str(x),ha='center',fontsize=24,fontweight='bold',color=NAVY)
ax.set_ylim(97,110); ax.set_xlim(-0.4,6.4); ax.set_yticks([])
ax.set_xticks(range(7)); ax.set_xticklabels([m if m=='첫 달' else m+' 달' for m in M],fontsize=20,color=TXT)
fig.text(0.045,0.035,'첫 두 달 전세 금액 = 100 · 같은 단지 같은 면적 전세 비교 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_1_month.png'); plt.close()
# 2 contract share bars
fig=base('입주장 시기 · 계약 4,533건이 나온 달','계약 10건 중 6건이 첫 넉 달에 몰립니다')
ax=fig.add_axes([0.07,0.13,0.88,0.6]); clean(ax)
s=[12,14,19,19,15,11,7]
cols=[NAVY if i<4 else GRAY for i in range(7)]
ax.bar(range(7),s,0.62,color=cols)
for i,x in enumerate(s): ax.text(i,x+0.6,f'{x}%',ha='center',fontsize=24,fontweight='bold',color=cols[i] if i<4 else '#7A8590')
ax.set_ylim(0,24); ax.set_yticks([]); ax.set_xticks(range(7)); ax.set_xticklabels([m if m=='첫 달' else m+' 달' for m in M],fontsize=20,color=TXT)
fig.text(0.045,0.035,'첫 계약 달부터 달마다 나온 전월세 계약 비중 · 전국 새 아파트 50곳 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_2_sigi.png'); plt.close()
# 3 spread
fig=base('입주장 전세급매 · 같은 단지 같은 면적 같은 달','싼 전세와 비싼 전세 차이가 넷째 달부터 벌어집니다')
ax=fig.add_axes([0.07,0.13,0.88,0.6]); clean(ax)
g=[2500,4500,4300,5000,7100,6100,9000]
cols=[GRAY,GRAY,GRAY,NAVY,NAVY,NAVY,NAVY]
ax.bar(range(7),g,0.62,color=cols)
for i,x in enumerate(g): ax.text(i,x+250,f'{x:,}만',ha='center',fontsize=22,fontweight='bold',color=NAVY if i>=3 else '#7A8590')
ax.set_ylim(0,10500); ax.set_yticks([]); ax.set_xticks(range(7)); ax.set_xticklabels([m if m=='첫 달' else m+' 달' for m in M],fontsize=20,color=TXT)
fig.text(0.045,0.035,'같은 달 전세 5건 이상일 때 아래위 10%씩 빼고 낮은 계약과 높은 계약의 차이 · 평균 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_3_geupmae.png'); plt.close()
# 4 jeonse share
fig=base('신축아파트 전세 · 계약 가운데 전세 비중','입주장 끝 무렵에는 월세 계약이 늘어납니다')
ax=fig.add_axes([0.07,0.13,0.88,0.6]); clean(ax)
j=[83,78,69,68,63,56]
ax.bar(range(6),j,0.62,color=NAVY); ax.bar(range(6),[100-x for x in j],0.62,bottom=j,color='#E3E8EF')
for i,x in enumerate(j):
    ax.text(i,x/2,f'전세\n{x}%',ha='center',va='center',fontsize=21,fontweight='bold',color='white')
    ax.text(i,x+(100-x)/2,f'{100-x}%',ha='center',va='center',fontsize=19,color='#555')
ax.set_ylim(0,100); ax.set_yticks([]); ax.set_xticks(range(6)); ax.set_xticklabels([m if m=='첫 달' else m+' 달' for m in M[:6]],fontsize=20,color=TXT)
fig.text(0.045,0.035,'회색은 월세 · 반전세 · 전국 새 아파트 50곳 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_4_wolse.png'); plt.close()
# 5 Segyo monthly
fig=base('오산 세교파라곤 84㎡ 입주장 전세 · 2026년','2억 8천과 4억 5천이 같은 달에 계약됐습니다',h=7.8)
ax=fig.add_axes([0.08,0.13,0.87,0.6]); clean(ax)
mm=['2월','3월','4월','5월','6월','7월','8월']
med=[3.05,3.2,3.1,3.5,3.7,3.9,3.8]; lo=[3.0,2.9,2.8,2.9,3.4,3.7,3.4]; hi=[3.1,3.5,4.5,4.2,4.5,4.5,4.8]
for i in range(7):
    ax.plot([i,i],[lo[i],hi[i]],color=GRAY,lw=12,solid_capstyle='butt')
ax.plot(range(7),med,color=NAVY,lw=4,marker='o',ms=14,zorder=3)
for i,x in enumerate(med): ax.text(i+0.16,x-0.13,f'{x:.2f}'.rstrip('0').rstrip('.')+'억',fontsize=19,fontweight='bold',color=NAVY,va='center',bbox=dict(fc='white',ec='none',pad=1))
ax.annotate('4월 한 달\n2억 8천 ~ 4억 5천',xy=(2,4.45),xytext=(0.2,4.55),fontsize=19,color='#555',arrowprops=dict(arrowstyle='-',color=GRAY))
ax.set_ylim(2.6,5.0); ax.set_yticks([3,3.5,4,4.5]); ax.set_yticklabels(['3억','3.5억','4억','4.5억'],fontsize=17,color='#7A8590')
ax.set_xticks(range(7)); ax.set_xticklabels(mm,fontsize=20,color=TXT); ax.set_xlim(-0.4,6.8)
fig.text(0.045,0.035,'남색 선은 달별 전세 중앙값 · 회색 막대는 그달 가장 낮은 계약 ~ 가장 높은 계약 · 국토교통부 전월세 실거래',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_5_segyo.png'); plt.close()
# 6 slope complexes
fig=base('신축 입주장 전세 · 단지별 처음 전세와 최근 전세','올라간 단지와 내려온 단지',h=9.6)
ax=fig.add_axes([0.05,0.1,0.9,0.66]); ax.axis('off')
D=[('오산 세교파라곤 84㎡',3.2,3.9),('포항 학산 한신더휴 84㎡',2.3,2.75),('오산 호반써밋 라프리미어 59㎡',2.48,3.0),('신검단 디에트르 더에듀 59㎡',2.55,3.0),('신검단 칸타빌 더스위트 84㎡',3.0,3.3),('대구 힐스테이트 동대구센트럴 84㎡',3.2,3.5),('검단 롯데캐슬 넥스티엘 84㎡',4.5,4.05),('이천 힐스테이트 이천역 1단지 84㎡',3.65,3.2)]
def f(x):
    e=int(round(x*10000))//10000; r=int(round(x*10000))%10000
    if not r: return f'{e}억'
    s=f'{r//1000}천' if r%1000==0 else f'{r:,}'
    return (f'{e}억 ' if e else '')+s+'만'
n=len(D)
for k,(nm,a,b) in enumerate(D):
    y=n-k; up=b>a; c=NAVY if up else '#7A8590'
    ax.text(0,y,nm,fontsize=20,color=NAVY if up else '#555',fontweight='bold',va='center')
    ax.text(0.60,y,f(a),fontsize=20,color='#555',va='center',ha='right')
    ax.annotate('',xy=(0.70,y),xytext=(0.615,y),arrowprops=dict(arrowstyle='-|>',color=c,lw=3,mutation_scale=22))
    ax.text(0.715,y,f(b),fontsize=21,color=c,fontweight='bold',va='center',ha='left')
    ax.text(1.0,y,('+' if up else '−')+f(abs(b-a)),fontsize=20,color=c,fontweight='bold',va='center',ha='right')
ax.set_xlim(0,1); ax.set_ylim(0.4,n+0.6)
fig.text(0.045,0.035,'처음 = 첫 계약 무렵 전세 중앙값 · 최근 = 가장 최근 달 중앙값 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_ipjujang_jeonse_6_danji.png'); plt.close()
print('ok')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_ipjujang_jeonse_2_sigi_v2.png', '계약 10건 중 6건이 첫 넉 달에 몰립니다', [('첫 달', 12.0, '12%', False), ('둘째 달', 14.0, '14%', False), ('셋째 달', 19.0, '19%', True), ('넷째 달', 19.0, '19%', False), ('일곱째 달', 7.0, '7%', False)], note='입주장 시기 · 계약 4,533건이 나온 달')
bars('img/nangman_ipjujang_jeonse_3_geupmae_v2.png', '싼 전세와 비싼 전세 차이가 넷째 달부터 벌어집니다', [('첫 달', 2500.0, '2,500만', False), ('셋째 달', 4300.0, '4,300만', False), ('넷째 달', 5000.0, '5,000만', True), ('다섯째 달', 7100.0, '7,100만', False), ('일곱째 달', 9000.0, '9,000만', False)], note='입주장 전세급매 · 같은 단지 같은 면적 같은 달')
bars('img/nangman_ipjujang_jeonse_4_wolse_v2.png', '입주장 끝 무렵에는 월세 계약이 늘어납니다', [('첫 달', 83.0, '83%', False), ('셋째 달', 69.0, '69%', False), ('넷째 달', 68.0, '68%', False), ('다섯째 달', 63.0, '63%', False), ('여섯째 달', 56.0, '56%', True)], note='전세 계약 비중 · 나머지는 월세')
print('v2 ok')

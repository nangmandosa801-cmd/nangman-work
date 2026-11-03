import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'; TXT='#444'; LINE='#D5DCE6'
def base(top,title,h=7.4):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.95,top,fontsize=19,color=BLUE,va='top')
    fig.text(0.045,0.885 if h<9 else 0.905,title,fontsize=31,color=NAVY,fontweight='bold',va='top')
    return fig
# 1 osan dumbbell
rows=[('힐스테이트 오산 더퍼스트 59㎡',2.1,2.205,2.8),('힐스테이트 오산 더퍼스트 84㎡',2.5,2.625,3.3),('오산 세교 한양수자인 59㎡',2.0,2.15,2.7),('오산 세교 한양수자인 64㎡',2.5,2.605,3.0),('중흥S-클래스 에듀파크 59㎡',2.3,2.415,2.8),('중흥S-클래스 에듀파크 72㎡',2.65,2.6775,3.3),('중흥S-클래스 에듀파크 84㎡',2.9,3.045,3.5),('오산 롯데캐슬 스카이파크 84㎡',2.8,2.85,3.2),('오산 라온프라이빗스위트 84㎡',2.6,2.75,3.0)]
fig=base('오산 아파트 전세 · 2024년 입주 단지 · 2026년 계약','갱신은 5%, 새 세입자는 24% 높았습니다',h=10.4)
ax=fig.add_axes([0.37,0.12,0.6,0.68])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
n=len(rows)
for i,(nm,p,g,nw) in enumerate(rows):
    y=n-i
    ax.plot([g,nw],[y,y],color='#DDE3EA',lw=10,solid_capstyle='round',zorder=1)
    ax.scatter([p],[y],s=170,facecolor='white',edgecolor=GRAY,lw=3,zorder=3)
    ax.scatter([g],[y],s=190,color=GRAY,zorder=3)
    ax.scatter([nw],[y],s=230,color=NAVY,zorder=4)
    ax.text(nw+0.04,y,f'+{round((nw-g)*10000):,}만',fontsize=18,color=NAVY,fontweight='bold',va='center')
    fig.text(0.355,0,'')
    ax.text(-0.02,y,nm,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=18,color=NAVY,fontweight='bold')
ax.set_xlim(1.9,3.85); ax.set_ylim(0.4,n+0.9); ax.set_yticks([])
ax.set_xticks([2,2.5,3,3.5]); ax.set_xticklabels(['2억','2억 5천','3억','3억 5천'],fontsize=17,color='#7A8590')
ax.scatter([2.0],[n+0.6],s=150,facecolor='white',edgecolor=GRAY,lw=3); ax.text(2.04,n+0.6,'2년 전 입주장',fontsize=17,va='center',color='#555')
ax.scatter([2.6],[n+0.6],s=170,color=GRAY); ax.text(2.64,n+0.6,'올해 갱신',fontsize=17,va='center',color='#555')
ax.scatter([3.1],[n+0.6],s=200,color=NAVY); ax.text(3.14,n+0.6,'올해 신규',fontsize=17,va='center',color=NAVY,fontweight='bold')
fig.text(0.045,0.035,'남색 숫자는 신규와 갱신의 차이 · 전세 중앙값 · 국토교통부 전월세 실거래 2026년 1월~10월 23일',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_osan_jeonse_1_osan.png'); plt.close()
# 2 sido
S=[('서울',16231),('부산',9162),('경기',7399),('세종',6388),('경남',5835),('경북',5562),('충남',5253),('인천',5214),('대구',4286),('광주·전남',3923),('대전',3850),('충북',3244),('강원',468)]
fig=base('전세 갱신요구권 · 2024년 입주 단지 259곳','같은 단지 같은 면적, 갱신과 신규 전세 차이',h=9.6)
ax=fig.add_axes([0.16,0.1,0.76,0.7])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE); ax.tick_params(length=0)
for i,(nm,v) in enumerate(S):
    y=len(S)-i; c=NAVY if nm=='경기' else GRAY
    ax.barh(y,v,0.62,color=c)
    ax.text(v+200,y,f'{v:,}만',fontsize=18,va='center',color=NAVY if c==NAVY else '#555',fontweight='bold')
ax.set_yticks([len(S)-i for i in range(len(S))]); ax.set_yticklabels([s[0] for s in S],fontsize=19,color=NAVY)
ax.set_xticks([]); ax.set_xlim(0,19000)
fig.text(0.045,0.035,'신규 전세 중앙값 − 갱신 전세 중앙값 · 단지·면적별 차이의 시도 평균 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_osan_jeonse_2_sido.png'); plt.close()
# 3 segyo 2-4 vs 6-8 and 4yr
fig=base('오산 세교파라곤 84㎡ 전세 · 2026년 입주','넉 달 차이가 4년 동안 이어집니다',h=7.8)
ax=fig.add_axes([0.07,0.13,0.88,0.6])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
X=[0,1,2.6,3.6]; V=[3.2,3.36,3.8,3.99]; C=[GRAY,GRAY,NAVY,NAVY]
L=['첫 2년','2년 뒤 갱신','첫 2년','2년 뒤 갱신']
ax.bar(X,V,0.7,color=C)
for x,v,c in zip(X,V,C):
    e=int(v); r=round((v-e)*10000); s=(f'{r//1000}천' if r%1000==0 else f'{r:,}'); ax.text(x,v+0.04,f'{e}억 {s}만' if r else f'{e}억',ha='center',fontsize=22,fontweight='bold',color=c if c==NAVY else '#555')
ax.set_xticks(X); ax.set_xticklabels(L,fontsize=19,color=TXT); ax.set_ylim(2.5,4.5); ax.set_yticks([])
ax.text(0.5,4.3,'2~4월 계약 세입자',ha='center',fontsize=21,color='#555',fontweight='bold')
ax.text(3.1,4.3,'6~8월 계약 세입자',ha='center',fontsize=21,color=NAVY,fontweight='bold')
fig.text(0.045,0.035,'2~4월 · 6~8월 신규 전세 중앙값 · 2년 뒤는 갱신요구권으로 5% 올린 금액 · 국토교통부 전월세 실거래',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_osan_jeonse_3_segyo.png'); plt.close()
print('ok')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'; TXT='#444'; LINE='#D5DCE6'
def base(top,title,h=7.4):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.95,top,fontsize=19,color=BLUE,va='top')
    fig.text(0.045,0.885 if h<9 else 0.905,title,fontsize=31,color=NAVY,fontweight='bold',va='top')
    return fig
def clean(ax,left=False):
    for s in ['top','right']+([] if left else ['left']): ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
# 1 split
fig=base('신축아파트 2년후 · 2024년에 지은 아파트 · 2026년 전월세 계약','올해 계약 두 건 중 한 건은 새 세입자였습니다',h=6.4)
ax=fig.add_axes([0.05,0.22,0.9,0.36]); ax.axis('off')
ax.barh(0,51.6,color=NAVY,height=0.6); ax.barh(0,46.2,left=51.6,color=GRAY,height=0.6); ax.barh(0,2.2,left=97.8,color='#E3E8EF',height=0.6)
ax.text(25.8,0,'새 세입자 (신규)\n52%',ha='center',va='center',fontsize=26,color='white',fontweight='bold')
ax.text(74.7,0,'다시 계약 (갱신)\n46%',ha='center',va='center',fontsize=26,color='white',fontweight='bold')
ax.set_xlim(0,100); ax.set_ylim(-0.5,0.5)
fig.text(0.045,0.06,'2024년에 지은 아파트 2026년 1월~10월 23일 전월세 계약 36,820건 · 나머지 2%는 구분 없음 · 국토교통부 전월세 실거래',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_sinchuk2_1_split.png'); plt.close()
# 2 money
fig=base('신축 전세 2년 뒤 · 2024년 입주 단지 259곳 · 같은 단지 같은 면적','다시 계약하면 4.6%, 새로 들어오면 26% 올랐습니다',h=7.6)
ax=fig.add_axes([0.07,0.13,0.88,0.58]); clean(ax); ax.spines['bottom'].set_color(LINE)
V=[3.19,3.34,4.03]; C=[GRAY,GRAY,NAVY]; L=['2년 전 입주장','올해 갱신','올해 신규']
ax.bar(range(3),V,0.55,color=C)
for i,(v,s) in enumerate(zip(V,['3억 1,900만','3억 3,400만 (+4.6%)','4억 300만 (+26%)'])): ax.text(i,v+0.05,s,ha='center',fontsize=23,fontweight='bold',color=NAVY if i==2 else '#555')
ax.set_xticks(range(3)); ax.set_xticklabels(L,fontsize=21,color=TXT); ax.set_yticks([]); ax.set_ylim(2.5,4.5)
fig.text(0.045,0.035,'단지·면적별 전세 중앙값의 평균 · 2년 전은 갱신 계약에 적힌 종전 보증금 · 국토교통부 전월세 실거래 2026년',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_sinchuk2_2_money.png'); plt.close()
# 3 sido share
S=[('대구',82),('강원',77),('경북',75),('광주·전남',73),('울산',69),('부산',65),('세종',64),('충남',64),('인천',57),('대전',51),('경남',45),('경기',44),('서울',40),('충북',38),('전북',23)]
fig=base('신축아파트 2년후 · 2024년에 지은 아파트 · 2026년 계약','새 세입자 비중, 대구 82% · 서울 40%',h=10.2)
ax=fig.add_axes([0.16,0.1,0.76,0.7]); clean(ax,left=True); ax.spines['bottom'].set_visible(False); ax.spines['left'].set_color(LINE)
for i,(nm,v) in enumerate(S):
    y=len(S)-i; c=NAVY if nm in ('대구','서울') else GRAY
    ax.barh(y,v,0.62,color=c); ax.text(v+1,y,f'{v}%',fontsize=18,va='center',color=NAVY if c==NAVY else '#555',fontweight='bold')
ax.set_yticks([len(S)-i for i in range(len(S))]); ax.set_yticklabels([s[0] for s in S],fontsize=19,color=NAVY); ax.set_xticks([]); ax.set_xlim(0,95)
fig.text(0.045,0.035,'전월세 계약 가운데 계약구분 「신규」 비중 · 계약 200건 넘는 시도 · 국토교통부 전월세 실거래 2026년 1월~10월 23일',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_sinchuk2_3_sido.png'); plt.close()
# 4 haja
fig=base('아파트 하자보수 기간 · 세대 안은 열쇠 받은 날부터','입주 2년 차에 끝나는 것은 마감공사입니다',h=8.2)
ax=fig.add_axes([0.05,0.12,0.9,0.66]); ax.axis('off')
R=[('2년','마감공사','도배 · 타일 · 도장 · 수장 · 주방기구 · 옥내가구',NAVY),('3년','설비 · 창호','창호 · 단열 · 난방 · 급배수 · 전기 · 목공사',GRAY),('5년','골조 · 방수','철근콘크리트 · 지붕 · 방수',GRAY),('10년','구조','기둥 · 보 · 내력벽 · 기초',GRAY)]
for i,(yr,nm,ex,c) in enumerate(R):
    y=3.5-i
    ax.barh(y,[0.16],left=0,color=c,height=0.72); ax.text(0.08,y,yr,ha='center',va='center',fontsize=28,color='white',fontweight='bold')
    ax.text(0.19,y+0.14,nm,fontsize=24,color=NAVY if c==NAVY else '#555',fontweight='bold',va='center')
    ax.text(0.19,y-0.2,ex,fontsize=19,color='#555',va='center')
ax.set_xlim(0,1); ax.set_ylim(-0.1,4)
fig.text(0.045,0.035,'공동주택관리법 시행령 별표 4 하자담보책임기간 · 공용부분은 사용검사일부터',fontsize=15,color='#8A8578')
fig.savefig('img/nangman_sinchuk2_4_haja.png'); plt.close()
print('ok')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_sinchuk2_3_sido_v2.png', '새 세입자 비중, 대구 82% · 서울 40%', [('대구', 82.0, '82%', False), ('강원', 77.0, '77%', False), ('인천', 57.0, '57%', False), ('서울', 40.0, '40%', True), ('전북', 23.0, '23%', False)], note='신축아파트 2년후 · 2024년에 지은 아파트 · 2026년 계약')
print('v2 ok')

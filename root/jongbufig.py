import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 공시가별 종부세: 현행 / 2027 실거주 / 2027 비거주
G=['13억','15억','20억','25억','30억']; cur=[16,47,161,353,581]; r1=[0,18,133,345,611]; r2=[73,133,345,611,958]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.06,0.14,0.90,0.62])
head(fig,'1주택 · 세액공제 전 · 농특세 별도 · 재산세 중복분 단순 공제 (추정치)','종부세 계산, 공시가 20억은 올해 161만원이고 2027년 비거주면 345만원입니다')
x=np.arange(len(G)); w=0.26
ax.bar(x-w,cur,w,color=NAVY); ax.bar(x,r1,w,color=LB); ax.bar(x+w,r2,w,color=WARN)
for i in range(len(G)):
    for dx,v,c in [(-w,cur[i],NAVY),(0,r1[i],'#5F7FA6'),(w,r2[i],WARN)]:
        ax.text(x[i]+dx,v+12,f'{v}',ha='center',va='bottom',fontsize=12.5,color=c,fontweight='bold')
    ax.text(x[i],-25,'공시가 '+G[i],ha='center',va='top',fontsize=14.5,color=NAVY,fontweight='bold')
ax.bar([0],[0],color=NAVY,label='현행 (공제 12억 · 60%)'); ax.bar([0],[0],color=LB,label='2027 실거주 (14억 · 70%)'); ax.bar([0],[0],color=WARN,label='2027 비거주 (9억 · 70%)')
ax.legend(loc='upper left',fontsize=13,frameon=False)
ax.text(4.6,1060,'단위 만원',fontsize=12.5,color=MID,va='top',ha='right')
ax.set_xlim(-0.6,4.6); ax.set_ylim(-90,1080); clean(ax)
finish(fig,O+'jongbu_fig1.png','재정경제부 2026년 세제개편안(8월 3일) 기준 · 국회 통과 전 · 고령·장기보유 세액공제는 별도',allow_outside=True,strict=False)

# fig2 84㎡ 종부세 선
fig=plt.figure(figsize=(11.2,7.4)); ax=fig.add_axes([0.06,0.12,0.90,0.64])
head(fig,'전용 84㎡ 단지 중 올해 3~8월 중앙값 17.4억(공시가 12억 환산) 초과 · 거래 2건 이상','경기 아파트 종부세, 84㎡로 선을 넘는 단지는 2,908개 중 63개입니다')
R=[('서울',1675,332),('경기',2908,63)]
for i,(nm,t,o) in enumerate(R):
    y=1-i; ax.barh(y,t,0.5,color=GREY); ax.barh(y,o,0.5,color=NAVY if i==0 else WARN)
    ax.text(t+40,y,f'{o}개 / {t:,}개 · {o/t*100:.1f}%',va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(-60,y,nm,ha='right',va='center',fontsize=17,color=NAVY,fontweight='bold',clip_on=False)
ax.text(1500,-0.55,'경기 63개 = 분당 49 · 과천 9 · 수원 영통 2 · 성남 수정 2 · 동탄 1',ha='center',va='top',fontsize=14.5,color=WARN,fontweight='bold')
ax.set_xlim(-250,4300); ax.set_ylim(-1.0,1.5); clean(ax)
finish(fig,O+'jongbu_fig2.png','국토교통부 아파트 실거래가 · 해제 거래 제외 · 공시가 환산은 시세×69% 단순 계산 · 내년 1월 공시가격 예상용',allow_outside=True,strict=False)

# fig3 일정
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.04,0.10,0.92,0.62])
head(fig,'2026년 종합부동산세 · 과세기준일 6월 1일 · 2025년은 11월 24일 발송','종부세 고지서 발송일 11월 말, 납부는 12월 1일부터 15일까지입니다')
T=[(6.0,'6월 1일','과세기준일',MID),(8.2,'9월 16~30일','합산배제·특례 신고',MID),(10.2,'11월 말','고지서 발송',WARN),(11.6,'12월 1~15일','납부 · 분납 신청',NAVY),(12.6,'12월 12일','납부유예 신청 마감',NAVY)]
ax.plot([5.5,13.0],[0,0],color=LINE,lw=3)
for i,(xp,a,b,c) in enumerate(T):
    ax.plot(xp,0,'o',ms=16,color=c)
    up=(i%2==0)
    ax.text(xp,0.55 if up else -0.55,a,ha='center',va='bottom' if up else 'top',fontsize=15,color=c,fontweight='bold')
    ax.text(xp,0.30 if up else -0.30,b,ha='center',va='bottom' if up else 'top',fontsize=13,color=NAVY)
ax.set_xlim(5.2,13.3); ax.set_ylim(-1.3,1.3); clean(ax)
finish(fig,O+'jongbu_fig3.png','250만원 초과 분납(절반은 12월, 나머지 이듬해 6월 15일) · 납부유예: 1주택 60세 이상 또는 5년 보유, 총급여 7천만원 이하',allow_outside=True,strict=False)

render('종부세 고지서',['11월 말 발송 · 12월 15일까지','12억 넘는 집 48만 7천 가구'],'경기 84㎡는 63개 단지 · 분당 49 과천 9',O+'jongbu_thumb.png')
print('ok')

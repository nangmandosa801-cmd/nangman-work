import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_jupjup_rule_'
TXT='#444'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 줍줍 청약 1편',['줍줍 청약 조건,','1주택자는 못 넣습니다'],'2025년 6월 10일부터 무주택세대구성원만',O+'thumb.png')
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,70); ax.axis('off')
fig.text(0.04,0.955,'무순위 청약 조건 · 민영주택 무순위 공급 기준',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'조였다가, 풀었다가, 다시 조였습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.plot([6,106],[58,58],color=LINE,lw=4)
S=[(21,'2021.5.28','조임',NAVY,'무주택세대구성원','해당 지역 거주자'),
   (56,'2023.2.28','풀림',OK,'국내 성년 누구나','집 여러 채도 · 거주지 제한 없음'),
   (91,'2025.6.10','다시 조임',WARN,'무주택세대구성원','거주지는 단지별로 · 시장·군수·구청장이 정함')]
for x,d,t,c,a,b in S:
    ax.add_patch(mp.Circle((x,58),2.4,fc=c,ec='white',lw=3))
    ax.text(x,64,d,ha='center',fontsize=19,color=c,fontweight='bold')
    ax.add_patch(mp.FancyBboxPatch((x-16,14),32,36,boxstyle='round,pad=0.3,rounding_size=2',fc='#F4F6F9',ec=c,lw=3))
    ax.text(x,44,t,ha='center',fontsize=24,color=c,fontweight='bold')
    ax.text(x,33,a,ha='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(x,22,b.replace(' · ','\n'),ha='center',va='center',fontsize=14.5,color=TXT,linespacing=1.5)
ax.text(56,6,'2024년 7월 동탄역 롯데캐슬 1가구에 294만 4,780명 → 다시 조인 계기',ha='center',fontsize=16,color=WARN,fontweight='bold')
finish(fig,O+'fig1.png','공공주택 무순위는 2023년에도 무주택 요건 유지 · 계약취소주택 재공급은 공고마다 조건이 다릅니다',allow_outside=True,strict=False)

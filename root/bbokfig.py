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

# fig1 붙이는 위치별 열손실 감소
R=[('창틀까지 덮어서 1겹',30,WARN),('안쪽에 2겹',25,NAVY),('안쪽 1겹 + 바깥 1겹',22,MID),('유리에 1겹',17,LB)]
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.26,0.12,0.70,0.66])
head(fig,'부산대 안영철 교수팀 · 1m×1m 미닫이창 · 5mm 단일유리 · KS F 2278 시험','창문 뽁뽁이 효과, 유리보다 창틀에 붙이면 열손실 30%가 줄어듭니다')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+0.6,y,f'{v}% 감소',va='center',fontsize=16,color=c,fontweight='bold')
    ax.text(-0.8,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,40); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'bbok_fig1.png','설비공학논문집 27권 9호(2015) · 이중유리는 개선 폭이 더 작고 로이유리 실험은 없음 · 아시아경제(2016.1.11) 수치',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 무엇이 무엇을 막나
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.04,0.08,0.92,0.70])
head(fig,'한국건설기술연구원 실험 · 창에 초속 5m 바람 · 새는 압력 7 기준','뽁뽁이는 유리로 새는 열, 문풍지는 틈바람, 현관은 중문이 맡습니다')
rows=[('뽁뽁이 (에어캡)','유리 표면 열손실','유리 표면 +2.5~3도 · 열손실 17~30%','틈바람은 못 막음'),
      ('문풍지','창짝·창틀 틈바람','외풍 20~30% 차단 (새는 압력 7→5)','유리 열손실은 그대로'),
      ('방풍비닐','창 전체','외풍 100% 차단 (7→0)','환기 안 됨 · 안 여는 창만'),
      ('암막 커튼','창 앞 공기층','난방 에너지 1.4% 절감 · 실내 0.2도','단열보다 빛 가림'),
      ('현관 중문','현관문 틈 찬 공기','찬 공기가 현관에서 멈춤','거실까지 오는 외풍 차단')]
ax.text(0.02,1.02,'무엇',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
ax.text(0.26,1.02,'막는 것',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
ax.text(0.47,1.02,'실험 수치',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
ax.text(0.80,1.02,'한계',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
for i,(a,b,c,d) in enumerate(rows):
    y=0.88-i*0.2; col=WARN if i==4 else NAVY
    ax.plot([0.02,0.98],[y-0.1,y-0.1],color=LINE,lw=1)
    ax.text(0.02,y,a,ha='left',va='center',fontsize=15.5,color=col,fontweight='bold')
    ax.text(0.26,y,b,ha='left',va='center',fontsize=14,color=NAVY)
    ax.text(0.47,y,c,ha='left',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(0.80,y,d,ha='left',va='center',fontsize=13,color=MID)
ax.set_xlim(0,1); ax.set_ylim(-0.15,1.12); clean(ax)
finish(fig,O+'bbok_fig2.png','YTN(2014.1.9) 건설연 실험 · SBS(2012.1.14) 커튼 실험 · 중문은 현장 사례 기준이며 실험 수치 없음',brand='낭만 인테리어',allow_outside=True,strict=False)

render_interior('낭만 인테리어 · 겨울 준비',['창문 뽁뽁이 효과','유리보다 창틀에 붙이세요'],'유리 표면 +2.5도 · 창틀 덮으면 열손실 30%','남향 창은 빼고 · 틈바람은 문풍지 · 현관은 중문',O+'bbok_thumb.png')
print('ok')

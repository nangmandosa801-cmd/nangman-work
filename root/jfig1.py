import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

fig, ax = plt.subplots(figsize=(10.4, 5.6))
fig.subplots_adjust(bottom=0.16, top=0.80, left=0.05, right=0.97)
ax.add_patch(mp.Rectangle((0,0.30),3,0.34, color=MID, zorder=3))
ax.add_patch(mp.Rectangle((3,0.30),2,0.34, color=WARN, zorder=3))
ax.text(1.5,0.47,'처음 제한  3년 이내', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
ax.text(4.0,0.47,'연장  2년 이내', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
ax.text(1.5,0.20,'도시계획위원회 심의 거침', ha='center', va='center', fontsize=15,
        color=MID, fontproperties=F_R, zorder=5)
ax.text(4.0,0.20,'심의 없음 · 3호~5호만', ha='center', va='center', fontsize=15,
        color=WARN, fontproperties=F_R, zorder=5)
ax.text(1.5,0.76,'한 차례만', ha='center', va='center', fontsize=15,
        color=SAND, fontproperties=F_R, zorder=5)
ax.text(4.0,0.76,'한 차례만', ha='center', va='center', fontsize=15,
        color=SAND, fontproperties=F_R, zorder=5)
for xx,lab in [(0,'0년'),(3,'3년'),(5,'5년')]:
    ax.plot([xx,xx],[0.26,0.68], color=SAND, lw=1.4, zorder=4)
    ax.text(xx,0.05,lab, ha='center', va='center', fontsize=16, color=NAVY, fontproperties=F_B)
ax.set_xlim(-0.55,5.6); ax.set_ylim(-0.05,1.02); ax.set_axis_off()
fig.text(0.05,0.945,'낭만 부동산 분석 플랫폼 · 부동산 공법', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.05,0.875,'3년에 2년, 합쳐서 최장 5년입니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/jehan/nangman_jehan_fig1.png',
       '국토의 계획 및 이용에 관한 법률 제63조 제1항 · 개발행위허가 제한 기간')
print('ok')

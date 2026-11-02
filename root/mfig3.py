import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

fig, ax = plt.subplots(figsize=(10.6, 6.4))
fig.subplots_adjust(bottom=0.14, top=0.82, left=0.04, right=0.97)
rows=[('어떤 곳','기반시설 설치가 곤란','기반시설 설치가 필요'),
      ('하는 일','용적률을 깎습니다','비용을 물립니다'),
      ('용도지역','주거 · 상업 · 공업','제한 없음'),
      ('지정','할 수 있다','하여야 한다')]
LX, RX = 1.55, 6.25; W = 4.0
ax.add_patch(mp.Rectangle((LX,0.55),W,0.75, color=MID, zorder=3))
ax.add_patch(mp.Rectangle((RX,0.55),W,0.75, color=WARN, zorder=3))
ax.text(LX+W/2,0.93,'개발밀도관리구역', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
ax.text(RX+W/2,0.93,'기반시설부담구역', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
for i,(k,a,b) in enumerate(rows):
    y = -0.35 - i*1.0
    ax.text(1.35,y,k, ha='right', va='center', fontsize=15.5, color=SAND, fontproperties=F_R, zorder=5)
    ax.text(LX+W/2,y,a, ha='center', va='center', fontsize=17.5, color=NAVY, fontproperties=F_B, zorder=5)
    ax.text(RX+W/2,y,b, ha='center', va='center', fontsize=17.5, color=NAVY, fontproperties=F_B, zorder=5)
    ax.plot([LX,RX+W],[y-0.42,y-0.42], color=LINE, lw=1.0, zorder=1)
ax.text((LX+RX+W)/2,-4.72,'둘은 겹치지 않습니다 · 부담구역은 개발밀도관리구역 밖에만',
        ha='center', va='center', fontsize=16, color=MID, fontproperties=F_B, zorder=5)
ax.set_xlim(-0.2,10.6); ax.set_ylim(-5.3,1.55); ax.set_axis_off()
fig.text(0.04,0.955,'낭만 부동산 분석 플랫폼 · 부동산 공법', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.04,0.892,'설치가 곤란하면 깎고, 필요하면 걷습니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/miltdo/nangman_miltdo_fig3.png',
       '국토의 계획 및 이용에 관한 법률 제2조 제18호·제19호와 제66조·제67조')
print('ok')

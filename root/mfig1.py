import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

fig, ax = plt.subplots(figsize=(10.4, 5.8))
fig.subplots_adjust(bottom=0.16, top=0.80, left=0.05, right=0.97)
# 원래 최대한도
ax.add_patch(mp.Rectangle((0,0.62),250,0.24, color=MID, zorder=3))
ax.text(125,0.74,'용적률 최대한도  250%', ha='center', va='center', fontsize=18,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
ax.text(-6,0.74,'원래', ha='right', va='center', fontsize=16, color=NAVY, fontproperties=F_B)
# 강화 후
ax.add_patch(mp.Rectangle((0,0.26),125,0.24, color=MID, zorder=3))
ax.plot([125,250,250,125,125],[0.26,0.26,0.50,0.50,0.26], color=WARN, lw=1.8, ls=(0,(4,3)), zorder=3)
ax.text(62,0.38,'125%', ha='center', va='center', fontsize=18,
        color='#FFFFFF', fontproperties=F_B, zorder=5)
ax.text(187,0.38,'최대 50%까지 깎을 수 있음', ha='center', va='center', fontsize=15.5,
        color=WARN, fontproperties=F_B, zorder=5)
ax.text(-6,0.38,'구역 안', ha='right', va='center', fontsize=16, color=NAVY, fontproperties=F_B)
for xx in (0,125,250):
    ax.plot([xx,xx],[0.20,0.90], color=LINE, lw=1.2, zorder=1)
    ax.text(xx,0.10,f'{xx}%', ha='center', va='center', fontsize=14, color=SAND, fontproperties=F_R)
ax.set_xlim(-62,262); ax.set_ylim(0.02,1.0); ax.set_axis_off()
fig.text(0.05,0.945,'낭만 부동산 분석 플랫폼 · 부동산 공법', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.05,0.875,'용적률 최대한도의 50퍼센트까지 깎습니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/miltdo/nangman_miltdo_fig1.png',
       '같은 법 시행령 제62조 제1항 · 제2종일반주거지역 최대한도를 250%로 가정한 예시')
print('ok')

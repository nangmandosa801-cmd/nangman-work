import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('1호','녹지·계획관리지역 보전이 필요한 곳',False),
   ('2호','환경·경관·미관·문화재 손상 우려',False),
   ('3호','도시·군기본계획이나 관리계획 수립 중',True),
   ('4호','지구단위계획구역',True),
   ('5호','기반시설부담구역',True)][::-1]

fig, ax = plt.subplots(figsize=(10.4, 6.0))
fig.subplots_adjust(bottom=0.15, top=0.82, left=0.04, right=0.97)
for i,(no,lab,ext) in enumerate(d):
    c = MID if ext else SAND
    ax.add_patch(mp.Rectangle((0,i-0.30),1.05,0.60, color=c, zorder=3))
    ax.text(0.52,i,no, ha='center', va='center', fontsize=19, color='#FFFFFF',
            fontproperties=F_B, zorder=5)
    ax.text(1.35,i,lab, ha='left', va='center', fontsize=17.5, color=NAVY,
            fontproperties=F_R, zorder=5)
    ax.text(9.75,i,'2년 연장 가능' if ext else '연장 안 됨', ha='right', va='center',
            fontsize=16, color=MID if ext else WARN, fontproperties=F_B, zorder=5)
ax.set_xlim(-0.25,10.0); ax.set_ylim(-0.85,len(d)+0.35); ax.set_axis_off()
fig.text(0.04,0.955,'낭만 부동산 분석 플랫폼 · 부동산 공법', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.04,0.892,'연장되는 건 3호부터 5호까지입니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/jehan/nangman_jehan_fig2.png',
       '같은 법 제63조 제1항 제1호~제5호 · 1호와 2호는 3년으로 끝납니다')
print('ok')

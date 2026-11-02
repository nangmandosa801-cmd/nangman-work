import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d = [('계획관리지역',66),('생산녹지지역',63),('자연녹지지역',58),('농림지역',51),
     ('보전관리지역',51),('일반공업지역',47),('개발제한구역',45),('생산관리지역',35),
     ('제2종일반주거지역',27),('제1종일반주거지역',2)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]
colors=[WARN if v<30 else (NAVY if v>=55 else MID) for v in vals]

fig, ax = plt.subplots(figsize=(9.4, 6.3))
y = np.arange(len(d))
ax.barh(y, vals, height=0.62, color=colors, zorder=3)
for i,v in enumerate(vals):
    ax.text(v+1.8, i, f'+{v}%', ha='left', va='center', fontsize=15,
            color=NAVY, fontproperties=F_B, zorder=5)
ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=15, fontproperties=F_R)
ax.set_xlim(0, 88); ax.set_ylim(-0.75, len(d)-0.25)
ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
finish(fig, '/mnt/user-data/outputs/재배치/nangman/yangju2/nangman_yangju2_fig3.png',
       '단독 필지 평당 중간값 · 2014~2016년 대비 2024~2026년 8월')
print('fig3 ok')

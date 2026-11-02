import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('광명',80.6,-9000),('김포',79.3,-7700),('고양',76.0,-7000),('용인',71.1,-5300),
   ('하남',70.3,-8800),('화성',67.3,-4500),('수원',65.7,-4000),('성남',64.3,-6000),
   ('부천',61.6,-2300),('안산',57.0,-1700),('평택',52.3,-500),('이천',43.7,400)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]; gap=[x[2] for x in d]
colors=[WARN if v>=70 else MID for v in vals]

fig, ax = plt.subplots(figsize=(10.2, 7.2))
fig.subplots_adjust(bottom=0.13, top=0.92, left=0.09, right=0.98)
y=np.arange(len(d))
ax.barh(y, vals, height=0.58, color=colors, zorder=3)
for i,(v,g) in enumerate(zip(vals,gap)):
    ax.text(v+1.2, i, f'{v}%', ha='left', va='center', fontsize=15,
            color=WARN if v>=70 else MID, fontproperties=F_B, zorder=5)
    s = ('+' if g>0 else '−')+f'{abs(g):,}만원'
    ax.text(116, i, s, ha='right', va='center', fontsize=13.5, color=SAND,
            fontproperties=F_R, zorder=5)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
ax.set_xlim(0, 118); ax.set_ylim(-0.85, len(d)+1.2); ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(0, len(d)+0.95, '낭만 부동산 분석 플랫폼 · 경기도 아파트', fontsize=13.5,
        color=MID, fontproperties=F_R, ha='left', va='center')
ax.text(0, len(d)+0.30, '같은 경기도인데 광명 80.6%, 이천 43.7%입니다', fontsize=21,
        color=NAVY, fontproperties=F_B, ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/loss/nangman_loss_fig2.png',
       '2021~2022년에 산 쌍의 손해 비율 · 오른쪽은 손해 본 쌍의 중간 손해액')
print('ok')

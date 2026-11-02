import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('3억 미만',43.4,400),('3~5억',69.6,-4300),('5~8억',79.7,-8500),
   ('8~12억',80.8,-11600),('12억 이상',70.1,-11000)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]; gap=[x[2] for x in d]
colors=[WARN if v>=75 else MID for v in vals]

fig, ax = plt.subplots(figsize=(10.2, 5.6))
fig.subplots_adjust(bottom=0.17, top=0.88, left=0.12, right=0.98)
y=np.arange(len(d))
ax.barh(y, vals, height=0.52, color=colors, zorder=3)
for i,(v,g) in enumerate(zip(vals,gap)):
    ax.text(v+1.2, i, f'{v}%', ha='left', va='center', fontsize=15,
            color=WARN if v>=75 else MID, fontproperties=F_B, zorder=5)
    s = ('+' if g>0 else '−')+f'{abs(g):,}만원'
    ax.text(118, i, s, ha='right', va='center', fontsize=13.5, color=SAND,
            fontproperties=F_R, zorder=5)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
ax.set_xlim(0, 120); ax.set_ylim(-0.8, len(d)+1.3); ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(0, len(d)+1.05, '낭만 부동산 분석 플랫폼 · 경기도 아파트', fontsize=13.5,
        color=MID, fontproperties=F_R, ha='left', va='center')
ax.text(0, len(d)+0.42, '비싼 집을 산 사람이 더 많이 잃었습니다', fontsize=21,
        color=NAVY, fontproperties=F_B, ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/loss/nangman_loss_fig3.png',
       '2021~2022년 매수 가격대별 손해 비율 · 오른쪽은 손해 본 쌍의 중간 손해액')
print('ok')

import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('2021년에 산 호실',10.3,13),('2023년에 산 호실',-13.0,30),
   ('2024년에 산 호실',-6.8,39),('2025년에 산 호실',-3.2,41)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]; n=[x[2] for x in d]
colors=[NAVY if v>0 else WARN for v in vals]

fig, ax = plt.subplots(figsize=(9.6, 5.6))
y=np.arange(len(d))
ax.barh(y, vals, height=0.56, color=colors, zorder=3)
ax.axvline(0, ymin=0.10, ymax=0.68, color=SAND, lw=2.2, zorder=4)
for i,(v,c) in enumerate(zip(vals,n)):
    off = 0.9 if v>0 else -0.9
    ax.text(v+off, i, ('+' if v>0 else '')+f'{v}%', ha='left' if v>0 else 'right',
            va='center', fontsize=16, color=NAVY if v>0 else WARN, fontproperties=F_B, zorder=5)
    ax.text(16.5, i, f'{c}짝', ha='left', va='center', fontsize=14, color=SAND,
            fontproperties=F_R, zorder=5)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
ax.set_xlim(-19, 24); ax.set_ylim(-0.8, len(d)+1.15); ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(-19, len(d)+0.95, '낭만 부동산 분석 플랫폼 · 동탄테크노밸리', fontsize=13.5,
        color=MID, fontproperties=F_R, ha='left', va='center')
ax.text(-19, len(d)+0.38, '영천동 지식산업센터, 언제 샀느냐로 나뉩니다', fontsize=20,
        color=NAVY, fontproperties=F_B, ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/hwaseong/nangman_hwaseong_fig2.png',
       '같은 건물 같은 전용면적끼리 짝지은 평당 가격 · 2026년 8월까지와 비교')
print('fig2 ok')

import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[(2014,71,55),(2015,191,64),(2016,62,82),(2017,71,63),(2018,279,88),(2019,1721,98),
   (2020,7,29),(2021,23,13),(2022,53,58),(2023,16,56),(2024,286,97),(2025,129,93),(2026,63,100)]
x=np.arange(len(d)); n=[a[1] for a in d]; r=[a[2] for a in d]
colors=[WARN if a[0]==2019 else MID for a in d]

fig, ax = plt.subplots(figsize=(10.4, 6.2))
fig.subplots_adjust(bottom=0.19, top=0.84, left=0.05, right=0.97)
ax.bar(x, n, width=0.6, color=colors, zorder=3)
for i,(y,c,rr) in enumerate(d):
    lab = f'{c:,}건' if c>=100 else f'{c}건'
    ax.text(i, c+38, lab, ha='center', va='bottom', fontsize=13,
            color=WARN if y==2019 else MID, fontproperties=F_B, zorder=5)
    ax.text(i, -95, f'{rr}%', ha='center', va='center', fontsize=12.5, color=SAND,
            fontproperties=F_R, zorder=5)
ax.set_xticks(x); ax.set_xticklabels([str(a[0]) for a in d], fontsize=13, fontproperties=F_R)
ax.set_ylim(-260, 2050); ax.set_xlim(-1.1, len(d)-0.3); ax.set_yticks([])
for s in ('top','right','left','bottom'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.axhline(0, color=LINE, lw=1.2, zorder=1)
fig.text(0.05, 0.945, '낭만 부동산 분석 플랫폼 · 성남 금토동', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.05, 0.885, '2019년 한 해에만 1,721건이 거래됐습니다', fontsize=21, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/land2/nangman_land2_fig3.png',
       '성남 금토동 개발제한구역 거래 건수 · 아래 숫자는 그중 지분 거래 비율')
print('ok')

import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

lab=['2018\n상','하','2019\n상','하','2020\n상','하','2021\n상','하','2022\n상','하',
     '2023\n상','하','2024\n상','하','2025\n상','하','2026\n상']
v=[1316,1119,1081,664,524,454,884,502,448,189,267,223,202,125,73,82,52]
x=np.arange(len(v))
colors=[MID if i<7 else (WARN if i<13 else '#8C4A38') for i in range(len(v))]

fig, ax = plt.subplots(figsize=(10.6, 6.2))
fig.subplots_adjust(bottom=0.20, top=0.80, left=0.05, right=0.97)
ax.bar(x, v, width=0.66, color=colors, zorder=3)
for i,c in enumerate(v):
    if True:
        ax.text(i, c+28, f'{c:,}', ha='center', va='bottom', fontsize=12,
                color=colors[i], fontproperties=F_B, zorder=5)
ax.axvline(6.5, ymin=0.06, ymax=0.70, color=SAND, lw=1.8, ls=(0,(5,3)), zorder=4)
ax.axvline(12.5, ymin=0.06, ymax=0.52, color=SAND, lw=1.8, ls=(0,(5,3)), zorder=4)
ax.text(6.65, 1290, '2021년 7월\n제한 지정', ha='left', va='top', fontsize=13.5,
        color=NAVY, fontproperties=F_B, zorder=5)
ax.text(12.65, 880, '2024년 6월\n2년 연장', ha='left', va='top', fontsize=13.5,
        color=NAVY, fontproperties=F_B, zorder=5)
ax.set_xticks(x); ax.set_xticklabels(lab, fontsize=11.5, fontproperties=F_R)
ax.set_ylim(0, 1500); ax.set_xlim(-0.9, len(v)-0.1); ax.set_yticks([])
for s in ('top','right','left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
fig.text(0.05,0.945,'낭만 부동산 분석 플랫폼 · 평택 안중역세권', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.05,0.880,'제한 지정 뒤 땅 거래가 줄었습니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/jehan/nangman_jehan_fig3.png',
       '제한지역 일곱 개 리의 반기별 토지 거래 건수 · 2026년은 상반기까지')
print('ok')

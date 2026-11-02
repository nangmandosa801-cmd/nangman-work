import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[(2015,22.9),(2016,28.1),(2017,34.8),(2018,29.6),(2019,13.1),(2020,9.2),
   (2021,61.3),(2022,77.6),(2023,34.6),(2024,38.1),(2025,30.6)]
x=np.arange(len(d)); v=[a[1] for a in d]
colors=[WARN if a[0] in (2021,2022) else (PALE if a[0] in (2019,2020) else MID) for a in d]

fig, ax = plt.subplots(figsize=(10.2, 6.1))
fig.subplots_adjust(bottom=0.20, top=0.95, left=0.04, right=0.98)
ax.bar(x, v, width=0.62, color=colors, zorder=3)
for i,(y,val) in enumerate(d):
    c = WARN if y in (2021,2022) else (MID if y not in (2019,2020) else NAVY)
    ax.text(i, val+2.2, f'{val}%', ha='center', va='bottom', fontsize=15,
            color=c, fontproperties=F_B, zorder=5)
ax.set_xticks(x); ax.set_xticklabels([str(a[0]) for a in d], fontsize=14, fontproperties=F_R)
ax.set_ylim(0, 108); ax.set_xlim(-0.85, len(d)-0.15); ax.set_yticks([])
for s in ('top','right','left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
ax.tick_params(length=0)
ax.text(-0.85, 103, '낭만 부동산 분석 플랫폼 · 경기도 아파트', fontsize=13.5,
        color=MID, fontproperties=F_R, ha='left', va='center')
ax.text(-0.85, 95, '산 해가 1년 다르면 결과가 달랐습니다', fontsize=21,
        color=NAVY, fontproperties=F_B, ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/loss/nangman_loss_fig1.png',
       '같은 집이 두 번 팔린 109만 4,695쌍 · 매수 연도별로 손해 보고 판 비율')
print('ok')

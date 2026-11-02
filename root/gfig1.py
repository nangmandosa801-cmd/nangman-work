import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

yrs=list(range(2010,2027))
gb=[5.9,15.4,31.9,35.7,48.2,50.3,63.3,66.0,72.6,79.2,68.9,47.2,52.9,59.0,69.2,61.3,66.8]
al=[24.5,25.5,29.4,31.7,37.8,38.1,41.9,45.5,49.7,53.2,47.5,43.6,44.1,48.6,47.5,48.4,51.4]

fig, ax = plt.subplots(figsize=(10.4, 6.2))
fig.subplots_adjust(bottom=0.19, top=0.84, left=0.06, right=0.97)
ax.plot(yrs, gb, color=WARN, lw=3.0, marker='o', ms=6, zorder=4)
ax.plot(yrs, al, color=PALE, lw=2.4, marker='o', ms=5, zorder=3)
ax.text(2010.18, 0.8, '5.9%', fontsize=15, color=WARN, fontproperties=F_B, ha='left', va='center')
ax.text(2019, gb[9]+6, '79.2%', fontsize=15, color=WARN, fontproperties=F_B, ha='center', va='center')
ax.text(2021, gb[11]-7, '47.2%', fontsize=15, color=WARN, fontproperties=F_B, ha='center', va='center')
ax.text(2026.15, gb[-1], '66.8%', fontsize=15, color=WARN, fontproperties=F_B, ha='left', va='center')
ax.text(2023.4, 33.5, '경기 토지 전체', fontsize=14.5, color=MID, fontproperties=F_R, ha='center', va='center')
ax.text(2014.6, 66, '개발제한구역', fontsize=15, color=WARN, fontproperties=F_B, ha='center', va='center')
ax.set_xticks([2010,2013,2016,2019,2022,2025])
ax.set_xticklabels(['2010','2013','2016','2019','2022','2025'], fontsize=14, fontproperties=F_R)
ax.set_yticks([0,20,40,60,80]); ax.set_yticklabels(['0','20','40','60','80%'], fontsize=13, fontproperties=F_R, color=SAND)
ax.set_ylim(-3, 92); ax.set_xlim(2009.2, 2027.6)
for s in ('top','right','left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
ax.grid(axis='y', color=LINE, lw=0.8, zorder=0)
fig.text(0.06, 0.945, '낭만 부동산 분석 플랫폼 · 경기 토지', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.06, 0.885, '그린벨트 지분 거래는 15년 만에 열 배가 됐습니다', fontsize=21, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/land2/nangman_land2_fig1.png',
       '경기도 토지 실거래 213만 건 · 계약 연도별 지분 거래 비율 · 2026년은 8월까지')
print('ok')

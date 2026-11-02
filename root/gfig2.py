import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('성남',85,150),('광명',83,148),('과천',83,20),('수원',82,49),('하남',79,136),
   ('부천',78,113),('화성',71,67),('의왕',68,87),('의정부',61,115),('남양주',59,97),
   ('고양',55,130),('김포',53,105),('안산',48,83),('시흥',48,83),('양주',41,56),('광주',39,38)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]; pp=[x[2] for x in d]
colors=[WARN if v>=75 else MID for v in vals]

fig, ax = plt.subplots(figsize=(10.2, 8.4))
fig.subplots_adjust(bottom=0.11, top=0.93, left=0.09, right=0.98)
y=np.arange(len(d))
ax.barh(y, vals, height=0.6, color=colors, zorder=3)
for i,(v,p) in enumerate(zip(vals,pp)):
    ax.text(v+1.2, i, f'{v}%', ha='left', va='center', fontsize=15,
            color=WARN if v>=75 else MID, fontproperties=F_B, zorder=5)
    ax.text(120, i, f'평당 {p}만원', ha='right', va='center', fontsize=13.5, color=SAND,
            fontproperties=F_R, zorder=5)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
ax.set_xlim(0, 122); ax.set_ylim(-0.85, len(d)+1.95); ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(0, len(d)+1.52, '낭만 부동산 분석 플랫폼 · 경기 그린벨트', fontsize=13.5,
        color=MID, fontproperties=F_R, ha='left', va='center')
ax.text(0, len(d)+0.80, '서울에 붙은 도시가 위에 있습니다', fontsize=21,
        color=NAVY, fontproperties=F_B, ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/land2/nangman_land2_fig2.png',
       '개발제한구역 토지 거래 1만 4,778건 · 2024년 1월~2026년 8월 · 거래 200건 이상 시군')
print('ok')

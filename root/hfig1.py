import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('우정·장안',119.9,1.2),('남양',105.8,53.2),('병점·진안',101.0,23.7),('봉담',99.4,53.1),
   ('향남',96.9,0.0),('동탄1',95.5,7.3),('송산·새솔',93.0,80.4),('동탄2',91.5,98.5)][::-1]
names=[x[0] for x in d]; vals=[x[1] for x in d]; new=[x[2] for x in d]
colors=[WARN if n=='동탄2' else (NAVY if v>=100 else MID) for n,v in zip(names,vals)]

fig, ax = plt.subplots(figsize=(9.6, 6.6))
y=np.arange(len(d))
ax.barh(y, vals, height=0.60, color=colors, zorder=3)
ax.axvline(100, ymin=0.07, ymax=0.82, color=SAND, lw=2, ls=(0,(4,3)), zorder=4)
for i,(v,nv) in enumerate(zip(vals,new)):
    ax.text(v-2.0, i, f'{v}%', ha='right', va='center', fontsize=15, color='white',
            fontproperties=F_B, zorder=5)
    ax.text(124, i, f'신축 {nv:.1f}%', ha='left', va='center', fontsize=14,
            color=NAVY if nv<30 else SAND, fontproperties=F_B if nv<30 else F_R, zorder=5)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
for t,n in zip(ax.get_yticklabels(), names):
    if n in ('동탄2','우정·장안'): t.set_fontproperties(F_B)
ax.set_xlim(0,160); ax.set_ylim(-0.8, len(d)+0.95); ax.set_xticks([])
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(0, len(d)+0.78, '낭만 부동산 분석 플랫폼 · 화성', fontsize=13.5, color=MID,
        fontproperties=F_R, ha='left', va='center')
ax.text(0, len(d)+0.22, '신축이 많은 권역일수록 덜 회복했습니다', fontsize=20, color=NAVY,
        fontproperties=F_B, ha='left', va='center')
ax.text(100, -0.62, '2021년 고점', ha='center', va='center', fontsize=13.5,
        color=SAND, fontproperties=F_R)
finish(fig, '/mnt/user-data/outputs/재배치/nangman/hwaseong/nangman_hwaseong_fig1.png',
       '같은 단지 같은 평형 700짝 · 신축은 2025년 이후 거래 중 2015년 이후 준공 비중')
print('fig1 ok')

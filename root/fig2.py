import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d = [('광적면',112.8),('장흥면',105.4),('백석읍',103.0),('광사동',88.8),('덕계동',86.6),
     ('고읍동',85.0),('삼숭동',80.8),('옥정동',75.9),('고암동',74.0),('덕정동',71.1)]
d = d[::-1]
names = [x[0] for x in d]; vals = [x[1] for x in d]
colors = [WARN if n=='덕정동' else (NAVY if n=='옥정동' else MID) for n,v in d]

fig, ax = plt.subplots(figsize=(9.2, 6.4))
y = np.arange(len(d))
ax.barh(y, vals, height=0.62, color=colors, zorder=3)
ax.axvline(100, color=SAND, lw=2, ls=(0,(4,3)), zorder=4)
ax.text(100, len(d)-0.30, '2021년 고점', ha='center', va='bottom',
        fontsize=14, color=SAND, fontproperties=F_B)

for i,(n,v) in enumerate(d):
    ax.text(v-2.5, i, f'{v:.1f}%', ha='right', va='center', fontsize=15,
            color='white', fontproperties=F_B, zorder=5)

ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=16, fontproperties=F_R)
for t,(n,v) in zip(ax.get_yticklabels(), d):
    if n=='옥정동': t.set_fontproperties(F_B); t.set_color(NAVY)
    if n=='덕정동': t.set_fontproperties(F_B); t.set_color(WARN)
ax.set_xlim(0, 118); ax.set_ylim(-0.7, len(d)+0.55)
ax.set_xticks([]); 
for s in ('top','right','bottom','left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
finish(fig, '/mnt/user-data/outputs/재배치/nangman/yangju2/nangman_yangju2_fig2.png',
       '같은 단지 같은 평형 182짝 · 2021년을 100으로 둔 최근 2년 가격')
print('fig2 ok')

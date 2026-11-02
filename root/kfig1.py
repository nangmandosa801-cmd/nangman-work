import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish

fig, ax = plt.subplots(figsize=(10.6, 6.4))
fig.subplots_adjust(bottom=0.14, top=0.82, left=0.04, right=0.97)
rows=[('건축물 용도','지식산업센터 지원시설','업무시설'),
      ('주택 수','안 들어갑니다','주거용이면 들어갑니다'),
      ('살 수 있는 사람','제한이 있었습니다','제한 없음'),
      ('같은 크기 값','더 쌉니다','더 비쌉니다')]
LX, RX = 1.75, 6.35; W = 3.95
ax.add_patch(mp.Rectangle((LX,0.55),W,0.78, color=DEEP, zorder=3))
ax.add_patch(mp.Rectangle((RX,0.55),W,0.78, color=CYAN, zorder=3))
ax.text(LX+W/2,0.94,'지산 기숙사', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=FB, zorder=5)
ax.text(RX+W/2,0.94,'오피스텔', ha='center', va='center', fontsize=19,
        color='#FFFFFF', fontproperties=FB, zorder=5)
for i,(k,a,b) in enumerate(rows):
    y = -0.4 - i*1.05
    ax.text(1.55,y,k, ha='right', va='center', fontsize=15, color=GREY, fontproperties=FR, zorder=5)
    ax.text(LX+W/2,y,a, ha='center', va='center', fontsize=17, color=DEEP, fontproperties=FB, zorder=5)
    ax.text(RX+W/2,y,b, ha='center', va='center', fontsize=17, color=DEEP, fontproperties=FB, zorder=5)
    ax.plot([LX,RX+W],[y-0.46,y-0.46], color=LINE, lw=1.0, zorder=1)
ax.text((LX+RX+W)/2,-4.28,'살 수 있는 사람이 좁으면 값이 눌립니다',
        ha='center', va='center', fontsize=16.5, color=CYAN, fontproperties=FB, zorder=5)
ax.set_xlim(-0.2,10.6); ax.set_ylim(-4.9,1.58); ax.set_axis_off()
fig.text(0.04,0.955,'지산드림 · 구리 갈매', fontsize=13.5, color=CYAN, ha='left', va='center')
fig.text(0.04,0.892,'기숙사는 오피스텔이 아닙니다', fontsize=22, color=DEEP, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/jisandream/gisuksa/jisandream_gisuksa_fig1.png',
       '건축물대장 용도 기준 · 주택 수 포함 여부는 실제 사용 형태에 따라 달라질 수 있습니다', brand='지산드림')
print('ok')

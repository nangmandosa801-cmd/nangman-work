import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

d=[('도로','도로서비스 수준이 매우 낮은 곳','교통영향평가의 예',SAND),
   ('도로','도로율이 용도지역별 기준에 미달','20% 이상 미달',WARN),
   ('수도','수요량이 시설용량을 넘을 곳','향후 2년 이내',MID),
   ('하수','발생량이 시설용량을 넘을 곳','향후 2년 이내',MID),
   ('학교','학생수가 수용능력을 넘을 곳','2년 · 20% 이상 초과',WARN)][::-1]

fig, ax = plt.subplots(figsize=(10.6, 6.2))
fig.subplots_adjust(bottom=0.14, top=0.82, left=0.04, right=0.97)
for i,(cat,lab,num,col) in enumerate(d):
    ax.add_patch(mp.Rectangle((0,i-0.28),1.25,0.56, color=col, zorder=3))
    ax.text(0.62,i,cat, ha='center', va='center', fontsize=18, color='#FFFFFF',
            fontproperties=F_B, zorder=5)
    ax.text(1.55,i,lab, ha='left', va='center', fontsize=17, color=NAVY,
            fontproperties=F_R, zorder=5)
    ax.text(9.9,i,num, ha='right', va='center', fontsize=16, color=col,
            fontproperties=F_B, zorder=5)
ax.set_xlim(-0.25,10.1); ax.set_ylim(-0.9,len(d)+0.3); ax.set_axis_off()
fig.text(0.04,0.955,'낭만 부동산 분석 플랫폼 · 부동산 공법', fontsize=13.5, color=MID, ha='left', va='center')
fig.text(0.04,0.892,'하나만 해당해도 지정할 수 있습니다', fontsize=22, color=NAVY, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/miltdo/nangman_miltdo_fig2.png',
       '같은 법 시행령 제62조 제2항 제1호 · 도로는 미달, 학생은 초과입니다')
print('ok')

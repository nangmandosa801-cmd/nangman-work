import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
WARN='#8A5548'

d=[('지원시설 이용자','입주업체 근로자로 한정하지 않음','갈매동 해당',True),
   ('입주 업종','열거식에서 네거티브로','갈매동 해당',True),
   ('편의시설 비중','2년 한시로 확대','갈매동 해당',True),
   ('공공임대 매입','수도권은 LH가 사들임','구리시 대상지역',True),
   ('오피스텔 전환','일반공업지역만 한시 허용','갈매동 아님',False)][::-1]

fig, ax = plt.subplots(figsize=(10.6, 6.2))
fig.subplots_adjust(bottom=0.14, top=0.82, left=0.04, right=0.97)
for i,(cat,lab,tag,ok) in enumerate(d):
    col = CYAN if ok else WARN
    ax.add_patch(mp.Rectangle((0,i-0.30),2.55,0.60, color=col, zorder=3))
    ax.text(1.27,i,cat, ha='center', va='center', fontsize=16, color='#FFFFFF',
            fontproperties=FB, zorder=5)
    ax.text(2.85,i,lab, ha='left', va='center', fontsize=16.5, color=DEEP,
            fontproperties=FR, zorder=5)
    ax.text(10.35,i,tag, ha='right', va='center', fontsize=15, color=col,
            fontproperties=FB, zorder=5)
ax.set_xlim(-0.25,10.55); ax.set_ylim(-0.95,len(d)+0.3); ax.set_axis_off()
fig.text(0.04,0.955,'지산드림 · 지식산업센터 대책', fontsize=13.5, color=CYAN, ha='left', va='center')
fig.text(0.04,0.892,'무엇이 풀리고 무엇이 안 풀리나', fontsize=22, color=DEEP, fontweight='bold', ha='left', va='center')
finish(fig, '/mnt/user-data/outputs/재배치/jisandream/gisuksa/jisandream_gisuksa_fig2.png',
       '산업통상자원부 2026년 9월 10일 발표 · 세부 기준은 법령 개정으로 정해집니다', brand='지산드림')
print('ok')

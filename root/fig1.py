import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, LINE, WARN, PALE, F_B, F_R
from note import finish

fig, ax = plt.subplots(figsize=(9.6, 6.2))

def 역(x, y, name, 신설=False, 끝=False, dy=-0.30, fs=15):
    ax.plot([x],[y],'o', ms=19 if 신설 else 14,
            mfc='#FFF3C4' if 신설 else 'white',
            mec=WARN if 신설 else MID, mew=3.4, zorder=5, clip_on=False)
    ax.text(x, y+dy, name, ha='center', va='top' if dy<0 else 'bottom',
            fontsize=fs, color=NAVY if 신설 else '#333',
            fontproperties=F_B if (신설 or 끝) else F_R, zorder=6)

# 1호선
y1 = 3.15
ax.plot([0.4, 5.6], [y1, y1], color=MID, lw=5, solid_capstyle='round', zorder=2)
for x, n, s in [(0.9,'덕정',False), (2.3,'회천중앙',True), (3.7,'덕계',False), (5.1,'양주',False)]:
    역(x, y1, n, 신설=s)
ax.text(0.15, y1+0.42, '1호선', fontsize=16, color=MID, fontproperties=F_B, ha='left')
ax.text(3.7, y1+0.40, '회천중앙역 2026년 7월 착공 · 2030년 개통 목표', ha='center', fontsize=13,
        color=WARN, fontproperties=F_B)

# GTX-C
y2 = 1.95
ax.plot([0.9, 8.2], [y2, y2], color=NAVY, lw=6, solid_capstyle='round', zorder=2)
역(0.9, y2, '덕정')
역(8.2, y2, '삼성', 끝=True)
ax.text(4.5, y2+0.26, '80분  →  30분대', ha='center', fontsize=15,
        color=NAVY, fontproperties=F_B)
ax.text(0.15, y2+0.42, 'GTX-C', fontsize=16, color=NAVY, fontproperties=F_B, ha='left')
ax.text(4.5, y2-0.42, '2026년 9월 본공사 · 2031년 9월 개통 목표', ha='center',
        fontsize=13, color=SAND, fontproperties=F_R)
ax.plot([0.9,0.9],[y1,y2], color=LINE, lw=2.2, ls=(0,(3,3)), zorder=1)

# 7호선
y3 = 0.55
ax.plot([0.4, 5.6], [y3, y3], color=MID, lw=5, solid_capstyle='round', zorder=2)
ax.plot([5.6, 7.9], [y3, y3], color=PALE, lw=5, solid_capstyle='round', zorder=2)
for x, n in [(0.8,'도봉산'), (1.9,'장암'), (3.0,'탑석'), (4.3,'고읍')]:
    역(x, y3, n)
역(5.6, y3, '옥정')
역(7.9, y3, '포천', 끝=True)
ax.text(0.15, y3+0.44, '7호선', fontsize=16, color=MID, fontproperties=F_B, ha='left')
ax.text(3.0, y3-0.70, '도봉산~옥정 · 공정률 62% · 2029년 말', ha='center',
        fontsize=13, color=SAND, fontproperties=F_R)
ax.text(6.75, y3-0.70, '옥정~포천 · 공정률 5% · 2031년', ha='center',
        fontsize=13, color=SAND, fontproperties=F_R)

ax.set_xlim(-0.25, 8.95); ax.set_ylim(-0.55, 4.05)
ax.axis('off')
finish(fig, '/mnt/user-data/outputs/재배치/nangman/yangju2/nangman_yangju2_fig1.png',
       '철도 넷이 모두 착공 단계 · 개통은 2029년에서 2031년 사이')
print('fig1 ok')

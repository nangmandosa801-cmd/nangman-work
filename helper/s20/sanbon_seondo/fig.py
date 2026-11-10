import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
P='nangman_sanbon_seondo_'

# 그림 1: 2026년 월별 매매 건수
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
A11=[28,21,13,10,15,29,15,13,17,6]
A92=[24,3,5,7,11,11,13,10,13,8]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'산본 재건축 선도지구 월별 매매 건수 · 2026년',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'LH 시행자 지정 뒤에도 매달 거래가 이어졌다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(M)); w=0.38
ax.bar(x-w/2,A11,w,color=NAVY,label='11구역 (백합 · 삼성장미 · 주공11)'); ax.bar(x+w/2,A92,w,color=GRAY,label='9-2구역 (한양 · 동성 · 극동 백두)')
for i,(a,b) in enumerate(zip(A11,A92)):
    ax.text(i-w/2,a+0.4,str(a),ha='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(i+w/2,b+0.4,str(b),ha='center',fontsize=13.5,color='#555')
ax.axvline(2.5,color=BLUE,lw=2,ls='--'); ax.text(2.6,33.5,'3월 20 · 27일\nLH 사업시행자 지정',fontsize=13.5,color=BLUE,va='top')
ax.set_xticks(x); ax.set_xticklabels(M,fontsize=15,color='#333'); ax.set_ylim(0,35); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(모든 크기 · 해제 거래 뺌) · 10월은 신고 기한이 남아 더 늘 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{P}1_count.png'); plt.close()

# 그림 2: 3.3㎡당 매매 중앙값 2025년 vs 2026년 1~10월
G=['11구역','9-2구역','선도지구 밖\n산본동 구축']
Y25=[2575,2057,2139]; Y26=[2802,2281,2272]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'산본 재건축 선도지구 3.3㎡당 매매 중앙값 · 2025년과 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'선도지구 9~11% · 밖 구축 6% 올랐다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(G)); w=0.34
ax.bar(x-w/2,Y25,w,color=GRAY,label='2025년'); ax.bar(x+w/2,Y26,w,color=[NAVY,NAVY,BLUE],label='2026년 1~10월')
for i,(a,b) in enumerate(zip(Y25,Y26)):
    ax.text(i-w/2,a+40,f'{a:,}',ha='center',fontsize=15,color='#555')
    ax.text(i+w/2,b+40,f'{b:,}',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i+w/2,b+220,f'+{(b/a-1)*100:.0f}%',ha='center',fontsize=15,color=BLUE)
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=16,color='#333')
ax.set_ylim(0,3400); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(군포시 산본동 · 모든 크기 · 전용면적 기준 3.3㎡당 · 해제 거래 뺌) · 밖 구축은 1997년 이전 준공 · 단위 만원',fontsize=12,color='#8A8578')
fig.savefig(f'img/{P}2_price.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 산본 · 1기 신도시 재건축',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'산본 선도지구',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'LH 시행자 지정 뒤',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'거래 181건',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'9-2구역 · 11구역 · 2026년 3월~10월',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{P}thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_sanbon_seondo_1_count_v2.png', 'LH 시행자 지정 뒤에도 매달 거래가 이어졌다', [('1월', 52, '52건', False), ('3월|LH 시행자 지정', 18, '18건', False), ('6월', 40, '40건', True), ('9월', 30, '30건', False), ('10월|신고 기한 남음', 14, '14건', False)], note='산본 선도지구 11구역 + 9-2구역 매매 건수 · 2026년')
bars('img/nangman_sanbon_seondo_2_price_v2.png', '선도지구 9~11% · 밖 구축 6% 올랐다', [('11구역|2025년', 2575.0, '2,575만', False), ('11구역|2026년 1~10월', 2802.0, '2,802만', True), ('선도지구 밖 산본동 구축|2025년', 2139.0, '2,139만', False), ('선도지구 밖 산본동 구축|2026년 1~10월', 2272.0, '2,272만', False)], note='산본 재건축 선도지구 3.3㎡당 매매 중앙값 · 2025년과 2026년 1~10월')
print('v2 ok')

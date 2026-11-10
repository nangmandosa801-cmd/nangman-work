import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 그림 1: 3.3㎡당 매매 중앙값 2025년 vs 2026년 1~10월
G=['꿈마을\n귀인블록','꿈마을\n민백블록','샘마을','선도지구 밖\n동안구 구축']
Y25=[4347,3812,3166,3360]; Y26=[4790,4404,3559,4052]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평촌 재건축 선도지구 3.3㎡당 매매 중앙값 · 2025년과 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'선도지구 10~16% · 밖 구축 21% 올랐다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(G)); w=0.36
ax.bar(x-w/2,Y25,w,color=GRAY,label='2025년'); ax.bar(x+w/2,Y26,w,color=[NAVY,NAVY,NAVY,BLUE],label='2026년 1~10월')
for i,(a,b) in enumerate(zip(Y25,Y26)):
    ax.text(i-w/2,a+60,f'{a:,}',ha='center',fontsize=14,color='#555')
    ax.text(i+w/2,b+60,f'{b:,}',ha='center',fontsize=15.5,color=NAVY,fontweight='bold')
    ax.text(i+w/2,b+330,f'+{(b/a-1)*100:.0f}%',ha='center',fontsize=14,color=BLUE)
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=15,color='#333')
ax.set_ylim(0,6000); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(모든 크기 · 전용면적 기준 3.3㎡당 · 해제 거래 뺌 · 2026년은 10월 신고분까지) · 단위 만원',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_pyeongchon_seondo_1_price.png'); plt.close()

# 그림 2: 2026년 월별 매매 건수
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
KM=[12,10,17,0,3,1,2,5,1,1]
SM=[12,17,16,19,21,8,25,12,4,2]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평촌 재건축 선도지구 월별 매매 건수 · 2026년',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'꿈마을 1~3월 39건 → 시행자 고시 뒤 13건',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
x=np.arange(len(M)); w=0.38
ax.bar(x-w/2,KM,w,color=NAVY,label='꿈마을 (귀인 · 민백블록)'); ax.bar(x+w/2,SM,w,color=GRAY,label='샘마을')
for i,(a,b) in enumerate(zip(KM,SM)):
    ax.text(i-w/2,a+0.4,str(a),ha='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(i+w/2,b+0.4,str(b),ha='center',fontsize=13.5,color='#555')
ax.axvline(3.5,color=BLUE,lw=2,ls='--'); ax.text(3.6,29.5,'4월 27일\n꿈마을 사업시행자 고시',fontsize=13,color=BLUE,va='top')
ax.axvline(8.5,color=BLUE,lw=2,ls='--'); ax.text(8.4,29.5,'9월 18일\n샘마을\n구역 고시',fontsize=13,color=BLUE,va='top',ha='right')
ax.set_xticks(x); ax.set_xticklabels(M,fontsize=15,color='#333'); ax.set_ylim(0,31); ax.set_yticks([])
for k in ['top','right','left']: ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(모든 크기 · 해제 거래 뺌) · 10월은 신고 기한이 남아 더 늘 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_pyeongchon_seondo_2_count.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평촌 · 1기 신도시 재건축',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'평촌 선도지구',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'시행자 고시 뒤 꿈마을',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'거래 13건',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'귀인 · 민백블록 · 2026년 4월 27일~10월',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_pyeongchon_seondo_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_pyeongchon_seondo_1_price_v2.png', '선도지구 10~16% · 밖 구축 21% 올랐다', [('꿈마을 귀인블록|2025년', 4347.0, '4,347만', False), ('꿈마을 귀인블록|2026년 1~10월', 4790.0, '4,790만', False), ('선도지구 밖 동안구 구축|2025년', 3360.0, '3,360만', False), ('선도지구 밖 동안구 구축|2026년 1~10월', 4052.0, '4,052만', True)], note='평촌 재건축 선도지구 3.3㎡당 매매 중앙값 · 2025년과 2026년 1~10월')
bars('img/nangman_pyeongchon_seondo_2_count_v2.png', '꿈마을 1~3월 39건 → 시행자 고시 뒤 13건', [('꿈마을 1~3월', 39, '39건', False), ('꿈마을 5~10월|시행자 고시 뒤', 13, '13건', True)], note='평촌 선도지구 꿈마을(귀인 · 민백블록) 매매 건수 · 2026년')
print('v2 ok')

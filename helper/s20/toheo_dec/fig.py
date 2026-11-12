import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
ms=['25.1','2','3','4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8','9']
a12=[534,946,1454,1028,1481,2136,701,869,1819,1610,532,1085,1098,1116,985,1463,1403,1082,1219,760,598]
oth=[1414,2000,2719,2356,2447,3192,1883,1760,2105,2548,2788,2465,2966,2319,3249,3061,3204,3357,3375,2826,2709]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'토지거래허가구역 해제 경기도 · 84㎡ 아파트 한 달 거래',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'묶인 12곳 9월 거래 598건, 1년 전 1,819건의 3분의 1',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.15,0.9,0.6]); x=range(len(ms))
ax.plot(x,oth,color=GRAY,lw=3,marker='o',ms=5); ax.plot(x,a12,color=NAVY,lw=3.5,marker='o',ms=6)
ax.axvline(9.6,color=BLUE,ls='--',lw=1.5); ax.text(9.7,3550,'2025년 10월 20일\n허가구역 지정',color=BLUE,fontsize=13,va='top')
ax.text(20,a12[-1]-260,'598건',ha='center',color=NAVY,fontsize=16,fontweight='bold')
ax.text(8,a12[8]+130,'1,819건',ha='center',color=NAVY,fontsize=16,fontweight='bold')
ax.text(20,oth[-1]+180,'2,709건',ha='center',color='#6B7685',fontsize=15,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(ms,fontsize=12.5,color='#333'); ax.set_ylim(0,3700); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.07,0.79,'■ 묶인 경기 12곳',color=NAVY,fontsize=15,fontweight='bold'); fig.text(0.27,0.79,'■ 안 묶인 경기 나머지 (구리 · 동탄 · 기흥 뺌)',color='#6B7685',fontsize=15,fontweight='bold')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 · 전용 83~86㎡ · 해제 거래 뺌 · 2025년 1월~2026년 9월 계약',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_toheo_dec_1_count.png'); plt.close()

rg=['분당','수정','하남','동안','광명','과천','수지','의왕','영통','중원','팔달','장안']
c25=[213,78,259,199,184,26,367,108,202,58,54,71]; c26=[33,16,57,48,48,7,100,46,101,30,44,68]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'경기도 토지거래허가구역 12곳 · 84㎡ 9월 거래 건수',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'분당은 213건에서 33건, 수원 장안은 71건에서 68건',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.15,0.9,0.6]); x=range(len(rg)); w=0.38
ax.bar([i-w/2-0.01 for i in x],c25,w,color=GRAY); ax.bar([i+w/2+0.01 for i in x],c26,w,color=NAVY)
for i in x:
    ax.text(i-w/2-0.01,c25[i]+6,str(c25[i]),ha='center',fontsize=12.5,color='#6B7685')
    ax.text(i+w/2+0.01,c26[i]+6,str(c26[i]),ha='center',fontsize=12.5,color=NAVY,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(rg,fontsize=15,color='#333'); ax.set_ylim(0,400); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.07,0.79,'■ 2025년 9월 (지정 직전)',color='#6B7685',fontsize=15,fontweight='bold'); fig.text(0.33,0.79,'■ 2026년 9월 (만료 석 달 앞)',color=NAVY,fontsize=15,fontweight='bold')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 · 전용 83~86㎡ · 해제 거래 뺌 · 남은 비율이 낮은 순서',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_toheo_dec_2_region.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 토지거래허가구역 해제 경기도',font=kr(san,30),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'12월 31일 만료 경기 12곳',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'84㎡ 9월 거래',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'1,819 → 598건',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,718),'같은 단지 값은 1년 새 21% 올랐습니다',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_toheo_dec_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_toheo_dec_1_count_v2.png', '묶인 12곳 9월 거래 598건, 1년 전 1,819건의 3분의 1', [('2025년 9월|지정 직전', 1819, '1,819건', False), ('2026년 9월|만료 석 달 앞', 598, '598건', True)], note='경기 토지거래허가구역 12곳 · 84㎡ 한 달 거래')
bars('img/nangman_toheo_dec_2_region_v2.png', '분당은 213건에서 33건, 수원 장안은 71건에서 68건', [('분당|2025년 9월', 213.0, '213건', False), ('분당|2026년 9월', 33.0, '33건', True), ('수원 장안|2025년 9월', 71.0, '71건', False), ('수원 장안|2026년 9월', 68.0, '68건', False)], note='경기도 토지거래허가구역 12곳 · 84㎡ 9월 거래 건수')
print('v2 ok')

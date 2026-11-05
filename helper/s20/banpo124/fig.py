import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
ms=['1월','2월','3월','4월','5월','6월','7월','8월','9월']
v=[12,7,13,33,52,18,10,7,11]; wb=[1,0,0,5,11,1,0,0,0]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'디에이치 반포124 청약일정 앞 · 반포동 · 잠원동 84㎡ 아파트 매매',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'5월 52건이던 거래가 9월 11건',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.15,0.9,0.6]); x=range(len(ms))
cols=[GRAY if i<6 else NAVY for i in x]
ax.bar(x,v,0.6,color=cols)
ax.bar(x,wb,0.6,color=BLUE,hatch='//',edgecolor='white')
for i in x: ax.text(i,v[i]+1,f'{v[i]}건',ha='center',fontsize=16,color=NAVY if i>=6 else '#6B7685',fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(ms,fontsize=15,color='#333'); ax.set_ylim(0,60); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.07,0.79,'■ 84㎡ 전체 거래',color=GRAY,fontsize=15,fontweight='bold'); fig.text(0.25,0.79,'▨ 그중 래미안원베일리 (7월부터 0건)',color=BLUE,fontsize=15,fontweight='bold')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 · 2026년 계약 · 서초구 반포동 · 잠원동 · 전용 83~86㎡ · 해제 · 직거래 뺌',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_banpo124_1_count.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 디에이치 반포124 청약일정',font=kr(san,30),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'디에이치 반포124',font=kr(ser,66),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'일반공급 1순위',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'12월 8일',font=kr(ser,120),fill='#D4B04C',anchor='mm')
d.text((W/2,718),'특별공급 12월 7일 · 당첨 발표 12월 16일',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_banpo124_thumb.png')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_cheolsan12vs13_'
M=['25.1','2','3','4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8','9','10']
V13=[4,5,15,14,22,17,6,7,8,10,2,8,14,6,20,6,0,3,7,1,2,0]
V12=[3,7,15,10,13,10,5,6,11,8,1,11,11,14,17,14,11,4,2,2,1,0]
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'철산주공 12단지 · 13단지 · 달마다 신고된 매매 건수(모든 면적)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'13단지는 4월 29일 인가 뒤 13건, 12단지는 9월 4일 인가 전에 이미 6~9월 9건',fontsize=23,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.14,0.9,0.62])
w=0.4; x=range(len(M))
ax.bar([i-w/2 for i in x],V13,w,color=NAVY,label='13단지 (2,460가구)')
ax.bar([i+w/2 for i in x],V12,w,color=GRAY,label='12단지 (1,800가구)')
for i,v in enumerate(V13):
    if v: ax.text(i-w/2,v+0.3,str(v),ha='center',fontsize=10,color=NAVY,fontweight='bold')
for i,v in enumerate(V12):
    if v: ax.text(i+w/2,v+0.3,str(v),ha='center',fontsize=10,color='#555')
ax.set_xticks(list(x)); ax.set_xticklabels(M,fontsize=11,color='#555')
ax.set_yticks([]); ax.set_ylim(0,26)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axvline(15.5,color=NAVY,lw=1.2,ls='--'); ax.text(15.6,24.2,'13단지 인가 4월 29일',fontsize=12,color=NAVY)
ax.axvline(19.5,color='#7A8590',lw=1.2,ls='--'); ax.text(19.6,21.5,'12단지 인가\n9월 4일',fontsize=12,color='#7A8590')
ax.legend(loc='upper left',fontsize=12,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(광명시 철산동 주공12 · 주공13 · 해제 거래 뺌 · 2026년 9~10월은 신고 기간이 남아 덜 들어옴)',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'1_count.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축 따라가기 4화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,350),'철산주공 12단지 재건축',font=kr(ser,78),fill='#F4F1EA',anchor='mm')
d.text((W/2,465),'13단지와 84㎡ 중앙값 차이',font=kr(ser,52),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'1,000만 → 6,750만',font=kr(ser,88),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2025년 → 2026년 · 조합설립인가 다섯 달 차이',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')

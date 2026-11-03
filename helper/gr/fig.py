import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S=[('발표 · 주민공람','2018.12.19','이날이 기준일',NAVY),('지구지정 고시','2019.10.15','영업보상 기준',BLUE),('보상계획 공고','2021.2.5','조서 열람 · 이의',GRAY),('협의 · 수용재결','2021~','계약 · 재결',GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'주민공람 공고일 · 하남 교산이 실제로 지난 순서',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'공람일에서 보상계획 공고까지 2년 2개월',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.04,0.12,0.92,0.66]); ax.set_xlim(0,4); ax.set_ylim(0,1); ax.axis('off')
ax.plot([0.5,3.5],[0.55,0.55],color='#D5DCE6',lw=6,zorder=1)
for i,(a,d,b,c) in enumerate(S):
    x=0.5+i
    ax.scatter([x],[0.55],s=900,color=c,zorder=2)
    ax.text(x,0.55,str(i+1),ha='center',va='center',fontsize=18,color='white',fontweight='bold',zorder=3)
    ax.text(x,0.80,a,ha='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(x,0.70,d,ha='center',fontsize=16,color=c if c!=GRAY else '#555')
    ax.text(x,0.33,b,ha='center',fontsize=15,color='#333')
ax.text(0.5,0.12,'이 뒤 지은 집 · 심은 나무 · 차린 가게는\n허가 없으면 보상에서 빠짐',ha='center',fontsize=13.5,color=NAVY)
fig.text(0.045,0.03,'LH 하남교산 공공주택지구 대토보상계획 추가공고(2021.6) · 국토교통부 고시 제2019-558호',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_gongram_1_steps.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 신규택지 · 토지보상',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'주민공람 공고일',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'이날 뒤에 생긴 것은',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'보상에서 빠집니다',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'하남감일2 · 미사 K-컬처 지장물 조사 전에',font=kr(san,34),fill='#D4B04C',anchor='mm')
im.save('img/nangman_gongram_thumb.png')

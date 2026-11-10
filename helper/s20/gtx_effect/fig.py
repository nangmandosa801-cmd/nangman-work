import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
A=json.load(open('an.json'))
def ser(city,grp): return [v[0]/10000 for v in A[city]['['+grp+' 합산]']['매매'].values()]
fig=plt.figure(figsize=(11.55,7.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'GTX 개통 · 역 앞 단지와 먼 단지 · 84㎡ 매매 중앙값(억원)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'동탄은 개통 전 1년에 역 앞이 10% 올랐고, 개통 뒤 1년은 둘 다 4~5%',fontsize=25,color=NAVY,fontweight='bold',va='top')
panels=[('동탄 · GTX-A 2024년 3월 개통',['2021','2023','개통 전\n1년','개통 뒤\n1년','2026'],'동탄','역 앞 500m 안 · 2015년 3단지','2km 밖 · 2015년 3단지'),
        ('운정 · GTX-A 2024년 12월 개통',['2021','2023','개통 전\n1년','개통 뒤\n1년','2026'],'운정','역 앞 700m 안 · 2단지','2km 밖 · 3단지'),
        ('별내 · GTX-B 공사 중',['2021','2023','2024','2025','2026'],'별내','역 1.5km 안 · 2012년 2단지','2.5km 밖 · 3단지')]
for i,(tt,xl,city,l1,l2) in enumerate(panels):
    ax=fig.add_axes([0.07+i*0.315,0.13,0.26,0.66])
    a=ser(city,'역세권'); b=ser(city,'먼곳'); xs=range(5)
    ax.plot(xs,a,color=NAVY,lw=3,marker='o',ms=7,label=l1); ax.plot(xs,b,color=GRAY,lw=3,marker='o',ms=7,label=l2)
    for x,v in zip(xs,a): ax.text(x,v+0.25,f'{v:.1f}',ha='center',fontsize=12,color=NAVY,fontweight='bold')
    for x,v in zip(xs,b): ax.text(x,v-0.55,f'{v:.1f}',ha='center',fontsize=12,color='#666')
    ax.set_xticks(list(xs)); ax.set_xticklabels(xl,fontsize=11.5,color='#333')
    lo=min(b)-1.2; hi=max(a)+3.0; ax.set_ylim(lo,hi); ax.set_yticks([])
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#C8D2DE')
    ax.set_title(tt,fontsize=14.5,color=NAVY,fontweight='bold',loc='left',pad=10)
    ax.legend(loc='upper right',fontsize=10.5,frameon=False,handlelength=1.6)
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 거래 뺌 · 직거래 뺌 · 단지 묶음 중앙값 · 2026년은 1~10월) · 역 거리는 지도로 잰 대략값',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_gtx_effect_1_line.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 동탄 · 운정 · 별내',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'GTX 개통',font=kr(ser_,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'동탄역 앞 84㎡ 개통 뒤 1년',font=kr(ser_,56),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'4% 상승',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'운정역 앞은 3% 하락',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gtx_effect_thumb.png'); print('fig ok')

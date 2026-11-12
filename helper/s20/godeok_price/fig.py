import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('리슈빌레이크파크 (2021)','0.6km',53000,53000),('호반써밋고덕신도시 (2021)','0.8km',59750,67400),('대광로제비앙 THE ART (2022)','0.8km',52900,53900),
('호반써밋 에듀파크 (2022)','1.0km',58700,60000),('제일풍경채 3차 센텀 (2023)','1.2km',67000,69250),('제일풍경채 2차 에듀 (2023)','1.4km',65600,69500),
('파라곤 (2019)','1.5km',61000,61850),('파라곤 에듀포레 (2021)','1.7km',54500,54500),('제일풍경채 (2019)','1.7km',61000,59000)]
def won(v): return f'{v//10000}억 {v%10000:,}' if v%10000 else f'{v//10000}억'
fig=plt.figure(figsize=(11.55,9.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'고덕국제신도시 아파트 시세 · 84㎡ 같은 단지 7~10월 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.935,'1년 전과 올해, 삼성 평택캠퍼스에서 가까운 순',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.09,0.6,0.75])
n=len(R); ys=list(range(n))[::-1]
for y,(nm,d,a,b) in zip(ys,R):
    ax.barh(y+0.19,a,height=0.36,color=GRAY); ax.barh(y-0.19,b,height=0.36,color=NAVY)
    ax.text(a+400,y+0.19,won(a),va='center',fontsize=12.5,color='#666')
    ch=(b/a-1)*100; s='그대로' if abs(ch)<0.05 else f'{ch:+.1f}%'
    ax.text(b+400,y-0.19,f'{won(b)}  {s}',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([f'{nm}\n캠퍼스까지 {d}' for nm,d,_,_ in R],fontsize=13,color='#333')
ax.set_xlim(40000,80000); ax.set_xticks([]); ax.set_ylim(-0.7,n-0.3)
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.36,0.862,'■ 2025년 7~10월',color=GRAY,fontsize=14); fig.text(0.53,0.862,'■ 2026년 7~10월',color=NAVY,fontsize=14,fontweight='bold')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 거래 뺌 · 단위 만원) · 거리는 단지 가운데에서 캠퍼스 담장까지 직선(오픈스트리트맵)',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_godeok_price_1_pair.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 고덕 · 84㎡ 매매',font=kr(san,30),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'고덕국제신도시',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'같은 단지 1년 전보다',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'10곳 중 6곳 올랐다',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'삼성 캠퍼스 0.6km 단지는 그대로',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_godeok_price_thumb.png')

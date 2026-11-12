import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_braincity_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def bars(M,cols,sub,head,ymax,src,fn):
    fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.955,sub,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,head,fontsize=28,color=NAVY,fontweight='bold',va='top')
    ax=fig.add_axes([0.07,0.13,0.88,0.64]); xs=range(len(M))
    ax.bar(xs,[v for _,v,_ in M],color=cols,width=0.6)
    for x,(m,v,n) in zip(xs,M):
        ax.text(x,v+ymax*0.012,won(v),ha='center',fontsize=16,color=NAVY,fontweight='bold')
        ax.text(x,ymax*0.035,f'{n}건',ha='center',fontsize=13,color='white')
    ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_,_ in M],fontsize=16,color='#333')
    ax.set_ylim(0,ymax); ax.set_yticks([])
    for s_ in ['top','right','left']: ax.spines[s_].set_visible(False)
    ax.spines['bottom'].set_color('#C8D2DE')
    fig.text(0.045,0.03,src,fontsize=12.5,color='#8A8578')
    fig.savefig(f'img/{S}{fn}.png'); plt.close()
# 1 브레인시티 2블록 84㎡ 전세 달별 중앙값
M=[('7월',24500,4),('8월',24000,15),('9월',25000,14),('10월',25000,4)]
bars(M,[NAVY]*4,'평택 브레인시티 2블록 로제비앙 모아엘가 · 84㎡ 전세 달별 중앙값(2026년)','7~10월 넉 달, 2억 4천~2억 5천 그대로',30000,
 '국토교통부 아파트 전월세 실거래(2026년 7~10월 계약 · 전용 80~86㎡ · 월세 없는 계약 중앙값 · 6월 1건 뺌)','1_jeonse')
# 2 브레인시티 2블록 84㎡ 분양권 달별 중앙값
M=[('7월',52359,37),('8월',48013,31),('9월',45512,27),('10월',44920,48)]
bars(M,[GRAY,BLUE,BLUE,NAVY],'평택 브레인시티 2블록 로제비앙 모아엘가 · 84㎡ 분양권 달별 중앙값(2026년)','분양권 84㎡, 넉 달 사이 7,400만원 내려',60000,
 '국토교통부 분양 · 입주권 실거래(2026년 7~10월 계약 · 전용 84~85㎡ · 해제 거래 뺌 · 11월 4건 뺌)','2_bunyang')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 브레인시티 · 2027년 2월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'브레인시티 중흥S클래스',font=kr(ser,72),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'옆 2블록 84㎡ 전세',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'2억 4천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2026년 7~10월 · 38건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def bars(R,t1,t2,src,fn,xmax):
    fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.955,t1,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,t2,fontsize=28,color=NAVY,fontweight='bold',va='top')
    ax=fig.add_axes([0.27,0.12,0.66,0.66])
    ys=list(range(len(R)))[::-1]
    ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
    ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
    for y,(_,v,c) in zip(ys,R):
        ax.text(v+xmax*0.012,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.set_xlim(0,xmax); ax.set_xticks([])
    for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#C8D2DE')
    fig.text(0.045,0.03,src,fontsize=12.5,color='#8A8578')
    fig.savefig(fn); plt.close()
bars([('래미안원베일리 84㎡\n(18건)',587500,GRAY),('아크로리버파크 84㎡\n(11건)',555000,GRAY),('반포 · 잠원 새 아파트\n84㎡ 전체 (71건)',508000,BLUE),('메이플자이 84㎡\n(17건)',501000,GRAY),('디에이치 클래스트 84㎡\n예상 분양가 (높은 쪽)',338000,NAVY),('디에이치 클래스트 84㎡\n예상 분양가 (낮은 쪽)',300000,NAVY)],
 '디에이치 클래스트 청약 · 반포 · 잠원 2015년 이후 아파트 올해 매매와 나란히',
 '84㎡ 예상 분양가, 옆 새 아파트보다 17억~20억 8천 낮다',
 '국토교통부 아파트 매매 실거래(2026년 1~9월 계약 · 중앙값 · 해제 거래 뺌) · 예상 분양가는 파이낸셜뉴스 · 아이뉴스24 2026년 10월 보도',
 'img/nangman_classt_1_price.png',700000)
bars([('옆 새 아파트 84㎡\n중앙값 50억 8천을 살 때',488000,GRAY),('84㎡ 예상 33억 8천\n당첨 시 현금',318000,NAVY),('84㎡ 예상 30억\n당첨 시 현금',280000,BLUE),('25억 넘는 집\n주택담보대출 한도',20000,GRAY)],
 '디에이치 클래스트 청약 · 84㎡ 당첨 뒤 입주까지 필요한 내 돈',
 '대출은 2억뿐, 현금 28억~31억 8천',
 '10 · 15 대책 주택담보대출 한도(25억 넘는 집 2억) · 현금 = 금액 - 대출 2억 · 국토교통부 아파트 매매 실거래(2026년 1~9월 · 반포동 · 잠원동 2015년 이후)',
 'img/nangman_classt_2_cash.png',600000)
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 반포 · 청약 계산서',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'디에이치 클래스트',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 옆 새 아파트보다',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'17억 낮다',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'반포 · 잠원 새 아파트 84㎡ 올해 중앙값 50억 8천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_classt_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_classt_1_price_v2.png', '84㎡ 예상 분양가, 옆 새 아파트보다 17억~20억 8천 낮다', [('래미안원베일리 84㎡|18건', 587500.0, '58억 7,500만', False), ('아크로리버파크 84㎡|11건', 555000.0, '55억 5,000만', False), ('반포 · 잠원 새 아파트 84㎡ 전체|71건', 508000.0, '50억 8,000만', False), ('디에이치 클래스트 84㎡ 예상 분양가|높은 쪽', 338000.0, '33억 8,000만', True), ('디에이치 클래스트 84㎡ 예상 분양가|낮은 쪽', 300000.0, '30억', False)], note='디에이치 클래스트 청약 · 반포 · 잠원 2015년 이후 아파트 올해 매매와 나란히')
print('v2 ok')

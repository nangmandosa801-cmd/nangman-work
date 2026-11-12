import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_dangwang_ipju_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 분양권 11건 (2024년 8월 ~ 2026년 11월 3일)
T=[('24.8',46800),('25.4',46800),('25.6',47790),('25.7',46820),('25.8',46820),('25.11',46820),('25.12',46800),('26.2',48780),('26.6',46800),('26.8',46350),('26.11',46800)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'안성당왕 경남아너스빌 하이스트 · 84㎡ 분양권 신고 11건(해제 없음)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'2년 넘게 4억 6천~4억 8천 안에서 신고됐다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.13,0.9,0.64])
xs=range(len(T)); cols=[GRAY]*7+[NAVY]*4
ax.bar(xs,[v for _,v in T],color=cols,width=0.62)
for x,(m,v) in zip(xs,T): ax.text(x,v+400,won(v).replace(' ','\n',1),ha='center',fontsize=12.5,color=NAVY,fontweight='bold')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_ in T],fontsize=14,color='#333')
ax.set_ylim(0,54000); ax.set_yticks([])
for s_ in ['top','right','left']: ax.spines[s_].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.83,'회색 2024~2025년 · 남색 2026년 (계약 연.월)',fontsize=12.5,color='#555')
fig.text(0.045,0.03,'국토교통부 분양권 실거래(2024년 8월~2026년 11월 3일 계약 · 전용 84㎡)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_bunyang.png'); plt.close()
# 2 월세 비율
R=[('올해 입주한 새 아파트 2곳\n(공도 진사리 · 양기리)',75.5,'98건 중 74건',BLUE),('2023~2024년 입주 4곳 합계\n(당왕 · 아양 · 공도)',45.1,'399건 중 180건',NAVY),('e편한세상안성그랑루체\n(당왕동 · 2024년)',71.1,'45건 중 32건',GRAY),('쌍용더플래티넘프리미어\n(공도 승두리 · 2023년)',38.7,'168건 중 65건',GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'안성 새 아파트 2026년 임대 계약 중 월세 비율',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'올해 입주한 단지는 10건 중 7~8건이 월세',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.3,0.12,0.6,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=14.5,color='#333')
for y,(_,v,n,c) in zip(ys,R): ax.text(v+1,y,f'{v:.0f}%  ({n})',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,105); ax.set_xticks([])
for s_ in ['top','right','bottom']: ax.spines[s_].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 모든 넓이 · 월세가 0원보다 큰 계약을 월세로 셈)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}2_wolse.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 안성 당왕지구 · 2027년 3월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,345),'안성 당왕 경남아너스빌',font=kr(ser,70),fill='#F4F1EA',anchor='mm')
d.text((W/2,450),'976세대 모두 84㎡',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,535),'옆 단지 84㎡ 전세',font=kr(ser,46),fill='#AFC0D8',anchor='mm')
d.text((W/2,640),'2억 5천',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,735),'2023~2024년 입주 옆 새 아파트 4곳 · 올해 86건 중앙값',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_dangwang_ipju_1_bunyang_v2.png', '2년 넘게 4억 6천~4억 8천 안에서 신고됐다', [('2024년 8월', 46800.0, '4억 6,800만', False), ('2025년 6월', 47790.0, '4억 7,790만', False), ('2026년 2월', 48780.0, '4억 8,780만', True), ('2026년 8월', 46350.0, '4억 6,350만', False), ('2026년 11월', 46800.0, '4억 6,800만', False)], note='안성당왕 경남아너스빌 하이스트 · 84㎡ 분양권 신고 11건(해제 없음)')
bars('img/nangman_dangwang_ipju_2_wolse_v2.png', '올해 입주한 단지는 10건 중 7~8건이 월세', [('올해 입주한 새 아파트 2곳|공도 진사리 · 양기리', 75.5, '76%', True), ('2023~2024년 입주 4곳 합계|당왕 · 아양 · 공도', 45.1, '45%', False), ('e편한세상안성그랑루체|당왕동 · 2024년', 71.1, '71%', False), ('쌍용더플래티넘프리미어|공도 승두리 · 2023년', 38.7, '39%', False)], note='안성 새 아파트 2026년 임대 계약 중 월세 비율')
print('v2 ok')

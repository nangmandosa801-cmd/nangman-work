import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    e,m=divmod(int(round(v)),10000)
    return f'{e}억 {m:,}만' if m else f'{e}억'
# 국토교통부 아파트 매매 실거래 2026년 1~10월 · 평택 지제동 · 동삭동 · 2018년 이후 · 전용 80~86㎡ · 해제 뺌 · 중앙값(만원), 건수
R=[('지제동 지제역 더샵 센트럴시티 (2022)',81000,101,GRAY),('한화포레나 지제역 84㎡A 분양가',70875,None,NAVY),('동삭동 평택 지제역 자이 (2023)',71700,37,GRAY),
   ('동삭동 힐스테이트 지제역 (2020)',60000,37,GRAY),('동삭동 힐스테이트 지제역 퍼스티움 (2022)',58450,44,GRAY),('동삭동 더샵 지제역 센트럴파크 2BL (2020)',53000,33,GRAY),
   ('동삭동 e편한세상 지제역 (2022)',51700,40,GRAY),('동삭동 지제역 푸르지오 엘리아츠 (2024)',50000,13,GRAY),('동삭동 평택 센트럴자이 3단지 (2019)',42250,66,GRAY)]
R=sorted(R,key=lambda r:-r[1])
fig=plt.figure(figsize=(11.55,8.8),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'한화포레나 지제역 청약 · 84㎡A 분양가와 동삭동 · 지제동 84㎡ 올해 매매',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.92,'분양가 7억 875만, 위에는 두 단지뿐',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.40,0.10,0.54,0.74])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.62)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=14,color='#333')
for y,(_,v,n,c) in zip(ys,R):
    ax.text(v+800,y,won(v),va='center',fontsize=15,color=NAVY,fontweight='bold')
    if n: ax.text(v-900,y,f'{n}건',va='center',ha='right',fontsize=12.5,color='white')
ax.set_xlim(0,100000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'입주자모집공고(2026년 10월 29일 · 84㎡A 가장 높은 금액 · 확장비 별도) · 국토교통부 매매 실거래(2026년 1~10월 · 전용 80~86㎡ · 해제 거래 뺌 · 중앙값)',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_jije_rate_1_sise.png'); plt.close()
# 동삭동 + 지제동 2018년 이후 84㎡ 달별 매매 중앙값
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
V=[53950,50850,48500,56000,51700,56500,70500,58800,57900,54000]
Z=[69750,None,70800,74500,None,69550,72000,75500,79250,77000]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'동삭동 · 지제동 2018년 이후 84㎡ · 2026년 달별 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'평택 지제역 자이 84㎡, 1월 6억 9,750만 → 9월 7억 9,250만',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.86,0.64])
x=list(range(len(M)))
ax.plot(x,[v/10000 for v in V],color=GRAY,lw=3,marker='o',ms=7,label='동삭동 · 지제동 84㎡ 전체 (440건)')
zx=[i for i,z in enumerate(Z) if z]; ax.plot(zx,[Z[i]/10000 for i in zx],color=BLUE,lw=3,marker='o',ms=7,label='평택 지제역 자이 84㎡ (37건)')
ax.axhline(7.0875,color=NAVY,lw=2,ls='--'); ax.text(2.0,6.8,'점선: 84㎡A 분양가 7억 875만',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
for i in [0,9]: ax.text(i,V[i]/10000-0.28,won(V[i]),ha='center',fontsize=12.5,color='#555')
ax.text(5.85,6.75,won(V[6]),ha='right',fontsize=12.5,color='#555')
for i in [0,8]: ax.text(i,Z[i]/10000+0.18,won(Z[i]),ha='center',fontsize=12.5,color=BLUE,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(M,fontsize=14); ax.set_ylim(4,8.6); ax.set_xlim(-0.4,10.4)
ax.set_yticks([4,5,6,7,8]); ax.set_yticklabels(['4억','5억','6억','7억','8억'],fontsize=13,color='#555')
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE'); ax.spines['bottom'].set_color('#C8D2DE'); ax.grid(axis='y',color='#EEF1F5')
ax.legend(loc='upper left',fontsize=13,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 평택 동삭동 · 지제동 · 전용 80~86㎡ · 해제 거래 뺌) · 자이는 거래 없는 달 빼고 이음',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_jije_rate_2_month.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 지제역 · 청약 결과',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'한화포레나 지제역',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'84㎡A 분양가',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'7억 875만',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'옆 평택 지제역 자이 84㎡ 올해 7억 1,700만',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_jije_rate_thumb.png')

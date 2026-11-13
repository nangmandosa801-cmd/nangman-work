import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_gwanggyo_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
# 1. 광교 단지별 84㎡ 2021 · 2026 중앙값 (2011~2013 준공 7곳 + 2018~2019 준공 3곳)
L=[('자연앤힐스테이트','자연앤힐\n2012'),('광교센트럴뷰','센트럴뷰\n2013'),('광교더리브','더리브\n2013'),('광교호수마을호반써밋','호반써밋\n2011'),('광교2차e편한세상','e편한2차\n2011'),('광교호반베르디움(이의)','호반베르디움\n2011'),('광교더포레스트','더포레스트\n2013'),('광교한양수자인','한양수자인\n2011'),('광교해모로','해모로\n2011'),('광교중흥에스클래스','중흥S\n2019'),('광교아이파크','아이파크\n2018'),('광교더샵','더샵\n2018')]
v21=[J[k]['2021']['med']/10000 for k,_ in L]; v26=[J[k]['2026']['med']/10000 for k,_ in L]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 아파트 시세 · 단지별 전용 84㎡ 매매 중앙값, 2021년과 2026년 1~10월',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'자연앤힐스테이트 18억 7,000만 · 2021년보다 22.6% 위',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.19,0.92,0.57])
x=list(range(len(L))); w=0.38
ax.bar([i-w/2 for i in x],v21,width=w,color=GRAY)
ax.bar([i+w/2 for i in x],v26,width=w,color=[NAVY if i<9 else BLUE for i in x])
for i,(a,b) in enumerate(zip(v21,v26)):
    ax.text(i-w/2,a+0.3,f'{a:.1f}',ha='center',fontsize=10,color='#777')
    ax.text(i+w/2,b+0.3,f'{b:.1f}',ha='center',fontsize=11.5,color=NAVY,fontweight='bold')
    p=(b/a-1)*100; ax.text(i+w/2,b+1.7,f'{p:+.1f}%',ha='center',fontsize=11,color=NAVY if p>=20 else '#777',fontweight='bold' if p>=20 else 'normal')
ax.set_xticks(x); ax.set_xticklabels([n for _,n in L],fontsize=11,color='#555')
ax.set_yticks([]); ax.set_ylim(0,24.5); ax.set_xlim(-0.6,len(L)-0.4)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axvline(8.5,color=NAVY,lw=1,ls='--'); ax.text(4,23.3,'2011~2013년 준공 · 이의동 · 하동',fontsize=13,color=NAVY,ha='center'); ax.text(10,23.3,'2018~2019년 · 원천동',fontsize=13,color=BLUE,ha='center')
fig.text(0.045,0.085,'회색 = 2021년 · 색 = 2026년 1~10월 · 숫자는 억원 · 막대 위 %는 2021년 대비 변화 · 호반베르디움은 2021년 6건 · 한양수자인 11건',fontsize=12,color='#8A8578')
fig.text(0.045,0.05,'국토교통부 아파트 매매 실거래(수원시 영통구 이의동 · 하동 · 원천동 · 전용 83~86㎡ · 해제 거래 · 직거래 뺌 · 2026년은 10월 24일 신고분까지)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_dan.png'); plt.close()

# 2. 2021~2026 해마다 중앙값 · 자연앤힐 · 센트럴뷰 · 호반써밋 · e편한2차 · 중흥
yrs=['2021','2022','2023','2024','2025','2026']
def ser(k): return [J[k][y]['med']/10000 for y in yrs]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 자연앤힐스테이트 · 전용 84㎡ 해마다 매매 중앙값, 2021~2026년',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'2023년 −13.1% · 2026년 +22.6%, 호반써밋은 −18.1% · +4.2%',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.84,0.64])
xs=list(range(6))
for k,col,ls,lab,dy in [('자연앤힐스테이트',NAVY,'-','자연앤힐스테이트 2012',0.5),('광교중흥에스클래스',BLUE,'--','중흥S클래스 2019',-0.9),('광교센트럴뷰',BLUE,'-','센트럴뷰 2013',0.5),('광교호수마을호반써밋',GRAY,'-','호반써밋 2011',-0.9),('광교2차e편한세상',GRAY,'--','e편한세상 2차 2011',-0.9)]:
    v=ser(k); ax.plot(xs,v,color=col,lw=2.8 if k=='자연앤힐스테이트' else 2.2,ls=ls,marker='o')
    ax.text(5.15,v[-1],lab,fontsize=12.5,color=col if col!=GRAY else '#777',va='center')
    for i,a in enumerate(v):
        if k=='자연앤힐스테이트' or (k=='광교호수마을호반써밋' and i in (0,2,5)): ax.text(i,a+dy,f'{a:.1f}',ha='center',fontsize=12,color=col if col!=GRAY else '#777',fontweight='bold')
ax.set_xticks(xs); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555'); ax.set_xlim(-0.3,6.8)
ax.set_yticks([8,10,12,14,16,18,20]); ax.set_yticklabels([f'{v}억' for v in [8,10,12,14,16,18,20]],fontsize=12,color='#555'); ax.set_ylim(8,20.5)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.055,'숫자는 억원 · 2022년은 거래가 적음(자연앤힐 26건 · 중흥 13건 · 센트럴뷰 6건 · 호반써밋 4건 · e편한세상 2차 2건)',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(2021년 1월~2026년 10월 24일 계약 · 전용 83~86㎡ · 해제 거래 · 직거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 8화 · 수원 광교',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'광교 자연앤힐스테이트',font=kr(ser_,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'84㎡ 매매 중앙값',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'18억 7,000만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2021년보다 22.6% 위 · 2026년 1~10월 43건 · 새 전세 9억 6천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

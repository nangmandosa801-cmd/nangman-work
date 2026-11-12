import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_junggye_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
# 1. 을지초 배정 네 단지 사다리 · 2026 매매 중앙값 · 새 세입자 전세 · 2021 중앙값
L=[('주공10단지 58㎡','주공10단지'),('건영3차 84㎡','건영3차'),('청구3차 84㎡','청구3차'),('롯데우성 115㎡','롯데우성 115㎡')]
mm=[J[k]['2026']['med']/10000 for _,k in L]; je=[J[k]['je2026']['new_med']/10000 for _,k in L]; m21=[J[k]['2021']['med']/10000 for _,k in L]
n26=[J[k]['2026']['n'] for _,k in L]; jn=[J[k]['je2026']['new_n'] for _,k in L]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'중계동 아파트 시세 · 을지초 배정 네 단지 2026년 1~10월 매매 · 새 세입자 전세 중앙값',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'7억 1,500 → 12억 5,800 → 13억 6,000 → 14억 1,250',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.2,0.16,0.76,0.6])
ys=list(range(4)); h=0.34
ax.barh([y+h/2 for y in ys],mm,height=h,color=NAVY)
ax.barh([y-h/2 for y in ys],je,height=h,color=BLUE)
for y,(a,b,c,n,k) in enumerate(zip(mm,je,m21,n26,jn)):
    ax.text(max(a,c)+0.2,y+h/2,f'매매 {a:.2f}억 ({n}건)',va='center',fontsize=12.5,color=NAVY,fontweight='bold')
    ax.text(b+0.15,y-h/2,f'전세 {b:.2f}억 ({k}건) · 전세가율 {b/a*100:.0f}%',va='center',fontsize=12,color=BLUE)
    ax.plot([c,c],[y+h/2-h/2,y+h/2+h/2],color='#D4B04C',lw=3); ax.text(c,y+h+0.06,f'2021년 {c:.2f}억',ha='center',fontsize=10.5,color='#8A7A3A')
ax.set_yticks(ys); ax.set_yticklabels([l for l,_ in L],fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_xticks([]); ax.set_xlim(0,19)
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.075,'남색 = 2026년 1~10월 매매 중앙값 · 파랑 = 2026년 새 세입자 전세 중앙값(월세 0원 · 신규 계약) · 노란 선 = 2021년 매매 중앙값 · 숫자는 억원',fontsize=12,color='#8A8578')
fig.text(0.045,0.04,'국토교통부 아파트 매매 · 전월세 실거래(노원구 중계동 · 해제 거래 뺌 · 2026년은 10월 23일 신고분까지) · 배정 단지는 보도 · 부동산 정보 서비스 목록 기준',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_ladder.png'); plt.close()

# 2. 84㎡ 2021~2026 해마다 중앙값 · 청구3차 · 건영3차 vs 하계동 하계1청구 · 하계2현대
yrs=['2021','2022','2023','2024','2025','2026']
def ser(k): return [J[k][y]['med']/10000 if J[k][y]['med'] else None for y in yrs]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'중계동 아파트 시세 · 84㎡ 해마다 매매 중앙값, 2021~2026년 · 하계동 1997년 단지와 비교',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'2026년 청구3차 2021년의 99% · 건영3차 99% · 하계동 두 단지 94%',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.86,0.64])
xs=list(range(6))
for k,col,ls,lab,dy,ly in [('청구3차',NAVY,'-','청구3차 84㎡',0.35,0),('건영3차',BLUE,'-','건영3차 84㎡',-0.6,0),('하계1청구',GRAY,'-','하계1청구 84㎡',0.35,0.3),('하계2현대','#7A8590','--','하계2현대 84㎡',-0.6,-0.3)]:
    v=ser(k); px=[x for x,a in zip(xs,v) if a]; pv=[a for a in v if a]
    ax.plot(px,pv,color=col,lw=2.8 if col in (NAVY,BLUE) else 2.2,ls=ls,marker='o')
    for x,a in zip(px,pv): ax.text(x,a+dy,f'{a:.1f}',ha='center',fontsize=11.5,color=col if col!=GRAY else '#777',fontweight='bold' if col in (NAVY,BLUE) else None)
    ax.text(5.15,pv[-1]+ly,lab,fontsize=12.5,color=col if col!=GRAY else '#777',va='center')
ax.set_xticks(xs); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555'); ax.set_xlim(-0.3,6.5)
ax.set_yticks([8,10,12,14]); ax.set_yticklabels(['8억','10억','12억','14억'],fontsize=12,color='#555'); ax.set_ylim(7,15)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.055,'숫자는 억원 · 2022년은 거래가 적음(청구3차 7건 · 건영3차 4건 · 하계1청구 2건 · 하계2현대 0건)',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(2021년 1월~2026년 10월 23일 계약 · 전용 83~86㎡ · 해제 거래 뺌) · 청구3차 1996년 · 건영3차 1995년 · 하계동 둘 1997년',fontsize=11.5,color='#8A8578')
fig.savefig('img/'+S+'2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 5화 · 노원구 중계동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'중계동 아파트 시세',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'을지초 배정 84㎡',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'13억 6,000만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'청구3차 · 2021년 고점의 99% · 새 세입자 전세 8억',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

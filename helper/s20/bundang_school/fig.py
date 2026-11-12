import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_bundang_school_'
J=json.load(open('ana.json'))
BINS=['S','59','84','101','131','164']
LAB=['28~49㎡','59㎡','84㎡','101㎡','131~135㎡','164㎡ 이상']
h=J['grp']['hak']; p=J['grp']['pair']
# 1. 2026년 넓이별 전용 3.3㎡당 매매 중앙값 · 학군 단지 vs 야탑 · 구미
hv=[h[b]['2026']['py']/10000 for b in BINS]; pv=[p[b]['2026']['py']/10000 for b in BINS]
hn=[h[b]['2026']['n'] for b in BINS]; pn=[p[b]['2026']['n'] for b in BINS]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'분당 아파트 시세 · 넓이별 전용 3.3㎡당 매매 중앙값(2026년 1~10월)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'수내 · 서현 학군 단지 소형 1억 900만 · 164㎡ 이상 5,100만 · 2.1배',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.15,0.92,0.6])
x=list(range(6)); w=0.38
ax.bar([i-w/2 for i in x],hv,width=w,color=NAVY); ax.bar([i+w/2 for i in x],pv,width=w,color=GRAY)
for i,(a,b,n1,n2) in enumerate(zip(hv,pv,hn,pn)):
    ax.text(i-w/2,a+0.015,f'{a:.2f}',ha='center',fontsize=12,color=NAVY,fontweight='bold')
    ax.text(i-w/2,a/2,f'{n1}건',ha='center',fontsize=10,color='white')
    ax.text(i+w/2,b+0.015,f'{b:.2f}',ha='center',fontsize=11,color='#666')
    ax.text(i+w/2,b/2,f'{n2}건',ha='center',fontsize=10,color='white')
ax.set_xticks(x); ax.set_xticklabels(LAB,fontsize=13,color='#555')
ax.set_yticks([]); ax.set_ylim(0,1.3)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(0.3,1.2,'■ 수내 · 서현 학군 단지(양지마을 · 파크타운 · 시범단지)',fontsize=13,color=NAVY)
ax.text(0.3,1.12,'■ 야탑 · 구미 같은 연식 단지(탑마을 · 매화 · 장미 · 까치 · 무지개 · 하얀마을)',fontsize=13,color='#777')
fig.text(0.045,0.055,'숫자는 억원 · 전용면적 3.3㎡당 · 막대 안은 거래 건수 · 1991~1996년 준공 단지',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(성남시 분당구 · 2026년 1월~10월 24일 신고분 · 해제 · 직거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_bin.png'); plt.close()

# 2. 2021~2026 해마다 전용 3.3㎡당 중앙값 · 학군 단지 소형 · 84 · 131 · 164 + 야탑 · 구미 소형
yrs=['2021','2022','2023','2024','2025','2026']
def ser(g,b): return [g[b][y]['py']/10000 for y in yrs]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'분당 아파트 시세 · 수내 · 서현 학군 단지 전용 3.3㎡당 매매 중앙값, 2021~2026년',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'소형이 2021년에도 1.7배, 2026년은 2.1배',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.86,0.64])
xs=list(range(6))
lines=[('S','학군 단지 28~49㎡',NAVY,3.0),('84','학군 단지 84㎡',BLUE,2.6),('131','학군 단지 131~135㎡','#6E8BAA',2.2),('164','학군 단지 164㎡ 이상','#9FB3C8',2.2)]
for b,lab,col,lw in lines:
    v=ser(h,b); ax.plot(xs,v,color=col,lw=lw,marker='o')
    ax.text(5.15,v[-1]-(0.03 if b=='131' else 0),lab,fontsize=12.5,color=col,va='center')
    if b in ('S','164'): ax.text(-0.12,v[0],f'{v[0]:.2f}',ha='right',fontsize=11.5,color=col,fontweight='bold',va='center')
    ax.text(5,v[-1]+0.03,f'{v[-1]:.2f}',ha='center',fontsize=11.5,color=col,fontweight='bold')
v=ser(p,'S'); ax.plot(xs,v,color=GRAY,lw=2.2,marker='o',ls='--'); ax.text(5.15,v[-1]+0.025,'야탑 · 구미 28~49㎡',fontsize=12.5,color='#777',va='center')
ax.set_xticks(xs); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555'); ax.set_xlim(-0.3,6.6)
ax.set_yticks([0.3,0.5,0.7,0.9,1.1]); ax.set_yticklabels(['3,000만','5,000만','7,000만','9,000만','1억 1천'],fontsize=12,color='#555'); ax.set_ylim(0.25,1.2)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.055,'숫자는 억원 · 전용면적 3.3㎡당 · 2022년은 학군 단지 거래 175건뿐 · 학군 단지 = 양지마을 · 파크타운 · 시범단지 5곳',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(성남시 분당구 · 2021년 1월~2026년 10월 24일 신고분 · 해제 · 직거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 6화 · 분당 수내 · 서현',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'분당 아파트 시세',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'소형 평당 1억 1,100만',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'큰 평형의 2배',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'양지마을 35㎡ 11억 8천 · 194~198㎡ 31억 8,750 · 2026년',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')

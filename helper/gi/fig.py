import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 감일지구(하남 감이동 · 감일동) 84㎡ 매매 · 월별 중앙값(만원) · 건수 · 해제 · 직거래 뺌
M=[('25.1',9,113000),('2',19,115800),('3',32,111250),('4',6,108500),('5',14,113500),('6',43,118000),('7',12,112000),('8',19,111000),('9',58,120000),('10',28,120000),('11',5,122000),('12',12,129000),
   ('26.1',9,127000),('2',14,142000),('3',12,142500),('4',12,138500),('5',13,136000),('6',13,149000),('7',16,136750),('8',10,145000),('9',7,143000),('10',4,143000)]
x=list(range(len(M)))
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'감일동 아파트 시세 · 84㎡ 매매 월별 중앙값과 거래 건수',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'값은 11억대에서 14억대로, 거래는 한 달 10건 안팎으로',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.40,0.88,0.40]); bx=fig.add_axes([0.07,0.12,0.88,0.22],sharex=ax)
ax.plot(x,[v/10000 for *_,v in M],color=NAVY,lw=3,marker='o',ms=6)
for i in (0,9,21):
    v=M[i][2]/10000; ax.text(i,v+0.35,f'{v:.1f}억',ha='center',fontsize=14,color=NAVY,fontweight='bold')
ax.set_ylim(9.5,16.5); ax.set_yticks([10,12,14,16]); ax.set_yticklabels(['10억','12억','14억','16억'],fontsize=12,color='#555')
bx.bar(x,[n for _,n,_ in M],color=[GRAY if i<9 or i>9 else BLUE for i in x],width=0.62)
for i,(_,n,_) in enumerate(M): bx.text(i,n+1.2,str(n),ha='center',fontsize=11,color='#555')
bx.set_ylim(0,70); bx.set_yticks([])
bx.set_xticks(x); bx.set_xticklabels([a for a,_,_ in M],fontsize=11.5,color='#555')
plt.setp(ax.get_xticklabels(),visible=False)
for a in (ax,bx):
    for s in ['top','right']: a.spines[s].set_visible(False)
    a.spines['left'].set_color('#C8D2DE'); a.spines['bottom'].set_color('#C8D2DE')
    a.axvline(9.5,color=BLUE,lw=1.4,ls='--')
ax.text(9.6,16.1,'2025.10.20 하남 토지거래허가 시작',fontsize=12.5,color=BLUE,va='top')
ax.text(20.9,10.2,'10.29 감일2지구 발표 →\n11월 2일 계약까지 매매 신고 0건',fontsize=12.5,color=NAVY,ha='right')
bx.text(-0.4,62,'거래 건수',fontsize=12,color='#7A8590')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 · 하남 감이동 · 감일동 전용 83~86㎡ · 2025년 1월~2026년 10월 계약 · 해제 · 직거래 뺌',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_gamilsise_1_flow.png'); plt.close()

# 단지별 2025 vs 2026
D=[('힐스테이트포웰시티',131250,161500),('감일파크센트레빌',123000,152000),('e편한세상감일',119000,149000),('감일수자인',124000,147500),('감일스타힐스',115000,145000),
   ('감일푸르지오마크베르',115000,137000),('감일한라비발디',110000,136250),('감일센트레빌',104750,130000),('감일금강펜테리움\n센트럴파크',104000,127750)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'감일동 아파트 시세 · 단지별 84㎡ 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.915,'아홉 단지 모두 올랐고 오른 폭은 2억 2천~3억',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.09,0.70,0.75])
ys=list(range(len(D)))[::-1]; h=0.36
ax.barh([y+h/2 for y in ys],[a/10000 for _,a,_ in D],height=h,color=GRAY,label='2025년')
ax.barh([y-h/2 for y in ys],[b/10000 for *_,b in D],height=h,color=NAVY,label='2026년 1~10월')
for y,(_,a,b) in zip(ys,D):
    ax.text(a/10000+0.15,y+h/2,f'{a/10000:.1f}억',va='center',fontsize=12,color='#555')
    ax.text(b/10000+0.15,y-h/2,f'{b/10000:.1f}억  (+{(b-a)/10000:.1f}억)',va='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([n for n,_,_ in D],fontsize=13.5,color='#333')
ax.set_xlim(0,21); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.legend(loc='lower right',bbox_to_anchor=(1.0,1.0),ncol=2,fontsize=13,frameon=False)
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래 · 전용 83~86㎡ · 해제 · 직거래 뺌 · 2025년 거래가 없는 감일스윗시티10단지는 뺌',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_gamilsise_2_danji.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감일 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'감일동 아파트 시세',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'84㎡ 1년 새',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'+2억 3천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'중앙값 11억 8천 → 14억 1천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gamilsise_thumb.png')

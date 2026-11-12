import pandas as pd
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
E=['더샵송도마리나베이','랜드마크시티센트럴더샵','송도오션파크베르디움','송도SKVIEW','호반써밋송도','e편한세상송도']
D=[]
for y in (2025,2026):
    m=pd.read_pickle(f'/home/claude/rtn/M{y}.pkl'); m=m[m['시군구'].str.contains('연수구 송도동')&(m['해제사유발생일']=='-')].copy(); m['y']=y; D.append(m)
m=pd.concat(D); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int); m['a']=m['전용면적(㎡)'].astype(float)
m=m[(m.a>=83)&(m.a<=86)].copy()
ym=m['계약년월'].astype(int); m['q']=(ym//100).astype(str)+'.'+(((ym%100-1)//3)+1).astype(str)
K=m[m['단지명'].isin(E)]
m=m[ym<202610]  # 분기 그래프는 10월(한 달뿐)을 뺌
k=m[m['단지명'].isin(E)]
qs=sorted(m.q.unique()); lab=[f"{q[2:4]}년\n{q[-1]}분기" for q in qs]
a=[k[k.q==q].p.median()/10000 for q in qs]; b=[m[m.q==q].p.median()/10000 for q in qs]

fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송도 8공구 아파트 84㎡ 매매 중앙값 · 분기별 (2025년 1월~2026년 9월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'8공구는 7개 분기 모두 6억 3천~6억 7천 사이',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.86,0.63]); x=range(len(qs))
ax.plot(x,b,color=GRAY,lw=4,marker='o',ms=9); ax.plot(x,a,color=NAVY,lw=4.5,marker='o',ms=10)
for i,(u,v) in enumerate(zip(a,b)):
    ax.text(i,u-0.13,f'{u:.2f}',ha='center',va='top',fontsize=14,color=NAVY,fontweight='bold')
    ax.text(i,v+0.09,f'{v:.2f}',ha='center',va='bottom',fontsize=13,color='#6B7686')
ax.text(len(qs)-1+0.15,a[-1],'8공구 6개 단지',fontsize=15,color=NAVY,fontweight='bold',va='center')
ax.text(len(qs)-1+0.15,b[-1],'송도동 전체',fontsize=15,color='#6B7686',va='center')
ax.set_xticks(list(x)); ax.set_xticklabels(lab,fontsize=14,color='#333'); ax.set_xlim(-0.4,len(qs)-1+1.3)
ax.set_ylim(5.8,8.0); ax.set_ylabel('억원',fontsize=14,color='#555'); ax.tick_params(axis='y',labelsize=13,colors='#555')
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 거래 뺌 · 2026년 10월은 한 달치라 뺌) · 8공구 6개 단지는 본문 표 · 송도동 전체는 옛 송도 포함',fontsize=11.5,color='#8A8578')
print([round(v,2) for v in a],[round(v,2) for v in b]);fig.savefig('img/nangman_songdo8_1_trend.png'); plt.close()

g=K.groupby(['단지명','y']).p.median().unstack()/10000
g=g.sort_values(2026)
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송도 8공구 아파트 84㎡ 단지별 매매 중앙값 · 2025년과 2026년(1~10월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'송도SKVIEW만 7억대, 나머지 다섯 곳은 6억대',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66]); ys=range(len(g))
ax.barh([y+0.2 for y in ys],g[2025],height=0.36,color=GRAY,label='2025년')
ax.barh([y-0.2 for y in ys],g[2026],height=0.36,color=NAVY,label='2026년 1~10월')
for y,(nm,r) in zip(ys,g.iterrows()):
    ax.text(r[2025]+0.05,y+0.2,f'{r[2025]:.2f}억',va='center',fontsize=13,color='#6B7686')
    ax.text(r[2026]+0.05,y-0.2,f'{r[2026]:.2f}억',va='center',fontsize=14,color=NAVY,fontweight='bold')
ax.set_yticks(list(ys)); ax.set_yticklabels(g.index,fontsize=15,color='#333')
ax.set_xlim(5,7.9); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE'); ax.legend(loc='lower right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 거래 뺌 · 2026년은 1~10월 계약) · 막대 왼쪽 끝은 5억',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_songdo8_2_danji.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 인천 연수구 · 송도국제도시',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'송도 8공구 아파트',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 올해 매매',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'6억 5천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'송도동 전체 84㎡는 7억 3천',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_songdo8_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_songdo8_2_danji_v2.png', '송도SKVIEW만 7억대, 나머지 다섯 곳은 6억대', [('송도오션파크베르디움', 6.2, '6.20억', False), ('랜드마크시티센트럴더샵', 6.4, '6.40억', False), ('e편한세상송도', 6.43, '6.43억', False), ('더샵송도마리나베이', 6.5, '6.50억', False), ('송도SKVIEW', 7.195, '7.20억', True)], note='송도 8공구 84㎡ 단지별 매매 중앙값 · 2026년 1~10월')
print('v2 ok')

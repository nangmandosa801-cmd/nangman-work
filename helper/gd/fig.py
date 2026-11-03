import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
G=['1차 시험','2차 시험']; R35=[15.07,30.89]; R36=[23.51,32.14]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'공인중개사 합격률 · 35회(2024)와 36회(2025) 큐넷 합격자 공고',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1차 합격률 15.07%에서 23.51%로 올랐습니다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.14,0.86,0.62])
x=[0,1]; w=0.34
b1=ax.bar([i-w/2-0.01 for i in x],R35,w,color=GRAY,label='35회 (2024)')
b2=ax.bar([i+w/2+0.01 for i in x],R36,w,color=[NAVY,BLUE],label='36회 (2025)')
for bars,vals in ((b1,R35),(b2,R36)):
    for b,v in zip(bars,vals):
        ax.text(b.get_x()+b.get_width()/2,v+0.7,f'{v:.2f}%',ha='center',fontsize=18,color=NAVY,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=18,color='#333')
ax.set_ylim(0,40); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=GRAY,label='35회 (2024)'),Patch(color=NAVY,label='36회 (2025)')],fontsize=15,frameon=False,loc='upper left')
ax.text(0+w/2+0.01,R36[0]/2,'응시 80,387명\n합격 18,901명',ha='center',va='center',fontsize=13.5,color='white')
ax.text(1+w/2+0.01,R36[1]/2,'응시 33,247명\n합격 10,686명',ha='center',va='center',fontsize=13.5,color='white')
ax.text(0-w/2-0.01,R35[0]/2,'응시 98,483명\n합격 14,850명',ha='center',va='center',fontsize=13.5,color=NAVY)
fig.text(0.045,0.03,'큐넷 제36회 합격자 공고(2025년 11월 26일) · 35회 1차 인원은 고시위크 보도 · 35회 2차 인원은 확인한 자료에 없음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gadap_1_passrate.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 공인중개사 시험 · 기출문제 풀이',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'37회 공인중개사 가답안',font=kr(ser,70),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'이의제기 마감',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'11월 6일 18시',font=kr(ser,88),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'최종정답 · 합격자 발표 12월 2일',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gadap_thumb.png')

import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_sash_'
TXT='#444'; GRY='#8A8578'; OK='#3C7A5A'
render_interior('낭만 인테리어 · 창호',['샷시 교체 지원금,','현금이냐 이자냐'],'보조금 · 융자 · 이자지원이 다릅니다','그린리모델링 · 서울 BRP · 새빛주택',O+'thumb.png')
def canvas(t1,t2,h=6.6):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=17,color=MID,va='center'); fig.text(0.04,0.905,t2,fontsize=23,color=NAVY,fontweight='bold',va='center')
    return fig,ax
# fig1 three cards
fig,ax=canvas('샷시 교체 지원금 · 세 가지 방식','공사비를 깎아 주는 것은 공사비 보조뿐입니다',h=8.6)
C=[('공사비 보조','서울 새빛주택','공사비 70%\n(공동주택 최대 300만원)','15년 넘고\n공시가격 3억원 이하',OK,'공사비가 줄어듦'),
   ('저금리 융자','서울 BRP','0.8% 고정금리\n최대 3,000만원\n96개월','15년 넘고\n공시가격\n12억원 이하',MID,'싸게 빌림'),
   ('이자 지원','그린리모델링 (전국)','이자율 4.5~5.5%만큼\n공동주택 3,000만원\n60개월','2016년 전\n사용승인 민간건물\n공사 전 신청',NAVY,'이자만 덜 냄')]
for i,(t,n,a,b,c,r) in enumerate(C):
    x=4+i*36
    ax.add_patch(mp.FancyBboxPatch((x,3),33,58,boxstyle='round,pad=0.3,rounding_size=2',fc='#F4F6F9',ec=c,lw=3))
    ax.text(x+16.5,54,t,ha='center',fontsize=24,fontweight='bold',color=c)
    ax.text(x+16.5,48,n,ha='center',fontsize=17,color=TXT)
    ax.text(x+16.5,36,a,ha='center',va='center',fontsize=17,color=NAVY,fontweight='bold',linespacing=1.5)
    ax.text(x+16.5,21,b,ha='center',va='center',fontsize=16,color=TXT,linespacing=1.5)
    ax.text(x+16.5,7,r,ha='center',fontsize=21,fontweight='bold',color=WARN if i==2 else c)
finish(fig,O+'fig1.png','2026년 공고 기준 · 예산이 떨어지면 일찍 마감합니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2 decision
fig,ax=canvas('샷시 교체 지원금 · 우리 집은 어디부터','서울인지, 공시가격이 얼마인지부터 봅니다',h=8.6)
def box(x,y,w,h,t,c,fc='#F4F6F9',fs=18):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.3,rounding_size=1.5',fc=fc,ec=c,lw=2.5)); ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=NAVY,fontweight='bold',linespacing=1.5)
box(34,52,44,9,'우리 집은 서울인가요?',NAVY,fs=21)
box(4,30,46,12,'공시가격 3억원 이하\n15년 넘은 집인가요?',MID)
box(64,31,44,10,'서울 밖',GRY)
box(1.5,3,25,16,'새빛주택\n공사비 70%',OK,'#EAF3EE')
box(29,3,26,16,'BRP 0.8% 융자\n+ 이자지원\n비교',MID)
box(60,3,48,16,'그린리모델링 이자지원\n+ 우리 시·군 자체 사업',NAVY)
for (x1,y1,x2,y2,l) in [(48,52,28,42.5,'예 '),(64,52,86,41.5,'아니오'),(18,30,13,19.5,'예'),(36,30,42,19.5,'아니오'),(86,31,86,19.5,'')]:
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color=GRY,lw=1.8))
    if l: ax.text((x1+x2)/2+(-6 if l=='예 ' else 1.5),(y1+y2)/2+(2.5 if l=='예 ' else 0),l.strip(),fontsize=16,color=GRY)
finish(fig,O+'fig2.png','어느 쪽이든 공사 전에 신청 · 창호 에너지효율 등급 조건 확인',brand='낭만 인테리어',allow_outside=True,strict=False)

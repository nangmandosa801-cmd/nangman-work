src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/sanji/'
GOLD='#C9962E'; RED='#B5503C'; GREEN='#4E7D4A'
def boxes(cols,title,sub,note,out,h=6.2,fs=16.5):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.10,top=0.76,left=0.03,right=0.97); ax.set_axis_off(); ax.set_xlim(0,15); ax.set_ylim(0,6)
    for k,(t,c,items) in enumerate(cols):
        x=0.2+k*5
        ax.add_patch(FancyBboxPatch((x,0.2),4.6,5.5,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
        ax.add_patch(FancyBboxPatch((x,4.6),4.6,1.1,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c))
        ax.text(x+2.3,5.15,t,ha='center',va='center',fontsize=20,color='white',fontproperties=FB)
        for j,it in enumerate(items): ax.text(x+2.3,3.6-j*1.15,it,ha='center',va='center',fontsize=fs,color=DEEP,fontproperties=FB)
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
boxes([('산지전용허가',DEEP,['산을 다른 땅으로','집 · 카페 · 창고','부담금 냄']),('산지전용신고',GREEN,['법이 정한 시설','임업용 관리사','작은 농업용 창고']),('일시사용허가',GOLD,['잠깐 쓰고 되돌림','자재 두기','임시 길'])],
      '지산드림 · 산지전용허가 뜻','허가 · 신고 · 일시사용, 무엇이 다른가','산지관리법 · 신고로 짓는 작은 농업용 창고는 대체산림자원조성비를 내지 않음',O+'jisandream_sanji_fig1.png')
# fig2 경사 기준
fig,ax=plt.subplots(figsize=(10.6,5.8)); fig.subplots_adjust(bottom=0.14,top=0.76,left=0.30,right=0.90)
rows=[('평균 경사도 · 법 기본',25,GREY,'25도'),('평균 경사도 · 가평군',30,GOLD,'30도'),('입목축적 · 법 기본',150,GREY,'평균의 150%'),('입목축적 · 가평군',180,GOLD,'평균의 180%')]
for i,(a,v,c,lab) in enumerate(rows):
    y=3-i; vv=v/30*100 if i<2 else v/180*100
    ax.barh(y,vv,color=c,height=0.55); ax.text(vv+2,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB); ax.text(-2,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
ax.set_xlim(0,135); ax.set_ylim(-0.6,3.6); ax.set_axis_off()
head(fig,'지산드림 · 산지전용허가 기준','가평군은 2025년 2월부터 넓혔습니다')
finish(fig,O+'jisandream_sanji_fig2.png','가평군 산지전용허가 기준 조례 2025년 2월 17일 공포 · 인구감소지역 특례',brand='지산드림',allow_outside=True,strict=False)
# fig3 비용 묶음 막대
import numpy as np
fig,ax=plt.subplots(figsize=(10.6,6.2)); fig.subplots_adjust(bottom=0.16,top=0.76,left=0.08,right=0.97)
areas=['200평','500평','1천 평']; data={'준보전산지':[550,1379,2757],'보전산지':[715,1792,3584],'제한지역':[1101,2757,5514]}
cs=[CYAN,GOLD,RED]; x=np.arange(3); w=0.26
for k,(n,v) in enumerate(data.items()):
    b=ax.bar(x+(k-1)*w,v,w,color=cs[k],label=n)
    for xx,vv in zip(x+(k-1)*w,v): ax.text(xx,vv+80,f'{vv:,}',ha='center',fontsize=13,color=DEEP,fontproperties=FB)
ax.set_xticks(x); ax.set_xticklabels(areas,fontproperties=FB,fontsize=17,color=DEEP)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.set_yticks([]); leg=ax.legend(prop=FB,fontsize=15,frameon=False,loc='upper left')
for t in leg.get_texts(): t.set_fontsize(15)
head(fig,'지산드림 · 산지전용허가 비용','대체산림자원조성비, 쓰는 넓이별 (만원)')
finish(fig,O+'jisandream_sanji_fig3.png','2026년 산림청 고시 ㎡당 8,340 · 10,840 · 16,680원 · 개별공시지가 몫은 따로 더함',brand='지산드림',allow_outside=True,strict=False)
# fig4 절차
fig,ax=plt.subplots(figsize=(10.6,5.0)); fig.subplots_adjust(bottom=0.12,top=0.74,left=0.02,right=0.98); ax.set_axis_off(); ax.set_xlim(0,18); ax.set_ylim(0,3)
steps=['서류 떼기','설계 맡기기','신청','돈 내기','허가 · 공사','준공 · 지목변경']
for i,s_ in enumerate(steps):
    x=0.2+i*3; c=GOLD if i==3 else DEEP
    ax.add_patch(FancyBboxPatch((x,0.9),2.5,1.3,boxstyle='round,pad=0.02,rounding_size=0.12',fc=c,ec=c))
    ax.text(x+1.25,1.75,str(i+1),ha='center',va='center',color='white',fontsize=18,fontproperties=FB)
    ax.text(x+1.25,1.25,s_,ha='center',va='center',color='white',fontsize=13.5,fontproperties=FB)
    if i<5: ax.annotate('',xy=(x+2.95,1.55),xytext=(x+2.55,1.55),arrowprops=dict(arrowstyle='->',color=GREY,lw=2.5))
head(fig,'지산드림 · 산지전용허가 받는법','서류에서 지목변경까지 여섯 단계')
finish(fig,O+'jisandream_sanji_fig4.png','집을 지을 때는 산지전용 · 개발행위 · 건축허가를 한 번에 넣는 경우가 많음',brand='지산드림',allow_outside=True,strict=False)
print('figs ok')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
FP='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; fm.fontManager.addfont(FP)
plt.rcParams['font.family']=fm.FontProperties(fname=FP).get_name()
NAVY='#1F3864'; BLUE='#2E5C8A'; GOLD='#C9A227'; GRAY='#B8C2CE'; BG='#FFFFFF'
def base(t,sub=None):
    f,ax=plt.subplots(figsize=(9,6),dpi=110); f.patch.set_facecolor(BG)
    f.text(0.05,0.93,t,fontsize=21,color=NAVY,weight='bold')
    if sub: f.text(0.05,0.87,sub,fontsize=13,color='#5A6675')
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.tick_params(left=False,labelleft=False,labelsize=14); return f,ax
def foot(f): f.text(0.05,0.03,'낭만 인테리어 · 문의 010-2882-8165',fontsize=12,color='#8A8578')
# 1 cheongso 기본: market bands + ours
f,ax=base('34평 입주청소, 37만 4천원은 어디쯤일까','올해 블로그에 적힌 입주청소 가격 · 34평 · 부가세 별도')
bands=[('저가 정찰',34,37,GRAY),('표준',41,51,'#9DB4CF'),('고급',54,68,'#6C8FB8')]
for i,(n,a,b,c) in enumerate(bands):
    ax.barh(i,b-a,left=a,color=c,height=0.55); ax.text(16,i,n,ha='left',va='center',fontsize=16,color=NAVY)
    ax.text(a-0.8 if i==0 else b+0.8,i,f'{a}~{b}만원',ha='right' if i==0 else 'left',va='center',fontsize=15,color=NAVY)
ax.axvline(37.4,color=GOLD,lw=3); ax.text(38,2.55,'우리 37만 4천원 · 정찰 금액에 탈거 청소',ha='left',fontsize=15,color='#8a6d00',weight='bold')
ax.set_xlim(16,82); ax.set_ylim(-0.6,3.2); ax.set_yticks([]); ax.set_xticks([])
foot(f); f.subplots_adjust(top=0.8,bottom=0.1,left=0.05); f.savefig('cs_market.png'); plt.close(f)
# 2 jinwi cheongso: 평형별 3가지
import numpy as np
f,ax=base('진위역 서희스타힐스 · 평형별 금액','청소만 · 새집증후군만 · 둘 다 하면(묶음) · 단위 만원')
L=['59㎡ (25평)','71㎡ (29평)','84㎡ (34평)']; c=[27.5,31.9,37.4]; s=[27.5,31.9,37.4]; b=[52.5,60.9,71.4]
x=np.arange(3); w=0.26
for k,(v,col,n) in enumerate([(c,BLUE,'청소만'),(s,GRAY,'새집증후군만'),(b,GOLD,'둘 다')]):
    bars=ax.bar(x+(k-1)*w,v,w,color=col,label=n)
    for r,val in zip(bars,v): ax.text(r.get_x()+r.get_width()/2,val+1,f'{val:g}',ha='center',fontsize=13,color=NAVY)
ax.set_xticks(x); ax.set_xticklabels(L,fontsize=14); ax.legend(frameon=False,fontsize=13,loc='upper left'); ax.set_ylim(0,82)
foot(f); f.subplots_adjust(top=0.8,bottom=0.15); f.savefig('jinwi_cs.png'); plt.close(f)
# 3 jinwi jungmun: 타입별 세대
f,ax=base('진위역 서희스타힐스 1,659세대','타입별 세대 수 · 같은 달에 현관 치수를 재는 집')
L=['59㎡','71㎡','84㎡']; v=[846,580,233]
bars=ax.bar(L,v,color=[BLUE,'#6C8FB8',GOLD],width=0.55)
for r,val in zip(bars,v): ax.text(r.get_x()+r.get_width()/2,val+15,f'{val}세대',ha='center',fontsize=16,color=NAVY)
ax.set_ylim(0,980); ax.tick_params(labelsize=16)
foot(f); f.subplots_adjust(top=0.8,bottom=0.12); f.savefig('jinwi_jm.png'); plt.close(f)
# 4 haerington timeline
f,ax=base('해링턴플레이스 · 박람회가 먼저 열립니다','가격은 박람회 전에 보고 가세요')
ev=[('11/13~15','입주 박람회'),('11/22~24','사전점검'),('2027년 2월','입주')]
ax.plot([0,2],[0,0],color=GRAY,lw=6,zorder=1)
for i,(d,n) in enumerate(ev):
    ax.scatter(i,0,s=900,color=[GOLD,BLUE,NAVY][i],zorder=2)
    ax.text(i,0.35,d,ha='center',fontsize=18,color=NAVY,weight='bold'); ax.text(i,-0.55,n,ha='center',fontsize=17,color='#333')
ax.text(0,-1.05,'▲ 이 날 전에 가격 확인',ha='center',fontsize=15,color='#8a6d00',weight='bold')
ax.set_xlim(-0.6,2.6); ax.set_ylim(-1.4,1); ax.axis('off')
foot(f); f.subplots_adjust(top=0.8,bottom=0.1); f.savefig('haer_tl.png'); plt.close(f)
# 5 geomdan types
f,ax=base('제일풍경채 검단 4차 · 타입별 세대','1,048세대 · 청소만 금액은 공급평수 × 1만 1천원')
L=['84A','84B','84C','110A','110B']; v=[481,191,98,140,138]
bars=ax.bar(L,v,color=[BLUE,BLUE,BLUE,GOLD,GOLD],width=0.55)
for r,val in zip(bars,v): ax.text(r.get_x()+r.get_width()/2,val+8,f'{val}',ha='center',fontsize=16,color=NAVY)
ax.set_ylim(0,560); ax.tick_params(labelsize=16)
ax.text(1,520,'84㎡ (34평) 청소만 37만 4천원',ha='center',fontsize=14,color=BLUE); 
foot(f); f.subplots_adjust(top=0.8,bottom=0.12); f.savefig('geomdan_types.png'); plt.close(f)

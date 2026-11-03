import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_jisan
O='/mnt/user-data/outputs/jisandream/'
LIGHT='#B9CEDB'; GOLD='#C9962E'

def head(fig,kick,title):
    fig.text(0.05,0.95,kick,fontsize=15,color=CYAN,ha='left',va='center')
    fig.text(0.05,0.875,title,fontsize=25,color=DEEP,fontproperties=FB,ha='left',va='center')

def hbar(rows,hi,kick,title,path,note,xmax,unit='만원',fmt='{:.1f}'):
    fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.12,top=0.78,left=0.30,right=0.93)
    n=len(rows); ys=list(range(n))[::-1]
    for y,(lab,v,cnt) in zip(ys,rows):
        c=CYAN if lab in hi else LIGHT
        ax.barh(y,v,color=c,height=0.58)
        ax.text(v+xmax*0.015,y,f'{fmt.format(v)}{unit}',va='center',ha='left',fontsize=21 if lab in hi else 17,color=DEEP if lab in hi else GREY,fontproperties=FB)
        ax.text(-xmax*0.02,y,lab,va='center',ha='right',fontsize=19,color=DEEP,fontproperties=FB)
        if cnt: ax.text(-xmax*0.02,y-0.33,cnt,va='center',ha='right',fontsize=13,color=GREY,fontproperties=FR)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
    head(fig,kick,title); finish(fig,O+path,note,brand='지산드림',allow_outside=True,strict=False)

# fig1 크기별
hbar([('1천~3천 평',7.0,'179건'),('3천~1만 평',3.9,'96건'),('1만~3만 평',1.6,'63건'),('3만 평 이상',1.2,'17건')],
     ['1만~3만 평','3만 평 이상'],'지산드림 · 가평 임야 실거래 2023년 1월~2026년 8월','가평 임야 평당 가격, 1만 평 넘으면 1만원대입니다',
     'jisandream_gpim_fig1.png','국토교통부 토지 실거래 · 가평군 지목 임야 · 지분·해제 거래 제외 · 계약면적 기준 평당 중간값',9.2)

# fig2 도로 유무
hbar([('도로가 붙은 땅',3.7,'14건'),('도로 없음 · 미기재',1.0,'66건')],['도로가 붙은 땅'],
     '지산드림 · 가평 임야 1만 평 이상 실거래','큰 산은 도로가 붙으면 3.7만원, 없으면 1.0만원입니다',
     'jisandream_gpim_fig2.png','국토교통부 토지 실거래 · 가평군 임야 1만 평 이상 · 2023년 1월~2026년 8월 · 도로조건은 신고 자료 기준',4.8)

# fig3 용도지역별
hbar([('자연녹지지역',15.0,'43건'),('계획관리지역',7.5,'79건'),('보전관리지역',7.4,'36건'),('농림지역',2.1,'187건')],['농림지역'],
     '지산드림 · 가평 임야 1,000평 이상 실거래','용도지역별 가평 임야, 농림지역이 평당 2.1만원으로 가장 쌉니다',
     'jisandream_gpim_fig3.png','국토교통부 토지 실거래 · 2023년 1월~2026년 8월 · 지분·해제 거래 제외 · 거래 5건 미만 용도지역 제외',18.5)

# fig4 임업 절차 flow
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.1,top=0.78,left=0.04,right=0.96); ax.set_axis_off()
steps=[('① 임야 취득','통째로 가진 땅\n차가 들어가는 길'),('② 임업인 조건','3ha 경영 · 연 90일\n연 120만원 · 조합원'),('③ 산림경영계획','군청 산림과 인가\n10년 계획'),('④ 임업경영체 등록','지방산림청\n신청서·임야대장'),('⑤ 혜택','임업직불금\n산림경영관리사')]
ax.set_xlim(0,10.6); ax.set_ylim(0,5)
for i,(t,s) in enumerate(steps):
    x=0.3+i*2.1; c=CYAN if i in (1,3) else DEEP
    ax.add_patch(FancyBboxPatch((x,2.1),1.8,1.9,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec='none'))
    ax.text(x+0.9,3.55,t,ha='center',va='center',fontsize=14.5,color='white',fontproperties=FB)
    ax.text(x+0.9,2.75,s,ha='center',va='center',fontsize=13,color='#DCE8F0',fontproperties=FR,linespacing=1.5)
    if i<4: ax.annotate('',xy=(x+2.1,3.05),xytext=(x+1.82,3.05),arrowprops=dict(arrowstyle='-|>',color=GREY,lw=2.5))
ax.text(5.3,1.3,'2ha 임야는 ②에서 90일 종사·판매액·조합원 길로 갑니다',ha='center',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.text(5.3,0.7,'임업직불금은 경영체 등록 이력 요건이 있어 새로 산 땅은 먼저 확인',ha='center',va='center',fontsize=14,color=GREY,fontproperties=FR)
head(fig,'지산드림 · 임업인이 되는 순서','임야 취득부터 임업직불금까지 다섯 단계입니다')
finish(fig,O+'jisandream_gpim_fig4.png','임업 및 산촌 진흥촉진에 관한 법률 시행령 제2조 · 산림청 임업직불금 통합포털 · 산지관리법 시행령 별표 3의3',brand='지산드림',allow_outside=True,strict=False)

# fig5 임업직불금 단가
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.14,top=0.78,left=0.27,right=0.95)
rows=[('임산물생산업 0.1~2ha',94),('임산물생산업 2~6ha',82),('임산물생산업 6~30ha',70),('육림업 3~10ha',62),('육림업 10~20ha',47),('육림업 20~30ha',32)]
n=len(rows)
for i,(lab,v) in enumerate(rows):
    y=n-1-i; c=CYAN if '임산물' in lab else DEEP
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+1.5,y,f'ha당 {v}만원',va='center',ha='left',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-2,y,lab,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
ax.set_xlim(0,118); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
ax.text(118,-0.55,'소규모임가직불금(0.1~0.5ha)은 가구당 130만원',ha='right',va='center',fontsize=14,color=GREY,fontproperties=FR)
head(fig,'지산드림 · 임업직불금 면적직불금 단가','임업직불금, 임산물생산업 ha당 94만원부터 육림업 32만원까지')
ax.set_xlim(-2,118); finish(fig,O+'jisandream_gpim_fig5.png','산림청 임업직불금 통합포털 제도 안내 · 송이 특화 단가는 별도 · 단가와 요건은 해마다 바뀜',brand='지산드림',allow_outside=True,strict=False)

render_jisan('지산드림 · 가평 임야와 임업인',['가평 임야 평당 가격','큰 산 1만원대 · 도로 붙으면 3.7만원'],'임업인 조건 · 임업직불금 · 산림경영관리사 한 글에',O+'jisandream_gpim_thumb.png')

# 산 104 fig: 3천~1만 평 비교
hbar([('도로가 붙은 땅',5.3,'18건'),('3천~1만 평 전체',3.9,'96건'),('도로 없음 · 미기재',3.8,'78건'),('이곡리 산 104 (호가)',4.0,'6m 임도')],['이곡리 산 104 (호가)'],
     '지산드림 · 가평 임야 3천~1만 평 실거래와 비교','이곡리 산 104 평당 4만원, 도로 있는 땅 중간값 5.3만원보다 낮습니다',
     'jisandream_igok104_fig1.png','국토교통부 토지 실거래 · 가평군 임야 3천~1만 평 · 2023년 1월~2026년 8월 · 지분·해제 제외 · 산 104는 매도 호가',6.6)
print('ok')

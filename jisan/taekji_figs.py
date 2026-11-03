src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/taekji/'
GOLD='#C9962E'; RED='#B5503C'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=5.8):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.76,left=left,right=0.93); n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off(); head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
hbar([('묶이기 전 석 달',172,GREY,'172건'),('묶인 동안',4,RED,'4건'),('풀린 뒤 석 달',71,CYAN,'71건')],230,
 '지산드림 · 하남 토지거래허가','2024년 감북 · 감일 · 감이 · 초이동 녹지 땅 계약','국토교통부 토지 실거래 · 이번 재지정은 2026.11.3~2029.11.2 (3년)',O+'jisandream_hanam_taekji_fig1.png',left=0.26)
hbar([('감북동',518,GOLD,'518만원'),('감이동',377,CYAN,'377만원'),('미사동',240,CYAN,'240만원'),('초이동',212,GREY,'212만원')],700,
 '지산드림 · 하남 신규택지 땅값','후보지 동네 그린벨트 밭 · 논 평당 중앙값','국토교통부 토지 실거래 · 2024.1~2026.8 · 개발제한구역 전 · 답 통째 거래',O+'jisandream_hanam_taekji_fig2.png',left=0.22)
print('figs')

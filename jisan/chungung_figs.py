src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/chungung/img/'
GOLD='#C9962E'; RED='#B5503C'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=5.6):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.13,top=0.77,left=left,right=0.93); n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off(); head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
hbar([('밭 · 논 전체',171,GOLD,'171만원 (13필지)'),('밭',138,CYAN,'138만원 (8필지)'),('논',211,CYAN,'211만원 (5필지)')],300,
 '지산드림 · 하남 토지 · 춘궁동','그린벨트 밭 · 논 평당 중앙값','국토교통부 토지 실거래 · 2024.1~2026.8 · 통째 거래 · 100~1,000평','/tmp/f2.png')
hbar([('도로에 붙은 땅',191,GOLD,'191만원 (6필지)'),('길이 없는 땅',134,GREY,'134만원 (7필지)')],280,
 '지산드림 · 하남 땅값 · 춘궁동','길이 붙으면 평당 57만원 더','국토교통부 토지 실거래 · 2024.1~2026.8 · 실거래 신고 도로 조건 기준','/tmp/f3.png',h=4.8)
print('ok')

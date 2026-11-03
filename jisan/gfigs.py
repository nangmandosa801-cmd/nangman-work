import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_jisan
O='/mnt/user-data/outputs/jisandream/'
M=['1월','2월','3월','4월','5월','6월','7월','8월']
def bars(vals,hi,kick,title,path,note,ymax):
    fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.17,top=0.78,left=0.05,right=0.97)
    cols=[CYAN if i==hi else '#B9CEDB' for i in range(8)]
    ax.bar(range(8),vals,color=cols,width=0.62)
    for i,v in enumerate(vals):
        ax.text(i,v+ymax*0.02,f'{v:,}',ha='center',va='bottom',fontsize=20 if i in (hi,hi-1) else 16,
                color=DEEP if i in (hi,hi-1) else GREY,fontproperties=FB)
    ax.set_xticks(range(8)); ax.set_xticklabels(M,color=DEEP)
    for l in ax.get_xticklabels(): l.set_fontproperties(FB); l.set_fontsize(19)
    ax.tick_params(axis='x',length=0,pad=8)
    ax.axvline(5.5,color=DEEP,lw=1.2,ls=(0,(4,3)))
    ax.text(5.42,ymax*0.99,'7월 1일 구리 규제',fontsize=15,color=DEEP,fontproperties=FB,va='top',ha='right')
    ax.set_ylim(0,ymax); ax.set_yticks([]); [s.set_visible(False) for k,s in ax.spines.items() if k!='bottom']
    ax.spines['bottom'].set_color(LINE)
    fig.text(0.05,0.95,kick,fontsize=15,color=CYAN,ha='left',va='center')
    fig.text(0.05,0.875,title,fontsize=25,color=DEEP,fontproperties=FB,ha='left',va='center')
    finish(fig,O+path,note,brand='지산드림')
bars([592,375,417,351,308,415,79,91],6,'지산드림 · 구리 아파트 매매 2026년','구리 아파트 매매, 6월 415건 → 7월 79건','jisandream_guri3m_fig1.png','국토교통부 아파트 매매 실거래 · 해제 거래 제외 · 8월은 9월 중순까지 신고분',680)
bars([61,57,67,87,86,116,141,73],6,'지산드림 · 별내 아파트 매매 2026년','별내동 아파트 매매, 7월 141건으로 올해 최다','jisandream_guri3m_fig2.png','남양주시 별내동 · 국토교통부 아파트 매매 실거래 · 해제 거래 제외 · 8월은 9월 중순까지 신고분',165)
# fig3 dumbbell 갈매 84
R=[('갈매역아이파크',8.49,8.835),('한라비발디',7.48,7.90),('구리갈매스타힐스',7.30,7.65),('갈매더샵나인힐스',7.27,7.58),('갈매6단지',7.25,7.375)]
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.12,top=0.78,left=0.05,right=0.95)
for i,(n,a,b) in enumerate(R):
    y=len(R)-1-i
    ax.plot([a,b],[y,y],color=LINE,lw=6,solid_capstyle='round',zorder=1)
    ax.scatter([a],[y],s=260,color='#B9CEDB',zorder=3); ax.scatter([b],[y],s=300,color=CYAN,zorder=3)
    ax.text(a-0.09,y,f'{a:.2f}억',ha='right',va='center',fontsize=16,color=GREY,fontproperties=FR)
    ax.text(b+0.09,y,f'{b:.2f}억',ha='left',va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(6.55,y,n,ha='right',va='center',fontsize=18,color=DEEP,fontproperties=FB,transform=ax.transData)
ax.set_xlim(4.9,9.5); ax.set_ylim(-0.7,len(R)-0.3); ax.set_axis_off()
ax.scatter([],[],s=160,color='#B9CEDB',label='규제 전 4~6월'); ax.scatter([],[],s=160,color=CYAN,label='규제 뒤 7~8월')
lg=ax.legend(loc='lower right',frameon=False)
for t in lg.get_texts(): t.set_fontproperties(FR); t.set_fontsize(17)
fig.text(0.05,0.95,'지산드림 · 구리 갈매동 아파트 시세 84㎡',fontsize=15,color=CYAN,ha='left',va='center')
fig.text(0.05,0.875,'규제 뒤에도 갈매동 84㎡는 올랐습니다',fontsize=25,color=DEEP,fontproperties=FB,ha='left',va='center')
finish(fig,O+'jisandream_guri3m_fig3.png','같은 단지·같은 전용면적 거래의 기간별 중간값 · 7~8월은 단지별 2~4건',brand='지산드림')
render_jisan('지산드림 · 구리 아파트 매매',['구리 아파트 매매','규제 뒤 415건→79건'],'옆 별내는 7월 141건 · 2026년 실거래',O+'jisandream_guri3m_thumb.png')
print('ok')

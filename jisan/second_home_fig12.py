src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/second_home/'
GRN='#2E7D50'; GRY='#8A8F96'
# fig1 가격 구간별 혜택
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.12,top=0.78,left=0.04,right=0.96)
ax.set_xlim(0,10); ax.set_ylim(0,6); ax.set_axis_off()
cols=[(0.2,'3억원 이하',['세컨드홈 특례 ○','취득세 50% 감면 ○'],CYAN),(3.5,'3억 넘고 4억 이하',['세컨드홈 특례 ○','취득세 감면 ✕'],LIGHT),(6.8,'4억원 넘음',['세컨드홈 특례 ✕','취득세 감면 ✕'],'#E3E6EA')]
for x,t,items,c in cols:
    ax.add_patch(FancyBboxPatch((x,0.5),3.0,4.6,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec='none'))
    tc='white' if c==CYAN else DEEP
    ax.text(x+1.5,4.45,t,ha='center',va='center',fontsize=22,color=tc,fontproperties=FB)
    for k,it in enumerate(items):
        ax.text(x+1.5,3.1-k*1.15,it.replace('○','').replace('✕','').strip(),ha='center',va='center',fontsize=18,color=tc,fontproperties=FB)
        ax.text(x+1.5,2.6-k*1.15,'됨' if '○' in it else '안 됨',ha='center',va='center',fontsize=17,color=tc if '○' in it else '#B5654E',fontproperties=FB)
head(fig,'지산드림 · 세컨드홈 특례 조건과 취득세 감면, 가평 집 가격별','세컨드홈 가평, 3억 이하 집은 특례와 감면을 함께 봅니다')
finish(fig,O+'jisandream_second_home_fig1.png','특례는 공시가격 4억 · 감면은 취득가액 3억 기준 · 2025.3.11 뒤 산 집 · 가평군청 안내',brand='지산드림',allow_outside=True,strict=False)
# fig2 매물 일곱 곳 매도가
rows=[('청평 삼회리','2,962평',2.4,GRN),('북면 이곡리 산 104','6,390평',2.55,GRY),('북면 이곡리','13,679평',5.47,GRY),('북면 이곡리','2만 평',7.0,GRY),('청평 호명리','1만 6천 평',8.0,GRN),('청평 호명리','3만 7천 평',14.85,GRN),('청평 상천리','4만 평',32.0,DEEP)]
fig,ax=plt.subplots(figsize=(10.6,8.2)); fig.subplots_adjust(bottom=0.17,top=0.80,left=0.27,right=0.93)
n=len(rows); ys=list(range(n))[::-1]; xmax=36
for y,(a,b,v,c) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    lab=f'{v:g}억' if v>=10 else (f'{v:g}억')
    ax.text(v+0.5,y,lab,va='center',fontsize=19,color=c if c!=GRY else GREY,fontproperties=FB)
    ax.text(-0.6,y+0.12,a,va='center',ha='right',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.6,y-0.28,b,va='center',ha='right',fontsize=13,color=GREY,fontproperties=FR)
ax.set_xlim(0,xmax); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
fig.text(0.27,0.115,'■ 집 짓기 땅',color=GRN,fontsize=15,fontproperties=FB); fig.text(0.46,0.115,'■ 보전관리 필지 확인',color=DEEP,fontsize=15,fontproperties=FB); fig.text(0.70,0.115,'■ 쉼터 · 임업',color=GRY,fontsize=15,fontproperties=FB)
head(fig,'지산드림 · 가평 전원주택 부지와 쉼터 땅 매물 일곱 곳','세컨드홈 가평, 2억대 집 지을 땅부터 32억 큰 산까지')
finish(fig,O+'jisandream_second_home_fig2.png','매도가 · 넓이는 각 매물 글 본문 그대로',brand='지산드림',allow_outside=True,strict=False)
print('ok')

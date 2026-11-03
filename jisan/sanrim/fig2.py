src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
O='/mnt/user-data/outputs/jisandream/sanrim/'
rows=[('청평 삼회리','2,962평',0.98),('북면 이곡리 산 104','6,390평',2.1),('북면 이곡리','13,679평',4.5),('청평 호명리','16,020평',5.3),('북면 이곡리','20,070평',6.6),('청평 호명리','37,124평',12.3),('청평 상천리','40,939평',13.5)]
fig,ax=plt.subplots(figsize=(10.6,8.2)); fig.subplots_adjust(bottom=0.10,top=0.80,left=0.27,right=0.93)
n=len(rows); ys=list(range(n))[::-1]; xmax=15.5
for y,(a,b,v) in zip(ys,rows):
    ok=v>=3; c=DEEP if ok else GREY
    ax.barh(y,v,color=c,height=0.6)
    ax.text(max(v,3.1)+0.25,y,f'{v}ha',va='center',fontsize=19,color=DEEP if ok else GREY,fontproperties=FB)
    ax.text(-0.3,y+0.12,a,va='center',ha='right',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.3,y-0.28,b,va='center',ha='right',fontsize=13,color=GREY,fontproperties=FR)
ax.axvline(3,color='#C9962E',ls='--',lw=2); ax.text(3,n-0.35,'3ha',ha='center',va='bottom',fontsize=16,color='#C9962E',fontproperties=FB)
ax.set_xlim(0,xmax); ax.set_ylim(-0.7,n); ax.set_axis_off()
head(fig,'가평 임야 매물 일곱 건 · 임업인 넓이 조건은 3ha 이상 산림에서 임업 경영','산림경영관리사 자격, 매물 다섯 건이 한 건으로 3ha를 넘습니다')
finish(fig,O+'jisandream_sanrim_gwanrisa_fig2.png','가평 임야 매물 일곱 건 가운데 4.5ha부터 13.5ha까지 다섯 건이 3ha를 넘습니다',brand='지산드림',allow_outside=True,strict=False)
print('ok')

exec(open('/home/claude/jisan/jcityfig.py').read())
exec(open('/home/claude/jisan/apt_figs.py').read().split('yrs=list(range(2018,2027))')[0].split("K='지산드림 · '")[1])
K='지산드림 · '
def mline2(yrs,series,kick,title,path,note,hl):
    fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.13,top=0.78,left=0.08,right=0.95)
    x=np.arange(len(yrs)); offs={'갈매':3200,'구리':-1200,'별내':-4200}
    for i,(nm,v) in enumerate(series):
        c=CYAN if nm==hl else (DEEP if i==1 else GREY); lw=4 if nm==hl else 2.2
        ax.plot(x,v,color=c,lw=lw,marker='o',ms=6 if nm==hl else 4)
        ax.text(x[-1]+0.15,v[-1]+offs.get(nm,0),f'{nm} {v[-1]/10000:.1f}억',va='center',fontsize=14,color=c,fontproperties=FB)
        j=int(np.argmax(v))
        if nm==hl: ax.text(x[j]-0.12,v[j]+3000,f'{v[j]/10000:.1f}억 (고점)',ha='right',fontsize=13,color=c,fontproperties=FB)
    lo=min(min(v) for _,v in series); hi_=max(max(v) for _,v in series)
    for i,y in enumerate(yrs): ax.text(x[i],lo-6000,str(y)[2:]+"'",ha='center',va='top',fontsize=12,color=GREY,fontproperties=FR)
    ax.set_xlim(-0.3,len(yrs)+1.1); ax.set_ylim(lo-16000,hi_+12000); ax.set_axis_off()
    head(fig,kick,title); finish(fig,O+path,note,brand='지산드림',allow_outside=True,strict=False)
yrs=list(range(2018,2027))
B=[44800,48700,60000,75400,75000,62000,63150,64000,69350]; G=[43000,49000,58000,75000,71650,65000,68000,71700,74000]; GM=[47000,52500,65800,81500,70400,65000,69900,72800,75000]
mline2(yrs,[('갈매',GM),('구리',G),('별내',B)],K+'84㎡ 매매 중앙값 · 2018~2026년 1~8월','갈매 아파트 84㎡ 7억 5천, 고점 8억 1,500만에서 7% 아래입니다','jisandream_galmae_apt_fig1.png','국토교통부 실거래 · 해제 거래 제외 · 전용 80~86㎡ · 갈매동은 2026년 7월부터 규제지역',hl='갈매')
hbar2([('갈매역아이파크 (2018)',8.58,'43건 · 전세 5.8억'),('구리갈매푸르지오 (2017)',8.08,'14건 · 전세 5.4억'),('한라비발디 (2016)',7.6,'29건 · 전세 5.45억'),('갈매와이시티 (2017)',7.58,'4건'),('구리갈매스타힐스 (2017)',7.39,'22건 · 전세 5.3억'),('갈매더샵나인힐스 (2016)',7.38,'19건 · 전세 5.5억'),('갈매6단지 (2018)',7.3,'16건 · 전세 5.5억')],
 ['갈매역아이파크 (2018)'],K+'갈매동 단지별 84㎡ 중앙값 · 2026년 3~8월','갈매 아파트 단지별, 8억 5,800만부터 7억 2,950만까지입니다','jisandream_galmae_apt_fig2.png','작은 글씨는 거래 건수 · 전세 중앙값(2026년 1~6월 신규) · 고점 대비 -3.5~-7.4%',10.5,unit='억')
# 구리 전세 금액대
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.14,top=0.78,left=0.08,right=0.95)
bands=['2억 미만','2억대','3억대','4억대','5억대','6억대','7억 이상']; n=[82,115,300,290,216,82,22]; a=['42㎡','59㎡','60㎡','85㎡','85㎡','85㎡','85㎡']
x=np.arange(7); ax.bar(x,n,0.62,color=[LIGHT,LIGHT,CYAN,CYAN,LIGHT,LIGHT,LIGHT])
for i in range(7): ax.text(x[i],n[i]+6,f'{n[i]}건',ha='center',fontsize=14,color=DEEP,fontproperties=FB); ax.text(x[i],-12,bands[i],ha='center',va='top',fontsize=13,color=DEEP,fontproperties=FB); ax.text(x[i],-40,'전용 '+a[i],ha='center',va='top',fontsize=11,color=GREY,fontproperties=FR)
ax.set_ylim(-70,360); ax.set_axis_off()
head(fig,K+'구리시 신규 전세 1,107건 · 2026년 1~6월 · 보증금 금액대','구리 아파트 전세, 3억대까지는 59㎡ 4억부터 84㎡입니다')
finish(fig,O+'jisandream_guri_jeonse_fig1.png','국토교통부 전월세 실거래 · 갱신 계약 제외 · 작은 글씨는 금액대별 전용면적 중앙값',brand='지산드림',allow_outside=True,strict=False)
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.14,top=0.78,left=0.10,right=0.95)
dongs=['토평동','갈매동','수택동','교문동','인창동']; e84=[5.9,5.5,5.35,5.3,4.6]; e59=[4.55,4.6,3.6,3.4,3.7]
x=np.arange(5); ax.bar(x-0.19,e84,0.36,color=CYAN); ax.bar(x+0.19,e59,0.36,color=LIGHT)
for i in range(5):
    ax.text(x[i]-0.19,e84[i]+0.08,f'{e84[i]:.2f}억'.replace('.00','').replace('0억','억'),ha='center',fontsize=13,color=DEEP,fontproperties=FB); ax.text(x[i]+0.19,e59[i]+0.08,f'{e59[i]:.2f}억'.replace('0억','억'),ha='center',fontsize=12,color=GREY,fontproperties=FB)
    ax.text(x[i],-0.25,dongs[i],ha='center',va='top',fontsize=15,color=DEEP,fontproperties=FB)
ax.text(4.4,6.9,'■ 84㎡',fontsize=13,color=CYAN,fontproperties=FB,ha='right'); ax.text(4.4,6.5,'■ 59㎡',fontsize=13,color=LIGHT,fontproperties=FB,ha='right')
ax.set_ylim(-0.9,7.3); ax.set_axis_off()
head(fig,K+'동별 전세 중앙값 · 2026년 1~6월 신규 계약','구리 전세 84㎡, 토평 5억 9천 갈매 5억 5천 인창 4억 6천입니다')
finish(fig,O+'jisandream_guri_jeonse_fig2.png','국토교통부 전월세 실거래 · 84㎡는 전용 80~86㎡, 59㎡는 55~62㎡ · 토평·교문은 59㎡가 인창 84㎡ 값',brand='지산드림',allow_outside=True,strict=False)
# 별내 오피스텔
hbar2([('이그제큐티브 92㎡ (2026)',255,'보증금 5천~1억 2,500 · 3건'),('힐스테이트 별내역 66㎡',190,'5천 · 55건'),('이그제큐티브 59㎡ (2026)',175,'7,500 · 10건'),('아이파크스위트 67㎡',170,'5천 · 86건'),('별내 자이엘라 60㎡',150,'3천 · 15건'),('별내자이 더 스타 48㎡',150,'3천 · 15건'),('메트로망 22㎡',55,'500 · 53건'),('백상앨리츠 24㎡',55,'500 · 75건'),('리치안위버 22㎡',53,'500 · 51건'),('스마트리치안 22㎡',52.5,'500 · 30건')],
 ['이그제큐티브 59㎡ (2026)','이그제큐티브 92㎡ (2026)'],K+'별내동 오피스텔 월세 중앙값 · 2026년 1~9월','별내 오피스텔 월세, 원룸 55만 투룸 170만 이그제큐티브 59㎡ 175만','jisandream_byeolnae_op_fig1.png','국토교통부 오피스텔 전월세 실거래 · 작은 글씨는 보증금 중앙값 · 거래 건수 · 월세 30만원 이상',300,unit='만원',fmt='{:.0f}')
render_jisan('갈매 아파트 시세',['84㎡ 7억 5천 · 고점 -7%','아이파크 8억 5,800만'],'전세 5억 5천 · 월세 1억에 180만 · 7월 규제 뒤 거래 4분의 1',O+'jisandream_galmae_apt_thumb.png')
render_jisan('구리 아파트 전세',['2억대 59㎡ 구축 · 4억대 84㎡','6억대 구리역·토평 신축'],'신규 전세 1,107건 금액대별 · 토평 5억 9천 인창 4억 6천',O+'jisandream_guri_jeonse_thumb.png')
render_jisan('별내 오피스텔 월세',['원룸 500에 55만 · 투룸 5천에 170만','이그제큐티브 59㎡ 7,500에 175만'],'별내역 오피스텔 669건 · 단지별 월세·전세·매매',O+'jisandream_byeolnae_op_thumb.png')
print('ok')

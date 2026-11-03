exec(open('/home/claude/jisan/gpimfigs.py').read().split('# fig1 크기별')[0])
import numpy as np, pandas as pd
WARN='#B5533C'
# fig1 연도별 거래·평당
yrs=list(range(2010,2027)); n=[1627,2284,1924,1806,1983,2594,2172,1991,1838,1838,2546,3453,2956,2440,2504,2361,1556]; py=[549,619,591,631,684,744,745,768,774,802,968,1131,1300,1300,1296,1198,1206]
fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.12,top=0.78,left=0.07,right=0.93)
x=np.arange(len(yrs))
ax.bar(x,n,0.65,color=[LIGHT if i<16 else CYAN for i in range(len(yrs))])
for i in [11,15,16]: ax.text(x[i],n[i]+60,f'{n[i]:,}건',ha='center',va='bottom',fontsize=13,color=DEEP,fontproperties=FB)
ax2=ax.twinx(); ax2.plot(x,py,color=DEEP,lw=3.2,marker='o',ms=6)
for i in [0,12,16]: ax2.text(x[i]+(0.5 if i==0 else 0),py[i]+45,f'{py[i]:,}만원',ha='center',va='bottom',fontsize=14,color=DEEP,fontproperties=FB)
for i,yv in enumerate(yrs):
    if i%2==0 and i<16: ax.text(x[i],-120,str(yv)[2:]+"'",ha='center',va='top',fontsize=12,color=GREY,fontproperties=FR)
ax.text(x[16],-120,"26'\n(1~8월)",ha='center',va='top',fontsize=11,color=GREY,fontproperties=FR,linespacing=1.3)
ax.set_ylim(-250,4200); ax2.set_ylim(0,1500); ax.set_axis_off(); ax2.set_axis_off()
ax.text(0.2,3900,'막대 = 거래 건수 · 선 = 평당 중앙값(전용)',fontsize=13,color=GREY,fontproperties=FR,va='top')
head(fig,'지산드림 · 경기 지식산업센터 실거래 37,873건 · 2010년 1월~2026년 8월','지식산업센터 시세 16년, 2.4배 오르고 고점에서 7% 내렸습니다')
finish(fig,O+'jisandream_jisan199_fig1.png','국토교통부 공장·창고 실거래 · 경기도 집합건물 공장 · 해제 거래 제외 · 2026년 8월은 신고 진행 중',brand='지산드림',allow_outside=True,strict=False)

# fig2 시군별 고점 대비
rows=[('성남',5.5,'612→350건'),('군포',-4.7,'206→72'),('수원',-6.4,'323→130'),('안산',-6.5,'353→127'),('시흥',-6.5,'267→153'),('부천',-6.8,'385→176'),('경기 전체',-7.2,'4,817→2,739'),('용인',-11.6,'520→194'),('하남',-13.2,'607→276'),('김포',-15.5,'173→49'),('안양',-15.8,'537→242'),('남양주',-25.3,'154→114')]
fig,ax=plt.subplots(figsize=(10.6,8.6)); fig.subplots_adjust(bottom=0.08,top=0.80,left=0.26,right=0.93)
m=len(rows); ys=list(range(m))[::-1]
for y,(lab,v,cnt) in zip(ys,rows):
    c=CYAN if v>0 else (DEEP if lab=='경기 전체' else (WARN if v<=-13 else LIGHT))
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+(0.5 if v>=0 else -0.5),y,f'{v:+.1f}%',va='center',ha='left' if v>=0 else 'right',fontsize=18 if lab in('성남','남양주','하남','경기 전체') else 15,color=DEEP if v>-13 else WARN,fontproperties=FB)
    ax.text(-34,y+0.12,lab,va='center',ha='right',fontsize=18,color=DEEP,fontproperties=FB); ax.text(-34,y-0.3,cnt,va='center',ha='right',fontsize=12,color=GREY,fontproperties=FR)
ax.axvline(0,color=LINE,lw=1.2); ax.set_xlim(-34,12); ax.set_ylim(-0.7,m-0.3); ax.set_axis_off()
head(fig,'지산드림 · 같은 건물 평당 중앙값 · 고점기(2021.7~2022.12) → 최근(2025.7~2026.8)','지식산업센터 하락, 남양주 -25% 하남 -13%인데 성남은 +5.5%입니다')
finish(fig,O+'jisandream_jisan199_fig2.png','읍면동·도로명·건축년도가 같은 건물 199개 · 작은 글씨는 고점기 → 최근 거래 건수 · 경기 전체 거래 43% 감소',brand='지산드림',allow_outside=True,strict=False)

# fig3 동별
rows=[('성남 상대원동',4.5,'581→325건'),('남양주 다산동',-3.6,'60→68'),('화성 영천동',-6.3,'51→298'),('구리 갈매동',-11.8,'14→41'),('하남 풍산동',-13.5,'319→143'),('안양 호계동',-13.5,'133→93'),('안양 관양동',-17.5,'204→55'),('하남 덕풍동',-21.1,'219→82'),('남양주 별내동',-32.7,'88→46')]
fig,ax=plt.subplots(figsize=(10.6,7.8)); fig.subplots_adjust(bottom=0.08,top=0.80,left=0.30,right=0.93)
m=len(rows); ys=list(range(m))[::-1]
for y,(lab,v,cnt) in zip(ys,rows):
    c=CYAN if v>0 else (WARN if v<=-20 else LIGHT)
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+(0.5 if v>=0 else -0.5),y,f'{v:+.1f}%',va='center',ha='left' if v>=0 else 'right',fontsize=17,color=DEEP if v>-20 else WARN,fontproperties=FB)
    ax.text(-44,y+0.12,lab,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB); ax.text(-44,y-0.3,cnt,va='center',ha='right',fontsize=12,color=GREY,fontproperties=FR)
ax.axvline(0,color=LINE,lw=1.2); ax.set_xlim(-44,10); ax.set_ylim(-0.7,m-0.3); ax.set_axis_off()
head(fig,'지산드림 · 동별 같은 건물 평당 중앙값 · 고점기 → 최근','별내 -33% · 미사(덕풍) -21% · 갈매 -12% · 상대원 +5%')
finish(fig,O+'jisandream_jisan199_fig3.png','갈매는 2023~2024년 입주 건물 첫 거래가 나오는 중 · 영천(동탄)은 최근 298건으로 경기에서 가장 활발 · 작은 글씨는 거래 건수',brand='지산드림',allow_outside=True,strict=False)

render_jisan('지산드림 · 경기 지식산업센터 실거래 37,873건',['지식산업센터 매매','고점보다 7% 내렸는데'],'별내 -33% · 하남 덕풍 -21% · 성남 상대원 +5% · 평균은 어디에도 없습니다',O+'jisandream_jisan199_thumb.png')
print('ok')

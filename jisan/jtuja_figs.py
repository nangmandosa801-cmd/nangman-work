src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
X='/mnt/user-data/outputs/jisandream/xi/'
O='/mnt/user-data/outputs/jisandream/jtuja/'
GOLD='#C9962E'; RED='#B5503C'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=6.4,xmin=0):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.76,left=left,right=0.93)
    n=len(rows); span=xmax-xmin
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55)
        ax.text((v if v>0 else 0)+span*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(xmin-span*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(xmin,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off()
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
hbar([('구리 갈매동',70,GOLD,'70%'),('하남 미사',38,CYAN,'38%'),('경기 전체',33,GREY,'33%'),('남양주 별내',20,CYAN,'20%'),('성남',19,CYAN,'19%')],
     95,'지산드림 · 지식산업센터 투자','2026년 매수자 가운데 개인 비율','국토교통부 공장 실거래 매수자 구분 · 2026년 1~8월',O+'jisandream_jisan_tuja_fig1.png')
hbar([('월세만 보면',4.8,GOLD,'연 4.8%'),('관리비 · 공실 · 재산세 빼면',3.5,CYAN,'3%대')],
     7.5,'지산드림 · 지식산업센터 투자 수익률','갈매 1억 160만원 호실, 월세 40만원이면','호실 가격은 갈매 35㎡ 이하 실거래 중앙값 · 3%대는 비용을 뺀 대략치',O+'jisandream_jisan_tuja_fig2.png',left=0.34,h=5.6)
# fig3 고점 대비
fig,ax=plt.subplots(figsize=(10.6,6.6)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.34,right=0.93)
rows=[('남양주 별내',-34,RED,'−34%'),('갈매 166번길 2022년',-29,RED,'−29%'),('하남 덕풍',-21,RED,'−21%'),('경기 199개 건물',-7,GREY,'−7%'),('성남 상대원',3,CYAN,'올랐음')]
for i,(a,v,c,lab) in enumerate(rows):
    y=len(rows)-1-i; ax.barh(y,abs(v),color=c,height=0.55); ax.text(abs(v)+0.6,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.6,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
ax.set_xlim(0,45); ax.set_ylim(-0.6,len(rows)-0.4); ax.set_axis_off()
head(fig,'지산드림 · 지식산업센터 투자 실패','고점보다 얼마나 내렸나, 전용 평당 중앙값')
finish(fig,O+'jisandream_jisan_tuja_fig3.png','지산드림이 국토교통부 실거래로 셈한 값 · 성남 상대원은 고점보다 오름',brand='지산드림',allow_outside=True,strict=False)
hbar([('영등포 2020년 뒤 건물',3851,DEEP,'3,851만원'),('자이타워 F-614',3874,GOLD,'3,874만원'),('영등포 신축 39건',3787,CYAN,'3,787만원'),('영등포 2009년 전 건물',2139,GREY,'약 2,140만원')],
     5000,'지산드림 · 지식산업센터 투자 전망','영등포 새 건물은 옛 건물의 1.8배','영등포 지식산업센터 2년 실거래 206건 · 전용 평당 · 자이타워는 분양금 그대로',O+'jisandream_jisan_tuja_fig4.png',left=0.33)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
def raw(n):
    im=Image.open(X+'jisandream_xi_tower_photo%d.png'%n).convert('RGB'); return im.crop((40,160,im.width-40,im.height-70))
p1=raw(1); p2=raw(2)
card(p1,'지식산업센터 투자 · 영등포 자이타워','F-614 전용 27.24평, 2026년 3월 준공',O+'jisandream_jisan_tuja_photo1.png')
card(p2,'지식산업센터 매매 · 코너 호실','두 면이 창 · 주차 법정 기준의 177%',O+'jisandream_jisan_tuja_photo2.png')
thumb([p1],'지산드림 · 경기 · 서울 지식산업센터','지식산업센터 투자','누가 사는 동네인가','갈매 개인 70% · 영등포 신축 평당 3,851만원',O+'jisandream_jisan_tuja_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'지식산업센터 투자',font=F2(52),fill=(255,226,63))
d.text((40,122),'그 건물 실거래 · 공실부터',font=F2(33),fill=(255,255,255))
d.text((40,170),'부가세 환급까지 계산해 드립니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_jisan_tuja_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='지식산업센터 투자, 갈매 개인 70% · 영등포 신축 전용 평당 3,851만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_jisan_tuja_banner_small.png')
print('ok')

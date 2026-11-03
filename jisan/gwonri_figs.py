src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/gwonri/'
GOLD='#C9962E'; RED='#B5503C'
# fig1 세 가지
fig,ax=plt.subplots(figsize=(10.6,6.2)); fig.subplots_adjust(bottom=0.10,top=0.76,left=0.03,right=0.97); ax.set_axis_off(); ax.set_xlim(0,15); ax.set_ylim(0,6)
for k,(t,c,items) in enumerate([('시설권리금',CYAN,['인테리어','주방 설비','간판 · 냉난방기']),('영업권리금',GOLD,['단골 · 거래처','장사 노하우','매출']),('바닥권리금',DEEP,['역 앞 · 코너','위치 덕에 드는 손님','업종 바꿔도 냄'])]):
    x=0.2+k*5
    ax.add_patch(FancyBboxPatch((x,0.2),4.6,5.5,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
    ax.add_patch(FancyBboxPatch((x,4.6),4.6,1.1,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c))
    ax.text(x+2.3,5.15,t,ha='center',va='center',fontsize=21,color='white',fontproperties=FB)
    for j,it in enumerate(items): ax.text(x+2.3,3.6-j*1.15,it,ha='center',va='center',fontsize=17,color=DEEP,fontproperties=FB)
head(fig,'지산드림 · 상가 권리금 뜻','앞 가게 사장에게 주는 돈, 세 가지')
finish(fig,O+'jisandream_gwonri_fig1.png','상가건물 임대차보호법 제10조의3 · 건물 주인에게 주는 돈이 아니라 돌려받지 못함',brand='지산드림',allow_outside=True,strict=False)
# fig2 세차장 사례 쌓은 막대
fig,ax=plt.subplots(figsize=(10.6,5.6)); fig.subplots_adjust(bottom=0.14,top=0.76,left=0.30,right=0.90)
ax.barh(1,3000,color=DEEP,height=0.5); ax.barh(1,500,left=3000,color=GOLD,height=0.5)
ax.barh(0,3000,color=DEEP,height=0.5)
ax.text(1500,1,'바닥 3,000만',ha='center',va='center',color='white',fontsize=16,fontproperties=FB)
ax.text(3250,1.42,'시설 500만',ha='center',va='center',color=GOLD,fontsize=15,fontproperties=FB)
ax.text(1500,0,'바닥 3,000만',ha='center',va='center',color='white',fontsize=16,fontproperties=FB)
ax.text(3560,1,'3,500만원',va='center',fontsize=18,color=DEEP,fontproperties=FB); ax.text(3060,0,'3,000만원',va='center',fontsize=18,color=DEEP,fontproperties=FB)
ax.text(-60,1,'같은 업종(세차)으로',ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB); ax.text(-60,0,'다른 업종으로',ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.set_xlim(0,4400); ax.set_ylim(-0.6,1.7); ax.set_axis_off()
head(fig,'지산드림 · 상가 권리금 계산','2022년 갈매동 세차장, 시설 · 바닥을 나눠 셈')
finish(fig,O+'jisandream_gwonri_fig2.png','지산드림 2022년 11월 갈매동 매물 글 그대로 · 전용 25평 · 보증금 1,000만 · 월세 170만원',brand='지산드림',allow_outside=True,strict=False)
# fig3 세금
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=6.0):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.76,left=left,right=0.93); n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off(); head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
hbar([('권리금',10000,GREY,'1억원'),('기타소득금액 (40%)',4000,CYAN,'4,000만원'),('떼는 세금 (22%)',880,RED,'880만원'),('받는 사람 손에',9120,GOLD,'9,120만원')],
     12500,'지산드림 · 상가 권리금 세금','개인사업자가 권리금 1억을 받으면','필요경비 60% · 원천징수 22%는 권리금의 8.8% · 부가세 10%는 따로 · 다음 해 5월 종합소득세 합산',O+'jisandream_gwonri_fig3.png',left=0.28)
# fig4 기간
fig,ax=plt.subplots(figsize=(10.6,5.4)); fig.subplots_adjust(bottom=0.14,top=0.76,left=0.05,right=0.95); ax.set_axis_off(); ax.set_xlim(0,20); ax.set_ylim(0,4)
ax.plot([0.5,19.5],[2,2],color=GREY,lw=3)
ax.add_patch(FancyBboxPatch((5,1.6),5,0.8,boxstyle='round,pad=0.02,rounding_size=0.1',fc=GOLD,ec=GOLD))
ax.add_patch(FancyBboxPatch((10.3,1.6),8.7,0.8,boxstyle='round,pad=0.02,rounding_size=0.1',fc=CYAN,ec=CYAN))
ax.text(7.5,2,'회수기회 보호',ha='center',va='center',color='white',fontsize=17,fontproperties=FB)
ax.text(14.65,2,'소송할 수 있는 3년',ha='center',va='center',color='white',fontsize=17,fontproperties=FB)
for x,t in [(5,'끝나기\n6개월 전'),(10.15,'계약\n끝나는 날'),(19,'3년 뒤')]:
    ax.plot([x,x],[1.4,2.6],color=DEEP,lw=2); ax.text(x,0.9,t,ha='center',va='center',fontsize=15,color=DEEP,fontproperties=FB)
ax.text(10,3.4,'이 기간에 건물 주인이 새 임차인을 막으면 배상',ha='center',fontsize=16,color=DEEP,fontproperties=FB)
head(fig,'지산드림 · 상가 권리금 회수기회 보호','언제부터 언제까지 지켜 주나')
finish(fig,O+'jisandream_gwonri_fig4.png','상가건물 임대차보호법 제10조의4 · 배상은 새 임차인이 주기로 한 권리금과 끝날 때 권리금 중 낮은 금액까지',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
G='/tmp/claude-0/-home-claude/cbfac2e5-e5d5-531e-ad5d-28b72a0f7fcf/scratchpad/gs/img/'
C='/mnt/user-data/outputs/jisandream/cafe/'
def cr(p): im=Image.open(p).convert('RGB'); return im.crop((40,160,im.width-40,im.height-70))
pg=cr(C+'jisandream_cafe_biyong_photo3.png')
pf=Image.open(G+'jisandream_firstar_photo2.png').convert('RGB')
print(pf.size)
card(pg,'상가 권리금 · 갈매 현대테라타워 1층 38평','권리금 0원 · 보증금 3천 · 월 250만원',O+'jisandream_gwonri_photo1.png')
card(pf,'상가 권리금 · 가산 하우스디 퍼스타 1층 105호','권리금 0원 · 보증금 3천 · 월 200만원',O+'jisandream_gwonri_photo2.png')
thumb([pg],'지산드림 · 갈매 · 가산 1층 상가','상가 권리금','0원인 1층 두 곳','받는 쪽은 1억이면 9,120만원',O+'jisandream_gwonri_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'상가 권리금',font=F2(52),fill=(255,226,63))
d.text((40,122),'권리금 0원 1층 두 곳',font=F2(33),fill=(255,255,255))
d.text((40,170),'계약서에 적을 내용까지 봐 드립니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_gwonri_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='상가 권리금, 갈매 38평 · 가산 11평은 권리금 0원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_gwonri_banner_small.png')
print('ok')

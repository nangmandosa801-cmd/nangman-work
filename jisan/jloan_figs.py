src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
X='/mnt/user-data/outputs/jisandream/xi/'
O='/mnt/user-data/outputs/jisandream/jloan/'
GOLD='#C9962E'; RED='#B5503C'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=6.4):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.76,left=left,right=0.93)
    n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55)
        ax.text(v+xmax*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off()
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
# fig1 두 갈래 표 그림
fig,ax=plt.subplots(figsize=(10.6,6.4)); fig.subplots_adjust(bottom=0.10,top=0.76,left=0.04,right=0.96); ax.set_axis_off()
ax.set_xlim(0,10); ax.set_ylim(0,6)
cols=[(0.2,'사업자 대출 (기업대출)',GOLD,['사업자등록한 회사 · 개인사업자','사옥 매입 · 사업 자금','담보인정비율 규제 직접 적용 안 됨','DSR 직접 적용 안 됨']),
      (5.2,'개인 가계대출',GREY,['사업자 아닌 개인','그 밖의 쓰임','비주택담보대출 70%','DSR 적용'])]
from matplotlib.patches import FancyBboxPatch
for x,t,c,items in cols:
    ax.add_patch(FancyBboxPatch((x,0.2),4.6,5.5,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
    ax.add_patch(FancyBboxPatch((x,4.7),4.6,1.0,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c))
    ax.text(x+2.3,5.2,t,ha='center',va='center',fontsize=20,color='white',fontproperties=FB)
    for k,it in enumerate(items):
        ax.text(x+2.3,3.9-k*1.0,it,ha='center',va='center',fontsize=16.5,color=DEEP,fontproperties=FB)
head(fig,'지산드림 · 지식산업센터 대출','누가 무엇에 쓰려고 빌리나')
finish(fig,O+'jisandream_jisan_loan_fig1.png','2021년 4월 가계부채 관리방안 · 사업자금으로 인정되면 기업대출 · 대표자 신용은 심사에 들어감',brand='지산드림',allow_outside=True,strict=False)
hbar([('금리 4%',8000,GOLD,'8,000만원'),('금리 4.5%',7111,CYAN,'7,111만원'),('금리 5%',6400,RED,'6,400만원')],
     10500,'지산드림 · 지식산업센터 대출 규제','월세 40만원 호실, 이자상환비율 1.5배로 빌릴 수 있는 돈','1년 월세 480만원 ÷ 1.5 = 1년 이자 320만원 · 월세 40만원과 금리는 계산 가정',O+'jisandream_jisan_loan_fig2.png',left=0.22,h=5.6)
hbar([('분양금 (부가세 포함)',108560,GREY,'10억 8,560만원'),('부가세 돌려받은 뒤',105542,DEEP,'10억 5,542만원'),('80%로 볼 때',84434,CYAN,'8억 4,434만원'),('70%로 볼 때',73879,GOLD,'7억 3,879만원')],
     140000,'지산드림 · 지식산업센터 대출 한도','영등포 자이타워 F-614 전용 27.24평','분양금은 매물 글 본문 그대로 · 70% · 80%는 가정 · 실제 한도는 감정가와 은행 심사',O+'jisandream_jisan_loan_fig3.png',left=0.30)
hbar([('금리 4%',246,CYAN,'월 246만원'),('금리 4.5%',277,GOLD,'월 277만원'),('금리 5%',308,RED,'월 308만원')],
     400,'지산드림 · 지식산업센터 대출 이자','7억 3,879만원 빌리면 한 달 이자','이자만 낼 때 · 원금을 같이 갚으면 달마다 내는 돈은 늘어남 · 금리는 가정',O+'jisandream_jisan_loan_fig4.png',left=0.22,h=5.6)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
def raw(n):
    im=Image.open(X+'jisandream_xi_tower_photo%d.png'%n).convert('RGB'); return im.crop((40,160,im.width-40,im.height-70))
p1=raw(1); p2=raw(2)
card(p1,'지식산업센터 대출 · 영등포 자이타워','F-614 전용 27.24평 · 회사가 쓰는 사옥',O+'jisandream_jisan_loan_photo1.png')
card(p2,'지식산업센터 대출 · 코너 호실','부가세 돌려받으면 10억 5,542만원',O+'jisandream_jisan_loan_photo2.png')
thumb([p2],'지산드림 · 영등포 · 갈매 지식산업센터','지식산업센터 대출','세 놓을까, 직접 쓸까','월세 40만원 호실 금리 5%면 6,400만원까지',O+'jisandream_jisan_loan_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'지식산업센터 대출',font=F2(52),fill=(255,226,63))
d.text((40,122),'세 놓을 호실은 월세 ÷ 1.5부터',font=F2(33),fill=(255,255,255))
d.text((40,170),'은행에 낼 서류까지 정리해 드립니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_jisan_loan_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='지식산업센터 대출, 세 놓으면 이자상환비율 1.5배 · 사옥은 사업자 대출'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_jisan_loan_banner_small.png')
print('ok')

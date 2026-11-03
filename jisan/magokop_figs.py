src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
G='/tmp/claude-0/-home-claude/cbfac2e5-e5d5-531e-ad5d-28b72a0f7fcf/scratchpad/mg/img/'
O='/mnt/user-data/outputs/jisandream/magokop/'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=6.4):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.76,left=left,right=0.93)
    n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+xmax*0.01,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off()
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
GOLD='#C9962E'
hbar([('30㎡ 미만 (원룸)',90.9,DEEP,'90.9% · 14,091건'),('30~44㎡',8.4,GREY,'8.4% · 1,299건'),('45~59㎡ (1.5룸 · 2룸)',0.3,GOLD,'0.3% · 39건 (르웨스트 31건)'),('60㎡ 넘음 (3룸)',0.5,GOLD,'0.5% · 70건 (르웨스트 63건)')],
     125,'지산드림 · 마곡 오피스텔','마곡 오피스텔 임대, 열에 아홉이 원룸','마곡동 오피스텔 전월세 2024.1~2026.6 · 15,499건',O+'jisandream_magok_op_fig1.png',left=0.32)
hbar([('르웨스트 1.5룸',5.6,GOLD,'5억 6,000만원'),('다른 오피스텔 46㎡급',3.2,GREY,'3억 2,000만원'),('르웨스트 2룸',7.5,CYAN,'7억 5,000만원')],
     9.5,'지산드림 · 마곡 오피스텔 전세','같은 1.5룸 크기, 르웨스트가 2억 4천 높습니다','국토교통부 전월세 실거래 중앙값 · 르웨스트 94건',O+'jisandream_magok_op_fig2.png')
hbar([('분양가 (45B)',8.37,DEEP,'8억 3,700만원'),('전세 중앙값 (1.5룸)',5.6,CYAN,'5억 6,000만원'),('전세 끼고 사면 (취득세 포함)',3.155,GOLD,'3억 1,550만원')],
     11,'지산드림 · 마곡 오피스텔 1.5룸','전세 끼고 사면 3억 1,550만원이 듭니다','취득세 4.6% 3,850만원 포함 · 전세는 호실마다 다름',O+'jisandream_magok_op_fig3.png')
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
def raw(n,crop=None):
    im=Image.open(G+'jisandream_lw_photo%d.png'%n).convert('RGB'); return im.crop(crop) if crop else im
p3=raw(1,(0,0,773,300)); p4=raw(4); p6=raw(6); p5=raw(3)
card(p3,'마곡 오피스텔 · 마곡 롯데캐슬 르웨스트','5개 동 876실, 2024년 8월 준공',O+'jisandream_magok_op_photo1.png')
card(p4,'마곡 오피스텔 1.5룸 · 열 개 타입','1.5룸 126실 · 2룸 39실 · 3룸 711실',O+'jisandream_magok_op_photo2.png')
card(p6,'마곡 오피스텔 1.5룸 · 실내','세탁기 · 건조기 · 인덕션까지 들어 있음',O+'jisandream_magok_op_photo3.png')
card(p5,'마곡 오피스텔 · 지하 연결','단지 지하 2층에서 마곡나루역 · 마곡역',O+'jisandream_magok_op_photo4.png')
thumb([p3],'지산드림 · 마곡 롯데캐슬 르웨스트','마곡 오피스텔 1.5룸','전세 5억 6천에 나갑니다','열에 아홉이 원룸인 마곡에서 · 8억 3,700만원부터',O+'jisandream_magok_op_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'마곡 오피스텔',font=F2(52),fill=(255,226,63))
d.text((40,122),'르웨스트 1.5룸 8억 3,700만원부터',font=F2(33),fill=(255,255,255))
d.text((40,170),'남은 호실 · 층 · 향 알려 드립니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_magok_op_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='마곡 오피스텔, 르웨스트 1.5룸 전세 5억 6천 · 8억 3,700만원부터'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_magok_op_banner_small.png')
print('ok')

import sys; sys.path.insert(0,'/home/claude'); from comic import *
from PIL import Image, ImageDraw
import os; os.chdir('/mnt/user-data/outputs/int/clip9')
C='/mnt/user-data/outputs/int/case04/'
def photo(im,f,x,y,w,h,label=None):
    p=Image.open(C+f).crop((0,0,780,905)); p=p.resize((w,int(w*905/780)))
    if p.height>h: p=p.crop((0,0,w,h))
    m=Image.new('L',p.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,p.width,p.height),36,fill=255)
    im.paste(p,(x,y),m); d=ImageDraw.Draw(im); d.rounded_rectangle((x,y,x+p.width,y+p.height),36,outline=NAVY,width=6)
    if label:
        d.rounded_rectangle((x+24,y+p.height-110,x+24+d.textlength(label,font=F(54))+50,y+p.height-24),26,fill=NAVY)
        d.text((x+49,y+p.height-104),label,font=F(54),fill=(255,255,255))
    return y+p.height
def save(im,n): im.save(f'y{n}.png')
# 1 이삿날
im,d=base()
caption(d,['이삿날,','냉장고가 안 들어가요'])
d.rectangle((560,520,720,1500),fill=FRAME); d.rectangle((580,540,700,1480),fill=GLASS)  # narrow door
d.rounded_rectangle((170,700,520,1500),30,fill=(225,228,232),outline=FRAME,width=8); d.line((170,980,520,980),fill=FRAME,width=6)
ctext(d,1080,'냉장고',F(60),NAVY,345)
person(d,860,1140,1.0,face='shock',shirt=WARN)
bubble(d,90,1560,900,200,['문이 너무 좁아요!'],size=64,fill=(255,243,196))
footer(d); save(im,1)
# 2 작은 문도 여세요
im,d=base()
caption(d,['작은 문 하나','더 여세요'])
yb=photo(im,'case04_03_both.jpg',140,380,800,1180,'두 짝을 다 연 모습')
person(d,900,1620,0.75,face='smile',shirt=NAVY,helmet=True)
bubble(d,90,1600,640,180,['통로가 넓어집니다'],size=52,fill=(234,243,238),c=OK,tail=((730,1660),(800,1690),(730,1720)))
footer(d); save(im,2)
# 3 평소엔 한 짝
im,d=base()
caption(d,['평소엔','큰 문 한 짝만'])
photo(im,'case04_01_open.jpg',140,380,800,1180,'큰 문만 연 모습')
ctext(d,1620,'작은 문은 고정해 두고',F(60),NAVY); ctext(d,1710,'이삿날에만 풉니다',F(60),WARN)
footer(d); save(im,3)
# 4 여는 법
im,d=base()
caption(d,['작은 문이','안 열린다면?'])
for i,(n,t,s) in enumerate([('1','큰 문을 먼저 열고',''),('2','작은 문 옆면·위아래','고정장치(플러시볼트)를 풉니다'),('3','기사에게','설치날 한 번 열어 보여 달라고')]):
    y=560+i*400
    d.ellipse((110,y,270,y+160),fill=NAVY); ctext(d,y+28,n,F(84),(255,255,255),190)
    d.text((310,y+10),t,font=F(64),fill=NAVY)
    if s: d.text((310,y+100),s,font=F(48,False),fill=SAND)
footer(d); save(im,4)
# 5 유리 + 간살
im,d=base()
caption(d,['큰 문은 유리','작은 문은 간살'])
photo(im,'case04_02_small.jpg',140,380,800,1080)
for i,t in enumerate(['블랙 초슬림 프레임','바닥 레일 없음']):
    ctext(d,1530+i*100,'· '+t,F(62),NAVY)
footer(d); save(im,5)
# 6 조심
im,d=base()
caption(d,['이런 집은','실측부터'])
rows=[('문 앞 공간이 좁다','도는 자리 필요',WARN),('열리는 쪽에 신발장','실측 필수',WARN),('고양이를 키운다','간살 간격 재기',WARN),('매일 두 짝을 연다','다른 방식 비교',MID)]
for i,(a,b,c) in enumerate(rows):
    y=520+i*300
    d.rounded_rectangle((70,y,1010,y+240),36,fill=(255,255,255),outline=c,width=7)
    d.text((115,y+30),a,font=F(62),fill=NAVY); d.text((115,y+130),'→ '+b,font=F(56),fill=c)
footer(d); save(im,6)
# 7 end
im,d=base(NAVY)
caption(d,['한 짝? 두 짝?','미닫이?'],c=(255,255,255))
for i,t in enumerate(['① 현관 정면 사진','② 입구 폭']):
    y=660+i*260
    d.rounded_rectangle((110,y,970,y+210),36,fill=(255,255,255))
    d.text((170,y+60),t,font=F(76),fill=NAVY)
ctext(d,1260,'두 가지만 보내 주시면',F(62),(240,190,40)); ctext(d,1350,'맞는 방식부터 봐 드립니다',F(62),(240,190,40))
ctext(d,1560,'양주 광사동 해동마을신도브래뉴',F(46,False),(210,220,235))
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235))
save(im,7)

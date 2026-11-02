import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image, ImageDraw
import os; os.chdir('/mnt/user-data/outputs/int/clip11')
C='/mnt/attach/outputs/int/case05/'
Y=(240,190,40)
def photo(im,f,x,y,w,h,label=None):
    p=Image.open(C+f).crop((18,18,762,1008)); p=p.resize((w,int(w*990/744)))
    if p.height>h: t=(p.height-h)//2; p=p.crop((0,t,w,t+h))
    m=Image.new('L',p.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,p.width,p.height),36,fill=255)
    im.paste(p,(x,y),m); d=ImageDraw.Draw(im); d.rounded_rectangle((x,y,x+p.width,y+p.height),36,outline=NAVY,width=6)
    if label:
        d.rounded_rectangle((x+24,y+p.height-110,x+24+d.textlength(label,font=F(54))+50,y+p.height-24),26,fill=NAVY)
        d.text((x+49,y+p.height-104),label,font=F(54),fill=(255,255,255))
    return y+p.height
def save(im,n): im.save(f's{n}.png')
BOX=(196,160,120)
# 1
im,d=base()
caption(d,['장 보고 왔는데','중문을 당겨야 해요'])
d.rectangle((600,560,860,1480),fill=FRAME); d.rectangle((620,580,840,1460),fill=GLASS)
d.ellipse((625,1000,655,1030),fill=NAVY)
person(d,380,960,1.05,face='worry',shirt=WARN)
d.rounded_rectangle((200,1150,560,1400),20,fill=BOX,outline=(150,115,85),width=6); d.line((200,1230,560,1230),fill=(150,115,85),width=5)
bubble(d,90,1560,900,200,['손이 없어요!'],size=80,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['양방향 스윙은','밀고 지나갑니다'])
photo(im,'case05_02_open_a.jpg',140,380,800,1180,'한쪽으로 연 모습')
ctext(d,1630,'어깨로 밀면 끝',F(80),WARN)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['반대쪽에서도','밀면 열립니다'])
photo(im,'case05_03_open_b.jpg',140,380,800,1180,'반대쪽으로 연 모습')
ctext(d,1630,'당길 일이 없습니다',F(80),OK)
footer(d); save(im,3)
# 4 damper
im,d=base()
caption(d,['손을 놓으면','천천히 가운데로'])
d.rectangle((150,1300,930,1320),fill=SAND)
d.rectangle((530,700,550,1300),fill=FRAME)
d.line((540,1300,300,850),fill=GLASS,width=26); d.line((540,1300,780,850),fill=GLASS,width=26)
d.arc((280,780,800,1820),235,265,fill=WARN,width=10); d.arc((280,780,800,1820),275,305,fill=WARN,width=10)
ctext(d,1400,'댐퍼가 속도를 잡아',F(66),NAVY); ctext(d,1500,'문이 쾅 닫히지 않습니다',F(66),NAVY)
ctext(d,1640,'고를 때 저절로 닫히는지 확인',F(56),WARN)
footer(d); save(im,4)
# 5 cost
im,d=base()
caption(d,['대신 이건','꼭 봐야 해요'])
rows=[('문이 도는 자리','현관 · 거실 양쪽 다'),('옆 가구','신발장 · 벤치와 부딪히나'),('틈 · 잠금','한방향보다 불리할 수 있음')]
for i,(a,b) in enumerate(rows):
    y=480+i*380
    d.rounded_rectangle((70,y,1010,y+320),40,fill=(255,255,255),outline=WARN,width=8)
    ctext(d,y+45,a,F(80),NAVY); ctext(d,y+180,b,F(60),WARN)
footer(d); save(im,5)
# 6 glass
im,d=base()
caption(d,['투명 유리를 쓴 건','너머를 보려고'])
photo(im,'case05_01_closed.jpg',140,380,800,1080,'블랙 프레임 · 6분할')
ctext(d,1530,'밀기 전에 반대편 사람이 보이고',F(58),NAVY); ctext(d,1630,'칸을 나눠 문이 눈에 띕니다',F(58),NAVY)
footer(d); save(im,6)
# 7 end
im,d=base(NAVY)
caption(d,['양방향? 한방향?','두 짝?'],c=(255,255,255))
for i,t in enumerate(['① 현관 사진','② 양쪽 가구 배치']):
    y=660+i*260
    d.rounded_rectangle((110,y,970,y+210),36,fill=(255,255,255))
    d.text((170,y+60),t,font=F(76),fill=NAVY)
ctext(d,1260,'두 가지만 보내 주시면',F(62),Y); ctext(d,1350,'돌릴 자리부터 봐 드립니다',F(62),Y)
ctext(d,1560,'양주 덕계동 현진에버빌',F(46,False),(210,220,235))
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235))
save(im,7)
D=[3.0,3.0,2.8,3.0,3.4,3.0,3.2]
assemble([f's{i}.png' for i in range(1,8)],D,'nangman_interior_swing2_short.mp4')
Image.open('s2.png').save('nangman_interior_swing2_cover.png')
ims=[Image.open(f's{i}.png').resize((270,480)) for i in range(1,8)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_s.png')
print(sum(D))

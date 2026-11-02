import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/int/clip_bm')
def footer(d): ctext(d,1830,'낭만 인테리어',F(40,False),SAND)
Y=(240,190,40); CAT=(230,150,70); SKY=(196,222,240)
def save(im,n): im.save(f'b{n}.png')
def cat(d,x,y,s=1.0):
    d.ellipse((x-int(70*s),y-int(40*s),x+int(70*s),y+int(45*s)),fill=CAT)
    d.ellipse((x+int(40*s),y-int(85*s),x+int(120*s),y-int(5*s)),fill=CAT)
    d.polygon([(x+int(48*s),y-int(65*s)),(x+int(58*s),y-int(110*s)),(x+int(80*s),y-int(78*s))],fill=CAT)
    d.polygon([(x+int(85*s),y-int(78*s)),(x+int(108*s),y-int(110*s)),(x+int(115*s),y-int(62*s))],fill=CAT)
    d.ellipse((x+int(62*s),y-int(55*s),x+int(72*s),y-int(43*s)),fill=HAIR); d.ellipse((x+int(90*s),y-int(55*s),x+int(100*s),y-int(43*s)),fill=HAIR)
    d.line((x-int(65*s),y,x-int(130*s),y-int(70*s)),fill=CAT,width=int(18*s))
def win(d,x,y,w,h,mesh=True,gap=0,torn=False):
    d.rectangle((x,y,x+w,y+h),fill=SKY,outline=FRAME,width=16)
    if mesh:
        mx=x+gap
        d.rectangle((mx,y+8,x+w-8,y+h-8),outline=(120,120,125),width=8)
        for gx in range(mx+26,x+w-8,34): d.line((gx,y+16,gx,y+h-16),fill=(150,150,155),width=4)
        for gy in range(y+34,y+h-8,34): d.line((mx+8,gy,x+w-16,gy),fill=(150,150,155),width=4)
    if torn:
        d.polygon([(x+w//2-60,y+h//2-70),(x+w//2+20,y+h//2-10),(x+w//2-40,y+h//2+80),(x+w//2-90,y+h//2)],fill=SKY)
# 1
im,d=base((238,240,236))
caption(d,['방충망 닫아 두면','괜찮지 않나요?'])
win(d,230,520,620,560)
cat(d,420,1260,1.15)
person(d,860,1180,0.72,face='o',shirt=MID)
bubble(d,60,1560,760,210,['닫아 뒀는데요'],size=68,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['일반 방충망은','벌레 막는 제품입니다'],size=72)
d.rounded_rectangle((70,500,1010,880),44,fill=(255,255,255),outline=WARN,width=10)
ctext(d,560,'고양이 추락 방지용으로',F(70),NAVY)
ctext(d,660,'만든 것이 아닙니다',F(78),WARN)
ctext(d,1000,'그래서 두 가지가 생깁니다',F(62),NAVY)
cat(d,420,1420,1.0)
footer(d); save(im,2)
# 3
im,d=base((238,240,236))
caption(d,['하나, 망이','손상될 수 있습니다'],c=WARN,size=72)
win(d,230,500,620,560,torn=True)
ctext(d,1140,'발톱이 걸리면 벌어집니다',F(64),NAVY)
ctext(d,1250,'작은 구멍이 이미 있으면 더 쉽게',F(54,False),SAND)
cat(d,400,1600,0.95)
footer(d); save(im,3)
# 4
im,d=base((238,240,236))
caption(d,['둘, 틀이','빠질 수 있습니다'],c=WARN,size=72)
win(d,230,500,620,560,gap=170)
d.line((240,540,400,1010),fill=WARN,width=16)
ctext(d,1140,'레일에 끼우는 방식이 많습니다',F(62),NAVY)
ctext(d,1250,'이탈방지 부품이 없으면 밀렸을 때 빠집니다',F(50,False),SAND)
person(d,540,1560,0.72,face='shock',shirt=MID)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['방묘창은 망 하나가','아닙니다'],size=72)
for i,(n,t,c) in enumerate([('망','발톱에 찢어지지 않을 것',MID),('프레임','밀어도 빠지지 않을 것',WARN),('창틀 고정','모서리에 틈이 없을 것',OK)]):
    y=480+i*300
    d.rounded_rectangle((70,y,1010,y+250),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+34,n,F(74),c); ctext(d,y+134,t,F(56),NAVY)
    if i<2: ctext(d,y+262,'↓',F(44),SAND)
ctext(d,1470,'셋이 같이 버텨야 합니다',F(66),NAVY)
footer(d); save(im,5)
# 6
im,d=base()
caption(d,['망이 강해도','프레임이 빠지면'])
ctext(d,560,'소용없습니다',F(130),WARN)
d.rounded_rectangle((70,800,1010,1120),44,fill=(255,255,255),outline=Y,width=10)
ctext(d,860,'교체형을 고르실 때는',F(58),NAVY)
ctext(d,950,'이탈방지 부품이 들어가는지',F(64),WARN)
ctext(d,1030,'먼저 확인하십시오',F(64),WARN)
cat(d,420,1520,1.0)
footer(d); save(im,6)
# 7
im,d=base()
caption(d,['설치 전에','꼭 볼 네 군데'])
for i,(a,b) in enumerate([('끝까지 덮였나','위아래 끝과 양옆 모서리까지'),('빠지지 않나','몸으로 밀었을 때 틀이 빠지는지'),('망이 버티나','긁고 매달려도 늘어나지 않는지'),('창 옆 가구','캣타워·소파처럼 뛰어오를 곳')]):
    y=440+i*270
    d.rounded_rectangle((70,y,1010,y+225),36,fill=(255,255,255),outline=MID,width=8)
    ctext(d,y+28,a,F(64),NAVY); ctext(d,y+118,b,F(50),SAND)
footer(d); save(im,7)
# 8
im,d=base(NAVY)
caption(d,['어떤 망을 쓸까보다','밀어도 안 빠지느냐'],c=(255,255,255),size=78)
ctext(d,640,'망 · 프레임 · 창틀 고정',F(84),Y)
ctext(d,770,'셋을 같이 보십시오',F(68),(255,255,255))
cat(d,400,1160,1.05)
ctext(d,1420,'현관까지 같이 막으실 분은',F(52,False),(210,220,235))
ctext(d,1500,'현관 사진을 보내 주시면 봐 드립니다',F(52,False),(210,220,235))
ctext(d,1740,'낭만 인테리어',F(48),(210,220,235))
save(im,8)
D=[3.2,3.4,3.4,3.6,3.8,3.6,3.8,3.4]
assemble([f'b{i}.png' for i in range(1,9)],D,'int_bangmyochang_short.mp4')
Image.open('b5.png').save('int_bangmyochang_cover.png')
ims=[Image.open(f'b{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_b.png')
print('ok')

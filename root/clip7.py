from PIL import Image, ImageDraw, ImageFont
import math
W,H=1080,1920
FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; FBo='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F(s,b=True): return ImageFont.truetype(FB if b else FBo,s,index=1)
NAVY=(31,56,100); MID=(46,92,138); WARN=(181,101,78); IV=(247,245,240); OK=(60,122,90); SAND=(138,133,120); SKIN=(248,215,185); HAIR=(60,45,40); GLASS=(205,225,238); FRAME=(90,90,95)
def base(bg=IV):
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); return im,d
def ctext(d,y,t,f,c,x=W//2):
    w=d.textlength(t,font=f); d.text((x-w/2,y),t,font=f,fill=c)
def caption(d,lines,y=110,c=NAVY,size=76):
    for i,l in enumerate(lines): ctext(d,y+i*(size+22),l,F(size),c)
def footer(d): ctext(d,1830,'낭만 인테리어',F(40,False),SAND)
def bubble(d,x,y,w,h,lines,size=58,tail=None,fill=(255,255,255),c=NAVY):
    d.rounded_rectangle((x,y,x+w,y+h),40,fill=fill,outline=NAVY,width=6)
    if tail: d.polygon([tail[0],tail[1],tail[2]],fill=fill,outline=NAVY); d.line([tail[0],tail[2]],fill=fill,width=10)
    tot=len(lines)*(size+14)
    for i,l in enumerate(lines): ctext(d,y+(h-tot)/2+i*(size+14)-6,l,F(size),c,x+w/2)
def person(d,x,y,s=1.0,hair=HAIR,shirt=MID,face='o',helmet=False):
    r=int(70*s)
    d.rounded_rectangle((x-int(95*s),y+r+10,x+int(95*s),y+r+int(260*s)),int(60*s),fill=shirt)
    d.ellipse((x-r,y-r,x+r,y+r),fill=SKIN)
    if helmet: d.pieslice((x-r-8,y-r-18,x+r+8,y+r-10),180,360,fill=(240,190,40)); d.rectangle((x-r-14,y-12,x+r+14,y-2),fill=(240,190,40))
    else: d.pieslice((x-r,y-r-6,x+r,y+r-20),180,360,fill=hair)
    e=int(22*s)
    if face=='shock':
        d.ellipse((x-e-12,y-8,x-e+12,y+16),fill=(255,255,255),outline=HAIR,width=4); d.ellipse((x+e-12,y-8,x+e+12,y+16),fill=(255,255,255),outline=HAIR,width=4)
        d.ellipse((x-14,y+28,x+14,y+56),fill=HAIR)
    else:
        d.ellipse((x-e-7,y-2,x-e+7,y+12),fill=HAIR); d.ellipse((x+e-7,y-2,x+e+7,y+12),fill=HAIR)
        if face=='smile': d.arc((x-26,y+14,x+26,y+48),10,170,fill=HAIR,width=6)
        elif face=='worry': d.arc((x-22,y+34,x+22,y+60),200,340,fill=HAIR,width=6)
        else: d.line((x-18,y+36,x+18,y+36),fill=HAIR,width=6)
def door(d,x,y,w,h,panels=3):
    d.rectangle((x-20,y-40,x+w+20,y),fill=FRAME)  # rail
    pw=w//panels
    for i in range(panels):
        px=x+i*pw
        d.rectangle((px,y,px+pw-6,y+h),fill=FRAME); d.rectangle((px+14,y+14,px+pw-20,y+h-14),fill=GLASS)
def save(im,n): im.save(f'd{n}.png')
# 1 쾅
im,d=base((40,44,60))
caption(d,['밤 11시,','중문이 쾅!'],c=(255,255,255))
door(d,140,1000,800,700)
for a in range(0,360,30):
    r1,r2=210,330; cx,cy=540,760
    d.line((cx+r1*math.cos(math.radians(a)),cy+r1*math.sin(math.radians(a)),cx+r2*math.cos(math.radians(a)),cy+r2*math.sin(math.radians(a))),fill=(240,190,40),width=12)
ctext(d,650,'쾅!!',F(190),(240,190,40))
person(d,830,1450,1.0,face='shock',shirt=WARN)
bubble(d,90,1330,560,230,['어제까진','스르륵 닫혔는데'],size=54,tail=((640,1450),(730,1470),(640,1510)))
footer(d); save(im,1)
# 2 통째로?
im,d=base()
caption(d,['문을 통째로','바꿔야 하나?'])
person(d,330,900,1.2,face='worry',shirt=WARN)
d.rounded_rectangle((560,760,960,1320),40,fill=(40,44,60)); d.rounded_rectangle((585,800,935,1280),20,fill=(255,255,255))
ctext(d,880,'중문 교체',F(52),NAVY,760); ctext(d,980,'견적',F(52),NAVY,760); ctext(d,1090,'???만원',F(70),WARN,760)
bubble(d,120,1440,840,200,['잠깐, 부품 하나일 수 있어요'],size=56,fill=(255,243,196))
footer(d); save(im,2)
# 3 위를 보세요
im,d=base()
caption(d,['문짝 말고','위를 보세요'])
door(d,120,700,620,900,2)
d.ellipse((150,560,470,760),outline=WARN,width=12)
ctext(d,590,'댐퍼',F(64),WARN,310)
person(d,880,1150,1.0,face='smile',shirt=NAVY,helmet=True)
bubble(d,480,1660,560,150,['낭만 기사'],size=50,fill=NAVY,c=(255,255,255))
footer(d); save(im,3)
# 4 핀이 빠졌네요
im,d=base()
caption(d,['핀이 걸쇠에서','빠졌네요'])
d.rounded_rectangle((120,650,960,1150),30,fill=(225,228,232),outline=FRAME,width=8)
ctext(d,690,'문짝 위 확대',F(48,False),SAND)
d.rounded_rectangle((200,820,640,960),25,fill=FRAME); ctext(d,850,'댐퍼',F(60),(255,255,255),420)
d.ellipse((700,850,780,930),fill=WARN); ctext(d,960,'빠진 핀',F(50),WARN,720)
d.rectangle((870,800,930,1000),fill=NAVY); ctext(d,1010,'걸쇠',F(46),NAVY,900)
bubble(d,120,1260,840,300,['안 깨졌으면','다시 걸면 끝'],size=68,fill=(234,243,238),c=OK)
footer(d); save(im,4)
# 5 다른 경우
im,d=base()
caption(d,['증상마다','볼 곳이 다릅니다'])
rows=[('갑자기 쾅','댐퍼 핀',OK),('닫힌 뒤 튕김','스토퍼',WARN),('기름 자국','댐퍼 교체',WARN),('걸리고 소리','레일 · 롤러',MID)]
for i,(a,b,c) in enumerate(rows):
    y=560+i*300
    d.rounded_rectangle((80,y,1000,y+240),36,fill=(255,255,255),outline=c,width=7)
    d.text((130,y+70),a,font=F(66),fill=NAVY); w=d.textlength(b,font=F(66)); d.text((950-w,y+70),b,font=F(66),fill=c)
footer(d); save(im,5)
# 6 보는 순서
im,d=base()
caption(d,['보는 순서'])
steps=['댐퍼','스토퍼','레일 줄','롤러']
for i,s in enumerate(steps):
    y=470+i*310
    d.ellipse((150,y,330,y+180),fill=NAVY); ctext(d,y+40,str(i+1),F(90),(255,255,255),240)
    d.text((390,y+40),s,font=F(96),fill=NAVY)
    if i<3: d.polygon([(225,y+200),(255,y+200),(240,y+270)],fill=SAND)
footer(d); save(im,6)
# 7 사진 세 장
im,d=base(NAVY)
caption(d,['사진 세 장만','보내 주세요'],c=(255,255,255))
for i,t in enumerate(['① 문 전체','② 레일 끝 스토퍼','③ 문짝 위 댐퍼']):
    y=620+i*250
    d.rounded_rectangle((110,y,970,y+200),36,fill=(255,255,255))
    d.text((170,y+55),t,font=F(72),fill=NAVY)
ctext(d,1450,'핀만 걸면 되는지',F(60),(240,190,40)); ctext(d,1540,'먼저 봐 드립니다',F(60),(240,190,40))
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235))
save(im,7)

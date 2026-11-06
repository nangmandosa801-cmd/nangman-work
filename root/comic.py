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

# ── 강아지 캐릭터 (10/9 20:49 사용자 「강아지 매트 숏폼 … 강아지 캐릭터 넣어서」) ──
FUR=(236,196,138); FURD=(176,122,74); INK=(60,45,40); TONGUE=(232,110,120); CHEEK=(244,160,150)
def dog(d,x,y,s=1.0,face='happy',fur=FUR,ear=FURD,slip=False,collar=(181,101,78)):
    """귀가 처진 강아지 — face: happy · worry · shock · sleep · love. slip=True면 다리가 벌어지고 미끄러지는 선"""
    S=lambda v:int(v*s)
    by=y+S(150)
    # 몸통 · 다리
    if slip:
        for dx,ang in((-95,-40),(-40,-15),(40,15),(95,40)):
            lx=x+S(dx); d.line((lx,by+S(40),lx+S(ang*1.8),by+S(150)),fill=fur,width=S(36))
            d.ellipse((lx+S(ang*1.8)-S(22),by+S(132),lx+S(ang*1.8)+S(22),by+S(168)),fill=fur)
        for k in range(3): d.line((x-S(260)-S(k*30),by+S(60)+S(k*35),x-S(170)-S(k*30),by+S(60)+S(k*35)),fill=(200,195,185),width=S(10))
    else:
        for dx in(-80,-30,30,80):
            d.rounded_rectangle((x+S(dx)-S(20),by+S(40),x+S(dx)+S(20),by+S(150)),S(18),fill=fur)
    d.ellipse((x-S(150),by-S(60),x+S(150),by+S(110)),fill=fur)
    d.ellipse((x+S(120),by-S(110),x+S(190),by-S(20)),fill=fur)  # 꼬리
    # 머리
    r=S(120)
    d.ellipse((x-r,y-r,x+r,y+r),fill=fur)
    d.ellipse((x-r-S(40),y-S(80),x-r+S(45),y+S(90)),fill=ear); d.ellipse((x+r-S(45),y-S(80),x+r+S(40),y+S(90)),fill=ear)
    d.ellipse((x-S(70),y+S(10),x+S(70),y+S(105)),fill=(250,230,200))  # 주둥이
    d.ellipse((x-S(22),y+S(18),x+S(22),y+S(48)),fill=INK)  # 코
    d.rounded_rectangle((x-S(80),y+S(105),x+S(80),y+S(130)),S(10),fill=collar)
    ex=S(48); ey=y-S(25)
    if face=='sleep':
        for sx in(-1,1): d.arc((x+sx*ex-S(20),ey-S(8),x+sx*ex+S(20),ey+S(16)),200,340,fill=INK,width=S(8))
    elif face=='shock':
        for sx in(-1,1): d.ellipse((x+sx*ex-S(20),ey-S(20),x+sx*ex+S(20),ey+S(20)),fill=(255,255,255),outline=INK,width=S(6)); d.ellipse((x+sx*ex-S(7),ey-S(7),x+sx*ex+S(7),ey+S(7)),fill=INK)
        d.ellipse((x-S(16),y+S(60),x+S(16),y+S(96)),fill=INK)
    elif face=='love':
        for sx in(-1,1):
            cx=x+sx*ex; d.ellipse((cx-S(18),ey-S(14),cx,ey+S(4)),fill=TONGUE); d.ellipse((cx,ey-S(14),cx+S(18),ey+S(4)),fill=TONGUE); d.polygon([(cx-S(18),ey-S(4)),(cx+S(18),ey-S(4)),(cx,ey+S(20))],fill=TONGUE)
    else:
        for sx in(-1,1): d.ellipse((x+sx*ex-S(15),ey-S(15),x+sx*ex+S(15),ey+S(15)),fill=INK); d.ellipse((x+sx*ex-S(6),ey-S(10),x+sx*ex+S(2),ey-S(2)),fill=(255,255,255))
    if face in('happy','love'):
        d.arc((x-S(36),y+S(40),x,y+S(80)),20,160,fill=INK,width=S(6)); d.arc((x,y+S(40),x+S(36),y+S(80)),20,160,fill=INK,width=S(6))
        d.rounded_rectangle((x-S(16),y+S(66),x+S(16),y+S(104)),S(14),fill=TONGUE)
        for sx in(-1,1): d.ellipse((x+sx*S(85)-S(16),y+S(25),x+sx*S(85)+S(16),y+S(45)),fill=CHEEK)
    elif face=='worry':
        d.arc((x-S(28),y+S(66),x+S(28),y+S(96)),200,340,fill=INK,width=S(6))
        for sx in(-1,1): d.line((x+sx*S(30),ey-S(42),x+sx*S(70),ey-S(30)),fill=INK,width=S(7))
        d.ellipse((x+S(105),y-S(70),x+S(135),y-S(25)),fill=(150,200,235))

# ── 귀여운 강아지 2판 (10/9 20:54 사용자 「더 귀엽고 깜찍하게 · 다양한 재미있는 상황」) ──
# 머리가 크고 몸이 작은 2등신 · 반짝이는 큰 눈 · 볼터치 · 외곽선 · 포즈(sit · run · slip · jump · sleep · roll · sink)와 소품
OUTL=(92,62,40)
def _ell(d,b,fill,w=6): d.ellipse(b,fill=fill,outline=OUTL,width=w)
def cdog(d,x,y,s=1.0,face='happy',pose='sit',fur=FUR,ear=FURD,tilt=0):
    S=lambda v:int(v*s); w=max(3,S(6))
    # 몸 · 다리 (머리 중심 x,y · 몸은 아래)
    bx,byy=x,y+S(150)
    if pose=='sleep':
        _ell(d,(x-S(170),y+S(60),x+S(170),y+S(190)),fur,w)
        _ell(d,(x+S(130),y+S(70),x+S(200),y+S(120)),fur,w)
    elif pose=='roll':
        _ell(d,(x-S(130),y+S(70),x+S(130),y+S(200)),(250,232,205),w)
        for dx,dy in((-90,-10),(-40,-40),(40,-40),(90,-10)):
            _ell(d,(x+S(dx)-S(24),y+S(70)+S(dy)-S(30),x+S(dx)+S(24),y+S(70)+S(dy)+S(18)),fur,w)
    else:
        _ell(d,(bx-S(110),byy-S(30),bx+S(110),byy+S(130)),fur,w)
        _ell(d,(bx-S(55),byy+S(10),bx+S(55),byy+S(110)),(250,232,205),0)  # 배
        if pose in('run','jump'):
            legs=[(-95,60,-150,95),(-50,80,-70,140),(50,80,80,140),(95,60,150,95)]
            for x1,y1,x2,y2 in legs: d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=OUTL,width=S(40)); d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=fur,width=S(28))
            for x1,y1,x2,y2 in legs: _ell(d,(bx+S(x2)-S(20),byy+S(y2)-S(16),bx+S(x2)+S(20),byy+S(y2)+S(16)),fur,w)
        elif pose=='slip':
            for x2,y2 in((-190,150),(-90,170),(90,170),(190,150)):
                d.line((bx+S(x2)//3,byy+S(80),bx+S(x2),byy+S(y2)),fill=OUTL,width=S(40)); d.line((bx+S(x2)//3,byy+S(80),bx+S(x2),byy+S(y2)),fill=fur,width=S(28))
                _ell(d,(bx+S(x2)-S(22),byy+S(y2)-S(16),bx+S(x2)+S(22),byy+S(y2)+S(16)),fur,w)
        elif pose=='sink':
            d.rectangle((bx-S(160),byy+S(95),bx+S(160),byy+S(150)),fill=(200,215,230))
        else:
            for dx in(-70,-25,25,70): _ell(d,(bx+S(dx)-S(24),byy+S(90),bx+S(dx)+S(24),byy+S(140)),fur,w)
        # 꼬리 (흔들림 선)
        _ell(d,(bx+S(95),byy-S(70),bx+S(150),byy-S(5)),fur,w)
        if face in('happy','love'):
            for k in(0,1): d.arc((bx+S(140)+S(k*22),byy-S(95)-S(k*10),bx+S(190)+S(k*22),byy-S(35)-S(k*10)),300,60,fill=OUTL,width=max(2,S(5)))
    # 머리 (크게)
    r=S(135); hy=y-(S(20) if pose=='sleep' else 0)
    if pose in('sleep',): hx=x-S(60)
    else: hx=x
    _ell(d,(hx-S(95)-r//2-S(30),hy-S(60),hx-S(95)+S(10),hy+S(110)),ear,w)   # 왼귀
    _ell(d,(hx+S(95)-S(10),hy-S(60),hx+S(95)+r//2+S(30),hy+S(110)),ear,w)  # 오른귀
    _ell(d,(hx-r,hy-r,hx+r,hy+r-S(10)),fur,w)
    _ell(d,(hx-S(60),hy+S(20),hx+S(60),hy+S(100)),(252,238,214),0)  # 주둥이
    _ell(d,(hx-S(20),hy+S(22),hx+S(20),hy+S(50)),INK,0)              # 코
    d.ellipse((hx-S(10),hy+S(26),hx-S(2),hy+S(33)),fill=(255,255,255))
    ex=S(58); ey=hy-S(18)
    if face=='sleep' or pose=='sleep':
        for sx in(-1,1): d.arc((hx+sx*ex-S(24),ey-S(10),hx+sx*ex+S(24),ey+S(22)),20,160,fill=INK,width=S(8))
        d.text((hx+S(120),hy-S(190)),'Z',font=F(S(70)),fill=MID); d.text((hx+S(180),hy-S(250)),'z',font=F(S(50)),fill=MID)
    elif face=='shock':
        for sx in(-1,1): d.ellipse((hx+sx*ex-S(30),ey-S(30),hx+sx*ex+S(30),ey+S(30)),fill=(255,255,255),outline=INK,width=S(6)); d.ellipse((hx+sx*ex-S(10),ey-S(10),hx+sx*ex+S(10),ey+S(10)),fill=INK)
        d.ellipse((hx-S(16),hy+S(60),hx+S(16),hy+S(98)),fill=INK)
    elif face=='dizzy':
        for sx in(-1,1):
            cx=hx+sx*ex; d.line((cx-S(18),ey-S(18),cx+S(18),ey+S(18)),fill=INK,width=S(8)); d.line((cx-S(18),ey+S(18),cx+S(18),ey-S(18)),fill=INK,width=S(8))
        d.arc((hx-S(26),hy+S(62),hx+S(26),hy+S(92)),200,340,fill=INK,width=S(6))
    elif face=='love':
        for sx in(-1,1):
            cx=hx+sx*ex; d.ellipse((cx-S(26),ey-S(20),cx+S(2),ey+S(6)),fill=TONGUE); d.ellipse((cx-S(2),ey-S(20),cx+S(26),ey+S(6)),fill=TONGUE); d.polygon([(cx-S(25),ey-S(4)),(cx+S(25),ey-S(4)),(cx,ey+S(28))],fill=TONGUE)
    else:  # happy · worry · sniff · proud
        for sx in(-1,1):
            cx=hx+sx*ex; d.ellipse((cx-S(26),ey-S(30),cx+S(26),ey+S(26)),fill=INK)
            d.ellipse((cx-S(14),ey-S(22),cx+S(2),ey-S(6)),fill=(255,255,255)); d.ellipse((cx+S(6),ey+S(4),cx+S(14),ey+S(12)),fill=(255,255,255))
        if face=='angry':
            for sx in(-1,1): d.line((hx+sx*S(20),ey-S(34),hx+sx*S(85),ey-S(62)),fill=INK,width=S(9))
            d.arc((hx-S(26),hy+S(64),hx+S(26),hy+S(94)),200,340,fill=INK,width=S(7))
            anger(d,hx+S(120),hy-S(120),s)
        elif face=='worry':
            for sx in(-1,1): d.line((hx+sx*S(30),ey-S(52),hx+sx*S(80),ey-S(40)),fill=INK,width=S(7))
            d.arc((hx-S(24),hy+S(66),hx+S(24),hy+S(92)),200,340,fill=INK,width=S(6))
            _ell(d,(hx+S(120),hy-S(80),hx+S(150),hy-S(30)),(150,200,235),0)
        else:
            d.arc((hx-S(34),hy+S(44),hx,hy+S(78)),20,160,fill=INK,width=S(6)); d.arc((hx,hy+S(44),hx+S(34),hy+S(78)),20,160,fill=INK,width=S(6))
            if face!='sniff': d.rounded_rectangle((hx-S(15),hy+S(66),hx+S(15),hy+S(104)),S(14),fill=TONGUE)
            if face=='proud':
                for k,(px,py) in enumerate(((-160,-150),(150,-170),(190,-60))): star(d,hx+S(px),hy+S(py),S(26),(240,190,40))
    for sx in(-1,1): d.ellipse((hx+sx*S(92)-S(22),hy+S(30),hx+sx*S(92)+S(22),hy+S(56)),fill=CHEEK)
    d.rounded_rectangle((x-S(70),hy+S(118),x+S(70),hy+S(142)),S(10),fill=(181,101,78))  # 목걸이
    d.ellipse((x-S(14),hy+S(132),x+S(14),hy+S(160)),fill=(240,190,40))           # 방울
def star(d,x,y,r,c):
    pts=[]
    for i in range(10):
        a=math.pi/2+i*math.pi/5; rr=r if i%2==0 else r*0.45
        pts.append((x+rr*math.cos(a),y-rr*math.sin(a)))
    d.polygon(pts,fill=c,outline=OUTL)
def floor(d,y,kind='tile',x0=0,x1=1080):
    if kind=='tile':
        d.rectangle((x0,y,x1,y+260),fill=(226,232,238))
        for gx in range(x0,x1,180): d.line((gx,y,gx-60,y+260),fill=(200,208,216),width=4)
        for k in range(3): d.line((x0+120+k*300,y+40,x0+200+k*300,y+20),fill=(255,255,255),width=10)  # 반짝
    elif kind=='mat':
        d.rectangle((x0,y,x1,y+260),fill=(214,190,160))
        for gx in range(x0,x1,150): d.line((gx,y,gx,y+260),fill=(196,170,138),width=3)
    elif kind=='matwhite':
        d.rectangle((x0,y,x1,y+260),fill=(240,236,228))
        for gx in range(x0,x1,150): d.line((gx,y,gx,y+260),fill=(220,214,204),width=3)
def sofa(d,x,y,s=1.0):
    S=lambda v:int(v*s)
    d.rounded_rectangle((x,y,x+S(380),y+S(150)),S(30),fill=(120,150,190),outline=OUTL,width=5)
    d.rounded_rectangle((x+S(20),y-S(90),x+S(360),y+S(30)),S(30),fill=(140,170,205),outline=OUTL,width=5)
def boom(d,x,y,text,size=70,c=WARN):
    pts=[]
    for i in range(16):
        a=i*math.pi/8; rr=150 if i%2==0 else 105
        pts.append((x+rr*math.cos(a)*1.4,y+rr*math.sin(a)))
    d.polygon(pts,fill=(255,236,140),outline=OUTL); ctext(d,y-size//2-8,text,F(size),c,x)
def speed(d,x,y,n=4,ln=180,c=(190,184,172)):
    for k in range(n): d.line((x-ln-k*25,y+k*38,x-k*25,y+k*38),fill=c,width=10)
def box(d,x,y,s=1.0,label=''):
    S=lambda v:int(v*s)
    d.rectangle((x,y,x+S(180),y+S(150)),fill=(214,170,110),outline=OUTL,width=5); d.line((x,y+S(40),x+S(180),y+S(40)),fill=OUTL,width=4)
    if label: ctext(d,y+S(70),label,F(S(40)),OUTL,x+S(90))
def sample(d,x,y,s=1.0,c=(214,190,160)):
    S=lambda v:int(v*s)
    d.rounded_rectangle((x,y,x+S(220),y+S(60)),S(10),fill=c,outline=OUTL,width=5)
def hand(d,x,y,s=1.0):
    S=lambda v:int(v*s)
    d.rounded_rectangle((x,y,x+S(150),y+S(80)),S(36),fill=SKIN,outline=OUTL,width=5)
    d.rectangle((x+S(150),y+S(10),x+S(330),y+S(70)),fill=MID,outline=OUTL,width=5)

# ── 귀여운 고양이 (10/9 21:20 사용자 「고양이 캐릭터도 좋을 듯」) ──
# 2등신 · 세모 귀 · 수염 · ω 입 · 줄무늬 · 포즈(sit · run · jump · land · slip · loaf · sleep)
CATF=(246,176,96); CATD=(214,128,58); CATW=(255,244,228)
def _tri(d,pts,fill,w): d.polygon(pts,fill=fill,outline=OUTL,width=w)
def ccat(d,x,y,s=1.0,face='happy',pose='sit',fur=CATF,stripe=CATD):
    S=lambda v:int(v*s); w=max(3,S(6)); bx,byy=x,y+S(150)
    def tail(x0,y0,x1,y1,x2,y2):
        d.line((x0,y0,x1,y1,x2,y2),fill=OUTL,width=S(38),joint='curve'); d.line((x0,y0,x1,y1,x2,y2),fill=fur,width=S(26),joint='curve')
        d.line((x1+(x2-x1)//2,y1+(y2-y1)//2-S(8),x1+(x2-x1)//2+S(4),y1+(y2-y1)//2+S(10)),fill=stripe,width=S(8))
    if pose in('loaf','sleep'):
        tail(bx+S(150),byy+S(110),bx+S(220),byy+S(60),bx+S(190),byy+S(10))
        _ell(d,(bx-S(170),byy-S(20),bx+S(170),byy+S(130)),fur,w)
        for dx in(-60,0,60): d.line((bx+S(dx),byy-S(16),bx+S(dx)+S(10),byy+S(30)),fill=stripe,width=S(12))
        for dx in(-60,20): _ell(d,(bx+S(dx)-S(30),byy+S(100),bx+S(dx)+S(30),byy+S(135)),CATW,w)
    else:
        if pose in('run','jump'):
            tail(bx-S(100),byy+S(40),bx-S(190),byy-S(20),bx-S(230),byy-S(120))
        elif pose=='slip':
            tail(bx+S(100),byy+S(60),bx+S(200),byy-S(40),bx+S(170),byy-S(160))
        else:
            tail(bx+S(90),byy+S(110),bx+S(190),byy+S(80),bx+S(200),byy-S(40))
        _ell(d,(bx-S(100),byy-S(30),bx+S(100),byy+S(130)),fur,w)
        _ell(d,(bx-S(50),byy+S(10),bx+S(50),byy+S(110)),CATW,0)
        for dx in(-80,80): d.line((bx+S(dx),byy+S(10),bx+S(dx)+(S(14) if dx>0 else -S(14)),byy+S(60)),fill=stripe,width=S(12))
        if pose=='jump':   # 앞발을 쭉 뻗고 붕 뜸
            for x1,y1,x2,y2 in((-60,60,-160,-30),(60,60,160,-30),(-50,110,-110,190),(50,110,110,190)):
                d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=OUTL,width=S(38)); d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=fur,width=S(26))
                _ell(d,(bx+S(x2)-S(20),byy+S(y2)-S(16),bx+S(x2)+S(20),byy+S(y2)+S(16)),CATW,w)
        elif pose=='run':
            for x1,y1,x2,y2 in((-80,60,-150,100),(-40,90,-60,150),(40,90,70,150),(80,60,150,100)):
                d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=OUTL,width=S(38)); d.line((bx+S(x1),byy+S(y1),bx+S(x2),byy+S(y2)),fill=fur,width=S(26))
                _ell(d,(bx+S(x2)-S(20),byy+S(y2)-S(15),bx+S(x2)+S(20),byy+S(y2)+S(15)),CATW,w)
        elif pose=='slip':
            for x2,y2 in((-190,150),(-90,170),(90,170),(190,150)):
                d.line((bx+S(x2)//3,byy+S(80),bx+S(x2),byy+S(y2)),fill=OUTL,width=S(38)); d.line((bx+S(x2)//3,byy+S(80),bx+S(x2),byy+S(y2)),fill=fur,width=S(26))
                _ell(d,(bx+S(x2)-S(22),byy+S(y2)-S(15),bx+S(x2)+S(22),byy+S(y2)+S(15)),CATW,w)
        elif pose=='land':   # 사뿐 착지 · 다리 벌림
            for dx in(-110,-40,40,110): _ell(d,(bx+S(dx)-S(26),byy+S(95),bx+S(dx)+S(26),byy+S(140)),CATW,w)
        else:
            for dx in(-60,-20,20,60): _ell(d,(bx+S(dx)-S(22),byy+S(95),bx+S(dx)+S(22),byy+S(140)),CATW,w)
    # 머리
    r=S(130); hx=x-(S(70) if pose in('loaf','sleep') else 0); hy=y+(S(40) if pose in('loaf','sleep') else 0)
    for sx in(-1,1):   # 세모 귀
        _tri(d,[(hx+sx*S(120),hy-S(40)),(hx+sx*S(115),hy-S(185)),(hx+sx*S(35),hy-S(110))],fur,w)
        d.polygon([(hx+sx*S(105),hy-S(65)),(hx+sx*S(105),hy-S(150)),(hx+sx*S(55),hy-S(105))],fill=(250,190,190))
    _ell(d,(hx-r-S(10),hy-r,hx+r+S(10),hy+r-S(15)),fur,w)
    for dx in(-30,0,30): d.line((hx+S(dx),hy-r+S(8),hx+S(dx),hy-r+S(48)),fill=stripe,width=S(10))
    _ell(d,(hx-S(55),hy+S(25),hx+S(55),hy+S(95)),CATW,0)
    d.polygon([(hx-S(13),hy+S(30)),(hx+S(13),hy+S(30)),(hx,hy+S(45))],fill=(232,120,130))
    ex=S(58); ey=hy-S(10)
    for sx in(-1,1):   # 수염
        for k in(-1,0,1): d.line((hx+sx*S(70),hy+S(55)+S(k*12),hx+sx*S(165),hy+S(45)+S(k*24)),fill=INK,width=max(2,S(4)))
    if face=='sleep' or pose=='sleep':
        for sx in(-1,1): d.arc((hx+sx*ex-S(24),ey-S(10),hx+sx*ex+S(24),ey+S(22)),20,160,fill=INK,width=S(8))
        d.text((hx+S(120),hy-S(200)),'Z',font=F(S(70)),fill=MID); d.text((hx+S(180),hy-S(260)),'z',font=F(S(50)),fill=MID)
    elif face=='shock':
        for sx in(-1,1): d.ellipse((hx+sx*ex-S(30),ey-S(30),hx+sx*ex+S(30),ey+S(30)),fill=(255,255,255),outline=INK,width=S(6)); d.ellipse((hx+sx*ex-S(9),ey-S(9),hx+sx*ex+S(9),ey+S(9)),fill=INK)
        d.ellipse((hx-S(14),hy+S(55),hx+S(14),hy+S(88)),fill=INK)
    elif face=='dizzy':
        for sx in(-1,1):
            cx=hx+sx*ex; d.line((cx-S(18),ey-S(18),cx+S(18),ey+S(18)),fill=INK,width=S(8)); d.line((cx-S(18),ey+S(18),cx+S(18),ey-S(18)),fill=INK,width=S(8))
        d.arc((hx-S(24),hy+S(58),hx+S(24),hy+S(86)),200,340,fill=INK,width=S(6))
    elif face=='love':
        for sx in(-1,1):
            cx=hx+sx*ex; d.ellipse((cx-S(26),ey-S(20),cx+S(2),ey+S(6)),fill=TONGUE); d.ellipse((cx-S(2),ey-S(20),cx+S(26),ey+S(6)),fill=TONGUE); d.polygon([(cx-S(25),ey-S(4)),(cx+S(25),ey-S(4)),(cx,ey+S(28))],fill=TONGUE)
    elif face=='smug':   # 실눈 · 만족
        for sx in(-1,1): d.arc((hx+sx*ex-S(26),ey-S(4),hx+sx*ex+S(26),ey+S(30)),200,340,fill=INK,width=S(8))
    else:  # happy · worry · proud · sniff
        for sx in(-1,1):
            cx=hx+sx*ex; d.ellipse((cx-S(24),ey-S(32),cx+S(24),ey+S(26)),fill=INK)
            d.ellipse((cx-S(13),ey-S(24),cx+S(3),ey-S(8)),fill=(255,255,255)); d.ellipse((cx+S(6),ey+S(4),cx+S(13),ey+S(11)),fill=(255,255,255))
        if face=='angry':
            for sx in(-1,1): d.line((hx+sx*S(18),ey-S(36),hx+sx*S(82),ey-S(64)),fill=INK,width=S(9))
            anger(d,hx+S(125),hy-S(130),s)
        if face=='worry':
            for sx in(-1,1): d.line((hx+sx*S(30),ey-S(55),hx+sx*S(80),ey-S(42)),fill=INK,width=S(7))
            _ell(d,(hx+S(125),hy-S(80),hx+S(155),hy-S(30)),(150,200,235),0)
        if face=='proud':
            for px,py in((-170,-160),(160,-180),(200,-60)): star(d,hx+S(px),hy+S(py),S(26),(240,190,40))
    if face=='angry':
        d.arc((hx-S(24),hy+S(52),hx+S(24),hy+S(80)),200,340,fill=INK,width=S(6))
    elif face not in('shock','dizzy'):   # ω 입
        d.arc((hx-S(30),hy+S(40),hx,hy+S(70)),20,160,fill=INK,width=S(6)); d.arc((hx,hy+S(40),hx+S(30),hy+S(70)),20,160,fill=INK,width=S(6))
    for sx in(-1,1): d.ellipse((hx+sx*S(95)-S(22),hy+S(22),hx+sx*S(95)+S(22),hy+S(48)),fill=CHEEK)
    if pose not in('loaf','sleep'):
        d.rounded_rectangle((x-S(65),hy+S(108),x+S(65),hy+S(130)),S(10),fill=(90,140,200))
        d.ellipse((x-S(13),hy+S(120),x+S(13),hy+S(146)),fill=(240,190,40))
def tower(d,x,y,s=1.0):
    """캣타워 — x 가운데 · y 바닥선"""
    S=lambda v:int(v*s); POST=(222,200,170); PAD=(150,110,90)
    d.rectangle((x-S(30),y-S(560),x+S(30),y),fill=POST,outline=OUTL,width=5)
    for k in range(10): d.line((x-S(30),y-S(560)+S(k*56),x+S(30),y-S(540)+S(k*56)),fill=(196,170,138),width=3)
    for (dx,dy,ww) in((0,0,260),(-60,-300,220),(40,-560,240)):
        d.rounded_rectangle((x+S(dx)-S(ww//2),y+S(dy)-S(30),x+S(dx)+S(ww//2),y+S(dy)+S(10)),S(10),fill=PAD,outline=OUTL,width=5)

# ── 너구리 공인중개사 (10/9 21:28 낭만 부동산 유튜브용 · 다른 캐릭터) ──
# 회색 털 · 눈가 검은 띠 · 둥근 귀 · 줄무늬 꼬리 · 동그란 안경 · 남색 조끼와 빨간 넥타이 · 포즈(stand · point · key · worry · cheer)
RAC=(168,164,160); RACD=(88,82,80); RACL=(236,232,226); VEST=(40,64,110); TIE=(196,70,60)
def racc(d,x,y,s=1.0,face='happy',pose='stand'):
    S=lambda v:int(v*s); w=max(3,S(6)); bx,byy=x,y+S(150)
    # 꼬리 (줄무늬)
    for k in range(4):
        c=RAC if k%2==0 else RACD
        _ell(d,(bx+S(80)+S(k*28),byy+S(20)-S(k*40),bx+S(170)+S(k*28),byy+S(90)-S(k*40)),c,w)
    # 몸 · 조끼 · 넥타이
    _ell(d,(bx-S(105),byy-S(30),bx+S(105),byy+S(135)),RAC,w)
    d.polygon([(bx-S(95),byy+S(10)),(bx-S(20),byy-S(20)),(bx-S(30),byy+S(120)),(bx-S(80),byy+S(100))],fill=VEST)
    d.polygon([(bx+S(95),byy+S(10)),(bx+S(20),byy-S(20)),(bx+S(30),byy+S(120)),(bx+S(80),byy+S(100))],fill=VEST)
    d.polygon([(bx-S(14),byy-S(22)),(bx+S(14),byy-S(22)),(bx+S(22),byy+S(70)),(bx,byy+S(95)),(bx-S(22),byy+S(70))],fill=TIE,outline=OUTL)
    # 발
    for dx in(-45,45): _ell(d,(bx+S(dx)-S(32),byy+S(105),bx+S(dx)+S(32),byy+S(145)),RACD,w)
    # 팔
    def arm(x1,y1,x2,y2):
        d.line((x1,y1,x2,y2),fill=OUTL,width=S(40)); d.line((x1,y1,x2,y2),fill=RAC,width=S(28)); _ell(d,(x2-S(22),y2-S(22),x2+S(22),y2+S(22)),RACD,w)
    if pose=='point': arm(bx+S(80),byy+S(10),bx+S(220),byy-S(110)); arm(bx-S(80),byy+S(20),bx-S(120),byy+S(90))
    elif pose=='cheer': arm(bx+S(80),byy+S(10),bx+S(170),byy-S(150)); arm(bx-S(80),byy+S(10),bx-S(170),byy-S(150))
    elif pose=='key':
        arm(bx+S(80),byy+S(10),bx+S(190),byy-S(60)); arm(bx-S(80),byy+S(20),bx-S(120),byy+S(90)); key(d,bx+S(200),byy-S(150),s*0.9)
    elif pose=='worry': arm(bx+S(80),byy+S(10),bx+S(60),byy-S(120)); arm(bx-S(80),byy+S(10),bx-S(60),byy-S(120))
    else:  # stand · 서류 가방
        arm(bx+S(80),byy+S(20),bx+S(130),byy+S(100)); arm(bx-S(80),byy+S(20),bx-S(120),byy+S(90))
        d.rounded_rectangle((bx+S(95),byy+S(95),bx+S(225),byy+S(185)),S(10),fill=(120,78,48),outline=OUTL,width=w)
        d.rectangle((bx+S(140),byy+S(80),bx+S(180),byy+S(96)),outline=OUTL,width=max(2,S(5)))
    # 머리
    hx,hy=x,y; r=S(130)
    for sx in(-1,1):
        _ell(d,(hx+sx*S(100)-S(45),hy-S(150),hx+sx*S(100)+S(45),hy-S(60)),RAC,w)
        d.ellipse((hx+sx*S(100)-S(22),hy-S(128),hx+sx*S(100)+S(22),hy-S(84)),fill=RACD)
    _ell(d,(hx-r-S(15),hy-r+S(10),hx+r+S(15),hy+r-S(10)),RAC,w)
    _ell(d,(hx-S(80),hy+S(15),hx+S(80),hy+S(110)),RACL,0)                    # 주둥이 · 볼 흰 털
    for sx in(-1,1): d.ellipse((hx+sx*S(60)-S(58),hy-S(52),hx+sx*S(60)+S(48),hy+S(22)),fill=RACD)  # 눈가 검은 띠
    d.ellipse((hx-S(20),hy+S(22),hx+S(20),hy+S(50)),fill=INK)
    ex=S(60); ey=hy-S(14)
    if face=='shock':
        for sx in(-1,1): d.ellipse((hx+sx*ex-S(24),ey-S(24),hx+sx*ex+S(24),ey+S(24)),fill=(255,255,255)); d.ellipse((hx+sx*ex-S(8),ey-S(8),hx+sx*ex+S(8),ey+S(8)),fill=INK)
        d.ellipse((hx-S(14),hy+S(62),hx+S(14),hy+S(96)),fill=INK)
    elif face=='wink':
        d.ellipse((hx-ex-S(20),ey-S(24),hx-ex+S(20),ey+S(20)),fill=(255,255,255)); d.ellipse((hx-ex-S(10),ey-S(12),hx-ex+S(8),ey+S(8)),fill=INK)
        d.arc((hx+ex-S(22),ey-S(8),hx+ex+S(22),ey+S(20)),200,340,fill=(255,255,255),width=S(7))
        d.arc((hx-S(34),hy+S(50),hx+S(34),hy+S(90)),20,160,fill=INK,width=S(6))
    else:
        for sx in(-1,1):
            d.ellipse((hx+sx*ex-S(20),ey-S(24),hx+sx*ex+S(20),ey+S(20)),fill=(255,255,255)); d.ellipse((hx+sx*ex-S(11),ey-S(14),hx+sx*ex+S(9),ey+S(8)),fill=INK)
            d.ellipse((hx+sx*ex-S(6),ey-S(10),hx+sx*ex,ey-S(4)),fill=(255,255,255))
        if face=='worry':
            for sx in(-1,1): d.line((hx+sx*S(30),ey-S(52),hx+sx*S(82),ey-S(40)),fill=INK,width=S(7))
            d.arc((hx-S(24),hy+S(64),hx+S(24),hy+S(92)),200,340,fill=INK,width=S(6))
            _ell(d,(hx+S(130),hy-S(70),hx+S(160),hy-S(22)),(150,200,235),0)
        else:
            d.arc((hx-S(34),hy+S(46),hx,hy+S(80)),20,160,fill=INK,width=S(6)); d.arc((hx,hy+S(46),hx+S(34),hy+S(80)),20,160,fill=INK,width=S(6))
    # 안경
    for sx in(-1,1): d.ellipse((hx+sx*ex-S(36),ey-S(36),hx+sx*ex+S(36),ey+S(34)),outline=(60,40,30),width=max(3,S(7)))
    d.line((hx-ex+S(36),ey,hx+ex-S(36),ey),fill=(60,40,30),width=max(3,S(6)))
    for sx in(-1,1): d.ellipse((hx+sx*S(98)-S(20),hy+S(34),hx+sx*S(98)+S(20),hy+S(58)),fill=CHEEK)
def key(d,x,y,s=1.0):
    S=lambda v:int(v*s); G=(240,190,40)
    d.ellipse((x-S(40),y-S(40),x+S(40),y+S(40)),fill=G,outline=OUTL,width=5); d.ellipse((x-S(14),y-S(14),x+S(14),y+S(14)),fill=(250,246,238))
    d.rectangle((x-S(9),y+S(36),x+S(9),y+S(140)),fill=G,outline=OUTL,width=4)
    for k in(0,1): d.rectangle((x+S(9),y+S(100)+S(k*26),x+S(36),y+S(116)+S(k*26)),fill=G,outline=OUTL,width=4)
def paper(d,x,y,s=1.0,title='계약서'):
    S=lambda v:int(v*s)
    d.rectangle((x,y,x+S(220),y+S(290)),fill=(255,255,255),outline=OUTL,width=5)
    ctext(d,y+S(20),title,F(S(40)),OUTL,x+S(110))
    for k in range(5): d.line((x+S(30),y+S(100)+S(k*36),x+S(190),y+S(100)+S(k*36)),fill=(200,196,190),width=6)

def anger(d,x,y,s=1.0,c=(220,60,60)):
    """화남 표시(빨간 십자 핏줄) + 김"""
    S=lambda v:int(v*s); w=max(4,S(9))
    for dx,dy in((-1,-1),(1,-1),(-1,1),(1,1)):
        d.arc((x+dx*S(22)-S(20),y+dy*S(22)-S(20),x+dx*S(22)+S(20),y+dy*S(22)+S(20)),
              {(-1,-1):(0,90),(1,-1):(90,180),(-1,1):(270,360),(1,1):(180,270)}[(dx,dy)][0],{(-1,-1):(0,90),(1,-1):(90,180),(-1,1):(270,360),(1,1):(180,270)}[(dx,dy)][1],fill=c,width=w)

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

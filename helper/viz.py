from PIL import Image, ImageDraw, ImageFont
NAVY=(31,56,100); BLUE=(46,92,138); ACC=(181,83,60); GRAY=(138,133,120); GOLD=(214,178,74); LINE=(222,218,208)
SANS='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; SANSR='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; SERIF='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
import os
if not os.path.exists(SANSR): SANSR='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
def F(p,s,idx=1):  # KR index in ttc
    for i in (idx,):
        try: return ImageFont.truetype(p,s,index=i)
        except: pass
    return ImageFont.truetype(p,s)
def kr(path,size):
    # find Korean face index
    for i in range(10):
        try:
            f=ImageFont.truetype(path,size,index=i)
            if 'KR' in f.getname()[0]: return f
        except: break
    return ImageFont.truetype(path,size)
def thumb(out,kicker,l1,l2,sub,badge=None):
    W=1000; im=Image.new('RGB',(W,W),(31,56,100)); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,14],fill=GOLD); d.rectangle([0,W-14,W,W],fill=GOLD)
    d.text((70,70),kicker,font=kr(SANSR,30),fill=(170,180,200))
    if badge:
        d.ellipse([862,46,954,138],outline=GOLD,width=4)
        f=kr(SANS,34); w=d.textlength(badge,font=f); d.text((908-w/2,72),badge,font=f,fill='white')
    d.line([70,248,930,248],fill=(60,90,140),width=3); d.line([70,752,930,752],fill=(60,90,140),width=3)
    def fit(t,mx,start):
        s=start
        while True:
            f=kr(SERIF,s)
            if d.textlength(t,font=f)<=mx or s<40: return f
            s-=2
    f1=fit(l1,860,84); f2=fit(l2,860,84); f=f1 if f1.size<f2.size else f2
    for t,y in ((l1,345),(l2,455)):
        w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=(246,244,238))
    fs=kr(SANSR,38); w=d.textlength(sub,font=fs); d.text(((W-w)/2,585),sub,font=fs,fill=(200,180,130))
    im.save(out)
def bars(out,kicker,title,rows,unit_fmt,note,src='낭만 부동산 분석 플랫폼  blog.naver.com/dong_jin_kim',vmax=None):
    # rows: (label, value, color, label_right)
    W,H=1440,260+len(rows)*110+160; im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    d.text((60,40),kicker,font=kr(SANSR,30),fill=BLUE); d.text((60,92),title,font=kr(SANS,46),fill=NAVY)
    vmax=vmax or max(r[1] for r in rows)*1.15; lf=kr(SANS,30); x0=max(430,int(max(d.textlength(r[0],font=lf) for r in rows))+90); x1=1180; y=250
    for lab,v,c,rt in rows:
        d.text((60,y+12),lab,font=kr(SANS,30),fill=NAVY)
        w=(x1-x0)*v/vmax; d.rectangle([x0,y,x0+w,y+62],fill=c)
        d.text((x0+w+18,y+10),rt,font=kr(SANS,32),fill=c)
        y+=110
    fn=kr(SANS,32); w=d.textlength(note,font=fn); d.text(((W-w)/2,H-120),note,font=fn,fill=ACC)
    fs=kr(SANSR,24); w=d.textlength(src,font=fs); d.text((W-w-20,H-50),src,font=fs,fill=(170,165,150))
    im.save(out)
def steps(out,kicker,title,items,note,src='낭만 부동산 분석 플랫폼  blog.naver.com/dong_jin_kim'):
    # items: (top label, circle color, value line, small line)
    W,H=1440,900; im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    d.text((60,40),kicker,font=kr(SANSR,30),fill=BLUE); d.text((60,92),title,font=kr(SANS,46),fill=NAVY)
    n=len(items); xs=[140+i*(1160/(n-1)) for i in range(n)]; cy=440
    d.line([xs[0],cy,xs[-1],cy],fill=LINE,width=8)
    for x,(t,c,v,s) in zip(xs,items):
        f=kr(SANS,30); w=d.textlength(t,font=f); d.text((x-w/2,cy-110),t,font=f,fill=NAVY)
        d.ellipse([x-42,cy-42,x+42,cy+42],fill=c)
        f=kr(SANS,30); w=d.textlength(v,font=f); d.text((x-w/2,cy+70),v,font=f,fill=c)
        f=kr(SANSR,24); 
        for k,line in enumerate(s.split('\n')):
            w=d.textlength(line,font=f); d.text((x-w/2,cy+125+k*34),line,font=f,fill=GRAY)
    fn=kr(SANS,32); w=d.textlength(note,font=fn); d.text(((W-w)/2,H-130),note,font=fn,fill=ACC)
    fs=kr(SANSR,24); w=d.textlength(src,font=fs); d.text((W-w-20,H-50),src,font=fs,fill=(170,165,150))
    im.save(out)

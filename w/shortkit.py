# -*- coding: utf-8 -*-
import glob, os, subprocess
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
BG='#1F3864'; BAND='#D9B44A'; TITLE='#F7F5F0'; SUB='#A9B4C9'
GOLD='#E3C36A'; RULE='#3E5A85'
def _face(bold):
    hit=glob.glob('/usr/share/fonts/**/NotoSansCJK-%s.ttc'%('Bold' if bold else 'DemiLight'),recursive=True)
    if not hit: hit=glob.glob('/usr/share/fonts/**/NotoSansCJK-Regular.ttc',recursive=True)
    return hit[0]
def F(s,bold=True): return ImageFont.truetype(_face(bold),s,index=1)
def _w(d,t,f):
    b=d.textbbox((0,0),t,font=f); return b[2]-b[0]
def _fit(d,t,size,bold,limit=904,floor=34):
    while size>floor:
        f=F(size,bold)
        if _w(d,t,f)<=limit: return f
        size-=2
    return F(floor,bold)
def frame(path, kicker, blocks, foot):
    """blocks: [(text, size, color, bold, gap_after)]  세로 가운데 정렬"""
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,14],fill=BAND); d.rectangle([0,H-14,W,H],fill=BAND)
    fk=_fit(d,kicker,46,False,860)
    d.text((W/2,182),kicker,font=fk,fill=SUB,anchor='mm')
    d.line([(88,252),(992,252)],fill=RULE,width=2)
    d.line([(88,1662),(992,1662)],fill=RULE,width=2)
    if foot:
        ff=_fit(d,foot,40,False,880,28)
        d.text((W/2,1742),foot,font=ff,fill=SUB,anchor='mm')
    fs=[]; total=0
    for t,s,c,b,g in blocks:
        f=_fit(d,t,s,b); fs.append(f); total+=int(f.size*1.30)+g
    y=(252+1662)/2-total/2
    for (t,s,c,b,g),f in zip(blocks,fs):
        lh=int(f.size*1.30)
        d.text((W/2,y+lh/2),t,font=f,fill=c,anchor='mm')
        y+=lh+g
    im.save(path); return path
def build(folder, frames, durs, out):
    ins=[]
    for i,(p,dur) in enumerate(zip(frames,durs)):
        ins+=['-loop','1','-t','%.2f'%dur,'-i',p]
    n=len(frames)
    fl=';'.join('[%d:v]settb=AVTB,fps=30,format=yuv420p[v%d]'%(i,i) for i in range(n))
    off=0; cur='v0'; parts=[]
    for i in range(1,n):
        off+=durs[i-1]-0.4
        parts.append('[%s][v%d]xfade=transition=fade:duration=0.4:offset=%.2f[x%d]'%(cur,i,off,i))
        cur='x%d'%i
    fl=fl+';'+';'.join(parts)
    open(os.path.join(folder,'filter.txt'),'w').write(fl)
    cmd=['ffmpeg','-y']+ins+['-filter_complex',fl,'-map','[%s]'%cur,
         '-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p',
         '-r','30','-movflags','+faststart',out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-1500:]); raise SystemExit(1)
    return sum(durs)-0.4*(n-1)

# ── 낭만 인테리어 세로 영상 ──
I_BG='#1F3864'; I_TITLE='#F7F5F0'; I_SUB='#A9B4C9'; I_KEY='#C7D6E6'; I_CARD='#FFFFFF'
def iframe(path, kicker, blocks, foot, card=None):
    """card: 가운데 넣을 이미지 경로 (없으면 글자만)"""
    im=Image.new('RGB',(W,H),I_BG); d=ImageDraw.Draw(im)
    fk=_fit(d,kicker,46,False,860)
    d.text((W/2,170),kicker,font=fk,fill=I_SUB,anchor='mm')
    d.line([(88,236),(992,236)],fill='#3E5A85',width=2)
    d.line([(88,1668),(992,1668)],fill='#3E5A85',width=2)
    d.text((W/2,1748),'낭만 인테리어',font=F(44,True),fill=I_TITLE,anchor='mm')
    if foot:
        d.text((W/2,1826),foot,font=_fit(d,foot,38,False,880,26),fill=I_SUB,anchor='mm')
    top,bot=236,1668
    if card:
        ci=Image.open(card).convert('RGB')
        cw=904; ch=int(ci.height*cw/ci.width)
        if ch>720:
            ch=720; cw=int(ci.width*ch/ci.height)
        ci=ci.resize((cw,ch),Image.LANCZOS)
        fs=[];tot=0
        for t,s,c,b,g in blocks:
            f=_fit(d,t,s,b); fs.append(f); tot+=int(f.size*1.30)+g
        block_h=tot+ch+56
        y=(top+bot)/2-block_h/2
        for (t,s,c,b,g),f in zip(blocks,fs):
            lh=int(f.size*1.30); d.text((W/2,y+lh/2),t,font=f,fill=c,anchor='mm'); y+=lh+g
        y+=56
        im.paste(ci,((W-cw)//2,int(y)))
    else:
        fs=[];tot=0
        for t,s,c,b,g in blocks:
            f=_fit(d,t,s,b); fs.append(f); tot+=int(f.size*1.30)+g
        y=(top+bot)/2-tot/2
        for (t,s,c,b,g),f in zip(blocks,fs):
            lh=int(f.size*1.30); d.text((W/2,y+lh/2),t,font=f,fill=c,anchor='mm'); y+=lh+g
    im.save(path); return path

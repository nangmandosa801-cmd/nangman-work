# 10/16 11:17 사용자 「네이버 클립도 앞으로 시공 영상을 올리자」 — 시공 사진으로 만든 세로 1080x1920 클립
import sys,json,os,subprocess
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/int/mp4_1015')
from PIL import Image,ImageDraw,ImageFilter
from sns_carousel import clean,font,FB,FBo
import bgm
W,H=1080,1920
GOLD=(255,214,120)
def fit(d,lines,start,mn,maxw):
    sz=start
    while sz>mn and max(d.textlength(l,font=font(FB,sz)) for l in lines)>maxw: sz-=2
    return sz
def slide(src,line,sub,out):
    im=Image.open(src).convert('RGB'); im=im if src.endswith('.png') else clean(im)
    r=max(W/im.width,H/im.height); bg=im.resize((int(im.width*r)+1,int(im.height*r)+1))
    bg=bg.crop(((bg.width-W)//2,(bg.height-H)//2,(bg.width-W)//2+W,(bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(40))
    bg=Image.eval(bg,lambda v:int(v*0.35))
    PW,PH=1000,1060; r=min(PW/im.width,PH/im.height); fg=im.resize((int(im.width*r),int(im.height*r)))
    top=560; bg.paste(fg,((W-fg.width)//2,top+(PH-fg.height)//2))
    d=ImageDraw.Draw(bg,'RGBA')
    d.rounded_rectangle((60,110,420,190),20,fill=GOLD)
    d.text((240,150),'낭만 인테리어',font=font(FB,48),fill=(20,20,26),anchor='mm')
    lines=line.split('\n'); sz=fit(d,lines,112,84,960)
    y=250
    for ln in lines:
        d.text((W//2,y),ln,font=font(FB,sz),fill=(255,255,255),anchor='ma',stroke_width=3,stroke_fill=(0,0,0)); y+=int(sz*1.25)
    if sub:
        d.rounded_rectangle((90,1640,990,1730),24,fill=(12,14,20,220))
        d.text((W//2,1685),sub,font=font(FB,50),fill=GOLD,anchor='mm')
    phone(d)
    bg.save(out,quality=92)
def phone(d):
    d.rectangle((0,1770,W,H),fill=GOLD)
    d.text((W//2,1825),'문의 010-2882-8165',font=font(FB,76),fill=(20,20,26),anchor='mm')
    d.text((W//2,1890),'사진 한 장 보내 주시면 무료로 봐 드립니다',font=font(FBo,34),fill=(40,40,46),anchor='mm')
def tslide(kicker,line,sub,out):
    bg=Image.new('RGB',(W,H),(24,40,72)); d=ImageDraw.Draw(bg,'RGBA')
    d.rounded_rectangle((60,110,420,190),20,fill=GOLD)
    d.text((240,150),'낭만 인테리어',font=font(FB,48),fill=(20,20,26),anchor='mm')
    d.text((W//2,520),kicker,font=font(FB,70),fill=GOLD,anchor='mm')
    lines=line.split('\n'); sz=fit(d,lines,150,90,980); y=640
    for ln in lines: d.text((W//2,y),ln,font=font(FB,sz),fill=(255,255,255),anchor='ma'); y+=int(sz*1.3)
    y+=40
    for ln in sub.split('\n'):
        d.text((W//2,y),ln,font=font(FB,62),fill=(220,226,238),anchor='ma'); y+=90
    phone(d)
    bg.save(out,quality=92)
import sys as _sy; _sy.path.insert(0,'/home/claude/blogkit'); 
try: import discount1130 as _D1130   # DISCOUNT1130 (11/3 끝 화면 할인 문구는 끔 · 모듈이 없어도 돌게)
except Exception: _D1130 = None
def ask(out,head,what):
    bg=Image.new('RGB',(W,H),(22,24,30)); d=ImageDraw.Draw(bg)
    d.text((W//2,240),'낭만 인테리어',font=font(FB,64),fill=GOLD,anchor='mm')
    sz=fit(d,head,120,84,960); y=400
    for ln in head: d.text((W//2,y),ln,font=font(FB,sz),fill=(255,255,255),anchor='ma'); y+=int(sz*1.3)
    y+=60
    for ln in [what+' 사진 한 장 보내 주시면','무료로 봐 드립니다']:
        d.text((W//2,y),ln,font=font(FB,72),fill=(230,232,238),anchor='ma'); y+=100
    d.rounded_rectangle((90,1180,990,1400),48,fill=GOLD)
    d.text((W//2,1290),'010-2882-8165',font=font(FB,112),fill=(22,24,30),anchor='mm')
    d.text((W//2,1480),'전화 · 문자 모두 됩니다',font=font(FB,64),fill=(210,214,222),anchor='mm')
    d.text((W//2,1580),'가까운 시공팀을 연결해 드립니다',font=font(FBo,54),fill=(170,175,185),anchor='mm')
    if False and _D1130.ON:   # 11/3 사용자 「빼」: 클립 끝 화면 할인 문구 제거(연락처만 남김)
        d.text((W//2,1700),_D1130.L1,font=font(FB,60),fill=GOLD,anchor='mm'); d.text((W//2,1785),_D1130.L2,font=font(FB,60),fill=GOLD,anchor='mm')
    bg.save(out,quality=92)
def build(spec,tag):
    s=json.load(open(spec)); dd=f'/home/claude/int/mp4_1015/v_{tag}'; os.makedirs(dd,exist_ok=True); outs=[]
    for i,x in enumerate(s.get('vintro',[])+s['slides'],1):
        o=f'{dd}/{i:02d}.jpg'
        if 'kicker' in x: tslide(x['kicker'],x['line'],x.get('sub',''),o)
        else: slide(x['src'],x.get('vline',x['line']),x.get('sub',''),o)
        outs.append(o)
    o=f'{dd}/{len(outs)+1:02d}.jpg'; ask(o,s['head'],s['what']); outs.append(o)
    return outs
def make(slides,out,per=2.6,last=4.0,fade=0.4,seed=7):
    n=len(slides); durs=[per]*(n-1)+[last]; total=sum(durs)-fade*(n-1)
    wav=out.replace('.mp4','_bgm.wav'); bgm.make(wav,total+0.5,seed)
    args=['ffmpeg','-y','-loglevel','error']
    for s in slides: args+=['-i',s]
    args+=['-i',wav]; fc=[]
    for i,d in enumerate(durs):
        fc.append(f"[{i}:v]scale=1188:2112,zoompan=z='min(zoom+0.0004,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(d*30)}:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
    prev='v0'; off=0
    for i in range(1,n):
        off+=durs[i-1]-fade; fc.append(f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={off:.2f}[x{i}]"); prev=f'x{i}'
    fc.append(f"[{n}:a]afade=t=out:st={total-1.0:.2f}:d=1.0,volume=0.55[a]")
    args+=['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',out]
    subprocess.run(args,check=True); os.remove(wav)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','1','-i',out,'-frames:v','1',out.replace('.mp4','_cover.jpg')],check=True)
if __name__=='__main__':
    make(build(sys.argv[1],sys.argv[2]),sys.argv[3],seed=int(sys.argv[4]) if len(sys.argv)>4 else 7); print('ok')

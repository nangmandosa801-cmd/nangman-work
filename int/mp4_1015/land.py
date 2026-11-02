# 10/15 18:37 사용자 「동영상을 가로형으로 만들어야지」 — 블로그 본문용 1920x1080
import sys,json,glob,os
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/int/mp4_1015')
from PIL import Image,ImageDraw,ImageFilter
from sns_carousel import clean,font,FB,FBo
W,H=1920,1080
def slide(src,line,sub,out):
    im=Image.open(src).convert('RGB'); im=im if src.endswith('.png') else clean(im)
    r=max(W/im.width,H/im.height); bg=im.resize((int(im.width*r)+1,int(im.height*r)+1)); bg=bg.crop(((bg.width-W)//2,(bg.height-H)//2,(bg.width-W)//2+W,(bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(34))
    bg=Image.eval(bg,lambda v:int(v*0.4))
    PW=1120; r=min(PW/im.width,(H-80)/im.height); fg=im.resize((int(im.width*r),int(im.height*r)))
    bg.paste(fg,(40+(PW-fg.width)//2,(H-fg.height)//2))
    d=ImageDraw.Draw(bg,'RGBA')
    d.rectangle((1200,0,W,H),fill=(12,14,20,215))
    d.rounded_rectangle((1250,70,1580,140),18,fill=(255,214,120))
    d.text((1272,78),'낭만 인테리어',font=font(FB,42),fill=(20,20,26))
    lines=line.split('\n'); sz=88
    while sz>56 and max(d.textlength(l,font=font(FB,sz)) for l in lines)>600: sz-=2
    f=font(FB,sz); y=H//2-len(lines)*int(sz*0.66)
    for ln in lines:
        d.text((1250,y),ln,font=f,fill=(255,255,255)); y+=int(sz*1.32)
    if sub: d.text((1252,H-130),sub,font=font(FBo,40),fill=(255,214,120))
    bg.save(out,quality=92)
def ask(out,head,what):
    bg=Image.new('RGB',(W,H),(22,24,30)); d=ImageDraw.Draw(bg)
    d.text((140,110),'낭만 인테리어',font=font(FBo,52),fill=(255,214,120))
    y=220
    hs=112
    while hs>70 and max(d.textlength(l,font=font(FB,hs)) for l in head)>860: hs-=2
    for ln in head: d.text((140,y),ln,font=font(FB,hs),fill=(255,255,255)); y+=int(hs*1.25)
    y+=20
    for ln in [what+' 사진 한 장 보내 주세요','무료로 봐 드립니다','가까운 시공팀을 연결해 드립니다']:
        d.text((140,y),ln,font=font(FBo,56),fill=(225,228,235)); y+=78
    d.rounded_rectangle((1060,330,1800,520),40,fill=(255,214,120))
    d.text((1430,425),'010-2882-8165',font=font(FB,92),fill=(22,24,30),anchor='mm')
    d.text((1430,590),'전화 · 문자 모두 됩니다',font=font(FBo,44),fill=(200,204,212),anchor='mm')
    d.text((1430,650),'마음에 드는 사진 번호도 같이',font=font(FBo,40),fill=(150,155,165),anchor='mm')
    bg.save(out,quality=92)
def build(spec,tag):
    s=json.load(open(spec)); os.makedirs('/home/claude/int/mp4_1015/'+tag,exist_ok=True)
    outs=[]
    for i,x in enumerate(s['slides'],1):
        o=f'/home/claude/int/mp4_1015/{tag}/{tag}_{i:02d}.jpg'; slide(x['src'],x['line'],x.get('sub',''),o); outs.append(o)
    o=f'/home/claude/int/mp4_1015/{tag}/{tag}_{len(outs)+1:02d}.jpg'; ask(o,s['head'],s['what']); outs.append(o)
    return outs
def text_slide(out,kicker,big,sub):
    bg=Image.new('RGB',(W,H),(31,56,100)); d=ImageDraw.Draw(bg)
    d.rounded_rectangle((140,120,470,190),18,fill=(255,214,120)); d.text((162,128),'낭만 인테리어',font=font(FB,42),fill=(20,20,26))
    d.text((140,300),kicker,font=font(FBo,56),fill=(255,214,120))
    y=400
    for ln in big.split('\n'): d.text((140,y),ln,font=font(FB,104),fill=(255,255,255)); y+=136
    d.text((142,y+30),sub,font=font(FBo,48),fill=(215,222,235))
    bg.save(out,quality=92)

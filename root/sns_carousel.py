import sys,json
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=1080,1350
FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
FBo='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font(p,s,i=1):
    return ImageFont.truetype(p,s,index=i)  # KR index
def clean(im):
    g=im.convert('L');w,h=im.size
    m=lambda y:sum(g.getpixel((x,y)) for x in range(0,w,8))/len(range(0,w,8))
    cut=h
    for y in range(max(0,h-260),h):
        if all(m(yy)>244 for yy in range(y,min(h,y+6))): cut=y;break
    im=im.crop((0,0,w,cut))
    from PIL import ImageChops
    bg=Image.new('RGB',im.size,(255,255,255)); d=ImageChops.difference(im,bg).convert('L').point(lambda v:255 if v>14 else 0)
    bb=d.getbbox()
    return im.crop(bb) if bb else im
def slide(src,line,sub,out):
    im=clean(Image.open(src).convert('RGB'))
    # background: blurred cover
    r=max(W/im.width,H/im.height); bg=im.resize((int(im.width*r)+1,int(im.height*r)+1)).crop((0,0,W,H)).filter(ImageFilter.GaussianBlur(30))
    bg=Image.eval(bg,lambda v:int(v*0.45))
    if im.height/im.width>1.15:  # tall: cover
        r=max(W/im.width,(H-0)/im.height); fg=im.resize((int(im.width*r),int(im.height*r)))
        x=(fg.width-W)//2; y=(fg.height-H)//2; bg=fg.crop((x,y,x+W,y+H))
    else:
        r=W/im.width; fg=im.resize((W,int(im.height*r))); bg.paste(fg,(0,(H-fg.height)//2-80))
    d=ImageDraw.Draw(bg,'RGBA')
    # bottom band
    for i in range(420):
        a=int(235*min(1,i/260)); d.line([(0,H-420+i),(W,H-420+i)],fill=(10,10,14,a))
    d.rounded_rectangle((40,40,330,104),18,fill=(0,0,0,150))
    d.text((62,46),'낭만 인테리어',font=font(FBo,38),fill=(255,255,255))
    f=font(FB,82); y=H-300
    for ln in line.split('\n'):
        d.text((60,y),ln,font=f,fill=(255,255,255)); y+=104
    if sub: d.text((62,H-90),sub,font=font(FBo,40),fill=(255,214,120))
    bg.save(out,quality=92)
def ask(out,head=('우리 집 현관도','이렇게 될까?'),what='현관'):
    bg=Image.new('RGB',(W,H),(22,24,30)); d=ImageDraw.Draw(bg)
    d.text((70,90),'낭만 인테리어',font=font(FBo,46),fill=(255,214,120))
    y=300
    for ln,s in [(head[0],96),(head[1],96)]:
        d.text((70,y),ln,font=font(FB,s),fill=(255,255,255)); y+=130
    y+=60
    for ln in [what+' 사진 한 장 보내 주세요','무료로 봐 드립니다','가까운 시공팀을 연결해 드립니다']:
        d.text((70,y),ln,font=font(FBo,56),fill=(225,228,235)); y+=88
    d.rounded_rectangle((60,1050,1020,1200),30,fill=(255,214,120))
    d.text((110,1080),'010-2882-8165',font=font(FB,82),fill=(22,24,30))
    d.text((72,1240),'전화 · 문자 · 마음에 드는 사진 번호도 같이',font=font(FBo,38),fill=(170,175,185))
    bg.save(out,quality=92)
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]))
    for i,s in enumerate(spec['slides'],1):
        slide(s['src'],s['line'],s.get('sub',''),f"{spec['out']}_{i:02d}.jpg")
    ask(f"{spec['out']}_{len(spec['slides'])+1:02d}.jpg",tuple(spec.get('head',['우리 집 현관도','이렇게 될까?'])),spec.get('what','현관'))

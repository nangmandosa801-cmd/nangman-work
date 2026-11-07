import sys,glob,os
from PIL import Image,ImageDraw,ImageFont
d=sys.argv[1]; rng=sys.argv[2] if len(sys.argv)>2 else None
fs=sorted(glob.glob(d+'/*.jpg'))
if rng: a,b=map(int,rng.split('-')); fs=[f for f in fs if a<=int(os.path.basename(f)[:2])<=b]
W=220;cols=6;rows=(len(fs)+cols-1)//cols
c=Image.new('RGB',(W*cols,W*rows),'white');dr=ImageDraw.Draw(c)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
for i,f in enumerate(fs):
    try: im=Image.open(f).convert('RGB')
    except: continue
    im.thumbnail((W-6,W-6));x=(i%cols)*W;y=(i//cols)*W;c.paste(im,(x+3,y+3))
    dr.rectangle([x+3,y+3,x+48,y+33],fill='yellow');dr.text((x+6,y+4),os.path.basename(f)[:2],fill='black',font=F)
c.save(sys.argv[3] if len(sys.argv)>3 else '/tmp/s.jpg',quality=80)

import json,sys
from PIL import Image,ImageDraw,ImageFont
W,H=1080,1350; NAVY=(31,56,100); GOLD=(255,214,120); WH=(255,255,255)
F=lambda s,b=True: ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-'+('Black' if b else 'Bold')+'.ttc',s,index=1)
def brand(d,dark=True):
    d.text((60,52),'낭만 부동산 분석 플랫폼',font=F(36,False),fill=GOLD if dark else NAVY)
def wrap(d,txt,f,maxw):
    out=[]
    for para in txt.split('\n'):
        line=''
        for ch in para:
            if d.textlength(line+ch,font=f)>maxw and line: out.append(line); line=ch
            else: line+=ch
        out.append(line)
    return out
def text_card(out,kicker,big,sub):
    im=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(im); brand(d)
    nb=len(wrap(d,big,F(104),W-120)); ns=len(wrap(d,sub,F(54,False),W-120)); y=(H-(110+nb*132+40+ns*80))//2; d.text((60,y),kicker,font=F(52,False),fill=GOLD); y+=110
    for ln in wrap(d,big,F(104),W-120): d.text((60,y),ln,font=F(104),fill=WH); y+=132
    y+=40
    for ln in wrap(d,sub,F(54,False),W-120): d.text((60,y),ln,font=F(54,False),fill=(215,222,235)); y+=80
    im.save(out,quality=92)
def num_card(out,head,items):
    im=Image.new('RGB',(W,H),(246,247,250)); d=ImageDraw.Draw(im); brand(d,False)
    y=150
    for ln in wrap(d,head,F(64),W-120): d.text((60,y),ln,font=F(64),fill=NAVY); y+=86
    y+=40
    for n,lab in items:
        d.rounded_rectangle((60,y,W-60,y+250),28,fill=WH,outline=(220,226,236),width=3)
        d.text((100,y+30),n,font=F(96),fill=NAVY)
        yy=y+150
        for ln in wrap(d,lab,F(44,False),W-200)[:2]: d.text((100,yy),ln,font=F(44,False),fill=(90,100,120)); yy+=50
        y+=280
    im.save(out,quality=92)
def img_card(out,src,cap):
    im=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(im); brand(d)
    s=Image.open(src).convert('RGB'); r=min((W-80)/s.width,(H-420)/s.height); s=s.resize((int(s.width*r),int(s.height*r)))
    im.paste(s,((W-s.width)//2,140))
    y=140+s.height+50
    for ln in wrap(d,cap,F(66),W-120)[:3]: d.text((60,y),ln,font=F(66),fill=WH); y+=88
    im.save(out,quality=92)
def end_card(out,kw,what='자세한 숫자는'):
    im=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(im); brand(d)
    y=330
    for ln in [kw]+wrap(d,what,F(76),W-120): d.text((60,y),ln,font=F(76),fill=WH); y+=110
    d.text((60,y),'블로그에 다 정리했습니다',font=F(76),fill=GOLD); y+=170
    d.rounded_rectangle((60,y,W-60,y+150),30,fill=GOLD)
    d.text((100,y+38),'프로필 링크 → 블로그',font=F(66),fill=NAVY)
    d.text((60,H-140),'네이버 블로그 「낭만 부동산 분석 플랫폼」',font=F(42,False),fill=(200,210,228))
    im.save(out,quality=92)
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]))
    for i,sl in enumerate(spec['slides'],1):
        o=f"{spec['out']}_{i:02d}.jpg"; t=sl['t']
        if t=='text': text_card(o,sl['k'],sl['big'],sl['sub'])
        elif t=='num': num_card(o,sl['head'],sl['items'])
        elif t=='img': img_card(o,sl['src'],sl['cap'])
        elif t=='end': end_card(o,sl['kw'],sl.get('what','자세한 숫자는'))

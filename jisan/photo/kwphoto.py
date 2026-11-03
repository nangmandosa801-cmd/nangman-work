import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; FR='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
def F(s,b=True): return ImageFont.truetype(FB if b else FR,s,index=1)
DEEP=(13,59,92); CY=(27,122,158); BG=(244,246,248); GOLD=(255,226,63)
def trim(path,top=0,bottom_band=True):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(int)
    a=a[top:]; im=im.crop((0,top,im.width,im.height))
    # 바깥 단색 여백 자르기
    m=np.abs(a-a[0,0]).sum(2)>30
    rows=np.where(m.mean(1)>0.5)[0]; cols=np.where(m.mean(0)>0.5)[0]
    if len(rows) and len(cols): im=im.crop((cols[0],rows[0],cols[-1]+1,rows[-1]+1)); a=np.asarray(im).astype(int)
    if bottom_band:
        h=a.shape[0]
        blue=(np.abs(a-np.array([27,122,158])).sum(2)<90).mean(1)
        ys=np.where(blue>0.5)[0]; ys=ys[ys>h*0.6]
        if len(ys): im=im.crop((0,0,im.width,ys.min()-2))
    return im
def card(src,kick,line,out,W=1080):
    ph=src.copy(); ph=ph.resize((W-80,int(ph.height*(W-80)/ph.width)))
    H=170+ph.height+70
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((40,48,48,128),fill=CY)
    d.text((66,40),kick,font=F(26,False),fill=CY)
    d.text((66,78),line,font=F(40),fill=DEEP)
    c.paste(ph,(40,160))
    d.text((W-40-d.textlength('지산드림  blog.naver.com/jisandream01',font=F(20,False)),H-50),'지산드림  blog.naver.com/jisandream01',font=F(20,False),fill=(140,150,160))
    c.save(out); return c
def thumb(srcs,kick,l1,l2,sub,out,S=1000):
    c=Image.new('RGB',(S,S))
    n=len(srcs); w=S//n
    for i,s in enumerate(srcs):
        im=s.copy(); r=max(w/im.width,S/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1))
        x=(im.width-w)//2; y=(im.height-S)//2; c.paste(im.crop((x,y,x+w,y+S)),(i*w,0))
    ov=Image.new('RGBA',(S,S),(8,30,50,0)); od=ImageDraw.Draw(ov)
    for y in range(S): od.line((0,y,S,y),fill=(8,30,50,int(90+120*(y/S))))
    c=Image.alpha_composite(c.convert('RGBA'),ov).convert('RGB'); d=ImageDraw.Draw(c)
    d.rectangle((0,0,S,12),fill=CY); d.rectangle((0,S-12,S,S),fill=CY)
    d.text((60,60),kick,font=F(32,False),fill=(220,230,238))
    def ct(y,t,f,col):
        w_=d.textlength(t,font=f); d.text(((S-w_)/2,y),t,font=f,fill=col)
    ct(560,l1,F(84),(255,255,255)); ct(675,l2,F(76),GOLD); ct(800,sub,F(34,False),(225,232,238))
    ct(890,'지산드림',F(36),(255,255,255))
    c.save(out)

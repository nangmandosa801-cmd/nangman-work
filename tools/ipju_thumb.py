#!/usr/bin/env python3
import argparse
from PIL import Image, ImageDraw, ImageFont
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; BO='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; M='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
F=lambda p,s:ImageFont.truetype(p,s,index=1)
BG='#F4F2ED'; INK='#1E2A24'; GREEN='#24493A'; GOLD='#B88A3E'; GREY='#6B7069'; LINE='#D9D4C8'
W=H=1080; X=80; MW=W-2*X
def fit(d,t,path,size,minsize=56):
    while size>minsize and d.textlength(t,font=F(path,size))>MW: size-=4
    return F(path,size)
a=argparse.ArgumentParser()
for k in ('tag','name','lead','key','out'): a.add_argument('--'+k,required=True)
a.add_argument('--top',default='시공 사례 데이터로 견적 검증'); a.add_argument('--sub',default=''); a.add_argument('--date',default='')
o=a.parse_args()
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,120],fill=GREEN)
d.text((X,60),'낭만 인테리어',font=F(B,46),fill='white',anchor='lm')
d.text((W-X,60),o.top,font=F(M,32),fill=(205,220,210),anchor='rm')
names=o.name.split('|')[:2]
nf=min((fit(d,n,B,92) for n in names),key=lambda f:f.size)
y=190 if o.sub else 205
f=F(BO,40); tw=d.textlength(o.tag,font=f)
d.rounded_rectangle([X,y,X+tw+56,y+70],radius=35,fill=GREEN); d.text((X+28,y+35),o.tag,font=f,fill='white',anchor='lm')
y+=110
for n in names: d.text((X,y),n,font=nf,fill=INK); y+=int(nf.size*1.28)
y+=30; d.rectangle([X,y,X+140,y+10],fill=GOLD); y+=50
d.text((X,y),o.lead,font=fit(d,o.lead,B,70),fill=GREEN); y+=96
kf=fit(d,o.key,B,104); d.text((X,y),o.key,font=kf,fill=GOLD); y+=int(kf.size*1.44)
if o.sub: d.text((X,y),o.sub,font=fit(d,o.sub,M,44,40),fill=GREY)
d.rectangle([X,H-110,W-X,H-108],fill=LINE)
d.text((X,H-60),'blog.naver.com/champion_chart',font=F(M,32),fill=GREY,anchor='lm')
if o.date: d.text((W-X,H-60),o.date,font=F(BO,34),fill=GREEN,anchor='rm')
im.save(o.out,quality=93); print(o.out)

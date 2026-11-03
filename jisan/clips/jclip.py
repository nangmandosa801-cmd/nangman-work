import sys,os; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
DEEP=(13,59,92); CY=(27,122,158); LCY=(70,180,215); GOLD=(226,178,96); WH=(255,255,255); BG=(244,246,248); GR=(190,200,210); RED=(181,101,78); GRN=(60,122,90); WATER=(120,190,225); MNT=(95,140,105)
def jb(bg=BG): return base(bg)
def foot(d,c=SAND): ctext(d,1830,'지산드림 · 구리 갈매',F(40,False),c)
def reg(d,c=SAND): ctext(d,1760,'지산드림공인중개사사무소 · 등록번호 41310-2022-00061',F(30,False),c)
def cap(d,lines,c=DEEP,size=80,y=110): caption(d,lines,y=y,c=c,size=size)
def apt(d,x,y,w,h,c=(170,180,195),fl=6):
    d.rectangle((x,y,x+w,y+h),fill=c)
    for i in range(fl):
        for j in range(3): d.rectangle((x+20+j*(w-40)//3,y+20+i*(h-40)//fl,x+10+(j+1)*(w-40)//3,y+10+(i+1)*(h-40)//fl),fill=GLASS)
def lock(d,x,y,t,c=RED):
    d.arc((x-45,y-95,x+45,y-5),180,360,fill=c,width=16); d.rounded_rectangle((x-70,y-20,x+70,y+100),18,fill=c)
    ctext(d,y+120,t,F(52),c,x=x)
def card(d,y,a,b,c):
    d.rounded_rectangle((70,y,1010,y+230),36,fill=WH,outline=c,width=8); ctext(d,y+36,a,F(64),c); ctext(d,y+130,b,F(58),SAND)

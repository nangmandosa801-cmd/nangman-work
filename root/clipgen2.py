# 캐릭터 없는 쇼츠 (10/24 사용자 「만화 캐릭터는 빼고」) — 글자 크게, 화면 가운데 채움
import clipgen as G
from clipgen import *
G.person=lambda *a,**k: None
def cap2(d,lines,c=NAVY,size=96,y=230):
    for i,l in enumerate(lines): cfit(d,y+i*(size+28),l,size,c,maxw=980)
def S_hook(d,b,lines,bub,c=NAVY,**k):
    cap2(d,lines,c)
    d.rounded_rectangle((60,680,1020,1360),52,fill=CREAM,outline=NAVY,width=8)
    n=len(bub); y0=1020-(n*140)//2
    for i,t in enumerate(bub): cfit(d,y0+i*140,t,104,NAVY,maxw=880)
    cfit(d,1500,'실거래로 확인했습니다',70,SAND)
def S_big(d,b,lines,num,sub1='',sub2='',c=WARN,nsize=250,**k):
    cap2(d,lines,NAVY,88)
    f=fit(d,num,nsize,1000); cfit(d,700,num,nsize,c,maxw=1000)
    y=700+int(f.size*1.3)+70
    if sub1: cfit(d,y,sub1,70,NAVY,maxw=1000)
    if sub2: cfit(d,y+120,sub2,62,SAND,maxw=1000)
def S_vs(d,b,lines,L,R,bottom='',c=NAVY,bc=WARN,**k):
    cap2(d,lines,c,88)
    d.rectangle((50,600,1030,1340),fill=WH,outline=(220,215,205),width=5); d.line((540,600,540,1340),fill=(220,215,205),width=5)
    for (lab,val,sub),x,cc in ((L,295,NAVY),(R,785,WARN)):
        cfit(d,660,lab,66,cc,x=x,maxw=450); cfit(d,860,val,150,cc,x=x,maxw=450)
        if sub: cfit(d,1120,sub,52,SAND,x=x,maxw=450)
    if bottom:
        for i,t in enumerate(bottom if isinstance(bottom,list) else [bottom]): cfit(d,1430+i*125,t,90,bc,maxw=1000)
def S_bars(d,b,lines,items,unit='',c=NAVY,**k):
    cap2(d,lines,c,88); n=len(items); mx=max(abs(it[1]) for it in items) or 1
    y0=600; h=min(250,880//n)
    for i,it in enumerate(items):
        lab,v=it[0],it[1]; cc=it[2] if len(it)>2 else (WARN if v<0 else NAVY)
        y=y0+i*h; d.text((70,y),lab,font=fit(d,lab,62,940),fill=NAVY)
        bh=min(110,h-100); w=int(600*abs(v)/mx); d.rounded_rectangle((70,y+86,70+max(w,14),y+86+bh),18,fill=cc)
        txt=it[3] if len(it)>3 else f'{v}{unit}'
        d.text((96+max(w,14),y+86+bh//2-38),txt,font=fit(d,txt,70,1010-96-max(w,14)),fill=cc)
    if k.get('note'): cfit(d,y0+n*h+60,k['note'],66,WARN,maxw=1000)
def S_end(d,b,lines,sub,sub2='자세한 숫자는'):
    cap2(d,lines,WH,90,y=300)
    for i,t in enumerate(sub): cfit(d,640+i*160,t,110,Y,maxw=1000)
    cfit(d,1230,sub2,64,PALE,maxw=1000); cfit(d,1320,'블로그에 정리했습니다',64,PALE)
    cfit(d,1480,'낭만 부동산 분석 플랫폼',70,Y); cfit(d,1580,BRAND[b][1],52,PALE)
G.TYPES.update(hook=S_hook,big=S_big,vs=S_vs,bars=S_bars,end=S_end)

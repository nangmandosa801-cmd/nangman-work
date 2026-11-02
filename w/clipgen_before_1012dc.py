import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
_REALP=person
import os, re
Y=(240,190,40); WH=(255,255,255); CREAM=(255,243,196); PALE=(210,220,235)
BRAND={'nm':('낭만 부동산 분석 플랫폼','blog.naver.com/dong_jin_kim','#낭만부동산'),
       'int':('낭만 인테리어','010-7678-9967','#낭만인테리어'),
       'js':('지산드림','blog.naver.com/jisandream01','#지산드림')}
def foot(d,b,c=SAND): ctext(d,1830,BRAND[b][0],F(40,False),c)
def fit(d,t,size,maxw=940):
    while size>30 and d.textlength(t,font=F(size))>maxw: size-=4
    return F(size)
def cfit(d,y,t,size,c,x=W//2,maxw=940,b=True):
    f=fit(d,t,size,maxw) if b else F(size,False)
    ctext(d,y,t,f,c,x)
def cap(d,lines,c=NAVY,size=76):
    for i,l in enumerate(lines): cfit(d,110+i*(size+22),l,size,c)
def card(d,y,h,t1,t2,c=NAVY,s1=66,s2=52):
    d.rounded_rectangle((70,y,1010,y+h),40,fill=WH,outline=c,width=8)
    if t2:
        cfit(d,y+h//2-s1-2,t1,s1,c,maxw=880); cfit(d,y+h//2+max(14,s1-50),t2,s2,SAND,maxw=880)
    else: cfit(d,y+h//2-s1//2-6,t1,s1,c,maxw=880)

def S_hook(d,b,lines,bub,face='worry',shirt=MID,c=NAVY,size=78):
    cap(d,lines,c,size); person(d,540,820,1.0,face=face,shirt=shirt)
    bubble(d,80,1250,920,230,bub,size=60,fill=CREAM)
def S_big(d,b,lines,num,sub1='',sub2='',c=WARN,face='smile',size=78,nsize=200):
    cap(d,lines,NAVY,size); f=fit(d,num,nsize,980); cfit(d,520,num,nsize,c,maxw=980)
    y=520+int(f.size*1.35)+30
    if sub1: cfit(d,y,sub1,60,NAVY)
    if sub2: cfit(d,y+90,sub2,54,SAND)
    if face: person(d,540,1380,0.8,face=face,shirt=MID)
def S_cards(d,b,lines,items,c=NAVY,size=76,y0=None):
    cap(d,lines,c,size); n=len(items); h=min(310,(1200)//n-30); y0=y0 or (460 if len(lines)>1 else 380)
    for i,it in enumerate(items):
        t1,t2,cc=(it+(NAVY,))[:3] if len(it)<3 else it
        card(d,y0+i*(h+30),h,t1,t2,cc,s1=64 if t2 else 70,s2=50)
    yb=y0+n*(h+30)
    if yb<1330: person(d,540,yb+110,0.6,face='smile',shirt=MID)
def S_vs(d,b,lines,L,R,bottom='',c=NAVY,size=76,bc=WARN):
    cap(d,lines,c,size)
    d.rectangle((60,420,1020,1120),fill=WH,outline=(220,215,205),width=4); d.line((540,420,540,1120),fill=(220,215,205),width=4)
    for (lab,val,sub),x,cc in ((L,300,NAVY),(R,780,WARN)):
        cfit(d,460,lab,64,cc,x=x,maxw=440); cfit(d,640,val,104,cc,x=x,maxw=440)
        if sub: cfit(d,820,sub,50,SAND,x=x,maxw=440)
    if bottom:
        for i,t in enumerate(bottom if isinstance(bottom,list) else [bottom]): cfit(d,1230+i*120,t,84,bc)
def S_bars(d,b,lines,items,unit='',c=NAVY,size=76):
    cap(d,lines,c,size); n=len(items); mx=max(abs(v) for _,v,*r in items) or 1
    y0=440; h=min(265,1270//n)
    for i,it in enumerate(items):
        lab,v=it[0],it[1]; cc=it[2] if len(it)>2 else (WARN if v<0 else NAVY)
        y=y0+i*h; d.text((80,y),lab,font=F(56),fill=NAVY)
        bh=min(120,h-96); w=int(640*abs(v)/mx); d.rounded_rectangle((80,y+76,80+max(w,14),y+76+bh),16,fill=cc)
        txt=it[3] if len(it)>3 else (f'{v:+}' if isinstance(v,int) else f'{v:+.1f}')+unit
        tw=d.textlength(txt,font=F(60))
        if 100+max(w,14)+tw>1050: d.text((80+w-16-tw,y+76+bh//2-32),txt,font=F(60),fill=WH)
        else: d.text((100+max(w,14),y+76+bh//2-32),txt,font=F(60),fill=cc)
    yb=y0+n*h
    if yb<1330: person(d,540,yb+110,0.6,face='smile',shirt=MID)
CTA=('사진 한 장 보내 주시면','무료로 봐 드립니다')   # 10/12 11:46 사용자 「6번 적용 전번도 공개」 — 인테리어 끝 장면은 문의 창구로
def S_end(d,b,lines,sub,sub2='블로그에 정리했습니다',tel=None):
    if b=='int':
        cap(d,lines,WH,74)
        cfit(d,430,CTA[0],86,Y); cfit(d,540,CTA[1],96,Y)
        person(d,540,860,0.7,face='smile',shirt=OK)
        t=tel or BRAND['int'][1]
        cfit(d,1180,t,120,WH,maxw=1000)
        cfit(d,1340,'전화 · 문자 모두 됩니다',58,Y)
        cfit(d,1460,'두 공정 넘게 맡기면 견적에서 3% 할인',50,WH)   # 10/12 11:58 사용자
        cfit(d,1540,'blog.naver.com/champion_chart',42,PALE)
        return
    cap(d,lines,WH,78); cfit(d,600,sub[0],88,Y)
    if len(sub)>1: cfit(d,730,sub[1],88,Y)
    person(d,540,1060,0.8,face='smile',shirt=OK)
    cfit(d,1400,sub2,52,PALE); cfit(d,1470,'블로그에 정리했습니다',52,PALE)
    cfit(d,1600,tel if tel else ((BRAND[b][0]+' '+BRAND[b][1]) if b=='int' else BRAND[b][1]),48,Y if (b=='int' or tel) else PALE)
    if tel: cfit(d,1670,'blog.naver.com/champion_chart',40,PALE)
def S_quote(d,b,lines,q,who='',c=NAVY,size=76,face='smile'):
    cap(d,lines,c,size); person(d,300,900,0.9,face=face,shirt=WARN); person(d,780,900,0.9,face='shock',shirt=MID)
    bubble(d,70,1260,940,260,q if isinstance(q,list) else [q],size=58,fill=CREAM)
    if who: cfit(d,1600,who,54,SAND)
def S_steps(d,b,lines,steps,c=NAVY,size=76):
    cap(d,lines,c,size); n=len(steps); y0=440; h=min(270,1260//n)
    for i,(a,bb) in enumerate(steps):
        y=y0+i*h; d.ellipse((80,y+10,80+100,y+110),fill=NAVY if i<n-1 else WARN); ctext(d,y+22,str(i+1),F(62),WH,130)
        d.text((210,y+4),a,font=fit(d,a,66,780),fill=NAVY); d.text((210,y+92),bb,font=fit(d,bb,50,780),fill=SAND)
        if i<n-1: d.line((130,y+110,130,y+h+10),fill=(200,195,185),width=6)
    yb=y0+n*h
    if yb<1330: person(d,540,yb+110,0.6,face='smile',shirt=MID)

def S_dog(d,b,lines,bub,face='happy',c=NAVY,size=78,slip=False,owner=None,owner_face='worry'):
    """강아지 캐릭터 장면 (10/9) — 강아지가 말풍선으로 말한다. owner를 주면 보호자가 옆에 선다."""
    cap(d,lines,c,size)
    if owner: _REALP(d,250,860,0.95,face=owner_face,shirt=MID); dog(d,700,880,1.15,face=face,slip=slip)
    else: dog(d,540,860,1.4,face=face,slip=slip)
    bubble(d,80,1330,920,230,bub,size=60,fill=CREAM)
def S_comic(d,b,lines,items,c=NAVY,size=78):
    """만화 장면 (10/9) — items: ('floor',y,kind[,x0,x1]) · ('dog',x,y,s,face,pose) · ('person',x,y,s,face) · ('sofa',x,y,s) · ('box',x,y,s,label)
    · ('sample',x,y,s) · ('hand',x,y,s) · ('boom',x,y,text,size) · ('speed',x,y,n,ln) · ('text',x,y,txt,size,color) · ('bubble',x,y,w,h,lines,size) · ('star',x,y,r)"""
    import comic as C
    cap(d,lines,c,size)
    for it in items:
        k=it[0]; a=it[1:]
        if k=='floor': C.floor(d,a[0],a[1],*(a[2:]))
        elif k=='cat': C.ccat(d,a[0],a[1],a[2],face=a[3],pose=a[4] if len(a)>4 else 'sit')
        elif k=='tower': C.tower(d,*a)
        elif k=='racc': C.racc(d,a[0],a[1],a[2],face=a[3],pose=a[4] if len(a)>4 else 'stand')
        elif k=='key': C.key(d,*a)
        elif k=='paper': C.paper(d,*a)
        elif k=='dog': C.cdog(d,a[0],a[1],a[2],face=a[3],pose=a[4] if len(a)>4 else 'sit')
        elif k=='person': _REALP(d,a[0],a[1],a[2],face=a[3],shirt=MID)
        elif k=='sofa': C.sofa(d,*a)
        elif k=='box': C.box(d,*a)
        elif k=='sample': C.sample(d,*a)
        elif k=='hand': C.hand(d,*a)
        elif k=='boom': C.boom(d,*a)
        elif k=='speed': C.speed(d,*a)
        elif k=='star': C.star(d,a[0],a[1],a[2],(240,190,40))
        elif k=='text': ctext(d,a[1],a[2],F(a[3]),a[4] if len(a)>4 else WARN,a[0])
        elif k=='bubble': bubble(d,a[0],a[1],a[2],a[3],a[4],size=a[5] if len(a)>5 else 60,fill=CREAM)
TYPES=dict(comic=S_comic,dog=S_dog,hook=S_hook,big=S_big,cards=S_cards,vs=S_vs,bars=S_bars,end=S_end,quote=S_quote,steps=S_steps)

def make(b,slug,scenes,durs,cover,info,outdir):
    os.makedirs(outdir,exist_ok=True); cwd=os.getcwd(); os.chdir(outdir)
    pre={'nm':'nangman_','int':'nangman_interior_','js':'jisandream_'}[b]
    files=[]
    for i,sc in enumerate(scenes):
        t=sc[0]; kw=sc[1]
        bg=NAVY if t=='end' else (kw.pop('bg',IV))
        im,d=base(bg); TYPES[t](d,b,**kw); foot(d,b,PALE if t=='end' else SAND)
        fn=f'{slug}_{i+1}.png'; im.save(fn); files.append(fn)
    mp4=f'{pre}{slug}_short.mp4'
    if not os.environ.get('NOMP4') and not (os.environ.get('SKIP') and os.path.exists(mp4)): assemble(files,durs,mp4)
    Image.open(files[cover-1]).save(f'{pre}{slug}_cover.png')
    ims=[Image.open(f).resize((270,480)) for f in files]
    c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)]; c.save(f'/tmp/claude-0/sheet_{slug}.png')
    tot=sum(durs)
    capn=info['cap']; tags=' '.join(info['tags5'])
    captxt=capn+' '+tags
    sc_lines='\n'.join(f'{i+1:<2} {s:<40} {dd:.1f}초' for i,(s,dd) in enumerate(zip(info['scenes'],durs)))
    TEL=info.get('tel',{'int':'010-7678-9967'}.get(b))   # 10/9 사용자: info에 전화 번호 — 전화가 올 수 있음
    telc=f"\n\n고정 댓글 (캡션 100자에 안 들어가서 댓글로)\n사진 한 장 보내 주시면 무료로 봐 드립니다 · 전화 · 문자 {TEL} · 사는 지역과 하고 싶은 공사를 말씀해 주세요" if TEL else ''
    teld=(f"\n\n사진 한 장 보내 주시면 무료로 봐 드립니다.\n전화 · 문자 {TEL}" if b=='int' else f"\n\n전화 문의 {TEL}") if TEL else ''
    txt=f"""{info['name']} 숏폼 · 1080×1920 · {tot:.1f}초
파일: {mp4}
=====================================


[ 네이버 클립 ]

캡션 ({len(captxt)}자)
{captxt}

대표 이미지
{pre}{slug}_cover.png (장면 {cover})

연결할 글
{info['title']}
{info.get('url','(발행 뒤 링크)')}{telc}


[ 유튜브 쇼츠 ]

제목
{info['yt']} #shorts

설명
{info['desc']}{teld}

전체 내용은 블로그에 있습니다.
{info.get('url','(발행 뒤 링크)')}

{' '.join(info['tags10'])}

해시태그 (쇼츠용 짧게)
#shorts {tags}


[ 장면 ]

{sc_lines}


[ 자료 ]

{info['src']}
"""
    open(f'{pre}{slug}_short_info.txt','w').write(txt)
    os.chdir(cwd)
    print(slug,f'{tot:.1f}초',f'캡션 {len(captxt)}자',' 경고: 캡션 100자 초과' if len(captxt)>100 else '')
    return [f'{outdir}/{mp4}',f'{outdir}/{pre}{slug}_cover.png',f'{outdir}/{pre}{slug}_short_info.txt']

import sys,math,io,os,urllib.request,time
sys.path.insert(0,'/home/claude/blogkit')
from PIL import Image,ImageDraw
from thumbnail import F
NAVY=(31,56,100); WARN=(181,83,60); MID=(46,92,138); GREY=(120,120,120)
def deg2px(lat,lon,z):
    n=2**z; x=(lon+180)/360*n*256; y=(1-math.log(math.tan(math.radians(lat))+1/math.cos(math.radians(lat)))/math.pi)/2*n*256; return x,y
def tile(z,x,y):
    p=f'/tmp/tiles/{z}_{x}_{y}.png'
    if not os.path.exists(p):
        os.makedirs('/tmp/tiles',exist_ok=True)
        d=urllib.request.urlopen(urllib.request.Request(f'https://tile.openstreetmap.org/{z}/{x}/{y}.png',headers={'User-Agent':'nangman-blog-map/1.0'}),timeout=30).read(); open(p,'wb').write(d); time.sleep(0.2)
    return Image.open(p).convert('RGB').resize((512,512),Image.LANCZOS)
def basemap(lat0,lat1,lon0,lon1,z):
    x0,y0=deg2px(lat1,lon0,z); x1,y1=deg2px(lat0,lon1,z)
    tx0,ty0,tx1,ty1=int(x0//256),int(y0//256),int(x1//256),int(y1//256)
    im=Image.new('RGB',((tx1-tx0+1)*512,(ty1-ty0+1)*512))
    for tx in range(tx0,tx1+1):
        for ty in range(ty0,ty1+1): im.paste(tile(z,tx,ty),((tx-tx0)*512,(ty-ty0)*512))
    ox,oy=tx0*256,ty0*256
    im=im.crop((int((x0-ox)*2),int((y0-oy)*2),int((x1-ox)*2),int((y1-oy)*2)))
    P=lambda la,lo:((deg2px(la,lo,z)[0]-x0)*2,(deg2px(la,lo,z)[1]-y0)*2)
    return im,P
def label(d,xy,t,size=34,c=NAVY,dx=0,dy=-60,bg=(255,255,255,235)):
    size=int(size*1.7); dx=int(dx*1.6); dy=int(dy*1.6); f=F(size,False,True); w=d.textlength(t,font=f); x,y=xy[0]+dx,xy[1]+dy
    d.rounded_rectangle((x-w/2-14,y-size/2-10,x+w/2+14,y+size/2+12),10,fill=bg,outline=c,width=3); d.text((x-w/2,y-size/2-4),t,font=f,fill=c)
def dot(d,xy,c,r=16):
    r=int(r*1.5)
    d.ellipse((xy[0]-r,xy[1]-r,xy[0]+r,xy[1]+r),fill='white',outline=c,width=7)
def frame(im,dst,kick,title,note):
    W=1400; h=int(im.height*(W-120)/im.width); im=im.resize((W-120,h),Image.LANCZOS)
    top=178; Hh=h+top+170
    c=Image.new('RGB',(W,Hh),'#F7F5F0'); d=ImageDraw.Draw(c)
    d.rectangle([0,0,W,12],fill='#D9B44A')
    d.text((60,42),kick,font=F(30,False,False),fill=MID); d.text((60,84),title,font=F(44,False,True),fill=NAVY)
    c.paste(im,(60,top)); d.rectangle([58,top-2,60+im.width+1,top+im.height+1],outline='#C7D6E6',width=3)
    d.text((60,top+im.height+28),note,font=F(28,False,False),fill=(90,106,120))
    d.text((60,Hh-58),'지도 © OpenStreetMap contributors',font=F(22,False,False),fill=(154,164,174))
    t='낭만 부동산 분석 플랫폼  blog.naver.com/dong_jin_kim'; f=F(24,False,False); d.text((W-60-d.textlength(t,font=f),Hh-58),t,font=f,fill=(154,164,174))
    c.save(dst)
S={'송도':(37.429714,126.654485),'원인재':(37.41240556,126.68790556),'인천대입구':(37.38594,126.6394),'인하대':(37.4485,126.6496),'초지':(37.32057,126.80592),'어천':(37.24972222,126.90916667)}
O='/mnt/user-data/outputs/nangman_new/nangman_'
# map1 local
im,P=basemap(37.372,37.462,126.605,126.712,14)
d=ImageDraw.Draw(im,'RGBA')
# 인천1호선 국제도시~원인재 (schematic)
d.line([P(*S['인천대입구']),P(37.400,126.6555),P(37.4085,126.6745),P(*S['원인재'])],fill=(122,166,214,255),width=18)
# 수인분당선 원인재~송도~인하대
d.line([P(*S['원인재']),P(37.4230,126.6700),P(*S['송도']),P(37.4400,126.6500),P(*S['인하대'])],fill=(230,180,40,255),width=18)
# BRT 계획 인하대~송도~인천대입구 (dashed)
pts=[P(*S['인하대']),P(37.437,126.640),P(*S['송도']),P(37.410,126.645),P(*S['인천대입구'])]
for a,b in zip(pts,pts[1:]):
    n=int(math.dist(a,b)//40)
    for k in range(n):
        if k%2==0: d.line([(a[0]+(b[0]-a[0])*k/n,a[1]+(b[1]-a[1])*k/n),(a[0]+(b[0]-a[0])*(k+1)/n,a[1]+(b[1]-a[1])*(k+1)/n)],fill=(181,83,60,220),width=12)
for k,c in [('원인재',MID),('인천대입구',MID),('인하대',MID)]: dot(d,P(*S[k]),c)
dot(d,P(*S['송도']),WARN,22)
label(d,P(*S['송도']),'송도역 · 인천발 KTX 출발',36,WARN,0,-72)
label(d,P(*S['원인재']),'원인재역 · 환승',30,MID,-20,-62)
label(d,P(*S['인천대입구']),'인천대입구역 · GTX-B 예정',30,MID,40,70)
label(d,P(*S['인하대']),'인하대역',28,MID,90,-10)
label(d,P(37.4205,126.628),'옥련동 (원도심)',30,(110,100,90),0,0)
label(d,P(37.392,126.660),'송도국제도시',34,NAVY,0,0)
# legend
L=[((122,166,214),'인천1호선'),((230,180,40),'수인분당선 · KTX 같은 선로'),((181,83,60),'BRT 계획 (2028~2030년)')]
for i,(c,t) in enumerate(L):
    y=40+i*80; d.rounded_rectangle((24,y-10,900,y+66),10,fill=(255,255,255,235)); d.line([(44,y+28),(140,y+28)],fill=c+(255,),width=16); d.text((160,y),t,font=F(46,False,True),fill=NAVY)
frame(im,O+'sd2_map1.png','인천발 KTX · 송도역 위치','송도역 KTX 위치, 송도국제도시가 아니라 옥련동입니다','송도국제도시에서는 인천1호선 → 원인재역 환승 → 수인분당선 송도역 · 선 위치는 개략도')
# map2 route
im,P=basemap(37.215,37.465,126.600,126.985,12)
d=ImageDraw.Draw(im,'RGBA')
d.line([P(*S['송도']),P(37.405,126.700),P(37.380,126.735),P(*S['초지']),P(37.300,126.840),P(37.275,126.875),P(*S['어천'])],fill=(230,180,40,255),width=20)
e=P(*S['어천']); g=P(37.228,126.975)
d.line([e,g],fill=(181,83,60,255),width=20)
d.polygon([g,(g[0]-36,g[1]-10),(g[0]-18,g[1]-34)],fill=(181,83,60,255))
for k in ['초지','어천']: dot(d,P(*S[k]),MID,18)
dot(d,P(*S['송도']),WARN,24)
label(d,P(*S['송도']),'송도역 · 출발',36,WARN,150,50)
label(d,P(*S['초지']),'초지역 (안산)',32,MID,0,-66)
label(d,P(*S['어천']),'어천역 (화성)',32,MID,-40,-66)
label(d,g,'경부고속선 → 부산·목포',30,WARN,-200,-75)
L=[((230,180,40),'수인선 선로 그대로 이용'),((181,83,60),'어천역~경부고속선 새 선로 3.19㎞')]
for i,(c,t) in enumerate(L):
    y=40+i*80; d.rounded_rectangle((24,y-10,1000,y+66),10,fill=(255,255,255,235)); d.line([(44,y+28),(140,y+28)],fill=c+(255,),width=16); d.text((160,y),t,font=F(46,False,True),fill=NAVY)
frame(im,O+'sd2_map2.png','인천발 KTX · 노선과 정차역','인천발 KTX 노선, 송도역 → 초지역 → 어천역 → 경부고속선','역 위치는 실제 좌표 · 선은 개략도 · 개통 2027년 상반기 목표')
print('ok')

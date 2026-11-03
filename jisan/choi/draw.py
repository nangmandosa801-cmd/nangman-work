import urllib.request,json,math,io,sys
sys.path.insert(0,'/home/claude/blogkit')
from PIL import Image,ImageDraw
from thumbnail import F
H={'User-Agent':'jisandream-blog/1.0'}
P=json.load(open('poly.json'))
def xy(lat,lon,z):
    n=2**z; x=(lon+180)/360*n; y=(1-math.log(math.tan(math.radians(lat))+1/math.cos(math.radians(lat)))/math.pi)/2*n; return x*256,y*256
def tile(z,x,y):
    u=f'https://a.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png'
    im=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read())).convert('RGB')
    return im.resize((256,256)) if im.width!=256 else im
def basemap(lat0,lon0,lat1,lon1,z,scale=2):
    x0,y0=xy(lat0,lon0,z); x1,y1=xy(lat1,lon1,z)
    tx0,ty0,tx1,ty1=int(x0//256),int(y0//256),int(x1//256),int(y1//256)
    can=Image.new('RGB',((tx1-tx0+1)*256,(ty1-ty0+1)*256))
    for tx in range(tx0,tx1+1):
        for ty in range(ty0,ty1+1):
            u=f'https://tile.openstreetmap.org/{z}/{tx}/{ty}.png'
            im=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read())).convert('RGB')
            can.paste(im,((tx-tx0)*256,(ty-ty0)*256))
    ox,oy=tx0*256,ty0*256
    crop=(int(x0-ox),int(y0-oy),int(x1-ox),int(y1-oy))
    can=can.crop(crop); can=can.resize((can.width*2,can.height*2),Image.LANCZOS)
    f=lambda la,lo:((xy(la,lo,z)[0]-ox-crop[0])*2,(xy(la,lo,z)[1]-oy-crop[1])*2)
    return can,f
def rings(g):
    if g['type']=='Polygon': return [g['coordinates'][0]]
    return [p[0] for p in g['coordinates']]
def poly(d,f,g,fill,outline,w):
    for r in rings(g):
        pts=[f(la,lo) for lo,la in r]; d.polygon(pts,fill=fill); d.line(pts+[pts[0]],fill=outline,width=w)
def center(g):
    r=max(rings(g),key=len); return sum(p[1] for p in r)/len(r), sum(p[0] for p in r)/len(r)
def label(d,x,y,t,size=34,c=(13,59,92)):
    f=F(size,False,True); w=d.textlength(t,font=f)
    d.rounded_rectangle((x-w/2-14,y-size/2-10,x+w/2+14,y+size/2+12),12,fill=(255,255,255,235),outline=c,width=3)
    d.text((x-w/2,y-size/2-4),t,font=f,fill=c)
def frame(im,dst,kick,title,note):
    W=1400; h=int(im.height*(W-120)/im.width); im=im.resize((W-120,h))
    top=178; bot=130; Hh=h+top+bot+40
    c=Image.new('RGB',(W,Hh),'#F4F6F8'); d=ImageDraw.Draw(c)
    d.rectangle([0,0,W-1,Hh-1],outline='#0D3B5C',width=6); d.rectangle([0,0,W,14],fill='#1B7A9E')
    d.text((60,42),kick,font=F(30,False,False),fill='#1B7A9E'); d.text((60,84),title,font=F(44,False,True),fill='#0D3B5C')
    d.rectangle([50,top-10,50+im.width+19,top+im.height+9],fill='#FFFFFF',outline='#9CBBCC',width=3); c.paste(im,(60,top))
    d.text((60,top+im.height+30),note,font=F(28,False,False),fill='#5A6A78')
    s='지도 © OpenStreetMap contributors'; d.text((60,Hh-58),s,font=F(22,False,False),fill='#9AA4AE')
    t='지산드림  blog.naver.com/jisandream01'; f=F(24,False,False); d.text((W-60-d.textlength(t,font=f),Hh-58),t,font=f,fill='#9AA4AE')
    c.save(dst)
O='/mnt/user-data/outputs/jisandream/'
# map1 wide
im,f=basemap(37.565,127.115,37.495,127.235,13)
im=im.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
for k in ['감북동','광암동','감일동','교산동','춘궁동']: poly(d,f,P[k],(120,130,140,40),(90,100,110,200),4)
poly(d,f,P['초이동'],(27,122,158,110),(13,59,92,255),8)
im=Image.alpha_composite(im,ov).convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
for k in ['감북동','광암동','감일동','교산동']:
    la,lo=center(P[k]); x,y=f(la,lo); label(d,x,y,k if k!='교산동' else '교산신도시',30,(80,90,100))
la,lo=center(P['초이동']); x,y=f(la,lo); label(d,x,y,'초이동',44,(13,59,92))
x,y=f(37.5417742,127.2067037); label(d,x,y-40,'하남시청',30,(80,90,100))
x,y=f(37.530,127.125); label(d,x,y,'서울 강동구',30,(181,101,78)); x,y=f(37.503,127.125); label(d,x,y,'서울 송파구',30,(181,101,78))
frame(im,O+'jisandream_choi_map1.png','지산드림 · 하남 부동산 · 초이동 위치','하남 초이동, 서울 강동·송파와 교산신도시 사이','파란 면은 행정동 초이동(초이·초일·광암동) · 서쪽이 서울, 동쪽이 교산신도시와 하남시청')
# map2 zoom
g=P['초이동']; rs=rings(g)[0]; las=[p[1] for p in rs]; los=[p[0] for p in rs]
im,f=basemap(max(las)+0.003,min(los)-0.004,min(las)-0.003,max(los)+0.004,15)
im=im.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
poly(d,f,g,(27,122,158,45),(13,59,92,255),8)
im=Image.alpha_composite(im,ov).convert('RGB')
frame(im,O+'jisandream_choi_map2.png','지산드림 · 하남 토지 · 초이동 토지와 도로','초이동 안에서도 도로가 닿는 땅은 일부입니다','파란 선은 행정동 초이동(초이·초일·광암동) · 흰 선과 노란 선이 도로, 녹색 면이 숲과 산지')
print('ok')
# map3 교통
im,f=basemap(37.575,127.130,37.495,127.225,14)
im=im.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
poly(d,f,P['초이동'],(27,122,158,70),(13,59,92,255),7)
im=Image.alpha_composite(im,ov).convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
ST=[('강일역 (5호선)',37.5570720,127.1751400,(0,-70)),('상일동역 (5호선)',37.5569597,127.1680417,(-120,-20)),('하남풍산역 (5호선)',37.5519584,127.2036311,(0,-60)),('하남시청역 (5호선)',37.5417742,127.2067037,(40,55))]
for n,la,lo,(dx,dy) in ST:
    x,y=f(la,lo); d.ellipse((x-16,y-16,x+16,y+16),fill=(142,68,173),outline='white',width=5)
    label(d,x+dx,y+dy,n,28,(110,50,140))
la,lo=center(P['초이동']); x,y=f(la,lo); label(d,x,y,'초이동',42,(13,59,92))
frame(im,O+'jisandream_choi_map3.png','지산드림 · 하남 부동산 · 초이동 교통','초이동에서 가까운 역과 초이IC·서하남IC','보라 점은 5호선 역 · 초이나들목(21)이 초이IC, 서하남(4)이 서하남IC')
print('map3 ok')

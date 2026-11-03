import sys,os,json
os.chdir('/home/claude/jisan/choi')
src=open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0]
exec(src)
print(list(P.keys()))
g=P['감북동']; rs=rings(g); las=[p[1] for r in rs for p in r]; los=[p[0] for r in rs for p in r]
print('감북동 범위',min(las),max(las),min(los),max(los))
O='/mnt/user-data/outputs/jisandream/'
im,f=basemap(37.555,127.105,37.490,127.225,13)
im=im.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
for k in ['초이동','감일동','교산동','춘궁동']:
    if k in P: poly(d,f,P[k],(120,130,140,40),(90,100,110,200),4)
poly(d,f,P['감북동'],(27,122,158,110),(13,59,92,255),8)
im=Image.alpha_composite(im,ov).convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
for k in ['초이동','감일동','교산동']:
    if k in P:
        la,lo=center(P[k]); x,y=f(la,lo); label(d,x,y,k if k!='교산동' else '교산신도시',30,(80,90,100))
la,lo=center(P['감북동']); x,y=f(la,lo); label(d,x,y,'감북동',44,(13,59,92))
x,y=f(37.530,127.122); label(d,x,y,'서울 강동구',30,(181,101,78)); x,y=f(37.505,127.118); label(d,x,y,'서울 송파구',30,(181,101,78))
frame(im,O+'jisandream_gambuk_map1.png','지산드림 · 하남 부동산 · 감북동 위치','하남 감북동, 서울 송파 · 강동과 붙어 있습니다','파란 면이 감북동 · 서쪽이 서울, 북쪽이 초이동, 남쪽이 감일동입니다')
print('map ok')

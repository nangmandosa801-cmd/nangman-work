import os,math
os.chdir('/home/claude/jisan/choi')
exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
O='/mnt/user-data/outputs/jisandream/'
im,f=basemap(37.875,127.325,37.630,127.665,12)
im=im.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
# 공구 경계 지점(보도): 금남IC → 대성리 → 상천리 → 상색리 → 하색리 → 서천리 → 당림리
W=[('금남IC',37.65765,127.36634),('대성리',37.68404,127.37922),('상천리',37.77036,127.45421),('상색리',37.79634,127.47595),('하색리',37.8117,127.47924),('서천리',37.84082,127.55209),('당림리',37.83402,127.59912)]
R=(196,78,52)
pts=[f(la,lo) for _,la,lo in W]
def dashed(d,p,q,w,c,dash=34,gap=20):
    L=math.hypot(q[0]-p[0],q[1]-p[1]); n=int(L//(dash+gap))+1; ux,uy=(q[0]-p[0])/L,(q[1]-p[1])/L
    for i in range(n):
        a=i*(dash+gap); b=min(a+dash,L)
        d.line([(p[0]+ux*a,p[1]+uy*a),(p[0]+ux*b,p[1]+uy*b)],fill=c,width=w)
for p,q in zip(pts,pts[1:]):
    d.line([p,q],fill=R+(70,),width=44)
    dashed(d,p,q,14,R+(255,))
im=Image.alpha_composite(im,ov).convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
def pin(la,lo,t,c,dx=0,dy=-62,s=30,r=15):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='white',width=5)
    if t: label(d,x+dx,y+dy,t,s,c)
PUR=(142,68,173); GR=(80,90,100)
pin(37.68404,127.37922,'대성리역',PUR,150,10,28)
pin(37.7366,127.4272,'청평역',PUR,120,20,28)
pin(37.77036,127.45421,'상천역',PUR,-120,-10,28)
pin(37.81424,127.51104,'가평역',PUR,60,62,28)
pin(37.83197,127.55726,'굴봉산역',PUR,60,110,28)
pin(37.6717,127.49774,'설악 나들목 (서울양양고속도로)',GR,0,-62,26)
x,y=f(37.79173,127.52514); label(d,x,y+30,'남이섬',26,GR)
pin(37.65765,127.36634,'시작 · 남양주 화도 금남리',R,150,62,32,20)
pin(37.83402,127.59912,'끝 · 춘천 서면 당림리',R,40,70,32,20)
for (n,la,lo) in W[1:-1]:
    x,y=f(la,lo); d.ellipse((x-11,y-11,x+11,y+11),fill='white',outline=R,width=6)
def mid(i,t,dx,dy):
    x=(pts[i][0]+pts[i+1][0])/2; y=(pts[i][1]+pts[i+1][1])/2; label(d,x+dx,y+dy,t,30,R)
mid(0,'1공구',-110,-10); mid(1,'2공구',-120,-20); mid(2,'3공구',-120,-6); mid(4,'4공구',0,-64); mid(5,'5공구',40,-64)
x,y=f(37.86,127.43); label(d,x,y,'가평군',44,(13,59,92))
frame(im,O+'jisandream_gp_ipji_map1.png','지산드림 · 가평 부동산 · 제2경춘국도','제2경춘국도, 남양주 화도에서 가평을 지나 춘천까지 33.6km','빨간 점선은 공구 경계 마을을 이은 선이라 실제 도로 선과 다릅니다 · 2026년 9월 착공 · 2032년 목표')
print('map ok')

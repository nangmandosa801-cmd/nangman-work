exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
O='/mnt/user-data/outputs/jisandream/yangdo/'
im,f=basemap(38.18,127.10,37.42,127.98,10)
d=ImageDraw.Draw(im,'RGBA')
x,y=f(37.8314,127.5098); d.ellipse((x-24,y-24,x+24,y+24),fill=(201,150,46),outline='white',width=6); label(d,x,y-70,'가평군 (임야 매물)',40,(150,100,20))
for n,la,lo,dx,dy in [('남양주시',37.6359,127.2165,0,-50),('포천시',37.8948,127.2007,0,-50),('양평군',37.4916,127.4875,0,-50),('춘천시',37.8811,127.7298,0,-50),('홍천군',37.6967,127.8888,-40,-50),('화천군',38.1063,127.7080,0,50)]:
    x,y=f(la,lo); d.ellipse((x-16,y-16,x+16,y+16),fill=(13,59,92),outline='white',width=5); label(d,x+dx,y+dy,n,34,(13,59,92))
frame(im,O+'jisandream_imya_yangdo_fig2.png','지산드림 · 임야 양도세','가평 산은 가평과 맞닿은 여섯 시군에 살면 재촌','산에서 직선 30km 안에 살아도 재촌 · 주민등록과 실제 거주가 함께 있어야 함')
print('ok')

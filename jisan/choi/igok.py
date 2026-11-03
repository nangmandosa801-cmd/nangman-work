exec(open('draw.py').read().split('O=\'/mnt/user-data/outputs/jisandream/\'')[0])
O='/mnt/user-data/outputs/jisandream/'
im,f=basemap(37.905,127.475,37.800,127.570,13)
d=ImageDraw.Draw(im,'RGBA')
def pin(la,lo,t,c,dx=0,dy=-70,s=34,r=18):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='white',width=5); label(d,x+dx,y+dy,t,s,c)
x,y=f(37.8793,127.5267); d.ellipse((x-150,y-150,x+150,y+150),fill=(27,122,158,50),outline=(13,59,92,255),width=6)
pin(37.8793,127.5267,'북면 이곡리 (매물 인근)',(13,59,92),0,-200,40,20)
pin(37.8142,127.5110,'가평역 (경춘선·ITX)',(142,68,173),0,60,32)
pin(37.8312,127.5096,'가평군청',(80,90,100),-150,0,30)
frame(im,O+'jisandream_igok_map1.png','지산드림 · 가평 토지 매물 위치','가평 북면 이곡리, 가평시내에서 차로 10분','파란 원이 이곡리 일대 · 가평역·가평군청이 있는 가평읍 시내에서 북쪽 · 정확한 필지 경계는 지적도로 안내')
print('ok')

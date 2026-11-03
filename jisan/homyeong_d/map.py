import os
os.chdir('/home/claude/jisan/choi')
exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
O='/mnt/user-data/outputs/jisandream/'
im,f=basemap(37.790,127.385,37.680,127.530,13)
d=ImageDraw.Draw(im,'RGBA')
def pin(la,lo,t,c,dx=0,dy=-70,s=34,r=18):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='white',width=5); label(d,x+dx,y+dy,t,s,c)
x,y=f(37.7170,127.4585); d.ellipse((x-170,y-170,x+170,y+170),fill=(27,122,158,50),outline=(13,59,92,255),width=6)
pin(37.7170,127.4585,'청평면 호명리 (매물 인근)',(13,59,92),0,-225,40,20)
pin(37.7366,127.4272,'청평역 (경춘선)',(142,68,173),-40,-70,32)
pin(37.7489,127.4756,'호명호수',(80,90,100),120,0,30)
pin(37.7704,127.4542,'상천역',(142,68,173),0,-70,30)
frame(im,O+'jisandream_homyeong_map1.png','지산드림 · 가평 토지 매물 위치','가평 청평면 호명리, 청평역에서 직선 3.5km쯤입니다','파란 원이 호명리 일대 · 호명산 남쪽, 청평호 옆 마을입니다 · 정확한 필지 경계는 지적도로 안내합니다')
print('map ok')

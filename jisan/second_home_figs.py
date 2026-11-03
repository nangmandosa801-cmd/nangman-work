import os
os.chdir('/home/claude/jisan/choi')
exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
O='/mnt/user-data/outputs/jisandream/second_home/'
im,f=basemap(37.910,127.370,37.650,127.560,12)
d=ImageDraw.Draw(im,'RGBA')
GRN=(46,125,80); BLU=(13,59,92); GRY=(110,110,110)
def zone(la,lo,t,c,dx,dy,r=95):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c+(55,),outline=c+(255,),width=6); label(d,x+dx,y+dy,t,34,c)
def pin(la,lo,t,c,dx=0,dy=-60,s=30,r=14):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='white',width=4); label(d,x+dx,y+dy,t,s,c)
zone(37.8793,127.5266,'북면 이곡리 · 쉼터 세 곳',GRY,0,-140)
zone(37.7775,127.4543,'청평 상천리 · 4만 평',BLU,-40,-140)
zone(37.7294,127.4568,'청평 호명리 · 집 두 곳',GRN,250,0)
zone(37.6865,127.4013,'청평 삼회리 · 집 한 곳',GRN,180,-120)
pin(37.8142,127.5110,'가평역',(142,68,173),110,0)
pin(37.7366,127.4272,'청평역',(142,68,173),-110,0)
frame(im,O+'jisandream_second_home_map1.png','지산드림 · 세컨드홈 가평 땅 매물 위치','세컨드홈 가평, 집 지을 땅은 청평에 쉼터 땅은 북면에 있습니다','초록 = 집을 지을 땅 · 파랑 = 일부 보전관리 · 회색 = 쉼터 · 원은 마을 일대이고 필지 경계는 지적도로 안내합니다')
import sys; sys.path.insert(0,'/home/claude/blogkit')
from thumbnail import render_jisan
render_jisan('지산드림 · 세컨드홈 가평',['세컨드홈 가평','4억 이하 집 더 사도 1주택'],'취득세 50% 감면 · 가평 땅 매물 일곱 곳',O+'jisandream_second_home_thumb.png')
print('ok')

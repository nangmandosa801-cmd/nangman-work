exec(open('draw.py').read().split('O=\'/mnt/user-data/outputs/jisandream/\'')[0])
O='/mnt/user-data/outputs/jisandream/imya/'
im,f=basemap(37.915,127.355,37.655,127.585,12)
d=ImageDraw.Draw(im,'RGBA')
def pin(la,lo,t,c,dx=0,dy=-70,s=34,r=18):
    x,y=f(la,lo); d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='white',width=5); label(d,x+dx,y+dy,t,s,c)
def ring(la,lo,rr=95):
    x,y=f(la,lo); d.ellipse((x-rr,y-rr,x+rr,y+rr),fill=(27,122,158,45),outline=(13,59,92,255),width=5)
for la,lo in [(37.68651,127.40132),(37.71695,127.45848),(37.77752,127.45437),(37.87931,127.52668)]: ring(la,lo)
pin(37.87931,127.52668,'북면 이곡리 · 3곳',(13,59,92),0,-130,36,20)
pin(37.77752,127.45437,'청평 상천리 · 4만 평',(13,59,92),210,-40,34,20)
pin(37.71695,127.45848,'청평 호명리 · 2곳',(13,59,92),200,30,34,20)
pin(37.68651,127.40132,'청평 삼회리 · 2,962평',(13,59,92),0,120,34,20)
pin(37.73625,127.42680,'청평역',(142,68,173),-130,0,28)
pin(37.81424,127.51104,'가평역',(142,68,173),-130,0,28)
frame(im,O+'jisandream_imya_maemae_map1.png','지산드림 · 임야 매매 하는 방법','가평 임야 매물 일곱 곳, 청평 넷 · 북면 셋','파란 원이 매물이 있는 마을 · 정확한 필지 경계는 지적도로 안내')
print('map ok')

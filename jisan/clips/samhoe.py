exec(open('/home/claude/jisan/clips/jclip.py').read())
O='/mnt/user-data/outputs/jisandream/clip_samhoe'; os.makedirs(O,exist_ok=True); os.chdir(O)
def sv(im,n): im.save(f's{n}.png')
def foot2(d,c=SAND): ctext(d,1830,'지산드림 · 가평 토지 매물',F(40,False),c)
def mountain(d,y=1100):
    d.polygon([(0,y),(260,y-380),(520,y)],fill=MNT); d.polygon([(380,y),(700,y-460),(1020,y)],fill=(80,125,92)); d.polygon([(760,y),(980,y-300),(1080,y-180),(1080,y)],fill=MNT)
def road(d,y,h=70,c=(120,125,130)):
    d.rectangle((0,y,1080,y+h),fill=c)
    for x in range(20,1080,140): d.rectangle((x,y+h//2-5,x+70,y+h//2+5),fill=(245,235,160))
def water(d,y):
    d.rectangle((0,y,1080,y+120),fill=WATER)
    for x in range(0,1080,120): d.arc((x,y+20,x+120,y+80),200,340,fill=WH,width=6)
# 1
im,d=jb(); cap(d,['서울 사는 김 과장','주말 집터를 찾습니다'],size=80)
for i,(x,h) in enumerate([(120,520),(330,700),(560,600),(780,760)]): apt(d,x,1250-h,190,h,(160,170,185),fl=7)
person(d,540,1330,0.7,face='o',shirt=DEEP)
bubble(d,120,1610,840,150,['계곡 소리 들리는 땅 없나…'],size=58,fill=(255,243,196))
foot2(d); sv(im,1)
# 2
im,d=jb(); cap(d,['가평 싼 임야 보러 갔더니','길이 없습니다'],size=74)
mountain(d,1150)
d.line((150,1300,930,1300),fill=RED,width=10); ctext(d,1330,'진입로 없음',F(70),RED)
person(d,540,1520,0.55,face='worry',shirt=DEEP)
ctext(d,1740,'길 내는 데 돈과 시간이 더 듭니다',F(50),SAND)
foot2(d); sv(im,2)
# 3
im,d=jb(); cap(d,['청평 삼회리 산 25-2','포장도로에 붙어 있습니다'],size=72)
mountain(d,1080)
d.polygon([(330,1080),(760,1080),(700,760),(420,720)],fill=(150,185,120),outline=CY,width=8)
ctext(d,880,'2,962평',F(70),WH)
road(d,1090,90)
ctext(d,1220,'3m 포장 법정도로',F(66),DEEP)
person(d,540,1420,0.6,face='smile',shirt=DEEP)
foot2(d); sv(im,3)
# 4
im,d=jb(); cap(d,['땅 앞에는','계곡이 흐릅니다'],size=86)
mountain(d,900); water(d,960)
ctext(d,1140,'졸졸졸',F(110),CY)
person(d,540,1400,0.7,face='smile',shirt=DEEP)
ctext(d,1680,'북한강도 걸어서 닿는 거리',F(58),SAND)
foot2(d); sv(im,4)
# 5
im,d=jb(); cap(d,['2,962평은','얼마나 넓을까'],size=86)
for k in range(2):
    x0=90+k*470; w=430 if k==0 else 160
    d.rectangle((x0,560,x0+w,1000),fill=(110,170,100),outline=WH,width=6)
    if k==0: d.line((x0+w//2,560,x0+w//2,1000),fill=WH,width=5); d.ellipse((x0+w//2-60,720,x0+w//2+60,840),outline=WH,width=5)
ctext(d,1060,'축구장 1.4개',F(110),DEEP)
ctext(d,1230,'약 9,792㎡',F(70),SAND)
person(d,540,1470,0.55,face='shock',shirt=DEEP)
foot2(d); sv(im,5)
# 6
im,d=jb(); cap(d,['가격은','총 2억 4,000만원'],size=86)
card(d,450,'길 없는 가평 대형 임야','평당 약 2만~7만원 (호가)',SAND)
d.rounded_rectangle((70,740,1010,1000),36,fill=(232,244,249),outline=CY,width=10)
ctext(d,780,'삼회리 산 25-2',F(68),CY); ctext(d,880,'평당 약 8만 1천원',F(66),DEEP)
card(d,1040,'다 만든 전원주택지','평당 약 70만원부터 (호가)',SAND)
ctext(d,1360,'도로 붙은 원형 임야 값',F(66),RED)
foot2(d); sv(im,6)
# 7
im,d=jb(); cap(d,['주말마다','어떻게 오가냐면'],size=86)
card(d,450,'청평시내','차로 5분',CY)
card(d,730,'청평역 ITX-청춘','청량리까지 약 35분',CY)
card(d,1010,'서종IC','서울양양고속도로',CY)
ctext(d,1330,'금요일 저녁·일요일 오후는 막힙니다',F(52),RED)
person(d,540,1500,0.5,face='smile',shirt=DEEP)
foot2(d); sv(im,7)
# 8
im,d=jb(DEEP); cap(d,['미리 알려 드리는 것'],c=WH,size=84)
for i,t in enumerate(['계획관리 + 보전관리 섞임','오른쪽 경계 끝 분묘 1기','2025년 산지전용 경사도 30도로 완화']):
    ctext(d,380+i*130,t,F(60),GOLD if i<2 else WH)
person(d,540,900,0.75,face='smile',shirt=CY)
ctext(d,1260,'서류 준비해서',F(66),WH); ctext(d,1350,'현장 같이 봐 드립니다',F(66),WH)
reg(d,(170,190,205)); foot2(d,(170,190,205)); sv(im,8)
assemble([f's{i}.png' for i in range(1,9)],[3.2,3.4,3.6,3.2,3.4,3.8,3.8,3.8],'jisandream_samhoe_short.mp4')
Image.open('s3.png').save('jisandream_samhoe_cover.png')
ims=[Image.open(f's{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_s.png')
print('ok')

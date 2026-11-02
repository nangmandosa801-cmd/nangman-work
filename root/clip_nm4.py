import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os
exec(open('clip_int2b.py').read().split('# ===== 투명 중문')[0].split('Y=(240,190,40)')[1])
Y=(240,190,40); WH=(255,255,255)
def footer(d,c=SAND): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),c)
def apt(d,x,y,w,h,c=(170,175,185),fl=6):
    d.rectangle((x,y,x+w,y+h),fill=c)
    for i in range(fl):
        for j in range(3): d.rectangle((x+20+j*(w-40)//3,y+20+i*(h-40)//fl,x+10+(j+1)*(w-40)//3,y+10+(i+1)*(h-40)//fl),fill=GLASS)
def end(l1,l2,sub):
    im,d=base(NAVY); ctext(d,560,l1,F(90),WH); ctext(d,690,l2,F(90),WH); ctext(d,900,sub,F(54,False),(220,215,200))
    ctext(d,1300,'낭만 부동산 분석 플랫폼',F(62),Y); ctext(d,1420,'실거래로 확인합니다',F(52,False),WH); return im
def bar(d,x,y,w,v,mx,c,lab,val):
    L=max(int(w*v/mx),40); d.rounded_rectangle((x,y,x+L,y+90),20,fill=c)
    if L>330: ctext(d,y+8,val,F(60),WH,x=x+L-130)
    else: d.text((x+L+24,y+8),val,font=F(60),fill=c if c!=(200,195,185) else SAND)
    d.text((x,y-92),lab,font=F(56),fill=NAVY)
O='/mnt/user-data/outputs/clip_nm4'; os.makedirs(O,exist_ok=True); os.chdir(O)

# ===== A 미사 감일
def sv(im,n): im.save(f'a{n}.png')
im,d=base(); caption(d,['미사 vs 감일','10억 오른 건 같은데'],size=80)
apt(d,120,560,360,800,(160,170,185)); apt(d,600,640,360,720,(175,165,150))
ctext(d,1400,'미사',F(80),MID,x=300); ctext(d,1400,'감일',F(80),WARN,x=780)
bubble(d,80,1560,920,200,['누가 더 빨리 올랐을까?'],size=70,fill=(255,243,196)); footer(d); sv(im,1)
im,d=base(); caption(d,['84㎡ 분양가'],size=84)
cards(d,[('미사강변푸르지오 (2013)','4억 3,800만원',MID),('힐스테이트포웰시티 (2018)','5억 7,200만원',WARN)],y0=480,h=300,gap=60,fs=(60,84))
ctext(d,1300,'감일이 1억 4천 비쌌습니다',F(64),NAVY); footer(d); sv(im,2)
im,d=base(); caption(d,['올해 84㎡ 평균 거래가'],size=80)
cards(d,[('미사강변푸르지오','14억 2,488만원',MID),('힐스테이트포웰시티','15억 9,643만원',WARN)],y0=480,h=300,gap=60,fs=(60,84))
ctext(d,1300,'둘 다 약 10억 올랐습니다',F(66),NAVY); footer(d); sv(im,3)
im,d=base(); caption(d,['그런데 걸린 시간은'],size=84)
ctext(d,520,'미사 13년',F(130),MID); ctext(d,760,'감일 8년',F(130),WARN)
ctext(d,1100,'연평균 상승률',F(66),NAVY); ctext(d,1210,'9.7%  vs  13.5%',F(90),NAVY)
ctext(d,1500,'금액은 같고 속도는 감일',F(62),WARN); footer(d); sv(im,4)
im,d=base(); caption(d,['청약 경쟁률은','정반대였습니다'],size=80)
cards(d,[('미사강변푸르지오','약 1.2대 1',MID),('힐스테이트포웰시티','26.29대 1',WARN)],y0=500,h=300,gap=60,fs=(60,72))
ctext(d,1340,'싸게 산 미사는 배수가 컸습니다',F(58),NAVY); footer(d); sv(im,5)
im=end('금액은 비슷','속도는 감일','미사 13년 · 감일 8년'); sv(im,6)
assemble([f'a{i}.png' for i in range(1,7)],[3.0,3.4,3.4,3.8,3.4,3.2],'nangman_misa_gamil_short.mp4'); Image.open('a4.png').save('nangman_misa_gamil_cover.png')

# ===== B 그린벨트 503㎢
def sv(im,n): im.save(f'g{n}.png')
im,d=base(); caption(d,['그린벨트 풀어','집 7.3만 호 짓는다는데'],size=76)
d.rectangle((120,500,960,1400),fill=(120,165,110)); 
for x,y in ((250,700),(500,900),(760,650),(380,1150),(780,1200)): d.ellipse((x-60,y-60,x+60,y+60),fill=(80,130,75))
bubble(d,80,1560,920,200,['어디가 풀리는데?'],size=72,fill=(255,243,196)); footer(d); sv(im,1)
im,d=base(); caption(d,['후보지는','아직 발표 전'],size=88)
ctext(d,700,'?',F(400),SAND)
ctext(d,1320,'거론: 내곡·세곡·자곡 · 방이동 · 하남 감북',F(48),NAVY); ctext(d,1440,'확정된 곳은 없습니다',F(66),WARN); footer(d); sv(im,2)
im,d=base(); caption(d,['그런데 거래부터','먼저 묶었습니다'],c=WARN,size=82)
ctext(d,560,'503㎢',F(200),WARN)
ctext(d,880,'서울 19개 구 · 경기 10개 시 · 인천 계양',F(48),NAVY)
ctext(d,1000,'8월 18일 ~ 12월 31일',F(66),NAVY)
ctext(d,1300,'고양 109㎢ · 하남 70㎢',F(70),MID); footer(d); sv(im,3)
im,d=base(); caption(d,['묶이기 직전','하루 거래가'],size=84)
bar(d,120,600,820,5.5,22,MID,'평소','5.5건'); bar(d,120,880,820,21.8,22,WARN,'지정 직전 5일','21.8건'); bar(d,120,1160,820,2.2,22,OK,'지정 뒤','2.2건')
ctext(d,1450,'막차 타려고 몰렸다가 멈춤',F(60),NAVY); footer(d); sv(im,4)
im,d=base(); caption(d,['하남 44건 중 28건은','같은 땅 한 필지'],size=76)
d.rectangle((200,520,880,1200),fill=(120,165,110))
for i in range(4):
    for j in range(7): d.rectangle((220+j*94,540+i*160,300+j*94,680+i*160),outline=WH,width=4)
ctext(d,1330,'항동 임야 하나가 28건으로 나뉘어 팔림',F(52),NAVY); ctext(d,1450,'건수와 땅 수는 따로 봐야',F(62),WARN); footer(d); sv(im,5)
im=end('후보지는 아직','거래는 먼저 묶임','503㎢ · 12월 31일까지'); sv(im,6)
assemble([f'g{i}.png' for i in range(1,7)],[3.0,3.2,3.6,3.8,3.6,3.2],'nangman_greenbelt_short.mp4'); Image.open('g3.png').save('nangman_greenbelt_cover.png')

# ===== C 하남 집값
def sv(im,n): im.save(f'h{n}.png')
im,d=base(); caption(d,['하남 집값','올해 17% 올랐다는데'],size=80)
person(d,540,900,1.0,face='worry',shirt=MID)
bubble(d,80,1500,920,240,['우리 집은','왜 그대로지?'],size=76,fill=(255,243,196)); footer(d); sv(im,1)
im,d=base(); caption(d,['작년 가격대별로','나눠 봤습니다'],size=80)
for i,(lab,v,c) in enumerate([('5억 이하',6.9,(200,195,185)),('5억~8억',14.6,MID),('8억~11억',18.7,NAVY),('11억 넘음',18.5,NAVY)]):
    bar(d,120,520+i*270,820,v,20,c,lab,f'{v}%')
footer(d); sv(im,2)
im,d=base(); caption(d,['싼 집은 7%','비싼 집은 18%'],c=WARN,size=88)
apt(d,140,700,300,600,(200,195,185),4); apt(d,620,500,320,800,(120,130,150),7)
ctext(d,1360,'6.9%',F(90),SAND,x=290); ctext(d,1360,'18.7%',F(90),NAVY,x=780)
ctext(d,1560,'차이가 1년 새 더 벌어졌습니다',F(58),NAVY); footer(d); sv(im,3)
im,d=base(); caption(d,['가장 많이 오른 곳'],size=84)
cards(d,[('미사강변효성해링턴 52㎡','7.00억 → 9.58억 · +36.9%',WARN),('미사강변트래지안 52㎡','+31.4%',MID),('감일센트레빌 60㎡','+30.7%',MID)],y0=440,h=280,gap=44,fs=(60,58))
footer(d); sv(im,4)
im,d=base(); caption(d,['내린 8곳은','모두 덕풍·신장'],size=84)
ctext(d,620,'8곳 중 5곳은',F(80),NAVY); ctext(d,740,'거래가 1건',F(110),WARN)
ctext(d,1000,'한 건 값에 결과가 바뀝니다',F(62),NAVY)
ctext(d,1300,'3.3㎡당 6,601만원 vs 1,784만원',F(56),MID); ctext(d,1400,'포웰시티 · 대동피렌체',F(50,False),SAND); footer(d); sv(im,5)
im=end('하남 17% 상승','5억 이하는 7%','같은 아파트 222곳 비교'); sv(im,6)
assemble([f'h{i}.png' for i in range(1,7)],[3.0,3.8,3.4,3.4,3.6,3.2],'nangman_hnjipgap_short.mp4'); Image.open('h2.png').save('nangman_hnjipgap_cover.png')
for p_,n in (('a',6),('g',6),('h',6)): sheet(p_,n,f'/tmp/claude-0/sheet_nm4{p_}.png')

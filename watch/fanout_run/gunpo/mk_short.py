# (원본 brain5bl) 브레인시티 대광로제비앙 그랜드센텀 사전점검 세로 숏폼 (10/25 fanout) — 만화 장면 · 큰 글자
# 이야기: 제휴 중문 시공팀 평택 동삭동 현장(신발장이 벽 끝까지 → 문짝 잘라 맞춤) · 겨울 제작 지연
import sys,os,subprocess
sys.path.insert(0,'/home/claude/sns/shorts1024'); sys.path.insert(0,'/home/claude/sns/shorts1018'); sys.path.insert(0,'/home/claude')
import mk_shorts1024 as M
import mk_shorts1018 as K
from mk_shorts1018 import *
from PIL import Image
IMG='/home/claude/watch/fanout_run/gunpo/img/'
OUTD='/home/claude/watch/fanout_run/gunpo/shorts'


def photo(im,d,name,y0=280,hh=620):
    ph=Image.open(IMG+name).convert('RGB')
    r=960/ph.width; ph=ph.resize((960,int(ph.height*r)))
    if ph.height>hh: ph=ph.crop((0,(ph.height-hh)//2,960,(ph.height-hh)//2+hh))
    im.paste(ph,(60,y0)); d.rectangle((60,y0,1020,y0+ph.height),outline=NAVY,width=8)
    return y0+ph.height
def s1(d):
    room(d); top(d,['베란다 장 뒤'],size=110)
    dog(d,300,1050,0.85,'worry','sit'); cat(d,780,1050,0.85,'shock','sit')
    bub(d,60,1420,960,300,['닦아도 겨울마다','또 핀다?'],100)
    return ['베란다 장 뒤','닦아도 겨울마다','또 핀다?']
def s2(im,d):
    top(d,['경기 군포 구축 아파트'],size=96)
    y=photo(im,d,'c4.jpg')
    ct(d,y+30,'창 옆 붙박이장',94,WARN,maxw=980)
    cat(d,540,1290,0.55,'worry','sit')
    bub(d,60,1500,960,260,['뒤로 바람이 안 돌아'],96)
    return ['경기 군포 구축 아파트','창 옆 붙박이장','뒤로 바람이 안 돌아']
def s3(im,d):
    top(d,['떼어 보니'],size=104)
    y=photo(im,d,'c5.jpg')
    ct(d,y+30,'숨어 있던 곰팡이',94,WARN,maxw=980)
    dog(d,540,1290,0.55,'shock','sit')
    bub(d,60,1500,960,260,['판부터 대면 안 돼!'],100)
    return ['떼어 보니','숨어 있던 곰팡이','판부터 대면 안 돼!']
def s4(im,d):
    top(d,['걷어 내고 살균'],size=104)
    y=photo(im,d,'c6.jpg')
    ct(d,y+30,'판 뒤에 가두지 않게',90,NAVY,maxw=980)
    rac(d,540,1290,0.55,'proud','point')
    bub(d,60,1500,960,260,['밑작업이 먼저!'],104)
    return ['걷어 내고 살균','판 뒤에 가두지 않게','밑작업이 먼저!']
def s5(im,d):
    top(d,['바깥 벽 전체 이보드'],size=96)
    y=photo(im,d,'c7.jpg')
    ct(d,y+30,'들뜸 없이 꼭 붙이기',92,WARN,maxw=980)
    dog(d,540,1290,0.55,'happy','point')
    bub(d,60,1500,960,260,['얼룩 한 곳 말고 전체!'],92)
    return ['바깥 벽 전체 이보드','들뜸 없이 꼭 붙이기','얼룩 한 곳 말고 전체!']
def END(d):
    top(d,['베란다 곰팡이','단열 상담'],WH,104,y=120)
    d.rounded_rectangle((60,420,1020,700),44,fill=Y)
    ct(d,450,'얼룩진 벽 한 장',86,NAVY,maxw=900); ct(d,570,'베란다 전체 한 장',86,NAVY,maxw=900)
    rac(d,540,1040,0.7,'happy','cheer')
    ct(d,1300,'문자 010-2882-8165',112,WH,maxw=1000)
    ct(d,1450,'수도권 11/30까지 5% 할인',80,Y,maxw=1000)
    ct(d,1590,'낭만 인테리어',96,Y,maxw=1000)
    return ['베란다 곰팡이','단열 상담','얼룩진 벽 한 장','베란다 전체 한 장','문자 010-2882-8165','수도권 11/30까지 5% 할인','낭만 인테리어']
scenes=[s1,s2,s3,s4,s5,END]; durs=[3.4,3.4,3.6,3.4,3.6,4.8]
od=f'{K.SCR}/s1025_gunpo'; os.makedirs(od,exist_ok=True); files=[]; texts=[]
for i,fn in enumerate(scenes):
    im,d=base(NAVY if fn is END else IV)
    if fn in (s2,s3,s4,s5): texts+=fn(im,d); foot(d)
    elif fn is END: texts+=fn(d)
    else: texts+=fn(d) or []; foot(d)
    p=f'{od}/{i+1:02d}.png'; im.save(p); files.append(p)
bad=[x for x in texts if BAN.search(x)]; print('금지어',bad)
raw=f'{od}/raw.mp4'; assemble(files,durs,raw)
w=bgm.make(f'{od}/bgm.wav',sum(durs),seed=211)
os.makedirs(OUTD,exist_ok=True)
v=f'{OUTD}/nangman_interior_gunpo_short.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',raw,'-i',w,'-filter:a','volume=0.6,loudnorm=I=-18:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',v],check=True)
print(v,sum(durs),os.path.getsize(v)//1024,'KB')
ims=[Image.open(f).resize((270,480)) for f in files]; c=Image.new('RGB',(270*len(files),480))
for i,x in enumerate(ims): c.paste(x,(270*i,0))
c.save(f'{OUTD}/sheet.jpg')

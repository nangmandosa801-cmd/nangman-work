# (원본 brain5bl) 브레인시티 대광로제비앙 그랜드센텀 사전점검 세로 숏폼 (10/25 fanout) — 만화 장면 · 큰 글자
# 이야기: 제휴 중문 시공팀 평택 동삭동 현장(신발장이 벽 끝까지 → 문짝 잘라 맞춤) · 겨울 제작 지연
import sys,os,subprocess
sys.path.insert(0,'/home/claude/sns/shorts1024'); sys.path.insert(0,'/home/claude/sns/shorts1018'); sys.path.insert(0,'/home/claude')
import mk_shorts1024 as M
import mk_shorts1018 as K
from mk_shorts1018 import *
from PIL import Image
IMG='/home/claude/watch/fanout_run/doorlock2/img/'
OUTD='/home/claude/watch/fanout_run/doorlock2/shorts'


def photo(im,d,name,y0=280,hh=620):
    ph=Image.open(IMG+name).convert('RGB')
    r=960/ph.width; ph=ph.resize((960,int(ph.height*r)))
    if ph.height>hh: ph=ph.crop((0,(ph.height-hh)//2,960,(ph.height-hh)//2+hh))
    im.paste(ph,(60,y0)); d.rectangle((60,y0,1020,y0+ph.height),outline=NAVY,width=8)
    return y0+ph.height
def s1(d):
    room(d); top(d,['이사 온 첫날'],size=110)
    K.doorframe(d,300,300,480,600)
    C.key(d,540,560,1.0)
    dog(d,300,1050,0.85,'happy','sit'); cat(d,780,1050,0.85,'worry','sit')
    bub(d,60,1420,960,300,['전에 살던 사람도','이 번호 알지?'],100)
    return ['이사 온 첫날','전에 살던 사람도','이 번호 알지?']
def s2(d):
    room(d); top(d,['번호부터','새로!'],size=110)
    d.rounded_rectangle((60,400,1020,720),40,fill=WH,outline=MID,width=9)
    ct(d,440,'번호 · 카드 · 지문',96,NAVY,maxw=900); ct(d,580,'전부 새로 등록',96,WARN,maxw=900)
    rac(d,540,1060,0.85,'proud','point')
    bub(d,60,1420,960,300,['옛 카드는','다 지우기!'],104)
    return ['번호부터','새로!','번호 · 카드 · 지문','전부 새로 등록','옛 카드는','다 지우기!']
def s3(im,d):
    top(d,['서울 잠실 어느 집'],size=100)
    y=photo(im,d,'dl2_jamsil_before.jpg')
    ct(d,y+30,'보조키 + 원형 손잡이',92,WARN,maxw=980)
    cat(d,540,1290,0.55,'shock','sit')
    bub(d,60,1500,960,260,['떼면 구멍이 두 개!'],100)
    return ['서울 잠실 어느 집','보조키 + 원형 손잡이','떼면 구멍이 두 개!']
def s4(im,d):
    top(d,['보강판으로 덮기'],size=104)
    y=photo(im,d,'dl2_jamsil_after.jpg')
    ct(d,y+30,'흰 판 위에 번호키 하나',90,NAVY,maxw=980)
    dog(d,540,1290,0.55,'happy','point')
    bub(d,60,1500,960,260,['감쪽같다!'],110)
    return ['보강판으로 덮기','흰 판 위에 번호키 하나','감쪽같다!']
def s5(im,d):
    top(d,['부산 학장동 빈집'],size=100)
    y=photo(im,d,'dl2_hakjang_after.jpg')
    ct(d,y+30,'이사 오기 전에 미리',94,WARN,maxw=980)
    rac(d,540,1290,0.55,'happy','point')
    bub(d,60,1500,960,260,['이삿날 바로 열림!'],100)
    return ['부산 학장동 빈집','이사 오기 전에 미리','이삿날 바로 열림!']
def END(d):
    top(d,['도어락 시공','전국 연결'],WH,104,y=120)
    d.rounded_rectangle((60,420,1020,700),44,fill=Y)
    ct(d,450,'서울 · 인천 · 부천',86,NAVY,maxw=900); ct(d,570,'경기 북부 · 부산',86,NAVY,maxw=900)
    rac(d,540,1040,0.7,'happy','cheer')
    ct(d,1300,'문자 010-2882-8165',112,WH,maxw=1000)
    ct(d,1450,'수도권 11/30까지 5% 할인',80,Y,maxw=1000)
    ct(d,1590,'낭만 인테리어',96,Y,maxw=1000)
    return ['도어락 시공','전국 연결','서울 · 인천 · 부천','경기 북부 · 부산','문자 010-2882-8165','수도권 11/30까지 5% 할인','낭만 인테리어']
scenes=[s1,s2,s3,s4,s5,END]; durs=[3.4,3.4,3.6,3.4,3.6,4.8]
od=f'{K.SCR}/s1025_doorlock2'; os.makedirs(od,exist_ok=True); files=[]; texts=[]
for i,fn in enumerate(scenes):
    im,d=base(NAVY if fn is END else IV)
    if fn in (s3,s4,s5): texts+=fn(im,d); foot(d)
    elif fn is END: texts+=fn(d)
    else: texts+=fn(d) or []; foot(d)
    p=f'{od}/{i+1:02d}.png'; im.save(p); files.append(p)
bad=[x for x in texts if BAN.search(x)]; print('금지어',bad)
raw=f'{od}/raw.mp4'; assemble(files,durs,raw)
w=bgm.make(f'{od}/bgm.wav',sum(durs),seed=137)
os.makedirs(OUTD,exist_ok=True)
v=f'{OUTD}/nangman_interior_doorlock2_short.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',raw,'-i',w,'-filter:a','volume=0.6,loudnorm=I=-18:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',v],check=True)
print(v,sum(durs),os.path.getsize(v)//1024,'KB')
ims=[Image.open(f).resize((270,480)) for f in files]; c=Image.new('RGB',(270*len(files),480))
for i,x in enumerate(ims): c.paste(x,(270*i,0))
c.save(f'{OUTD}/sheet.jpg')

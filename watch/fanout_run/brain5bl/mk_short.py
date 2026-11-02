# 브레인시티 대광로제비앙 그랜드센텀 사전점검 세로 숏폼 (10/25 fanout) — 만화 장면 · 큰 글자
# 이야기: 제휴 중문 시공팀 평택 동삭동 현장(신발장이 벽 끝까지 → 문짝 잘라 맞춤) · 겨울 제작 지연
import sys,os,subprocess
sys.path.insert(0,'/home/claude/sns/shorts1024'); sys.path.insert(0,'/home/claude/sns/shorts1018'); sys.path.insert(0,'/home/claude')
import mk_shorts1024 as M
import mk_shorts1018 as K
from mk_shorts1018 import *
from PIL import Image
IMG='/home/claude/watch/fanout_run/brain5bl/img/'
OUTD='/home/claude/watch/fanout_run/brain5bl/shorts'

def s1(d):
    room(d); top(d,['그랜드센텀 사전점검','10/30 ~ 11/1'],size=96)
    C.key(d,540,500,1.2)
    dog(d,300,1000,0.85,'happy','sit'); cat(d,780,1000,0.85,'worry','sit')
    bub(d,60,1420,960,300,['중문 달 건데','뭘 봐야 해?'],104)
    return ['그랜드센텀 사전점검','10/30 ~ 11/1','중문 달 건데','뭘 봐야 해?']
def s2(d):
    room(d); top(d,['평택 동삭동','어느 집 현관'],size=100)
    K.doorframe(d,120,380,420,640)
    d.rectangle((560,380,1000,1020),fill=(200,170,130),outline=(120,90,60),width=10)
    for k in range(3): d.line((560,380+k*213,1000,380+k*213),fill=(120,90,60),width=6)
    ct(d,600,'신발장',80,NAVY,x=780,maxw=400)
    cat(d,540,1060,0.75,'shock','sit')
    bub(d,60,1420,960,300,['신발장이','벽 끝까지!'],110)
    return ['평택 동삭동','어느 집 현관','신발장','신발장이','벽 끝까지!']
def s3(d):
    room(d); top(d,['문 박을 벽이','없다?!'],size=104)
    d.rounded_rectangle((60,400,1020,700),40,fill=WH,outline=MID,width=9)
    ct(d,450,'신발장 문짝을',92,NAVY,maxw=900); ct(d,570,'잘라서 문을 달았다',92,WARN,maxw=900)
    rac(d,540,1040,0.85,'proud','point')
    bub(d,60,1420,960,300,['점검 날','신발장 끝부터!'],104)
    return ['문 박을 벽이','없다?!','신발장 문짝을','잘라서 문을 달았다','점검 날','신발장 끝부터!']
def s4(d):
    room(d); top(d,['스위치 · 인터폰'],size=104)
    K.doorframe(d,300,330,480,640)
    d.rounded_rectangle((820,560,900,660),12,fill=WH,outline=NAVY,width=6)
    M.xmark(d,860,610,70) if hasattr(M,'xmark') else None
    dog(d,540,1050,0.8,'worry','point')
    bub(d,60,1420,960,300,['문이 닿을 벽에','붙어 있나?'],104)
    return ['스위치 · 인터폰','문이 닿을 벽에','붙어 있나?']
def s5(d):
    top(d,['줄자로 숫자 셋'],size=108)
    d.rounded_rectangle((40,300,1040,1000),36,fill=WH,outline=NAVY,width=8)
    for i,t in enumerate(['① 현관 폭','② 천장 높이','③ 옆 벽 길이']): ct(d,360+i*210,t,108,NAVY if i!=1 else WARN,maxw=920)
    room(d); cat(d,540,1150,0.6,'happy','sit')
    bub(d,60,1500,960,260,['사진은 두 장!'],110)
    return ['줄자로 숫자 셋','① 현관 폭','② 천장 높이','③ 옆 벽 길이','사진은 두 장!']
def s6(im,d):
    top(d,['1월 입주 = 겨울'],size=108)
    ph=Image.open(IMG+'nangman_interior_brain5bl_jungmun_02_m_open.jpg').convert('RGB')
    r=960/ph.width; ph=ph.resize((960,int(ph.height*r))); ph=ph.crop((0,(ph.height-560)//2,960,(ph.height-560)//2+560))
    im.paste(ph,(60,280)); d.rectangle((60,280,1020,840),outline=NAVY,width=8)
    ct(d,890,'중문 주문이 몰리는 때',96,WARN,maxw=980)
    dog(d,540,1250,0.6,'happy','point')
    bub(d,60,1500,960,260,['점검 날 문을 정하기!'],96)
    return ['1월 입주 = 겨울','중문 주문이 몰리는 때','점검 날 문을 정하기!']
def END(d):
    top(d,['공동구매 모집'],WH,110,y=150)
    d.rounded_rectangle((60,330,1020,640),44,fill=Y)
    ct(d,370,'사전점검 · 중문 · 줄눈',90,NAVY,maxw=900); ct(d,500,'치수 + 사진 두 장',96,NAVY,maxw=900)
    rac(d,540,1000,0.75,'happy','cheer')
    ct(d,1290,'문자 010-2882-8165',112,WH,maxw=1000)
    ct(d,1450,'11/30까지 견적 5% 할인',84,Y,maxw=1000)
    ct(d,1590,'낭만 인테리어',96,Y,maxw=1000)
    return ['공동구매 모집','사전점검 · 중문 · 줄눈','치수 + 사진 두 장','문자 010-2882-8165','11/30까지 견적 5% 할인','낭만 인테리어']

scenes=[s1,s2,s3,s4,s5,s6,END]; durs=[3.2,3.4,3.6,3.2,3.4,3.4,4.6]
od=f'{K.SCR}/s1025_brain5bl'; os.makedirs(od,exist_ok=True); files=[]; texts=[]
for i,fn in enumerate(scenes):
    im,d=base(NAVY if fn is END else IV)
    if fn is s6: texts+=fn(im,d); foot(d)
    elif fn is END: texts+=fn(d)
    else: texts+=fn(d) or []; foot(d)
    p=f'{od}/{i+1:02d}.png'; im.save(p); files.append(p)
bad=[x for x in texts if BAN.search(x)]; print('금지어',bad)
raw=f'{od}/raw.mp4'; assemble(files,durs,raw)
w=bgm.make(f'{od}/bgm.wav',sum(durs),seed=131)
os.makedirs(OUTD,exist_ok=True)
v=f'{OUTD}/nangman_interior_brain5bl_short.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',raw,'-i',w,'-filter:a','volume=0.6,loudnorm=I=-18:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',v],check=True)
print(v,sum(durs),os.path.getsize(v)//1024,'KB')
ims=[Image.open(f).resize((270,480)) for f in files]; c=Image.new('RGB',(270*7,480))
for i,x in enumerate(ims): c.paste(x,(270*i,0))
c.save(f'{OUTD}/sheet.jpg')

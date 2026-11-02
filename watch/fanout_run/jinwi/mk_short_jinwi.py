# 진위역 서희스타힐스 사전점검 세로 숏폼 (10/25 fanout) — 만화 장면 · 큰 글자
import sys,os,subprocess
sys.path.insert(0,'/home/claude/sns/shorts1024'); sys.path.insert(0,'/home/claude/sns/shorts1018'); sys.path.insert(0,'/home/claude')
import mk_shorts1024 as M
import mk_shorts1018 as K
from mk_shorts1018 import *
from PIL import Image
IMG='/home/claude/watch/fanout_run/jinwi/img/'
OUTD='/home/claude/watch/fanout_run/jinwi/shorts'

def s1(d):
    room(d); top(d,['진위역 서희스타힐스','사전점검 11/14~15'],size=92)
    C.key(d,540,520,1.2)
    dog(d,300,1000,0.85,'happy','sit'); cat(d,780,1000,0.85,'worry','sit')
    bub(d,60,1420,960,300,['어디부터','열어 봐야 하지?'],96)
    return ['진위역 서희스타힐스','사전점검 11/14~15','어디부터','열어 봐야 하지?']
def s2(d):
    top(d,['1,659세대 평형별'],size=100)
    M.row_table(d,280,'',[('59㎡','846세대'),('71㎡','580세대'),('84㎡','233세대')])
    room(d); rac(d,540,1330,0.7,'proud','point')
    bub(d,60,1500,960,260,['평형마다 볼 곳이 다름!'],84)
    return ['1,659세대 평형별','59㎡','846세대','71㎡','580세대','84㎡','233세대','평형마다 볼 곳이 다름!']
def s3(d):
    room(d); top(d,['59㎡는','팬트리 · 드레스룸'],size=96)
    M.doorframe(d,300,380,480,620) if hasattr(M,'doorframe') else K.doorframe(d,300,380,480,620)
    cat(d,540,1020,0.85,'shock','sit')
    bub(d,60,1420,960,300,['안쪽 바닥까지','사진 찰칵!'],100)
    return ['59㎡는','팬트리 · 드레스룸','안쪽 바닥까지','사진 찰칵!']
def s4(d):
    room(d); top(d,['71㎡는','욕실이 두 곳'],size=104)
    d.rounded_rectangle((60,420,1020,740),40,fill=WH,outline=MID,width=9)
    ct(d,460,'두드리기 → 물 붓기',84,NAVY,maxw=900); ct(d,600,'→ 세면대 밑 실리콘',84,WARN,maxw=900)
    dog(d,540,1030,0.85,'happy','point')
    bub(d,60,1420,960,300,['두 곳 다','같은 순서로!'],104)
    return ['71㎡는','욕실이 두 곳','두드리기 → 물 붓기','→ 세면대 밑 실리콘','두 곳 다','같은 순서로!']
def s5(d):
    room(d); top(d,['84㎡ C타입은','꺾인 창 모서리'],size=96)
    M.window(d,140,380,800,520)
    rac(d,540,1040,0.85,'wink','point')
    bub(d,60,1420,960,300,['실리콘을','가까이서 보기!'],100)
    return ['84㎡ C타입은','꺾인 창 모서리','실리콘을','가까이서 보기!']
def s6(im,d):
    top(d,['30세대가 모이면'],size=104)
    ph=Image.open(IMG+'nangman_interior_jinwi_parkview_sajeon_02_nano.jpg').convert('RGB').resize((960,556))
    im.paste(ph,(60,300)); d.rectangle((60,300,1020,856),outline=NAVY,width=8)
    ct(d,900,'욕실 나노코팅 무료',100,WARN,maxw=980)
    cat(d,540,1250,0.6,'love','sit')
    bub(d,60,1500,960,260,['물때가 덜 붙게!'],100)
    return ['30세대가 모이면','욕실 나노코팅 무료','물때가 덜 붙게!']
def END(d):
    top(d,['세대를 모으면'],WH,104,y=170)
    d.rounded_rectangle((60,360,1020,640),44,fill=Y)
    ct(d,400,'사전점검',96,NAVY,maxw=900); ct(d,510,'공동구매 단가로 안내',90,NAVY,maxw=900)
    rac(d,540,1000,0.75,'happy','cheer')
    ct(d,1300,'문자 010-2882-8165',110,WH,maxw=1000)
    ct(d,1460,'11/30까지 견적 5% 할인',80,Y,maxw=1000)
    ct(d,1600,'낭만 인테리어',96,Y,maxw=1000)
    return ['세대를 모으면','사전점검','공동구매 단가로 안내','문자 010-2882-8165','11/30까지 견적 5% 할인','낭만 인테리어']

scenes=[s1,s2,s3,s4,s5,s6,END]; durs=[3.2,3.6,3.0,3.4,3.0,3.4,4.4]
od=f'{K.SCR}/s1025_jinwi'; os.makedirs(od,exist_ok=True); files=[]; texts=[]
for i,fn in enumerate(scenes):
    im,d=base(NAVY if fn is END else IV)
    if fn is s6: texts+=fn(im,d); foot(d)
    elif fn is END: texts+=fn(d)
    else: texts+=fn(d) or []; foot(d)
    p=f'{od}/{i+1:02d}.png'; im.save(p); files.append(p)
bad=[x for x in texts if BAN.search(x)]; print('금지어',bad)
raw=f'{od}/raw.mp4'; assemble(files,durs,raw)
w=bgm.make(f'{od}/bgm.wav',sum(durs),seed=125)
os.makedirs(OUTD,exist_ok=True)
v=f'{OUTD}/nangman_interior_jinwi_seohui_short.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',raw,'-i',w,'-filter:a','volume=0.6,loudnorm=I=-18:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',v],check=True)
print(v,sum(durs),os.path.getsize(v)//1024,'KB')
# contact sheet
ims=[Image.open(f).resize((270,480)) for f in files]; c=Image.new('RGB',(270*7,480))
for i,x in enumerate(ims): c.paste(x,(270*i,0))
c.save(f'{OUTD}/sheet.jpg')

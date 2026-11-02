# 문자 답장 없는 중개사에게 일주일 뒤 보낼 「입주 준비 순서표」 (1080×1350 JPG) — python3 gift.py
import json,re,os
from PIL import Image,ImageDraw
from letter import F,NAVY,INK,GREY,GOLD,SOFT,_qr
import qrcode
OUT='/mnt/user-data/outputs/mail1018/gift'
# 단지별 내용 — 순서는 낭만 인테리어 발행 글(champion_chart)에서, 숫자는 단지 발행 글 또는 ipju_pub_plan.json에서만
BASE=['사전점검 날 현관 치수 재기','줄눈 · 탄성코트 · 중문','입주청소','새집증후군 · 코팅 · 매트','이삿짐 · 가전','입주 뒤 방충망 · 방묘창']  # 224437487580
D={
 'e편한세상 신곡 시그니처뷰':(['2026년 9월 입주 예정','옵션 중문 245만원'],   # 224444617706
   ['사전점검 날 현관 벽 확인','이사 2주 전 중문 실측','줄눈 · 탄성코트 · 필름','입주청소','새집증후군 · 중문','매트 · 이삿짐']),
 '검단호수공원역 풍경채 어바니티':(['10월 2일 입주 시작','옵션 중문 180만원'],  # 224443130434
   ['우리 집 타입 · 옵션 확인','중문 · 줄눈 · 탄성코트','입주청소','매트','가전 · 이삿짐']),
 '고양 장항 제일풍경채':(['12월 입주','옵션 중문 3연동 180만원'], BASE),        # ipju_pub_plan.json (글은 미발행)
 '디에이치 방배':(['9월부터 입주','옵션 자동 중문 244만원'],                     # 224437510757
   ['현관 벽 · 천장 확인','이사 2주 전 중문 실측','줄눈 · 탄성코트','입주청소','청소 끝나고 중문 설치','이삿짐 · 가전']),
 '송내역 푸르지오 센트비엔':(['2026년 9~10월 입주','옵션 중문 없음'],           # 224436104166
   ['사전방문 날 현관 치수 재기','중문 · 줄눈 · 탄성코트','입주청소','매트 · 상판 코팅','가전 · 이삿짐']),
 '신검단중앙역 센트레빌':(['2026년 10월 입주','옵션 중문 174만원'],             # 224436072769
   ['사전방문 날 현관 치수 재기','줄눈 · 탄성코트 · 중문','입주청소','새집증후군 · 코팅 · 매트','가전 · 이삿짐']),
 '영통역자이 프라시엘':(['12월 입주'], BASE),                                    # ipju_pub_plan.json (글 안 씀)
 '오산역 금강펜테리움 센트럴파크':(['2026년 10월 입주','옵션 중문 여닫이 126만원'], # 224442889901 · 224436127312
   ['사전점검 날 치수 재기','중문 · 줄눈 · 탄성코트','입주청소','매트','가전 · 이삿짐']),
}
BAN=['자리','갈','최고','프리미엄','가능성','헷갈','놓습니다','가정','까닭','견줘','1위','값','기준','차례로']
MAN={'신곡파크프라임보라부동산':'보라','센트비엔단지앞리치온부동산공인중개사사무소':'리치온','부동산뉴스 공인중개사사무소':'부동산뉴스','서천역아이파크 단지내공인중개사사무소':'서천역아이파크'}
def short(o):
    if o in MAN: return MAN[o]
    s=re.sub(r'\s+','',o)
    for t in ['공인중개사사무소','부동산공인중개사사무소','부동산중개','공인중개사']:
        if s.endswith(t) and len(s)>len(t): s=s[:-len(t)]; break
    return s
def josa(t):
    c=t[-1]; return '이' if (0xAC00<=ord(c)<=0xD7A3 and (ord(c)-0xAC00)%28) else '가'
def fit(d,t,w,fs,mn,wt='Bold'):
    while d.textlength(t,font=F(wt,fs))>w and fs>mn: fs-=1
    return fs
def make(x,no):
    W,H=1080,1350; im=Image.new('RGB',(W,H),SOFT); d=ImageDraw.Draw(im)
    office=x['office'].strip(); dj=x['danji']; facts,steps=D[dj]
    texts=[]
    d.rounded_rectangle([40,40,W-40,H-40],radius=40,fill='white',outline=NAVY,width=6)
    # 위 띠
    d.rounded_rectangle([46,46,W-46,150],radius=34,fill=NAVY); d.rectangle([46,110,W-46,150],fill=NAVY)
    top=office+josa(office)+' 드리는'; fs=fit(d,top,W-180,46,30); texts.append(top)
    d.text((W//2,98),top,font=F('Bold',fs),fill='white',anchor='mm')
    # 큰 제목
    y=190; tf=F('Black',78)
    words=(dj+' 입주 준비 순서').split(' '); lines=[]; ln=''
    for wd in words:
        if ln and d.textlength(ln+' '+wd,font=tf)>W-180: lines.append(ln); ln=wd
        else: ln=(ln+' '+wd).strip()
    lines.append(ln)
    if d.textlength(dj,font=tf)<=W-180: lines=[dj,'입주 준비 순서']
    if len(lines)>2: tf=F('Black',64)
    for l in lines: d.text((90,y),l,font=tf,fill=INK); texts.append(l); y+=tf.size+18
    y+=20; ft=' · '.join(facts); d.text((90,y),ft,font=F('Bold',38),fill=GOLD); texts.append(ft); y+=70
    d.line([(90,y),(W-90,y)],fill=(220,224,230),width=3); y+=34
    # 번호 단계
    n=len(steps); gap=(1010-y)//n; sf=54
    for s in steps: sf=min(sf,fit(d,s,W-90-190,56,52))
    for i,s in enumerate(steps,1):
        cy=y+gap//2-6
        d.ellipse([90,cy-34,158,cy+34],fill=NAVY); d.text((124,cy),str(i),font=F('Black',40),fill='white',anchor='mm')
        d.text((182,cy),s,font=F('Bold',sf),fill=INK,anchor='lm'); texts.append(s); y+=gap
    # 아래 작은 칸
    bx=[70,1040,W-70,H-70]; d.rounded_rectangle(bx,radius=26,fill=(253,248,236),outline=GOLD,width=4)
    qs=210; msg=f"SMSTO:01028828165:[{office}] 입주 준비 문의 / 단지: {dj} / 품목: "
    im.paste(_qr(msg,qs,qrcode.constants.ERROR_CORRECT_L),(W-100-qs,bx[1]+20))
    l1='입주 준비 쿠폰'; l2='두 곳 견적 무료 비교'; l3='QR을 찍으면 문자가 열립니다'; l4='낭만 인테리어'; l5='010-2882-8165'
    d.text((100,bx[1]+26),l1,font=F('Black',44),fill=NAVY)
    d.text((100,bx[1]+82),l2,font=F('Bold',40),fill=INK)
    d.text((100,bx[1]+136),l3,font=F('Medium',28),fill=GREY)
    d.text((100,bx[1]+176),l4+'  '+l5,font=F('Bold',34),fill=NAVY)
    assert d.textlength(l4+'  '+l5,font=F('Bold',34))<W-100-qs-30-100
    texts+= [l1,l2,l3,l4,l5]
    for t in texts:
        for b in BAN: assert b not in t,(b,t)
    fn=f"{OUT}/nangman_gift_{no:02d}_{short(office)}.jpg"; im.save(fn,quality=92); return fn,msg,sf
if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True)
    L=[x for x in json.load(open('brokers_010_msg.json')) if x.get('sent')]
    R=[]
    for i,x in enumerate(L,1):
        fn,msg,sf=make(x,i); R.append({'file':fn,'msg':msg}); print(fn,sf)
    json.dump(R,open('/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad/gift_qr.json','w'),ensure_ascii=False)

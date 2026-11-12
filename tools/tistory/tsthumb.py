"""티스토리 목록용 썸네일(1200x690 · 카드 비율 그대로 · 잘림 없음).
python3 tsthumb.py <제목> <out.png> [라벨]  /  import: make(title,out,label)
제목을 쉼표로 나눠 앞=검색어(크게 · 검정), 뒤에서 숫자 한 덩이=파랑 크게."""
import re, sys
from PIL import Image, ImageDraw, ImageFont
F='/home/claude/tools/tistory/fonts/Pretendard-'
INK,GRAY,ACC,BG,LINE='#191F28','#6B7684','#3182F6','#FFFFFF','#E5E8EB'
NUM=re.compile(r'(\d[\d,.]*\s*(?:억\s*\d[\d,]*\s*(?:천|만)?|억|천만|천|만원?|%포인트|%|곳|건|세대|배|㎡|원|필지|가구|년|ha)?(?:[~\-]\d[\d,.]*\s*(?:억|만|천|%|㎡)?)?)')
def font(w,s): return ImageFont.truetype(F+w+'.otf',s)
def wrap(d,t,f,maxw):
    out,cur=[], ''
    for ch in t.split(' '):
        nx=(cur+' '+ch).strip()
        if d.textlength(nx,font=f)<=maxw: cur=nx
        else: out.append(cur); cur=ch
    out.append(cur); return out
def pick(title):
    head,_,tail=title.partition(',')
    tail=tail.strip()
    m=NUM.search(tail) or NUM.search(head)
    big=m.group(1).strip() if m and m.group(1) and not re.fullmatch(r'\d{4}년?',m.group(1).strip()) else ''
    if not big and m:
        ms=[x.group(1).strip() for x in NUM.finditer(tail) if not re.fullmatch(r'\d{4}년?',x.group(1).strip())]
        big=ms[0] if ms else ''
    # 숫자 앞 한두 낱말을 붙여 뜻이 보이게
    ctx=''
    if big and big in tail:
        pre=tail[:tail.index(big)].split()[-2:]
        ctx=' '.join(pre)
    return head.strip(), ctx, big
def make(title,out,label='낭만 부동산 노트'):
    W,H=1200,690; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    head,ctx,big=pick(title)
    d.rectangle([0,0,W,12],fill=ACC)
    d.text((80,78),label,font=font('SemiBold',30),fill=GRAY)
    s=96
    while True:
        fh=font('ExtraBold',s); ls=wrap(d,head,fh,W-160)
        if len(ls)<=2 or s<=64: break
        s-=6
    y=170
    for l in ls[:2]: d.text((80,y),l,font=fh,fill=INK); y+=int(s*1.22)
    y+=24
    if big:
        if ctx: d.text((80,y),ctx,font=font('SemiBold',40),fill=GRAY); y+=62
        fb=font('ExtraBold',120)
        while d.textlength(big,font=fb)>W-160: fb=font('ExtraBold',fb.size-8)
        d.text((80,y),big,font=fb,fill=ACC)
    d.line([80,H-70,W-80,H-70],fill=LINE,width=2)
    d.text((80,H-52),'talk7921.tistory.com',font=font('Medium',24),fill=GRAY)
    im.save(out,quality=92)
if __name__=='__main__': make(sys.argv[1],sys.argv[2],*(sys.argv[3:4]))

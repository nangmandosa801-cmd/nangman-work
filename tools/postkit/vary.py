#!/usr/bin/env python3
"""사진 변형 — 같은 사진이라도 글마다 다른 모양으로 만든다 (중복 사진으로 묶이지 않게).
seed = 글 제목 + 사진 출처 → 같은 글에서는 늘 같은 결과, 다른 글에서는 다른 결과.
바꾸는 것: 자르는 위치·비율 · 살짝 기울기 · 색온도·밝기·대비 · 선명도 · 미세 입자 ·
           틀 모양(띠 위치·색·여백) · 확대 원(세부 확대) 끼움. 내용(시공 결과)은 바꾸지 않는다.
"""
import random,hashlib,io
from PIL import Image,ImageEnhance,ImageDraw,ImageFont,ImageFilter,ImageOps
FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
BANDS=['#1d3d5c','#2f5d8a','#3a4a3f','#5a3e2b','#222831','#41506b']
def dhash(im,n=8):
    g=im.convert('L').resize((n+1,n),Image.LANCZOS); p=list(g.getdata())
    return [p[r*(n+1)+c]>p[r*(n+1)+c+1] for r in range(n) for c in range(n)]
def dist(a,b): return sum(x!=y for x,y in zip(dhash(a),dhash(b)))
def pretty(im):
    import numpy as np
    a=np.asarray(im).astype('float32')
    # 회색 기준 화이트밸런스(절반만) — 누렇거나 퍼런 사진 바로잡기
    m=a.reshape(-1,3).mean(0); g=m.mean(); a=a*(1+0.5*(g/np.maximum(m,1)-1))
    # 양끝 0.7% 잘라 펴기(자동 레벨)
    lo=np.percentile(a,0.7); hi=np.percentile(a,99.5); a=(a-lo)/max(hi-lo,1)*255
    a=np.clip(a,0,255)/255.0
    # 어두운 곳 살짝 올리기(감마) — 실내 사진이 답답하지 않게
    mean=a.mean(); gam=0.82 if mean<0.42 else 0.9 if mean<0.55 else 1.0
    a=a**gam
    out=Image.fromarray((a*255).astype('uint8'))
    out=ImageEnhance.Color(out).enhance(1.12)
    out=out.filter(ImageFilter.UnsharpMask(radius=2.2,percent=55,threshold=2))
    return out
def vary(src,cap,seed,W=720,gentle=False):
    R=random.Random(hashlib.md5(seed.encode()).hexdigest())
    im=ImageOps.exif_transpose(Image.open(src)).convert('RGB'); orig=im.copy()
    # 1) 살짝 기울여 돌리고 빈 모서리는 잘라 냄
    a=R.uniform(-0.6,0.6) if gentle else R.uniform(-2.2,2.2); w,h=im.size
    im=im.rotate(a,resample=Image.BICUBIC,expand=False); m=int(max(w,h)*abs(a)*0.02)+2
    im=im.crop((m,m,w-m,h-m)); w,h=im.size
    # 2) 비율 · 위치를 바꿔 자름 (원본의 70~88%)
    ratio=None if gentle else R.choice([4/3,1.0,4/5,3/2,None])
    s=R.uniform(.93,.97) if gentle else R.uniform(.82,.93); cw,ch=int(w*s),int(h*s)
    if ratio:
        if cw/ch>ratio: cw=int(ch*ratio)
        else: ch=int(cw/ratio)
    x=(w-cw)//2 if gentle else R.randint(0,w-cw); y=(h-ch)//2 if gentle else R.randint(0,h-ch); im=im.crop((x,y,x+cw,y+ch))
    im=im.resize((W,int(ch*W/cw)),Image.LANCZOS)
    # 3) 예쁘게 (11/2 사용자 「사진 좀 가공해서 이쁘게 보이게」) — 색 틀어짐 바로잡기 · 어두운 곳 살리기 · 또렷하게
    im=pretty(im)
    im=ImageEnhance.Brightness(im).enhance(R.uniform(.98,1.05))
    im=ImageEnhance.Contrast(im).enhance(R.uniform(.98,1.06))
    im=ImageEnhance.Color(im).enhance(R.uniform(.98,1.08))
    t=R.uniform(-5,5); r,g,b=im.split()
    r=r.point(lambda v:max(0,min(255,v+t))); b=b.point(lambda v:max(0,min(255,v-t)))
    im=Image.merge('RGB',(r,g,b))
    im=im.filter(ImageFilter.UnsharpMask(radius=R.uniform(1,2),percent=R.randint(40,90),threshold=3))
    # 4) 미세 입자
    n=Image.effect_noise(im.size,R.uniform(6,12)).convert('RGB')
    im=Image.blend(im,n,R.uniform(.02,.04))
    # 5) 확대 원 (세부 확대) — 반쯤만
    if False:
        iw,ih=im.size; zs=int(iw*R.uniform(.12,.16)); zx=R.randint(int(iw*.25),int(iw*.75)-zs); zy=R.randint(int(ih*.25),int(ih*.75)-zs)
        z=im.crop((zx,zy,zx+zs,zy+zs)).resize((int(zs*1.8),)*2,Image.LANCZOS); D=z.size[0]
        mk=Image.new('L',(D,D),0); ImageDraw.Draw(mk).ellipse((0,0,D-1,D-1),fill=255)
        px=R.choice([14,iw-D-14]); py=R.choice([14,ih-D-14])
        im.paste(z,(px,py),mk); ImageDraw.Draw(im).ellipse((px,py,px+D-1,py+D-1),outline='white',width=5)
    # 6) 틀: 띠 위치(아래/위) · 색 · 바깥 여백
    acc=R.choice(BANDS); pad=R.choice([18,22,26]); bh=70 if cap else 0; rad=R.choice([14,18,22])
    BG=R.choice(['#ffffff','#f7f5f1','#f3f6f9'])
    iw,ih=im.size; out=Image.new('RGB',(iw+pad*2,ih+bh+pad*2),BG)
    mk=Image.new('L',(iw,ih),0); ImageDraw.Draw(mk).rounded_rectangle((0,0,iw-1,ih-1),rad,fill=255)
    sh=Image.new('RGB',out.size,BG); sd=Image.new('L',out.size,0); ImageDraw.Draw(sd).rounded_rectangle((pad+4,pad+6,pad+iw+4,pad+ih+6),rad,fill=70)
    sd=sd.filter(ImageFilter.GaussianBlur(8)); out=Image.composite(Image.new('RGB',out.size,'#9aa3ad'),out,sd)
    out.paste(im,(pad,pad),mk)
    if cap:
        f=ImageFont.truetype(FB,28,index=1); d=ImageDraw.Draw(out); ty=pad+ih+18
        d.rounded_rectangle((pad,ty+4,pad+8,ty+34),3,fill=acc)
        d.text((pad+20,ty),cap,font=f,fill='#2b3440')
    d=dist(orig,im)
    b=io.BytesIO(); out.save(b,'JPEG',quality=R.randint(78,86)); return b.getvalue(),d
if __name__=='__main__':
    import sys; data,d=vary(sys.argv[1],sys.argv[3] if len(sys.argv)>3 else '',sys.argv[2]); open('/tmp/vary_test.jpg','wb').write(data); print('dhash 거리',d,'/64')

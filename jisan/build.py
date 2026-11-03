import cv2,numpy as np,sys
sys.path.insert(0,'/home/claude/blogkit'); sys.path.insert(0,'/home/claude/jisan/choi')
from PIL import Image,ImageDraw
from thumbnail import F
def mask(f,box):
    im=cv2.imread(f+'-image.png'); b,g,r=[im[...,i].astype(int) for i in range(3)]
    m=((b>200)&(r<110)&(g>80)&(g<180)).astype(np.uint8)
    z=np.zeros_like(m); x0,y0,x1,y1=box; z[y0:y1,x0:x1]=m[y0:y1,x0:x1]; return z
def poly(m,A=None):
    pts=np.argwhere(m>0)[:,::-1].astype(np.float32)
    if A is not None: pts=pts@A[:,:2].T+A[:,2]
    return cv2.convexHull(pts.astype(np.float32)).reshape(-1,2)
b=cv2.imread('5a9423e5-image.png'); a1=cv2.warpAffine(cv2.imread('a05c9716-image.png'),np.load('a05c9716.npy'),(b.shape[1],b.shape[0]))
b[536:614,636:792]=a1[536:614,636:792]
mk=np.zeros(b.shape[:2],np.uint8); mk[526:537,690:745]=255; b=cv2.inpaint(b,mk,5,cv2.INPAINT_TELEA)
base=Image.fromarray(cv2.cvtColor(b,cv2.COLOR_BGR2RGB))
p104=poly(mask('a05c9716',(580,390,810,500)),np.load('a05c9716.npy'))
p105=poly(mask('5a9423e5',(580,480,850,625)))
p1051=poly(mask('9b2b838f',(800,410,870,460)),np.load('9b2b838f.npy'))
print(p104.mean(0),p105.mean(0),p1051.mean(0),len(p1051))
# cover naver red pin on base (small) by blur patch
im=base.convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
for p,c in [(p104,(255,196,0)),(p105,(255,196,0)),(p1051,(255,196,0))]:
    P=[tuple(x) for x in p]; d.polygon(P,fill=c+(95,)); d.line(P+[P[0]],fill=c+(255,),width=5)
im=Image.alpha_composite(im,ov).convert('RGB')
x0,y0,x1,y1=380,260,1480,1150
im=im.crop((x0,y0,x1,y1)); im=im.resize((im.width*2,im.height*2),Image.LANCZOS)
T=lambda x,y:((x-x0)*2,(y-y0)*2)
d=ImageDraw.Draw(im,'RGBA')
def tag(x,y,t,size=34,c=(13,59,92),bg=(255,255,255,240)):
    f=F(size,False,True); w=d.textlength(t,font=f)
    d.rounded_rectangle((x-w/2-16,y-size/2-12,x+w/2+16,y+size/2+14),12,fill=bg,outline=c,width=3)
    d.text((x-w/2,y-size/2-4),t,font=f,fill=c)
def lead(a,b,c=(255,196,0)):
    d.line([a,b],fill=c+(255,),width=5); d.ellipse((a[0]-9,a[1]-9,a[0]+9,a[1]+9),fill=c+(255,))
for p,t,dx,dy in [(p104,'① 산 104',-330,-150),(p105,'② 산 105',-420,150),(p1051,'③ 산 105-1',380,-230)]:
    cx,cy=T(*p.mean(0)); lead((cx,cy),(cx+dx,cy+dy)); tag(cx+dx,cy+dy,t,40)
tag(*T(930,640),'6m 임도',34,(27,122,158))
tag(*T(1200,1060),'가평천',30,(80,90,100))
tag(*T(1070,420),'이곡리 마을',30,(80,90,100))
f=F(40,False,True); s='3필지 합계 임야 20,070평'
w=d.textlength(s,font=f); d.rounded_rectangle((30,30,w+90,120),14,fill=(13,59,92,235)); d.text((60,50),s,font=f,fill='white')
f2=F(30,False,True); s2='임업 경영 · 산림경영관리사(농막) · 임산물창고 · 작업로'
w2=d.textlength(s2,font=f2); d.rounded_rectangle((30,132,w2+90,204),14,fill=(27,122,158,235)); d.text((60,146),s2,font=f2,fill='white')
im.save('combo_raw.png'); print(im.size)
exec(open("fr.py").read())
frame(im,"/mnt/user-data/outputs/jisandream/jisandream_igok_map2.png","가평 토지 매물 · 북면 이곡리","가평 임야 3필지, 6m 임도를 따라 붙어 있습니다","노란 선은 지적 경계 캡처를 한 장에 겹친 것입니다 · 정확한 경계는 지적도로 확인")

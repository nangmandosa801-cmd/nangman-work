import sys,os,json
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/int/mp4_1015')
from PIL import Image,ImageDraw
from sns_carousel import font,FB
import vert
O='/mnt/user-data/outputs/int/'
def mark(im,out):
    im=im.convert('RGB')
    if im.width<966: im=im.resize((966,int(im.height*966/im.width)),Image.LANCZOS)
    d=ImageDraw.Draw(im,'RGBA'); t='출처 · 서울 24시 출장 열쇠 블로그'; f=font(FB,max(26,im.width//34))
    w=d.textlength(t,font=f); h=f.size+14
    d.rounded_rectangle((12,im.height-h-12,12+w+24,im.height-12),8,fill=(0,0,0,170))
    d.text((24,im.height-12-h//2),t,font=f,fill=(255,255,255),anchor='lm'); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out,quality=93)
    return out
SUB='출처 서울 24시 출장 열쇠'
def P(slug,n,crop=None,name=None):
    im=Image.open(f'{O}{slug}/사진/{n}.jpg')
    if crop: im=im.crop(crop)
    return mark(im,f'{O}{slug}/사진_출처/{name or n}.jpg')
specs={}
s='door_gaemun_biyong'
L=[("도어락 개문\n3만원부터"),("과하게 크게\n뚫은 문"),("너무 조여\n부러진 나사"),("날카롭게 잘린\n타공 면"),("그라인더로\n뚫은 문")]
specs[s]=dict(head=["도어락 개문 3만원부터","부수지 않고 엽니다"],what="도어락",slides=[dict(src=P(s,i+1),line=L[i],sub=SUB) for i in range(5)])
s='yurimun_beonhoki'
L=["유리문 번호키\n15만원부터","검은 틀 문에\n검은 몸체","얇은 샷시문\n한강로 상가","위아래로 잠기는\n구조 그대로","번호키 가까이\n유리는 그대로","제작 유리문\n힌지도 같은 날"]
cr={1:(325,0,966,1288)}
specs[s]=dict(head=["유리문 번호키","샷시문 전용 슬림형"],what="유리문",slides=[dict(src=P(s,i+1,cr.get(i+1)),line=L[i],sub=SUB) for i in range(6)])
s='floor_hinge'
sl=[dict(src=P(s,1,None,'a'),line="플로어 힌지\n몸통만 교체",sub=SUB),
 dict(src=P(s,1,(380,200,780,640),'b'),line="하우징은\n그대로 둡니다",sub=SUB),
 dict(src=P(s,1,(400,540,740,1000),'c'),line="같은 규격\n새 힌지 몸통",sub=SUB),
 dict(src=P(s,1,(160,720,820,1200),"d"),line="바닥을 깨지\n않습니다",sub=SUB),
 dict(kicker="플로어 힌지",line="문이 처지면\n사진 한 장",sub="하우징 사진이 중요합니다")]
specs[s]=dict(head=["플로어 힌지 교체","바닥 안 깨고 몸통만"],what="유리문",slides=sl)
per={'door_gaemun_biyong':3.1,'yurimun_beonhoki':2.6,'floor_hinge':3.1}
seed={'door_gaemun_biyong':11,'yurimun_beonhoki':12,'floor_hinge':13}
for s,sp in specs.items():
    j=f'/home/claude/int/mp4_1015/spec_{s}_v.json'; json.dump(sp,open(j,'w'),ensure_ascii=False,indent=1)
    out=f'{O}clip_sigong/nangman_interior_{s}_clip.mp4'
    vert.make(vert.build(j,s),out,per=per[s],seed=seed[s]); print(s,'ok')

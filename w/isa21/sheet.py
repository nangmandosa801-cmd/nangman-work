import json,urllib.request,io,sys
from PIL import Image
R=json.load(open(sys.argv[1]))
def dl(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u+'?type=w400',headers={'User-Agent':'Mozilla/5.0','Referer':'https://m.blog.naver.com/'}),timeout=8).read()
        return Image.open(io.BytesIO(r)).convert('RGB')
    except Exception as e: return None
for r in R:
    ims=[]
    for s in r['sample']:
        for u in s[1][1:]:
            if len(ims)>=12: break
            if u.lower().endswith('.gif'): continue
            im=dl(u)
            if im and im.width>150: ims.append(im)
    if not ims: print(r['b'],'none'); continue
    W=300;cells=[]
    for im in ims:
        h=int(im.height*W/im.width); cells.append(im.resize((W,min(h,400))))
    cols=4; rows=(len(cells)+cols-1)//cols
    sh=Image.new('RGB',(W*cols,400*rows),'white')
    for i,c in enumerate(cells): sh.paste(c,((i%cols)*W,(i//cols)*400))
    sh.save(f"img/{r['b']}.jpg",quality=70); print(r['b'],len(ims))

exec(open('/home/claude/w/relink1018/ni/common.py').read())
import re
from PIL import Image
import numpy as np
SKIP={'auto_okjeong','asym_wolgye'}
HEAD=re.compile(r'<p style="font-size:2[67]px;font-weight:700[^"]*">')
out={}
for s in inv:
    h=open(inv[s]['cur']).read()
    m={}
    for a,b in R[s]['map']:
        if a.endswith('.jpg'): m[b[:-4]]=a
    groups=[(mm.start(),int(mm.group(1)),int(mm.group(2))) for mm in re.finditer(r'\[사진 (\d+)번 · (\d+)장\]',h)]
    jg=[(pos,g) for pos,g,n in groups if any(f'{g}-{k}' in m for k in range(1,n+1))]
    last=jg[-1][0] if jg else None
    hd=[x.start() for x in HEAD.finditer(h) if last and x.start()>last]
    end=min([i for i in (h.find('[배너]'),h.find('같이 보면 좋은 글')) if i>0])
    ins=hd[0] if hd and hd[0]<end else None
    # caption widths
    over=[]
    for gk,a in m.items():
        p=pick(s,a)
        if not p: continue
        im=np.array(Image.open(p).convert('L')); H=im.shape[0]
        band=im[H-124:H-94,18:762]; cols=np.where((band<200).any(axis=0))[0]
        xe=18+cols.max() if len(cols) else 18
        if xe+160>762: over.append((gk,int(xe)))
    out[s]=dict(ins=ins,last=last,end=end,over=over)
    print(s,'last',last,'ins',ins,'end',end,'over',over)

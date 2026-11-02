# 옛 동파 도우미(post.html · 자리표) → 창고 방식 도우미. 사용: conv.py slug stage|build
import sys,re,os,json,base64,html,subprocess
from PIL import Image
slug,mode=sys.argv[1],sys.argv[2]
S=f'/mnt/user-data/outputs/int/{slug}/';W=f'/home/claude/w/dongpa/{slug}/';os.makedirs(W,exist_ok=True)
src=open(S+f'nangman_interior_{slug}_post.html').read()
title=re.search(r'<!-- 제목: (.*?) -->',src).group(1)
PH=re.compile(r'<table[^>]*><tr><td style="border:1px dashed #C7D6E6;[^>]*><span[^>]*>(nangman_interior_[^ ]+\.(?:png|jpg)) — ([^<]*)</span></td></tr></table>')
files=[m.group(1) for m in PH.finditer(src)]
body_files=[f for f in files if not f.endswith('_thumb.png')]
if mode=='stage':
    items=[];
    for i,f in enumerate(body_files):
        im=Image.open(S+f).convert('RGB')
        if im.width>966: im=im.resize((966,int(im.height*966/im.width)))
        items.append((f'{slug}_{i:02d}',im))
    sp=[];cur=[];h=0
    for n,im in items:
        if h+im.height>15000: sp.append(cur);cur=[];h=0
        cur.append((n,im,h));h+=im.height
    sp.append(cur);meta=[]
    for k,s in enumerate(sp):
        Wd=max(im.width for _,im,_ in s);H=sum(im.height for _,im,_ in s);c=Image.new('RGB',(Wd,H),'white')
        for n,im,y in s:c.paste(im,(0,y))
        c.save(W+f'sp{k}.jpg',quality=92);meta.append([[n,0,y,im.width,im.height] for n,im,y in s])
    json.dump(meta,open(W+'sp.json','w'));print(title);print(len(body_files),[os.path.getsize(W+f'sp{k}.jpg') for k in range(len(sp))])
else:
    U={n[:-4]:u for n,u in json.load(open(W+'urls.json'))}
    t=json.load(open(W+'thumb.json'))
    th=W+'thumb.jpg'
    cmd=['python3','/home/claude/tools/ipju_thumb.py','--tag',t['tag'],'--name',t['name'],'--lead',t['lead'],'--key',t['key'],'--out',th]+(['--sub',t['sub']] if t.get('sub') else [])
    subprocess.run(cmd,check=True,capture_output=True)
    idx={f:i for i,f in enumerate(body_files)}
    def rep(m):
        f=m.group(1)
        if f.endswith('_thumb.png'): return ''
        u=U[f'{slug}_{idx[f]:02d}']
        im=Image.open(S+f).convert('RGB');im.thumbnail((780,4000));import io;bb=io.BytesIO();im.save(bb,'JPEG',quality=80)
        d='data:image/jpeg;base64,'+base64.b64encode(bb.getvalue()).decode()
        return f'<p style="text-align:center"><img src="{d}" data-real="{u}" style="max-width:100%"></p>'
    body=PH.sub(rep,src); body=re.sub(r'<!-- 제목:.*?-->','',body)
    D='/home/claude/tools/postkit/'
    base=open(D+'base.html').read();head=base.split('<div class="w">')[0].replace('단열 원고 3편',title[:20]).replace('</style>','.ph{display:grid;grid-template-columns:minmax(0,260px);gap:10px;margin-top:8px}.ph figure{margin:0;display:flex;flex-direction:column;gap:6px}.ph img{width:100%;border-radius:6px}.ph button{padding:7px 10px;font-size:19px}</style>')
    pk=open(D+'postkit.py').read();js=eval(pk[pk.index("js=(")+3:pk.index("</script>')")+11])
    tb='data:image/jpeg;base64,'+base64.b64encode(open(th,'rb').read()).decode()
    o=[head,f'<div class="w"><div class="c"><h1>낭만 인테리어 · {html.escape(title)}</h1><p>제목 복사 → 본문 복사(사진 포함 통째로) → 썸네일 복사.</p></div>',
       (f'<div class="c" id="when">{open(W+"when.txt").read().strip()}</div>' if os.path.exists(W+'when.txt') else '')+f'<div class="c"><div class="t" id="t0">{html.escape(title)}</div><div class="b"><button onclick="ct(\'t0\',this)">제목 복사</button><button onclick="cb(\'h0\',this)">본문 복사</button></div>',
       f'<div class="ph"><figure><img src="{tb}"><button onclick="ci(this.previousElementSibling.src,this)">썸네일 복사</button></figure></div>',
       f'<details><summary>본문 미리보기</summary><div class="body" id="h0">{body}</div></details></div></div>'+js]
    out=f'/home/claude/w/dongpa/{slug}.html';open(out,'w').write(''.join(o));print(out,os.path.getsize(out)//1024,'KB', body.count('blogger.googleusercontent'))

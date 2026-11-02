import sys,re,os,json
sys.path.insert(0,'/home/claude/blogkit'); sys.path.insert(0,'/home/claude/int')
exec(open('/home/claude/w/relink1018/ni/common.py').read())
exec(open('/home/claude/w/relink1018/ni/ven.py').read())
import serial as SN
from thumbnail import F
from PIL import Image,ImageDraw
import numpy as np
SKIP={'auto_okjeong':'사진 4장이 모두 컨테이너에 없음(원본 사진 폴더도 없음) — 번호를 찍을 사진이 없음',
      'asym_wolgye':'사진 4장이 모두 컨테이너에 없음(원본 사진 폴더도 없음) — 번호를 찍을 사진이 없음'}
INS_OVERRIDE={'pocket_jinju':'포켓 중문 설치, 우리 집은 몇 짝짜리가 맞을까'}
CAPFIX={('living_suwon','02_stack'):'옆에서 본 모습 — 문 세 짝이 겹쳐 서고 바닥 레일은 세 줄입니다 (짐은 가렸습니다)'}
src=open('/home/claude/int/nk.py').read(); i=src.index('def LIKE('); j=src.index('\n# 10/11',i)
G={'DC':lambda x:''}; exec(src[i:j],G); LIKEF=G['LIKE']
HEAD=re.compile(r'<p style="font-size:2[67]px;font-weight:700[^"]*">(.*?)</p>')
OUTP='/mnt/user-data/outputs/relink1018/'; OUTI='/mnt/user-data/outputs/relink1018_ni/'
f19=F(19,False,False)
res={}
only=sys.argv[1:] or list(inv)
for s in only:
    rel=inv[s]['rel']; folder=rel.split('/')[0]
    if s in SKIP: res[s]=dict(rel=rel,skip=SKIP[s]); continue
    cur=OUTP+rel if os.path.exists(OUTP+rel) else '/mnt/user-data/uploads/블로그/interior/'+rel   # 지금 디스크에 있는 판을 다시 읽음
    h=open(cur,encoding='utf-8').read()
    assert 'NI-0' not in h and '이 사진처럼 하고 싶다면' not in h, s
    post=open(f'/mnt/user-data/outputs/int/{s}/nangman_interior_{s}_post.html').read() if os.path.exists(f'/mnt/user-data/outputs/int/{s}/nangman_interior_{s}_post.html') else ''
    gk=sorted([(b[:-4],a) for a,b in R[s]['map'] if a.endswith('.jpg')],key=lambda x:tuple(map(int,x[0].split('-'))))
    made=[];missing=[];first=None
    for g,a in gk:
        name=a[len('nangman_interior_'+s+'_'):-4]; p=pick(s,a)
        pc='C:\\블로그\\interior\\'+folder+'\\사진\\'+g+'.jpg'
        if not p: missing.append(dict(file=g+'.jpg',name=name,pc=pc)); continue
        m=re.search(re.escape(a)+r' — ([^<]*)',post); desc=m.group(1).strip() if m else name
        v=VEN[s](name)
        c=SN.code(s,name,v[0],v[1],v[2],desc)
        im=Image.open(p).convert('RGB'); W,H=im.size
        ph=im.crop((18,18,762,H-140)); st=SN.stamp(ph,c).resize(ph.size,Image.LANCZOS); im.paste(st,(18,18))
        d=ImageDraw.Draw(im); a_=np.array(im.convert('L'))[H-124:H-94,18:762]; cols=np.where((a_<200).any(axis=0))[0]; xe=18+int(cols.max())
        add=f'(사진 {c})'
        if xe+7+d.textlength(add,font=f19)<=762:
            d.text((xe+7,H-122),add,font=f19,fill='#555555')
        else:
            cap=CAPFIX[(s,name)]; d.rectangle([18,H-124,762,H-90],fill='white')
            for fs in (18,17,16,15):
                f=F(fs,False,False); t=cap+' '+add
                if d.textlength(t,font=f)<=744: break
            d.text((18,H-122+(19-fs)//2),t,font=f,fill='#555555')
        od=OUTI+folder+'/사진/'; os.makedirs(od,exist_ok=True); im.save(od+g+'.jpg',quality=92)
        made.append(dict(file=g+'.jpg',name=name,code=c,src=p,out=od+g+'.jpg',pc=pc))
        if first is None: first=c
    # LIKE 상자
    G['s']=s
    box=LIKEF(first,two=s in TWO).rstrip()
    hs=[x for x in HEAD.finditer(h)]
    if s in INS_OVERRIDE: pos=[x.start() for x in hs if re.sub('<[^>]+>','',x.group(1)).startswith(INS_OVERRIDE[s])][0]
    else:
        last=[mm.start() for mm in re.finditer(r'\[사진 (\d+)번 · (\d+)장\]',h) if any(f"{mm.group(1)}-{k}" in dict(gk) for k in range(1,int(mm.group(2))+1))][-1]
        pos=[x.start() for x in hs if x.start()>last][0]
    k=pos
    while True:
        t=h[:k].rstrip()
        if t.endswith('<p><br></p>'): k=len(t)-len('<p><br></p>')
        else: k=len(t); break
    h2=h[:k]+'\n\n'+box+h[k:]
    os.makedirs(os.path.dirname(OUTP+rel),exist_ok=True); open(OUTP+rel,'w',encoding='utf-8').write(h2)
    res[s]=dict(rel=rel,src_read=cur,like=first,two=s in TWO,made=made,missing=missing,box_at=k)
    print(s,'번호',len(made),'없음',len(missing),'상자',first)
json.dump(res,open('/home/claude/w/relink1018/ni/run_res.json','w'),ensure_ascii=False,indent=1)

"""사진 가공 · 장부 기록.  python3 mkimg.py <slug> <blog/logNo> <idx:캡션> [<idx:캡션> ...]
→ w/int11/img/nangman_interior_<slug>_NN.jpg 를 만들고 원고에 붙일 '!=' 줄을 출력. NI 번호는 장부 마지막 다음."""
import sys,os,re,glob
sys.path.insert(0,'/home/claude/tools/postkit')
from vary import vary
LED='/home/claude/낭만인테리어_사진번호.md'; IMG='/home/claude/w/int11/img'; os.makedirs(IMG,exist_ok=True)
NAME={'user':'낭만 인테리어 현장','door-diy777':'펠리체 중문','flowhc':'플로우홈케어 설비','lmg4455':'엘엠지 줄눈','specialcoking':'스페셜코킹','febric_cleaning':'패브릭클리닝','amrita2580':'오렌지 입주청소','dd2homecare':'단디홈케어'}
from PIL import Image
def crop_logo(path,blog):
    # 플로우홈케어 사진은 오른쪽 아래 로고를 잘라 냄
    if blog!='flowhc': return path
    im=Image.open(path).convert('RGB'); w,h=im.size; q='/tmp/_crop_'+os.path.basename(os.path.dirname(path))+'_'+os.path.basename(path)
    im.crop((0,0,int(w*0.87),int(h*0.89))).save(q,quality=95); return q
def redo(slug):
    # 장부에 적힌 같은 NI 번호 · 캡션으로 다시 만듦
    rows=[l for l in open(LED).read().split('\n') if f'| {slug} |' in l and int(re.search(r'NI-(\d+)',l).group(1))>=1635]
    for k,l in enumerate(rows,1):
        c=[x.strip() for x in l.strip('|').split('|')]; n=c[0][3:]; blog,log,idx=c[2].split(); path=f'/home/claude/v2src/partners/{blog}/{log}/{idx[1:]}.jpg'; cap=c[4]
        b,_=vary(crop_logo(path,blog),f'{cap} · NI-{n}',f'{slug}|{path}',W=720,gentle=False)
        open(f'{IMG}/nangman_interior_{slug}_{k:02d}.jpg','wb').write(b)
    return len(rows)
def last_ni():
    m=re.findall(r'NI-(\d+)',open(LED).read()); return max(map(int,m))
def run(slug,src,items,gentle=False):
    blog,log=src.split('/'); n=last_ni()+1; out=[]; led=[]
    k=len(glob.glob(f'{IMG}/nangman_interior_{slug}_*.jpg'))
    for it in items:
        idx,cap=it.split(':',1); path=f'/home/claude/v2src/partners/{blog}/{log}/{int(idx):02d}.jpg'
        k+=1
        b,_=vary(crop_logo(path,blog),f'{cap} · NI-{n}',f'{slug}|{path}',W=720,gentle=gentle)
        o=f'{IMG}/nangman_interior_{slug}_{k:02d}.jpg'; open(o,'wb').write(b)
        led.append(f'| NI-{n} | {NAME.get(blog,blog)} | {blog} {log} #{int(idx):02d} | {slug} | {cap} |'); out.append('!='+o); n+=1
    open(LED,'a').write('\n'.join(led)+'\n'); return out
if __name__=='__main__':
    if sys.argv[1]=='redo': print(redo(sys.argv[2])); sys.exit()
    slug,src=sys.argv[1],sys.argv[2]; g='--gentle' in sys.argv
    items=[a for a in sys.argv[3:] if not a.startswith('--')]
    print('\n'.join(run(slug,src,items,g)))

def pick(slug,src,cap,n=5):
    # 원 글 사진에서 배너 · 첫 장 · 끝 세 장 빼고 고르게 n장
    sys.path.insert(0,'/home/claude/tools/followup')
    from post_followup import is_banner
    blog,log=src.split('/'); fs=sorted(glob.glob(f'/home/claude/v2src/partners/{blog}/{log}/*.jpg'))
    body=fs[1:-3] if len(fs)>6 else fs[1:]; ok=[]
    for f in body:
        try:
            im=Image.open(f); w,h=im.size
            if h/w>2.2 or w<300 or is_banner(f): continue
            ok.append(f)
        except Exception: pass
    sel=[ok[int(j*(len(ok)-1)/max(n-1,1))] for j in range(n)] if len(ok)>=n else ok
    items=[f"{int(os.path.basename(f)[:2])}:{cap}" for f in sel]
    return run(slug,src,items)

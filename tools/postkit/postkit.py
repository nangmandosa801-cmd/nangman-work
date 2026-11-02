#!/usr/bin/env python3
"""낭만 인테리어 네이버 원고 키트 — 짧은 원고 텍스트(.md) 여러 개 → 도우미 HTML 1장.
사용: python3 postkit.py out.html "페이지 제목" a.md b.md ...
원고 꼴:
  # 검색어, 나머지 제목          (제목 · 쉼표에서 본문 첫 제목 줄바꿈)
  kicker: 결로 · 곰팡이
  tags: 태그1, 태그2, ...           (본문 끝에 #태그로 들어감)
  thumb: 꼬리표 | 이름1 | 이름2 | 앞말 | 핵심 | 설명
  links: 제목 = 주소 ; 제목 = 주소 ...   (기본 꼬리 링크 6개 뒤에 추가)
  ---
  본문: 빈 줄 = 문단 (「답부터 적습니다」 같은 말 쓰지 않음 · 글자 최소 19px) · "## " 소제목 · "| a | b |" 표(첫 줄 머리) · "> " 문의/요약 상자
        "!블로그ID/글번호#사진번호 캡션"  사진(가공 · 도우미 「사진」 칸으로)
        "[CALL]" 표준 문의 상자
"""
import sys,os,re,json,base64,io,html,subprocess,urllib.request
from PIL import Image,ImageEnhance,ImageDraw,ImageFont
D=os.path.dirname(os.path.abspath(__file__)); CACHE=os.path.join(D,'cache'); os.makedirs(CACHE,exist_ok=True)
FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
SP='<p><br></p>'
DEF_LINKS=[('대구 단열 시공 비용, 1헤베 10만원 선','https://blog.naver.com/champion_chart/224456973595'),
 ('결로 페인트 시공, 곰팡이는 늦춰도 차가운 벽은 못 고칩니다','https://blog.naver.com/champion_chart/224444946484'),
 ('군포 곰팡이 제거, 장 뒤 벽까지 이보드 단열','https://blog.naver.com/champion_chart/224452126321'),
 ('베란다 곰팡이 탄성코트','https://blog.naver.com/champion_chart/224444882883'),
 ('이중창 결로','https://blog.naver.com/champion_chart/224444840593'),
 ('벽지 곰팡이 원인','https://blog.naver.com/champion_chart/224438517059')]
CALL=('<div style="background:#f3f6fa;border-left:5px solid #2f5d8a;padding:14px 16px;margin:18px 0"><b>사진 한 장이면 됩니다</b><br>'
 '문제 생긴 곳 사진 한 장과 사는 동네를 문자로 보내 주세요. 가까운 시공팀을 이어 드립니다.<br><b style="font-size:19px">문자 · 전화 010-2882-8165</b></div>')
from vary import vary
VLOG=[]
def photo(ref,cap,seed=''):
    if ref.startswith('='):  # 「!=/경로」 = 손대지 않고 그대로
        return 'data:image/jpeg;base64,'+base64.b64encode(open(ref[1:],'rb').read()).decode()
    if ref.startswith('/'):
        data,d=vary(ref,cap,seed+'|'+ref); VLOG.append((ref,d)); return 'data:image/jpeg;base64,'+base64.b64encode(data).decode()
    blog,rest=ref.split('/'); no,idx=rest.split('#'); idx=int(idx)
    d=os.path.join(CACHE,blog,no); os.makedirs(d,exist_ok=True); pj=os.path.join(d,'post.json')
    if not os.path.exists(pj):
        x=urllib.request.urlopen(urllib.request.Request(f'https://blog.naver.com/PostView.naver?blogId={blog}&logNo={no}',headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf8','ignore')
        imgs=[]
        for s in re.findall(r'data-lazy-src="([^"]+)"',x):
            s=s.split('?')[0]
            if s not in imgs: imgs.append(s)
        json.dump(imgs,open(pj,'w'))
    imgs=json.load(open(pj)); fn=os.path.join(d,f'{idx:02d}.jpg')
    if not os.path.exists(fn):
        open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(imgs[idx]+'?type=w966',headers={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}),timeout=20).read())
    data,d=vary(fn,cap,seed+'|'+ref); VLOG.append((ref,d)); return 'data:image/jpeg;base64,'+base64.b64encode(data).decode()
def thumb(args,slug):
    t=[a.strip() for a in args.split('|')]
    out=os.path.join(CACHE,slug+'_thumb.jpg')
    cmd=['python3',os.path.join(D,'..','ipju_thumb.py'),'--tag',t[0],'--name',t[1]+'|'+t[2],'--lead',t[3],'--key',t[4],'--out',out]
    if len(t)>5 and t[5]: cmd+=['--sub',t[5]]
    subprocess.run(cmd,check=True,capture_output=True); return 'data:image/jpeg;base64,'+base64.b64encode(open(out,'rb').read()).decode()
def LK(x): return re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',r'<a href="\2" style="color:#2f5d8a;font-weight:700">\1</a>',x)
def parse(path):
    raw=open(path).read(); head,body=raw.split('\n---\n',1); m={}
    for ln in head.splitlines():
        if ln.startswith('# '): m['title']=ln[2:].strip()
        elif ':' in ln: k,v=ln.split(':',1); m[k.strip()]=v.strip()
    slug=os.path.splitext(os.path.basename(path))[0]
    a,b=(m['title'].split(',',1)+[''])[:2]
    parts=[f'<p style="font-size:19px;color:#2f5d8a;font-weight:700">낭만 인테리어 · {m.get("kicker","")}</p>',
           f'<h2 style="font-size:28px;color:#1d3d5c;line-height:1.45;margin:6px 0 4px">{a},<br>{b.strip()}</h2><hr style="border:0;border-top:1px solid #d9dee5;margin:14px 0">']
    photos=[]; tbl=[]
    def flush():
        if tbl:
            s='<table style="width:100%;border-collapse:collapse;font-size:19px;margin:12px 0">'
            for k,r in enumerate(tbl):
                tg='th' if k==0 else 'td'; bg=' style="background:#1d3d5c;color:#fff"' if k==0 else ''
                s+=f'<tr{bg}>'+''.join(f'<{tg} style="padding:9px;border:1px solid #c9d4df">{c}</{tg}>' for c in map(LK,r))+'</tr>'
            parts.append(s+'</table>'); tbl.clear()
    for blk in re.split(r'\n\s*\n',body.strip()):
        for ln in blk.splitlines():
            ln=ln.strip()
            if ln.startswith('|'): tbl.append([c.strip() for c in ln.strip('|').split('|')]); continue
            flush()
            if ln.startswith('## '): parts.append(f'<h2 style="font-size:22px;color:#1d3d5c;margin:34px 0 10px">{ln[3:]}</h2>')
            elif ln.startswith('!'): r,cap=(ln[1:].split(' ',1)+[''])[:2]; photos.append((cap,photo(r,cap,m.get('title','')))); parts.append(f'<!--IMG{len(photos)-1}-->')
            elif ln=='[CALL]': parts.append(CALL)
            elif ln.startswith('> '): parts.append(f'<div style="background:#f3f6fa;border-left:5px solid #2f5d8a;padding:14px 16px;margin:18px 0">{ln[2:]}</div>')
            elif ln: parts.append(f'<p>{LK(re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",ln))}</p>')
        flush()
    links=([] if m.get('nodef') else DEF_LINKS)+[tuple(x.split('=',1)) for x in m.get('links','').split(';') if '=' in x]
    parts.append('<h3 style="font-size:19px;color:#1d3d5c;margin:30px 0 8px">같이 보면 좋은 글</h3><ul>'+''.join(f'<li><a href="{u.strip()}">{t.strip()}</a></li>' for t,u in links)+'</ul>')
    tags=[t.strip() for t in m.get('tags','').split(',') if t.strip()]
    parts.append('<p style="color:#2f5d8a;font-size:19px">'+' '.join('#'+t for t in tags)+'</p>')
    h=SP.join(parts)
    return dict(title=m['title'],html='<div style="font-size:19px;line-height:1.85;color:#222">'+h+'</div>',photos=photos,thumb=thumb(m['thumb'],slug) if m.get('thumb') else None)
def build(out,ptitle,paths):
    base=open(os.path.join(D,'base.html')).read()
    head=base.split('<div class="w">')[0].replace('단열 원고 3편',ptitle).replace('</style>','.ph{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:8px}.ph figure{margin:0;display:flex;flex-direction:column;gap:6px}.ph img{width:100%;border-radius:6px}.ph button{padding:7px 10px;font-size:19px}</style>')
    js=('<script>function done(b){const o=b.textContent;b.textContent="복사됨";setTimeout(()=>b.textContent=o,1500)}'
        'function ct(id,b){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>done(b)).catch(()=>{})}'
        'function cb(id,b){const el=document.getElementById(id);const t=el.cloneNode(true);t.querySelectorAll("img[data-real]").forEach(i=>i.src=i.dataset.real);try{navigator.clipboard.write([new ClipboardItem({"text/html":new Blob([t.innerHTML],{type:"text/html"}),"text/plain":new Blob([el.innerText],{type:"text/plain"})})]).then(()=>done(b)).catch(()=>sel(el,b))}catch(e){sel(el,b)}}'
        'function sel(el,b){el.closest("details").open=true;const r=document.createRange();r.selectNodeContents(el);const s=getSelection();s.removeAllRanges();s.addRange(r);document.execCommand("copy");done(b)}'
        'async function ci(src,b){try{const im=new Image();im.src=src;await im.decode();const c=document.createElement("canvas");c.width=im.naturalWidth;c.height=im.naturalHeight;c.getContext("2d").drawImage(im,0,0);const bl=await new Promise(r=>c.toBlob(r,"image/png"));await navigator.clipboard.write([new ClipboardItem({"image/png":bl})]);done(b)}catch(e){b.textContent="길게 눌러 저장"}}</script>')
    o=[head,f'<div class="w"><div class="c"><h1>낭만 인테리어 · {html.escape(ptitle)}</h1><p>제목 복사 → 본문 복사(태그 포함) → 썸네일 복사 → 사진은 「사진」 칸에서 한 장씩.</p></div>']
    U=json.load(open(os.environ['URLS'])) if os.environ.get('URLS') else []
    for i,p in enumerate(map(parse,paths)):
        for k,(c,src) in enumerate(p['photos']):
            real=f' data-real="{U[k]}"' if k<len(U) else ''
            p['html']=p['html'].replace(f'<!--IMG{k}-->',f'<p style="text-align:center"><img src="{src}"{real} style="max-width:100%"></p>')
        fig=lambda src,lab:f'<figure><img src="{src}"><button onclick="ci(this.previousElementSibling.src,this)">{lab}</button></figure>'
        th=f'<div class="ph" style="grid-template-columns:minmax(0,260px)">{fig(p["thumb"],"썸네일 복사")}</div>' if p['thumb'] else ''
        ph=''.join(fig(s,f'사진 {k+1} 복사') for k,(c,s) in enumerate(p['photos']))
        o.append(f'<div class="c"><div class="ok">{i+1}편</div><div class="t" id="t{i}">{html.escape(p["title"])}</div><div class="b"><button onclick="ct(\'t{i}\',this)">제목 복사</button><button onclick="cb(\'h{i}\',this)">본문 복사</button></div>{th}'
                 f'<details><summary>사진 {len(p["photos"])}장</summary><div class="ph">{ph}</div></details><details><summary>본문 미리보기</summary><div class="body" id="h{i}">{p["html"]}</div></details></div>')
    o.append('</div>'+js); open(out,'w').write(''.join(o)); print(out,os.path.getsize(out)//1024,'KB')
if __name__=='__main__': build(sys.argv[1],sys.argv[2],sys.argv[3:])

# -*- coding: utf-8 -*-
# 지산드림 발행 도우미 — 글 폴더 하나로 붙여넣기 도우미 페이지(html)를 만든다
# 사용: python3 helper_build.py <폴더> <슬러그> "<예약 시각 안내>"
#  예: python3 helper_build.py /mnt/user-data/outputs/jisandream/imya imya_maemae "10/25(일) 오전 9시"
import sys,re,io,base64,html,os
from PIL import Image
import json
D,slug=sys.argv[1],sys.argv[2]; when=sys.argv[3] if len(sys.argv)>3 else '사용자가 정함'
post=open(f'{D}/jisandream_{slug}_post.html',encoding='utf-8').read()
UP=f'{D}/jisandream_{slug}_imgurls.json'
URLS=json.load(open(UP)) if os.path.exists(UP) else {}
m=re.search(r'<p style="font-size:34px;font-weight:700;color:#0D3B5C;">(.*?)</p>',post); title=html.unescape(re.sub('<[^>]+>','',m.group(1)))
tags=re.search(r'line-height:1.9;">(#.*?)</span>',post); tags=tags.group(1) if tags else ''
def uri(fn,w=1100):
    im=Image.open(f'{D}/{fn}').convert('RGB')
    if im.width>w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'JPEG',quality=86,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
PH=re.compile(r'<table width="693"[^>]*><tr><td style="border:1px dashed[^>]*><span[^>]*>(jisandream_[\w]+\.(?:png|jpg))\s—\s(.*?)</span></td></tr></table>')
order=[]
HD=re.compile(r'<p style="font-size:27px;font-weight:700;color:#0D3B5C;">(.*?)</p>')
def plain(x): return html.unescape(re.sub('<[^>]+>','',x)).strip()
def where(pos):
    hs=[m for m in HD.finditer(post,0,pos)]
    st=hs[-1].end() if hs else 0
    sec=plain(hs[-1].group(1)) if hs else '제목 바로 아래'
    seg=post[st:pos]
    seg=re.sub(r'(\s*<p><br></p>)+\s*$','',seg).rstrip()
    tops=[m for m in re.finditer(r'<table|<p[ >]',seg)]
    # 맨 마지막 덩어리(최상위 표 또는 문단) 찾기
    blocks=[];i=0
    while i<len(seg):
        m=re.compile(r'<table|<p[ >]').search(seg,i)
        if not m: break
        if m.group(0)=='<table':
            depth=0;j=m.start()
            for t in re.finditer(r'<table|</table>',seg[m.start():]):
                depth+=1 if t.group(0)=='<table' else -1
                if depth==0: j=m.start()+t.end();break
            blocks.append(('t',seg[m.start():j])); i=j
        else:
            j=seg.find('</p>',m.start())+4; blocks.append(('p',seg[m.start():j])); i=j
    blocks=[x for x in blocks if plain(x[1])]
    if not blocks: return sec,'소제목 바로 아래'
    k,t=blocks[-1]
    if k=='t':
        if 'dashed' in t: return sec,'앞 그림 바로 아래'
        if 'border-left:3px solid #0D3B5C' in t:
            return sec,'「'+plain(re.search(r'font-size:21px;font-weight:700[^>]*>(.*?)</p>',t).group(1))+'」 상자 바로 아래'
        cells=[plain(x) for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',t)[:3]]
        return sec,'「'+' · '.join(c for c in cells if c)+'」 표 바로 아래'
    tx=plain(t)
    if len(blocks)>1 and blocks[-2][0]=='t' and 'color:#8A8578' in t[:60]:
        cells=[plain(x) for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',blocks[-2][1])[:3]]
        return sec,'「'+' · '.join(c for c in cells if c)+'」 표와 그 밑 설명줄 다음'
    return sec,'「…'+tx[-22:]+'」 문단 다음'
for mm in PH.finditer(post):
    sec,prev=where(mm.start()); order.append((mm.group(1),mm.group(2),sec,prev))
cnt=[0]
def slot_preview(mm):
    cnt[0]+=1; n=cnt[0]; return f'<div class="slot">▶ 그림 {n} 넣는 곳 · {html.escape(mm.group(2))}</div>'
preview=PH.sub(slot_preview,post) if not URLS else None
cnt2=[0]
def slot_clean(mm):
    cnt2[0]+=1; n=cnt2[0]; fn=mm.group(1)
    if fn in URLS:
        return f'<p style="text-align:center;"><img src="{URLS[fn]}" width="693" style="width:100%;max-width:693px;" alt="{html.escape(mm.group(2))}"></p>'
    return ('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border:2px dashed #E08A00;padding:14px;text-align:center;background-color:#FFF8E8;">'
            f'<span style="font-size:19px;font-weight:700;color:#B05A00;">▶ 그림 {n} 넣는 곳 · 이 칸을 지우고 그림 {n}을 붙이세요</span></td></tr></table>')
clean=PH.sub(slot_clean,post)
if preview is None: preview=PH.sub(lambda mm:f'<p style="text-align:center;"><img src="{uri(mm.group(1))}" style="width:100%;max-width:693px;" alt=""></p>',post)
ONE=bool(URLS) and all(fn in URLS for fn,*_ in order)
thumb=f'jisandream_{slug}_thumb.png'
folder='C:\\블로그\\jisandream\\[미발행] '+title
def gcard(i,fn,c,sec,prev):
    n=i+1
    if not os.path.exists(f'{D}/{fn}'): return f'<div class="miss">그림 {n} · {fn} 파일 없음</div>'
    return (f'<figure class="g"><img id="img{n}" src="{uri(fn)}" alt="{html.escape(c)}"><figcaption><span class="n">그림 {n}</span>'
            f'<span class="c">{html.escape(c)}</span></figcaption><div class="loc">넣는 곳 · <b>{html.escape(sec)}</b> · {html.escape(prev)}</div><div class="row"><button type="button" data-img="{n}">그림 {n} 복사</button><span class="done" id="d{n}"></span></div></figure>')
imglist=''.join(gcard(i,fn,c,sec,prev) for i,(fn,c,sec,prev) in enumerate(order))
page=f'''<title>{html.escape(title[:24])}… 발행 도우미</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* 한 줄로 내려가는 작업 순서표: 번호가 실제 붙여넣기 순서 */
:root{{--bg:#F3F6F7;--card:#FFFFFF;--fg:#14262E;--mute:#5E7078;--line:#D3DEE2;--accent:#1B6F8A;--accent-fg:#FFFFFF;--hl:#FFF3C4;
--f-display:"Gowun Dodum","Noto Sans KR",sans-serif;--f-body:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0F1A1F;--card:#17252B;--fg:#E3ECEF;--mute:#93A6AE;--line:#2C3E46;--accent:#5BB4D0;--accent-fg:#0F1A1F;--hl:#4A4220;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0F1A1F;--card:#17252B;--fg:#E3ECEF;--mute:#93A6AE;--line:#2C3E46;--accent:#5BB4D0;--accent-fg:#0F1A1F;--hl:#4A4220;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.65 var(--f-body)}}
.wrap{{max-width:760px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:18px}}
.eyebrow{{font-size:13px;letter-spacing:.08em;color:var(--accent);font-weight:700}}
h1{{font:700 24px/1.4 var(--f-display);margin:4px 0 0;text-wrap:balance}}
.meta{{color:var(--mute);font-size:14px}}
section{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px 20px;display:grid;gap:12px;min-width:0}}
h2{{font-size:17px;margin:0;display:flex;gap:10px;align-items:baseline}}
h2 b{{font-variant-numeric:tabular-nums;color:var(--accent);font-size:15px}}
.when{{background:var(--hl);padding:2px 8px;border-radius:4px;font-weight:700}}
.box{{border:1px solid var(--line);border-radius:6px;padding:10px 12px;font-size:15px;overflow-wrap:anywhere}}
.row{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
button{{font:700 15px var(--f-body);background:var(--accent);color:var(--accent-fg);border:0;border-radius:6px;padding:9px 16px;cursor:pointer}}
button:focus-visible{{outline:3px solid var(--fg);outline-offset:2px}}
.done{{font-size:14px;color:var(--accent);font-weight:700}}
details summary{{cursor:pointer;color:var(--mute);font-size:14px}}
#body{{background:#fff;color:#333;border-radius:6px;padding:14px;margin-top:10px;overflow-x:auto}}
#body table{{min-width:0!important}}
.ph{{margin:10px 0;border:1px dashed #9CBBCC;border-radius:6px;padding:8px;background:#F7FAFB}}
.ph img{{display:block;width:100%}}
.ph figcaption{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding-top:8px;font-size:14px;color:#0D3B5C}}
.ph .n{{font-weight:700}} .ph .c{{flex:1;min-width:0}}
.ph button{{padding:6px 12px;font-size:14px;background:#1B6F8A;color:#fff}}
.miss{{color:#B03A2E}}
.loc{{font-size:14px;background:var(--hl);padding:6px 10px;border-radius:4px}}
.slot{{margin:10px 0;border:1px dashed #9CBBCC;padding:10px;color:#0D3B5C;font-weight:700;font-size:14px}}
.gal{{display:grid;gap:16px}}
.g{{margin:0;display:grid;gap:8px;border-top:1px solid var(--line);padding-top:14px}}
.g img{{display:block;width:100%;max-width:560px;border-radius:6px}}
.g figcaption{{display:flex;gap:8px;font-size:14px;flex-wrap:wrap}} .g .n{{font-weight:700;color:var(--accent)}} .g .c{{color:var(--mute);min-width:0}}
ol.imgs{{margin:0;padding-left:0;list-style:none;display:grid;gap:6px;font-size:14px}}
ol.imgs li{{display:grid;gap:2px}} .fn{{font-family:ui-monospace,Consolas,monospace;overflow-wrap:anywhere}} .cap{{color:var(--mute)}}
.thumb img{{max-width:360px;width:100%;border-radius:6px;display:block}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Sans+KR:wght@400;700&display=swap">
<div class="wrap">
<header><div class="eyebrow">지산드림 · 발행 도우미</div><h1>{html.escape(title)}</h1>
<div class="meta">예약 시각 <span class="when">{html.escape(when)}</span> · 그림 {len(order)}장 + 대표 사진 · 태그 {tags.count('#')}개</div></header>

<section><h2><b>0</b>대표 사진 · 따로 올리기</h2><div class="meta">본문에는 넣지 않았습니다. 이 그림을 붙여 대표로 지정합니다.</div>
<div class="thumb"><img id="thumbimg" src="{uri(thumb,900)}" alt="대표 사진"></div>
<div class="row"><button type="button" data-img="0">대표 사진 복사</button><span class="done" id="d0"></span></div></section>

<section><h2><b>1</b>본문 (제목 · 태그 포함)</h2>
<div class="meta">{'그림 '+str(len(order))+'장이 본문 안에 들어 있습니다. 「본문 복사」 한 번이면 글과 그림이 같이 붙습니다. 대표 사진(0번)만 따로 올려 대표로 지정합니다.' if ONE else '본문을 붙이면 주황 점선 칸에 「▶ 그림 N 넣는 곳」이 보입니다. 칸 번호와 2번의 그림 번호가 같습니다.'}</div>
<div class="row"><button type="button" id="bb">본문 복사</button><span class="done" id="db"></span></div>
<details><summary>본문 미리보기</summary><div id="body">{preview}</div></details></section>

{'<section><h2><b>2</b>그림 확인</h2><div class="meta">본문에 그림이 이미 들어 있습니다. 붙인 뒤 그림이 빠진 곳이 있을 때만 여기서 같은 번호를 복사해 넣습니다.</div><details><summary>그림 '+str(len(order))+'장 따로 보기</summary><div class="gal">'+imglist+'</div></details></section>' if ONE else '<section><h2><b>2</b>그림 넣기</h2><div class="meta">위에서부터 1번씩 차례로 넣습니다. 노란 줄이 본문 속 위치입니다. 「그림 N 복사」를 누르고 「▶ 그림 N 넣는 곳」 칸을 지운 자리에 붙입니다.</div><div class="gal">'+imglist+'</div></section>'}

<section><h2><b>3</b>발행한 뒤</h2><div>발행하거나 예약한 글 주소를 채팅에 붙여 주세요. 다음 글 연결 목록에 넣습니다.</div></section>
</div>
<template id="clean">{clean}</template>
<script>
function mark(id,t){{var e=document.getElementById(id);if(e){{e.textContent=t;setTimeout(function(){{e.textContent=''}},2500)}}}}
function sel(el){{var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);}}
function txt(src,done){{var el=document.getElementById(src);var v=el.textContent;
 (navigator.clipboard?navigator.clipboard.writeText(v):Promise.reject()).then(function(){{mark(done,'복사됨')}}).catch(function(){{sel(el);try{{document.execCommand('copy');mark(done,'복사됨')}}catch(e){{mark(done,'선택됨 · Ctrl+C')}}}});}}
document.getElementById('bb').onclick=function(){{
 var h=document.getElementById('clean').innerHTML;var tmp=document.createElement('div');tmp.innerHTML=h;var p=tmp.innerText;
 try{{navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob([p],{{type:'text/plain'}})}})]).then(function(){{mark('db','복사됨')}}).catch(fb)}}catch(e){{fb()}}
 function fb(){{var d=document.createElement('div');d.innerHTML=h;d.style.position='fixed';d.style.left='-9999px';document.body.appendChild(d);sel(d);try{{document.execCommand('copy');mark('db','복사됨')}}catch(e){{mark('db','복사 안 됨')}}d.remove();}}
}};
function imgCopy(img,btn,done){{
 var c=document.createElement('canvas');c.width=img.naturalWidth;c.height=img.naturalHeight;c.getContext('2d').drawImage(img,0,0);
 c.toBlob(function(b){{try{{navigator.clipboard.write([new ClipboardItem({{'image/png':b}})]).then(function(){{mark(done,'복사됨 · 붙여넣기')}}).catch(function(){{mark(done,'복사 안 됨 · 그림에서 오른쪽 클릭 → 이미지 복사')}})}}catch(e){{mark(done,'복사 안 됨 · 그림에서 오른쪽 클릭 → 이미지 복사')}}}},'image/png');}}
document.querySelectorAll('button[data-img]').forEach(function(b){{b.onclick=function(){{
 var n=b.getAttribute('data-img');var img=n==='0'?document.getElementById('thumbimg'):document.getElementById('img'+n);imgCopy(img,b,'d'+n);}}}});
</script>
'''
out=f'{D}/jisandream_{slug}_helper.html'; open(out,'w',encoding='utf-8').write(page)
print(out,len(page)//1024,'KB',len(order),'그림')

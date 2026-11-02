"""발행 도우미 페이지 만들기: python3 helper.py <body.html> <meta.json> <out.html> <페이지제목> <썸네일파일명> <예약안내>"""
import json,html,re,sys
bp,mp,out,ptitle,thumb,when=sys.argv[1:7]
date=sys.argv[7] if len(sys.argv)>7 else ""
b=open(bp).read();m=json.load(open(mp))
prev=re.sub(r'<img src="[^"]*" alt="([^"]*)"[^>]*>',lambda x:'<span class="ph">사진 · %s</span>'%x.group(1),b)
import base64,os
def tcard(t):
    pth=t if os.path.isabs(t) else '/mnt/user-data/outputs/int/'+t
    du='data:image/png;base64,'+base64.b64encode(open(pth,'rb').read()).decode()
    return '<div class="card"><h2><span class="n">2</span>썸네일</h2><img id="th" src="%s" alt="썸네일" style="max-width:320px;border:1px solid var(--line);border-radius:8px"><button id="tb">썸네일 복사</button><span class="done" id="d-th"></span><p class="mute">네이버 본문 맨 위에 붙여 넣기(Ctrl+V) → 사진 눌러 「대표」 체크. 버튼이 안 되면 그림을 길게 누르거나 오른쪽 클릭 → 이미지 복사</p></div>'%du
thumb_card=tcard(thumb) if thumb!='-' else '<div class="card"><h2><span class="n">2</span>썸네일</h2><p class="mute">대표 사진은 지금 글의 것을 그대로 둡니다.</p></div>'
P='''<title>%s</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{--bg:#f4f3ee;--card:#fff;--fg:#1c2420;--mute:#66706a;--line:#dedbd2;--accent:#1F3864;--val:#f2f4f7;--ok:#2f7a4a}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121614;--card:#1b211e;--fg:#e6ece8;--mute:#9aa69f;--line:#2b332f;--accent:#9db7e6;--val:#232a27;--ok:#7fd19b;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121614;--card:#1b211e;--fg:#e6ece8;--mute:#9aa69f;--line:#2b332f;--accent:#9db7e6;--val:#232a27;--ok:#7fd19b;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:17px/1.65 "Pretendard","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:20px 48px}
main{max-width:720px;margin:0 auto;display:grid;gap:14px}h1{font-size:23px;margin:0;text-wrap:balance}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;display:grid;gap:10px;min-width:0}
h2{font-size:18px;margin:0}.n{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%%;background:var(--accent);color:var(--card);font-size:15px;margin-right:6px}
.v{background:var(--val);border-radius:8px;padding:10px 12px;word-break:break-all}
.mute{color:var(--mute);font-size:15px;margin:0}
button{font:inherit;font-weight:700;padding:10px 14px;border-radius:9px;border:1.5px solid var(--accent);background:var(--card);color:var(--accent);cursor:pointer;justify-self:start}
.done{color:var(--ok);font-weight:700;font-size:15px}
.prev{border:1px solid var(--line);border-radius:10px;padding:14px;max-height:420px;overflow:auto;background:#fff;color:#222}
.ph{display:block;background:#e9edf3;color:#445;border-radius:6px;padding:18px;text-align:center;font-size:14px}
#raw{position:fixed;left:-20000px;top:0;width:700px;height:10px;overflow:hidden;pointer-events:none;opacity:0}
</style>
<main>
<h1>%s</h1>
<div class="card" style="border:2px solid var(--accent)"><h2>발행 일자</h2><div class="v" style="font-size:22px;font-weight:700">%s</div></div>
<div class="card"><h2><span class="n">1</span>제목</h2><div class="v" id="t">%s</div><button data-c="t">제목 복사</button><span class="done" id="d-t"></span></div>
%s
<div class="card"><h2><span class="n">3</span>본문</h2><button id="cb">본문 복사</button><span class="done" id="d-b"></span><p class="mute">회색 칸은 붙여 넣으면 실제 사진으로 들어갑니다.</p><div class="prev">%s</div></div>
<div class="card"><h2><span class="n">4</span>태그</h2><div class="v" id="g">%s</div><button data-c="g">태그 복사</button><span class="done" id="d-g"></span></div>
<div class="card"><h2><span class="n">5</span>발행</h2><p class="mute">%s</p></div>
</main>
<div id="raw">%s</div>
<script>
const BODY=%s;
function mark(id){document.getElementById(id).textContent='복사됨 ✓';}
function sel(el){const r=document.createRange();r.selectNodeContents(el);const s=getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');s.removeAllRanges();}
document.querySelectorAll('button[data-c]').forEach(bt=>bt.onclick=async()=>{const el=document.getElementById(bt.dataset.c);try{await navigator.clipboard.writeText(el.textContent);}catch(e){sel(el);}mark('d-'+bt.dataset.c);});
const tb=document.getElementById('tb');if(tb)tb.onclick=async()=>{const im=document.getElementById('th');let ok=false;try{const c=document.createElement('canvas');c.width=im.naturalWidth;c.height=im.naturalHeight;c.getContext('2d').drawImage(im,0,0);const bl=await new Promise(r=>c.toBlob(r,'image/png'));await navigator.clipboard.write([new ClipboardItem({'image/png':bl})]);ok=true;}catch(e){}if(!ok){try{const r=document.createRange();r.selectNode(im);const s=getSelection();s.removeAllRanges();s.addRange(r);ok=document.execCommand('copy');s.removeAllRanges();}catch(e){}}document.getElementById('d-th').textContent=ok?'복사됨 ✓ (붙여 넣었는데 글자가 나오면 그림 오른쪽 클릭 → 이미지 복사)':'그림 오른쪽 클릭(휴대폰은 길게 누르기) → 이미지 복사';};
document.getElementById('cb').onclick=async()=>{try{await navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([BODY],{type:'text/html'}),'text/plain':new Blob([document.getElementById('raw').innerText],{type:'text/plain'})})]);}catch(e){sel(document.getElementById('raw'));}mark('d-b');};
</script>'''%(html.escape(ptitle),html.escape(ptitle),date,html.escape(m['title']),thumb_card,prev,html.escape(' '.join('#'+t for t in m['tags'])),when,b,json.dumps(b).replace('</','<\\/'))
open(out,'w').write(P)

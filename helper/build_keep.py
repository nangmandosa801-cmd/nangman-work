import base64,html,json,sys,re
src,title,when,blog,imgs,out,ptitle=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5].split(','),sys.argv[6],sys.argv[7]
body=open(src).read()
# body tags line
cards=[]
for i,f in enumerate(imgs,1):
    b=base64.b64encode(open(f).read() if False else open(f,'rb').read()).decode()
    cards.append(f'''<li class="imgcard"><div class="imgname">{i}. {html.escape(f)}</div><img id="im{i}" alt="{html.escape(f)}" src="data:image/png;base64,{b}"><div class="row"><button type="button" data-img="im{i}">그림 복사</button></div><div class="done" id="dim{i}"></div></li>''')
page=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(ptitle)}</title>
<style>
:root{{--bg:#f4f6f9;--fg:#1b2433;--sub:#5d6878;--line:#d5dce6;--accent:#1F3864;--card:#fff;--ok:#0b7a3b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#11151c;--fg:#e4e9f0;--sub:#9aa6b6;--line:#2a3340;--accent:#7fa6dd;--card:#181e27;--ok:#5fe39b;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#11151c;--fg:#e4e9f0;--sub:#9aa6b6;--line:#2a3340;--accent:#7fa6dd;--card:#181e27;--ok:#5fe39b;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 "Noto Sans KR",system-ui,sans-serif;padding:24px 16px 48px}}
.wrap{{max-width:760px;margin:0 auto;display:grid;gap:18px}}
h1{{font-size:22px;margin:0;text-wrap:balance}}
.meta{{color:var(--sub);font-size:14px}}
.when{{font-size:28px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums}}
.step{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;display:grid;gap:10px;min-width:0}}
.step h2{{font-size:15px;margin:0;display:flex;gap:10px;align-items:center}}
.n{{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--accent);color:var(--card);font-size:13px;font-weight:700;flex:none}}
.val{{background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:10px;word-break:break-all}}
button{{font:inherit;font-weight:600;background:var(--accent);color:var(--card);border:0;border-radius:8px;padding:10px 16px;cursor:pointer;justify-self:start}}
button:focus-visible{{outline:3px solid var(--fg);outline-offset:2px}}
.done{{color:var(--ok);font-size:14px;min-height:1.2em}}
ol.imgs{{list-style:none;margin:0;padding:0;display:grid;gap:14px}}
.imgcard img{{max-width:100%;border:1px solid var(--line);border-radius:6px;display:block;margin:6px 0}}
.row{{display:flex;gap:12px;align-items:center;flex-wrap:wrap}} .dl{{color:var(--accent)}}
details summary{{cursor:pointer;color:var(--sub);font-size:14px}}
#body{{background:#fff;color:#222;border:1px solid var(--line);border-radius:6px;padding:12px;overflow:auto;max-height:420px}}
</style></head><body><div class="wrap">
<div><h1>{html.escape(title)}</h1><div class="meta">{html.escape(blog)} · 네이버 붙여넣기용 · 위에서부터 차례대로</div></div>
<div class="step"><div class="meta">예약 시각</div><div class="when">{html.escape(when)}</div></div>
<div class="step"><h2><span class="n">1</span>제목</h2><div class="val" id="t">{html.escape(title)}</div><button id="bt" type="button">제목 복사</button><div class="done" id="dt"></div></div>
<div class="step"><h2><span class="n">2</span>본문 (글 · 표 · 상자)</h2><div class="meta">네이버 본문을 한 번 클릭한 뒤 Ctrl+V. 점선 상자는 그림 자리입니다.</div><button id="bb" type="button">본문 복사</button><div class="done" id="db"></div>
<details><summary>본문 미리 보기</summary><div id="body">{body}</div></details></div>
<div class="step"><h2><span class="n">3</span>그림 — 점선 상자 자리에 이 순서로</h2><ol class="imgs">{''.join(cards)}</ol></div>
<div class="step"><h2><span class="n">4</span>발행한 뒤</h2><div class="meta">글 주소를 채팅에 알려 주시면 장부와 스레드 홍보(19:40 루틴)에 넣습니다.</div></div>
</div>
<script>
function ok(id,m){{document.getElementById(id).textContent=m}}
document.getElementById('bt').onclick=async()=>{{try{{await navigator.clipboard.writeText(document.getElementById('t').textContent);ok('dt','복사했습니다')}}catch(e){{ok('dt','복사가 막혔습니다. 글자를 직접 선택해 복사하세요')}}}};
document.getElementById('bb').onclick=async()=>{{const h=document.getElementById('body').innerHTML;try{{await navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob([document.getElementById('body').innerText],{{type:'text/plain'}})}})]);ok('db','복사했습니다')}}catch(e){{const r=document.createRange();r.selectNodeContents(document.getElementById('body'));const s=getSelection();s.removeAllRanges();s.addRange(r);try{{document.execCommand('copy');ok('db','복사했습니다')}}catch(_){{ok('db','미리 보기를 열어 직접 선택해 복사하세요')}}s.removeAllRanges()}}}};
document.querySelectorAll('button[data-img]').forEach(b=>b.onclick=async()=>{{const id=b.dataset.img;try{{const r=await fetch(document.getElementById(id).src);const bl=await r.blob();await navigator.clipboard.write([new ClipboardItem({{'image/png':bl}})]);ok('d'+id,'그림을 복사했습니다')}}catch(e){{ok('d'+id,'복사가 막혔습니다. 그림을 오른쪽 클릭해 복사하세요')}}}});
</script></body></html>'''
open(out,'w').write(page)

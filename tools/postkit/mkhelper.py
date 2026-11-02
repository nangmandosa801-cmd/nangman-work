#!/usr/bin/env python3
"""발행 도우미 만들기 한 줄 (사용자 11/3 「도우미 만들기를 명령 한 줄로 줄이기」)
원고 md 하나 → 사진 창고 주소 → 도우미 html + 큐 줄. 도구 호출 약 25번 → 약 8번.

1) prep   python3 mkhelper.py prep <원고.md> <tag>
          원고의 !=사진을 순서대로 한 장(세로 15,000px 이하씩)으로 이어 붙임 → /home/claude/w/_mk/<tag>/sp0.jpg …
          출력 JSON: 스프라이트 파일 · 크기(Upload-Post create_media_upload에 그대로 넣음)
2) put    python3 mkhelper.py put <sprite.jpg> '<upload_url>'      (curl PUT, 200 확인)
3) js     python3 mkhelper.py js <tag> '<media_url0>' ['<media_url1>' …]
          → 브라우저(블로거 낭만 창고 새 초안)에서 javascript_tool 로 그대로 실행할 코드 한 덩어리를 출력.
             코드가 사진을 넣고 30초 기다린 뒤 「이름 토큰」 목록을 돌려준다.
4) build  python3 mkhelper.py build <원고.md> <tag> '<YYYY-MM-DD HH:MM | 카테고리>' <tokens.txt>
          tokens.txt = 3)의 결과를 그대로 저장한 것. → urls.json · 도우미 html(when 줄 포함) · 큐 「대기」 줄 추가
          출력: 도우미 파일 경로(→ Artifact publish) · 큐 파일 경로(→ Artifact publish, url=큐 주소)
"""
import sys, os, re, json, subprocess
from PIL import Image
K = os.path.dirname(os.path.abspath(__file__)); W = '/home/claude/w/_mk'
QUEUE = '/home/claude/w/queue/naver_queue.html'; MAXH = 15000
def imgs(md):
    return [l[2:].strip() for l in open(md, encoding='utf8') if l.startswith('!=')]
def prep(md, tag):
    d = f'{W}/{tag}'; os.makedirs(d, exist_ok=True)
    L = imgs(md); sheets = [[]]; h = 0
    for k, p in enumerate(L, 1):
        im = Image.open(p).convert('RGB')
        if h + im.height > MAXH and sheets[-1]: sheets.append([]); h = 0
        sheets[-1].append((f'{tag}_{k:02d}', p, im)); h += im.height
    out = []; boxes = []
    for i, sh in enumerate(sheets):
        Wd = max(x[2].width for x in sh); Ht = sum(x[2].height for x in sh)
        S = Image.new('RGB', (Wd, Ht), 'white'); y = 0; b = []
        for n, p, im in sh: S.paste(im, (0, y)); b.append([n, 0, y, im.width, im.height]); y += im.height
        f = f'{d}/sp{i}.jpg'; S.save(f, quality=92); out.append({'file': f, 'size': os.path.getsize(f)}); boxes.append(b)
    json.dump({'boxes': boxes, 'n': len(L)}, open(f'{d}/sp.json', 'w'))
    print(json.dumps({'tag': tag, 'photos': len(L), 'sprites': out}, ensure_ascii=False))
def put(f, url):
    r = subprocess.run(['curl', '-sS', '-X', 'PUT', '-H', 'Content-Type: image/jpeg', '--data-binary', '@' + f, url, '-w', '%{http_code}'], capture_output=True, text=True)
    print(r.stdout[-3:] or r.stderr[-200:])
def js(tag, urls):
    B = json.load(open(f'{W}/{tag}/sp.json'))['boxes']
    D = [{'u': u, 'b': b} for u, b in zip(urls, B)]
    code = ("const D=" + json.dumps(D) + ";window._st='run';await (async()=>{const files=[];for(const s of D){const bmp=await createImageBitmap(await (await fetch(s.u)).blob());"
            "for(const [n,x,y,w,h] of s.b){const c=document.createElement('canvas');c.width=w;c.height=h;c.getContext('2d').drawImage(bmp,x,y,w,h,0,0,w,h);"
            "const b=await new Promise(r=>c.toBlob(r,'image/jpeg',0.9));files.push(new File([b],n+'.jpg',{type:'image/jpeg'}));}}"
            "const fr=document.querySelector('iframe.editable');const body=fr.contentDocument.body;const dt=new DataTransfer();files.forEach(x=>dt.items.add(x));"
            "for(const t of ['dragenter','dragover','drop']) body.dispatchEvent(new DragEvent(t,{bubbles:true,cancelable:true,dataTransfer:dt}));"
            "const need=files.length;for(let i=0;i<40;i++){await new Promise(r=>setTimeout(r,1500));const n=[...fr.contentDocument.querySelectorAll('img')].filter(i=>i.src.includes('googleusercontent')).length;if(n>=need)break;}"
            "})();const d=document.querySelector('iframe.editable').contentDocument;"
            "[...d.querySelectorAll('img')].map(i=>(i.closest('a')?.href||i.src)).filter(s=>s.includes('googleusercontent')).map(s=>{const m=s.match(/R29vZ2xl\\/([^/]+)\\/[^/]+\\/([^/?]+)$/);return m?m[2]+' '+m[1]:''}).filter(Boolean).join('\\n')")
    print(code)
def build(md, tag, when, tok):
    d = f'{W}/{tag}'; n = json.load(open(f'{d}/sp.json'))['n']; m = {}
    for l in open(tok, encoding='utf8'):
        p = l.split()
        if len(p) == 2 and p[0].startswith(tag + '_'): m[p[0]] = f'https://blogger.googleusercontent.com/img/b/R29vZ2xl/{p[1]}/s1600/{p[0]}'
    U = [m.get(f'{tag}_{k:02d}.jpg') for k in range(1, n + 1)]
    miss = [k + 1 for k, u in enumerate(U) if not u]
    if miss: print(json.dumps({'error': 'missing_urls', 'photos': miss})); return
    json.dump(U, open(f'{d}/urls.json', 'w'))
    title = open(md, encoding='utf8').readline().lstrip('# ').strip()
    out = f'{os.path.dirname(os.path.abspath(md))}/{tag}.html'
    subprocess.run(['python3', f'{K}/postkit.py', out, title.split(',')[0], md], env={**os.environ, 'URLS': f'{d}/urls.json'}, check=True, capture_output=True)
    s = open(out).read().replace('<div class="t" id="t0">', f'<div class="c" id="when">{when}</div><div class="t" id="t0">', 1); open(out, 'w').write(s)
    print(json.dumps({'helper': out, 'photos': n, 'title': title, 'queue_row': 'Artifact publish 후 helper_url로 mkhelper.py queue 실행'}, ensure_ascii=False))
def queue(when, title, url, label):
    q = open(QUEUE, encoding='utf8').read()
    row = f'<tr data-state="wait"><td class="st">대기</td><td>{when}</td><td>{title}</td><td><a href="{url}">{label}</a></td></tr>'
    w = when.split('|')[0].strip(); i = q.find(f'<td>{w}')
    if i > 0:  # 같은 날짜·시간의 「원고 준비」 줄을 바꿈
        a = q.rfind('<tr', 0, i); b = q.find('</tr>', i) + 5; q = q[:a] + row + q[b:]
    else:
        k = q.find('<tr data-state="plan">'); k = k if k > 0 else q.find('</tbody>'); q = q[:k] + row + '\n' + q[k:]
    open(QUEUE, 'w', encoding='utf8').write(q); print(json.dumps({'queue': QUEUE, 'row': w}, ensure_ascii=False))
if __name__ == '__main__':
    a = sys.argv[1:]
    {'prep': lambda: prep(a[1], a[2]), 'put': lambda: put(a[1], a[2]), 'js': lambda: js(a[1], a[2:]),
     'build': lambda: build(a[1], a[2], a[3], a[4]), 'queue': lambda: queue(a[1], a[2], a[3], a[4])}[a[0]]()

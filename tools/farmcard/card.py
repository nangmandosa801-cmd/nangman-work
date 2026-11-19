"""농장 글 썸네일 · 소개 카드 (실사 + 정감 있는 글씨) — Playwright로 HTML을 그림으로.
글꼴: /home/claude/fonts/farmcard (없으면 npm pack @fontsource/{nanum-pen-script,gowun-batang,gowun-dodum} 풀어 넣기).
python3 card.py thumb <사진> <out.jpg> "<작은말>" "<큰 제목 · |로 줄바꿈>" "<아래 이름>"
python3 card.py intro <사진> <out.jpg> "<제목>" "<줄1>|<줄2>|..." "<아래>"
"""
import sys, base64, pathlib
from playwright.sync_api import sync_playwright
F = pathlib.Path('/home/claude/fonts/farmcard')
def css():
    out = ''
    for n in ['nanum-pen-script', 'gowun-batang', 'gowun-dodum']:
        for w in ['400', '700']:
            p = F/n/f'{w}.css'
            if p.exists(): out += p.read_text().replace("url(./", f"url(file://{F/n}/")
    return out
def img64(p):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
BASE = """<meta charset="utf-8"><style>{css}*{{margin:0;box-sizing:border-box}}body{{width:{w}px;height:{h}px;background:#F6F1E4}}</style>"""
def thumb(photo, out, small, big, name):
    parts = big.split('|'); big = parts[0]; sub = '<br>'.join(parts[1:])
    html = BASE.format(css=css(), w=1080, h=1080) + f"""
<div style="position:relative;width:1080px;height:1080px;overflow:hidden">
 <img src="{img64(photo)}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
 <div style="position:absolute;left:0;right:0;bottom:0;height:62%;background:linear-gradient(to bottom,rgba(246,241,228,0) 0%,rgba(246,241,228,.92) 38%,#F6F1E4 60%)"></div>
 <div style="position:absolute;left:70px;right:70px;bottom:70px;color:#3F4A36">
  <div style="font-family:'Nanum Pen Script';font-size:64px;color:#7E9470;line-height:1">{small}</div>
  <div style="font-family:'Gowun Batang';font-weight:700;font-size:92px;line-height:1.15;margin-top:14px;letter-spacing:-1px">{big}</div>
  <div style="font-family:'Gowun Batang';font-weight:700;font-size:58px;line-height:1.3;margin-top:10px;color:#5E7552">{sub}</div>
  <div style="display:flex;align-items:center;gap:16px;margin-top:30px;font-family:'Gowun Dodum';font-size:36px;color:#6B6455">
   <span style="display:inline-block;width:46px;height:3px;background:#C9A86A"></span>{name}</div>
 </div>
 <div style="position:absolute;top:44px;left:50px;font-family:'Gowun Dodum';font-size:30px;color:#fff;background:rgba(63,74,54,.55);padding:10px 22px;border-radius:30px">팜 에디터</div>
</div>"""
    shot(html, out, 1080, 1080)
def intro(photo, out, title, lines, foot):
    lis = ''.join(f'<li style="margin:14px 0">{x}</li>' for x in lines.split('|'))
    html = BASE.format(css=css(), w=1080, h=1350) + f"""
<div style="width:1080px;height:1350px;background:#F6F1E4;padding:60px;display:flex;flex-direction:column;gap:36px">
 <img src="{img64(photo)}" style="width:960px;height:560px;object-fit:cover;border-radius:28px">
 <div style="font-family:'Nanum Pen Script';font-size:58px;color:#7E9470;line-height:1">농장을 소개합니다</div>
 <div style="font-family:'Gowun Batang';font-weight:700;font-size:74px;color:#3F4A36;line-height:1.1;margin-top:-14px">{title}</div>
 <ul style="font-family:'Gowun Dodum';font-size:38px;color:#55594F;line-height:1.45;padding-left:40px;margin:0">{lis}</ul>
 <div style="margin-top:auto;font-family:'Gowun Dodum';font-size:30px;color:#8A8270;border-top:2px solid #E2D8C2;padding-top:22px">{foot}</div>
</div>"""
    shot(html, out, 1080, 1350)
def shot(html, out, w, h):
    tmp = pathlib.Path('/tmp/_card.html'); tmp.write_text(html, encoding='utf-8')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto('file://' + str(tmp)); pg.wait_for_timeout(800)
        pg.screenshot(path='/tmp/_card.png'); b.close()
    from PIL import Image
    Image.open('/tmp/_card.png').convert('RGB').save(out, quality=90)
if __name__ == '__main__':
    a = sys.argv
    (thumb if a[1] == 'thumb' else intro)(*a[2:])

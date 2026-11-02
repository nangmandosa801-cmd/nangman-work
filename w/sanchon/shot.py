import sys,asyncio
from playwright.sync_api import sync_playwright
src,out,w=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 760
html=open(src,encoding='utf-8').read()
page_html='<html><head><meta charset="utf-8"><style>body{font-family:"Noto Sans KR","Noto Sans CJK KR",sans-serif;width:693px;margin:20px auto;line-height:1.8;} p{margin:0;}</style></head><body>'+html+'</body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':w,'height':1000}); pg.set_content(page_html); pg.wait_for_timeout(300)
    h=pg.evaluate('document.body.scrollHeight'); print('height',h)
    n=0; step=1500
    for y in range(0,h,step):
        pg.screenshot(path=f'{out}_{n}.png',clip={'x':0,'y':y,'width':w,'height':min(step,h-y)},full_page=True); n+=1
    b.close(); print('shots',n)

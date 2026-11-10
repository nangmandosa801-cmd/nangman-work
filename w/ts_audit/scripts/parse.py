import re,json,glob,os
from bs4 import BeautifulSoup
out=[]
for f in sorted(glob.glob('/home/claude/w/ts_audit/raw/*.html'),key=lambda x:int(os.path.basename(x)[:-5])):
    n=int(os.path.basename(f)[:-5]); h=open(f,encoding='utf8').read()
    s=BeautifulSoup(h,'lxml')
    def meta(p):
        m=s.find('meta',attrs={'property':p}); return m['content'] if m else ''
    c=s.select_one('div.article-view div.contents_style') or s.select_one('div.contents_style')
    cat=''
    a=s.select_one('div.another_category h4 a')
    if a: cat=a.get_text(strip=True)
    body=c.get_text(' ',strip=True) if c else ''
    nolsp=re.sub(r'\s','',body)
    links=[x.get('href','') for x in c.find_all('a')] if c else []
    nav=[]
    for l in links:
        m=re.search(r'blog\.naver\.com/(?:PostView\.naver\?blogId=)?([A-Za-z0-9_\-]+)(?:/|&logNo=)(\d+)',l)
        if m: nav.append([m.group(1),m.group(2),l])
    # sentences
    paras=[p.get_text(' ',strip=True) for p in c.find_all(['p','li','h2','h3','h4','td','th'])] if c else []
    og=meta('og:image')
    out.append(dict(no=n,title=meta('og:title'),url=f'https://talk7921.tistory.com/{n}',
      date=meta('article:published_time')[:10],category=cat,chars=len(body),chars_nospace=len(nolsp),
      tables=len(c.find_all('table')) if c else 0,images=len(c.find_all('img')) if c else 0,
      og_image=og,og_real=bool(og) and 'opengraph.png' not in og,
      naver_links=nav,text=body,visibility=(re.search(r'data-entry-visibility="(\w+)"',h) or [None,''])[1]))
json.dump(out,open('/home/claude/w/ts_audit/raw/parsed.json','w'),ensure_ascii=False)
for o in out: print(o['no'],o['date'],o['category'],o['chars'],o['tables'],o['images'],int(o['og_real']),len(o['naver_links']),o['title'][:40])

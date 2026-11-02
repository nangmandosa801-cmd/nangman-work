import sys
from bs4 import BeautifulSoup
n=sys.argv[1]
s=BeautifulSoup(open(f'src/{n}.html').read(),'html.parser'); c=s.select_one('.se-main-container')
for i,x in enumerate(c.find_all('div',class_='se-component',recursive=False)):
    k=x['class'][1]
    if k=='se-text':
        for j,p in enumerate(x.select('p.se-text-paragraph')):
            for br in p.find_all('br'): br.replace_with('⏎')
            t=p.get_text('',strip=True).strip('​')
            if t: print(f'[{i}.{j}] {t}')
    elif k=='se-table':
        print(f'[{i}] <TABLE>')
        for tr in x.select('tr'):
            cells=[]
            for td in tr.select('td'):
                cells.append(' / '.join(p.get_text('',strip=True).strip('​') for p in td.select('p') if p.get_text('',strip=True).strip('​')))
            print('    ',' || '.join(cells))
    elif k=='se-image':
        im=x.select_one('img'); u=(im.get('data-lazy-src') or im.get('src')); print(f'[{i}] <IMG {u.split("/")[-1][:50]}>')
    else: print(f'[{i}] <{k}>',x.get_text(' ',strip=True)[:100])

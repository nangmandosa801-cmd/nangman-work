import sys
from bs4 import BeautifulSoup
n=sys.argv[1]
s=BeautifulSoup(open(f'src/{n}.html').read(),'html.parser'); c=s.select_one('.se-main-container')
for i,x in enumerate(c.find_all('div',class_='se-component',recursive=False)):
    k=x['class'][1]
    if k=='se-text':
        ps=[p.get_text('',strip=True) for p in x.select('p.se-text-paragraph')]
        ps=[p for p in ps if p.strip('​')]
        print(i,'T',' | '.join(p[:70] for p in ps) or '(blank)')
    elif k=='se-table':
        tds=x.select('td'); print(i,'TABLE',len(x.select('tr')),'x',len(tds),'|',x.get_text(' ',strip=True)[:110])
    elif k=='se-image':
        im=x.select_one('img'); print(i,'IMG',(im.get('data-lazy-src') or im.get('src'))[-50:], '| cap:',x.select_one('.se-caption').get_text(strip=True)[:40] if x.select_one('.se-caption') else '')
    else:
        print(i,k,x.get_text(' ',strip=True)[:100])

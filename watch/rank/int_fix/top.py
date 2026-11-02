import sys
from bs4 import BeautifulSoup
n=sys.argv[1]; k=int(sys.argv[2]) if len(sys.argv)>2 else 4
s=BeautifulSoup(open(f'src/{n}.html').read(),'html.parser'); c=s.select_one('.se-main-container')
for i,x in enumerate(c.find_all('div',class_='se-component',recursive=False)[:k]):
    for p in x.select('p.se-text-paragraph'):
        t=p.get_text('',strip=True).strip('​')
        sp=p.find('span'); cl=' '.join(sp.get('class',[])) if sp else ''
        print(i,'|',cl.replace('se-ff- ','')[:22],'|',t)

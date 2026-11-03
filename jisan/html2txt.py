import sys,re,json,os
from bs4 import BeautifulSoup
def conv(html,title,tags):
    import re as _r
    s=BeautifulSoup(html,'html.parser'); out=['[제목] '+title,'']
    for el in s.find_all(['p','table'],recursive=False):
        if el.name=='p':
            t=el.get_text('').replace('\xa0',' ')
            if not t: continue
            st=el.get('style','')
            if 'font-size:34px' in st: continue
            if 'font-size:27px' in st: out+=['','## '+t,'']; continue
            if 'font-size:17px' in st and 'letter-spacing' in st: out.append('[머리말] '+t); continue
            if 'color:#8A8578' in st: out.append('[표 설명] '+t); continue
            a=[x for x in el.find_all('a')]
            if a:
                for x in a: x.replace_with(x.get_text(strip=True)+' ('+x.get('href','')+')')
                t=el.get_text('')
            out.append(t)
        else:
            txt=el.get_text(' ',strip=True).replace('\xa0',' ')
            if not txt: out.append('---'); continue
            m=re.match(r'(jisandream_\S+\.png) — (.*)',txt)
            if m: out.append('[그림: %s — %s]'%(m.group(1),m.group(2))); continue
            rows=el.find_all('tr')
            if len(rows)==1 and len(rows[0].find_all('td'))==1:
                ps=[p.get_text(' ',strip=True) for p in el.find_all('p')]
                for x in el.find_all('a'): pass
                lines=[]
                for p in el.find_all('p'):
                    for x in p.find_all('a'): x.replace_with(x.get_text(strip=True)+' ('+x.get('href','')+')')
                    lines.append(p.get_text(''))
                if not [l for l in lines if l]: lines=[el.get_text(' ',strip=True)]
                out+=['[상자]']+[l for l in lines if l]+['[/상자]']; continue
            out.append('[표]')
            for r in rows:
                cells=[]
                for c in r.find_all('td'):
                    for x in c.find_all('a'): x.replace_with(x.get_text(strip=True)+' ('+x.get('href','')+')')
                    cells.append(c.get_text(''))
                out.append(' | '.join(cells))
            out.append('[/표]')
    out+=['','[태그] '+' '.join('#'+t for t in tags)]
    out=[_r.sub(r'[ \t\xa0]+',' ',x).strip() for x in out]
    txt='\n'.join(out); txt=re.sub(r'\n{3,}','\n\n',txt); return txt

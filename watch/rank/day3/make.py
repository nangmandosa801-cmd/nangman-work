import json,re
from bs4 import BeautifulSoup
D=json.load(open('../helper_v2_data.json'));S=json.load(open('stage2.json'))
items=[]
for i in range(17,25):
    x=D[i-1]
    r=BeautifulSoup('<div>'+S[str(i)]+'</div>','html.parser').div
    def empty(c): return c.name=='p' and not c.get_text(strip=True) and not c.find('img')
    ch=[c for c in r.children if getattr(c,'name',None)]
    while ch and empty(ch[-1]): ch.pop().decompose()
    prev=0
    for c in list(r.children):
        if not getattr(c,'name',None): continue
        if empty(c):
            prev+=1
            if prev>=3: c.decompose()
        else: prev=0
    body=str(r)[5:-6]
    open(f'body_{i}_{x["n"]}.html','w').write(body)
    items.append(dict(no=i,n=x['n'],g=x['g'],kw=x['kw'],old=x['old'],nt=x['nt'],tags=x['tags'],body=body))
json.dump(items,open('day3_items.json','w'),ensure_ascii=False)
data=json.dumps(items,ensure_ascii=False).replace('</','<\\/')
tpl=open('tpl.html').read()
open('helper_day3.html','w').write(tpl.replace('/*DATA*/',data))
print(len(data))

import subprocess,re,json,html,sys
from concurrent.futures import ThreadPoolExecutor
ids=json.load(open('res.json'))
from collections import Counter
c=Counter(i for v in ids.values() for i in v)
cand=[i for i,_ in c.most_common(45)]
def rss(i):
    x=subprocess.run(['curl','-s','-m','15',f'https://rss.blog.naver.com/{i}.xml'],capture_output=True,text=True).stdout
    t=re.search(r'<title>(.*?)</title>',x,re.S); t=html.unescape(t.group(1)) if t else ''
    titles=[html.unescape(a) for a in re.findall(r'<item>.*?<title>(.*?)</title>',x,re.S)][:12]
    desc=html.unescape(re.search(r'<description>(.*?)</description>',x,re.S).group(1)) if '<description>' in x else ''
    phones=sorted(set(re.findall(r'010[-. ]?\d{3,4}[-. ]?\d{4}',x)))[:4]
    dates=re.findall(r'<pubDate>(.*?)</pubDate>',x)[:1]
    door=sum(1 for s in titles if re.search(r'강화|자동문|도어|샷시|샤시|유리문|출입문|외풍',s))
    return dict(id=i,name=t[:40],desc=desc[:80],phones=phones,last=dates,door=door,titles=titles[:6])
with ThreadPoolExecutor(6) as ex: out=list(ex.map(rss,cand))
json.dump(out,open('rss.json','w'),ensure_ascii=False,indent=1)
for o in sorted(out,key=lambda o:-o['door']):
    if o['door']>=4: print(o['id'],'|',o['name'],'|',o['phones'],'|',o['last'],'|',o['door'],'|',' / '.join(o['titles'][:4])[:250])

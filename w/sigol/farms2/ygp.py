import json,re,ssl,urllib.request,concurrent.futures as cf
ids=set()
for c in ['농장','체험','체험마을','키즈']: ids|=set(json.load(open(f'list_{c}.json')))
ids=sorted(ids,key=int)
ctx=ssl.create_default_context()
def one(i):
    try:
        r=urllib.request.urlopen(urllib.request.Request(f'https://xn--ok0b236bp0a.com/place/{i}',headers={'User-Agent':'Mozilla/5.0'}),timeout=15,context=ctx)
        h=r.read(9000).decode('utf8','ignore'); r.close()
    except Exception: return None
    g=lambda p:(re.search(p,h,re.S) or [None,''])[1]
    return dict(id=i,name=g(r'"name":\s*"([^"]*)"'),tel=g(r'"telephone":\s*"([^"]*)"'),addr=g(r'"streetAddress":\s*"([^"]*)"').strip(),desc=g(r'"description":\s*"([^"]*)"')[:200],kw=g(r"name='keywords' content='([^']*)'"))
with cf.ThreadPoolExecutor(4) as ex: res=[r for r in ex.map(one,ids) if r]
json.dump(res,open('places.json','w'),ensure_ascii=False)
mob=[r for r in res if re.match(r'01[016789]',r['tel'].replace('-',''))]
print(len(ids),len(res),len(mob))

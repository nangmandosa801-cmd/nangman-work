import re,json,sys,ssl,urllib.request,concurrent.futures as cf,time
a,b=int(sys.argv[1]),int(sys.argv[2]); out=sys.argv[3]
ctx=ssl.create_default_context()
def one(i):
    try:
        r=urllib.request.urlopen(urllib.request.Request(f'https://xn--ok0b236bp0a.com/place/{i}',headers={'User-Agent':'Mozilla/5.0'}),timeout=12,context=ctx)
        h=r.read(9000).decode('utf8','ignore'); r.close()
    except Exception as e: return None
    tel=re.search(r'"telephone":\s*"([^"]*)"',h)
    if not tel or not re.search(r'01[016789]-?\d{3,4}-?\d{4}',tel.group(1)): return None
    g=lambda p:(re.search(p,h,re.S) or [None,''])[1]
    return dict(id=i,name=g(r'"name":\s*"([^"]*)"'),tel=tel.group(1),addr=g(r'"streetAddress":\s*"([^"]*)"').strip(),
        desc=g(r'"description":\s*"([^"]*)"')[:300],kw=g(r"name='keywords' content='([^']*)'"))
t=time.time();res=[]
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(one,range(a,b)):
        if r: res.append(r)
json.dump(res,open(out,'w'),ensure_ascii=False)
print(len(res),round(time.time()-t,1))

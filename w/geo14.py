import json,urllib.request,urllib.parse,time,pandas as pd
def get(params):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=20&'+urllib.parse.urlencode(params)
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-research/1.0 (blog analysis)'}),timeout=30))
        except Exception as e: time.sleep(3)
    return []
a=pd.read_pickle('addr14.pkl')
t=pd.read_pickle('seoul8.pkl'); t=t[t['동']!='-']
t['d']=pd.to_numeric(t['동'].str.extract(r'^(\d{3,4})$')[0],errors='coerce')
out={}
for n,r in a.iterrows():
    c=get({'q':f"서울 {r['시군']} {r['도로명']}"}); time.sleep(1.1)
    if not c: c=get({'q':f"{r['시군']} {r['읍면동']} {r['번지']}"}); time.sleep(1.1)
    if not c: print(n,'NO CENTER',flush=True); continue
    lat,lon=float(c[0]['lat']),float(c[0]['lon'])
    ds=sorted(t[t.단지명==n].d.dropna().astype(int).unique())
    lo,hi=min(ds),max(ds)
    allds=[x for x in range(lo,hi+1) if x//100 in {d//100 for d in ds}]
    vb=f"{lon-0.008},{lat+0.006},{lon+0.008},{lat-0.006}"
    res={}
    for d in allds:
        rr=get({'q':f'{d}동','viewbox':vb,'bounded':1}); time.sleep(1.1)
        b=[x for x in rr if x.get('class')=='building']
        if b: res[d]=(float(b[0]['lat']),float(b[0]['lon']),b[0]['display_name'][:60])
    out[n]={'center':(lat,lon),'all':allds,'found':res}
    print(n,(lat,lon),f"{len(res)}/{len(allds)}",flush=True)
    json.dump(out,open('geo14.json','w'),ensure_ascii=False)
print('DONE',flush=True)

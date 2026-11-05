import json,math
ST={'풍산':(37.5519584,127.2036311),'시청':(37.5417742,127.2067037),'검단산':(37.5397035,127.2235329)}
def d(a,b):
    R=6371000; la1,lo1=map(math.radians,a); la2,lo2=map(math.radians,b)
    x=(lo2-lo1)*math.cos((la1+la2)/2); y=la2-la1; return R*math.hypot(x,y)
cx=json.load(open('cx.json')); fix=json.load(open('fix.json')) if __import__('os').path.exists('fix.json') else {}
for k,v in cx.items():
    v=fix.get(k,v)
    if not v: print('NONE',k); continue
    ds={s:round(d((v[0],v[1]),p)) for s,p in ST.items()}
    s=min(ds,key=ds.get)
    if ds[s]<1500:
        exact = v[2].split(',')[0].strip()[0].isdigit() or '아파트' in v[2] or k in fix
        print(f"{s:4} {ds[s]:5} {'ok ' if exact else 'ROAD'} {k} | {v[2][:30]}")

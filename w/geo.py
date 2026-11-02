import pandas as pd, urllib.request, urllib.parse, json, time, re
g=pd.read_pickle('unjeong_cx.pkl')
def q(s):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=kr&q='+urllib.parse.quote(s)
    try:
        j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-analysis/1.0'}),timeout=20).read())
    except Exception as e: return None
    time.sleep(1.1)
    return (float(j[0]['lat']),float(j[0]['lon']),j[0]['display_name'][:60]) if j else None
out=[]
for _,r in g.iterrows():
    res=None;how=''
    if isinstance(r.road,str) and r.road.strip():
        res=q('파주시 '+r.road); how='road'
    if not res:
        nm=re.sub(r'\(.*?\)','',r['단지명']); res=q('파주 '+nm); how='name'
    out.append((r['읍면동'],r['단지명'],how,res))
    print(r['단지명'],how,res,flush=True)
pd.to_pickle(out,'unjeong_geo.pkl')

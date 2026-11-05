import pandas as pd, urllib.request, urllib.parse, json, time, os
m=pd.concat([pd.read_pickle('/home/claude/rtn/M2025.pkl'),pd.read_pickle('/home/claude/rtn/M2026.pkl')])
m=m[m['시군구'].str.contains('하남시')]
m['dong']=m['시군구'].str.split().str[-1]
m=m[m.dong.isin(['풍산동','덕풍동','신장동','창우동','선동'])]
cx=m.groupby(['dong','단지명','도로명']).size().reset_index()
def q(s):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=kr&q='+urllib.parse.quote(s)
    try: j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-analysis/1.0'}),timeout=20).read())
    except Exception as e: j=None
    time.sleep(1.1)
    return (float(j[0]['lat']),float(j[0]['lon']),j[0]['display_name'][:60]) if j else None
out=json.load(open('cx.json')) if os.path.exists('cx.json') else {}
for _,r in cx.iterrows():
    k=r['단지명']+'|'+r['도로명']
    if k in out: continue
    res=q('하남시 '+r['도로명'])
    if not res: res=q('하남 '+r['단지명'])
    out[k]=res; print(k,res,flush=True)
    json.dump(out,open('cx.json','w'),ensure_ascii=False)

import json,urllib.request,urllib.parse,time,pandas as pd,re
s=pd.read_pickle('songdo.pkl')
g=s[s.y>=2023].groupby('단지명').agg(road=('도로명',lambda x:x.mode().iloc[0])).reset_index()
out={}
for _,r in g.iterrows():
    road=re.sub(r'\s+',' ',str(r.road)).strip()
    u='https://nominatim.openstreetmap.org/search?format=json&limit=3&addressdetails=1&'+urllib.parse.urlencode({'q':f'인천 연수구 {road}'})
    try: res=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-research/1.0'}),timeout=30))
    except Exception as e: res=[]
    dn=[x['display_name'] for x in res]
    hd=[m for d in dn for m in re.findall(r'송도\d동',d)]
    out[r.단지명]={'road':road,'hd':hd[0] if hd else '', 'dn':dn[0][:90] if dn else '','lat':res[0]['lat'] if res else None,'lon':res[0]['lon'] if res else None}
    print(r.단지명,out[r.단지명]['hd'],flush=True); time.sleep(1.1)
json.dump(out,open('sdgeo.json','w'),ensure_ascii=False)
print('DONE')

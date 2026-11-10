import requests, os, json, time
S=requests.Session(); S.headers['User-Agent']='nangman-analysis/1.0'
S.verify=os.path.expanduser('~/.ccr/ca-bundle.crt')
boxes={'dongtan':(37.150,127.040,37.230,127.140),'unjeong':(37.690,126.690,37.750,126.790)}
out=json.load(open('osm.json'))
for k,(s,w,n,e) in boxes.items():
    if k in out: continue
    Q=f'[out:json][timeout:90];(way["landuse"="residential"]["name"]({s},{w},{n},{e});relation["landuse"="residential"]["name"]({s},{w},{n},{e});way["building"="apartments"]["name"]({s},{w},{n},{e});node["railway"="station"]({s},{w},{n},{e}););out center tags;'
    for t in range(25):
        try:
            r=S.post('https://overpass-api.de/api/interpreter',data={'data':Q},timeout=150)
            if r.status_code==200 and 'elements' in r.text:
                out[k]=r.json()['elements']; print(k,len(out[k]),flush=True); json.dump(out,open('osm.json','w'),ensure_ascii=False); break
            else: print(k,r.status_code,flush=True); time.sleep(20)
        except Exception as e: print(k,'ERR',str(e)[:60],flush=True); time.sleep(20)
print('DONE')

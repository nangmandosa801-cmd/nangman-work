import pandas as pd, urllib.request, urllib.parse, json, time, sys
def q(s):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=kr&q='+urllib.parse.quote(s)
    try: j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-analysis/1.0'}),timeout=20).read())
    except Exception as e: j=None; print('ERR',e)
    time.sleep(1.1)
    return (float(j[0]['lat']),float(j[0]['lon']),j[0]['display_name'][:70]) if j else None
out={}
for s in sys.argv[1:]:
    out[s]=q(s); print(s,out[s],flush=True)
json.dump(out,open('st.json','w'),ensure_ascii=False)

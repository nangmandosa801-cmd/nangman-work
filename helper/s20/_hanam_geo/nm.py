import urllib.request, urllib.parse, json, time, sys
for s in sys.argv[1:]:
    u='https://nominatim.openstreetmap.org/search?format=json&limit=3&countrycodes=kr&viewbox=127.17,127.25&q='+urllib.parse.quote(s)
    u='https://nominatim.openstreetmap.org/search?format=json&limit=3&countrycodes=kr&q='+urllib.parse.quote(s)
    j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-analysis/1.0'}),timeout=20).read())
    print(s,[(e['lat'][:9],e['lon'][:10],e['type'],e['display_name'][:45]) for e in j],flush=True); time.sleep(1.1)

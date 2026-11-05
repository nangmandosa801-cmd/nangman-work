import urllib.request,urllib.parse,json,time
Q='''[out:json][timeout:90];
(
  way["landuse"="residential"]["name"](37.545,127.155,37.590,127.225);
  relation["landuse"="residential"]["name"](37.545,127.155,37.590,127.225);
  node["railway"="station"](37.530,127.150,37.600,127.240);
  way["highway"]["name"~"미사강변대로|미사강변한강로|미사강변중앙로|미사대로|미사강변북로|미사강변남로|미사강변동로|미사강변서로|미사강변한강로"](37.545,127.170,37.590,127.225);
  way["amenity"="school"]["name"](37.545,127.155,37.590,127.225);
);
out center tags;
'''
u='https://overpass-api.de/api/interpreter'
r=urllib.request.Request(u,data=urllib.parse.urlencode({'data':Q}).encode(),headers={'User-Agent':'nangman-analysis/1.0'})
j=json.loads(urllib.request.urlopen(r,timeout=120).read())
json.dump(j,open('op.json','w'),ensure_ascii=False)
els=j['elements']; print(len(els))
for e in els:
    t=e.get('tags',{}); c=e.get('center',{'lat':e.get('lat'),'lon':e.get('lon')})
    print(e['type'],e['id'],t.get('name'),t.get('railway') or t.get('landuse') or t.get('highway') or t.get('amenity'),round(c['lat'],5),round(c['lon'],5))

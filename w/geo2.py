import json,urllib.request,urllib.parse,time
def get(params):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=40&'+urllib.parse.urlencode(params)
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'nangman-research/1.0 (blog analysis)'}),timeout=30))
        except Exception: time.sleep(3)
    return []
g=json.load(open('geo14.json'))
keep=['DMC롯데캐슬더퍼스트','강동리버스트4단지','래미안힐스테이트고덕','마포그랑자이','마포프레스티지자이','북한산푸르지오','태릉해링턴플레이스']
out={}
for n in keep:
    lat,lon=g[n]['center']; cand={}
    for d in g[n]['all']:
        rr=get({'q':f'{d}동','viewbox':f"{lon-0.007},{lat+0.0055},{lon+0.007},{lat-0.0055}",'bounded':1}); time.sleep(1.05)
        cand[d]=[(float(x['lat']),float(x['lon']),x['display_name'][:70],x.get('osm_id')) for x in rr if x.get('class')=='building']
    out[n]={'center':(lat,lon),'cand':cand}
    json.dump(out,open('geo2.json','w'),ensure_ascii=False); print(n,'ok',flush=True)
print('DONE',flush=True)

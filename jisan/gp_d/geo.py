import urllib.request,urllib.parse,json,time
H={'User-Agent':'jisandream-blog/1.0'}
Q={'금남리':'금남리, 화도읍, 남양주시','대성리':'대성리, 청평면, 가평군','상천리':'상천리, 청평면, 가평군','상색리':'상색리, 가평읍, 가평군','하색리':'하색리, 가평읍, 가평군','서천리':'서천리, 남산면, 춘천시','당림리':'당림리, 서면, 춘천시',
 '금남IC':'금남IC, 남양주시','청평역':'청평역, 가평군','가평역':'가평역, 가평군','굴봉산역':'굴봉산역, 춘천시','자라섬':'자라섬, 가평군','남이섬':'남이섬, 춘천시','대성리역':'대성리역, 가평군','상천역':'상천역, 가평군','강촌역':'강촌역, 춘천시','설악IC':'설악IC, 가평군'}
out={}
for k,q in Q.items():
    u='https://nominatim.openstreetmap.org/search?format=json&limit=3&accept-language=ko&q='+urllib.parse.quote(q)
    try:
        j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read())
        out[k]=[(round(float(x['lat']),5),round(float(x['lon']),5),x.get('type'),x['display_name'][:60]) for x in j]
    except Exception as e: out[k]=str(e)[:100]
    print(k,out[k]); time.sleep(1.1)
json.dump(out,open('geo.json','w'),ensure_ascii=False)

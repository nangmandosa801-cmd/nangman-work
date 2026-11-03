import urllib.request,urllib.parse,json,time,math,io,sys
sys.path.insert(0,'/home/claude/blogkit')
from PIL import Image,ImageDraw
from thumbnail import F
H={'User-Agent':'jisandream-blog/1.0'}
def nom(q):
    u='https://nominatim.openstreetmap.org/search?format=json&limit=3&polygon_geojson=1&countrycodes=kr&q='+urllib.parse.quote(q)
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30)); time.sleep(1.2)
    for x in r:
        if x.get('geojson',{}).get('type') in ('Polygon','MultiPolygon'): return x['geojson']
    return None
P={}
for k,q in [('초이동','초이동, 하남시'),('감북동','감북동, 하남시'),('광암동','광암동, 하남시'),('감일동','감일동, 하남시'),('교산동','교산동, 하남시'),('춘궁동','춘궁동, 하남시'),('상산곡동','상산곡동, 하남시'),('하산곡동','하산곡동, 하남시')]:
    P[k]=nom(q); print(k, bool(P[k]))
json.dump(P,open('poly.json','w'))

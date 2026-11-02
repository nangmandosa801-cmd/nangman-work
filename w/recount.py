# -*- coding: utf-8 -*-
import pickle, urllib.request, re, time, os
from concurrent.futures import ThreadPoolExecutor
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
ids=[p['id'] for p in pickle.load(open('prospects.pkl','rb'))]
print('업체 블로그', len(ids))
CF='recount_raw.pkl'
raw=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def grab(bid):
    if bid in raw: return
    try:
        h=urllib.request.urlopen(urllib.request.Request(
            'https://rss.blog.naver.com/%s.xml'%bid,headers=UA),timeout=20).read().decode('utf-8','ignore')
        t=re.findall(r'<title><!\[CDATA\[(.*?)\]\]></title>',h,re.S)
        raw[bid]=t[1:] if t else []
    except Exception:
        raw[bid]=None
with ThreadPoolExecutor(8) as ex: list(ex.map(grab, ids))
pickle.dump(raw,open(CF,'wb'))
ok={k:v for k,v in raw.items() if v}
print('응답한 블로그', len(ok), '· 실패', sum(1 for v in raw.values() if not v))
print('제목 총합', sum(len(v) for v in ok.values()))

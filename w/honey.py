import json, urllib.parse, urllib.request, pickle
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def ac(w):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(w)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0'
       '&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=8) as r:
            return [i[0] for i in json.loads(r.read().decode('utf-8')).get('items',[[]])[0]]
    except Exception: return None
SEED=['꿀','벌꿀','아카시아꿀','밤꿀','야생화꿀','잡화꿀','사양벌꿀','천연꿀','토종꿀','honey',
      '꿀 선물','꿀 효능','꿀 구매','벌꿀 가격','꿀 추천','로얄제리','프로폴리스','화분',
      '벌집꿀','마누카꿀','꿀 고르는법','진짜 꿀','꿀 보관','꿀 결정']
SUF=list('가나다라마바사아자차카타파하')+[' 효능',' 가격',' 추천',' 선물',' 구매',' 차이',' 진짜',' 후기']
words=set(SEED)
for s in SEED:
    for x in SUF: words.add(s+x if x.startswith(' ') else s+' '+x)
words=sorted(words)
with ThreadPoolExecutor(32) as ex: r=dict(zip(words, ex.map(ac,words)))
h={}
for w,v in r.items():
    for s in (v or []): h[s]=h.get(s,0)+1
pickle.dump((r,h),open('honey.pkl','wb'))
print('조회',len(words),'수확',len(h))

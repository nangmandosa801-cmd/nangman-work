import json, urllib.parse, urllib.request, pickle, itertools
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
SEED=['인테리어','리모델링','올수리','도배','장판','싱크대','화장실 공사','욕실 공사',
      '주방 리모델링','샷시','중문','붙박이장','필름 시공','타일','조명 공사','확장 공사',
      '베란다 확장','인테리어 견적','인테리어 하자','인테리어 계약서','반셀프 인테리어',
      '셀프 인테리어','아파트 인테리어','구축 아파트','신축 입주','전세 인테리어']
SUF=list('가나다라마바사아자차카타파하')+list('0123456789')+[' 비용',' 가격',' 견적',' 추천',' 후기',' 순서',' 기간',' 주의']
words=set(SEED)
for s in SEED:
    for x in SUF: words.add(s+x if x.startswith(' ') else s+' '+x)
words=sorted(words)
print('1차 조회',len(words),flush=True)
with ThreadPoolExecutor(32) as ex: r1=dict(zip(words, ex.map(ac,words)))
harvest={}
for w,v in r1.items():
    for s in (v or []): harvest[s]=harvest.get(s,0)+1
print('수확한 말',len(harvest),flush=True)
pickle.dump((r1,harvest),open('intmine.pkl','wb'))

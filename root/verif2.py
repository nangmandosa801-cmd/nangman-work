import json,re,subprocess,urllib.parse,pickle
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
def ac(q):
    u='https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
    try:
        o=subprocess.run(['curl','-s','-A',UA,'--max-time','10',u],capture_output=True).stdout.decode('utf-8','replace')
        return q,[i[0] for i in json.loads(o).get('items',[[]])[0]]
    except Exception: return q,None
bad=['갈매동 상가','강남 아파트 30억 대신 경기도 여러 채','계약갱신청구권 낀 전세','광역시설 설치 비용',
'구리 아파트 수익률','구리시 개발','남양주 전세 갱신','도시개발 조건부 인가','시흥동 지식산업센터',
'아파트 평형별 가격','여주 산북면 토지','제1종전용주거지역 땅값','토지 도로 폭','하남 교산 토지',
'하남 초일동 그린벨트','화성 새솔동 땅값']
pref=set()
for h in bad:
    w=h.split()
    for i in range(len(w)-1,0,-1): pref.add(' '.join(w[:i]))
extra=['계약갱신청구권','광역시설','조건부 인가','토지 도로','하남 초일동','초일동','제1종전용주거지역','아파트 평형','평형별','갈매동 1층 상가','구리 수익률']
pref.update(extra)
pref=sorted(pref)
with ThreadPoolExecutor(max_workers=10) as ex: out=dict(ex.map(ac,pref))
for h in bad:
    w=h.split(); best=None
    for i in range(len(w)-1,0,-1):
        p=' '.join(w[:i])
        if out.get(p): best=(p,len(out[p]),out[p][:4]); break
    print(f'{h}  →  앞부분 {best[0]!r}({best[1]}) {best[2]}' if best else f'{h}  →  앞부분도 전부 0')
print()
print('--- 추가 확인')
for e in extra:
    v=out.get(e); print(f'  {e}: {len(v) if v else 0}  {(v or [])[:4]}')

import urllib.request,urllib.parse,re,time,json
exec(open('nm.py').read().split('def blog')[0])
def rank(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for t in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore'); break
        except Exception: time.sleep(5); h=''
    ids=[]
    for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
        if b not in ids: ids.append(b)
    f=lambda k: ids.index(k)+1 if k in ids else 0
    return len(ids),f('hanam-curator'),f('dong_jin_kim'),f('jisandream01')
Q=['하남 토지','하남 토지 매매','하남 땅','하남 땅값','하남 부동산','하남 초이동 토지','하남 초이동','초이동 토지','하남 창우동 토지','하남 미사동 토지','하남 감북동 토지','감북동 토지','하남 광암동 토지','교산신도시 주변 토지','하남 신규택지','하남 교산신도시 개발계획','하남 집값','하남 토지가격','하남 부동산 매물','하남 상가 매매','하남 그린벨트 토지','하남 자연녹지','하남 토지 투자','광주 남종면 토지','퇴촌 토지']
res=[]
for q in Q:
    a=ac(q); time.sleep(1); r=rank(q); time.sleep(3)
    res.append((q,a[:6],r)); print(f'{q:14s} 제안{len(a):2d} 경쟁{r[0]:3d} 정성희{r[1]:3d} 낭만{r[2]:3d} 지산{r[3]:3d} | {" / ".join(a[:5])}',flush=True)
json.dump(res,open('/tmp/claude-0/hcrank.json','w'),ensure_ascii=False)

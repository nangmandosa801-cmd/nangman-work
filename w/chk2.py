import urllib.request,urllib.parse,re,time
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def get(u):
    for _ in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
        except Exception: time.sleep(3)
    return ''
for t,kw,no in [('양주 중문,평소엔 한 짝 이사할 땐 두 짝 엽니다','양주 중문','224421890640'),('창문 단열필름, 붙이기 전에 우리 집 유리부터 봅니다','창문 단열필름','224422155844'),('중문 댐퍼 고장,쾅 닫히면 핀부터 봅니다','중문 댐퍼 고장','224421877196'),('남양주 중문, 트인 면이 둘이면 ㄱ자로 갑니다','남양주 중문','224421392281')]:
    for q,lab in [(t,'제목'),(kw,'키워드')]:
        for w in ['m_blog','m_view']:
            h=get('https://m.search.naver.com/search.naver?where=%s&query='%w+urllib.parse.quote(q)); time.sleep(2)
            ids=[]
            for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
                if (b,n) not in ids: ids.append((b,n))
            hit=[i+1 for i,(b,n) in enumerate(ids) if n==no]
            print(kw,lab,w,'노출' if hit else '없음',hit[:1],len(ids),flush=True)

import urllib.request,urllib.parse,re,time
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
C=[('hanbyul_housing','한별도어'),('moonnmore','문모아중문'),('luminadoor','루미나도어'),('vivadoor1928','비바도어'),('modedoor','모드도어'),('doorthink','중문생각'),('gmdoor82','지엠도어'),('247door','247중문'),('nature_door','네이처도어'),('joadoor-','문가온'),('joeunmoon30','조은문 중문'),('withdoor79','위드도어'),('golddoor_8204','금문 중문'),('morningdoor','모닝도어'),('gdesign_door','지디자인도어'),('kdoor_0701','케이도어 중문'),('jbdr','고집코리아'),('yeindoor','예인중문'),('showmethedoor','쇼미더목공도어'),('prodoor1004','프로중문'),('highdoor','여미지중문')]
for bid,name in C:
    q=name+' 후기'
    for _ in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q),headers=UA),timeout=25).read().decode('utf-8','ignore'); break
        except Exception: time.sleep(4); h=''
    ids=[]
    for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
        if b not in ids: ids.append(b)
    # blocks containing the name
    plain=re.sub(r'<[^>]+>',' ',h)
    hits=plain.count(name.split()[0])
    others=[b for b in ids if b!=bid]
    print(f"{name:10} 이름언급{hits:3} 결과블로그{len(ids):3} 본인포함{'Y' if bid in ids else 'N'}",flush=True)
    time.sleep(2.5)

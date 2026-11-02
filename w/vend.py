import urllib.request,urllib.parse,re,time,pickle,html
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def get(u):
    for _ in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
        except Exception: time.sleep(4)
    return ''
R=['수원','용인','화성','인천','부천','김포','고양','파주','성남','안양','의정부','평택','시흥','광명','하남']
out={}
for r in R:
    h=get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(r+' 중문 시공'))
    items=re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h)
    ids=[]
    for b,n in items:
        if b not in ids: ids.append(b)
    out[r]=ids
    print(r,ids[:15],flush=True); time.sleep(2.5)
pickle.dump(out,open('vend.pkl','wb'))

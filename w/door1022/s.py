import urllib.parse,subprocess,re,json,time
qs=['강화도어 틈막이','강화도어 외풍차단','상가 유리문 외풍차단','강화유리문 바람막이 시공','자동문 모헤어 교체','자동문 외풍차단','마포 강화도어','강화도어 수리 마포','상가 출입문 외풍차단 시공','강화도어 하부 틈막이','강화도어 풍지판','자동문 수리 마포','강화도어 수리 서울','유리문 문풍지 시공','강화도어 사이 틈']
res={}
for q in qs:
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    h=subprocess.run(['curl','-s','-m','15','-A','Mozilla/5.0 (iPhone)',u],capture_output=True,text=True).stdout
    ids=[]
    for m in re.findall(r'blog\.naver\.com/([a-zA-Z0-9_-]+)',h):
        if m not in ids: ids.append(m)
    res[q]=ids[:15]; time.sleep(1.5)
json.dump(res,open('res.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
c=Counter(i for v in res.values() for i in v)
print(c.most_common(60))

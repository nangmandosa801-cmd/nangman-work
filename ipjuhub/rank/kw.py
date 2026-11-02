# 키워드별 순위: 단지 × 일거리 검색어마다 우리 네이버 글이 블로그 검색 몇 위인지
import sys,re,json,urllib.parse,time,datetime,pickle,os
sys.path.insert(0,'/home/claude/blogkit'); import seo
a,_=pickle.load(open('/home/claude/ipjuhub/data.pkl','rb'))
OURS={'champion_chart':'낭만 인테리어','dong_jin_kim':'낭만 부동산'}
WORDS=['입주','입주청소','중문','사전점검','줄눈','새집증후군','분양가','전세']
def res(q):
    s=seo._get('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q))
    us=[]
    for u in re.findall(r'https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if u not in us: us.append(u)
    return us
def short(n):
    n=re.sub(r'\(.*?\)|\+.*','',n).strip()
    return n
rows=[]
for r in a:
    if not r['_p']: continue
    nm=short(r['단지'])
    qs=set(f'{nm} {w}' for w in WORDS)
    for p in r['_p']:
        if 'blog.naver.com' in p['u']: qs.add(p['t'].split(',')[0].strip())
    mine={tuple(re.search(r'blog\.naver\.com/([A-Za-z0-9_]+)/(\d+)',p['u']).groups()):p for p in r['_p'] if 'blog.naver.com' in p['u']}
    for q in sorted(qs):
        us=res(q); time.sleep(1.0)
        hit=[(k,u) for k,u in enumerate(us,1) if u in mine]
        any_ours=[(k,u) for k,u in enumerate(us,1) if u[0] in OURS]
        best=hit[0] if hit else (any_ours[0] if any_ours else None)
        rows.append(dict(단지=r['단지'],입주=r['입주시작'],q=q,pos=best[0] if best else None,
            u=(f'https://blog.naver.com/{best[1][0]}/{best[1][1]}' if best else None),
            b=(OURS.get(best[1][0]) if best else None),n=len(us),
            mine=any(q==p['t'].split(',')[0].strip() for p in r['_p'])))
day=str(datetime.date.today())
json.dump(dict(day=day,rows=rows),open(f'kw_{day}.json','w'),ensure_ascii=False,indent=1)
print('done',len(rows),sum(1 for x in rows if x['pos']))

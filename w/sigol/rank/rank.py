#!/usr/bin/env python3
"""팜 에디터 검색 순위 점검.  python3 rank.py [블로그ID=sea69] [kw40.txt]
모바일 네이버 블로그 탭 첫 화면에 그 블로그가 몇 번째로 나오는지 센다(서로 다른 글 기준 · 없으면 null).
결과: rank_<날짜>.json + 한 줄 요약(JSON). 매달 1일 한 번."""
import sys,re,json,subprocess,urllib.parse,datetime,os
me=sys.argv[1] if len(sys.argv)>1 else 'sea69'
kwf=sys.argv[2] if len(sys.argv)>2 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'kw40.txt')
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
out=[]
for line in open(kwf,encoding='utf-8'):
    line=line.strip()
    if not line or line.startswith('#'): continue
    grp,kw=line.split('|',1)
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(kw)
    t=subprocess.run(['curl','-s','-m','20','-A',UA,u],capture_output=True,text=True).stdout
    seen=[]
    for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',t):
        if (b,n) not in seen: seen.append((b,n))
    pos=next((i+1 for i,(b,n) in enumerate(seen) if b==me),None)
    out.append({'grp':grp,'kw':kw,'pos':pos,'n':len(seen),'top5':[b for b,n in seen[:5]]})
d=datetime.date.today().isoformat()
json.dump(out,open(os.path.join(os.path.dirname(kwf),f'rank_{d}.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=0)
hit=[o for o in out if o['pos']]
print(json.dumps({'date':d,'blog':me,'kw':len(out),'first_screen':len(hit),'top5':sum(1 for o in hit if o['pos']<=5),
 'hits':[(o['kw'],o['pos']) for o in hit],'fail':[o['kw'] for o in out if o['n']==0]},ensure_ascii=False))

import subprocess,json,re,html,urllib.parse
def get(u,ref=None):
    a=['curl','-s','-m','20','-A','Mozilla/5.0']+(['-e',ref] if ref else [])+[u]
    return subprocess.run(a,capture_output=True,text=True,errors='ignore').stdout
P=[]
for bid,label in [('champion_chart','낭만 인테리어'),('dong_jin_kim','낭만 부동산 분석 플랫폼')]:
    seen=set()
    for p in range(1,30):
        s=get(f'https://blog.naver.com/PostTitleListAsync.naver?blogId={bid}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30',f'https://blog.naver.com/{bid}')
        L=re.findall(r'"logNo":"(\d+)","title":"([^"]*)"',s)
        new=[x for x in L if x[0] not in seen]
        if not new: break
        for n,t in new: seen.add(n);P.append(dict(b=label,u=f'https://blog.naver.com/{bid}/{n}',t=urllib.parse.unquote_plus(t)))
for b,label in [('nangmaninterior','낭만 인테리어 티스토리'),('talk7921','낭만 노트 티스토리')]:
    s=get(f'https://{b}.tistory.com/rss')
    for t,l in re.findall(r'<item>\s*<title>([^<]*)</title>\s*<link>([^<]*)</link>',s): P.append(dict(b=label,u=l,t=html.unescape(html.unescape(t))))
for b,label in [('nangman-ipju','낭만 부동산 입주 노트'),('nangman-budongsan','낭만 부동산 구글'),('nangmanisa','낭만 이사')]:
    s=get(f'https://{b}.blogspot.com/feeds/posts/summary?alt=json&max-results=300')
    try:
        for e in json.loads(s)['feed'].get('entry',[]):
            u=[l['href'] for l in e['link'] if l['rel']=='alternate'][0];P.append(dict(b=label,u=u,t=e['title']['$t']))
    except Exception as ex: print(b,'fail',ex)
json.dump(P,open('posts.json','w'),ensure_ascii=False)
import collections;print(len(P),collections.Counter(p['b'] for p in P))

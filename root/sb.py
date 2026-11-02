# 통합검색(모바일) 첫 화면 확인: python3 sb.py "검색어" ["검색어2" ...]
# ① 「함께 많이 찾는」 검색어(요즘 인기 표시 포함) ② 첫 화면에 나오는 글의 순서·종류(블로그/카페/지식인/웹) ③ 우리 블로그 글 위치
import subprocess,re,urllib.parse,sys,json,html,time
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
MINE={'champion_chart':'낭만 인테리어','dong_jin_kim':'낭만','jisandream01':'지산드림','give_me_travel':'낭만도사'}
def get(u,ref=None):
    c=['curl','-sS','-m','25','-A',UA]+(['-H','Referer: '+ref] if ref else [])+[u]
    for _ in range(3):
        h=subprocess.run(c,capture_output=True,text=True).stdout
        if len(h)>500: return h
        time.sleep(1.5)
    return ''
def T(x): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',html.unescape(x.encode().decode('unicode_escape') if '\\u' in x else x))).strip()
def kind(u):
    return '블로그' if 'blog.naver' in u else '카페' if 'cafe.naver' in u else '지식인' if 'kin.naver' in u else '웹'
def one(q):
    s=get('https://m.search.naver.com/search.naver?where=m&query='+urllib.parse.quote(q))
    rel=[]
    m=re.search(r'"apiURL":"(https://s\.search\.naver\.com/p/qra/[^"]+)"',s)
    if m:
        u=m.group(1).replace('\\u0026','&')
        try:
            j=json.loads(get(u,'https://m.search.naver.com/'))
            for c in j['result']['contents']: rel.append(c['query']+('('+c['badge']['text']+')' if c.get('badge') else ''))
        except Exception as e: pass
    items=[]; prev=0
    for mm in re.finditer(r'"templateId":"(ugcItem|webItem|kinItem)"',s):
        seg=s[prev:mm.start()]; prev=mm.end()
        us=re.findall(r'"(?:keepTriggerUrl|href|titleHref)":"(https?://[^"]+)"',seg)
        us=[x for x in us if re.search(r'/\d{5,}|docId=|\.(html|php)|/[a-z0-9\-]{6,}',x)] or us
        ts=re.findall(r'"title":"([^"]+)"',seg)
        if us and ts: items.append((kind(us[-1]),us[-1].replace('\\u0026','&'),T(ts[-1])))
    print('■ '+q)
    print('  함께 많이 찾는: '+(' · '.join(rel) if rel else '없음'))
    cnt={}
    for i,(k,u,t) in enumerate(items,1):
        cnt[k]=cnt.get(k,0)+1
        me=[v for b,v in MINE.items() if '/'+b+'/' in u]
        print('  %2d %-4s %s%s'%(i,k,t[:46],'  ← '+me[0] if me else ''))
    print('  종류: '+' · '.join(f'{k} {v}' for k,v in cnt.items())+' | 우리 글: '+(', '.join(f'{i}번째({v})' for i,(k,u,t) in enumerate(items,1) for b,v in MINE.items() if '/'+b+'/' in u) or '없음'))
if __name__=='__main__':
    for q in sys.argv[1:]:
        one(q); time.sleep(0.8)

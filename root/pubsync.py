# 발행 · 미발행 맞추기. 쓰는 법: python3 /home/claude/pubsync.py  (블로그 글 목록을 직접 읽어 와서 원고와 맞춤)
import subprocess,re,os,json,time,glob,urllib.parse,html,sys,datetime
from difflib import SequenceMatcher
UA='Mozilla/5.0'
BLOGS={'int':'champion_chart','nm':'dong_jin_kim','js':'jisandream01','dosa':'give_me_travel'}
NAME={'int':'낭만 인테리어','nm':'낭만 부동산 분석 플랫폼','js':'지산드림','dosa':'낭만도사'}
PRE={'int':'nangman_interior_','nm':'nangman_','js':'jisandream_','dosa':'dosa_'}
OUT='/mnt/user-data/outputs/'
def fetch(blog,maxpage=40):
    res=[]
    for p in range(1,maxpage+1):
        u=f'https://blog.naver.com/PostTitleListAsync.naver?blogId={blog}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=&countPerPage=30'
        t=''
        for _ in range(3):
            t=subprocess.run(['curl','-sS','-m','30','-A',UA,'-e',f'https://blog.naver.com/{blog}',u],capture_output=True,text=True).stdout
            if '"postList"' in t: break
            time.sleep(1.5)
        items=re.findall(r'"logNo":"(\d+)","title":"([^"]*)".*?"addDate":"([^"]*)"',t)
        if not items: break
        new=[(n,urllib.parse.unquote_plus(ti),d) for n,ti,d in items if n not in {x[0] for x in res}]
        if not new: break
        res+=new; time.sleep(0.4)
        if len(items)<30: break
    return res
def norm(t): return re.sub(r'[^0-9A-Za-z가-힣]','',html.unescape(t))
def draft_title(path):
    h=open(path,errors='ignore').read(4000)
    m=re.search(r'<!-- 제목: (.*?) -->',h)
    if m: return m.group(1).strip()
    m=re.search(r'font-size:34px[^>]*>(.*?)</p>',h,flags=re.S)
    if m: return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',m.group(1))).strip()
    return ''
def drafts(key):
    pre=PRE[key]; d={}
    for f in glob.glob(OUT+'**/'+pre+'*post*.html',recursive=True):
        b=os.path.basename(f)
        if 'jisikin' in b or '백업' in f or '/재배치' in f: continue
        if key=='nm' and b.startswith('nangman_interior_'): continue
        slug=re.sub(r'_post.*\.html$','',b[len(pre):])
        t=draft_title(f)
        if not t: continue
        mt=os.path.getmtime(f)
        if slug not in d or mt>d[slug][2]: d[slug]=(t,f,mt)
    return d
def match(dr,pub):
    P=[(n,t,norm(t)) for n,t,_ in pub]; got={}; maybe={}
    for slug,(t,f,mt) in dr.items():
        nt=norm(t); best=(0,None)
        for n,pt,np_ in P:
            if nt==np_: best=(1.0,(n,pt)); break
            r=SequenceMatcher(None,nt,np_).ratio()
            if r>best[0]: best=(r,(n,pt))
        if best[0]>=0.80: got[slug]=best[1]
        elif best[0]>=0.62 and best[1] and norm(best[1][1])[:6]==nt[:6]: maybe[slug]=(best[1],round(best[0],2))
    return got,maybe
if __name__=='__main__':
    keys=sys.argv[1:] or list(BLOGS)
    rep={}; today=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for k in keys:
        pub=fetch(BLOGS[k]); json.dump(pub,open(f'/home/claude/pub/{k}_published.json','w'),ensure_ascii=False)
        dr=drafts(k); got,maybe=match(dr,pub)
        json.dump({s:list(v) for s,v in got.items()},open(f'/home/claude/pub/{k}_auto.json','w'),ensure_ascii=False,indent=0)
        un={s:v for s,v in dr.items() if s not in got}
        rep[k]=dict(pub=pub,dr=dr,got=got,maybe=maybe,un=un)
        print(f'{NAME[k]}: 발행 {len(pub)}편 · 원고 {len(dr)}편 · 맞춘 것 {len(got)} · 헷갈 {len(maybe)} · 미발행 {len(un)}')
    json.dump({k:{'got':{s:list(v) for s,v in r['got'].items()},'maybe':{s:[list(v[0]),v[1]] for s,v in r['maybe'].items()},'un':{s:[v[0],v[1],v[2]] for s,v in r['un'].items()}} for k,r in rep.items()},open('/home/claude/pub/report.json','w'),ensure_ascii=False)

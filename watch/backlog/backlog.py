# 미발행 원고 세기 (10/15 「목표 달성 하자」 — 쓰는 양을 발행할 수 있는 양에 맞춤)
import glob,re,json,subprocess,urllib.parse,os,datetime,html
def pub(b):
    hs=set()
    for p in range(1,40):
        t=subprocess.run(['curl','-sS','-m','30','-A','Mozilla/5.0','-H','Referer: https://blog.naver.com/'+b,f'https://blog.naver.com/PostTitleListAsync.naver?blogId={b}&currentPage={p}&countPerPage=30&categoryNo=0&viewdate=&parentCategoryNo=0'],capture_output=True,text=True).stdout
        ti=[urllib.parse.unquote_plus(x) for x in re.findall(r'"title":"([^"]*)"',t)]
        new=[x for x in ti if x not in hs]
        if not new: break
        hs.update(new)
    return hs
def head(t): return re.sub(r'\s','',t.split(',')[0])
def title_of(f):
    h=open(f,encoding='utf-8',errors='ignore').read()
    m=re.search(r'font-size:3[0-9]px;font-weight:700[^"]*">(.*?)</p>',h,re.S)
    return html.unescape(re.sub(r'<[^>]+>','',m.group(1))).strip() if m else None
SRC={'champion_chart':['/mnt/user-data/outputs/int/**/nangman_interior_*_post.html'],
     'dong_jin_kim':['/mnt/user-data/outputs/nangman_new/nangman_*_post.html'],
     'jisandream01':['/mnt/user-data/outputs/jisandream/**/jisandream_*_post.html','/mnt/user-data/outputs/jisandream_*_post.html']}
CAP=json.load(open('/home/claude/watch/backlog/cap.json'))
out={'made':datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
for b,pats in SRC.items():
    P={head(t) for t in pub(b)}
    files=[f for p in pats for f in glob.glob(p,recursive=True) if 'before' not in f and '_v' not in os.path.basename(f)]
    seen={}; 
    for f in files:
        t=title_of(f)
        if not t: continue
        h=head(t)
        if h in P: continue
        seen.setdefault(h,(t,f,os.path.getmtime(f)))
    items=sorted(seen.values(),key=lambda x:-x[2])
    if b=='champion_chart':  # 10/19 08:10 사용자 「팔아야 하는데」→「응」: 상품 말이 제목 앞머리에 있는 글 먼저
        SELL=CAP.get('sell_words',[])
        items=sorted(items,key=lambda x:0 if any(w in x[0].split(',')[0] for w in SELL) else 1)
    out[b]={'unpublished':len(items),'cap':CAP[b]['backlog_max'],'over':len(items)>CAP[b]['backlog_max'],'list':[[t,f] for t,f,_ in items],'sell_first':b=='champion_chart'}
json.dump(out,open('/home/claude/watch/backlog/backlog.json','w'),ensure_ascii=False,indent=1)
for b in SRC: print(b,out[b]['unpublished'],'한도',out[b]['cap'],'넘음' if out[b]['over'] else '')

# 중복 점검: 새 글을 쓰기 전에 돌린다.  python3 dupcheck.py int "중문 틈새 막이, ..."   (제목 없이 돌리면 지금 원고끼리 겹치는 것을 보여 줌)
import json,re,sys,glob,os
from difflib import SequenceMatcher as SM
KEY=sys.argv[1] if len(sys.argv)>1 else 'int'
rep=json.load(open('/home/claude/pub/report.json'))[KEY]
pub=json.load(open(f'/home/claude/pub/{KEY}_published.json'))
P=[(str(x[0]) if isinstance(x,(list,tuple)) else str(x.get('logNo')), x[1] if isinstance(x,(list,tuple)) else x.get('title')) for x in (pub if isinstance(pub,list) else pub.get('posts',[]))]
U=[(k,v[0]) for k,v in rep['un'].items()]
def head(t): return re.split(r'[,，]',t)[0].strip()
def norm(t): return re.sub(r'[\s·,.\-]','',t)
STOP={'중문','현관','아파트','설치','시공','입주','가격','비용','했습니다','달았습니다','입니다','먼저','봅니다','우리','현관에'}
def toks(t): return {w for w in re.findall(r'[가-힣A-Za-z0-9]{2,}',t) if w not in STOP}
def score(a,b):
    ha,hb=norm(head(a)),norm(head(b))
    s=SM(None,ha,hb).ratio()
    inc=1.0 if (ha in hb or hb in ha) and min(len(ha),len(hb))>=4 else 0
    ta,tb=toks(a),toks(b); j=len(ta&tb)/max(1,min(len(ta),len(tb)))
    return max(s,inc),j
ALL=[('발행 '+n,t) for n,t in P]+[('미발행 '+k,t) for k,t in U]
if len(sys.argv)>2 and sys.argv[2]=='--sent':
    pass
elif len(sys.argv)>2:
    c=sys.argv[2]; out=[]
    for tag,t in ALL:
        h,j=score(c,t)
        if h>=0.6 or j>=0.5: out.append((max(h,j),tag,t))
    print('후보:',c)
    for s,tag,t in sorted(out,reverse=True)[:12]: print(f'  {s:.2f} | {tag} | {t[:70]}')
    if not out: print('  겹치는 글 없음')
else:
    seen=[]
    for i in range(len(ALL)):
        for k in range(i+1,len(ALL)):
            h,j=score(ALL[i][1],ALL[k][1])
            if h>=0.72 or j>=0.6: seen.append((max(h,j),ALL[i],ALL[k]))
    for s,a,b in sorted(seen,reverse=True,key=lambda x:x[0]): print(f'{s:.2f} | {a[0]} | {a[1][:46]}\n      | {b[0]} | {b[1][:46]}')
    print('겹치는 쌍',len(seen))
# 이미 쓴 업체 사례 번호
used={}
for f in glob.glob('/home/claude/int/**/*.py',recursive=True):
    s=open(f,errors='ignore').read()
    for n in set(re.findall(r"22[34]\d{9}",s)):
        if n not in {p[0] for p in P}: used.setdefault(n,set()).add(os.path.basename(f))
json.dump({k:sorted(v) for k,v in used.items()},open('/home/claude/pub/used_cases.json','w'),ensure_ascii=False)
if len(sys.argv)<=2: print('쓴 업체 사례 번호',len(used),'→ pub/used_cases.json')

# 문장 겹침 점검:  python3 dupcheck.py int --sent <post.html>   → 다른 원고와 똑같은 문장 수 (3문장 넘으면 고친다)
if len(sys.argv)>3 and sys.argv[2]=='--sent':
    def sents(p):
        h=open(p).read().split('같이 보면 좋은 글')[0].split('함께 보면 좋은 글')[0]   # 낭만 글은 「함께 보면 좋은 글」 — 꼬리 링크 줄은 세지 않는다
        t=re.sub(r'<br\s*/?>|</p>|</td>|</tr>','\n',h); t=re.sub('<[^>]+>','',t); out=set()
        for l in t.split('\n'):
            for x in re.split(r'(?<=[다요]\.)\s+',l.strip()):
                x=re.sub(r'\s+',' ',x).strip()
                if len(x)>=18 and '.png' not in x and '.jpg' not in x: out.add(x)
        return out
    me=sents(sys.argv[3]); res=[]
    cand=[v[1] for v in rep['un'].values()]+glob.glob('/mnt/user-data/outputs/int/*/nangman_interior_*_post.html')+glob.glob('/mnt/user-data/outputs/int/nangman_interior_*_post.html')
    for q in sorted(set(cand)):
        if os.path.abspath(q)==os.path.abspath(sys.argv[3]) or not os.path.exists(q): continue
        c=me&sents(q)
        if len(c)>3: res.append((len(c),os.path.basename(q)))
    print('문장 겹침 점검:',os.path.basename(sys.argv[3]))
    for n,q in sorted(res,reverse=True)[:10]: print(f'  {n}문장 같음 | {q}')
    if not res: print('  3문장 넘게 같은 원고 없음')

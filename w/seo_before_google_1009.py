# -*- coding: utf-8 -*-
# SEO 자동완성 점검 (2026.10.5 02:36 사용자: 「SEO 자동완성 최적화 무조건 반영해 앞으로」)
# 글을 만들 때마다 돈다. 낭만(nmbuild.build) · 지산드림(jpost.build)은 저절로, 다른 글은  python3 /home/claude/blogkit/seo.py <post.html>
# 보는 곳 여섯: ① 제목 앞머리 ② 리드 ③ 소제목 ④ 본문 ⑤ 태그 ⑥ 그림 설명
# 자료: 네이버 자동완성(ac · 막히지 않음) + 통합검색 첫 화면 「함께 많이 찾는」(하루에 검색어마다 한 번만 받음)
import re, os, sys, json, html as _h, subprocess, urllib.parse, time, datetime
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
C='/home/claude/seo_cache/'; os.makedirs(C,exist_ok=True)
DAY=(datetime.datetime.utcnow()+datetime.timedelta(hours=9)).strftime('%Y%m%d')
MINE={'champion_chart':'낭만 인테리어','dong_jin_kim':'낭만','jisandream01':'지산드림','give_me_travel':'낭만도사'}
def _jl(p):
    try: return json.load(open(p,encoding='utf-8'))
    except Exception: return {}
def _jd(o,p):
    # 여러 작업이 같이 돌아도 저장한 것이 사라지지 않게: 다시 읽어 합치고, 임시 파일에 쓴 뒤 바꿔 넣는다
    cur=_jl(p); cur.update(o); t=p+f'.{os.getpid()}.tmp'
    json.dump(cur,open(t,'w',encoding='utf-8'),ensure_ascii=False,indent=0); os.replace(t,p)
def _ac(q):
    u='https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
    try:
        o=subprocess.run(['curl','-s','-A',UA,'--max-time','8',u],capture_output=True).stdout.decode('utf-8','replace')
        return [i[0] for i in json.loads(o).get('items',[[]])[0]]
    except Exception: return None
def ac_many(qs):
    p=C+f'ac_{DAY}.json'; A=_jl(p); need=[q for q in dict.fromkeys(qs) if q and q not in A]
    if need:
        with ThreadPoolExecutor(8) as ex:
            for q,r in zip(need,ex.map(_ac,need)):
                if r is not None: A[q]=r
        _jd(A,p)
    return {q:A.get(q) for q in qs}
def _get(u,ref=None):
    c=['curl','-sS','-m','25','-A',UA]+(['-H','Referer: '+ref] if ref else [])+[u]
    for _ in range(3):
        s=subprocess.run(c,capture_output=True,text=True).stdout
        if len(s)>500: return s
        time.sleep(1.5)
    return ''
def sb(q):
    """통합검색 첫 화면: 함께 많이 찾는 말 · 글 종류 · 우리 글 위치 (하루 한 번)"""
    p=C+f'sb_{DAY}.json'; S=_jl(p)
    if q in S: return S[q]
    s=_get('https://m.search.naver.com/search.naver?where=m&query='+urllib.parse.quote(q))
    if not s or 'templateId' not in s: return None   # 403 등으로 막힘
    rel=[]; m=re.search(r'"apiURL":"(https://s\.search\.naver\.com/p/qra/[^"]+)"',s)
    if m:
        try:
            j=json.loads(_get(m.group(1).replace('\\u0026','&'),'https://m.search.naver.com/'))
            rel=[c['query'] for c in j['result']['contents']]
        except Exception: pass
    kinds={}; mine=[]; prev=0; i=0
    for mm in re.finditer(r'"templateId":"(ugcItem|webItem|kinItem)"',s):
        seg=s[prev:mm.start()]; prev=mm.end()
        us=re.findall(r'"(?:keepTriggerUrl|href|titleHref)":"(https?://[^"]+)"',seg)
        if not us: continue
        i+=1; u=us[-1]
        k='블로그' if 'blog.naver' in u else '카페' if 'cafe.naver' in u else '지식인' if 'kin.naver' in u else '웹'
        kinds[k]=kinds.get(k,0)+1
        for b,v in MINE.items():
            if '/'+b+'/' in u: mine.append(f'{i}번째({v})')
    if not rel and not kinds: return None   # 막혔거나 못 읽은 것 — 저장하지 않는다
    S[q]=dict(rel=rel,kinds=kinds,mine=mine); _jd(S,p); return S[q]
def _t(x): return re.sub(r'\s+',' ',_h.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
def _n(x): return re.sub(r'[\s·,]','',x)
def parts(h):
    """글 HTML에서 제목 · 소제목 · 본문 · 태그 · 그림 설명을 꺼낸다"""
    tm=re.search(r'<p style="font-size:3[0-9]px;font-weight:700[^"]*">(.*?)</p>',h,flags=re.S)
    title=_t(tm.group(1)) if tm else ''
    cut=min([i for i in (h.find('함께 보면 좋은 글'),h.find('같이 보면 좋은 글')) if i>0] or [len(h)])
    body=h[(tm.end() if tm else 0):cut]
    heads=[_t(x) for x in re.findall(r'<p style="font-size:2[4-9]px;font-weight:700[^"]*">(.*?)</p>',body,flags=re.S)]
    caps=[_t(x) for x in re.findall(r'border:1px dashed[^>]*>\s*<span[^>]*>(.*?)</span>',h,flags=re.S)]
    caps=[c for c in caps if '_banner.png' not in c and '_contact_' not in c]   # 안내 그림 · 연락처 그림은 글마다 같은 그림이라 검색어를 보지 않는다
    tg=h[h.rfind('>태그<'):] if '>태그<' in h else ''
    if not tg:   # 낭만 인테리어 글: 「태그」 머리 없이 맨 끝 문단에 #태그가 한 줄로 있다
        ps=[x for x in re.findall(r'<p[^>]*>(.*?)</p>',h,flags=re.S) if len(re.findall(r'#[^\s#<]+',_t(x)))>=3]
        tg=ps[-1] if ps else ''
    tags=re.findall(r'#([^\s#<]+)',_t(tg))
    return title,heads,_t(body),tags,caps
def _prefixes(x):
    w=x.split(); return [' '.join(w[:n]) for n in range(len(w),0,-1)]
def check(h,main=None,keys=(),slug='',quiet=False):
    """h: 글 HTML. main: 글의 으뜸 검색어(안 주면 keys[0], 그것도 없으면 제목 앞머리에서 자동완성에 뜨는 가장 긴 앞부분).
    빠진 것이 있으면 ✘ 줄을 낸다. dict를 돌려준다."""
    if os.environ.get('SEO')=='0': return {}
    title,heads,body,tags,caps=parts(h)
    front=title.split(',')[0].strip()
    hf=[re.sub(r'^(?:[①-⑳]\s*|\d+[.)]\s+)','',x).split(',')[0].strip() for x in heads]   # 「1. 」 · 「①」 같은 번호만 뗀다 (「3연동」의 3은 떼지 않는다)
    qs=[]
    for x in [front]+hf+list(keys): qs+=_prefixes(x)
    A=ac_many(list(dict.fromkeys(qs+[q.replace(' ','') for q in qs[:1]])))
    def inac(q):
        r=A.get(q) or []
        return any(_n(x)==_n(q) or _n(x).startswith(_n(q)) for x in r)
    if not main:
        main=keys[0] if keys else next((q for q in _prefixes(front) if inac(q) and len(_n(q))>=3),front)
    A.update(ac_many([main,main.replace(' ','')]))
    S=sb(main) or dict(rel=[],kinds={},mine=[])
    A.update(ac_many(_prefixes(main)))
    core=next((q for q in reversed(_prefixes(main)) if len(q.split())>=2 and inac(q)),main)   # 리드 · 그림 설명에 꼭 있어야 하는 말
    acm=list(dict.fromkeys((A.get(main) or [])+(A.get(main.replace(' ','')) or [])))
    rel=[re.sub(r'\(.*?\)$','',r) for r in S['rel']]
    pool=[_n(x) for x in acm+rel]
    def live(q): return inac(q) or _n(q) in pool
    def livepart(x):   # 앞에서부터 가장 긴, 자동완성에 뜨는 말
        return next((q for q in _prefixes(x) if live(q) and len(_n(q))>=3),None)
    nb=_n(body); nt=_n(' '.join(tags)); out=[]; bad=0
    def has(q,where): return _n(q) in where
    # ① 제목
    lp=livepart(front); ok=bool(lp); bad+=not ok
    out.append(('✔' if ok else '✘')+f' ① 제목 앞머리 「{front}」 '+(f'→ 자동완성 「{lp}」' if ok else '자동완성에 없습니다 · 뜨는 말: '+' · '.join(acm[:6])))
    # ② 리드
    ok=has(core,_n(body[:500])); bad+=not ok
    out.append(('✔' if ok else '✘')+f' ② 리드에 「{core}」 '+('있음' if ok else '없음'))
    # ③ 소제목
    hp=[(f,livepart(f)) for f in hf]; dead=[f for f,l in hp if not l]; bad+=bool(dead)
    out.append(('✔' if not dead else '✘')+f' ③ 소제목 {len(hf)}개 '+('· '+' / '.join(l for f,l in hp) if not dead else '자동완성에 없는 앞머리: '+' / '.join(dead)))
    # ④ 본문
    cand=list(dict.fromkeys(acm+rel)); miss=[q for q in cand if not has(q,nb)]
    out.append(f'· ④ 본문에 든 말 {len(cand)-len(miss)}/{len(cand)} · 빠진 말: '+(' · '.join(miss) if miss else '없음'))
    # ⑤ 태그
    ok=has(main,nt); tmiss=[q for q in cand if not has(q,nt)]; bad+=not ok
    out.append(('✔' if ok else '✘')+f' ⑤ 태그 {len(tags)}개 · 「{main}」 '+('있음' if ok else '없음')+' · 태그에 없는 말: '+(' · '.join(tmiss[:10]) if tmiss else '없음'))
    # ⑥ 그림 설명
    if caps:
        cm=[c.split('—')[-1].strip()[:20] for c in caps if not has(core,_n(c))]; bad+=bool(cm)
        out.append(('✔' if not cm else '✘')+f' ⑥ 그림 설명 {len(caps)}개 '+('모두 검색어가 들어 있음' if not cm else '검색어가 없는 것: '+' / '.join(cm)))
    else: out.append('· ⑥ 그림 넣을 곳 없음')
    head=f'SEO [{slug}] 「{main}」 자동완성 {len(acm)}개 · 함께 많이 찾는 {len(rel)}개 · 첫 화면 '+(' · '.join(f'{k} {v}' for k,v in S['kinds'].items()) or '못 받음')+' · 우리 글 '+(', '.join(S['mine']) or '없음')
    if not quiet:
        print(head)
        for o in out: print('   '+o)
        if bad: print(f'   ▶ ✘ {bad}곳 — 고친 뒤에 건넵니다')
    r=dict(slug=slug,main=main,day=DAY,ac=acm,rel=rel,kinds=S['kinds'],mine=S['mine'],bad=bad,lines=out)
    if slug:
        L=_jl(C+'log.json'); L[slug]=r; _jd(L,C+'log.json')
    return r
if __name__=='__main__':
    for f in sys.argv[1:]:
        check(open(f,encoding='utf-8').read(),slug=os.path.basename(f).replace('_post.html',''))

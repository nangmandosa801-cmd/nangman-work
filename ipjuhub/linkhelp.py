#!/usr/bin/env python3
"""기존 글 꼬리 링크 도우미 (11/2 사용자 「새로운 글 올라올 때마다 도우미로 알려줘 · 기존 글 링크 달고 · 어떤 링크 붙여야 하는지」)
새 글 하나 → 같은 블로그의 관련 기존 글 최대 5편(검색 상위 글 먼저) → 기존 글마다 「수정 열기」 + 「새 글 링크 복사」.
사용: python3 linkhelp.py <logNo> [<logNo> ...]   (인자 없으면 posts.json에서 아직 처리 안 한 최신 인테리어 글)
출력: /home/claude/ipjuhub/linkhelp/index.html (같은 아티팩트에 다시 게시) · 상태 linkhelp_state.json (최근 12편)"""
import json,re,sys,os,html,datetime
D='/home/claude/ipjuhub'; ST=f'{D}/linkhelp_state.json'; OUT=f'{D}/linkhelp/index.html'
P=json.load(open(f'{D}/posts.json'))
BLOG={'낭만 인테리어':'champion_chart','낭만 부동산 분석 플랫폼':'dong_jin_kim'}
CAT=['중문','무타공','3연동','원슬라이딩','입주청소','이사청소','새집증후군','줄눈','탄성코트','누수','누수탐지','결로','단열','곰팡이','샷시','코킹','보일러','도어락','타일','방수','사전점검','입주','전세','분양가','하자','베이크아웃','철거','이사']
STOP=set('그리고 하면 합니다 있습니다 먼저 다음 같이 이렇게 부터 까지 에서 으로 입니다 하는 아파트 가격 비용 방법 이유 정리 후기 시공 업체'.split())
def toks(t):
    w=re.findall(r'[가-힣A-Za-z0-9]{2,}',t)
    return set(x for x in w if x not in STOP)
def head(t): return re.sub(r'\s+','',t.split(',')[0])
def ranked():
    try:
        f=sorted([x for x in os.listdir(f'{D}/rank') if x.startswith('kw_') and x.endswith('.json')])[-1]
        R=json.load(open(f'{D}/rank/{f}'))['rows']
        best={}
        for r in R:
            if r.get('u') and r.get('pos'): best[r['u']]=min(best.get(r['u'],99),r['pos'])
        return best
    except Exception: return {}
RK=ranked()
M=json.load(open('/home/claude/watch/ipju_master.json'))['단지목록']
def _n(t): return re.sub(r'[^가-힣A-Za-z0-9]','',re.sub(r'\(.*?\)','',t)).lower()
MK=[(_n(r['단지']),r.get('지역') or '') for r in M if r.get('단지')]
AREA='서울 인천 경기 충북 충남 전북 전남 경북 경남 강원 부산 대구 대전 광주 울산 세종 청주 천안 아산 전주 군산 창원 김해 포항 평택 화성 동탄 수원 용인 성남 하남 남양주 구리 고양 일산 파주 운정 김포 검단 청라 송도 부천 안산 시흥 의왕 오산 이천 의정부 양주 송파 강동 강남 서초 동작 성동 마포 은평 노원 계양 미추홀 부평 지제 고덕 브레인시티 화양 진위 영통 광교 위례 미사 감일 교산 세교 다산'.split()
def region(t):
    s=set(a for a in AREA if a in t); h=_n(t.split(',')[0])
    for L in (8,6,5):
        k=h[:L]
        if len(k)<4: break
        hit=[reg for full,reg in MK if k in full]
        if hit: s|=set(a for a in AREA if a in hit[0]); break
    return s
def cands(new):
    blog=new['u'].split('/')[3]; nt=toks(new['t']); nh=head(new['t']); nr=region(new['t']); out=[]
    for p in P:
        if p['u']==new['u'] or f'/{blog}/' not in p['u']: continue
        pt=toks(p['t']); s=0
        if head(p['t'])==nh or _n(p['t'].split(',')[0])[:6]==_n(new['t'].split(',')[0])[:6]: s+=10
        rg=len(nr&region(p['t'])); s+=5*min(rg,1)
        cat=[w for w in nt&pt if w in CAT]; s+=3*len(cat)+len((nt&pt)-set(cat))
        pos=RK.get(p['u'])
        if pos and s>=4: s+=2 if pos<=3 else 1
        if s>=5: out.append((s,pos,p))
    out.sort(key=lambda x:(-x[0],x[1] or 99)); return out[:5]
def logno(u): return u.rstrip('/').split('/')[-1]
def main(args):
    st=json.load(open(ST)) if os.path.exists(ST) else {'done':[],'items':[]}
    if not args:
        args=[logno(p['u']) for p in P if '/champion_chart/' in p['u'] and logno(p['u']) not in st['done']][:1]
    for n in args:
        new=next((p for p in P if logno(p['u'])==n),None)
        if not new: print('posts.json에 없음',n); continue
        st['items']=[i for i in st['items'] if i['n']!=n]
        st['items'].insert(0,dict(n=n,t=new['t'],u=new['u'],at=datetime.datetime.now().strftime('%m/%d %H:%M'),
            rows=[dict(t=p['t'],u=p['u'],pos=pos) for s,pos,p in cands(new)]))
        if n not in st['done']: st['done'].append(n)
        print(n,new['t'][:40],'→',len(st['items'][0]['rows']),'편')
    st['items']=st['items'][:12]; json.dump(st,open(ST,'w'),ensure_ascii=False,indent=1); render(st)
def render(st):
    os.makedirs(os.path.dirname(OUT),exist_ok=True); E=html.escape
    sec=[]
    for i in st['items']:
        blog=i['u'].split('/')[3]
        rows=''.join(f'''<li class="row" data-k="{i['n']}-{logno(r['u'])}"><label class="chk"><input type="checkbox"></label>
<div class="rt"><a href="{E(r['u'])}" target="_blank" rel="noopener">{E(r['t'])}</a>{f'<span class="pos">검색 {r["pos"]}위</span>' if r.get('pos') else ''}</div>
<div class="act"><a class="btn ghost" href="https://blog.naver.com/PostUpdateForm.naver?blogId={blog}&logNo={logno(r['u'])}" target="_blank" rel="noopener">수정 열기</a>
<button class="btn" data-t="{E(i['t'])}" data-u="{E(i['u'])}">새 글 링크 복사</button></div></li>''' for r in i['rows'])
        sec.append(f'''<section class="card"><div class="when">{E(i['at'])} 새 글</div><h2><a href="{E(i['u'])}" target="_blank" rel="noopener">{E(i['t'])}</a></h2>
<div class="paste"><span>붙일 줄</span><code>{E(i['t'])}</code></div>
<ol>{rows or '<li class="none">같이 묶을 기존 글이 없습니다</li>'}</ol></section>''')
    page=f'''<title>꼬리 링크 도우미</title><meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{{--bg:#f5f6f8;--card:#fff;--fg:#1c2430;--mut:#687384;--line:#e2e6ec;--acc:#2f5d8a;--accb:#e8eff7;--ok:#1f8a5b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#12161c;--card:#1a2028;--fg:#e6eaf0;--mut:#98a3b1;--line:#2a323d;--acc:#7fb0e0;--accb:#1e2b3a;--ok:#5fd39d;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#12161c;--card:#1a2028;--fg:#e6eaf0;--mut:#98a3b1;--line:#2a323d;--acc:#7fb0e0;--accb:#1e2b3a;--ok:#5fd39d;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.6 "Noto Sans KR",system-ui,sans-serif}}
.w{{max-width:860px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1{{font-size:22px;margin:0 0 4px}}.sub{{color:var(--mut);font-size:14px;margin:0 0 16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:16px}}
.when{{color:var(--mut);font-size:13px}}h2{{font-size:17px;margin:4px 0 10px;text-wrap:balance}}h2 a{{color:var(--fg)}}
.paste{{display:flex;gap:8px;align-items:baseline;background:var(--accb);border-radius:8px;padding:8px 10px;font-size:14px;margin-bottom:10px;min-width:0}}
.paste span{{color:var(--acc);font-weight:700;white-space:nowrap}}.paste code{{font-family:inherit;overflow-wrap:anywhere}}
ol{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}}
.row{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;border-top:1px solid var(--line);padding-top:8px}}
.rt{{flex:1 1 260px;min-width:0;font-size:15px}}.rt a{{color:var(--fg)}}.pos{{margin-left:6px;font-size:12px;color:var(--ok);font-weight:700}}
.act{{display:flex;gap:6px}}.btn{{font:inherit;font-size:14px;border:1px solid var(--acc);background:var(--acc);color:var(--card);border-radius:8px;padding:6px 10px;cursor:pointer;text-decoration:none}}
.btn.ghost{{background:transparent;color:var(--acc)}}.row.done .rt{{opacity:.45;text-decoration:line-through}}
.chk input{{width:18px;height:18px}}.none{{color:var(--mut);font-size:14px}}
</style>
<div class="w"><h1>꼬리 링크 도우미</h1>
<p class="sub">새 글이 올라올 때마다 위에 쌓입니다. 기존 글 「수정 열기」 → 맨 아래 「같이 보면 좋은 글」에 「새 글 링크 복사」로 붙여 넣기 → 저장 → 체크.</p>
{''.join(sec)}</div>
<script>
document.querySelectorAll('.btn[data-u]').forEach(b=>b.addEventListener('click',()=>{{
 const t=b.dataset.t,u=b.dataset.u,h='<a href="'+u+'">'+t.replace(/</g,'&lt;')+'</a>';
 const done=()=>{{const o=b.textContent;b.textContent='복사됨';setTimeout(()=>b.textContent=o,1500)}};
 try{{navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob([t+' '+u],{{type:'text/plain'}})}})]).then(done).catch(()=>navigator.clipboard.writeText(t+' '+u).then(done).catch(()=>{{b.textContent='길게 눌러 복사'}}))}}
 catch(e){{navigator.clipboard.writeText(t+' '+u).then(done).catch(()=>{{b.textContent='길게 눌러 복사'}})}}
}}));
document.querySelectorAll('.row').forEach(r=>{{const c=r.querySelector('input');const k='lh-'+r.dataset.k;
 try{{if(localStorage.getItem(k)){{c.checked=true;r.classList.add('done')}}}}catch(e){{}}
 c.addEventListener('change',()=>{{r.classList.toggle('done',c.checked);try{{c.checked?localStorage.setItem(k,1):localStorage.removeItem(k)}}catch(e){{}}}})}});
</script>'''
    open(OUT,'w').write(page)
if __name__=='__main__': main(sys.argv[1:])

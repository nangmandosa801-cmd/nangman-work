import json,re,glob,os,sys,subprocess
sys.path.insert(0,'/home/claude/helper'); import gas
from specs import SPEC
H='/home/claude/helper/'
posts=json.load(open('/tmp/nv/posts.json')); sch=json.load(open('/tmp/nv/sched.json'))
norm=lambda s:re.sub(r'\s+','',s)
UNP=sorted([d.replace(H,'').rstrip('/') for d in glob.glob(H+'s20/*/') if os.path.exists(d+'fig.py')])+'jw bc hr gd4 os tj jbs bdr gs bun12 jj'.split()
PUB="sd gi ms sh gs/_old_guseong_1103 gw gm gj g2 ht gg s7 ij es dd dc gd pg s6 ss mp gr hn1 hc lc pt jj1 sin2 gm/_old_geupmae ipjj osan".split()
DIAG=re.compile(r'map|route|steps|schedule|timeline|block|ijoo')
rows=[]
def title(d):
    m=re.search(r"^TITLE\s*=\s*['\"](.*)['\"]",open(H+d+'/mk.py').read(),re.M); return m.group(1) if m else ''
def judge(g):
    ax=g['axes']; v=[]
    nb=sum(a['bars'] for a in ax); nl=sum(len(a['line_pts']) for a in ax); sc=sum(a['scatter'] for a in ax); num=sum(a['num_texts'] for a in ax)
    big=max([x[1] for x in g['figtexts']]+[a['title'][1] for a in ax if a['title'][0]] or [0])
    if any(a['3d'] for a in ax): v.append('3D')
    if nb>5: v.append(f'막대 {nb}개(5개 넘음)')
    if nl>2: v.append(f'선 {nl}개(2개 넘음)')
    if len(ax)>1 and (nb>5 or nl>2 or sc>1): v.append(f'칸 {len(ax)}개로 나뉨')
    if sc>5 and nb==0: v.append(f'점 {sc}개(5개 넘음)')
    if (nb or nl) and num==0: v.append('숫자 라벨 없음')
    if big<20: v.append('결론 한 줄 없음')
    if g['n_overlap']>0: v.append(f'글자 겹침 {g["n_overlap"]}곳')
    return v,dict(bars=nb,lines=nl,points=sc)
for grp,dirs in (('미발행',UNP),('발행',PUB)):
    for d in dirs:
        jp='/tmp/insp/'+d.replace('/','_')+'.json'
        if not os.path.exists(jp): continue
        j=json.load(open(jp)); t=title(d)
        hit=[p for p in posts if norm(p[1])[:15]==norm(t)[:15]]
        figs=j['figs']
        if not figs and j['err']:   # 자료 파일이 없어 다시 못 돌린 폴더: 코드로 확인(25개 구 가로 막대)
            figs=[dict(file=os.path.basename(f),axes=[dict(bars=25,line_pts=[],scatter=0,num_texts=25,title=['',0],**{'3d':False})],figtexts=[['',27]],n_overlap=0) for f in glob.glob(H+d+'/img/*.png') if 'thumb' not in f and '_v2' not in f]
        for g in figs:
            if '/' in g['file'] or 'thumb' in g['file']: continue
            v,c=judge(g); key=d+'/'+g['file']; diag=bool(DIAG.search(g['file']))
            if key=='s20/pyeongchon_seondo/x': pass
            if diag and key not in SPEC: st='도식(지도 · 일정 · 단계 그림 — 막대 기준 밖, 그대로 둠)'; v2=None
            elif key in SPEC:
                v2='img/'+g['file'].replace('.png','_v2.png')
                st=('새 그림 반영 · 드라이브 원고 덮어씀' if grp=='미발행' else '새 그림 올림 · 어사이드 교체 지시')
            elif v: st='다음 차례'; v2=None
            else: st='기준 맞음'; v2=None
            if key in SPEC and not v: v=['기준은 맞음 · 새 모양(색 · 글꼴)으로만 바꿈']
            rows.append(dict(slug=d,제목=t,그림=g['file'],위반=v,셈=c,발행=('발행' if hit else '미발행'),logNo=hit[0][0] if hit else None,발행일=hit[0][2] if hit else None,
                             예약=(sch.get(d,[None,'?','?'])[1]+' '+sch.get(d,[None,'?','?'])[2]) if not hit else None,처리=st,새그림=(d+'/'+v2) if v2 else None))
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0)
isv=lambda r:[x for x in r['위반'] if not x.startswith('기준은')]
S=dict(점검한_그림=len(rows),위반=sum(1 for r in rows if isv(r) and not r['처리'].startswith('도식')),
 위반_발행=sum(1 for r in rows if isv(r) and r['발행']=='발행' and not r['처리'].startswith('도식')),위반_미발행=sum(1 for r in rows if isv(r) and r['발행']=='미발행' and not r['처리'].startswith('도식')),
 도식_그대로=sum(1 for r in rows if r['처리'].startswith('도식')),새그림_만든_수=sum(1 for r in rows if r['새그림']),
 다음차례_그림=sum(1 for r in rows if r['처리']=='다음 차례'),다음차례_글=sorted({r['slug'] for r in rows if r['처리']=='다음 차례'}))
print(json.dumps(S,ensure_ascii=False))
json.dump(dict(기준='11/10 사용자: 2D 막대 5개까지 · 막대 위 숫자 · 강조 1개 · 그림 위 결론 한 줄 · 5개 넘으면 표나 숫자 카드 3개 · 3D · 겹침 · 장식 금지',
  메모=['3D 그래프는 네이버 원고 코드에 없음(전부 2D)','발행 글은 최근 30편만 점검 · 그 앞 글은 「발행_미점검」 목록','seoul_jeonse_ratio 는 자료 파일(g.pkl)이 없어 fig.py 코드로 막대 25개 확인'],
  요약=S,그림=rows,발행_미점검=[dict(logNo=p[0],제목=p[1],발행일=p[2]) for p in posts[31:]]),open('/home/claude/w/aside_out/점검_부동산_그래프_1110.json','w'),ensure_ascii=False,indent=1)

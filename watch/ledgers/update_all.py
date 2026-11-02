# 장부 일괄 갱신 — python3 update_all.py [--light]
# 1 발행 글 목록 새로 고침 → 2 백업 → 3 일정 · 통합장부 상태 맞춤 → 4 사이클 장부(새 실거래면) → 5 변경 기록
import json,os,re,shutil,subprocess,sys,datetime as dt,urllib.parse
W='/home/claude/watch'; L=W+'/ledgers'; NOW=dt.datetime.now(); T=NOW.strftime('%Y-%m-%d %H:%M')
PUB='/home/claude/proj/발행글_목록_부동산_인테리어.md'
log=[]
def fetch(blog,pages=8):
    out=[]
    for p in range(1,pages+1):
        r=subprocess.run(['curl','-s','-m','20',f'https://blog.naver.com/PostTitleListAsync.naver?blogId={blog}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30','-A','Mozilla/5.0'],capture_output=True,text=True).stdout
        got=[(m.group(1),urllib.parse.unquote_plus(m.group(2)),urllib.parse.unquote_plus(m.group(3))) for m in re.finditer(r'"logNo":"(\d+)","title":"([^"]*)".*?"addDate":"([^"]*)"',r)]
        if not got: break
        out+=got
    return out
# 1
blogs=[('낭만 부동산 분석 플랫폼','dong_jin_kim'),('낭만 인테리어','champion_chart')]
pub={}
for name,b in blogs:
    pub[b]=fetch(b)
if all(pub.values()):
    o=['# 낭만 부동산 · 낭만 인테리어 발행 글 목록 (공부 블로그 링크용)','',f'만든 때: {T} · update_all.py(장부 일괄 갱신)가 다시 만든다. 형식은 예전과 같다.','']
    for name,b in blogs:
        o+= [f'## {name} ({b}) · {len(pub[b])}편','','| 날 | 번호 | 제목 |','|---|---|---|']+[f'| {d} | {n} | {t} |' for n,t,d in pub[b]]+['']
    shutil.copy(PUB,PUB+'.bak') if os.path.exists(PUB) else None
    open(PUB,'w').write('\n'.join(o)); log.append(f'발행 글 목록: 부동산 {len(pub["dong_jin_kim"])} · 인테리어 {len(pub["champion_chart"])}')
else: log.append('발행 글 목록: 네이버 응답 없음 → 그대로 둠')
# 2 백업(최근 8개만)
reg=json.load(open(L+'/registry.json'))
bd=L+'/backup/'+NOW.strftime('%Y%m%d_%H%M'); os.makedirs(bd,exist_ok=True)
for x in reg['장부']:
    f=x['파일']
    if f.startswith('/') and os.path.isfile(f): shutil.copy(f,bd+'/'+os.path.basename(f))
bs=sorted(os.listdir(L+'/backup'))
for old in bs[:-8]: shutil.rmtree(L+'/backup/'+old,ignore_errors=True)
# 3 일정 상태 맞춤
norm=lambda s: re.sub(r'[\s·,.「」\'"]','',s or '')
title2no={norm(t):n for n,t,d in pub.get('champion_chart',[])}
MS=W+'/mix_schedule_1017c.json'; ms=json.load(open(MS)); ch=0
for r in ms:
    st=r.get('상태','') or ''
    if st.startswith('발행'): continue
    n=title2no.get(norm(r.get('제목','')))
    if n:
        r['상태']=f'발행 {n} (자동 {NOW:%m/%d} · 전: {st})' if st else f'발행 {n} (자동 {NOW:%m/%d})'; ch+=1
if ch: json.dump(ms,open(MS,'w'),ensure_ascii=False,indent=1)
log.append(f'일정: 발행으로 바뀐 칸 {ch}')
r=subprocess.run(['python3',W+'/ipju_query.py','갱신'],capture_output=True,text=True); log.append('통합장부: '+(r.stdout.strip().splitlines() or ['(출력 없음)'])[-1][:120])
# 4 사이클 장부
if '--light' not in sys.argv:
    pk='/home/claude/w/apt_all.pkl'; cj=W+'/cycle/apt_cycle.json'
    import glob
    srcs=[pk]+glob.glob('/home/claude/watch/rt/apt_*_*.csv')+glob.glob('/mnt/user-data/uploads/블로그/실거래/아파트매매_*.csv')
    if not os.path.exists(cj) or max(os.path.getmtime(s) for s in srcs)>os.path.getmtime(cj):
        subprocess.run(['python3',W+'/cycle/build_cycle.py'],capture_output=True,text=True); subprocess.run(['python3',W+'/cycle/mkdoc.py']); log.append('사이클 장부: 다시 만듦(문서 /home/claude/w/apt_cycle_doc.md → claude/아파트_사이클장부_1022.md 로 올릴 것)')
    else: log.append('사이클 장부: 새 실거래 없음')
# 5 변경 기록
with open(L+'/changelog.md','a') as f: f.write(f'\n## {T}\n'+''.join(f'- {x}\n' for x in log))
print('\n'.join(log))

# 입주 허브(/53) · 시공팀 리스트(/54) 갱신: 새 글 목록을 받아 다시 만들고, 바뀐 단지 링크를 알려 준다
import subprocess,json,hashlib,os,sys
D='/home/claude/ipjuhub'
def run(c): subprocess.run(['python3',c],cwd=D,capture_output=True)
old=set(json.dumps(p,ensure_ascii=False) for p in json.load(open(f'{D}/posts.json')))
run('fetch.py');run('partners.py');run('build.py');run('render.py');run('vend.py')
new=[p for p in json.load(open(f'{D}/posts.json')) if json.dumps(p,ensure_ascii=False) not in old]
st=json.load(open(f'{D}/state.json')) if os.path.exists(f'{D}/state.json') else {}
out={}
for k,f in (('53','body.html'),('54','vend.html')):
    h=hashlib.md5(open(f'{D}/{f}','rb').read()).hexdigest()
    out[k]=dict(changed=st.get(k)!=h,hash=h,size=os.path.getsize(f'{D}/{f}'))
print(json.dumps(dict(new_posts=[p['t'][:40] for p in new][:20],pages=out),ensure_ascii=False))
# 글 없는 단지 목록(낭만 부동산 공유용) 갱신
import pickle
a,_=pickle.load(open(f'{D}/data.pkl','rb'))
L=sorted([r for r in a if not r['_p']],key=lambda r:r['입주시작'])
up=[r for r in L if r['입주시작']>=__import__('datetime').date.today().isoformat()[:8]+'01']
txt=["# 입주 글 없는 단지 — 낭만 부동산 공유","",
"/53 · /54에서 아래 단지는 우리 글이 없어 「글 준비 중」으로 표시됨(링크 없음). 글이 발행되면 매일 21:07 자동 점검이 링크를 붙임(부동산 글 1순위, 인테리어 글 ②③④).",
"- 제목에 단지 이름을 공고 이름 그대로 넣을 것(예: 「개봉 루브루 입주」).","",f"## 이번 달 이후 입주 · 글 없는 단지 {len(up)}곳 (입주 빠른 순)",""]
txt+=[f"- {r['입주시작']} · {r['단지']} · {r['지역']} · {r['세대']}세대" for r in up]
open(f'{D}/nopost_share.md','w').write('\n'.join(txt))
print(json.dumps(dict(nopost=len(L),nopost_upcoming=len(up)),ensure_ascii=False))

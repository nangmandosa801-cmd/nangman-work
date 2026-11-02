import json,glob,html as H,os
fs=sorted(glob.glob('kw_*.json'));cur=json.load(open(fs[-1]));prev=json.load(open(fs[-2])) if len(fs)>1 else None
pm={(x['단지'],x['q']):x['pos'] for x in prev['rows']} if prev else {}
import pickle
A,_=pickle.load(open('/home/claude/ipjuhub/data.pkl','rb'));SE={r['단지']:(r['세대'] or 0) for r in A}
rows=[]
for x in cur['rows']:
    if SE.get(x['단지'],0)<600: continue
    p=x['pos'];o=pm.get((x['단지'],x['q']),'na') if prev else 'na'
    if p and p<=3: g='top';todo='시공팀 소개를 붙여 문의로 잇기'
    elif p and p<=10: g='mid';todo='꼬리 링크 · 스레드로 손님 보내기'
    elif p: g='low';todo='소제목 · 첫 문단에 검색어 다시 넣고, /53 · /54 · 다른 글에서 링크 걸기'
    elif x['mine']: g='out';todo='제목 검색어를 자동완성으로 다시 확인 → 제목 앞머리 교체'
    else: g='none';todo='우리 글 없음 → 새 글 소재'
    rows.append(dict(s=SE.get(x['단지'],0),c=x['단지'],d=x['입주'],q=x['q'],p=p,o=(None if o=='na' else o),u=x['u'],b=x['b'],g=g,t=todo,m=x['mine']))
import datetime,re as _re
M=json.load(open('/home/claude/watch/ipju_master.json'))['단지목록'];POSTS=json.load(open('/home/claude/ipjuhub/posts.json'))
def _n(t):return _re.sub(r'[^가-힣A-Za-z0-9]','',_re.sub(r'\(.*?\)','',t)).lower()
today=str(datetime.date.today());pre=[]
for r in sorted([r for r in M if r.get('입주시작')],key=lambda r:r['입주시작']):
    if r['구분']!='입주예정' or (r['세대'] or 0)<1000 or r['입주시작'][:7]<today[:7]: continue
    k=_n(r['단지']);ps=[p for p in POSTS if k in _n(p['t']) and ('blog.naver.com' in p['u'])]
    pre.append(dict(c=r['단지'],a=r['지역'],s=r['세대'],d=r['입주시작'][:7],n=len(ps),u=ps[0]['u'] if ps else None))
data=json.dumps(dict(pre=pre,day=cur['day'],prev=prev['day'] if prev else None,rows=rows),ensure_ascii=False)
tpl=open('tpl.html').read().replace('__DATA__',data)
open('index.html','w').write(tpl);print(len(rows),os.path.getsize('index.html'))

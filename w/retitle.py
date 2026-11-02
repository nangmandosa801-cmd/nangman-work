import pandas as pd, re, pickle
src=open('nm.py').read(); exec(src[:src.index('def blog')])
d=pd.read_csv('/mnt/user-data/uploads/블로그/SEO목록_전체.csv',encoding='utf-8-sig')
p=d[(d['블로그']=='낭만')&(d['상태']=='발행')].copy()
def norm(s): return re.sub(r'\s','',s.lower())
rows=[]
for _,r in p.iterrows():
    t=r['제목']; head=re.split(r'\s*[|,]\s*',t)[0]
    words=head.split()
    cands=[' '.join(words[:k]) for k in range(len(words),0,-1)]
    prop=r['제목수정안'] if isinstance(r['제목수정안'],str) else ''
    if prop:
        ph=prop.split(',')[0]; pw=ph.split(); cands=[' '.join(pw[:k]) for k in range(len(pw),0,-1)]+cands
    best=None; sugg=[]
    for c in cands:
        if len(c)<2: continue
        s=ac(c)
        if any(norm(x)==norm(c) for x in s):
            best=c; sugg=s[:5]; break
    rows.append(dict(title=t,head=head,prop=prop,kw=best,sugg=' / '.join(sugg),url=r['URL'],pipe='|' in t))
o=pd.DataFrame(rows); o.to_pickle('retitle.pkl')
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',60)
print(o[['head','kw','sugg','pipe']].to_string())

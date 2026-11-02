import json,re,pickle,collections
hits,P=pickle.load(open('raw.pkl','rb'))
CATRE={'중문':'중문|도어','입주청소':'청소|클린|크린|홈케어|케어','줄눈':'줄눈|탄성','이사':'이사|익스프레스|통운|물류|포장'}
BAD='부동산|공인중개|맛집|여행|육아|리뷰|일상|분양|대출|감성|에피소드|공간:\)|뽀작|블로그$'
phreg=collections.defaultdict(set)
for (rg,c,b) in hits:
    for p in P[b]['ph']: phreg[re.sub(r'\D','',p)].add(rg)
out=[]
for (rg,c,b),rks in hits.items():
    p=P[b]; ph=[x for x in p['ph'] if re.match(r'01[016]|0[2-6]\d|1[5-8]\d\d',re.sub(r'\D','',x)) and not re.sub(r'\D','',x).startswith('07')]
    if not ph or re.search(BAD,p['name']): continue
    if not re.search(CATRE[c],p['name']+' '+p['desc'][:120]): continue
    if p['n30']>25 or p['n30']==0: continue
    if any(len(phreg[re.sub(r'\D','',x)])>2 for x in ph): continue
    out.append(dict(region=rg,cat=c,blog=b,name=p['name'],ph=ph,n30=p['n30'],hits=len(rks),best=min(rks),score=len(rks)*10-min(rks)))
g=collections.defaultdict(list)
for x in sorted(out,key=lambda x:-x['score']): g[(x['region'],x['cat'])].append(x)
pick=[];seen=set()
R=['부산','경남','울산','대구','경북','광주','전남','전북','대전','세종','충북','충남','강원','제주']
for r in R:
  for c in ['중문','입주청소','줄눈','이사']:
    n=0
    for x in g[(r,c)]:
        if x['blog'] in seen: continue
        seen.add(x['blog']); pick.append(x); n+=1
        if n==2: break
json.dump(pick,open('pick.json','w'),ensure_ascii=False,indent=1)
print(len(pick))
for x in pick: print(x['region'],x['cat'],x['name'][:24],x['ph'][0],x['n30'])
print('missing',[(r,c) for r in R for c in ['중문','입주청소','줄눈','이사'] if not any(x['region']==r and x['cat']==c for x in pick)])

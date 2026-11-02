import pickle,re,json,collections
hits,P=pickle.load(open('scan.pkl','rb'))
BIG='통인|영구|이사방|KGB|kgb|짐싸|다방|로젠|국민트랜스|GS이사|이사몰|다이사|이사플래닛|짐닷컴|위매치|오케이로지스|OK로지스|이사연구소|공식블로그|본사|지점|점\]|점 |직영점|가맹|프랜차이즈|용달|원룸|소형|청소|1톤'
OLD={'memuoo','luckyhong3','wlsgur9098','shl6273','bully135265','yjs0721aa','tjddlf9553','yongdal_24','dragonj2580','hosahe02','hso7678','logixjys','moodzang','tkfkqk4030','brlove930','zmcxdoihana','26express','intlmoving'}
out=[]
for b,p in P.items():
    ts=p['titles']
    if not ts or len(ts)<5: continue
    mv=sum(1 for t in ts if re.search('이사|포장|이삿짐',t))
    if mv/len(ts)<0.6 or p['n30']<2: continue
    big=bool(re.search(BIG,p['name']+p['desc'][:80]))
    regs=collections.Counter(g for g,q,r in hits[b])
    out.append(dict(b=b,name=p['name'],n30=p['n30'],ph=p['ph'],nq=len(hits[b]),reg=regs.most_common(3),big=big,old=b in OLD,desc=p['desc'][:150].replace('\n',' '),t=ts[:4]))
out.sort(key=lambda x:-x['nq'])
json.dump(out,open('cand.json','w'),ensure_ascii=False,indent=0)
for o in out:
  if o['nq']>=2: print(o['nq'],o['n30'],'BIG' if o['big'] else '','OLD' if o['old'] else '',o['b'],'|',o['name'][:30],o['ph'],o['reg'],'|',o['desc'][:70],'|',' / '.join(o['t'][:2])[:110])

import pickle,re,json,sys,os
REG=['노원','도봉','은평','강서','구로','금천','송파','강동','강남','서초','마포','부천','인천','수원','영통','일산','고양','파주','하남','구리','남양주','다산','광명','안양','군포','분당','성남','용인','의정부','양주','안산','평택','동탄','화성','김포','시흥','대전','세종','청주','천안','부산','대구','가평','양평','여주','이천','포천','안성','광주','홍천','춘천','횡성','충주','강화','원주','제천','괴산','서산','당진','세종']
def pick(slug,top=9,minr=0.5):
    R,agg,INFO,pat=pickle.load(open(slug+'.pkl','rb')); out=[]
    for b,i in INFO.items():
        T=i['titles']
        if len(T)<8: continue
        ratio=sum(1 for t in T if re.search(pat,t))/len(T)
        if ratio<minr or not (2<=i['n30']<=25): continue
        rc={}
        for t in T:
            for r in REG:
                if r in t: rc[r]=rc.get(r,0)+1
        tp=sorted(rc.items(),key=lambda x:-x[1])[:4]
        mob=[p for p in i['ph'] if re.match(r'01[016]',p)]
        big=bool(re.search('본사|전국|가맹|지사|체인|플랫폼|공식|대표번호|24시',i['name']+i['desc']))
        out.append(dict(b=b,name=i['name'][:26],n30=i['n30'],ratio=round(ratio,2),nq=len(agg[b]),reg=tp,mob=mob[:1],ph=i['ph'][:2],big=big,desc=i['desc'][:64].replace('\n',' ')))
    out.sort(key=lambda x:(not x['mob'],x['big'],-x['nq'],-x['ratio']))
    json.dump(out,open(slug+'_cand.json','w'),ensure_ascii=False)
    print('=====',slug,len(out),'· 휴대전화 있는 곳',sum(1 for o in out if o['mob']))
    for o in out[:top]: print(' ',o['b'],'|',o['name'],'|30일',o['n30'],'|',o['ratio'],'|검색어',o['nq'],'|',' '.join(f'{k}{v}' for k,v in o['reg']),'|',o['mob'] or o['ph'],'|','큰곳' if o['big'] else '','|',o['desc'])
for s in sys.argv[1:]:
    if os.path.exists(s+'.pkl'): pick(s)
    else: print('없음',s)

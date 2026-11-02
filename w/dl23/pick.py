import pickle,re,collections
R,agg,INFO=pickle.load(open('dl.pkl','rb'))
KNOWN={'01020689774','01040654088','01054743021','01057862535','01034114520','01028134569','01026468309','01098834363','01021701304','01034558191','01064453443'}
pat=re.compile('도어락|도어록|번호키|열쇠|현관문|방화문|문수리|키')
REG=['송파','강동','강남','서초','강서','구로','금천','관악','양천','영등포','노원','도봉','중랑','광진','성북','은평','마포','서대문','하남','미사','남양주','구리','다산','별내','의정부','양주','일산','고양','파주','인천','부천','분당','성남','수원','용인','안양','동탄','화성','광명','김포','위례','감일','평택','시흥','안산','군포','의왕']
rows=[]
for b,i in INFO.items():
    txt=i['name']+' '+i['desc']+' '+' '.join(i['titles'])
    hits=sum(1 for t in i['titles'] if pat.search(t))
    if hits<5: continue
    ph=[re.sub(r'\D','',p) for p in i['ph']]
    known=any(p in KNOWN for p in ph)
    big=bool(re.search('24시|전국|본사|1588|1644|1577|1899|1666|공식',i['name']+i['desc']))
    rc=collections.Counter()
    for t in i['titles']:
        for r in REG:
            if r in t: rc[r]+=1
    fd=sum(1 for t in i['titles'] if re.search('현관문|방화문',t))
    rows.append((len(agg[b]),b,i['name'][:30],i['last'],i['n30'],hits,fd,ph,known,big,rc.most_common(4),i['desc'][:80]))
rows.sort(key=lambda r:-r[0])
for r in rows: print(r)
print(len(rows))

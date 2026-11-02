import pickle,re,json
R,agg,INFO=pickle.load(open('screen.pkl','rb'))
pat=re.compile('방충망|방묘창|촘촘망|미세망|방범창|모헤어|롤망|주름망')
REGS=['강남','서초','송파','강동','노원','도봉','은평','마포','강서','관악','구로','금천','영등포','성북','광진','남양주','다산','별내','하남','미사','구리','수원','영통','용인','수지','기흥','성남','분당','위례','고양','일산','파주','운정','김포','인천','송도','청라','검단','부천','시흥','안양','평촌','화성','동탄','평택','안산','의정부','양주','대전','세종','청주','부산','창원','김해','양산','경남','대구','광명','군포','오산','천안']
rows=[]
for b,v in INFO.items():
    its=v['items']
    if not its: continue
    rec=[i for i in its if i['days']<=60] or its[:20]
    ratio=sum(1 for i in its[:30] if pat.search(i['t']))/max(1,len(its[:30]))
    n30=sum(1 for i in its if i['days']<=30)
    alltxt=v['name']+' '+v['desc']+' '+' '.join(i['t'] for i in its)
    reg={}
    for r in REGS:
        c=alltxt.count(r)
        if c: reg[r]=c
    mob=sorted(set(re.sub(r'[ .]','-',p) for p in v['ph'] if p.startswith('01')))
    big=bool(re.search(r'1[5-8]\d{2}[-.]\d{4}',' '.join(v['ph'])))
    last=min((i['days'] for i in its),default=9999)
    rows.append(dict(b=b,name=re.sub(r'\s+',' ',v['name'])[:40],n30=n30,ratio=round(ratio,2),nq=len(agg.get(b,{})),best=min(agg.get(b,{9:99}).values()),reg=sorted(reg.items(),key=lambda x:-x[1])[:5],mob=mob,ph=v['ph'][:4],big=big,last=last,desc=re.sub(r'\s+',' ',v['desc'])[:150]))
rows.sort(key=lambda r:(-(r['ratio']>=0.3 and 2<=r['n30']<=30), -r['nq']))
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0)
for r in rows:
    if r['ratio']>=0.3 and r['last']<=60:
        print(r['b'],'|',r['name'],'|30d',r['n30'],'|r',r['ratio'],'|q',r['nq'],r['best'],'|',r['mob'] or r['ph'],'|',[x[0] for x in r['reg']],'|last',r['last'])

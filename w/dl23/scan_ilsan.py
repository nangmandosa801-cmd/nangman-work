exec(open('scan.py').read().split('REG=')[0])
REG=['일산','고양','일산 동구','일산 서구','파주','운정','김포','한강신도시','김포 장기동','고양 삼송','파주 야당']
P=['도어락 교체','도어락 설치','열쇠 도어락','비디오폰 교체']
QS=[r+' '+p for r in REG for p in P]
R={}
for i in range(0,len(QS),4):
    with ThreadPoolExecutor(4) as ex: R.update(dict(zip(QS[i:i+4],ex.map(ranks,QS[i:i+4]))))
    time.sleep(1.0)
agg={}
for q,d in R.items():
    for b,r in d.items(): agg.setdefault(b,{})[q]=r
B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:120]
INFO={}
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss,B[i:i+10]))))
pickle.dump((R,agg,INFO),open('ilsan.pkl','wb'))
print(len(QS),sum(1 for v in R.values() if v),len(agg),len(INFO))
for b in B:
    i=INFO[b]
    if i['last']<'2026-09-20': continue
    kw=sum(1 for t in i['titles'] if re.search('도어락|열쇠|번호키|비디오폰|인터폰',t))
    print(b,len(agg[b]),i['last'],i['n30'],kw,i['ph'],'|',i['name'][:25],'|',re.sub(r'\s+',' ',i['desc'])[:90])

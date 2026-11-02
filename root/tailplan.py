import json,re,datetime
P=json.load(open('/tmp/claude-0/pub_now.json')); Lk=json.load(open('/tmp/claude-0/links.json'))
T={no:t for no,t,d in P}
def dt(d):
    m=re.match(r'(\d{4})\. (\d+)\. (\d+)\.',d)
    return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else datetime.date(2026,9,29)
D={no:dt(d) for no,t,d in P}
C={'하남':['하남','미사','감일','교산','초이','감북','위례','망월','K-스타월드'],
'1기재건축':['분당','일산','평촌','산본','1기 신도시','선도지구'],
'정비사업':['정비사업','정비기반','재건축','토지등소유자','은마','압구정','목동'],
'서울':['서울','강남','마용성','노도강','동북권','창동','대치','임대동','목동','압구정','은마'],
'동탄화성':['동탄','화성','광교'],
'신도시택지':['3기 신도시','교산','계양','토평','창릉','왕숙','a6'],
'철도':['GTX','호선','노선','옥정'],
'공법':['개발행위','도시계획','도시군','지구단위','시가화','성장관리','개발밀도','정비기반','훼손지','지정시행자'],
'토지':['땅값','토지','그린벨트','훼손지','토지거래허가'],
'경기시세':['경기도','양주','운정','다산','용인','구리','광교'],
'세금금리':['종부세','기준금리','금 투자'],
'상업':['지식산업센터','오피스텔'],
'시험':['부동산학개론','민법','민사특별법','부동산중개사','부동산학 개론','공인중개사 부동산학개론'],
'인테리어':['인테리어']}
SKIP={'224377990326','224375585302','224397832357'}  # 허브, 인사말, 예측 글
def cl(t): return {k for k,ws in C.items() if any(w in t for w in ws)}
CL={no:cl(t) for no,t in T.items()}
def cand(a):
    out=[]
    for b in T:
        if b==a or b in SKIP or b in Lk.get(a,[]): continue
        s=len(CL[a]&CL[b])
        if s==0: continue
        if CL[a]=={'시험'} and CL[b]!={'시험'}: continue
        newer = D[b]>D[a]
        out.append((s+(1 if newer else 0)+(0.5 if D[b]>=datetime.date(2026,9,20) else 0),b))
    return [b for s,b in sorted(out,reverse=True)[:3] if s>=1.5]
plan={a:cand(a) for a in T if a not in SKIP}
hubmiss=[no for no in T if no not in Lk['224377990326'] and no not in SKIP]
json.dump({'plan':plan,'hub':hubmiss},open('/tmp/claude-0/tailplan.json','w'),ensure_ascii=False)
n=sum(1 for v in plan.values() if v); print('targets',n,'hubmiss',len(hubmiss))
for a,v in plan.items():
    if v: print(len(Lk.get(a,[])),T[a][:28],'<=',[T[b][:18] for b in v])

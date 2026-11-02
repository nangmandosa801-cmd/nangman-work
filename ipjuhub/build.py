import json,re,datetime,collections
M=json.load(open('/home/claude/watch/ipju_master.json'))['단지목록']
POSTS=json.load(open('posts.json'));PART=[p for p in json.load(open('partners.json')) if p['name']!='말끔하게']
TODAY=datetime.date(2026,11,1)
S='!important'
PROV={'서울':'서울','경기':'경기','인천':'인천','부산':'부산','대구':'대구','울산':'울산','대전':'대전','세종':'세종','충북':'충북','충남':'충남','전북':'전북','전남':'전남','경북':'경북','경남':'경남','강원':'강원','제주':'제주'}
CITY={'평택':'경기','오산':'경기','의왕':'경기','이천':'경기','용인':'경기','수원':'경기','화성':'경기','동탄':'경기','시흥':'경기','부천':'경기','성남':'경기','안성':'경기','양주':'경기','고양':'경기','일산':'경기','파주':'경기','운정':'경기','광명':'경기','구리':'경기','남양주':'경기','하남':'경기','김포':'경기','안양':'경기','평촌':'경기','의정부':'경기','군포':'경기','안산':'경기','위례':'경기','퇴계원':'경기',
 '검단':'인천','송도':'인천','계양':'인천','청라':'인천','영종':'인천','미추홀':'인천','연희':'인천',
 '김해':'경남','창원':'경남','양산':'경남','밀양':'경남','포항':'경북','경주':'경북','영주':'경북','안동':'경북','청주':'충북','천안':'충남','아산':'충남','서산':'충남','공주':'충남','보령':'충남','계룡':'충남','부여':'충남','청양':'충남',
 '전주':'전북','익산':'전북','군산':'전북','완주':'전북','여수':'전남','광양':'전남','장성':'전남','강릉':'강원','기장':'부산'}
SOUTH=['수원','용인','화성','동탄','오산','평택','안성','이천','성남','안양','군포','의왕'];WEST=['시흥','부천','안산','광명','김포'];NORTH=['의정부','양주','파주','고양','일산','남양주','구리','운정']
def cplace(reg):
    toks=set();prov=None
    for k,v in PROV.items():
        if reg.startswith(k): prov=v
    if reg.startswith('광주') and ('북구' in reg or '남구' in reg or '서구' in reg or '광산' in reg or '광주시' not in reg and '경기' not in reg): prov=prov or '광주'
    if reg.startswith('광주시'): prov='경기';toks.add('경기광주')
    for c,v in CITY.items():
        if c in reg: toks.add(c);prov=prov or v
    for w in re.split(r'[\s()·,]+',reg):
        w=re.sub(r'(시|구|군|동|읍|면)$','',w)
        if len(w)>=2: toks.add(w)
    return prov,toks
def covers(area,prov,toks):
    a=area
    if '전국' in a: return 1
    if prov in ('서울','경기','인천') and '수도권' in a: return 1
    if prov=='경기':
        if '경기 남부' in a and toks&set(SOUTH): return 2
        if '경기 서부' in a and toks&set(WEST): return 2
        if '경기 북부' in a and toks&set(NORTH): return 2
        if re.search(r'경기(?! (남부|서부|북부))',a) or '경기도' in a: return 1
    if prov in ('서울','인천','부산','대구','울산','대전','세종','충북','전남','경북','경남') and prov in a: return 1
    if prov=='광주' and ('광주 · 전남' in a or '광주광역시' in a): return 2
    if prov in ('부산','대구','울산','경북','경남') and ('경상' in a): return 1
    for t in toks:
        if t in CITY and t in a and CITY[t]==prov: return 2
        if prov=='서울' and t in SEOULD and t in a and '서울' in a: return 2
        if prov=='서울' and t in SEOULD and t in a and t in ('노원','성북','도봉','동대문','중랑','강북','양천','강서','송파','강동','마포','서대문','강남','서초'): return 2
    return 0
SEOULD=('강남','서초','송파','강동','마포','서대문','양천','강서','노원','성북','도봉','동대문','중랑','강북','동작','은평','구로','금천','관악','영등포','용산','성동','광진','종로','중구')
ORDER=['사전점검','입주청소','새집증후군','줄눈','중문','결로 · 단열','보일러','이사']
def vendors(reg):
    prov,toks=cplace(reg);out=[]
    for c in ORDER:
        L=sorted([(covers(p['area'],prov,toks),p) for p in PART if c in p['cats']],key=lambda x:-x[0])
        L=[p for s,p in L if s>0][:1]
        if L: out.append((c,L))
    return out
def norm(s): return re.sub(r'[\s\-·,()\[\]「」]','',re.sub(r'\(.*?\)','',s)).lower()
REGW=('평택','인천','부산','울산','대전','광주','이천','용인','고양','오산','성남','청주','전주','부천','서울','경기','천안','김해','창원','아산','동탄','검단')
def keys(x):
    n=x['단지'];K={norm(n)}
    w=n.split()
    if len(w)>1 and any(w[0].startswith(r) for r in REGW) and len(norm(' '.join(w[1:])))>=8: K.add(norm(' '.join(w[1:])))
    for a in x.get('별칭') or []: K.add(norm(a))
    w2=[t for t in re.sub(r'\(.*?\)|\+.*','',n).split() if not re.fullmatch(r'[0-9A-Za-z\-]+(BL|블록|단지)?',t) ]
    if len(w2)>1 and any(w2[0].startswith(r) for r in REGW): w2=w2[1:]
    if len(w2)>=2 and len(norm(' '.join(w2)))>=6: K.add(norm(' '.join(w2)))
    return [k for k in K if len(k)>=5]
def posts(x):
    K=keys(x);R=[]
    for p in POSTS:
        t=norm(p['t'])
        if p['b']=='낭만 부동산 입주 노트': continue
        if any(k in t for k in K) and p['u'] not in [r['u'] for r in R]: R.append(p)
    for p in POSTS:   # 입주 노트는 단지 이름을 줄여 쓰는 일이 많아 낱말 맞추기로 한 번 더 찾는다 (11/1 사용자 「입주 노트 각 아파트마다 링크」)
        if p['b']=='낭만 부동산 입주 노트' and p['u'] not in [r['u'] for r in R] and note_hit(x['단지'],p['t']): R.append(p)
    return R
GEN={'아파트','단지','반도체밸리','신도시'}
def _n(s): return re.sub(r'[^가-힣A-Za-z0-9]','',s).lower()
def note_hit(name,title):
    k=_n(title.split(',')[0]); name=re.sub(r'\(.*?\)|\+.*','',name)
    T=[_n(t) for t in name.split() if _n(t) and _n(t) not in GEN and not re.fullmatch(r'[0-9a-z\-]+(bl|블록|단지)?',_n(t))]
    if len(T)<2: return False
    def has(t):
        if t in k: return True
        for r in REGW:
            if t.startswith(r) and len(t)>len(r)+1 and t[len(r):] in k: return True
        return False
    hit=[t for t in T if has(t)]
    if not has(T[0]) and T[0] not in REGW: return False
    return len(hit)>=2 and sum(len(t) for t in hit)/sum(len(t) for t in T)>=0.6
def datestr(x):
    d=x['입주시작'];y,m,dd=map(int,d.split('-'))
    exact=not re.search('월만|추정',x.get('확인정도') or '')
    s=f'{m}월 {dd}일' if exact else f'{m}월 중 (날짜 공지 전)'
    if x.get('입주지정기간'): s+=f' · 입주지정 {x["입주지정기간"]}'
    if x.get('사전점검일') and '미공개' not in str(x['사전점검일']): s+=f' · 사전점검 {x["사전점검일"]}'
    return s,exact
items=[x for x in M if x['구분']=='입주예정' and x['입주시작'] and x['입주시작'][:4] in ('2026','2027')]
for x in items: x['_p']=posts(x);x['_v']=vendors(x['지역'] or '')
items.sort(key=lambda x:(x['입주시작'][:7],0 if datestr(x)[1] else 1,x['입주시작'],-(x['세대'] or 0)))
by=collections.OrderedDict()
for x in items: by.setdefault(x['입주시작'][:7],[]).append(x)
json.dump({k:[dict(n=x['단지'],p=len(x['_p']),v=len(x['_v'])) for x in v] for k,v in by.items()},open('summary.json','w'),ensure_ascii=False)
print(len(items),{k:len(v) for k,v in by.items()},sum(1 for x in items if x['_p']),'with posts')
import pickle;pickle.dump((items,by),open('data.pkl','wb'))

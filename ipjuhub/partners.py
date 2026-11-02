import json,re
d=json.load(open('nb.json'))
CAT={'중문':['중문'],'사전점검':['사전점검','하자점검'],'입주청소':['입주청소','종합청소','종합클린'],'새집증후군':['새집증후군','베이크아웃'],'줄눈':['줄눈'],'탄성코트':['탄성코트'],
 '코킹':['코킹','실리콘'],'결로 · 단열':['단열','결로'],'보일러':['보일러','온도조절기'],'필름':['필름'],'매트':['매트'],'방묘문':['방묘문'],'이사':['포장이사','보관이사'],
 '도어락':['도어락','열쇠'],'에어컨':['에어컨'],'누수':['누수','동파','배관'],'샷시':['샷시','창호'],'타일':['타일'],'방충망 · 외풍':['방충망','외풍']}
P=[]
for e in d['feed']['entry']:
    t=e['title']['$t'];u=[l['href'] for l in e['link'] if l['rel']=='alternate'][0]
    if not re.match(r'^[ㄱ-ㅎ]',t): continue
    cats=[c for c,ks in CAT.items() if any(k in t for k in ks)]
    P.append(dict(name=t.split(' · ')[0],cats=cats,area=t,u=u))
# 10/31~11/1 새 제휴 (낭만 명함 소개 글 없음 → 업체 블로그)
NEW=[('결로 · 단열','말끔하게','경상도 대구 부산 창원 울산 포항 경북 경남','febric_cleaning'),
 ('결로 · 단열','리담디자인','부산 김해 양산 창원','redamdesign'),
 ('결로 · 단열','스텔라리페어','서울 경기 인천','stellar_repair'),
 ('결로 · 단열','JU인 공간케어','서울 성남 용인 경기 광주 수원','killerno44'),
 ('결로 · 단열','홈어바웃','노원 성북 도봉 동대문 중랑 강북','younghomecare'),
 ('결로 · 단열','몰드케어','양천 강서','moldcare2945'),
 ('결로 · 단열','클린VIP','청주 충북','cleanvip'),
 ('보일러','보일러의모든것','전주 익산 군산','veteran_mj'),('보일러','진보일러','전주','jangsk1219'),
 ('보일러','대성보일러','김해 창원 양산 부산','daesungboiler_'),('보일러','광주 보일러','광주광역시 전남','mari5nette'),
 ('보일러','포항 보일러','포항 경주','0549111'),('보일러','창원 보일러','창원','rlatjdwns0210')]
for c,n,a,b in NEW: P.append(dict(name=n,cats=[c],area=a,u=f'https://blog.naver.com/{b}'))
json.dump(P,open('partners.json','w'),ensure_ascii=False,indent=0)
for p in P: print(p['cats'],p['name'],'|',p['area'][-40:])

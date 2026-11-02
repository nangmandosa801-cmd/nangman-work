import csv,math,json,re,collections
B='/home/claude/w/broker/'
FP='고보애 고희정 김화연 성경숙 송혜영 윤수경 이경숙 이재은 현은옥 김영자 김윤희 조정숙 이경미 유혜경 이원미 정화은 하성란 박영미 강은숙 김민숙 방혜경 권효정 연선숙 이은주 최말애 김점순 백선미 김민희 박선자 박윤정 유순화 이영숙 정미나 황영미'
FO='양순례 양현주 김이순 이금희 송은정 성주희 박수정 정현경 최은진 김진아 김선희 윤희정 전연주 어진희 곽숙경 고옥순 문미화 장예린 박지혜 이금숙 신성옥 윤효선 유미숙 오유진 최미애 김선미 송은영 권연희 염혜인 이미애 구선미'
def km(a,b,c,d): return math.hypot((a-c)*111,(b-d)*88)
r=list(csv.DictReader(open(B+'paju_u.csv',encoding='utf-8-sig')))
cen=(37.716,126.740)
pj=[]
for x in r:
    try: la,lo=float(x['위도']),float(x['경도'])
    except: continue
    if not x['전화번호'].strip(): continue
    if x['대표자명'].strip() not in FP.split(): continue
    x['_d']=km(la,lo,*cen)
    if x['_d']<1.3: pj.append(x)
pj.sort(key=lambda x:x['_d'])
per=collections.Counter(); sel=[]; phones=set()
for x in pj:
    k=x['소재지도로명주소'].strip(); ph=x['전화번호'].strip()
    if per[k]>=2 or ph in phones: continue
    per[k]+=1; phones.add(ph); sel.append(x)
    if len(sel)==15: break
out=[]
for i,x in enumerate(sel,1):
    out.append(dict(code=f'PJ-{i:02d}',danji='운정중앙역 제일풍경채 (파주 운정3지구 · 2026.10.2 입주 시작)',office=x['중개업소명'].strip(),ceo=x['대표자명'].strip(),addr=x['소재지도로명주소'].strip(),jibun=x['소재지지번주소'].strip(),tel=x['전화번호'].strip(),km=round(x['_d'],2)))
o=list(csv.DictReader(open(B+'osan_u.csv',encoding='utf-8-sig')))
pat=re.compile(r'가수|삼국마을로|여들동로|초평중앙로|서동|벌음동|가장동')
os_=[x for x in o if x['중개업자명'].strip() in FO.split() and pat.search(x['사무소주소']) and x['행정처분상태']=='영업중']
os_=[x for x in os_ if ',' not in x['사무소전화번호'] and not x['사무소전화번호'].startswith('1588')]
pri=lambda a: 0 if re.search(r'초평중앙로|삼국마을로|여들동로',a) else 1 if '가수' in a else 2
os_.sort(key=lambda x:(not x['사무소전화번호'].strip(), pri(x['사무소주소'])))
phones=set(); n=0
for x in os_:
    ph=x['사무소전화번호'].strip()
    if ph and ph in phones: continue
    phones.add(ph); n+=1
    out.append(dict(code=f'OS-{n:02d}',danji='오산 세교2지구 금강펜테리움 센트럴파크 (A8블록 · 2026.10 입주 시작)',office=re.sub(r'\(?0[0-9]{1,2}[.\-][0-9]{3,4}[.\-][0-9]{4}\)?','',x['사무소명']).strip(),ceo=x['중개업자명'].strip(),addr=x['사무소주소'].strip(),jibun='',tel=ph,km=None))
    if n==15: break
json.dump(out,open('list.json','w'),ensure_ascii=False,indent=1)
for x in out: print(x['code'],x['office'],'|',x['ceo'],'|',x['addr'],'|',x['tel'],x['km'])
print(len(os_))

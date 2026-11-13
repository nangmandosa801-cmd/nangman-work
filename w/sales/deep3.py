import re, subprocess, json, urllib.parse
def get(u):
    return subprocess.run(['curl','-sL','--max-time','20','-A','Mozilla/5.0','-e','https://blog.naver.com/champion_chart',u],capture_output=True,text=True).stdout
T = []
for p in range(1, 14):
    r = get(f'https://blog.naver.com/PostTitleListAsync.naver?blogId=champion_chart&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30')
    r = r.replace("\\'", "'")
    try: d = json.loads(r)
    except Exception as e:
        print('page', p, 'ERR', r[:120]); break
    L = d.get('postList', [])
    if not L: break
    for x in L: T.append((x.get('addDate',''), x.get('logNo'), urllib.parse.unquote_plus(x.get('title',''))))
    if len(L) < 30: break
print('전체 글', len(T), '| 가장 오래된', T[-1][0] if T else '')
json.dump(T, open('titles.json','w'), ensure_ascii=False)
P = r'가격|비용|견적|얼마|만원'
price = [t for t in T if re.search(P, t[2])]
diy = [t for t in T if re.search(r'셀프|방법|하는 법|고르는 법|예방|방지|뜻|차이|이유|원인|시기|언제|순서|체크|책임|보험', t[2]) and not re.search(P, t[2])]
REG = '서울|인천|수원|부산|대구|대전|울산|창원|평택|동탄|화성|하남|성남|송파|강동|구리|남양주|김포|시흥|파주|고양|일산|청주|전주|포항|광주|용인|안양|부천|의정부|노원|마포|판교|분당|검단|운정'
reg = [t for t in T if re.search(REG, t[2])]
print('가격 말이 제목에:', len(price), '| 정보 · 방법형(가격 말 없음):', len(diy), '| 지역 이름이 제목에:', len(reg))
for t in ['중문','무타공','누수','결로|곰팡이|단열','입주청소','사전점검','줄눈','코킹|실리콘','동파|해빙|보일러','도어락','샷시|창호','새집증후군|베이크아웃','매트','필름','이사|퇴실|원상복구']:
    L = [x for x in T if re.search(t, x[2])]
    print(f'  {t}: {len(L)}편 · 가격 말 {sum(1 for x in L if re.search(P, x[2]))}편')
for cell in ['부산.*중문','대전.*중문','수원.*중문','대구.*중문','평택.*중문','동탄.*중문','인천.*중문','부산.*누수','인천.*누수','성남.*누수','청주.*누수','울산.*누수','하남.*누수','대구.*(곰팡이|단열)','인천.*입주청소','수원.*입주청소','평택.*입주청소','전주.*입주청소']:
    L = [x for x in T if re.search(cell, x[2])]
    print(f'  [{cell}] {len(L)}편', '|', ' / '.join(x[2][:34] for x in L[:2]))

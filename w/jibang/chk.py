import json,urllib.parse,subprocess,re,html
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"
def get(u): return subprocess.run(["curl","-s","-m","20","-A",UA,u],capture_output=True,text=True).stdout
D=[
 dict(권역="부산·울산·경남",단지="울산다운2지구 우미린 더 시그니처",키="다운2지구 우미린 더 시그니처",지역="울산 울주군 범서읍",세대=1430,시공사="",입주="2026-11-11",지정="2026-11-11~2027-01-13",점검="",출처=["ipju_master.json","https://www.iusm.co.kr/news/articleView.html?idxno=1069318"]),
 dict(권역="부산·울산·경남",단지="에코델타시티 중흥S-클래스(16BL)",키="에코델타시티 중흥S클래스",지역="부산 강서구 강동동",세대=1067,시공사="",입주="2026-11-17",지정="",점검="",출처=["ipju_master.json","https://www.busan.com/view/busan/view.php?code=2026101909464320067"]),
 dict(권역="부산·울산·경남",단지="해링턴 마레",키="해링턴마레",지역="부산 남구 우암동",세대=2205,시공사="",입주="2026-12",지정="",점검="",출처=["ipju_master.json","https://kbthink.com/realestate/issue/hosing-261014.html"]),
 dict(권역="부산·울산·경남",단지="일광 노르웨이숲 오션포레",키="일광노르웨이숲오션포레",지역="부산 기장군 일광읍",세대=1294,시공사="유림E&C",입주="2027-03",지정="",점검="",출처=["ipju_master.json","https://listup24.com/2027%EB%85%84-%EB%B6%80%EC%82%B0-%EC%9E%85%EC%A3%BC-%EC%98%88%EC%A0%95-%EC%95%84%ED%8C%8C%ED%8A%B8-%EB%AC%BC%EB%9F%89-%EC%B4%9D%EC%A0%95%EB%A6%AC/"]),
 dict(권역="부산·울산·경남",단지="대연 디아이엘",키="대연디아이엘",지역="부산 남구 대연동",세대=4488,시공사="HDC현대산업개발 · 롯데건설",입주="2027-04",지정="",점검="",메모="임대 238세대 포함",출처=["ipju_master.json","https://listup24.com/2027%EB%85%84-%EB%B6%80%EC%82%B0-%EC%9E%85%EC%A3%BC-%EC%98%88%EC%A0%95-%EC%95%84%ED%8C%8C%ED%8A%B8-%EB%AC%BC%EB%9F%89-%EC%B4%9D%EC%A0%95%EB%A6%AC/"]),
 dict(권역="광주·전라",단지="서신 더샵 비발디",키="서신더샵비발디",지역="전북 전주시 완산구",세대=1914,시공사="",입주="2026-11-20",지정="2026-11-20~2027-01-19",점검="10/2~10/3",메모="장부 이름 「서신더샵에피트」 — 같은 단지인지 확인 필요",출처=["ipju_master.json","https://kbthink.com/realestate/issue/hosing-261014.html"]),
 dict(권역="대전·세종·충청",단지="더샵 탕정인피니티시티(1차)",키="더샵탕정인피니티시티",지역="충남 아산시 탕정면",세대=1140,시공사="",입주="2026-12",지정="",점검="",출처=["ipju_master.json","https://www.apartsearcher.ai/move-in/%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84"]),
 dict(권역="대전·세종·충청",단지="신영지웰 푸르지오 테크노폴리스 센트럴",키="신영지웰푸르지오테크노폴리스센트럴",지역="충북 청주시 흥덕구 송절동",세대=1034,시공사="",입주="2027-01",지정="",점검="",메모="주상복합",출처=["ipju_master.json","https://www.apartsearcher.ai/move-in/%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84"]),
 dict(권역="대전·세종·충청",단지="더샵 탕정인피니티시티 2차",키="더샵탕정인피니티시티2차",지역="충남 아산시 탕정면",세대=1214,시공사="",입주="2027-02",지정="",점검="",출처=["ipju_master.json"]),
 dict(권역="대전·세종·충청",단지="배방 필하우스 리버시티",키="배방필하우스리버시티",지역="충남 아산시 배방읍",세대=1083,시공사="",입주="2027-02",지정="",점검="",출처=["ipju_master.json"]),
]
def ac(q):
  u="https://ac.search.naver.com/nx/ac?q="+urllib.parse.quote(q)+"&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100"
  try: return [i[0] for i in json.loads(get(u))['items'][0]]
  except: return []
titles={}
for b in ['champion_chart','dong_jin_kim']:
  ts=[]
  for p in range(1,8):
    x=get(f"https://blog.naver.com/PostTitleListAsync.naver?blogId={b}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=&countPerPage=30")
    t=re.findall(r'"title":"(.*?)"',x); n=re.findall(r'"logNo":"(\d+)"',x)
    if not t: break
    ts+= [(no,html.unescape(urllib.parse.unquote_plus(tt))) for no,tt in zip(n,t)]
  titles[b]=ts
print({k:len(v) for k,v in titles.items()})
for r in D:
  a1=ac(r['키']); a2=ac(r['키']+' 입주청소'); a3=ac(r['키']+' 사전점검')
  r['자동완성_단지']=a1[:6]; r['자동완성_입주청소']=a2[:5]; r['자동완성_사전점검']=a3[:5]
  r['뜸']={'단지':bool(a1),'입주청소':bool(a2),'사전점검':bool(a3)}
  core=re.sub(r'[\s()·0-9a-zA-Z차]','',r['단지'])[:5]
  hits=[]
  for b,ts in titles.items():
    for no,t in ts:
      if core and core in t.replace(' ',''): hits.append(f"{b}/{no} {t[:40]}")
  r['우리글']=hits[:5]
json.dump(D,open('danji_1023.json','w'),ensure_ascii=False,indent=1)
for r in D: print(r['단지'],r['뜸'],len(r['우리글']),r['자동완성_단지'][:4],r['우리글'][:2])

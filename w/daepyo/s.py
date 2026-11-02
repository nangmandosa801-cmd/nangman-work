import urllib.parse,subprocess,re,json,time,html
dj=['힐스테이트 동작 시그니처','성동자이리버뷰','연희공원 호반써밋','래미안 레벤투스','신검단중앙역 센트레빌','은계 에피트','회천중앙역 로제비앙','화양 동문 디이스트','푸르지오 라디우스파크','e편한세상 일산 메이포레','검단아테라자이','판교테크노밸리 중흥S클래스','서광교 한라비발디','제일풍경채 검단4','오산세교 힐데스하임']
out={}
for d in dj:
    q=d+' 입주예정자협의회'
    u='https://m.search.naver.com/search.naver?where=m_cafe&query='+urllib.parse.quote(q)
    h=subprocess.run(['curl','-s','-m','15','-A','Mozilla/5.0 (iPhone)',u],capture_output=True,text=True).stdout
    cafes=[]
    for m in re.findall(r'cafe\.naver\.com/([a-zA-Z0-9_]+)',h):
        if m not in cafes and m not in ('ca-fe','cafe','MyCafeIntro'): cafes.append(m)
    names=re.findall(r'class="[^"]*(?:cafe_name|name)[^"]*"[^>]*>(.*?)<',h)
    out[d]={'cafes':cafes[:6],'names':[html.unescape(re.sub('<[^>]+>','',n)) for n in names][:6]}
    time.sleep(1.2)
json.dump(out,open('cafes.json','w'),ensure_ascii=False,indent=1)
for k,v in out.items(): print(k,'|',v['cafes'],'|',v['names'][:4])

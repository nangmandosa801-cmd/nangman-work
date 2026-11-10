import json,re,os
from bs4 import BeautifulSoup
B='/home/claude/w/ts_audit'
P=json.load(open(f'{B}/raw/parsed.json'))
def norm(t): return re.sub(r'[^0-9A-Za-z가-힣]','',t)
nvcache={}
def nv(bid,no):
    k=f'{bid}_{no}'
    if k in nvcache: return nvcache[k]
    f=f'{B}/nv/{k}.html'; t=''
    if os.path.exists(f):
        s=BeautifulSoup(open(f,encoding='utf8',errors='ignore').read(),'lxml')
        c=s.select_one('div.se-main-container') or s.select_one('#postViewArea')
        t=c.get_text(' ',strip=True) if c else ''
    nvcache[k]=(t,norm(t)); return nvcache[k]
def sents(t):
    return [x for x in (norm(s) for s in re.split(r'(?<=[다요까죠])[.?!]\s*|\?\s*|\n',t)) if len(x)>=10]
def overlap(tt,nn):
    ss=sents(tt)
    if not ss or not nn: return None,None
    sh=sum(1 for s in ss if s in nn)
    a=norm(tt); g=[a[i:i+10] for i in range(0,max(1,len(a)-9),3)]
    ng=sum(1 for x in g if x in nn)
    return round(sh/len(ss)*100,1), round(ng/len(g)*100,1)
TOP={}
for n in [13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,39,40,41,42,46,47,48,52,55,56,57,68,70,71,73,74]: TOP[n]='인테리어'
for n in [44,58,59,60,69,72,75,82,87,89,90,92]: TOP[n]='입주'
for n in [16,33,34,35,38,51,53,61,62,63,64,65,67,78,81,84,93]: TOP[n]='시세 · 실거래'
for n in [49,76,79,80,88]: TOP[n]='분양가 · 청약'
for n in [30,31,32,36,37,43,45,66,77,91]: TOP[n]='공법 · 용어'
for n in [17,50,54]: TOP[n]='지산 · 지식산업센터'
for n in [83,85,86]: TOP[n]='기타'
EXPIRED={43:'과천 갈현지구 대토보상 10/16 마감 지남',66:'신설1구역 조서 이의 10/15 기한 지남',85:'수진1구역 4분기 이주 소식(시한성)'}
SRC={'dong_jin_kim':'dong_jin_kim','jisandream01':'jisandream01','champion_chart':'champion_chart'}
rows=[]
for p in P:
    n=p['no']; links=p['naver_links'][:12]
    best=None
    for bid,no,url in links:
        t,nn=nv(bid,no)
        if not nn: continue
        sr,gr=overlap(p['text'],nn)
        if sr is None: continue
        if best is None or gr>best[1]: best=(sr,gr,bid,no)
    orig=None; src='알 수 없음'
    h=open(f"{B}/raw/{n}.html",encoding='utf8').read(); c=BeautifulSoup(h,'lxml').select_one('div.contents_style')
    wl=[a.get('href','') for a in c.find_all('a') if '원문' in a.get_text() and 'blog.naver.com' in a.get('href','')] if c else []
    pick=None
    if wl:
        m=re.search(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d+)',wl[0])
        if m:
            t,nn=nv(m.group(1),m.group(2)); o=overlap(p['text'],nn)
            if o[0] is not None: pick=(o[0],o[1],m.group(1),m.group(2))
    if pick is None and best and best[1]>=5: pick=best
    best=pick
    empty=p['chars']<100
    if best:
        orig=f'https://blog.naver.com/{best[2]}/{best[3]}'; src=SRC.get(best[2],best[2])
    if src=='알 수 없음' and not empty and p['chars']>1000: src='알 수 없음(원문 링크 없음 · 독자 글)'
    if src=='알 수 없음' and ('사주' in p['title'] or '명리' in p['title']): src='사주 글'
    topic=TOP.get(n,'기타')
    reason=''
    sr=best[0] if best and orig else None; gr=best[1] if best and orig else None
    indep = (gr is None or gr<10)
    if empty: v='비공개 후보'; reason='빈 글(본문 0자)'
    elif topic=='인테리어': v='비공개 후보'; reason='인테리어'
    elif topic=='입주' and src.startswith('champion_chart'): v='비공개 후보'; reason='인테리어 원천 입주 · 중문 글'
    elif n in EXPIRED: v='비공개 후보'; reason='기한 지남: '+EXPIRED[n]
    elif topic=='기타': v='비공개 후보'; reason='홍보 · 대행 안내'
    elif indep and p['chars']>=2000 and p['images']>=1: v='남김'; reason='독자 내용 · 2,000자+ · 그림'
    elif topic=='분양가 · 청약': v='비공개 후보'; reason='분양 소식'
    elif topic in ('시세 · 실거래','입주') or (topic=='지산 · 지식산업센터' and n!=54): v='표페이지로 교체'; reason='시세 · 실거래 류'
    elif topic=='공법 · 용어' or n==54: v='공법글로 다시 쓰기'; reason='공법 · 용어(세금 포함)'
    else: v='비공개 후보'; reason='기타'
    rows.append(dict(번호=n,제목=p['title'],주소=p['url'],발행일=p['date'],카테고리=p['category'] or '(없음)',
      본문글자수=p['chars'],본문글자수_공백제외=p['chars_nospace'],표=p['tables'],그림=p['images'],
      대표이미지=p['og_real'],원천블로그=src,네이버원문=orig,문장겹침률=sr,글조각겹침률=gr,
      주제=topic,판정=v,판정근거=reason))
from collections import Counter
agg=dict(전체=len(rows),판정별=dict(Counter(r['판정'] for r in rows)),주제별=dict(Counter(r['주제'] for r in rows)),
  원천별=dict(Counter(r['원천블로그'] for r in rows)),
  빈글=[r['번호'] for r in rows if r['본문글자수']<100],대표이미지없음=sum(1 for r in rows if not r['대표이미지']),
  본문2000자이상=sum(1 for r in rows if r['본문글자수']>=2000),
  문장겹침_평균=round(sum(r['문장겹침률'] for r in rows if r['문장겹침률'] is not None)/max(1,sum(1 for r in rows if r['문장겹침률'] is not None)),1),
  문장겹침_50이상=sum(1 for r in rows if (r['문장겹침률'] or 0)>=50),
  기준='본문=글 화면 div.contents_style 글자(공백 포함) · 대표이미지=og:image가 티스토리 기본 opengraph.png 아닌 것 · 문장겹침률=티스토리 문장(10자+) 중 네이버 원문에 그대로 있는 비율 · 글조각겹침률=10글자 조각 포함률 · 원문=본문의 「원문 보기」 링크, 없으면 본문 속 네이버 링크 중 글조각 겹침 최대(5% 미만이면 원문 없음=독자 글로 봄; 관련 없는 글끼리 겹침은 0~3%)',
  점검일='2026-11-10',sitemap_글번호='13~93 (81편, 1~12 · 94~ 없음)')
json.dump(dict(집계=agg,글=rows),open(f'{B}/talk7921.json','w'),ensure_ascii=False,indent=1)
# md
L=['# talk7921.tistory.com 전수 점검 (2026-11-10)','',f"전체 {agg['전체']}편 · 기준: {agg['기준']}",'','## 집계','','| 항목 | 값 |','|---|---|']
for k,v in agg['판정별'].items(): L.append(f'| 판정: {k} | {v} |')
L+= [f"| 빈 글 | {len(agg['빈글'])}편 ({', '.join(map(str,agg['빈글']))}) |",f"| 대표 이미지 없음 | {agg['대표이미지없음']}편 |",f"| 본문 2,000자 이상 | {agg['본문2000자이상']}편 |",f"| 문장 겹침 평균 | {agg['문장겹침_평균']}% |",f"| 문장 겹침 50% 이상 | {agg['문장겹침_50이상']}편 |"]
for k,v in agg['주제별'].items(): L.append(f'| 주제: {k} | {v} |')
for k,v in agg['원천별'].items(): L.append(f'| 원천: {k} | {v} |')
L+=['','## 글별','','| 번호 | 제목 | 발행일 | 카테고리 | 글자 | 표 | 그림 | 대표이미지 | 원천 | 문장겹침 | 조각겹침 | 주제 | 판정 | 근거 |','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for r in rows:
    f=lambda x:'-' if x is None else f'{x}%'
    t=f"[{r['제목'][:38]}]({r['주소']})"
    o=r['원천블로그'] if not r['네이버원문'] else f"[{r['원천블로그']}]({r['네이버원문']})"
    L.append(f"| {r['번호']} | {t} | {r['발행일']} | {r['카테고리']} | {r['본문글자수']:,} | {r['표']} | {r['그림']} | {'O' if r['대표이미지'] else 'X'} | {o} | {f(r['문장겹침률'])} | {f(r['글조각겹침률'])} | {r['주제']} | **{r['판정']}** | {r['판정근거']} |")
open(f'{B}/talk7921_audit.md','w').write('\n'.join(L)+'\n')
print(json.dumps(agg,ensure_ascii=False))

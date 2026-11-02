# 수요 신호 정기 확인 (2026.10.8 08:47 사용자 「오케이」 — ① 제휴 업체가 요즘 일하는 동네 ④ 자동완성에 새로 생긴 말을 화 · 금 정기 확인에 넣음)
#   python3 demand_watch.py            → watch/demand_watch.json(이번 결과) · 화면에 요약 · 지난번 결과는 demand_watch_prev.json으로 옮김
#   ① partner(): 자료를 써도 되는 제휴 업체 블로그의 최근 60편 제목에서 지역 이름을 센다(발행 목록 두 쪽만 새로 받음 · src/*_list.json은 건드리지 않음)
#   ④ ac(): 품목별 씨앗 검색어의 네이버 자동완성을 저장하고 지난번에 없던 말을 찾는다
import subprocess, json, re, os, sys, collections, urllib.parse, datetime, time
sys.path.insert(0,'/home/claude/blogkit')
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36'
D='/home/claude/watch/'
PARTNERS=[('daonsash','샷시'),('dbswkdrms89','중문'),('ejn590807','중문'),('rodeosky','중문'),('clovermc2644','중문'),('pjh20712','중문'),('ssu2058','코킹'),('doha_film','필름'),('thebigfilm','필름'),('jinair7','시스템에어컨')]
REG=('수원|영통|광교|매탄|권선|용인|수지|기흥|화성|동탄|병점|성남|분당|판교|위례|안양|평촌|군포|산본|의왕|과천|부천|중동|상동|인천|부평|송도|청라|검단|고양|일산|화정|행신|파주|운정|김포|남양주|다산|별내|구리|하남|미사|의정부|양주|평택|오산|안산|시흥|광명|'
     '노원|상계|중계|도봉|창동|강서|마곡|양천|목동|구로|영등포|송파|강동|강남|서초|마포|은평|성북|동대문|중랑|관악|천안|아산|청주|세종|대전|부산|창원|김해|양산')
def recent(B,pages=2):
    out=[]
    for p in range(1,pages+1):
        u=f'https://blog.naver.com/PostTitleListAsync.naver?blogId={B}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30'
        s=subprocess.run(['curl','-s','-m','20','-A',UA,'-H','Referer: https://blog.naver.com/'+B,u],capture_output=True).stdout.decode('utf-8','replace')
        try: L=json.loads(s.replace("\\'","'")).get('postList',[])
        except Exception: break
        out+=[(x['logNo'],urllib.parse.unquote_plus(x['title']),x.get('addDate','')) for x in L]
        if len(L)<30: break
        time.sleep(0.8)
    return out
def partner():
    R={}
    for B,kind in PARTNERS:
        L=recent(B); c=collections.Counter()
        for n,t,d in L:
            for k in set(re.findall(REG,t)): c[k]+=1
        R[B]=dict(kind=kind,n=len(L),top=c.most_common(8),latest=[t for n,t,d in L[:3]])
    return R
SEED=['중문','현관 중문','중문 설치','무타공 중문','샷시 교체','샷시 교체 비용','창틀 코킹','외벽 코킹','베란다 누수','인테리어 필름','샷시 필름','입주청소','이사청소','결로','외풍','구축 아파트 인테리어','부분 인테리어','방묘문','방음 중문','샷시 지원금','농막','체류형 쉼터',
      '수원 인테리어','영통 인테리어','산본 인테리어','부천 인테리어','상계동 인테리어','일산 인테리어','평촌 인테리어','분당 인테리어','수원 샷시','부천 샷시','군포 샷시','안양 샷시','용인 샷시','수원 중문','동탄 중문','인천 중문']
def ac():
    import seo
    r=seo.ac_many(SEED); return {k:list(v) for k,v in r.items()}
if __name__=='__main__' and len(sys.argv)==1:
    f=D+'demand_watch.json'; prev=json.load(open(f)) if os.path.exists(f) else None
    now=dict(made=str(datetime.datetime.now())[:16],partner=partner(),ac=ac())
    if prev:
        now['ac_new']={k:[x for x in v if x not in prev['ac'].get(k,[])] for k,v in now['ac'].items() if k in prev['ac'] and [x for x in v if x not in prev['ac'].get(k,[])]}
        os.replace(f,D+'demand_watch_prev.json')
    json.dump(now,open(f,'w'),ensure_ascii=False,indent=1)
    print('업체가 요즘 일하는 동네(최근 60편 제목)')
    for B,v in now['partner'].items(): print('  ',v['kind'],B,v['n'],'편 |',' · '.join(f'{a} {b}' for a,b in v['top']))
    print('자동완성에 새로 생긴 말:',json.dumps(now.get('ac_new','(첫 실행 · 비교할 지난 결과 없음)'),ensure_ascii=False))

# ② 전세 만기가 몰리는 단지 (10/8 08:55 한 번 계산해 보고 넣음) — 전월세 실거래의 「계약기간」 끝 달이 앞으로 석 달 안인 계약을 단지별로 센다
#   python3 demand_watch.py lease  → watch/lease_end.json · 한 달에 한 번이면 됨(2년 전 계약이라 자료가 바뀌지 않는다) · 임대 · 행복주택 · 뉴스테이 단지는 뺀다
PUBLIC=r'임대|행복주택|뉴스테이|엘에이치|LH|국민|영구|공공|리츠|청년|기숙사|사원|드림타운|따복|휴먼시아.*단지$'
def lease(today=None,fetch=True):
    import pandas as pd, io
    sys.path.insert(0,D); import rt_fetch
    d0=today or datetime.date.today()
    def add(y,m,k):
        m+=k; y+=(m-1)//12; m=(m-1)%12+1; return f'{y}{m:02d}'
    ends=[add(d0.year,d0.month,k) for k in (1,2,3)]                       # 다음 달부터 석 달
    src=sorted({add(int(e[:4])-2,int(e[4:]),k) for e in ends for k in (-2,-1,0)})   # 2년 계약은 보통 만기 24~26달 전에 계약
    if fetch:
        for ym in src:
            for sido in rt_fetch.SIDO:
                f=rt_fetch.D+f'rent_{rt_fetch.SIDO[sido]}_{ym}.csv'
                if not os.path.exists(f):
                    n=rt_fetch.fetch(sido,ym,rent=True) or rt_fetch.fetch(sido,ym,rent=True); print('전월세',sido,ym,n if n is not None else '못 받음',flush=True); time.sleep(1.5)
    fr=[]
    for fn in sorted(os.listdir(rt_fetch.D)):
        m=re.match(r'rent_(\d+)_(\d{6})\.csv$',fn)
        if m and m.group(2) in src:
            t=open(rt_fetch.D+fn,'rb').read().decode('cp949','ignore'); i=t.find('"NO","시군구"')
            if i>=0: fr.append(pd.read_csv(io.StringIO(t[i:]),dtype=str))
    d=pd.concat(fr,ignore_index=True); d['end']=d['계약기간'].str.extract(r'~(\d{6})')[0]
    x=d[d['end'].isin(ends)&(d['전월세구분']=='전세')&~d['단지명'].str.contains(PUBLIC,na=False)].copy()
    g=x.groupby(['시군구','단지명','건축년도']).size().sort_values(ascending=False).head(40)
    out=dict(made=str(d0),ends=ends,src=src,n=int(len(x)),rows=[dict(시군구=k[0],단지=k[1],지은해=k[2],n=int(v)) for k,v in g.items()])
    json.dump(out,open(D+'lease_end.json','w'),ensure_ascii=False,indent=1); return out
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='lease':
    R=lease(); print('전세 만기',R['ends'],'· 민간 전세',R['n'],'건')
    for r in R['rows'][:20]: print('  ',r['시군구'],r['단지'],r['지은해'],r['n'])

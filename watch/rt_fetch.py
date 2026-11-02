# 국토교통부 실거래가 공개시스템(rt.molit.go.kr)에서 아파트 매매 실거래를 달별로 받는다 (2026.10.8 08:23 사용자: 「거래가 많은지는 네가 확인할 수 있지? 정기적으로 확인해」)
#   python3 rt_fetch.py            → 가장 최근 석 달(이번 달 포함)을 서울 · 경기 · 인천에서 다시 받음(신고가 30일 안에 들어오고 해제가 생겨서 지난 달도 다시 받는다)
#   python3 rt_fetch.py 202607 202608   → 그 달만
#   load(yms) → DataFrame(시군구 · 단지명 · a 전용면적 · p 억원 · ym · y 건축년도 · 해제 · 광역 · 시군 · 구 · 읍면동)  해제된 거래는 뺀 것
# 하루 내려받기 100건 제한이 있다(사이트 안내) → 한 번에 아홉 건(세 시도 × 석 달)만. 한 달 · 한 시도씩 받는다(기간은 1년까지).
import subprocess, re, os, sys, io, time, datetime
D='/home/claude/watch/rt/'; UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36'
SIDO={'서울특별시':'11000','경기도':'41000','인천광역시':'28000'}
def _last_day(ym):
    y,m=int(ym[:4]),int(ym[4:]); n=(datetime.date(y+(m==12),(m%12)+1,1)-datetime.timedelta(days=1)).day
    return f'{y}-{m:02d}-01',f'{y}-{m:02d}-{n:02d}'
def fetch(sido,ym,rent=False):
    from urllib.parse import quote
    ck=D+'ck.txt'; h=subprocess.run(['curl','-sS','-m','40','-c',ck,'-A',UA,'https://rt.molit.go.kr/pt/xls/xls.do?mobileAt='],capture_output=True).stdout.decode('utf-8','ignore')
    js=re.search(r'jsessionid=[A-Za-z0-9._]+',h); js=';'+js.group(0) if js else ''
    a,b=_last_day(ym); q=quote('전체')
    data=(f'srhThingNo=A&srhDelngSecd={2 if rent else 1}&srhAddrGbn=1&srhLfstsSecd=1&sidoNm={quote(sido)}&sggNm={q}&emdNm={q}&loadNm={q}&areaNm={q}&hsmpNm={q}&mobileAt=&srhFromDt={a}&srhToDt={b}'
          f'&srhNewRonSecd=&srhSidoCd={SIDO[sido]}&srhSggCd=&srhEmdCd=&srhRoadNm=&srhLoadCd=&srhHsmpCd=&srhArea=&srhLrArea=&srhFromAmount=&srhToAmount=')
    f=D+f'{"rent" if rent else "apt"}_{SIDO[sido]}_{ym}.csv'; tmp=f+'.tmp'   # rent=True면 전월세(10/8 08:50 전세 만기 단지 계산용)
    r=subprocess.run(['curl','-sS','-m','150','-b',ck,'-A',UA,'-H','Referer: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=','-X','POST','-d',data,'-o',tmp,'-w','%{http_code}','https://rt.molit.go.kr/pt/xls/ptXlsCSVDown.do'+js],capture_output=True).stdout.decode()
    t=open(tmp,'rb').read().decode('cp949','ignore') if os.path.exists(tmp) else ''
    if r!='200' or '"NO","시군구"' not in t: 
        if os.path.exists(tmp): os.remove(tmp)
        return None
    os.replace(tmp,f); return t.count('\n')-16
def recent(n=3,today=None):
    d=today or datetime.date.today(); out=[]
    for i in range(n):
        y,m=d.year,d.month-i
        while m<=0: y-=1; m+=12
        out.append(f'{y}{m:02d}')
    return sorted(out)
def load(yms=None,sidos=None):
    import pandas as pd
    fr=[]
    for fn in sorted(os.listdir(D)):
        m=re.match(r'apt_(\d+)_(\d{6})\.csv$',fn)
        if not m or (yms and m.group(2) not in yms): continue
        t=open(D+fn,'rb').read().decode('cp949','ignore'); i=t.find('"NO","시군구"')
        if i<0: continue
        x=pd.read_csv(io.StringIO(t[i:]),dtype=str); fr.append(x)
    if not fr: return None
    d=pd.concat(fr,ignore_index=True)
    d=d[d['해제사유발생일']=='-'].copy()
    d['p']=d['거래금액(만원)'].str.replace(',','').astype(float)/1e4; d['a']=d['전용면적(㎡)'].astype(float); d['ym']=d['계약년월'].astype(int); d['y']=pd.to_numeric(d['건축년도'],errors='coerce')
    s=d['시군구'].str.split(); d['광역']=s.str[0]; d['읍면동']=s.str[-1]
    d['시군']=s.apply(lambda v: v[1] if len(v)>1 else ''); d['구']=s.apply(lambda v: v[2] if len(v)>3 else '')
    return d
if __name__=='__main__':
    yms=sys.argv[1:] or recent(3)
    for ym in yms:
        for sido in SIDO:
            n=fetch(sido,ym); print(sido,ym,n if n is not None else '못 받음',flush=True); time.sleep(1.5)

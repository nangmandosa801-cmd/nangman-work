"""하남시 아파트 매매 실거래 2014~2024년을 국토부에서 받아 2025(M2025.pkl) · 2026(/tmp/fresh/M_hanam26.pkl 또는 M2026.pkl)과 합쳐
/home/claude/rtn/M_hanam_2014_2026.pkl 로 만든다. 해제 · 직거래 뺌. 컬럼 p(만원) a(㎡) ym y dong.
사용: python3 dl_hanam.py  (raw는 /home/claude/rtn/raw_hanam/M<년>_hanam.csv, 있으면 건너뜀)"""
import requests, os, time, io, glob, pandas as pd
RAW='/home/claude/rtn/raw_hanam'; os.makedirs(RAW,exist_ok=True)
S=requests.Session(); S.headers['User-Agent']='Mozilla/5.0'; S.verify='/root/.ccr/ca-bundle.crt'
B='https://rt.molit.go.kr'; S.get(B+'/pt/xls/xls.do?mobileAt=')
def dl(fr,to,out):
    if os.path.exists(out) and os.path.getsize(out)>5000: return 'skip'
    d=dict(srhThingNo='A',srhDelngSecd='1',srhAddrGbn='1',srhLfstsSecd='1',sidoNm='경기도',sggNm='하남시',emdNm='전체',loadNm='전체',areaNm='전체',hsmpNm='전체',mobileAt='',srhFromDt=fr,srhToDt=to,srhSidoCd='41000',srhSggCd='41450',srhEmdCd='',srhRoadNm='',srhLoadCd='',srhHsmpCd='',srhArea='',srhLrArea='',srhFromAmount='',srhToAmount='',srhNewRonSecd='')
    S.post(B+'/pt/xls/ptXlsDownDataCheck.do',data=d,headers={'Referer':B+'/pt/xls/xls.do?mobileAt='})
    r=S.post(B+'/pt/xls/ptXlsCSVDown.do',data=d,headers={'Referer':B+'/pt/xls/xls.do?mobileAt='},timeout=600)
    open(out,'wb').write(r.content); return len(r.content)
for y in range(2014,2025):
    for k in range(3):
        try: print(y,dl(f'{y}-01-01',f'{y}-12-31',f'{RAW}/M{y}_hanam.csv'),flush=True); break
        except Exception as e: print('ERR',y,e); time.sleep(5)
def load(path):
    raw=open(path,'rb').read().decode('cp949',errors='replace'); lines=raw.splitlines()
    i=[k for k,l in enumerate(lines) if l.startswith('"NO"')][0]
    return pd.read_csv(io.StringIO('\n'.join(lines[i:])),dtype=str)
D=[load(f) for f in sorted(glob.glob(f'{RAW}/M*_hanam.csv'))]
a=pd.read_pickle('/home/claude/rtn/M2025.pkl'); a=a[a['시군구'].str.contains('경기도 하남시')]
f26='/tmp/fresh/M_hanam26.pkl' if os.path.exists('/tmp/fresh/M_hanam26.pkl') else '/home/claude/rtn/M2026.pkl'
b=pd.read_pickle(f26); b=b[b['시군구'].str.contains('경기도 하남시')]
m=pd.concat(D+[a,b],ignore_index=True)
m=m[m['해제사유발생일'].astype(str).str.strip().isin(['-',''])|m['해제사유발생일'].isna()]
m=m[m['거래유형']!='직거래']
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m['p']=num(m['거래금액(만원)']); m['a']=num(m['전용면적(㎡)']); m['ym']=m['계약년월'].astype(int); m['y']=m.ym//100
m['dong']=m['시군구'].str.split().str[-1]
m.to_pickle('/home/claude/rtn/M_hanam_2014_2026.pkl'); print(len(m), m.y.value_counts().sort_index().to_dict(), '2026 from', f26)

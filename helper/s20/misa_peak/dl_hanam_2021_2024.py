import requests, os, sys, time
S=requests.Session(); S.headers['User-Agent']='Mozilla/5.0'
S.verify='/root/.ccr/ca-bundle.crt' if os.path.exists('/root/.ccr/ca-bundle.crt') else os.path.expanduser('~/.ccr/ca-bundle.crt')
B='https://rt.molit.go.kr'
S.get(B+'/pt/xls/xls.do?mobileAt=')
def dl(fr,to,out):
    if os.path.exists(out) and os.path.getsize(out)>1000: return 'skip'
    d=dict(srhThingNo='A',srhDelngSecd='1',srhAddrGbn='1',srhLfstsSecd='1',sidoNm='경기도',sggNm='하남시',emdNm='전체',loadNm='전체',areaNm='전체',hsmpNm='전체',mobileAt='',srhFromDt=fr,srhToDt=to,srhSidoCd='41000',srhSggCd='41450',srhEmdCd='',srhRoadNm='',srhLoadCd='',srhHsmpCd='',srhArea='',srhLrArea='',srhFromAmount='',srhToAmount='',srhNewRonSecd='')
    c=S.post(B+'/pt/xls/ptXlsDownDataCheck.do',data=d,headers={'Referer':B+'/pt/xls/xls.do?mobileAt='}).json()
    r=S.post(B+'/pt/xls/ptXlsCSVDown.do',data=d,headers={'Referer':B+'/pt/xls/xls.do?mobileAt='},timeout=600)
    open(out,'wb').write(r.content)
    return c, len(r.content), r.headers.get('Content-Type')
for y in [2021,2022,2023,2024]:
    for k in range(3):
        try: print(y,dl(f'{y}-01-01',f'{y}-12-31',f'rawH/MH{y}.csv'),flush=True); break
        except Exception as e: print('ERR',y,e,flush=True); time.sleep(5)
    time.sleep(2)

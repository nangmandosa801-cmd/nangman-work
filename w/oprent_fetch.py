import sys; sys.path.insert(0,'/home/claude/watch')
import rt_fetch,subprocess,re,os
from urllib.parse import quote
def fetch_land(sido,a,b,code='G'):
    D=rt_fetch.D; UA=rt_fetch.UA; ck=D+'ck.txt'
    subprocess.run(['curl','-sS','-m','40','-c',ck,'-A',UA,'https://rt.molit.go.kr/pt/xls/xls.do?mobileAt='],capture_output=True)
    q=quote('전체')
    data=(f'srhThingNo={code}&srhDelngSecd=2&srhAddrGbn=1&srhLfstsSecd=1&sidoNm={quote(sido)}&sggNm={q}&emdNm={q}&loadNm={q}&areaNm={q}&hsmpNm={q}&mobileAt=&srhFromDt={a}&srhToDt={b}'
          f'&srhNewRonSecd=&srhSidoCd={rt_fetch.SIDO[sido]}&srhSggCd=&srhEmdCd=&srhRoadNm=&srhLoadCd=&srhHsmpCd=&srhArea=&srhLrArea=&srhFromAmount=&srhToAmount=')
    f=D+f'oprent_{rt_fetch.SIDO[sido]}_{a[:7]}_{b[:7]}.csv'
    url=re.search(r"'(https://rt\.molit\.go\.kr/pt/xls/ptXlsCSVDown[^']*)'",open(rt_fetch.__file__).read()).group(1)
    r=subprocess.run(['curl','-sS','-m','170','-b',ck,'-A',UA,'-H','Referer: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=','-X','POST','-d',data,'-o',f,'-w','%{http_code}',url],capture_output=True)
    print(r.stdout.decode(),r.stderr.decode()[:200])
    if os.path.exists(f):
        t=open(f,'rb').read().decode('cp949','ignore'); i=t.find('"NO"'); print(len(t)); print(t[:300] if i<0 else t[i:i+500])
fetch_land(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4] if len(sys.argv)>4 else 'G')

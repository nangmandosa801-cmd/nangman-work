import re,json,subprocess,sys
def sh(*a): return subprocess.run(list(a),capture_output=True).stdout
for pid in sys.argv[1:]:
    h=open(f'p{pid}.html',encoding='utf8',errors='ignore').read() if False else sh('curl','-s','-m','20','-c','cj','-b','cj',f'https://www.data.go.kr/data/{pid}/fileData.do').decode('utf8','ignore')
    m=re.search(r"fn_fileDataDown\('(\d+)', '(uddi:[^']+)'",h)
    if not m: print(pid,'no uddi'); continue
    j=sh('curl','-s','-m','20','-c','cj','-b','cj','-H','X-Requested-With: XMLHttpRequest','--data',f'publicDataPk={pid}&publicDataDetailPk={m.group(2)}','https://www.data.go.kr/tcs/dss/selectFileDataDownload.do').decode('utf8','ignore')
    try: o=json.loads(j)
    except Exception: print(pid,'bad',j[:100]); continue
    a,s=o.get('atchFileId'),o.get('fileDetailSn'); nm=o.get('dataSetFileDetailInfo',{}).get('dataNm','')
    ext=o.get('dataSetFileDetailInfo',{}).get('atchFileExtsn') or 'csv'
    b=sh('curl','-s','-m','40','-c','cj','-b','cj',f'https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId={a}&fileDetailSn={s}')
    open(f'd{pid}.{ext}','wb').write(b); print(pid,nm,ext,len(b))

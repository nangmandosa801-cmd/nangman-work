import re,subprocess,sys,urllib.parse,html
def search(k):
    u="https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword="+urllib.parse.quote(k)
    t=subprocess.run(['curl','-s','--max-time','25',u],capture_output=True,text=True).stdout
    out=[]
    for m in re.finditer(r'/data/(\d+)/fileData\.do',t):
        i=m.start(); seg=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t[max(0,i-1500):i+300]))
        out.append((m.group(1),seg[-500:]))
    # titles
    titles=re.findall(r'(경기도 [가-힣]+_[^<\n]{2,40}중개[^<\n]{0,20})',t)
    return sorted(set(m.group(1) for m in re.finditer(r'/data/(\d+)/fileData\.do',t))),sorted(set(titles))
def dl(did,out):
    t=subprocess.run(['curl','-s','--max-time','25',f'https://www.data.go.kr/data/{did}/fileData.do'],capture_output=True,text=True).stdout
    a=re.findall(r'atchFileId[^&"\']*[=:][\'"]?(FILE_[0-9]+)',t); title=re.findall(r'<title>([^<]*)',t)
    if not a: print('no file',did); return
    subprocess.run(['curl','-s','--max-time','30','-L','-A','Mozilla/5.0','-e',f'https://www.data.go.kr/data/{did}/fileData.do',f'https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId={a[0]}&fileDetailSn=1',
                    '-o',out])
    print(did,title[:1],out)
if __name__=='__main__':
    for k in sys.argv[1:]: print(k,search(k))

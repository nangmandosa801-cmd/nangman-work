import re,sys,subprocess
q=sys.argv[1]
for pg in range(1,8):
    f=f'l_{q}_{pg}.html'
    subprocess.run(['curl','-sS','-m','40','-A','Mozilla/5.0','-o',f,'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do','--data-urlencode','beginPd=202001','--data-urlencode','endPd=202610','--data-urlencode',f'houseNm={q}','--data-urlencode',f'pageIndex={pg}'])
    h=open(f,errors='ignore').read();n=0
    for m in re.finditer(r'<tr data-pbno="(\d+)" data-hmno="(\d+)"(?: data-hsecd="(\d+)")? data-honm="([^"]*)"[^>]*>(.*?)</tr>',h,re.S):
        n+=1;ds=re.findall(r'\d{4}-\d{2}-\d{2}',m.group(5));print(m.group(1),m.group(2),m.group(3),m.group(4),ds[:1])
    if n<10: break

import sys,re,subprocess,os
pb=sys.argv[1]
f=f'apt{pb}.html'
subprocess.run(['curl','-sS','-m','50','-A','Mozilla/5.0','-o',f,'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do','--data-urlencode',f'houseManageNo={pb}','--data-urlencode',f'pblancNo={pb}'])
h=open(f,errors='ignore').read()
m=re.findall(r'href="(https://static\.applyhome\.co\.kr/ai/aia/getAtchmnfl[^"]+)"',h)
print(pb,len(h),m[:2])
if m:
    p=f'apt{pb}.pdf'
    subprocess.run(['curl','-sS','-m','200','-A','Mozilla/5.0','-o',p,m[0].replace('&amp;','&')])
    subprocess.run(['pdftotext','-layout',p,f'apt{pb}.txt'])
    print(os.path.getsize(p), os.path.getsize(f'apt{pb}.txt') if os.path.exists(f'apt{pb}.txt') else 0)

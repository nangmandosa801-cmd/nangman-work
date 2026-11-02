import re,sys,subprocess,os
UA='Mozilla/5.0'
for hm in sys.argv[1:]:
    f=f'd{hm}.html'
    subprocess.run(['curl','-sS','-m','50','-A',UA,'-o',f,'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do','--data-urlencode',f'houseManageNo={hm}','--data-urlencode',f'pblancNo={hm}'])
    h=open(f,errors='ignore').read(); m=re.findall(r'href="(https://static\.applyhome\.co\.kr/ai/aia/getAtchmnfl[^"]+)"',h)
    print(hm,len(m))
    if m:
        p=f'apt{hm}.pdf'
        subprocess.run(['curl','-sS','-m','200','-A',UA,'-o',p,m[0].replace('&amp;','&')])
        subprocess.run(['pdftotext','-layout',p,f'apt{hm}.txt'])
        print(os.path.getsize(p), os.path.getsize(f'apt{hm}.txt') if os.path.exists(f'apt{hm}.txt') else 0)

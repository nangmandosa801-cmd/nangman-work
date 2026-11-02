import json,os,subprocess,csv
from PIL import Image
import letter, blogpage
from pypdf import PdfWriter
L=json.load(open('list.json')); B='build'; O='/mnt/user-data/outputs/mail1018'; os.makedirs(O,exist_ok=True)
allw=PdfWriter()
for x in L:
    lp=letter.page(x,B)
    subprocess.run(['python3','/home/claude/int/partner/flyer.py',x['code'],x['office']],env={**os.environ,'OUTDIR':B},check=True,capture_output=True)
    fp=f"{B}/nangman_interior_partner_flyer_{x['code']}.png"
    bp=f"{B}/letter_blog.png"; blogpage.page_blog(x).save(bp)  # 10/19 블로그 대행 제안 장
    pages=[Image.open(p).convert('RGB').resize((1654,2339),Image.LANCZOS) for p in (*lp,bp,fp)]
    out=f"{O}/nangman_interior_mail_{x['code']}.pdf"
    pages[0].save(out,'PDF',resolution=200,quality=85,save_all=True,append_images=pages[1:])
    allw.append(out)
allw.write(f'{O}/nangman_interior_mail_전체_30곳.pdf')
with open(f'{O}/nangman_interior_mail_주소록_30곳.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['단지','입주 시작','보낼 기한','순서','코드','받는 사람','사무소','도로명주소','우편번호','사무소 전화'])
    for i,x in enumerate(L,1):
        dj=x['danji'].split(' (')[0]; ip='2026-10-02' if x['code'].startswith('PJ') else '2026-10 (날짜는 단지 공고 확인)'
        w.writerow([dj,ip,'2026-10-23(금) 접수',i,x['code'],x['ceo']+' 대표',x['office'],x['addr'],'',x['tel']])
print('done')

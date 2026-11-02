# 10/19 19:28 사용자 「1번으로 가자」 — e그린우편에 한 파일 + 주소록으로 보낼 공통판 두 개(2년차 25 · 입주 DJ-01)
import json,os,subprocess,csv
from PIL import Image
import letter_common as letter, blogpage
B='build_common'; O='/mnt/user-data/outputs/mail1019_common'; os.makedirs(B,exist_ok=True); os.makedirs(O,exist_ok=True)
bp=f'{B}/letter_blog.png'; blogpage.page_blog({}).save(bp)
two=json.load(open('list_two.json'))
dj={'code':'DJ-01','office':'수정 공인중개사사무소','danji':'힐스테이트 동작 시그니처','ceo':'','addr':'서울 동작구 양녕로 174, 103호','tel':'010-6246-3010'}
for name,code,mode,rows in (('2년차','T2','two',two),('입주','IP','',[dj])):
    x={'code':code,'office':'단지 안 공인중개사사무소','danji':'대표님 단지','ceo':'','mode':mode}
    lp=letter.page(x,B)
    env={**os.environ,'OUTDIR':B,'COMMON':'1'}
    if mode: env['MODE']=mode
    subprocess.run(['python3','/home/claude/int/partner/flyer.py',code,''],env=env,check=True,capture_output=True)
    pg=[Image.open(p).convert('RGB').resize((1654,2339),Image.LANCZOS) for p in (*lp,bp,f"{B}/nangman_interior_partner_flyer_{code}.png")]
    pg[0].save(f"{O}/nangman_interior_mail_공통_{name}.pdf",'PDF',resolution=200,quality=85,save_all=True,append_images=pg[1:])
    with open(f'{O}/nangman_interior_mail_주소록_{name}_{len(rows)}곳.csv','w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['코드','단지','받는 사람','사무소','주소','전화'])
        for r in rows: w.writerow([r['code'],r['danji'].split(' (')[0],(r['ceo']+' 대표') if r.get('ceo') else '대표님',r['office'],r['addr'],r.get('tel','')])
print(os.listdir(O))

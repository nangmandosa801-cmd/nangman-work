# 10/19 00:47 사용자 「발송 안 한 모든 편지 내용 다 바꿔줘」 — 보낸 1차 6곳 빼고 전부 다시 뽑음
# 편지 2쪽(중개사 연락 010-2882-8165) → 블로그 대행 → 손님 전단(손님 번호 010-2882-8165)
import json,os,subprocess,csv
from PIL import Image
import letter, blogpage
SENT={'PJ-01','PJ-04','PJ-05','OS-01','OS-07','OS-11'}
L=[x for x in json.load(open('list.json')) if x['code'] not in SENT]+json.load(open('list_two.json'))
L.append({'code':'DJ-01','office':'수정 공인중개사사무소','danji':'힐스테이트 동작 시그니처','ceo':'','addr':'서울 동작구 양녕로 174, 103호','tel':'010-6246-3010','ipju':'2026-12-01'})
B='build'; O='/mnt/user-data/outputs/mail1019'; os.makedirs(O,exist_ok=True)
bp=f'{B}/letter_blog.png'; blogpage.page_blog({}).save(bp)
for x in L:
    lp=letter.page(x,B)
    env={**os.environ,'OUTDIR':B}; 
    if x.get('mode')=='two': env['MODE']='two'
    subprocess.run(['python3','/home/claude/int/partner/flyer.py',x['code'],x['office']],env=env,check=True,capture_output=True)
    fp=f"{B}/nangman_interior_partner_flyer_{x['code']}.png"
    pg=[Image.open(p).convert('RGB').resize((1654,2339),Image.LANCZOS) for p in (*lp,bp,fp)]
    pg[0].save(f"{O}/nangman_interior_mail_{x['code']}.pdf",'PDF',resolution=200,quality=85,save_all=True,append_images=pg[1:])
with open(f'{O}/nangman_interior_mail_주소록_1019.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['코드','단지','받는 사람','사무소','주소','전화','파일'])
    for x in L: w.writerow([x['code'],x['danji'].split(' (')[0],(x['ceo']+' 대표') if x.get('ceo') else '대표님',x['office'],x['addr'],x.get('tel',''),f"nangman_interior_mail_{x['code']}.pdf"])
print(len(L))

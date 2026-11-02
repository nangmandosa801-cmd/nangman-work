import json,re,collections,csv,os,subprocess
from PIL import Image
import letter
d=json.load(open('two_year.json'))
pre={'광명':'GM','안양':'AY','용인':'YI','안성':'AS','오산':'OS','화성':'HS','이천':'IC'}
cnt=collections.Counter({'OS':15}); L=[]
for x in d:
    for f in x.get('offices',[]):
        p=next(v for k,v in pre.items() if k in x['city']); cnt[p]+=1
        off=re.sub(r'\(?0[0-9]{1,2}[.\-)]?[0-9]{3,4}[.\-][0-9]{4}\)?|\([0-9]{3}-[0-9]{4}\)','',f['office']).replace('()','').strip()
        off=re.sub(r'\((안양역푸르지오더샵)\)','',off).strip()
        dj=re.sub(r'\(.*?\)','',x['danji']).strip()
        L.append(dict(code=f'{p}-{cnt[p]:02d}',danji=dj,office=off,ceo=f['ceo'],addr=f['addr'],tel=f.get('tel',''),ipju=x['ipju'],mode='two'))
json.dump(L,open('list_two.json','w'),ensure_ascii=False,indent=1)
O='/mnt/user-data/outputs/mail1018/two'; os.makedirs(O,exist_ok=True)
for x in L:
    p=letter.page(x,'build')
    subprocess.run(['python3','/home/claude/int/partner/flyer.py',x['code'],x['office']],env={**os.environ,'OUTDIR':'build','MODE':'two'},check=True,capture_output=True)
    pg=[Image.open(q).convert('RGB').resize((1654,2339),Image.LANCZOS) for q in (*p,f"build/nangman_interior_partner_flyer_{x['code']}.png")]
    pg[0].save(f"{O}/nangman_{x['code'].replace('-','')}.pdf",'PDF',resolution=200,quality=88,save_all=True,append_images=pg[1:])
with open(f'{O}/nangman_2년차_주소록.csv','w',encoding='utf-8-sig',newline='') as fh:
    w=csv.writer(fh); w.writerow(['단지','입주','보낼 기한','파일','코드','받는 사람','사무소','주소','우편번호','전화'])
    for x in L: w.writerow([x['danji'],x['ipju'],'2026-10-23(금) 접수',f"nangman_{x['code'].replace('-','')}.pdf",x['code'],x['ceo']+' 대표',x['office'],x['addr'],'',x['tel']])
for x in L: print(x['code'],x['danji'],'|',x['office'],'|',x['ceo'],'|',x['addr'],'|',x['tel'])

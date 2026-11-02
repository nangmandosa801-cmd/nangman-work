import json,subprocess
SIDO={'11':'서울','26':'부산','27':'대구','28':'인천','29':'광주','30':'대전','31':'울산','36':'세종','41':'경기','51':'강원','42':'강원','43':'충북','44':'충남','52':'전북','45':'전북','46':'전남','47':'경북','48':'경남','50':'제주'}
out=[]
for a in SIDO:
    u=f'https://asil.kr/app/data/data_movein.jsp?area={a}&order=movein_yyyymm&orderby=asc&sY=2026&sM=10&eY=2027&eM=12'
    r=subprocess.run(['curl','-s','-m','30','-A','Mozilla/5.0','-e','https://asil.kr/app/household_rts_list.jsp',u],capture_output=True).stdout.decode('utf8','ignore')
    try: d=json.loads(r)
    except Exception: d=[]
    d=[x for x in d if 'name' in x]
    for x in d: x['sido']=SIDO[a]
    out+=d; print(a,len(d))
json.dump(out,open('asil_movein.json','w'),ensure_ascii=False,indent=0)
print('total',len(out))

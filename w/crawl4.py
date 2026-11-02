src=open('nm.py').read().split('def blog')[0]; exec(src)
import csv,json,os
rows=list(csv.reader(open('/mnt/user-data/outputs/int/낭만인테리어_글감_106.csv',encoding='utf-8-sig')))[1:]
out=json.load(open('kw_depth.json')) if os.path.exists('kw_depth.json') else {}
for r in rows:
    k=r[2]
    if k in out: continue
    try: c=ac(k)
    except: c=[]
    stem=' '.join(k.split()[:-1]) if len(k.split())>1 else k[:2]
    try: s=ac(stem) if stem else []
    except: s=[]
    out[k]={'kids':c,'stem':stem,'stem_list':s}
    json.dump(out,open('kw_depth.json','w'),ensure_ascii=False)
print('done',len(out))

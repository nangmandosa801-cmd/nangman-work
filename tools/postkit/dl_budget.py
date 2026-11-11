# 수도권 매매 2026-08-01~오늘 새로 받기 (budget_map.py 가 씀) · python3 dl_budget.py [from] [to]
import sys,time,datetime
from dl import dl
fr=sys.argv[1] if len(sys.argv)>1 else '2026-08-01'
to=sys.argv[2] if len(sys.argv)>2 else datetime.date.today().isoformat()
for c,n in [('11000','서울특별시'),('41000','경기도'),('28000','인천광역시')]:
    for k in range(3):
        try: print(n,dl(c,n,'1',fr,to,f'rawBud/M_{c}_{fr}_{to}.csv'),flush=True); break
        except Exception as e: print('ERR',n,e,flush=True); time.sleep(10)
    time.sleep(2)

src=open('nm.py').read().split('def blog')[0]; exec(src)
import json,os
Q=['5억으로 살수있는 아파트','5억 아파트','6억 아파트','7억 아파트','8억 아파트','10억 아파트','3억 아파트','4억 아파트','예산 5억 아파트','5억대 아파트','6억대 아파트','7억대 아파트','신혼부부 아파트 예산','서울 5억 아파트','경기도 5억 아파트','5억 이하 아파트','6억 이하 아파트','9억 이하 아파트','15억 이하 아파트','내집마련 예산','아파트 살 때 예산','종잣돈 아파트','전세끼고 매매','갭투자 아파트','대출 끼고 아파트','아파트 대출 한도','생애최초 주택','신생아 특례대출','디딤돌 대출','보금자리론']
out=json.load(open('budget_ac.json')) if os.path.exists('budget_ac.json') else {}
for q in Q:
    if q in out: continue
    try: r=ac(q)
    except: r=[]
    out[q]=r; json.dump(out,open('budget_ac.json','w'),ensure_ascii=False)
print('done',len(out))

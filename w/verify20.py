src=open('nm.py').read().split('def blog')[0]; exec(src)
import json,os,re
ks=json.load(open('n20.json'))
extra=['중문 후회','중문 이전','중문 재설치','로봇청소기 문턱','로봇청소기 현관','중문 하자','중문 공동구매','자동중문 정전','중문 옵션','중문 유효폭','중문 설치 불가','중문 하부고시','망입유리','중문 접합유리','중문 실측','중문 계약 취소','중문 공사 순서','입주청소 중문','중문 문턱','중문 로봇청소기']
out=json.load(open('n20_ac.json')) if os.path.exists('n20_ac.json') else {}
for q in ks+extra:
    if q in out: continue
    try: r=ac(q)
    except: r=[]
    out[q]=r; json.dump(out,open('n20_ac.json','w'),ensure_ascii=False)
print('done',len(out))

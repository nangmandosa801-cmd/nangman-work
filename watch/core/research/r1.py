import json,subprocess,urllib.parse,re,sys
from concurrent.futures import ThreadPoolExecutor
def ac(q):
    u='https://ac.search.naver.com/nx/ac?'+urllib.parse.urlencode(dict(q=q,con=1,frm='nv',ans=2,r_format='json',r_enc='UTF-8',r_unicode=0,t_koreng=1,run=2,rev=4,q_enc='UTF-8',st=100))
    try: return [i[0] for i in json.loads(subprocess.run(['curl','-s','-m','10',u,'-A','Mozilla/5.0'],capture_output=True,text=True).stdout)['items'][0]]
    except Exception: return []
SEEDS={'견적비교':['인테리어 견적','인테리어 견적 비교','견적 비교','입주청소 견적','줄눈 견적','인테리어 견적서','견적서 보는법','인테리어 업체 고르는 법','인테리어 사기'],
 '샷시':['샷시 교체','샷시 교체 비용','아파트 샷시 교체','샷시 가격','샷시 교체 지원금','창호 교체','창호 교체 비용','하이샷시'],
 '도배':['도배 비용','아파트 도배 비용','도배 가격','도배 장판','도배 평당','실크벽지 합지벽지','도배 견적'],
 '입주청소':['입주청소','입주청소 가격','입주청소 비용','입주청소 평당','입주청소 업체','이사청소','이사청소 비용','입주청소 견적']}
out={}
for g,ss in SEEDS.items():
    with ThreadPoolExecutor(8) as ex: l1=dict(zip(ss,ex.map(ac,ss)))
    lv2=sorted({x for v in l1.values() for x in v}-set(ss))
    with ThreadPoolExecutor(8) as ex: l2=dict(zip(lv2,ex.map(ac,lv2)))
    out[g]={'l1':l1,'l2':l2}
json.dump(out,open('ac2.json','w'),ensure_ascii=False,indent=1)
for g,v in out.items():
    allw=set(x for vv in v['l1'].values() for x in vv)|set(x for vv in v['l2'].values() for x in vv)
    print(f'## {g}: L1 {sum(len(x) for x in v["l1"].values())} · 고유 {len(allw)}')
    for k,s in v['l1'].items(): print(' ',k,'→',' · '.join(s))

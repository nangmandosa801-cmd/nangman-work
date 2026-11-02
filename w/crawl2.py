src=open('nm.py').read().split('def blog')[0]; exec(src)
import json,time,os
base=json.load(open('jm_ac.json'))
terms=sorted(set(x for v in base.values() for x in v if '중문' in x or '양개' in x or '도어' in x))
terms=[t for t in terms if not any(k in t for k in ['관광','아기랑','제주','산책로','흑돼지'])]
extra=['중문 '+c for c in '가나다라마바사아자차카타파하']+['현관 중문 '+c for c in '가나다마바사아자차']+['아파트 중문','현관문 중문','중문 없는','신축 중문','구축 중문','중문 리모델링','중문 인테리어','중문 고장','중문 소리','중문 삐걱','중문 틈','중문 바람','중문 겨울','중문 청소','중문 먼지','중문 결로','중문 스티커','중문 커튼','중문 블라인드','중문 방충망','중문 펫도어','중문 높이','중문 폭','중문 규격','중문 견적','중문 as','중문 하자','중문 철거','중문 이사','중문 중고','중문 당근']
out=json.load(open('jm_ac2.json')) if os.path.exists('jm_ac2.json') else {}
for q in terms+extra:
    if q in out: continue
    try: r=ac(q)
    except: r=[]
    out[q]=r
    json.dump(out,open('jm_ac2.json','w'),ensure_ascii=False)
print('done',len(out))

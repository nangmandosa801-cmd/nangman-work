src=open('nm.py').read().split('def blog')[0]; exec(src)
import json,os
Q=['로봇청소기 문턱','망입유리','인테리어 후회','리모델링 후회','인테리어 실패','샷시 후기','도배 후기','욕실 리모델링 후기','인테리어 비용 30평','30평 샷시 가격','24평 인테리어','아파트 전체 인테리어 비용','인테리어 순서 체크리스트','입주청소','입주청소 비용','이사 청소','새집증후군','베이크아웃','인테리어 기간','반셀프 인테리어','셀프 인테리어','인테리어 앱','인테리어 견적서 양식','인테리어 감리','하자보수 청구','아파트 하자','누수 책임','결로 곰팡이','겨울 준비 집','난방 텐트','뽁뽁이','문풍지','방풍비닐','단열재','단열 공사','외벽 단열','베란다 단열','확장 단열','우풍 벽지','층간소음 매트']
out=json.load(open('click_ac.json')) if os.path.exists('click_ac.json') else {}
for q in Q:
    if q in out: continue
    try: r=ac(q)
    except: r=[]
    out[q]=r; json.dump(out,open('click_ac.json','w'),ensure_ascii=False)
print('done',len(out))

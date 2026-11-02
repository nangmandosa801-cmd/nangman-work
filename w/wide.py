import json, urllib.parse, urllib.request, pickle, os
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def ac(w):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(w)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0'
       '&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=8) as r:
            return [i[0] for i in json.loads(r.read().decode('utf-8')).get('items',[[]])[0]]
    except Exception: return None
G={
'연봉·이직':['연봉 실수령액','퇴직금 계산','이직 준비','대기업 연봉','공무원 봉급표'],
'정부지원금':['소상공인 지원금','청년 지원금','정부지원금 신청','근로장려금','출산 지원금'],
'사업자 세무':['사업자등록 절차','부가세 신고','종합소득세 신고','간이과세자 기준','세금계산서 발행'],
'4대보험·노무':['4대보험 계산기','퇴직금 지급기한','주휴수당 계산','근로계약서 양식','실업급여 조건'],
'실버타운·요양':['실버타운 비용','요양원 비용','요양병원 비용','장기요양등급','주야간보호센터'],
'육아·출산':['산후조리원 비용','어린이집 대기','유치원 비용','아이 보험','출산 준비물'],
'결혼':['스드메 비용','예식장 비용','신혼여행 비용','예단 비용','결혼 준비 순서'],
'자동차 유지':['자동차 보험료 할증','엔진오일 교환주기','타이어 교체 비용','차량 정기검사'],
'통신·구독':['휴대폰 요금제 비교','인터넷 결합할인','알뜰폰 요금제','OTT 요금'],
'반려동물':['강아지 분양가','펫호텔 비용','강아지 사료 추천','동물병원 진료비'],
'헬스·다이어트':['헬스장 가격','PT 가격','다이어트 한약','단백질 보충제'],
'취미 장비':['자전거 입문','등산화 추천','캠핑 장비','낚시 입문','드론 자격증'],
'전자제품':['에어컨 전기요금','건조기 추천','로봇청소기 추천','노트북 추천'],
'식자재·외식':['배달비 비교','밀키트 추천','정육 도매','식자재 마트'],
'이민·해외':['워킹홀리데이 비용','해외이사 비용','유학 비용','영주권 조건'],
'중고거래':['당근마켓 사기','중고 명품 감정','리셀 시세','중고 거래 세금'],
'에너지':['태양광 설치 비용','전기차 충전 요금','보일러 교체 비용','단열 공사 비용'],
'법률 분쟁':['임대차 분쟁','소액소송 절차','내용증명 작성','명도소송 비용'],
'상속·증여':['상속세 계산','상속 포기 절차','유류분','가족간 계좌이체'],
'농지·귀촌':['농지연금','농지 취득자격증명','농막 규제','귀촌 지원'],
}
allw=[w for v in G.values() for w in v]
with ThreadPoolExecutor(32) as ex: r=dict(zip(allw, ex.map(ac,allw)))
pickle.dump((G,r),open('wide.pkl','wb'))
sc=[]
for g,ws in G.items():
    live=sum(1 for w in ws if r.get(w)); depth=sum(len(r.get(w) or []) for w in ws)
    sc.append((depth,live,g,ws))
sc.sort(reverse=True)
for depth,live,g,ws in sc:
    print('\n■ %-12s 살아있는 말 %d/%d   제안어 %d' % (g,live,len(ws),depth))
    for w in ws:
        v=r.get(w)
        print('   %-18s %s' % (w, (' / '.join(v[:4]) if v else '— 없음')))

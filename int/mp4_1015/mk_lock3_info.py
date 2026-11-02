import sys; sys.path.insert(0,'/home/claude/int/mp4_1015')
import clipinfo,re
L='https://blog.naver.com/champion_chart'
items=[
('door_gaemun_biyong','도어락 개문','도어락 개문 3만원부터, 부수지 않고 엽니다. 서울 어디든 출장 #도어락개문비용 #도어락개문 #도어락교체 #출장열쇠 #낭만인테리어','도어락','10/29(목) 10:00','도어락 개문 비용, 3만원부터인데 부수고 열면 문값이 붙습니다',['도어락 개문 3만원부터','과하게 크게 뚫은 문','너무 조여 부러진 나사','날카롭게 잘린 타공 면','그라인더로 뚫은 문','문의 010-2882-8165']),
('yurimun_beonhoki','유리문 번호키','유리문 번호키 15만원부터, 얇은 샷시문은 슬림형으로 답니다 #유리문번호키 #상가번호키 #샷시문번호키 #슬림번호키 #낭만인테리어','유리문','10/31(토) 10:00','유리문 번호키, 얇은 상가 샷시문은 전용 슬림형으로 답니다',['유리문 번호키 15만원부터','검은 틀 문에 검은 몸체','얇은 샷시문 한강로 상가','위아래로 잠기는 구조 그대로','번호키 가까이 유리는 그대로','제작 유리문 힌지도 같은 날','문의 010-2882-8165']),
('floor_hinge','플로어 힌지 교체','플로어 힌지 교체, 하우징이 멀쩡하면 바닥을 깨지 않고 몸통만 바꿉니다 #플로어힌지교체 #플로어힌지 #유리문힌지 #문처짐 #낭만인테리어','유리문','11/1(일) 10:00','플로어 힌지 교체 비용, 하우징을 살리면 바닥을 깨지 않습니다',['플로어 힌지 몸통만 교체','하우징은 그대로 둡니다','같은 규격 새 힌지 몸통','바닥을 깨지 않습니다','문이 처지면 사진 한 장','문의 010-2882-8165'])]
bad=['값','자리','어요','예요','고요','최고','프리미엄','기준','헷갈','갈']
for slug,name,cap,what,when,title,sc in items:
    for w in bad:
        for t in cap.split():
            if w=='갈' and t.lstrip('#').startswith('갈'): raise SystemExit('갈 '+t)
            if w!='갈' and w in t: raise SystemExit(w+' '+t)
    clipinfo.make(slug,name,cap,L,title,what,sc,'시공 사진은 제휴 업체 「서울 24시 출장 열쇠」 블로그 사진 · 출처를 화면에 표기(사진 구석 · 하단 띠)')
    p=f'/mnt/user-data/outputs/int/clip_sigong/nangman_interior_{slug}_clip_info.txt'; t=open(p).read()
    t=t.replace('연결할 글\n','연결할 글 (글 발행 뒤 주소로 바꿀 것 · 발행 예정 %s · %s)\n'%(when,title),1)
    t=t.replace('[ 장면 ]','첫 화면 문구\n'+sc[0].replace('\n',' ')+'\n\n[ 장면 ]',1)
    open(p,'w').write(t)
    print(slug,len(cap),cap.count('#'))

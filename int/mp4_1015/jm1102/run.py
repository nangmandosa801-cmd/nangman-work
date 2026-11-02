import sys,os
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/int/mp4_1015')
import land,mk
D='/home/claude/int/mp4_1015/jm1102/'
outs=[]
land.text_slide(D+'s0.jpg','신규 입주 아파트 · 일반 시공','3연동 65만원부터\n원슬라이딩 55만원','스윙폴딩 83만원부터')
outs.append(D+'s0.jpg')
sl=[('p01.png',"3연동 65만원\n아치형 유리","강화유리 · 국내산 자재"),
('p02.png',"원슬라이딩\n55만원부터","옆 벽이 비어 있는 현관"),
('p03.png',"옵션 3연동\n121만~180만원","따로 달면 56만원 넘게 낮음"),
('p05.png',"불소도장\n알루미늄 틀","색이 잘 바래지 않음"),
('p07.png',"2년 무상 A/S\n맞춤 제작","집마다 치수를 재서 제작")]
for i,(f,l,s) in enumerate(sl,1):
    o=D+f's{i}.jpg'; land.slide(D+f,l,s,o); outs.append(o)
land.ask(D+'s9.jpg',["신축아파트 중문","박람회 전에 가격 보기"],'현관'); outs.append(D+'s9.jpg')
mk.make(outs,D+'nangman_interior_sinchuk_jungmun_long.mp4',seed=11); print('ok')

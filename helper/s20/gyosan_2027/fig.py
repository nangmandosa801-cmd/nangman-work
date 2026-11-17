import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars
bars('img/nangman_gyosan_2027_rise.png', '사전청약 뒤 본청약 분양가, 교산 A2는 17% 올랐습니다',
     [('인천계양|59㎡', 39.5, '39%', False), ('남양주왕숙2 A3|84㎡', 30.4, '30%', False), ('고양창릉 S1|84㎡', 21.9, '22%', False), ('하남교산 A2|59㎡', 16.7, '17%', True)],
     sub='3기 신도시 사전청약 추정 분양가에서 본청약까지 오른 비율',
     note='자료: 파이낸셜뉴스(11월 14일) · 교산 A2는 하남일보 · LH 모집공고')
print('ok')

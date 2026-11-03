src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from thumbnail import render_listing
hbar([('도로가 붙은 땅',3.7,'14건'),('도로 없음 · 미기재',1.0,'66건'),('이곡리 산 105 (호가)',4.0,'6m 임도')],['이곡리 산 105 (호가)'],
     '지산드림 · 1만 평 넘는 가평 임야 실거래 80건과 비교','이곡리 산 105 평당 4만원, 도로 붙은 큰 산 중간값은 3.7만원입니다',
     'jisandream_igok105_fig1.png','국토교통부 토지 실거래 · 가평군 임야 1만 평 이상 · 2023년 1월~2026년 8월 · 지분·해제 제외',5.4)
render_listing('가평 산 매매 · 북면 이곡리 임야','임업인 3ha 면적 기준을 넘는','4.5ha','임야 13,679평','농림지역 · 임업용산지 · 6m 임도 · 계곡','총 5억 4,700만원',O+'jisandream_igok105_thumb.png')
print('ok')

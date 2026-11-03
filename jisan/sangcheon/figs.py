src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from thumbnail import render_listing
import os
O='/mnt/user-data/outputs/jisandream/sangcheon/'; os.makedirs(O,exist_ok=True)
hbar([('청평면 큰 산 · 길 없음',1.0,'9건 · 평당 중앙값'),('청평면 큰 산 · 길 붙음',1.9,'상천리 2건'),('상천리 이 매물 (매도가)',7.8,'6m 아스콘 길 · 전기'),('보전관리 산 · 4천 평대',14.0,'상천리 · 하천리 2건')],['상천리 이 매물 (매도가)'],
     '지산드림 · 가평임야가격, 청평면 산 실거래와 비교','상천리 4만 평 평당 7.8만원, 길 붙은 큰 산 실거래는 1.9만원입니다',
     'jisandream_sangcheon_fig1.png','국토부 토지 실거래 · 청평면 임야 · 2023.1~2026.8 · 지분·해제 제외 · 이 매물은 매도가',16)
render_listing('가평 토지 매물 · 청평 상천리 임야','산에 이미 들어와 있는','6m 아스콘 길·전기','임야 40,939평 · 9필지','농림 · 일부 보전관리 · 계곡 앞','총 32억원',O+'jisandream_sangcheon_thumb.png')
print('figs ok')

src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
O='/mnt/user-data/outputs/jisandream/hwesonji/'
hbar([('2015년까지 지음',418,'정비사업 시기 조건 안'),('2016년 지음',48,'3월 30일 전후 대장 확인'),('2017년 뒤 지음',135,'정비사업에 못 넣음')],['2015년까지 지음'],
     '지산드림 · 훼손지정비사업 조건, 남양주 그린벨트 축사','지은 해가 적힌 601건 가운데 418건이 2015년까지 지은 건물입니다',
     '../hwesonji/jisandream_hwesonji_fig1.png','국토부 공장·창고 실거래 · 남양주 개발제한구역 동물·식물 시설 · 2010.1~2026.8',480,unit='건',fmt='{:.0f}')
render_jisan('지산드림 · 그린벨트 창고',['훼손지정비사업 뜻','축사 땅 1만㎡ 모아 30% 공원'],'남은 땅에 물류창고 · 2016.3.30 전 시설만',O+'jisandream_hwesonji_thumb.png')
print('ok')

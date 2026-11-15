# -*- coding: utf-8 -*-
# 11/16~11/22 지산드림 일주일치 그림: 01 썸네일 · 02 · 03 · 06 배너 → /mnt/user-data/outputs/jisandream/<폴더>/img/
import os,sys
exec(open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0])
exec(open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0].split("GRN=")[1].join(["GRN=",""]) if False else open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0])
sys.path.insert(0,'/home/claude/jisan/photo'); from kwphoto import thumb
cwd=os.getcwd(); os.chdir('/home/claude/jisan/choi')
exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
os.chdir(cwd)
exec(open('/home/claude/jisan/two_figs.py').read().split("for s in ['maedo'")[0])
_head=head
def head(f,a,b): _head(f,b,a)
OUT='/mnt/user-data/outputs/jisandream/'
def P(f): d=OUT+f+'/img/'; os.makedirs(d,exist_ok=True); return d
def J(src,dst): Image.open(src).convert('RGB').save(dst,quality=92)
def ban(f,big,l1,l2):
    global H; _h=H; H='/mnt/user-data/outputs/jisandream/hwesonji/'
    d=P(f); banners(d,'tmp',big,l1,l2,'지산드림'); H=_h; J(d+'jisandream_tmp_banner.png',d+'06.jpg')
    for x in ['jisandream_tmp_banner.png','jisandream_tmp_banner_small.png']:
        try: os.remove(d+x)
        except: pass
def card(lines,title,sub,note,out):
    fig,ax=plt.subplots(figsize=(10.6,5.4)); fig.subplots_adjust(bottom=0.13,top=0.77,left=0.05,right=0.95)
    ax.set_xlim(0,10); ax.set_ylim(0,len(lines)); ax.set_axis_off()
    for i,(a,b) in enumerate(lines):
        y=len(lines)-1-i+0.5
        ax.text(0.3,y,a,fontsize=26,color=CYAN,fontproperties=FB,va='center'); ax.text(1.3,y,b,fontsize=21,color=DEEP,fontproperties=FB,va='center')
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
TMP='/tmp/wk_'
SANG='/mnt/user-data/outputs/jisandream/sangga/'
ph1=Image.open(SANG+'jisandream_sangga_upjong_photo1.png').convert('RGB').crop((40,172,1040,1155))
ph2=Image.open(SANG+'jisandream_sangga_upjong_photo2.png').convert('RGB').crop((40,172,1040,1155))
hanam,_=basemap(37.585,127.13,37.49,127.26,13)

# 1 토허 해제
d=P('toheo')
hbar([('11월 2일까지',70.14,GREY,'70.14㎢'),('11월 3일부터',7.17,CYAN,'7.17㎢ · 감북 · 감일 · 미사 일원')],95,
 '하남 토지거래허가구역, 열에 아홉이 풀렸습니다','하남 그린벨트 토지거래허가구역 넓이','경기도 2026.11.3 발표 · 기간 2029.11.2까지',TMP+'1a.png',h=4.4); J(TMP+'1a.png',d+'02.jpg')
hbar([('풀린 동네',1665,CYAN,'1,665건 (82%)'),('남은 세 동',359,GREY,'359건 (감북 · 감일 · 미사)')],2300,
 '하남 땅 거래 열에 여덟은 이제 허가 없이','2025.1~2026.8 하남 땅 거래 2,024건','국토교통부 토지 실거래 · 해제 거래 빼고 · 남은 세 동은 일원이라 일부 필지만',TMP+'1b.png',h=4.4); J(TMP+'1b.png',d+'03.jpg')
thumb([hanam],'지산드림 · 하남 토지거래허가','하남 땅 허가','70㎢ → 7㎢','11월 3일부터 · 감북 · 감일 · 미사만 남음',d+'01.jpg')
ban('toheo','하남 토지거래허가 해제','70㎢ → 7㎢ · 감북 · 감일 · 미사만','내 땅이 남았는지 지번으로 봐 드립니다')

# 2 김밥집
d=P('gimbap'); J_=lambda im,p: im.save(p,quality=92)
J_(ph1,d+'02.jpg'); J_(ph2,d+'03.jpg')
thumb([ph1],'지산드림 · 김밥집 창업 비용','가산 1층 11평','권리금 없음','보증금 3천 · 월세 200만원 · 바로 입주',d+'01.jpg')
ban('gimbap','김밥집 창업 비용','가산 1층 11평 · 권리금 없음','보증금 3천 · 월 200만원 · 바로 입주')

# 3 하남 땅값
d=P('ttangap')
hbar([('그린벨트 밭 · 논',219,CYAN,'219만원 (157필지)'),('그린벨트 산',40,GREY,'40만원 (77필지)'),('집 지을 땅 (대)',1190,GOLD,'1,190만원 (69필지)')],1550,
 '하남 땅, 종류에 따라 평당 30배','하남 땅 평당 중앙값 · 통째 거래','국토교통부 토지 실거래 · 2025.1~2026.8 · 지분 빼고',TMP+'3a.png',h=5.0); J(TMP+'3a.png',d+'02.jpg')
hbar([('길에 붙은 밭',270,CYAN,'270만원 (78필지)'),('길이 없는 밭',195,GREY,'195만원 (79필지)')],360,
 '하남 그린벨트 밭, 길 하나로 평당 75만원','그린벨트 밭 · 논 평당 중앙값','국토교통부 토지 실거래 · 2025.1~2026.8 · 지분 빼고',TMP+'3b.png',h=4.4); J(TMP+'3b.png',d+'03.jpg')
thumb([hanam],'지산드림 · 하남 땅값','그린벨트 밭','평당 219만원','산 40만 · 집 지을 땅 1,190만 · 동네별 표',d+'01.jpg')
ban('ttangap','하남 땅값','밭 219만 · 산 40만 · 집터 1,190만','내 땅 하나만의 시세표를 드립니다')

# 4 지산 상가
d=P('jsangga')
hbar([('전용 (쓰는 칸)',11.43,CYAN,'11.43평 · 평당 월 17만 5천원'),('공급 (전용+공용)',16.30,GREY,'16.30평 · 12만 3천원'),('분양 (계약서)',22.61,GREY,'22.61평 · 8만 8천원')],34,
 '같은 월세 200만원, 평당은 두 배 차이','가산 1층 105호 면적과 평당 월세','하우스디 가산 퍼스타 105호 분양계약서 · 관리비 · 부가세 빼고',TMP+'4a.png',h=5.0); J(TMP+'4a.png',d+'02.jpg')
J_(ph2,d+'03.jpg')
thumb([ph1],'지산드림 · 지식산업센터 상가','전용으로 따지면','평당 17만 5천원','가산 1층 105호 · 월세 200만원 · 분양 22.61평',d+'01.jpg')
ban('jsangga','지식산업센터 상가 임대','가산 1층 전용 11.43평 · 코너 통창','보증금 3천 · 월 200만원 · 바로 입주')

# 5 비사업용 양도세
d=P('ybisaeop')
hbar([('농사 지은 땅',7734,CYAN,'7,734만원'),('비사업용 (지금)',10347,GREY,'1억 347만원'),('비사업용 (2028 개정안)',16787,GOLD,'1억 6,787만원')],23000,
 '같은 하남 밭, 2028년엔 세금 1.6배','10년 전 2억 → 지금 5억 · 양도세 + 지방소득세','가정: 보유 10년 · 경비 0 · 기본공제 250만 · 2028은 정부 2026.8.3 개편안',TMP+'5a.png',left=0.33,h=5.0); J(TMP+'5a.png',d+'02.jpg')
card([('1','팔기 전 5년 중 3년 넘게 직접 농사'),('2','팔기 전 3년 중 2년 넘게 직접 농사'),('3','가진 기간의 60% 넘게 직접 농사')],
 '하나라도 맞으면 사업용 밭','비사업용토지 양도세 · 기간 기준','소득세법 시행령 168조의6 · 땅 가까이 살면서 직접 농사',TMP+'5b.png'); J(TMP+'5b.png',d+'03.jpg')
thumb([hanam],'지산드림 · 비사업용토지 양도세','하남 밭 세금','2028년 1.6배','같은 밭 3억 차익 · 1억 347만 → 1억 6,787만',d+'01.jpg')
ban('ybisaeop','비사업용토지 양도세','2028년부터 하남 밭 세금 1.6배','파는 해 정하기 전 세금 셈부터')

# 6 초일동
d=P('choil')
hbar([('초일동',78,CYAN,'78%'),('창우동',77,GREY,'77%'),('상산곡동',61,GREY,'61%'),('초이동',34,GREY,'34%'),('하남 전체',26,GOLD,'26%')],100,
 '초일동 땅은 열에 여덟이 통째로 팔립니다','2025.1~2026.8 거래 중 통째 비율','국토교통부 토지 실거래 · 지분 표시 없는 거래',TMP+'6a.png',h=5.6); J(TMP+'6a.png',d+'02.jpg')
hbar([('2020년',271,GREY,'271만원 (8필지)'),('2024년',320,GREY,'320만원 (3필지)'),('2025년',270,CYAN,'270만원 (10필지)'),('2026년 1~8월',216,GREY,'216만원 (9필지)')],420,
 '초일동 논밭, 길 붙은 땅 270만원이 기준','그린벨트 논밭 · 통째 · 100~1,000평 · 평당 중앙값','국토교통부 토지 실거래 · 한 해 10필지 안팎이라 오르내림이 큼',TMP+'6b.png',h=5.2); J(TMP+'6b.png',d+'03.jpg')
m,_=basemap(37.545,127.135,37.505,127.195,15)
thumb([m],'지산드림 · 하남땅가격 · 초일동','초일동 논','평당 270만원','열에 여덟이 통째 · 감일2 옆 · 허가는 풀림',d+'01.jpg')
ban('choil','하남땅가격 · 초일동','그린벨트 논 평당 270만원','열에 여덟이 통째로 팔리는 동네')

# 7 상산곡동
d=P('sangsan')
hbar([('2019년',115,GREY,'115만원'),('2020년',115,GREY,'115만원'),('2021년',192,GREY,'192만원'),('2024년',250,GREY,'250만원 (7필지)'),('2025년',190,CYAN,'190만원')],330,
 '상산곡동 밭, 5년 동안 1.7배','그린벨트 밭 · 논 · 통째 · 100~1,000평 · 평당 중앙값','국토교통부 토지 실거래',TMP+'7a.png',h=5.6); J(TMP+'7a.png',d+'02.jpg')
hbar([('그린벨트',24,CYAN,'24건'),('제1종일반주거',16,GOLD,'16건 · 마을 안 집 지을 땅'),('자연녹지',4,GREY,'4건')],38,
 '상산곡동은 마을 안 땅도 팔립니다','2025.1~2026.8 상산곡동 땅 거래 · 용도지역별','국토교통부 토지 실거래 · 마을 안 대 평당 839만원',TMP+'7b.png',h=4.8); J(TMP+'7b.png',d+'03.jpg')
m,_=basemap(37.535,127.195,37.495,127.255,15)
thumb([m],'지산드림 · 하남 밭 땅값 · 상산곡동','상산곡동 밭','평당 188만원','검단산 아래 · 한 필지 284평 · 허가 없이 거래',d+'01.jpg')
ban('sangsan','하남 밭 땅값 · 상산곡동','그린벨트 밭 평당 188만원','넓은 밭도 마을 안 땅도 봐 드립니다')
print('ok')

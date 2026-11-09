src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image
import os,shutil
GOLD='#C9962E'
def hbar(rows,xmax,title,sub,note,out,left=0.30,h=5.6):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.13,top=0.77,left=left,right=0.93); n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off(); head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
for s in ['maedo','saneunbeop']: os.makedirs('/mnt/user-data/outputs/jisandream/%s/img'%s,exist_ok=True)
M='/mnt/user-data/outputs/jisandream/maedo/img/'; S='/mnt/user-data/outputs/jisandream/saneunbeop/img/'
D=[('배알미동',110,'5필지'),('춘궁동',185,'12필지'),('상산곡동',188,'12필지'),('초이동',214,'22필지'),('초일동',270,'19필지'),('창우동',318,'8필지'),('감북동',426,'6필지'),('감일동',619,'4필지')]
hbar([(a,v,CYAN,'%d만원 (%s)'%(v,n)) for a,v,n in D]+[('하남 전체',240,GOLD,'240만원 (98필지)')],800,
 '지산드림 · 토지 매도 · 하남','그린벨트 밭 · 논 동네별 평당 중앙값','국토교통부 토지 실거래 · 2025.1~2026.8 · 통째 거래 · 100~1,000평','/tmp/m2.png',h=7.4)
hbar([('3억원에 팔면',270,CYAN,'270만원 이내'),('5억원에 팔면',450,GOLD,'450만원 이내'),('10억원에 팔면',900,CYAN,'900만원 이내')],1150,
 '지산드림 · 토지 매매 수수료','상한 0.9% · 부가세 따로 · 중개사와 협의','공인중개사법 시행규칙 · 주택 외 거래 0.9% 이내','/tmp/m3.png',h=4.8)
hbar([('2024년',71,CYAN,'71% (773건 중 549건)'),('2025년',76,GOLD,'76% (1,303건 중 984건)'),('2026년 1~8월',72,CYAN,'72% (721건 중 522건)')],115,
 '지산드림 · 하남 땅 사는법','하남 땅 거래 가운데 지분 거래 비율','국토교통부 토지 실거래 · 해제 거래 빼고 · 지분 표시 기준','/tmp/s2.png',h=4.8)
hbar([('도로에 붙은 땅',270,GOLD,'270만원 (57필지)'),('길이 없는 땅',163,GREY,'163만원 (41필지)')],380,
 '지산드림 · 하남 땅 사는법','그린벨트 밭 · 논 평당 중앙값 · 길 유무','국토교통부 토지 실거래 · 2025.1~2026.8 · 통째 · 100~1,000평','/tmp/s3.png',h=4.8)
for a,b in [('/tmp/m2.png',M+'02.jpg'),('/tmp/m3.png',M+'03.jpg'),('/tmp/s2.png',S+'02.jpg'),('/tmp/s3.png',S+'03.jpg')]:
    Image.open(a).convert('RGB').save(b,quality=92)
ban='/mnt/user-data/outputs/jisandream/hwesonji/jisandream_hwesonji_banner.png'
for d in [M,S]: Image.open(ban).convert('RGB').save(d+'06.jpg',quality=92)
print('ok')

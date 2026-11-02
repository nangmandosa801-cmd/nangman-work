# 낭만 인테리어 숏폼 — 10/10 발행 5편 + 10/11 00:12 강아지 매트 추천 (10/11 02:04 사용자 「어제 발행한 글들 mp4 info 만들자」)
# 틀(10/9 23:00): 메시지 하나 · 장면 3개 · 10초 안팎 · 사람 자리는 너구리 · 반려동물 글은 강아지
# 숫자와 문장은 v2src/t1010/*.txt(발행 글 본문)에서만
import sys,os,subprocess,shutil; sys.path.insert(0,'/home/claude')
import clipgen, bgm
from clipgen import *
from comic import racc, cdog
FACE={'o':'happy','smile':'happy','worry':'worry','shock':'shock'}
clipgen.person=lambda d,x,y,s=1.0,face='o',shirt=None,**k: racc(d,x,y-int(20*s),s*0.8,face=FACE.get(face,face))
out=[]; ONLY=sys.argv[1:]
def go(slug,scenes,durs,cover,info,seed):
    if ONLY and slug not in ONLY: return
    od='/mnt/user-data/outputs/int/clip_'+slug
    out.extend(make('int',slug,scenes,durs,cover,info,od))
    if os.environ.get('NOMP4'): return
    v=f'{od}/nangman_interior_{slug}_short.mp4'; S='/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad'
    w=bgm.make(f'{S}/bgm_{slug}.wav',sum(durs),seed=seed); src=f'{S}/{slug}_noaudio.mp4'; shutil.copy(v,src)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-i',w,'-filter:a','loudnorm=I=-16:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',v],check=True)
NI='#낭만인테리어'
B='https://blog.naver.com/champion_chart/'
END=lambda what: f'\n\n사는 지역과 연락처를 블로그 비밀댓글로 남겨 주시면 {what}을 연결해 드립니다.'


# 강아지 매트 추천 셋째 숏폼 — 강아지전용 vs 논슬립 (10/11 14:56 사용자 「다른 강아지 가자」 · 본문 v2src/t1010/int_mat_chucheon.txt 71~107줄)
go('gangaji_mat_nonslip',[
 ('comic',dict(lines=['반짝이는 타일 바닥','뛰다가 또 주르륵?!'],items=[('floor',1180,'tile'),('dog',540,930,1.0,'shock','sit'),('boom',820,480,'주르륵!',80),('bubble',80,1420,920,250,['슬개골 약한 아이는','바닥부터 바꿔!'])])),
 ('big',dict(lines=['슬개골이 약하면','논슬립 쪽'],num='논슬립',nsize=170,sub1='강아지전용 · 가격 낮고 우레탄 적음',sub2='논슬립 · 우레탄 많아 더 받쳐 줌',face='smile')),
 ('end',dict(lines=['강아지전용 vs 논슬립 차이'],sub=['블로그에서','확인하세요'],sub2='서울 번동 타일 집 사진은')),
],[3.6,3.4,3.4],1,dict(url=B+'224437536765',
 name='강아지 매트 추천 · 강아지전용 vs 논슬립',title='강아지 매트 추천, 같은 2.2cm라도 겉면 TPU와 속 우레탄 양이 달라서 샘플을 눌러 보고 고릅니다',
 cap='타일 바닥에서 자꾸 미끄러지는 강아지, 슬개골이 약하면 논슬립 매트를 많이 고릅니다.',
 tags5=['#강아지매트추천','#강아지논슬립매트','#강아지슬개골','#강아지미끄럼방지매트',NI],
 yt='강아지 매트 추천, 강아지전용과 논슬립 차이',
 desc='같은 시공팀에도 강아지 매트가 두 가지 있습니다. 강아지전용 매트와 논슬립 매트입니다.\n\n강아지전용 매트는 가격이 낮은 대신 우레탄이 덜 들어가 탄성이 조금 낮습니다.\n논슬립 매트는 가격이 꽤 높지만 우레탄이 많아 같은 2.2cm라도 받쳐 주는 힘이 다릅니다.\n\n강아지만 거실에서 노는 집이라면 강아지전용으로도 됩니다. 사람도 맨발로 오래 다니는 집, 슬개골이 약한 강아지가 사는 집은 논슬립 쪽을 많이 고릅니다.\n밝은 타일 바닥에서 강아지가 자꾸 미끄러지던 서울 번동 신축빌라도 여러 제품을 비교한 뒤 논슬립 2.2cm를 골랐습니다.'+'\n\n평수와 깔 곳을 비밀댓글로 남겨 주시면 몇 장 드는지 알려 드립니다.',
 tags10=['#강아지매트추천','#강아지논슬립매트','#강아지미끄럼방지매트','#강아지슬개골','#강아지슬개골매트','#강아지매트','#애견매트추천','#강아지매트추천가성비','#반려견매트',NI],
 scenes=['주르륵','논슬립','블로그에서 확인'],
 src='내용은 낭만 인테리어 「강아지 매트 추천」 글 · 두 매트 차이는 시공팀 설명'),seed=48)
print('\n'.join(out))

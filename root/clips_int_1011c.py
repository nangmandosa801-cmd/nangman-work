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


# 거실 매트 시공 글의 강아지 숏폼 — 강아지 발소리도 아래층으로 (10/11 15:00 사용자 「다른 거 꺼내」 · 본문 v2src/t1009/int_geosil_mat.txt 78~91줄)
go('gangaji_cheunggan',[
 ('comic',dict(lines=['소파에서 쿵!','아래층에 다 들려?!'],items=[('floor',1180,'tile'),('dog',540,930,1.0,'shock','sit'),('boom',820,480,'쿵!',110),('bubble',80,1420,920,250,['강아지 발소리도','아래층으로 간다구!'])])),
 ('big',dict(lines=['미끄럼 · 층간소음','한 번에'],num='겸용 매트',nsize=150,sub1='강아지 매트 + 층간소음매트 2.2cm 하나로',sub2='깔기 전 · 방문이 걸리지 않는지 보기',face='smile')),
 ('end',dict(lines=['강아지 층간소음 매트'],sub=['블로그에서','확인하세요'],sub2='시흥 배곧 집 사진은')),
],[3.6,3.4,3.4],1,dict(url=B+'224435602789',
 name='거실 매트 시공 · 강아지 발소리도 층간소음',title='거실 매트 시공, 아이 있는 집은 층간소음매트를 놀이매트 한 장이 아니라 주방과 복도까지 이어 깝니다',
 cap='강아지가 뛰고 뛰어내리는 소리도 아래층으로 갑니다. 미끄럼과 층간소음을 매트 하나로 줄입니다.',
 tags5=['#강아지층간소음','#강아지매트','#층간소음매트','#반려견층간소음',NI],
 yt='강아지 층간소음, 발소리도 아래층으로 갑니다',
 desc='강아지가 뛰고 소파에서 뛰어내리는 소리도 아이 발소리처럼 아래층으로 갑니다.\n\n시흥 배곧의 한 아파트는 강아지와 사는 집이라 강아지 매트와 층간소음매트를 겸하는 2.2cm 매트를 깔았습니다. 방 안까지 같은 매트로 이었습니다.\n\n매트를 깔면 발소리 충격을 줄이고 미끄러지는 바닥을 잡아 줍니다. 다만 아래층 소리를 모두 없애지는 못합니다.\n바닥이 2cm쯤 높아지니 방문이 매트에 걸리지 않는지 깔기 전에 꼭 보세요.'+'\n\n평수와 깔 곳을 비밀댓글로 남겨 주시면 몇 장 드는지 알려 드립니다.',
 tags10=['#강아지층간소음','#반려견층간소음','#층간소음매트','#층간소음매트시공','#강아지매트','#강아지매트시공','#거실매트시공','#반려견매트','#강아지미끄럼방지매트',NI],
 scenes=['쿵!','겸용 매트','블로그에서 확인'],
 src='내용은 낭만 인테리어 「거실 매트 시공」 글 · 사례는 매트 제휴 시공팀의 작업 기록'),seed=49)
print('\n'.join(out))

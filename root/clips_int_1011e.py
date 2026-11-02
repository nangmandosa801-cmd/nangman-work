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


# 강아지 매트 시공 글(224435609606) 여섯째 숏폼 — 몇 장 드나 (10/11 15:06 사용자 「발행했어」 · 본문 v2src/t1009/int_gangaji_mat.txt 110~120줄)
go('gangaji_mat_jangsu',[
 ('comic',dict(lines=['강아지 매트 시공','얼마예요?'],items=[('floor',1180,'tile'),('dog',540,930,1.0,'shock','sit'),('boom',820,480,'얼마?',90),('bubble',80,1420,920,250,['평당 얼마가 아니라','몇 장인지부터!'])])),
 ('big',dict(lines=['34평 거실부터 방까지'],num='110~120장',nsize=140,sub1='매트는 한 장씩 셉니다',sub2='장당 가격은 매트 종류에 따라 다릅니다',face='smile')),
 ('end',dict(lines=['강아지 매트 시공 가격'],sub=['블로그에서','확인하세요'],sub2='가격이 달라지는 네 가지는')),
],[3.6,3.4,3.4],1,dict(url=B+'224435609606',
 name='강아지 매트 시공 가격 · 34평 110~120장',title='강아지 매트 시공, 다리 수술을 두 번 한 강아지 집은 두께보다 발이 밀리지 않는 매트를 거실부터 복도까지 이어 깔았습니다',
 cap='강아지 매트 시공 가격은 몇 장 깔지부터 봅니다. 34평 거실부터 방까지 110~120장입니다.',
 tags5=['#강아지매트시공가격','#강아지매트시공비용','#강아지매트시공','#강아지매트',NI],
 yt='강아지 매트 시공 가격, 34평이면 몇 장?',
 desc='강아지 매트는 대개 한 장씩 셉니다.\n업체에 물어보니 34평 아파트를 거실부터 방까지 이어 깔면 110~120장이 든다고 합니다. 장당 가격은 매트 종류에 따라 다릅니다.\n\n가격이 달라지는 것은 네 가지입니다.\n깔 넓이(거실만인지, 주방 · 복도 · 방까지인지), 매트 종류(소재와 두께 · 표면 무늬), 집 상태(빈집인지, 살고 있는 집인지), 잘라 맞출 곳(문턱 · 기둥 · 붙박이장 둘레).\n\n그래서 강아지 매트 시공 비용은 서비스 수준과 매트 종류에 따라 천차만별입니다. 견적을 받을 때는 몇 장인지, 어디까지 까는지 같이 물어보세요.'+'\n\n평수와 깔 곳을 비밀댓글로 남겨 주시면 몇 장 드는지 알려 드립니다.',
 tags10=['#강아지매트시공가격','#강아지매트시공비용','#강아지매트시공','#강아지매트','#강아지미끄럼방지매트','#강아지논슬립매트','#강아지매트추천','#반려견매트시공','#강아지거실매트',NI],
 scenes=['얼마예요?','110~120장','블로그에서 확인'],
 src='내용은 낭만 인테리어 「강아지 매트 시공」 글 · 장 수는 업체에 물어본 것'),seed=51)
print('\n'.join(out))

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


# 강아지 매트 추천 둘째 숏폼 — 매트 색은 털 색부터 (10/11 13:25 사용자 「강아지 매트 시리즈 mp4 하나 더 발행하자」 · 본문 v2src/t1010/int_mat_chucheon.txt)
go('gangaji_mat_color',[
 ('comic',dict(lines=['새로 깐 흰 매트에','털이 다 보여?!'],items=[('floor',1180,'tile'),('dog',540,930,1.0,'shock','sit'),('boom',820,480,'헉!',100),('bubble',80,1420,920,250,['매트 색은','내 털 색 보고 골라!'])])),
 ('big',dict(lines=['매트 색은','털 색부터'],num='털 색',nsize=170,sub1='검은 털은 브라운 · 흰 털은 스톤화이트',sub2='마블아이보리 무늬는 털과 얼룩을 덜 드러냅니다',face='smile')),
 ('end',dict(lines=['강아지 매트 색 고르는 법'],sub=['블로그에서','확인하세요'],sub2='세 가지 색 시공 사진은')),
],[3.6,3.4,3.4],1,dict(url=B+'224437536765',
 name='강아지 매트 추천 · 매트 색은 털 색부터',title='강아지 매트 추천, 같은 2.2cm라도 겉면 TPU와 속 우레탄 양이 달라서 샘플을 눌러 보고 고릅니다',
 cap='흰 매트엔 검은 털, 브라운엔 흰 털이 보입니다. 강아지 매트 색은 털 색부터 보세요.',
 tags5=['#강아지매트추천','#강아지매트','#강아지바닥매트','#애견매트',NI],
 yt='강아지 매트 색, 털 색부터 보고 고릅니다',
 desc='강아지 매트 색을 고를 때는 우리 집 강아지 털 색부터 떠올려 보세요.\n\n흰 매트(스톤화이트)는 집이 밝고 넓어 보이는 대신 검은 털이 눈에 띕니다.\n브라운은 차분하고 생활 얼룩이 덜 보이지만 흰 털이 보입니다.\n대리석 무늬 마블아이보리는 무늬가 털과 얼룩을 덜 드러냅니다.\n\n고르기 전에 샘플을 우리 집 바닥과 강아지 털 옆에 놓아 보세요. 블로그 비밀댓글에 「샘플」이라고 남기시면 시공팀에 요청해 보내 드립니다.'+'\n\n평수와 깔 곳을 비밀댓글로 남겨 주시면 몇 장 드는지 알려 드립니다.',
 tags10=['#강아지매트추천','#강아지매트','#강아지바닥매트','#강아지매트색','#강아지논슬립매트','#애견매트추천','#반려견매트','#강아지매트시공','#펫매트',NI],
 scenes=['털이 다 보여','털 색','블로그에서 확인'],
 src='내용은 낭만 인테리어 「강아지 매트 추천」 글 · 색 설명은 그 글의 매트 색 표'),seed=47)
print('\n'.join(out))

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


# 강아지 매트 시공 글(224435609606)의 다섯째 숏폼 — 나이 든 강아지 (10/11 15:04 사용자 「다음거」 · 본문 v2src/t1009/int_gangaji_mat.txt 57~70줄 · 남양주 별내)
go('gangaji_noyeon',[
 ('comic',dict(lines=['나이 든 우리 강아지','마루에서 자꾸 미끌!'],items=[('floor',1180,'tile'),('dog',540,930,1.0,'shock','sit'),('boom',820,480,'미끌!',90),('bubble',80,1420,920,250,['다리에 힘이 빠지면','작은 미끄럼도 아파!'])])),
 ('big',dict(lines=['푹신함보다','붙잡는 힘'],num='실리콘',nsize=170,sub1='발이 닿을 때 붙잡아 덜 밀림',sub2='눌러서 조금 들어가고 바로 받쳐 주면 딱',face='smile')),
 ('end',dict(lines=['나이 든 강아지 매트'],sub=['블로그에서','확인하세요'],sub2='남양주 별내 집 사진은')),
],[3.6,3.4,3.4],1,dict(url=B+'224435609606',
 name='강아지 매트 시공 · 나이 든 강아지는 붙잡는 힘',title='강아지 매트 시공, 다리 수술을 두 번 한 강아지 집은 두께보다 발이 밀리지 않는 매트를 거실부터 복도까지 이어 깔았습니다',
 cap='나이 든 강아지가 마루에서 자꾸 미끄러진다면, 푹신함보다 발을 붙잡는 매트를 고르세요.',
 tags5=['#노견매트','#강아지슬개골매트','#강아지미끄럼방지매트','#강아지매트시공',NI],
 yt='나이 든 강아지 매트, 푹신함보다 붙잡는 힘',
 desc='남양주 별내의 한 아파트. 나뭇결 마루 위에서 나이 든 강아지가 거실을 뛰다 자꾸 미끄러졌습니다.\n다리에 힘이 빠지는 나이라 작은 미끄러짐도 관절에 부담이 됩니다.\n\n이 집에는 실리콘으로 된 2.2T 논슬립 매트를 깔았습니다. 실리콘은 발이 닿을 때 붙잡는 힘이 커서 밀리는 느낌이 덜합니다.\n\n푹신한 것만 찾으면 곤란합니다. 너무 푹 꺼지는 매트는 발이 빠졌다가 올라오면서 오히려 균형을 잡기 어렵습니다. 손으로 눌렀을 때 조금 들어가고 바로 받쳐 주는 정도가 맞습니다.'+'\n\n평수와 깔 곳을 비밀댓글로 남겨 주시면 몇 장 드는지 알려 드립니다.',
 tags10=['#노견매트','#강아지슬개골매트','#강아지미끄럼방지매트','#강아지논슬립매트','#강아지매트시공','#강아지매트추천','#노견미끄럼방지','#반려견매트','#강아지거실매트',NI],
 scenes=['미끌!','실리콘','블로그에서 확인'],
 src='내용은 낭만 인테리어 「강아지 매트 시공」 글 · 사례는 제휴 업체의 작업 기록'),seed=50)
print('\n'.join(out))

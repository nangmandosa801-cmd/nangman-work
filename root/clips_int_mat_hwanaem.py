# 낭만 인테리어 숏폼 — 매트가 없어서 화난 강아지와 고양이 (2026.10.9 22:30 사용자 「강아지 매트가 없어서 강아지도 화내고 고양이도 화내는 거 만들어도 재밌을 듯」)
# 사실은 발행 글 「강아지 매트 시공」(224435609606)과 써 둔 「고양이 매트 두께」 글에서만: 2.2cm · 강아지 둘 · 고양이 셋이 한 매트(아산) · 캣타워 아래만 깔면 내려와 달리는 길은 다시 마루
import sys,os,subprocess,shutil; sys.path.insert(0,'/home/claude')
import clipgen, bgm
from clipgen import *
from comic import cdog
FACE={'o':'happy','smile':'happy','worry':'worry','shock':'shock'}
clipgen.person=lambda d,x,y,s=1.0,face='o',shirt=None,**k: cdog(d,x,y-int(20*s),s*0.8,face=FACE.get(face,face))
slug='mat_hwanaem'; od='/mnt/user-data/outputs/int/clip_'+slug
U='https://blog.naver.com/champion_chart/224435609606'
durs=[3.6,3.6,3.6,3.8,3.6,3.2]
out=make('int',slug,[
 ('comic',dict(lines=['우리 집 바닥 회의','긴급 소집!'],items=[('floor',1180,'tile'),('dog',300,880,0.9,'angry','sit'),('cat',780,880,0.9,'angry','sit'),('bubble',80,1450,920,230,['매트 언제','깔아 줄 거야!'])])),
 ('comic',dict(lines=['강아지의 주장','간식 주우러 가다가'],items=[('floor',1180,'tile'),('dog',620,930,1.0,'dizzy','slip'),('boom',850,560,'꽈당!',72),('speed',420,960,3,140),('bubble',80,1480,920,220,['마루에서 또 미끌','화난다멍!'])])),
 ('comic',dict(lines=['고양이의 주장','캣타워에서 내려왔더니'],items=[('floor',1180,'tile'),('tower',230,1180,0.8),('cat',720,930,0.95,'shock','slip'),('boom',880,560,'미끌!',72),('bubble',80,1480,920,220,['내려오면','다시 마루다냥!'])])),
 ('comic',dict(lines=['둘이 손잡고','파업 선언!'],items=[('floor',1180,'tile'),('box',380,1030,1.6,'매트 줘'),('dog',240,860,0.75,'angry','sit'),('cat',840,860,0.75,'angry','sit'),('bubble',80,1450,920,230,['산책 거부멍!','꾹꾹이 거부냥!'])])),
 ('comic',dict(lines=['거실부터 복도까지','2.2cm 매트를 깔았더니'],items=[('floor',1180,'mat'),('dog',320,930,0.85,'happy','run'),('cat',770,930,0.85,'love','run'),('star',540,560,34),('star',880,520,26),('bubble',80,1480,920,220,['이제야','말이 통하네!'])])),
 ('end',dict(lines=['강아지 · 고양이 매트'],sub=['화내기 전에','다니는 길부터'],sub2='강아지 · 고양이 집 사례는')),
],durs,1,dict(
 name='매트가 없어서 화난 강아지와 고양이',title='강아지 매트 시공, 다리 수술을 두 번 한 강아지 집은 두께보다 발이 밀리지 않는 매트를 거실부터 복도까지 이어 깔았습니다',url=U,
 cap='매트가 없어서 강아지도 고양이도 화났다! 마루에서 미끌, 캣타워에서 미끌.',
 tags5=['#강아지매트','#고양이매트','#반려동물매트','#강아지고양이',NI:='#낭만인테리어'],
 yt='매트가 없어서 강아지도 고양이도 화났습니다',
 desc='강아지는 간식을 주우러 가다 마루에서 미끄러지고, 고양이는 캣타워에서 내려오자마자 다시 마루를 밟습니다.\n\n강아지 두 마리와 고양이 세 마리가 사는 한 집은 2.2cm 매트 하나로 둘 다 해결했습니다.\n강아지는 방향을 틀어도 덜 미끄러지고, 고양이는 뛰어내릴 때 충격을 덜 받습니다.\n캣타워 아래만 깔면 내려와 달리는 길은 다시 마루라서, 거실부터 복도까지 다니는 길을 따라 이어 깔았습니다.\n\n사는 지역과 연락처를 블로그 비밀댓글로 남겨 주시면 매트 시공팀을 연결해 드립니다.',
 tags10=['#강아지매트','#고양이매트','#반려동물매트','#강아지미끄럼방지매트','#고양이미끄럼방지매트','#강아지매트시공','#다묘집사','#강아지고양이','#반려견매트시공','#낭만인테리어'],
 scenes=['바닥 회의','강아지의 주장','고양이의 주장','파업 선언','매트를 깔았더니','마무리'],
 src='내용은 낭만 인테리어 「강아지 매트 시공」 발행 글과 「고양이 매트 두께」 글 · 시공은 제휴 시공팀이 맡습니다'),od)
if not os.environ.get('NOMP4'):
    v=f'{od}/nangman_interior_{slug}_short.mp4'; S='/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad'
    w=bgm.make(f'{S}/bgm_{slug}.wav',sum(durs),seed=12); src=f'{S}/{slug}_noaudio.mp4'; shutil.copy(v,src)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-i',w,'-filter:a','loudnorm=I=-16:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',v],check=True)
print(out)

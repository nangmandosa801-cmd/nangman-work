# 10/9 23:05 사용자 「응」(아직 안 올린 숏츠를 새 틀로 다시) — 한 편에 메시지 하나 · 장면 3개 · 10초 안팎 · 끝은 「블로그에서 확인하세요」
# 대상: 강아지 매트 test · hall · ipju(10/10~12) · 화난 강아지 고양이 · 고양이 매트 넷 · 낭만 부동산 입주 매트(너구리). 옛 판은 w/short3_before/
# 10/9 23:31 사용자 「너구리 캐릭터를 인테리어 쇼츠로 가져와 · 인테리어에서만 쇼츠 발행」 → 사람 자리(big · end 장면)는 너구리, 반려동물 장면은 강아지 · 고양이 그대로. nm ipju_mat은 dogmat_ipju와 겹쳐 만들지 않음
# info(제목 · 캡션 · 태그 · 설명 · 주소 · 전화)는 옛 스크립트의 것을 그대로 받아 쓰고 장면만 바꿈
import sys,os,subprocess,shutil; sys.path.insert(0,'/home/claude')
import clipgen, bgm
from comic import cdog, racc
FACE={'o':'happy','smile':'happy','worry':'worry','shock':'shock'}
REAL=clipgen.make; CAP={}
def grab(b,slug,scenes,durs,cover,info,outdir): CAP[slug]=dict(b=b,scenes=scenes,info=info,od=outdir); return []
clipgen.make=grab; os.environ['NOMP4']='1'
for f in ['clips_int_dogmat.py','clips_int_mat_hwanaem.py','clips_int_catmat.py','clips_nm_matracc.py']:
    try: exec(open('/home/claude/w/short3_before/'+f).read(),{'__name__':'x'})
    except Exception as e: print('capture',f,e)
del os.environ['NOMP4']; clipgen.make=REAL
from clipgen import WARN,OK,MID,NAVY
S='/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad'
def END(name,sub2,tel=None):
    d=dict(lines=[name],sub=['블로그에서','확인하세요'],sub2=sub2)
    if tel: d['tel']=tel
    return ('end',d)
def run(slug,scenes,names,seed,who='dog'):
    c=CAP[slug]; info=dict(c['info']); info['scenes']=names
    clipgen.person=(lambda d,x,y,s=1.0,face='o',shirt=None,**k: cdog(d,x,y-int(20*s),s*0.8,face=FACE.get(face,face))) if who=='dog' else (lambda d,x,y,s=1.0,face='o',shirt=None,**k: racc(d,x,y-int(20*s),s*0.8,face=FACE.get(face,face)))
    durs=[3.6,3.4,3.4]
    out=REAL(c['b'],slug,scenes,durs,0,info,c['od'])
    v=[o for o in out if o.endswith('_short.mp4')][0]
    w=bgm.make(f'{S}/bgm_{slug}.wav',sum(durs),seed=seed); src=f'{S}/{slug}_noaudio.mp4'; shutil.copy(v,src)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-i',w,'-filter:a','loudnorm=I=-16:TP=-1.5','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',v],check=True)
    print('\n'.join(out))
sc=lambda slug,i: CAP[slug]['scenes'][i]
ONLY=sys.argv[1:]
J=[
 ('dogmat_test',[sc('dogmat_test',0),
   ('big',dict(lines=['두께보다 먼저','이걸 보세요'],num='밀어 보기',nsize=160,sub1='반려견 매트도 밀어 보면 미끄러운 게 많았습니다',sub2='샘플은 손바닥으로 밀어 보세요',face='shock')),
   END('강아지 매트 고르는 법','샘플로 해 볼 네 가지는')],['두꺼우면 다 좋나요','밀어 보기','블로그에서 확인'],21,'racc'),
 ('dogmat_hall',[('comic',dict(lines=['거실에만','매트를 깔았더니'],items=sc('dogmat_hall',0)[1]['items'])),
   ('big',dict(lines=['강아지는 거실에만','있지 않습니다'],num='복도까지',nsize=170,sub1='다니는 길을 따라 이어 깝니다',sub2='거실 · 주방 · 복도 · 방',face='smile')),
   END('강아지 거실매트','이어 깐 세 집 사진은')],['매트 끝에서 꽈당','복도까지','블로그에서 확인'],22,'racc'),
 ('dogmat_ipju',[sc('dogmat_ipju',0),
   ('big',dict(lines=['짐 들어오기 전','빈집에 깔면'],num='하루',sub1='옮길 가구가 없어 하루에 끝납니다',sub2='입주청소 다음, 이삿짐 전',face='smile')),
   END('입주 매트 시공','영종 새 아파트 사진은')],['새 집 매트는 언제','빈집이면 하루','블로그에서 확인'],23,'racc'),
 ('mat_hwanaem',[('comic',dict(lines=['강아지도 고양이도','화났다!'],items=sc('mat_hwanaem',0)[1]['items'])),
   ('comic',dict(lines=['마루에서 미끌','캣타워에서 내려와도 미끌'],items=[('floor',1180,'tile'),('dog',300,930,0.85,'dizzy','slip'),('cat',780,930,0.85,'shock','slip'),('boom',540,560,'미끌!',90)])),
   END('강아지 · 고양이 매트','한 매트로 해결한 집은')],['강아지도 고양이도 화남','둘 다 미끌','블로그에서 확인'],24,'racc'),
 ('catmat_tower',[('comic',dict(lines=['캣타워에서 뛰어내리면','딱딱한 마루에 쿵!'],items=sc('catmat_tower',0)[1]['items'])),
   ('big',dict(lines=['고양이 세 집이','모두 고른 두께'],num='2.2cm',sub1='아산 · 구로 · 안양',sub2='어디까지 까느냐가 달랐습니다',face='smile')),
   END('고양이 미끄럼방지 매트','세 집 사진은')],['캣타워에서 쿵','2.2cm','블로그에서 확인'],25,'racc'),
 ('catmat_udada',[sc('catmat_udada',0),sc('catmat_udada',1),
   END('고양이 층간소음 매트','구로 집 전후 사진은')],['새벽 우다다','아래층까지 쿵쿵','블로그에서 확인'],26,'racc'),
 ('catmat_together',[sc('catmat_together',0),
   ('big',dict(lines=['한 매트를','같이 씁니다'],num='다섯 마리',nsize=170,sub1='강아지 둘 · 고양이 셋 · 충남 아산',sub2='반려견 매트 · 고양이 매트를 따로 고르지 않았습니다',face='smile')),
   END('강아지 매트 = 고양이 매트','함께 사는 집 사진은')],['고양이도 쓸 수 있나요','다섯 마리 한 매트','블로그에서 확인'],27,'racc'),
 ('catmat_vomit',[sc('catmat_vomit',0),
   ('comic',dict(lines=['토해도 · 찢어져도','그 장만 바꾸면 끝'],items=sc('catmat_vomit',2)[1]['items'] if sc('catmat_vomit',2)[0]=='comic' else sc('catmat_vomit',1)[1]['items'])),
   END('고양이 매트 관리','안양 집 사진은')],['헤어볼을 토했다','그 장만','블로그에서 확인'],28,'racc'),
 ('ipju_mat',None,None,29,'racc'),
]
for slug,scenes,names,seed,who in J:
    if ONLY and slug not in ONLY: continue
    if slug not in CAP: print('없음',slug,list(CAP)); continue
    if scenes is None:
        TEL='매트 시공 문의 010-2882-8165'
        scenes=[('comic',dict(lines=['입주 열쇠 받았다!','매트는 언제 깔지?'],items=sc(slug,0)[1]['items'])),
          ('big',dict(lines=['청소 다음','짐 들어오기 전'],num='빈집에',nsize=170,sub1='옮길 가구가 없어 작업이 빠릅니다',sub2='입주 순서 · 청소 → 매트 → 이삿짐',face='smile')),
          END('입주 순서와 매트','빈집에 깐 매트 사진은',tel=TEL)]
        names=['열쇠 받은 날','빈집에','블로그에서 확인']
    run(slug,scenes,names,seed,who)

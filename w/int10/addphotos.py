import sys,os,re,json,glob
sys.path.insert(0,'/home/claude/tools/postkit'); sys.path.insert(0,'/home/claude/tools/followup')
from vary import vary; from post_followup import is_banner
from PIL import Image
INB='/home/claude/w/review/inbox'; IMG='/home/claude/w/int10/img'; os.makedirs(IMG,exist_ok=True)
src=json.load(open('/home/claude/w/int10/src_map.json'))
SITE={'daemun_doorlock':'의정부 가능동 단독주택 대문','sajeon_daehaeng':'부천 오정 월드메르디앙 에듀파크 사전점검','bakeout':'대광로제비앙 모아엘가 입주청소 · 베이크아웃',
 'uiwang_julnun':'의왕 센트라인 데시앙 줄눈','maegyo_julnun':'수원 매교역 팰루시드 줄눈','pyeongchon_urban':'e편한세상 평촌어반밸리 입주청소','gangdong_sk':'강동역 SK리더스뷰 입주청소',
 'julnun_jaesigong':'서울 번동 아파트 줄눈 재시공','hyeongwan_julnun':'현관 줄눈 무펄 연브라운','oebyeok_coking':'병점역 센트럴허브시티 외벽 코킹'}
CTA={'daemun_doorlock':'대문 사진 한 장이면 쓰던 문에 번호키가 달리는지 먼저 봐 드립니다','sajeon_daehaeng':'단지 이름과 점검 날짜만 보내 주시면 점검팀 일정을 잡아 드립니다',
 'bakeout':'입주 날짜만 알려 주시면 청소 · 베이크아웃 날짜를 같이 잡아 드립니다','uiwang_julnun':'욕실 바닥 사진 한 장이면 같은 범위로 줄눈 견적을 받아 드립니다',
 'maegyo_julnun':'타입과 열쇠 받는 날만 알려 주시면 줄눈 날짜를 먼저 잡아 드립니다','pyeongchon_urban':'평형과 열쇠 받는 날만 알려 주시면 청소 날짜를 먼저 잡아 드립니다',
 'gangdong_sk':'평형과 열쇠 받는 날만 알려 주시면 청소 날짜를 먼저 잡아 드립니다','julnun_jaesigong':'지금 욕실 바닥 사진 한 장이면 재시공 범위와 견적을 받아 드립니다',
 'hyeongwan_julnun':'현관 사진 한 장이면 타일에 맞는 줄눈 색을 같이 골라 드립니다','oebyeok_coking':'샌 자리 사진 한 장이면 코킹으로 막히는지 먼저 봐 드립니다'}
led=[]; ni=[1578]
def mk(slug,path,cap,k):
    n=ni[0]; ni[0]+=1
    b,_=vary(path,f'{cap} · NI-{n}',f'{slug}|{path}',W=720,gentle=False)
    out=f'{IMG}/nangman_interior_{slug}_{k:02d}.jpg'; open(out,'wb').write(b)
    led.append(f'| NI-{n} | 제휴 블로그 | {path.replace("/home/claude/v2src/partners/","")} | {slug} | {cap} |'); return '!='+out
for slug,v in src.items():
    md=f'{INB}/nangman_interior_{slug}.md'; L=open(md).read().split('\n'); k=[0]
    # 1) 이미 넣은 「!/경로 캡션」 줄 → 가공 사진(!=)
    for i,l in enumerate(L):
        m=re.match(r'!(/home/claude/v2src/partners/\S+\.jpg) (.*?) \(제휴 시공팀 현장 · NI-\d+\)$',l)
        if m: k[0]+=1; L[i]=mk(slug,m.group(1),m.group(2),k[0])
    # 2) 원 글 사진 4장(배너 · 첫 장 · 끝 세 장 빼고 고르게)
    fs=sorted(glob.glob(f'/home/claude/v2src/partners/{v}/*.jpg'))
    ok=[]
    for f in fs[1:-3] if len(fs)>6 else fs[1:]:
        try:
            im=Image.open(f); w,h=im.size
            if h/w>2.2 or is_banner(f): continue
            ok.append(f)
        except Exception: pass
    pick=[ok[int(j*(len(ok)-1)/3)] for j in range(4)] if len(ok)>=4 else ok
    H=[i for i,l in enumerate(L) if l.startswith('## ') and '같이 보면' not in l]
    def para_end(i):
        j=i+1
        while j<len(L) and L[j].strip()=='': j+=1
        while j<len(L) and L[j].strip()!='': j+=1
        return j
    ins=[]
    if pick:
        a=pick[:2]; b_=pick[2:]
        p1=para_end(H[0]) if H else 6; p2=para_end(H[len(H)//2]) if len(H)>2 else p1
        blk1=['']+[mk(slug,f,SITE[slug]+' 현장',(k.__setitem__(0,k[0]+1) or k[0])) for f in a]
        blk2=['']+[mk(slug,f,SITE[slug]+' 현장',(k.__setitem__(0,k[0]+1) or k[0])) for f in b_]+['',f'[CALL] {CTA[slug]}']
        for pos,blk in sorted([(p1,blk1),(p2,blk2)],reverse=True): L[pos:pos]=blk
    open(md,'w').write('\n'.join(L))
    print(slug,len(pick),sum(1 for l in L if l.startswith('!=')))
open('/home/claude/낭만인테리어_사진번호.md','a').write('\n'.join(led)+'\n'); print('NI',ni[0]-1)

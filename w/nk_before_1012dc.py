# 10/7 새 글 묶음(제목 10편 + 주제 10편) 공용 — sg_kit 위에 사진 · 그림 · 점검을 얹음
exec(open('/home/claude/int/sg_kit.py').read())
import sys,subprocess; sys.path.insert(0,'/home/claude/src'); sys.path.insert(0,'/home/claude/int')
import wm, fx, figkit as FK
from PIL import ImageOps
def SET(slug,kw):
    global s,KW; s=slug; KW=kw; os.makedirs(OUT+s,exist_ok=True)
def ph(n,c): return PH(f'nangman_interior_{s}_{n}.jpg — {KW} · {c}')
def fg(n,c): return PH(f'nangman_interior_{s}_fig{n}.png — {KW} · {c}')
def FP(n): return OUT+s+f'/nangman_interior_{s}_fig{n}.png'
def SRCIM(blog,no,i): fx.photos(blog,no); return Image.open(f'/home/claude/src/{blog}/{no}/{i:02d}.jpg').convert('RGB')
def MD(no,i,part=None,box=None,extra=(),skip=False,blog='pjh20712'):
    """모던중문 사진 — 업체 표시를 낭만 인테리어 표시로 덮고, part='L'/'R'이면 전 · 뒤 가운데 한쪽만, box면 그만큼 자른다"""
    im,n=wm.cover(SRCIM(blog,no,i),extra=extra,skip=skip)
    W,H=im.size
    if part=='L': im=im.crop((0,0,int(W*0.455),H))
    if part=='R': im=im.crop((int(W*0.545),0,W,H))
    if box: im=im.crop(box)
    return im
def pair(a,b,la='바꾸기 전',lb='바꾼 뒤',W_=900):
    g=12; w=(W_-g)//2; h=min(int(a.height*w/a.width),int(b.height*w/b.width)); a=ImageOps.fit(a,(w,h),Image.LANCZOS); b=ImageOps.fit(b,(w,h),Image.LANCZOS)
    c=Image.new('RGB',(W_,h),'white'); c.paste(a,(0,0)); c.paste(b,(w+g,0)); d=ImageDraw.Draw(c); f=F(34,False,True)
    for x,t,col in ((0,la,'#8A8578'),(w+g,lb,'#1F3864')):
        if t: tw=d.textlength(t,font=f); d.rectangle([x,0,x+tw+36,58],fill=col); d.text((x+18,7),t,font=f,fill='white')
    return c
def DONE(T,photos,nfig=0):
    """사진 설명에 검색어를 넣고 SEO 점검 · 그림 수 세기"""
    p=OUT+s+f'/nangman_interior_{s}_post.html'; h=open(p).read(); kw=T.split(',')[0]
    h=re.sub(r'(nangman_interior_'+s+r'_\w+\.(?:jpg|png) — )(?!낭만 인테리어 안내)(?!'+re.escape(KW)+')',lambda m:m.group(1)+KW+' · ',h); open(p,'w').write(h)
    used=set(re.findall(rf'nangman_interior_{s}_[\w]+\.(?:jpg|png)',h)); have=set(os.listdir(OUT+s)); print('  없는 그림',used-have,'· 안 쓴 그림',{f for f in have if f.endswith(('.jpg','.png')) and 'thumb' not in f}-used,'· 사진',len(photos),'+ 그림',nfig)
    t=re.sub('<[^>]+>',' ',re.sub('<!--.*?-->','',h)).split('같이 보면 좋은 글')[0]
    t=re.sub(r'(?:제휴 |시공은 제휴 )?업체가 맡습니다|업체에게서 계약 금액','',t)   # 수수료 고지는 빼고 본다
    # 10/9 20:34 사용자: 「업체는 이라는 주어로 블로그 쓰면 안됨 너무 남인 듯 들리자나」 → 본문에 「업체는 · 업체가」 주어 금지(시공팀 · 저희 · 주어 생략으로)
    print('  금지어',re.findall(r'\S*(?:업체[는가](?=\s)|가장자리|자리|갈[라랐렸리린아색]|나갈|고요\b|(?<!입주청소 )프리미엄(?! 입주청소| 입주케어)|최고|헷갈|트렌드|퀄리티|가능성|모던중문|소소리|썬중문|크로바|도하|더빅|다온|줄남|010-\d)\S*',t))
    print(subprocess.run(['python3','/home/claude/blogkit/seo.py',p],capture_output=True,text=True).stdout)
PUB.update({'byeokji_gompangi':('224438517059','벽지 곰팡이 원인, 창가와 모서리부터 피면 결로이고 벽 아래쪽 한 줄로 번지면 누수부터 봅니다')})
PUB.update({'rail':('224430402740','중문 레일 고장, 청소로 끝나는 집과 바퀴를 바꿀 집과 레일을 다시 깔 집이 다릅니다'),
 'witjip':('224432310037','윗집 베란다 누수, 아랫집 천장이 비 올 때만 젖으면 윗집 바닥이 아니라 외벽 네 곳부터 봅니다'),
 'maegyo':('224430494646','매교역 팰루시드 입주, 옵션 중문은 3연동 180만원이고 이 집 현관에는 간살을 넣은 3연동을 달았습니다'),
 'icheon':('224430505012','힐스테이트 이천역 2단지 중문, 옵션은 3연동 280만원이고 이 집 현관에는 우드 간살 원슬라이딩을 달았습니다'),
 'unjeong':('224430507870','운정중앙역 동문디이스트 중문, 현관 복도에 뿌연 유리 원슬라이딩을 달았습니다')})
def MDc(no,i,box,extra=(),skip=False,blog='pjh20712',minw=176):
    """합성 사진에서 한 칸을 먼저 잘라 낸 뒤 업체 표시를 덮는다. extra는 자른 뒤 좌표"""
    return wm.cover(SRCIM(blog,no,i).crop(box),extra=extra,skip=skip,minw=minw,minh=int(minw*0.34))[0]
def TRIM(im,thr=9,maxit=400):
    """둘레의 단색 띠(회색 틀 · 흰 여백)를 잘라 낸다"""
    import numpy as np
    a=np.array(im.convert('L')).astype(float); x0,y0,x1,y1=0,0,a.shape[1],a.shape[0]
    for _ in range(maxit):
        ch=False
        if y1-y0>50 and a[y0,x0:x1].std()<thr: y0+=1; ch=True
        if y1-y0>50 and a[y1-1,x0:x1].std()<thr: y1-=1; ch=True
        if x1-x0>50 and a[y0:y1,x0].std()<thr: x0+=1; ch=True
        if x1-x0>50 and a[y0:y1,x1-1].std()<thr: x1-=1; ch=True
        if not ch: break
    return im.crop((x0+2,y0+2,x1-2,y1-2))
def MDh(no,i,part,top=60,extra=(),minw=150,skip=False,blog='pjh20712'):
    """머리띠가 붙은 두 칸짜리 합성 사진에서 한 칸(part 'L'/'R')의 사진만 꺼내 업체 표시를 덮는다"""
    im=SRCIM(blog,no,i); W,H=im.size; im=im.crop((0,top,W//2,H) if part=='L' else (W//2,top,W,H)); im=TRIM(im)
    return wm.cover(im,extra=extra,skip=skip,minw=minw,minh=int(minw*0.34))[0]
def NOPHOTO_BANNER(kind,T,q,items,ex=None,two=False):
    """사진을 못 쓰는 글(입주청소 등)의 끝 배너 — build_s 뒤에 부른다"""
    import post_banner; post_banner.render(OUT+s+f'/nangman_interior_{s}_banner.png',kind,T,q,items,[],ex=ex,two=two)
# 10/7 01:05 발행: 입주청소 추가금
PUB.update({'cheongso_chugageum':('224433569335','입주청소 추가금, 청소하는 날 30만원을 더 달라는 말을 듣지 않으려면 계약 전에 일곱 가지를 문자로 받습니다')})
# 10/7 22:22 발행: 힐스테이트 메디알레 입주 (10/8에 PUB에 넣음)
PUB.update({'ipju_medialle':('224434575801','힐스테이트 메디알레 입주, 현관 옵션은 신발장뿐이었고 다른 힐스테이트 네 곳의 옵션 중문은 120만~280만원이었습니다')})
def NUMBER(photos,ven,descs=None):
    """시공 사진 일련번호(NI-) — 10/9 00:07 · 20:14 사용자 「시공 사진에 일련번호 부여하는거 적용해」.
    photos: [(im,name,caption)] · ven: 이름 둘째 토막(예 's1') → (업체, '블로그 글번호', 지역). 사진에 번호를 찍고 설명 끝에 (사진 NI-xxxx)를 붙여 (PHOTOS, C)를 돌려준다."""
    import serial as SN
    out=[];C={}
    for im,n,cap in photos:
        v=ven[n.split('_')[1]]; d=(descs or {}).get(n,cap.split(' — ')[-1])
        c=SN.code(s,n,v[0],v[1],v[2],d)
        out.append((SN.stamp(im,c),n,cap+f' (사진 {c})')); C[n]=cap.split(' — ')[0]+' '+cap.split(' — ')[1]+f' (사진 {c})'
    return out,C
def LIKE(no, two=False, ipju=False, title=None, mat=False):
    """「이 사진처럼 하고 싶다면」 상자 — 10/9 20:40 · 20:41 사용자 「장점을 어필하는 내용이 더 들어가야」 「넣고 일련번호까지 포함하라니깐」.
    사례를 다 보여 준 바로 뒤(문의 띠 근처)에 한 번. no: 이 글 사진 번호 하나(예 'NI-0185') · two: 두 곳 견적이 실제로 되는 품목 · 지역(중문 서울 · 경기 · 인천 · 충청 / 필름 서울 · 경기)일 때만 True · ipju: 입주 단지 글.
    글마다 같은 문장이 반복되지 않게 slug로 문장 꼴을 고른다."""
    k=sum(map(ord,s))%3
    num=[f'사진 오른쪽 아래 번호({no} 같은)를 비밀댓글에 같이 적어 주세요. 그 사진을 시공한 팀으로 바로 연결해 드립니다.',
         f'마음에 드는 사진이 있으면 번호만 알려 주세요. {no}처럼 적으면 같은 시공을 한 팀이 연락드립니다.',
         f'「{no}처럼 해 주세요」라고 남기면 됩니다. 사진 속 그 집을 맡았던 시공팀으로 연결해 드리죠.'][k]
    rows=[num]
    if mat:   # 10/9 20:44 사용자: 강아지 매트 업체는 현재 매출 1위 · 평단가를 픽스함 → 매트 글(블라썸매트)에만
        rows.append(['연결해 드리는 매트 시공팀은 반려동물 매트 시공을 이끄는 선도 업체입니다.','매트는 이 분야 선도 업체의 시공팀으로 연결해 드립니다.','이 매트를 시공한 곳은 반려동물 매트 시공의 선도 업체입니다.'][k])   # 10/9 20:45 사용자: 「매출 1위라고 하지 말고 선도 업체라고」
        rows.append(['평당 단가를 정해 두어서, 같은 평수면 견적이 따로 부풀지 않습니다.','평당 단가가 정해져 있어 집마다 값을 높여 부를 일이 없죠.','단가는 평당으로 정해져 있습니다. 같은 넓이면 같은 단가로 계산합니다.'][k].replace('값을','가격을'))
    if two: rows.append(['두 곳 견적을 한 번에 받아 나란히 비교할 수 있습니다.','원하시면 시공팀 두 곳의 견적을 같이 받아 보실 수 있습니다.','견적은 두 곳에서 받아 비교하셔도 됩니다.'][k])
    rows.append(['다른 곳에서 받아 둔 견적서가 있으면 같은 공사인지 봐 드립니다.','이미 받은 견적서가 있다면 빠진 항목이 없는지 같이 봐 드립니다.','받아 두신 견적서와 같은 범위인지 맞춰 봐 드립니다.'][k])
    rows.append(['소개받은 시공팀이 마음에 안 들면 거절 연락은 저희가 대신 드립니다.','상담해 보고 아니다 싶으면 거절은 저희가 전해 드립니다.','마음에 안 들 때 직접 거절하기 어렵다면 저희가 대신 연락합니다.'][k])
    rows.append(['공정 두 가지 넘게 같이 맡기시면 견적 금액에서 3% 할인해 드립니다.','두 공정 넘게 함께 맡기시면 견적 금액의 3%를 빼 드립니다.','공정을 두 가지 넘게 묶어 맡기시면 견적에서 3% 할인됩니다.'][k])   # 10/12 11:58 사용자 「공정 2개 하면 3프로 견적가에서 DC 하자」
    if ipju: rows.append(['입주하는 집이라면 중문 · 샷시 · 청소 · 매트를 한 번 문의로 맡길 수 있습니다.','입주 전 공사를 하나씩 따로 찾지 않아도 됩니다. 한 번 문의로 연결해 드립니다.','입주 준비는 중문부터 청소 · 매트까지 한 번에 문의하시면 됩니다.'][k])
    return ('<p style="background:#FFF8EC;border-left:4px solid #C98A2E;padding:18px 20px;font-size:19px;color:#333;line-height:1.95;"><b style="color:#7A4E12;font-size:21px;">'+(title or '이 사진처럼 하고 싶다면')+'</b><br><br>'+'<br>'.join('▸ '+r for r in rows)+'</p>\n\n')
# 10/11 00:14 발행: 강아지 매트 추천
PUB.update({'gangaji_mat_chucheon':('224437536765','강아지 매트 추천, 같은 2.2cm라도 겉면 TPU와 속 우레탄 양이 달라서 샘플을 눌러 보고 고릅니다'),'gangaji_mat':('224435609606','강아지 매트 시공, 다리 수술을 두 번 한 강아지 집은 두께보다 발이 밀리지 않는 매트를 거실부터 복도까지 이어 깔았습니다')})

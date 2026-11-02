# 10/31 12시 뒤 미발행 글 링크 현행화 (사용자 10/18 02:11)
import json,re,os,sys
sys.path.insert(0,'/home/claude/int'); import links
pub=json.load(open('/home/claude/pub/int_live_1018.json')); T={i:t for i,t in pub}
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
NEW_DAN=('224444765222',T['224444765222']); OLD_DAN=('224422155844','창문 단열필름, 붙이기 전에 우리 집 유리부터 봅니다')
links.DESC['224444765222']='겨울에 단열필름이 해 주는 것과 로이유리 집 순서입니다'
FILM_ALT=['224433582512','224435807923','224421914315']
norm=lambda s:re.sub(r'[\s,·「」.\-~～]','',s)
def match(t):
    n=norm(t)
    for i,pt in pub:
        p=norm(pt)
        if p==n or p.startswith(n[:16]) or n.startswith(p[:16]): return i
MAP={'스윙 중문, 고장 날':'224421972563','중문 가벽, 세우는':'224430320746','자동 중문, 전기 없이':'224429875441','중문 사이즈 재는':'224424110739',
     '베란다 방묘문 제작':'224421379783','방충망 고양이 교체':'224426986850','중문 색상, 프레임':'224421914315','현관 조명, 중문을':'224422168377',
     '중문 설치 비용, 3연동':'224420365390','샷시 등급, 같은':'224423105514','중문 브랜드, 검색은':'224419299693','베란다 중문, 낡은':'224439530451',
     '베란다 태양광 지원사업':None,'태양광 설치 비용':None}
FALL=['224435585820','224444906311','224430190408','224444596338','224419299693','224420365390']
def target(t,used):
    i=match(t)
    if i is None:
        k=next((k for k in MAP if t.startswith(k)),'__')
        i=MAP.get(k,'X')
        if i is None: return None
        if i=='X': i=None
    if i is None or i in used:
        i=next((f for f in FALL if f not in used),None)
    return i
ZERO={'jungmun_brand':['224419299693','224420365390','224430190408','224444596338','224421360439'],
 'hyeongwan_light':['224422168377','224426338443','224419299693','224435796181','224420365390'],
 'jungmun_color':['224421914315','224435796181','224424199956','224422061785','224419299693'],
 'jungmun_cost':['224420365390','224430190408','224430352435','224444906311','224424110739'],
 'jungmun_mutagong':['224424176442','224431136138','224435839462','224420250220','224430352435'],
 'sash_grade':['224433582512','224423105514','224439530451','224444765222','224432259684']}
log=[]
for s in sel:
    f=B+s; h=open(f).read(); h0=h; ch=[]
    used=set(re.findall(r'champion_chart/(\d{12})',h))
    # A 단열필름
    if OLD_DAN[0] in h:
        h=h.replace('「<a href="https://blog.naver.com/champion_chart/224422155844"','「<a href="https://blog.naver.com/champion_chart/224444765222"')
        h=h.replace(OLD_DAN[1]+'</a>」을',NEW_DAN[1]+'</a>」 글을').replace(OLD_DAN[1],NEW_DAN[1]).replace('224422155844','224444765222')
        h=h.replace('유리 종류에 따라 단열필름을 고르는 방법입니다',links.DESC['224444765222']); ch.append('단열필름 링크 교체')
    # B 필름 가격(삭제된 글)
    if '224430339313' in h:
        # 본문 속 한 문장 빼기
        def cut(m):
            return ''
        n0=h.count('224430339313')
        h=re.sub(r'(?<=[.>]) ?[^.<>]*「<a href="https://blog.naver.com/champion_chart/224430339313"[^>]*>[^<]*</a>」[^.<]*\.','',h)
        # 꼬리 카드: 다른 필름 글로
        alt=next((a for a in FILM_ALT if a not in used),None)
        if alt and '224430339313' in h:
            h=h.replace('인테리어 필름 시공 가격, 34평은 방문·싱크대·현관문만 150만~250만원이고 샷시까지 하면 300만원을 넘습니다',T[alt]).replace('224430339313',alt)
            h=h.replace('방문·싱크대·현관문·샷시 부위별 필름 가격입니다',links.DESC.get(alt,'')); used.add(alt)
        ch.append(f'필름 가격 링크 {n0}곳 정리')
    # C span 발행 예정
    def rep(m):
        t=m.group(1); i=target(t,used)
        if i is None: return '__DROP__'
        used.add(i); ch.append(f'예정→{T[i][:14]}')
        return f'<a href="https://blog.naver.com/champion_chart/{i}" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">{T[i]}</a>'
    h=re.sub(r'<span style="color:#1F3864;">([^<]+)</span> <span style="font-size:1[56]px;color:#A8A296;">발행 예정</span>',rep,h)
    h=re.sub(r'<p style="font-size:19px;color:#333;line-height:1.9;">· __DROP__</p>\n?','',h)
    # D 옛 모양 「발행 예정 · 제목」 블록
    m=re.search(r'\n</p>\n\n<p style="font-size:16px;color:#8A8578;line-height:2.0;">(발행 예정 · .*?)</p>',h)
    if m:
        add=''
        for t in re.findall(r'발행 예정 · ([^<]+)',m.group(1)):
            i=target(t.strip(),used)
            if i: used.add(i); add+=f'<br>\n<a href="https://blog.naver.com/champion_chart/{i}" style="color:#2E5C8A;">{T[i]} ›</a>'; ch.append(f'예정→{T[i][:14]}')
        h=h[:m.start()]+add+'\n</p>'+h[m.end():]
    # E href="#"
    def rep2(m):
        t=m.group(2); i=target(t,used)
        if i is None: return m.group(0)
        used.add(i); ch.append(f'#→{T[i][:14]}')
        return m.group(1)+f'https://blog.naver.com/champion_chart/{i}'+m.group(3)+T[i]+'</a>'
    h=re.sub(r'(<a href=")#("[^>]*>)([^<]+)</a>',lambda m: rep2(type('M',(),{'group':lambda self,k:{0:m.group(0),1:m.group(1),2:m.group(3),3:m.group(2)}[k]})()),h)
    # G 링크 없는 글에 같이 보면 좋은 글 5편
    slug=os.path.basename(f)[len('nangman_interior_'):-len('_paste.html')]
    if slug in ZERO and h.count('champion_chart/')<5:
        pairs=[(i,T[i]) for i in ZERO[slug] if i in T]
        sec=links.section(pairs)
        k=h.rfind('<p style="font-size:17px;color:#8A8578;">#')
        h=(h[:k]+sec+'\n'+h[k:]) if k>0 else h+sec
        ch.append(f'같이 보면 좋은 글 {len(pairs)}편 넣음')
    dead=[i for i in re.findall(r'champion_chart/(\d{12})',h) if i not in T]
    nlink=len(set(re.findall(r'champion_chart/(\d{12})',h)))
    if h!=h0:
        os.makedirs(O+os.path.dirname(s),exist_ok=True); open(O+s,'w').write(h)
    log.append(dict(file=s,changes=ch,dead=dead,links=nlink,left_ph=h.count('발행 예정'),changed=h!=h0))
json.dump(log,open('/home/claude/w/relink1018/log.json','w'),ensure_ascii=False,indent=1)
for l in log:
    if l['changed'] or l['dead'] or l['left_ph'] or l['links']<5: print(l['file'][9:30],l['links'],l['left_ph'],l['dead'],l['changes'])
print(sum(l['changed'] for l in log))

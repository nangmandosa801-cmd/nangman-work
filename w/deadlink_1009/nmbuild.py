import sys,re; sys.path.insert(0,'/home/claude/gs'); sys.path.insert(0,'/home/claude/blogkit')
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from lotto import L
from kit import P,B,DIV,H,NOTE,table,BR,ph
from ui import HL,KV,STATS,CALL
from intbox import NANGMAN,BRAND

# 글 끝 「옆 블로그 · 낭만 인테리어」 상자 — 10/4 사용자: 「계속 같은 링크라 식상하다, 다른 링크를 달자」 → 글마다 묶음을 바꾼다. p['ibox']로 고르고, 없으면 slug에 따라 돌아간다.
IBOX={
 'jeonse':('전세나 월세로 이사한다면',[('224431136138','전세집 중문, 집주인 동의 받고 달거나 무타공으로 달 수 있고 나갈 때 철거 비용은 10만~30만원입니다','전세집에 중문을 다는 방법 세 가지'),('224424176442','무타공 중문, 구멍 대신 천장과 바닥을 눌러서 버팁니다','벽에 구멍을 내지 않는 중문'),('224423038831','중문 슬라이딩도어 빼는법, 위로 들어 올리고 아래를 앞으로 뺍니다','이삿짐이 안 들어갈 때 문짝 빼는 순서')]),
 'ipju':('새 아파트 입주를 앞두고 있다면',[('224430190408','중문 옵션 사제 차이, 입주 단지 19곳 옵션 중문은 110만원에서 365만원입니다','옵션으로 할지 입주 뒤에 달지'),('224430339313','인테리어 필름 시공 가격, 34평은 방문·싱크대·현관문만 150만~250만원이고 샷시까지 하면 300만원을 넘습니다','입주 전에 색을 바꾸는 가격'),('224422168377','현관 신발장, 중문을 달 거면 같이 정해야 합니다','신발장과 중문을 같이 정하는 이유')]),
 'winter':('겨울이 오기 전에 집을 손본다면',[('WIND','현관 외풍 차단, 휴지 한 장으로 새는 곳 찾고 5단계로 막습니다','현관에서 바람이 새는 곳을 찾는 순서'),('224422155844','창문 단열필름, 붙이기 전에 우리 집 유리부터 봅니다','붙여도 되는 유리와 안 되는 유리'),('224423105514','샷시 교체 지원금, 현금으로 주는 곳과 이자만 내주는 곳이 다릅니다','샷시를 바꿀 때 받는 지원')]),
 'base':('이사나 집수리를 앞두고 있다면',[('224419299693','현관중문 종류, 우리 집 현관엔 뭐가 맞을까요','중문을 처음 알아볼 때 보는 글'),('224420365390','아파트 중문 가격, 32평이라고 정해지지 않습니다','중문 가격이 어디서 달라지는지'),('224422155844','창문 단열필름, 붙이기 전에 우리 집 유리부터 봅니다','겨울 전에 창문 손볼 때')]),
}
def ibox(p):
    import json
    k=p.get('ibox') or ['jeonse','ipju','winter'][sum(map(ord,p['slug']))%3]
    head,items=IBOX[k]
    wind=json.load(open('/home/claude/pub/int_auto.json')).get('wind',[None])[0]
    s=('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F4F6F9;border-left:4px solid #2E5C8A;padding:18px 20px;">\n'
       '<span style="font-size:16px;color:#7A8590;letter-spacing:1px;">옆 블로그 · 낭만 인테리어</span><br>\n'
       f'<span style="font-size:19px;font-weight:700;color:#1F3864;">{head}</span><br><br>\n')
    for n,t,d in items:
        n=wind if n=='WIND' else n
        s+=(f'<a href="https://blog.naver.com/champion_chart/{n}" style="font-size:19px;font-weight:700;color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n'
            f'<span style="font-size:16px;color:#7A8590;">{d}</span><br><br>\n')
    return s+'</td></tr></table>\n<p><br></p>\n'
def LN(k):
    n,t,d=L[k]
    return '「<a href="https://blog.naver.com/dong_jin_kim/'+n+'" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">'+t+'</a>」'
def build(p):
    o=['<p style="font-size:17px;color:#2E5C8A;letter-spacing:1px;">낭만 부동산 분석 플랫폼 · '+p['kick']+'</p>\n'+BR,
       f'<p style="font-size:34px;font-weight:700;color:#1F3864;">{p["title"]}</p>\n'+BR]
    for l in p['lead']: o.append(P(l))
    o+=p['body']
    o.append(DIV); o.append(NOTE(p['src']))
    o.append('<p style="font-size:27px;font-weight:700;color:#1F3864;">함께 보면 좋은 글</p>\n'+BR)
    for k in p['links']:
        n,t,d=L[k]
        o.append(f'<p style="font-size:19px;font-weight:700;"><a href="https://blog.naver.com/dong_jin_kim/{n}" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n<span style="font-size:17px;color:#7A8590;">{d}</span></p>\n'+BR)   # 10/5 02:39 사용자: 꼬리 링크 사이에 빈 줄 하나
    o.append(BRAND)
    if p.get('intbanner',True):   # 10/9 사용자: 낭만 부동산 글 끝에 인테리어 배너 + 한 줄 링크
        import intbanner; o.append(intbanner.block(p['slug'],p['title']))
    o.append(ibox(p))
    o.append('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">\n<tr><td style="background-color:#F4F6F9;border-left:3px solid #2E5C8A;padding:16px 18px;">\n<span style="font-size:16px;color:#8A8578;">태그</span><br>\n<span style="font-size:18px;color:#555;line-height:1.9;">'+' '.join('#'+t for t in p['tags'])+'</span>\n</td></tr>\n</table>\n')
    h=''.join(o); body=h[:h.find('함께 보면 좋은 글')]; t=re.sub(r'<[^>]+>',' ',body)
    bad=re.findall(r'\S*(?:갈|자리|고요|프리미엄|%p|어요|예요|헷갈|최고|가능성|놓습니다|놓고|가정)\S*',t)
    open(f'/mnt/user-data/outputs/nangman_new/nangman_{p["slug"]}_post.html','w').write(h)
    sys.stdout.write(f'{p["slug"]} 표 {h.count("table-layout:fixed")} 금지 {bad} 글자 {len(re.sub(chr(92)+"s","",t))} 링크 {h.count("blog.naver.com/dong_jin_kim/")} 숫자 {len(re.findall(r"[0-9][0-9,.]*",t))}\n')
    for kw in p.get('keys',[]): sys.stdout.write(f'   {kw} {body.count(kw)}\n')
    try:
        import seo; seo.check(h,keys=p.get('keys',[]),slug='nangman_'+p['slug'])   # SEO 자동완성 점검 — 글을 만들 때마다 (10/5 사용자: 무조건 반영)
    except Exception as e: sys.stdout.write(f'   SEO 점검 못 함: {e}\n')
L['ndg']=('224414230923','노도강 아파트 시세, 전세가율 67%인데 왜 아직 2021년 고점 아래일까','노원 · 도봉 · 강북 아파트 가격을 본 글입니다')
L['s5']=('224425144688','서울 5억대 아파트, 같은 5억 5천으로 금천은 85㎡ 송파는 32㎡입니다','5억대로 살 수 있는 서울 집을 구별로 본 글입니다')
L['g3']=('224409734321','강남 3구 아파트, 매매 29.4억인데 전세는 9.25억입니다','15억 넘는 집이 많은 강남 3구입니다')
L['dtr']=('224413595031','동탄 규제, 두 달 만에 매매는 바로 멈췄고 전세는 천천히 움직였습니다','7월에 규제지역이 된 동탄의 두 달입니다')
L['hn']=('224427544220','하남 집값, 올해 17% 올랐는데 5억 이하 집은 7%뿐입니다','하남 집을 값 구간으로 나눠 센 글입니다')
L['gm']=('224423346736','광명 아파트 시세, 40년 된 철산주공이 1년 새 30% 올라 광명역 신축을 넘어섰습니다','올해 경기도에서 많이 오른 광명입니다')
L['mys']=('224410297285','마용성 아파트, 성동 18.06억이 용산 18.62억을 0.56억까지 좁혔습니다','마포 · 용산 · 성동 아파트 가격입니다')
L['jb']=('224409052077','종부세 기준, 내가 살면 20억, 전세 주면 9억으로 줄어듭니다','집을 산 뒤 해마다 내는 세금 기준입니다')
L['jjc']=('224423322072','줍줍 청약 조건, 2025년 6월 10일부터 1주택자는 못 넣습니다','무순위 청약에 넣을 수 있는 사람입니다')
L['gc']=('224423155571','과천 로또 청약, 1순위 미달 써밋도 415대 1 라비엔오도 13억 올랐습니다','9월에 나온 과천 줍줍입니다')
L['db']=('224415206586','동북권 아파트 시세, 광진 낡은 집은 새 집과 같고, 동대문은 절반입니다','광진구 아파트 값을 본 글입니다')
L['janghang']=('224431122476','고양 장항 아테라 줍줍, 84㎡ 6가구 분양가 6억대는 장항동 1994년 아파트 가격이고 고양 사는 무주택 세대주만 10월 7·8일에 넣습니다','고양에서 나온 줍줍의 자격과 드는 돈입니다')
L['gb']=('224430977217','서울 줍줍, 강변역 센트럴아이파크 84㎡ 12.2억 1가구는 옆 광진그랜드파크 21억의 58%이고 10월 6일 접수입니다','10월 6일에 받는 서울 줍줍입니다')
L['bdc']=('224431548418','더샵 분당센트로 줍줍, 5차 84㎡ 1가구에 104명이 넣었는데 6차에 또 나왔고 분양가 20억 5,900만원은 올해 구미동에서 가장 비싸게 팔린 84㎡보다 1억 2천 높습니다','분당에서 여섯 번째로 나온 줍줍입니다')
L['cjn']=('224431526825','충정로역 자이르네 줍줍, 84㎡ 35가구 중 21가구는 올해 중구에서 가장 비싸게 팔린 22억 9천만원보다 비싸고 강변역 줍줍과 같이 넣을 수 없습니다','서울 중구에서 나온 줍줍입니다')
L['medialle']=('224434552062','힐스테이트 메디알레 분양가, 분양 때는 옆 새 아파트보다 5천만원 비쌌는데 지금은 1억 7천만원 쌉니다','은평구 재개발 새 아파트의 분양가와 옆 단지 실거래가를 비교한 글입니다')

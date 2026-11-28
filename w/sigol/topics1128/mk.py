"""팜 에디터 11/28 글 그림 — honey4/mkimg.py 와 같은 틀(크림 바탕 · 녹색 · 금색 · Noto Sans CJK KR)"""
import pathlib
from playwright.sync_api import sync_playwright
D=pathlib.Path(__file__).parent
F="font-family:'Noto Sans CJK KR'"
C=dict(bg='#F6F1E4',ink='#3F4A36',g='#5E7552',lg='#7E9470',gold='#B08A4A',hon='#E0A43A',pale='#EFE6D2',line='#E2D8C2',gray='#8A8270',red='#B5523B',per='#E07A2E')
def page(inner,h=1080):
    return f'<meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:{h}px;background:{C["bg"]};{F};color:{C["ink"]}}}</style><div style="position:relative;width:1080px;height:{h}px;overflow:hidden">{inner}</div>'
def card(lab,head,body,src=''):
    return page(f'''<div style="position:absolute;inset:0;padding:70px 70px 60px;display:flex;flex-direction:column">
 <div style="display:flex;align-items:center;gap:14px;font-size:30px;color:{C['gold']};font-weight:700"><span style="width:46px;height:4px;background:{C['gold']}"></span>{lab}</div>
 <div style="font-size:62px;font-weight:700;line-height:1.22;margin-top:22px;letter-spacing:-1px">{head}</div>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:center">{body}</div>
 <div style="display:flex;justify-content:space-between;font-size:24px;color:{C['gray']};border-top:2px solid {C['line']};padding-top:18px"><span>{src}</span><span>팜 에디터</span></div></div>''')
def thumb(lab,kw,sub,visual,tag):
    return page(f'''<div style="position:absolute;right:-20px;top:90px">{visual}</div>
<div style="position:absolute;top:44px;left:50px;font-size:30px;color:#fff;background:rgba(63,74,54,.85);padding:10px 22px;border-radius:30px">팜 에디터</div>
<div style="position:absolute;left:70px;right:70px;bottom:80px">
 <div style="font-size:52px;font-weight:500;color:{C['lg']}">{lab}</div>
 <div style="font-size:120px;font-weight:700;line-height:1.08;margin-top:10px;letter-spacing:-2px">{kw}</div>
 <div style="font-size:54px;font-weight:700;line-height:1.3;margin-top:22px;color:{C['g']}">{sub}</div>
 <div style="display:flex;align-items:center;gap:16px;margin-top:30px;font-size:34px;color:#6B6455"><span style="width:46px;height:3px;background:#C9A86A"></span>{tag}</div></div>''')
def persim(n=5,w=420):
    s=''.join(f'<g transform="translate({40+i*70},{0})"><line x1="20" y1="0" x2="20" y2="{60+i%2*20}" stroke="{C["gold"]}" stroke-width="4"/><ellipse cx="20" cy="{110+i%2*20}" rx="32" ry="40" fill="{C["per"]}"/><path d="M8 {72+i%2*20} q12 -10 24 0" stroke="{C["g"]}" stroke-width="7" fill="none"/></g>' for i in range(n))
    return f'<svg width="{w}" height="{w}" viewBox="0 0 420 420"><line x1="20" y1="2" x2="400" y2="2" stroke="{C["ink"]}" stroke-width="6"/>{s}{s.replace("translate(","translate(0 190) translate(")}</svg>'
def rings():
    t=[('32°C+',90,C['red']),('20°C+',160,C['per']),('15~16°C',230,C['hon']),('10°C',300,'#C9BFA8')]
    cs=''.join(f'<circle cx="320" cy="320" r="{r}" fill="{c}" opacity=".9"/>' for _,r,c in reversed(t))
    ls=''.join(f'<text x="{320}" y="{320-r+48 if r>90 else 335}" font-size="{40 if r>90 else 46}" font-weight="700" text-anchor="middle" fill="#fff" font-family="Noto Sans CJK KR">{l}</text>' for l,r,_ in t)
    return f'<svg width="640" height="640">{cs}{ls}</svg>'
def step(n,t,s):
    return f'<div style="display:flex;gap:28px;align-items:flex-start;margin:18px 0"><div style="flex:none;width:80px;height:80px;border-radius:50%;background:{C["g"]};color:#fff;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div><div><div style="font-size:40px;font-weight:700">{t}</div><div style="font-size:31px;color:#55594F;margin-top:6px;line-height:1.4">{s}</div></div></div>'
def bar(lab,v,w,col,note):
    return f'<div style="margin:22px 0"><div style="font-size:36px;font-weight:700;margin-bottom:10px">{lab}</div><div style="display:flex;align-items:center;gap:20px"><div style="width:{w}px;height:84px;background:{col};border-radius:14px;display:flex;align-items:center;padding-left:26px;color:#fff;font-size:42px;font-weight:700">{v}</div><span style="font-size:30px;color:{C["gray"]}">{note}</span></div></div>'
def tile(v,s):
    return f'<div style="background:#fff;border-radius:24px;padding:30px;border:3px solid {C["line"]};text-align:center"><div style="font-size:64px;font-weight:700;color:{C["g"]}">{v}</div><div style="font-size:30px;margin-top:8px">{s}</div></div>'
IM={}
A='01_gotgam/'
IM[A+'01.jpg']=thumb('제철 이야기','곶감 만들기','깎은 감을<br>60일 바람에 맡깁니다',persim(),'상주에서 배운 곶감 달력')
IM[A+'02.jpg']=card('곶감 달력','감 깎기부터 설까지',step(1,'10월 중순 ~ 11월 초','감을 따서 바로 껍질 깎기')+step(2,'35~40일','반건시 · 속이 말랑')+step(3,'50~60일','곶감 · 상주 둥시는 60일쯤')+step(4,'11월 말 ~ 12월','햇곶감 · 12월에 가장 많이')+step(5,'설 대목','보관해 둔 곶감의 70%가 나감'),'매일신문 · 경북매일')
IM[A+'03.jpg']=card('반건시 곶감 차이','같은 감, 말린 날수만 다릅니다',bar('반건시','35~40일',520,C['per'],'속이 말랑')+bar('곶감(건시)','50~60일',800,C['g'],'겉이 단단 · 색이 짙음')+f'<div style="font-size:34px;line-height:1.5;margin-top:24px">둘 다 떫은감을 깎아 말린 것입니다.</div>','매일신문(2013.10.17)')
IM[A+'04.jpg']=card('집에서 곶감 만들기','네 가지만 보세요',step(1,'단단한 떫은감','꼭지가 붙어 있는 것')+step(2,'비 안 맞고 바람 드는 그늘','베란다는 낮밤 온도 차이에 주의')+step(3,'서로 닿지 않게','눅눅하면 곰팡이가 피기 쉬움')+step(4,'겉을 보고 판단','끈적한 물기 · 하얀 솜은 의심'),'바람 · 습도 조건: 머니투데이(2026.1.14)')
IM[A+'05.jpg']=card('상주곶감 숫자로 보기','전국 곶감의 60%가 상주에서',f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">{tile("60%","전국 생산량 중")}{tile("560여 년","이어 온 방식")}{tile("5천여","곶감 농가")}{tile("3천억 원+","한 해 매출")}</div><div style="font-size:32px;line-height:1.5;margin-top:30px">국가중요농업유산 · 2027년 1월 22~24일 상주곶감축제</div>','매일신문(2026.11.9)')
B='02_bee_winter/'
IM[B+'01.jpg']=thumb('꿀 공부','꿀벌<br>겨울나는법','겨울잠 대신 뭉쳐서<br>한가운데 32도',f'<div style="transform:scale(.62);transform-origin:top right">{rings()}</div>','양봉 농가의 겨울')
IM[B+'02.jpg']=card('꿀벌 겨울나는법','바깥 7도일 때 벌통 안',f'<div style="display:flex;align-items:center;gap:30px"><div style="transform:scale(.82);transform-origin:left center;width:530px">{rings()}</div><div style="font-size:32px;line-height:1.7">가운데 <b style="color:{C["red"]}">32°C+</b><br>안쪽 <b style="color:{C["per"]}">20°C+</b><br>겉 <b style="color:{C["gold"]}">15~16°C</b><br>벌통 안 <b>10°C</b></div></div><div style="font-size:32px;line-height:1.5;margin-top:16px">추운 벌은 안으로, 안쪽 벌은 밖으로 자리를 바꿉니다.</div>','「꿀벌의 월동관리 요령」 농업 기술 자료')
IM[B+'03.jpg']=card('꿀벌 월동 성공률','추위보다 무서운 건 「들쭉날쭉」',bar('전체 월동 성공률','69.1%',720,C['g'],'농촌진흥청 조사')+bar('2022~2023 겨울 실패','40%+',420,C['red'],'전국 보고')+f'<div style="font-size:33px;line-height:1.5;margin-top:24px">평균 기온보다 <b>기온이 고르게 유지된 곳</b>에서 성공률이 높았습니다.</div>','농촌진흥청 · 국제 학술지 Apidologie')
IM[B+'04.jpg']=card('양봉 농가의 겨울 달력','겨울 준비는 여름 끝에 시작합니다',step(1,'8~9월 · 겨울을 날 일벌 키우기','응애 · 말벌도 이때 가장 많이 늘어남')+step(2,'늦가을 · 약한 무리 합치기','벌집틀 4장 이하는 겨울 넘기기 어려움')+step(3,'겨울 · 벌통 보온 · 지켜보기','문을 열지 않음')+step(4,'봄 · 힘 붙은 무리로 첫 꿀','꽃이 피면 다시 채밀'),'농식품부 민관 합동 조사(2022.3) · 월동관리 요령')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1080})
    for k,h in IM.items():
        pg.set_content(h); pg.wait_for_timeout(250); pg.screenshot(path=str(D/k),type='jpeg',quality=90)
    b.close()
print(len(IM))

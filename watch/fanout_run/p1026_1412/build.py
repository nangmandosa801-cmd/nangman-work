import json
P='<p style="font-size:17px;color:#333;line-height:1.9;">%s</p>'
H='<h2 style="font-size:23px;color:#1F3864;margin:34px 0 12px;">%s</h2>'
NOTE='<span style="color:#777;font-size:14px;">낭만 인테리어는 시공을 직접 하지 않습니다. 집마다 맞는 시공팀을 이어 드리고, 수수료는 시공팀이 냅니다.</span>'
def li(items): return '<ul style="font-size:17px;color:#333;line-height:1.9;">'+''.join('<li><a href="%s" target="_blank">%s</a></li>'%(u,t) for u,t in items)+'</ul>'
def nv(n): return 'https://blog.naver.com/champion_chart/'+n
A=dict(title='영통 자이 프라시엘 사전점검, 견적서 두 장을 나란히 놓으면 무엇이 보일까요',
html=P%NOTE+
P%'<b>물음.</b> 입주예정자협의회가 정한 청소 · 줄눈 견적서가 한 장 도착했습니다. 이 금액이 적당한지 어떻게 아나요?'+
P%'<b>답.</b> 같은 범위로 견적서를 한 장 더 받아 옆에 놓으면 줄마다 차이가 보입니다. 청소 · 새집증후군 금액, 부가세를 넣었는지, 날짜가 하루인지 이틀인지, 박람회 참가비가 들었는지 네 줄만 맞춰 보세요.'+
H%'사전점검은 11월 14일(토) · 15일(일)'+
P%'영통역 자이 프라시엘은 입주박람회 참여 청소 · 줄눈 5곳, 새집증후군 2곳, 중문 3곳이 정해져 있다고 카페 메뉴에 나옵니다. 견적서는 이 팀들에게서 집집이 옵니다. 점검 날에는 타입마다 볼 곳이 다릅니다. 84㎡B는 3면 발코니 세 곳 모두에 물을 부어 배수구로 모이는지 보고, 100㎡는 방과 욕실이 늘어 점검 시간이 2시간을 넘깁니다.'+
H%'중문은 옵션 유무에 따라 점검 날 할 일이 갈립니다'+
P%'모집공고 옵션표의 현관 중문은 3연동 슬라이딩 자동 한 가지이고 84㎡ 230만원, 100㎡ 237만원입니다. 옵션을 넣은 집은 끝까지 열고 닫히는지 센서와 유리 흠을 봅니다. 넣지 않은 집은 현관 폭과 천장까지 사진을 한 장씩 찍어 두면 중문 견적을 사진으로 받을 수 있습니다.'+
H%'견적서 옆에 놓을 두 번째 장'+
P%'낭만 인테리어 기본형 제휴 시공팀은 청소와 새집증후군을 묶어 34평 71만 4천원, 30평 63만원입니다(부가세 별도). 84㎡는 공급 약 33평이라 이 안쪽에 들어갑니다. 에어컨 필터를 떼어 씻으면 1대 1만원이고, 바깥 창 떼어 닦기는 따로 견적입니다. 박람회 참가비가 붙지 않은 금액이라 같은 범위로 맞추면 차이가 바로 보입니다.'+
P%'수도권은 11월 30일까지 낭만 인테리어로 문의하시면 견적 금액에서 5% 할인해 드립니다. 문의 010-2882-8165'+
P%'더 자세한 타입별 점검표와 이웃 30세대 욕실 나노코팅 이야기는 네이버 원문에 있습니다. → <a href="%s" target="_blank"><b>네이버 원문 · 영통역 자이 프라시엘 사전점검, 지정 업체 견적서 옆에 한 장 더 놓고 보세요</b></a>'%nv('224452463443')+
H%'같이 보면 좋은 글'+
li([(nv('224452463443'),'영통역 자이 프라시엘 사전점검, 지정 업체 견적서 옆에 한 장 더 놓고 보세요 (네이버 원문)'),
(nv('224452438208'),'진위역 서희스타힐스 사전점검, 59 · 71 · 84㎡ 평형마다 먼저 볼 곳이 다릅니다'),
(nv('224453190862'),'브레인시티 대광로제비앙 그랜드센텀 사전점검, 중문 달 집이 줄자와 사진 두 장으로 챙길 다섯 가지'),
(nv('224439665559'),'래미안 레벤투스 사전점검일, 입주 45일쯤 전에 날짜가 오니 옵션 자동 중문 268만원과 청소 범위를 그날 같이 보세요'),
(nv('224436117715'),'의왕 센트라인 데시앙 사전점검, 입주 한두 달 전에 하는 이날 현관 치수를 재 두면 중문이 입주 전에 달립니다'),
(nv('224436220073'),'힐스테이트 등촌역 사전점검, 새 집에도 공사 먼지가 남아 있어서 점검 날 서랍 안과 창틀 레일까지 열어 봐야 합니다'),
('https://www.threads.com/@kimdongjin24/post/De8jAruEt89','사전점검 견적서는 한 장 더 받아 나란히 (스레드)'),
('https://blog.naver.com/champion_chart','네이버 블로그 · 낭만 인테리어 전체 글')]))
B=dict(title='입주청소 평당 1만 1천원과 3만원, 세 배 가까운 차이는 어디서 나는지 표로 봅니다',
html=P%NOTE+
P%'<b>물음.</b> 입주청소 평당 가격을 찾으면 1만 1천원과 3만원이 같이 나옵니다. 같은 청소인데 왜 이렇게 벌어지나요?'+
P%'<b>답.</b> 금액 차이는 하는 일의 차이입니다. 평당 1만 1천원 기본형은 입주청소와 새집증후군을 이틀 연달아 묶어 날짜와 사람을 줄인 코스이고, 평당 3만원 고급형은 한 집에 하루를 다 쓰며 떼어서 닦는 코스입니다.'+
H%'기본형 · 30평 63만원, 34평 71만 4천원'+
P%'30평은 청소 33만원에 새집증후군을 묶으면 63만원, 34평은 청소 37만 4천원에 묶으면 71만 4천원입니다(부가세 별도). 새집증후군에는 시공 전후 포름알데히드 · 라돈 측정, 열기를 돌려 40도까지 올리는 베이크아웃, 붙박이장 안 촉매 분사, 가구 잘린 면 코팅, 오존 · 편백 연무, 변기 · 욕실 자외선 살균이 들어갑니다. 작업 사진은 카톡으로 받습니다.'+
H%'고급형 · 평당 3만원, 금액은 현장에서 정합니다'+
P%'30평은 대략 90만원, 34평은 대략 102만원으로 셈하되 분진이 얼마나 남았는지, 분진집중케어를 넣는지에 따라 현장 견적이 정해집니다. 기본 작업에 스팀 살균 · 편백수 연무 · 자외선 살균이 들어가고, 떼어 낸 선반과 수납장을 다시 보고 수전 광택까지 봅니다. 외창을 떼어 닦는 일은 따로 견적입니다.'+
H%'우리 집은 어느 쪽일까'+
P%'금액을 먼저 정하고 새집 냄새까지 한 번에 끝내고 싶으면 기본형, 공사 분진이 많이 남았거나 임산부 · 어린아이가 있거나 테라스 세대처럼 손이 많이 가는 집이면 고급형이 맞습니다. 평수와 날짜만 문자로 보내 주시면 맞는 코스를 알려 드립니다. 문의 010-2882-8165'+
P%'두 코스를 한 장 표로 나란히 놓은 것과 연락 방법은 네이버 원문에 있습니다. → <a href="%s" target="_blank"><b>네이버 원문 · 입주청소 평당 가격, 1만 1천원 코스와 3만원 코스는 하는 일이 이렇게 다릅니다</b></a>'%nv('224452136498')+
H%'같이 보면 좋은 글'+
li([(nv('224452136498'),'입주청소 평당 가격, 1만 1천원 코스와 3만원 코스는 하는 일이 이렇게 다릅니다 (네이버 원문)'),
(nv('224444760801'),'입주청소, 평당 1만원대부터 3만원까지'),
(nv('224451151010'),'입주청소 새집증후군, 묶어서 맡기면 이틀 연달아 잡고 받은 견적보다 낮춥니다'),
(nv('224437558848'),'입주청소 업체 추천, 가격보다 먼저 하루 한 집인지 · 떼어서 닦는지 · 분진 장비가 있는지 봅니다'),
(nv('224433569335'),'입주청소 추가금, 청소하는 날 30만원을 더 달라는 말을 듣지 않으려면 계약 전에 일곱 가지를 문자로 받습니다'),
(nv('224447111398'),'힐스테이트 동작 시그니처 입주청소, 줄눈보다 먼저 하면 두 번 닦습니다'),
(nv('224444852418'),'수원 입주청소 업체 비교, 84타입이 37만~185만원'),
('https://blog.naver.com/champion_chart','네이버 블로그 · 낭만 인테리어 전체 글')]))
import re
for n,d in (('A',A),('B',B)):
    txt=re.sub('<[^>]+>','',d['html']); print(n,len(txt))
    js="const d="+json.dumps(d,ensure_ascii=False)+";"+open('/home/claude/watch/fanout_run/doorlock2/inject_blogger.js').read().split('};',1)[1].lstrip(';') if False else None
    open(n+'.json','w').write(json.dumps(d,ensure_ascii=False))
    code="const d="+json.dumps(d,ensure_ascii=False)+";const fs=[...document.querySelectorAll('iframe')].filter(f=>{try{return f.contentDocument.body.contentEditable=='true'}catch(e){return false}});const ifr=fs.find(f=>f.getBoundingClientRect().width>0);const ti=[...document.querySelectorAll('input[aria-label=\"제목\"],input[aria-label=\"Title\"]')].find(x=>x.getBoundingClientRect().width>0);ti.focus();Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(ti,d.title);ti.dispatchEvent(new Event('input',{bubbles:true}));ti.dispatchEvent(new Event('change',{bubbles:true}));ifr.contentDocument.body.innerHTML=d.html;ifr.contentDocument.body.dispatchEvent(new Event('input',{bubbles:true}));[ti.value,ifr.contentDocument.body.innerText.length]"
    open(n+'.js','w').write(code)
# forbidden check
for w in ['최고','프리미엄','가능성','1위','갈-','업체는','업체가']:
    for n,d in (('A',A),('B',B)):
        if w in d['html'] or w in d['title']: print('HIT',n,w)

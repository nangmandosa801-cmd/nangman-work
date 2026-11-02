import json,re
P='<p style="font-size:17px;color:#333;line-height:1.9;">%s</p>'
H='<h2 style="font-size:23px;color:#1F3864;margin:34px 0 12px;">%s</h2>'
NOTE='<span style="color:#777;font-size:14px;">낭만 인테리어는 시공을 직접 하지 않습니다. 집마다 맞는 시공팀을 이어 드리고, 수수료는 시공팀이 냅니다.</span>'
def li(items): return '<ul style="font-size:17px;color:#333;line-height:1.9;">'+''.join('<li><a href="%s" target="_blank">%s</a></li>'%(u,t) for u,t in items)+'</ul>'
def nv(n): return 'https://blog.naver.com/champion_chart/'+n
T='무타공 중문, 구멍이 없는데 시공형은 왜 25만~37만원이고 셀프는 4만~7만원대일까요'
h=(P%NOTE+
P%'<b>물음.</b> 구멍을 내지 않는 무타공 중문인데 시공형은 25만~37만원, 셀프 접이식은 4만~7만원대입니다. 이 차이는 무엇인가요?'+
P%'<b>답.</b> 문의 무게와 서는 방식이 다릅니다. 셀프 접이식은 압축봉에 얇은 판이나 천을 걸어 시선만 가립니다. 시공형은 알루미늄 틀에 유리를 넣은 문이라 무겁습니다. 그래서 양옆 기둥을 천장과 바닥에 눌러 세우고, 그 위에 레일을 얹습니다. 폭 90cm 기준 25만~37만원이고(2026년 9월 공개 시세), 구멍을 내고 다는 일반 3연동은 55만~90만원대입니다.'+
H%'시공형을 고르기 전에 재 볼 세 곳'+
P%'천장 높이는 양쪽 끝 두 군데를 잽니다. 두 곳이 다르거나 천장이 얇은 판이면 기둥이 누른 자리가 꺼집니다. 현관 폭은 위 · 가운데 · 아래 세 군데를 재서 가장 작은 숫자에 맞춥니다. 신발장이 붙은 집은 신발장 문을 끝까지 열어 기둥이 문을 막지 않는지 봅니다.'+
H%'이사 갈 집이라면'+
P%'구멍을 낸 일반 중문은 뗄 때 10만~30만원이 더 듭니다. 무타공은 기둥 나사를 풀면 끝납니다. 대신 철이 바뀔 때마다 기둥 나사를 한 번씩 다시 조여 주어야 흔들리지 않습니다. 바람을 막는 힘은 일반 중문보다 약합니다.'+
P%'현관 폭과 천장 높이를 찍은 사진 두 장이면 무타공이 되는 집인지 먼저 봐 드립니다. 문의 010-2882-8165'+
P%'기둥이 서는 원리, 금액 한 표, 신발장 옆 시공 사진은 네이버 원문에 있습니다. → <a href="%s" target="_blank"><b>네이버 원문 · 현관 무타공 중문, 셀프는 4만~7만원대 기둥식 시공은 25만~37만원</b></a>'%nv('224454576114')+
H%'같이 보면 좋은 글'+
li([(nv('224454576114'),'현관 무타공 중문, 셀프는 4만~7만원대 기둥식 시공은 25만~37만원 (네이버 원문)'),
(nv('224424176442'),'무타공 중문, 구멍 대신 천장과 바닥을 눌러서 버팁니다'),
(nv('224431136138'),'전세집 중문, 집주인 동의 받고 달거나 무타공으로 답니다'),
(nv('224420365390'),'아파트 중문 가격, 32평이라고 정해지지 않습니다'),
(nv('224430352435'),'중문 철거 비용, 떼는 데 10만~30만원이고 벽과 바닥 자국은 따로 손봅니다'),
(nv('224422168377'),'현관 신발장, 중문을 달 거면 같이 정해야 합니다'),
('https://www.threads.com/@kimdongjin24/post/De9RYOKkhDG','무타공 중문 금액이 두 층인 까닭 (스레드)'),
('https://blog.naver.com/champion_chart','네이버 블로그 · 낭만 인테리어 전체 글')]))
txt=re.sub('<[^>]+>','',h);print(len(txt))
for w in ['최고','프리미엄','가능성','1위','갈라','갈렸','갈랐','업체는','업체가','5%']:
    if w in h+T: print('HIT',w)
code="const T="+json.dumps(T,ensure_ascii=False)+";const H="+json.dumps(h,ensure_ascii=False)+";const cm=document.querySelector('.CodeMirror').CodeMirror;cm.setValue(H);const ti=[...document.querySelectorAll('input')].find(x=>/제목|Title/.test(x.getAttribute('aria-label')||'')&&x.getBoundingClientRect().width>0);ti.focus();Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(ti,T);ti.dispatchEvent(new Event('input',{bubbles:true}));ti.dispatchEvent(new Event('change',{bubbles:true}));[ti.value,cm.getValue().length]"
open('inject.js','w').write(code)

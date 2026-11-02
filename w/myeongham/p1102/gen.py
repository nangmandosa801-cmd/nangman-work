import json,urllib.parse
B='https://nangmanbusinesscards.blogspot.com/search/label/'
def chip(lab,c): return f'<a href="{B}{urllib.parse.quote(lab)}" style="display:inline-block;margin:2px 4px 2px 0;padding:4px 10px;border-radius:14px;background:{c};color:#fff;font-size:14px;text-decoration:none;">{lab}</a>'
LC={'tt_nusu':'누수 · 배관'}
RG={'tt_nusu':'충북','jin_boiler':'전북','mdg_boiler':'전북','cw_boiler':'부산 · 경남','gj_rinnai':'광주 · 전남','ph_boiler':'경북','gh_boiler':'부산 · 경남'}
V=[
 dict(slug='tt_nusu',name='ㅌㅌ 누수설비',cat='누수 · 설비',region='충북',area='청주 전 지역',
  jobs=['누수 탐지 · 화장실 · 우수관 · 베란다 방수','하수구 · 변기 · 싱크대 막힘 뚫기','변기 · 세면대 · 수도꼭지 · 수전 교체','수도 동파 해빙 · 수도 설비','보일러 분배기 · 온수기 설치','화장실 악취 제거','환풍기 · 렌지후드 교체','정화조 뚜껑 · 수도계량기 뚜껑 · 맨홀 교체','아파트 매매 때 하자 점검'],
  lead='청주 전 지역, 누수부터 하수구 · 분배기까지 설비 일을 한 팀이 봅니다',intro='누수 탐지와 방수, 막힘, 수전 교체, 보일러 분배기 교체까지 집 설비 일을 하는 청주 팀입니다.',
  how=['급한 일은 바로 나갑니다','현장을 보고 원인부터 설명합니다','아파트 매매 전 하자 점검도 봅니다']),
 dict(slug='jin_boiler',name='ㅈ 보일러',cat='보일러',region='전북',area='전주',
  jobs=['가스보일러 교체 · 설치 (경동 · 귀뚜라미 · 린나이 · 대성)','콘덴싱 1등급 친환경 보일러','가스 · 전기 온수기','전기보일러','각방 시스템 · 난방 분배기'],
  lead='전주 아파트 보일러 교체, 브랜드별로 맞춰 설치합니다',intro='전주 아파트 · 주택의 보일러와 온수기, 각방 시스템을 시공하는 팀입니다.',
  how=['평형과 배관을 보고 맞는 모델을 고릅니다','기존 각방 시스템을 살려 교체할 수 있는지 봅니다','설치 뒤 사용법을 안내합니다']),
 dict(slug='mdg_boiler',name='ㅁㄷㄱ 보일러',cat='보일러',region='전북',area='전주 주력 · 익산 · 군산 출장',
  jobs=['가스보일러 교체 · 콘덴싱 보일러','구글네스트 · 유선 AI 각방 시스템','난방 분배기 교체 · 각방용 분배기','캐스케이드 시스템','전기온수기'],
  lead='전주 보일러와 각방 시스템, 현장을 보고 견적합니다',intro='가스시설시공업(2종)을 갖춘 전주 보일러 · 각방 시스템 팀입니다.',
  how=['현장을 보고 견적을 냅니다','매립 분배기 누수도 각방용으로 바꿔 답니다','익산 · 군산도 출장 갑니다']),
 dict(slug='cw_boiler',name='ㄱㄷ 보일러',cat='보일러',region='경남',area='창원 · 부산 · 울산',
  jobs=['경동나비엔 보일러 교체 · 설치','각방 제어 시스템','순간 온수기 (LPG 포함)','환기 · 전열교환기'],
  lead='창원 · 부산 경동나비엔 보일러, 각방 제어까지 맞춰 답니다',intro='경동나비엔 보일러와 각방 제어, 온수기를 시공하는 경남 팀입니다.',
  how=['인테리어 중이면 보일러 넣을 시점부터 같이 잡습니다','각방 제어 연동까지 확인합니다','기본 견적을 먼저 드립니다']),
 dict(slug='gj_rinnai',name='ㄹㄴㅇ 보일러',cat='보일러',region='광주 · 전남',area='광주 · 전남',
  jobs=['린나이 보일러 교체 · 설치','보일러 연통 새로 내기','전기온수기 교체','각방 연동','린나이 가스기구 A/S'],
  lead='광주 · 전남 린나이 보일러, 설치부터 A/S까지 맡습니다',intro='린나이 보일러와 가스기구를 설치하고 A/S까지 하는 광주 · 전남 팀입니다.',
  how=['원룸 · 아파트 배관 상태를 먼저 봅니다','연통이 없는 집은 새로 내는 방법을 안내합니다','설치 뒤 A/S도 같은 팀이 봅니다']),
 dict(slug='ph_boiler',name='ㄱㅇㄱ 보일러',cat='보일러',region='경북',area='포항 · 경주 안강 · 강동면',
  jobs=['아파트 보일러 교체','가스보일러 설치','온수기 교체'],
  lead='포항 아파트 보일러 교체, 단지별 현장 사례가 많습니다',intro='포항 아파트 보일러 교체를 주로 하는 팀입니다.',
  how=['단지 · 평형을 알려 주시면 맞는 모델을 안내합니다','교체 당일 설치를 마칩니다','경주 안강 · 강동면도 갑니다']),
 dict(slug='gh_boiler',name='ㄷㅅ 보일러',cat='보일러',region='경남',area='김해 · 창원 · 양산 · 부산 (봄 · 여름엔 경남 전역)',
  jobs=['보일러 교체 · 설치','보일러 수리'],
  lead='김해 · 창원 · 양산 · 부산 보일러 교체를 맡습니다',intro='김해를 중심으로 경남 보일러 교체를 하는 팀입니다.',
  how=['현장을 보고 견적을 냅니다','봄 · 여름엔 경남 전역으로 갑니다','설치 뒤 사용법을 안내합니다']),
]
for v in V:
    lab_c=LC.get(v['slug'],'보일러'); v['region']=RG[v['slug']]
    h=(f'<div style="background:#F4F6F9;border-left:5px solid #2E5C8A;padding:16px 18px;margin:0 0 18px 0;"><p style="margin:0 0 8px 0;font-size:22px;font-weight:700;color:#1F3864;">{v["name"]}</p>'
       f'<p style="margin:0 0 6px 0;">{chip(lab_c,"#2E5C8A")}{chip(v["region"],"#8A6D3B")}</p>'
       f'<p style="margin:6px 0;"><b>일하는 지역</b> · {v["area"]}</p><p style="margin:6px 0;"><b>하는 일</b> · {v["cat"]}</p></div>'
       f'<div id="nm-svc" style="border:2px solid #2E5C8A;border-radius:12px;padding:16px 18px;margin:0 0 22px 0;background:#ffffff;"><p style="margin:0 0 6px 0;font-size:19px;font-weight:700;color:#1F3864;">{v["lead"]}</p><p style="margin:0 0 12px 0;">{v["intro"]}</p>'
       '<p style="margin:0 0 4px 0;"><b style="color:#2E5C8A;">하는 일</b></p><ul style="margin:0 0 10px 0;padding-left:20px;line-height:1.7;">'+''.join(f'<li style="margin:3px 0;">{j}</li>' for j in v['jobs'])+'</ul>'
       f'<p style="margin:0 0 10px 0;"><b style="color:#2E5C8A;">다니는 지역</b> · {v["area"]}</p><p style="margin:0 0 4px 0;"><b style="color:#2E5C8A;">이렇게 일합니다</b></p><ul style="margin:0 0 10px 0;padding-left:20px;line-height:1.7;">'+''.join(f'<li style="margin:3px 0;">{j}</li>' for j in v['how'])+'</ul>'
       '<p style="margin:8px 0 0 0;padding:10px 12px;background:#F4F6F9;border-radius:8px;">가격은 집 상황을 보고 낭만 인테리어가 따로 안내합니다.<br>전화 · 문자 <b>010-2882-8165</b></p></div>'
       '<div style="border:2px solid #1F3864;border-radius:10px;padding:14px 16px;margin:20px 0;"><p style="margin:0;"><b style="color:#1F3864;">시공 사례 · 문의</b><br>사례와 문의는 <a href="https://blog.naver.com/champion_chart" target="_blank" rel="noopener">낭만 인테리어 블로그</a>에서 받습니다. 사는 동네와 집 상태를 남겨 주시면 맞는 팀으로 이어 드립니다.</p></div>'
       '<h2>함께 보면 좋은 글</h2><ul><li style="margin:8px 0;"><a href="https://nangmanbusinesscards.blogspot.com/search/label/%EC%A0%9C%ED%9C%B4%20%EC%97%85%EC%B2%B4" style="color:#1F3864;">제휴 시공팀 모아 보기</a></li></ul>'
       f'<p>같은 일을 하는 다른 시공팀 보기 → {chip(lab_c,"#2E5C8A")}</p><p>같은 지역 시공팀 보기 → {chip(v["region"],"#8A6D3B")}</p>'
       '<p style="font-size:13px;color:#8A8578;">낭만 명함은 낭만 인테리어와 제휴한 시공팀을 지역 · 업무별로 모아 소개합니다.</p>')
    v['title']=f'{v["name"]} · {" · ".join(v["jobs"][0].split(" · ")[:2])} · {v["area"].split(" (")[0]} · 낭만 명함 제휴 업체'
    v['labels']=[lab_c,v['region'],'제휴 업체']+(['동파 · 해빙','하수구'] if v['slug']=='tt_nusu' else [])
    open(f'{v["slug"]}.html','w').write(h)
json.dump([{k:v[k] for k in ('slug','name','title','labels')} for v in V],open('pages.json','w'),ensure_ascii=False,indent=1)
for v in V: print(v['title'])

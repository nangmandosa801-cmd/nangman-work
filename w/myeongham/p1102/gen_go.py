import json,urllib.parse
B='https://nangmanbusinesscards.blogspot.com/search/label/'
def chip(lab,c): return f'<a href="{B}{urllib.parse.quote(lab)}" style="display:inline-block;margin:2px 4px 2px 0;padding:4px 10px;border-radius:14px;background:{c};color:#fff;font-size:14px;text-decoration:none;">{lab}</a>'
LC={'tt_nusu':'누수 · 배관','go_nusu':'누수 · 배관'}
RG={'go_nusu':'울산','tt_nusu':'충북','jin_boiler':'전북','mdg_boiler':'전북','cw_boiler':'부산 · 경남','gj_rinnai':'광주 · 전남','ph_boiler':'경북','gh_boiler':'부산 · 경남'}
V=[
 dict(slug='go_nusu',name='ㄱㅊㄱ 누수설비',cat='누수 · 방수 · 설비',region='울산',area='울산',
  jobs=['누수 탐지 공사','방수 공사','누수로 생긴 피해 복구 공사','상가 · 주택 · 아파트 설비'],
  lead='울산 누수 탐지부터 방수, 피해 복구까지 한 팀이 맡습니다',intro='울산의 상가 · 주택 · 아파트 누수를 찾고 방수와 피해 복구 공사까지 하는 팀입니다.',
  how=['출장비는 받지 않습니다','누수 자리를 찾은 뒤 방수와 복구 범위를 설명합니다','공사 뒤 보증 기간은 1년입니다']),
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
    v['labels']=[lab_c,v['region'],'제휴 업체']+(['동파 · 해빙','하수구'] if v['slug']=='tt_nusu' else ['방수'] if v['slug']=='go_nusu' else [])
    open(f'{v["slug"]}.html','w').write(h)
json.dump([{k:v[k] for k in ('slug','name','title','labels')} for v in V],open('pages_go.json','w'),ensure_ascii=False,indent=1)
for v in V: print(v['title'])

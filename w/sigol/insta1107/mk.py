import asyncio
from playwright.async_api import async_playwright
CSS="""*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;font-family:'Noto Sans CJK KR',sans-serif;background:#f3efe2;color:#25261d;overflow:hidden}
.s{height:1350px;padding:90px 80px;display:flex;flex-direction:column}.k{font-size:34px;font-weight:700;color:#8a6d16;letter-spacing:.03em}
.t{font-size:84px;font-weight:900;line-height:1.2;margin:24px 0 40px}.t2{font-size:70px;font-weight:900;line-height:1.22;margin:20px 0 44px}
.p{font-size:44px;line-height:1.55}.box{background:#fff;border:4px solid #d9cfa6;border-radius:28px;padding:40px 44px;margin-bottom:28px}
.g{background:#3c5a28;color:#fff;border-color:#3c5a28}.box h3{font-size:50px;margin-bottom:14px}.box p{font-size:42px;line-height:1.5}
.y{color:#b3860f}.r{color:#b03a2e}.big{font-size:120px;font-weight:900;color:#b3860f;line-height:1}
.ft{margin-top:auto;font-size:30px;color:#7d7863;display:flex;justify-content:space-between}.n{font-weight:800;color:#3c5a28}
.cover{background:#3c5a28;color:#fff}.cover .k{color:#e8c95b}.cover .ft{color:#cfd8c4}.cover .n{color:#e8c95b}"""
F=lambda i:f'<div class=ft><span class=n>낭만 시골</span><span>{i}/8{"" if i==8 else " →"}</span></div>'
S=[
f'''<div class="s cover"><div class=k>귀산촌 · 귀농 준비 노트</div><div class=t style="font-size:100px;margin-top:120px">귀농이랑<br>귀산촌,<br><span style="color:#e8c95b">둘 다</span><br>할 수 있을까?</div><div class=p style="color:#e6ecdf">산 한 자락으로 두 가지 지원을<br>같이 챙기는 방법</div>{F(1)}</div>''',
f'''<div class=s><div class=k>먼저 차이부터</div><div class=t2>둘은 담당 부처가<br>다릅니다</div>
<div class=box><h3>귀농</h3><p>농식품부 · 농업과 <b>축산</b><br>논밭 · 소 · 닭 · <b class=y>꿀벌</b></p></div>
<div class="box g"><h3>귀산촌</h3><p>산림청 · <b>임업</b><br>산나물 · 약초 · 밤 · 나무</p></div>{F(2)}</div>''',
f'''<div class=s><div class=k>답</div><div class=t2>한 산에서<br>두 가지를 같이</div>
<div class=box><h3>벌통 10~30개</h3><p>꿀벌은 축산법상 <b>가축</b><br>→ <b class=y>귀농인</b></p></div>
<div class="box g"><h3>밀원수 · 산나물</h3><p>쉬나무 · 헛개 · 산마늘<br>→ <b>임업인 (귀산촌)</b></p></div>
<div class=p style="font-size:38px">밀원수는 벌 먹이도 됩니다</div>{F(3)}</div>''',
f'''<div class=s><div class=k>양봉으로 귀농인 되기</div><div class=t2>벌통 몇 개부터?</div>
<div class=box><p><b class=big>10군</b><br>꿀벌 10군 이상 키우면 농업인</p></div>
<div class=box><p>판매하려면 양봉농가 등록<br>토종벌 10군 · 서양벌 30군 이상</p></div>
<div class="box g"><p>2024년 10월부터<br><b>산(임야)에서 양봉해도</b><br>농업경영체 등록 가능</p></div>{F(4)}</div>''',
f'''<div class=s><div class=k>산나물로 임업인 되기</div><div class=t2>넓은 산 없어도<br>됩니다</div>
<div class=box><h3>넷 중 하나만</h3><p>① 산림 3ha 이상<br>② 1년에 <b class=y>90일</b> 이상 임업<br>③ 임산물 판매 <b class=y>120만 원</b> 이상<br>④ 산림조합 조합원</p></div>
<div class="box g"><p>300평(1,000㎡) 산나물로도<br>②나 ③을 채울 수 있습니다</p></div>{F(5)}</div>''',
f'''<div class=s><div class=k>받을 수 있는 돈</div><div class=t2>대부분 융자,<br>현금은 조금</div>
<div class=box><p>창업자금 <b>최대 3억</b> · 연 2% 융자<br><span class=r>귀농 + 귀산촌 합쳐 3억까지</span></p></div>
<div class=box><p>주택자금 <b>최대 7,500만 원</b> · 연 2%</p></div>
<div class="box g"><p>괴산군 현금 보조<br>설계비 200만 · 수리비 500만</p></div>{F(6)}</div>''',
f'''<div class=s><div class=k>많이 하는 오해</div><div class=t2>이건 아닙니다</div>
<div class=box><p><span class=r>✕</span> 임업직불금 <b>월</b> 130만 원<br><b>→ 1년에 한 번</b></p></div>
<div class=box><p><span class=r>✕</span> 혼자 내려오면 부부가 따로<br><b>→ 배우자는 같은 임가</b></p></div>
<div class=box><p><span class=r>✕</span> 산 사서 바로 집 짓기<br><b>→ 임업인 · 660㎡ 미만 · 실거주</b></p></div>{F(7)}</div>''',
f'''<div class="s cover"><div class=k>순서 정리</div><div class=t2 style="color:#fff">이 순서로<br>준비합니다</div>
<div class=p style="font-size:42px;line-height:1.8;color:#eef2e8">① 귀농 · 귀산촌 교육 듣기<br>② 마을 안 집 먼저 · 전입<br>③ 벌통 몇 개로 배우기<br>④ 산에 산나물 · 밀원수<br>⑤ 10군 넘으면 양봉농가 등록<br>⑥ 군청 · 산림조합에 서면 확인</div>
<div class=p style="font-size:34px;color:#e8c95b;margin-top:30px">자세한 표와 출처는 블로그 「낭만 시골」</div>{F(8)}</div>''',
]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,h in enumerate(S,1):
            await pg.set_content(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{h}</body></html>")
            await pg.screenshot(path=f"nangman_sigol_귀농귀산촌_{i:02d}.png")
        await b.close()
asyncio.run(main())

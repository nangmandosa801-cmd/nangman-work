import asyncio
from playwright.async_api import async_playwright
CSS="""*{box-sizing:border-box;margin:0}body{width:1080px;font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif;background:#f4f1e6;color:#2b2a22}
.c{padding:64px 64px 56px}.k{font-size:30px;color:#7a6a2a;font-weight:700;letter-spacing:.04em}.t{font-size:58px;font-weight:800;line-height:1.25;margin:14px 0 36px}
.row{display:flex;gap:22px;align-items:stretch}.box{flex:1;background:#fff;border:3px solid #d8cfa8;border-radius:22px;padding:30px}
.box h3{font-size:36px;margin-bottom:14px}.box p{font-size:30px;line-height:1.5}.hl{background:#3d5a2a;color:#fff;border-color:#3d5a2a}
.arrow{font-size:60px;align-self:center;color:#b08a1e;font-weight:800}.big{font-size:64px;font-weight:900;color:#b08a1e}
table{width:100%;border-collapse:collapse;font-size:32px;background:#fff;border-radius:18px;overflow:hidden}td,th{padding:22px 24px;border-bottom:2px solid #e6dfc4;text-align:left}th{background:#3d5a2a;color:#fff}
.f{font-size:24px;color:#8a8470;margin-top:28px}.x{color:#a33}.o{color:#3d5a2a;font-weight:800}"""
CARDS={
"1_양봉귀농순서":"""<div class=c><div class=k>낭만 시골 · 귀농 양봉</div><div class=t>산에서 벌 키우면<br>귀농인이 되는 순서</div>
<div class=row><div class=box><h3>① 농업인</h3><p>꿀벌<br><b class=big>10군</b><br>이상 사육</p></div><div class=arrow>→</div>
<div class=box><h3>② 양봉농가 등록</h3><p>판매 목적<br>토종벌 10군↑<br>서양벌 30군↑</p></div><div class=arrow>→</div>
<div class="box hl"><h3>③ 농업경영체</h3><p>2024.10부터<br>임야 양봉도<br>등록 가능</p></div></div>
<div class=f>꿀벌은 축산법상 가축 · 산림청 2025.11 공문: 산지 양봉시설은 축산시설</div></div>""",
"2_귀농지원표":"""<div class=c><div class=k>낭만 시골 · 귀농 양봉</div><div class=t>귀농인이 되면<br>받을 수 있는 지원</div>
<table><tr><th>지원</th><th>금액</th><th>형태</th></tr>
<tr><td>귀농 창업자금</td><td><b>최대 3억 원</b></td><td>연 2% 융자</td></tr>
<tr><td>귀농 주택자금</td><td><b>최대 7,500만 원</b></td><td>연 2% 융자</td></tr>
<tr><td>괴산 신축 설계비</td><td><b>최대 200만 원</b></td><td class=o>현금 보조</td></tr>
<tr><td>괴산 주택 수리비</td><td><b>500만 원</b></td><td class=o>현금 보조</td></tr></table>
<div class=f>귀농자금 + 귀산촌자금 합쳐 3억 원까지 · 전입 5~6년 안 · 전입 전 1년 이상 도시 거주 · 귀농 교육</div></div>""",
"3_직불금130":"""<div class=c><div class=k>낭만 시골 · 임업직불금</div><div class=t>소규모 임가 직불금<br><span class=big>130만 원</span>은 <u>1년에 한 번</u></div>
<table><tr><th>질문</th><th>답</th></tr>
<tr><td>월 130만 원?</td><td class=x>아니요, 연 1회</td></tr>
<tr><td>1인 가구도?</td><td class=o>네, 1인 세대도 임가</td></tr>
<tr><td>혼자 내려와 세대를 나누면?</td><td class=x>배우자는 같은 임가</td></tr>
<tr><td>지금 산 사서 바로?</td><td class=x>어려움 (2019.4~2022.9 등록 산지 · 3년 종사 · 3년 거주)</td></tr>
<tr><td>양봉만으로?</td><td class=x>대상 품목 아님</td></tr></table>
<div class=f>근거: 임업직불제법 시행령 제3조 · 제9조, 2026년 임업직불사업 공고</div></div>""",
"4_한산두가지":"""<div class=c><div class=k>낭만 시골 · 제 귀산촌 계획</div><div class=t>한 산에서 두 가지</div>
<div class=row><div class=box><h3>🐝 양봉 = 축산</h3><p>벌통 10~30개<br>→ <b>귀농인</b><br>귀농 창업 · 주택 지원</p></div>
<div class="box hl"><h3>🌳 밀원수 · 산나물 = 임업</h3><p>쉬나무 · 헛개 · 산나물<br>→ <b>임업인</b><br>90일 종사 또는 판매 120만 원</p></div></div>
<div class=row style="margin-top:22px"><div class=box><p>쉬나무 1ha 꿀 <b class=big>400kg</b> · 아까시나무 38kg의 10배 넘음 (국립산림과학원)</p></div></div>
<div class=f>집은 마을 안에 · 산에는 벌통과 33㎡ 이하 쉼터(2026년 하반기 시행)</div></div>""",
}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':800},device_scale_factor=1)
        for n,h in CARDS.items():
            await pg.set_content(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{h}</body></html>")
            await pg.screenshot(path=f"nangman_sigol_{n}.png",full_page=True)
        await b.close()
asyncio.run(main())

# 10/18 13:09 사용자 「소소리 중문 사진 이쁘게 나온거 공사 사진도 같이 올리고 S사 시공이라고 해줘 다 구분해서 고객이 고르게 하자」
# 구글 명함 블로그(nangmanbusinesscards) · 손님용 · 디에이치 방배 84A 중문 견적 (S사 = 소소리 · 10/18 13:08 견적)
# 사진: 소소리 rodeosky 224442373006 · 224420797808 · 224428303486 · 224433921468 · 224439036713 (다른 아파트 시공 사례)
import json,re
title="디에이치 방배 84A 입주 견적, 중문 · 입주청소 · 줄눈 · 매트를 한 장에 모아 품목별로 고릅니다"
B='style="font-size:17px;line-height:1.9"'
H='style="font-size:22px;margin:38px 0 12px;color:#1f3864"'
td='style="padding:10px;border:1px solid #ccd;text-align:center"'
tl='style="padding:10px;border:1px solid #ccd"'
th='style="padding:10px;border:1px solid #ccd;background:#1f2d4d;color:#fff"'
T='style="width:100%;border-collapse:collapse;font-size:16px"'
CAP='style="font-size:14px;color:#666;text-align:center;margin:4px 0 22px"'
def img(n,cap): return f'{{IMG:{n}}}\n<p {CAP}>{cap}</p>'
BOX='style="background:#F2F4F7;border-left:4px solid #2E5C8A;padding:16px 20px;font-size:17px;line-height:1.9;margin:18px 0"'
html=f'''
{{IMG:0}}
<p {B}>디에이치 방배 84A(판상형) 입주 견적을 한 문서에 모았습니다. 현관 중문 · 입주청소 · 줄눈 · 매트, 네 가지입니다. 품목마다 제휴 시공팀의 금액과 시공 사례를 나란히 두었습니다. 필요한 것만 골라 문의하시면 됩니다.</p>
<table {T}>
<tr><th {th}>품목</th><th {th}>시공팀</th><th {th}>금액</th></tr>
<tr><td {tl}><b>① 현관 중문</b></td><td {tl}>S사</td><td {tl}>75만~165만원 · 아래 표</td></tr>
<tr><td {tl}><b>② 입주청소</b></td><td {tl}>경제형 · 고급형(B사 · 이 단지 시공 사례 있음)</td><td {tl}>견적 받는 중</td></tr>
<tr><td {tl}><b>③ 줄눈 · 탄성코트</b></td><td {tl}>J사</td><td {tl}>견적 받는 중</td></tr>
<tr><td {tl}><b>④ 강아지 · 층간소음 매트</b></td><td {tl}>M사</td><td {tl}>견적 받는 중</td></tr>
</table>
<p {CAP}>금액은 실측 전 금액 · 2026년 10월 18일부터 받은 순서로 채웁니다</p>

<h2 style="font-size:26px;margin:44px 0 10px;color:#0f1116">① 현관 중문 · S사</h2>
<p {B}>이 단지 옵션 중문은 자동 중문 244만원 한 가지였습니다. 옵션을 넣지 않은 집은 현관에 중문이 없습니다. 아래 금액은 S사가 10월 18일에 보내 준 실측 전 금액입니다. 사진은 S사가 다른 아파트에 시공한 사례입니다.</p>

<h3 {H}>S사 금액 (만원 · 실측 전)</h3>
<table {T}>
<tr><th {th}>문 종류</th><th {th}>투명유리</th><th {th}>모루유리</th></tr>
<tr><td {tl}><b>3연동</b></td><td {td}>80</td><td {td}>85</td></tr>
<tr><td {tl}><b>3연동 자동</b></td><td {td}>160</td><td {td}>165</td></tr>
<tr><td {tl}><b>원슬라이딩</b></td><td {td}>75</td><td {td}>80</td></tr>
<tr><td {tl}><b>원슬라이딩 자동</b></td><td {td}>140</td><td {td}>145</td></tr>
</table>
<p {CAP}>S사 견적 · 2026년 10월 18일 · 철거비는 현관 사진을 보고 10~20만원</p>

<div {BOX}><b>옵션 자동 중문 244만원과 비교하면</b><br>
▸ S사 3연동 자동(투명) 160만원 · 옵션보다 84만원 적습니다<br>
▸ S사 원슬라이딩 자동(투명) 140만원 · 옵션보다 104만원 적습니다<br>
▸ 손으로 여는 3연동(투명)은 80만원입니다<br>
▸ 중문이 없는 집은 떼어 낼 문이 없습니다. 철거비가 붙는지는 현관 사진으로 확인합니다</div>

<h3 {H}>① 3연동 · 문 세 짝이 겹치며 옆으로 열립니다</h3>
<p {B}>문 세 짝이 줄로 이어져 같이 움직입니다. 다 열면 세 짝이 입구 한쪽에 모입니다. 옆 벽이 넓지 않아도 달 수 있습니다. 손으로 여는 3연동은 80만원(투명) · 85만원(모루)입니다.</p>
{img(1,'S사 시공 · 서울 상계주공4단지 · 초슬림 3연동 · 화이트 · 세로 모루유리 · 닫은 모습')}
{img(2,'S사 시공 · 같은 집 · 세 짝을 한쪽으로 모아 연 모습')}
{img(3,'S사 시공 · 서울 답십리 동서울한양 · 초슬림 3연동 · 우드 틀 · 미스트 유리')}
{img(4,'S사 시공 · 의정부 호원우성3차 · 초슬림 3연동 · 화이트 · 위 투명 · 아래 샤틴(고시)')}

<h3 {H}>② 원슬라이딩 · 큰 문 한 짝이 옆으로 밀립니다</h3>
<p {B}>문 한 짝이 벽을 따라 옆으로 밀려 열립니다. 틀이 적어 유리 면이 넓어 보입니다. 다만 옆 벽에 열린 문 한 짝이 붙을 만큼 빈 벽이 있어야 합니다. 84A 현관 옆 벽 폭은 실측 때 확인합니다. 손으로 여는 원슬라이딩은 75만원(투명) · 80만원(모루)입니다.</p>
{img(6,'S사 시공 · 남양주 오남 쌍용스윗닷홈 · 원슬라이딩 · 우드 틀 · 부분 간살 · 투명 강화유리')}
{img(7,'S사 시공 · 서울 은평뉴타운 아이파크 · 원슬라이딩 · 간살 · 패브릭 접합유리')}

<h3 {H}>③ 자동 · 다가가면 문이 스스로 열립니다</h3>
<p {B}>3연동과 원슬라이딩 모두 자동으로 바꿀 수 있습니다. 장을 보고 두 손에 짐을 든 날이나 아이를 안고 들어오는 날에 편합니다. 3연동 자동은 160만원(투명) · 165만원(모루), 원슬라이딩 자동은 140만원(투명) · 145만원(모루)입니다.</p>

<h3 {H}>중문 공사는 이렇게 끝납니다</h3>
{img(5,'S사 시공 · 의정부 호원우성3차 · 막 달아 보호 비닐이 붙은 3연동 · 현관 쪽에서 본 모습')}
{img(8,'S사 시공 · 은평 아이파크 · 바닥 마루 위에 올린 원슬라이딩 레일 · 마루를 깨지 않고 얹습니다')}
<p {B}>S사는 집에 와서 현관 입구를 직접 재고 문을 그 치수로 따로 만듭니다. 84A 현관 바닥은 600각 타일, 거실 바닥은 동화마루 7.5T입니다. 레일은 이 두 바닥이 만나는 선에 맞춰 올립니다.</p>

<h3 {H}>중문 유리는 이렇게 고릅니다</h3>
<table {T}>
<tr><th {th}>유리</th><th {th}>보이는 모습</th><th {th}>이런 집에</th></tr>
<tr><td {tl}><b>투명</b></td><td {tl}>문 너머 복도가 다 보입니다</td><td {tl}>현관이 어두워 빛을 많이 들이고 싶은 집</td></tr>
<tr><td {tl}><b>모루</b></td><td {tl}>세로줄 무늬로 안쪽이 흐릿합니다 · 5만원 더</td><td {tl}>현관에서 거실이 훤히 보이는 것이 싫은 집</td></tr>
</table>

<h2 style="font-size:26px;margin:44px 0 10px;color:#0f1116">② 입주청소 · 경제형 · 고급형</h2>
<p {B}>B사는 이 단지, 디에이치 방배 새 아파트의 입주청소를 이미 했습니다. 수납장 선반과 서랍을 모두 떼어 내 닦고, 레일과 모서리에 쌓인 공사 분진까지 걷어 냅니다. 새집증후군 저감(광촉매 · UVC · 편백수)도 같이 맡깁니다.</p>
{img(9,'B사 시공 · 디에이치 방배 · 서랍과 선반을 모두 빼낸 주방')}
{img(10,'B사 시공 · 디에이치 방배 · 서랍 레일에 쌓여 있던 공사 분진')}
{img(11,'B사 시공 · 디에이치 방배 · 서랍장 칸마다 비추는 UVC')}
<h3 {H}>입주청소는 두 가지 중에 고릅니다</h3>
<table {T}>
<tr><th {th}>구분</th><th {th}>경제형</th><th {th}>고급형</th></tr>
<tr><td {tl}><b>이런 집에</b></td><td {tl}>새 아파트 기본 청소면 되는 집</td><td {tl}>아이 · 반려동물이 있거나 냄새 · 먼지가 걱정인 집</td></tr>
<tr><td {tl}><b>바닥 · 창 · 욕실 · 주방</b></td><td {td}>✔</td><td {td}>✔</td></tr>
<tr><td {tl}><b>공사 스티커 · 실리콘 찌꺼기</b></td><td {td}>✔</td><td {td}>✔</td></tr>
<tr><td {tl}><b>서랍 · 선반 떼어 내 닦기</b></td><td {td}>—</td><td {td}>✔</td></tr>
<tr><td {tl}><b>레일 · 모서리 분진 집중케어</b></td><td {td}>—</td><td {td}>✔</td></tr>
<tr><td {tl}><b>새집증후군 저감 (광촉매 · UVC · 편백수)</b></td><td {td}>—</td><td {td}>✔</td></tr>
<tr><td {tl}><b>금액 (84㎡)</b></td><td {td}>견적 받는 중</td><td {td}>견적 받는 중</td></tr>
</table>
<p {CAP}>고급형은 B사가 이 단지에서 한 방식 · 경제형은 B사와 다른 제휴 청소팀에 같이 받는 중</p>
<p {B}>추가 요금이 붙는 경우와 A/S 기간도 같이 받아 적습니다. 금액이 오는 대로 이 표를 채웁니다.</p>

<h2 style="font-size:26px;margin:44px 0 10px;color:#0f1116">③ 줄눈 · 탄성코트 · J사</h2>
<p {B}>줄눈은 타일 사이 틈을 메우는 공사입니다. 입주청소보다 먼저 해야 청소를 두 번 하지 않습니다. 욕실 두 곳 · 현관 · 베란다 바닥을 나눠 견적을 받습니다. 재료는 폴리우레아와 케라폭시 두 가지로 받습니다.</p>
{img(12,'J사 시공 · 경기 입주 전 집 · 줄눈을 넣은 직후 하얀 자국이 남은 바닥')}
{img(13,'J사 시공 · 같은 집 · 줄눈을 마친 베란다 바닥')}

<h2 style="font-size:26px;margin:44px 0 10px;color:#0f1116">④ 강아지 · 층간소음 매트 · M사</h2>
<p {B}>마루 위에 까는 매트입니다. 반려견이 미끄러지지 않고, 아래층으로 가는 발소리가 줄어듭니다. 84A 거실과 복도에 깔 때 금액을 두께별로 받습니다. 청소가 끝난 뒤 깔아야 들뜨지 않습니다.</p>
{img(14,'M사 시공 · 서울 서초 · 거실 전체에 깐 2.2cm 매트')}
{img(15,'M사 시공 · 같은 집 · 긴 복도까지 이어 깐 매트')}

<h3 {H}>네 가지를 같이 한다면 이 순서로</h3>
<ol {B}>
<li>줄눈 · 탄성코트 · 빈집에 먼저</li>
<li>중문 · 레일을 올린 뒤 먼지를 같이 치웁니다</li>
<li>입주청소 · 줄눈과 중문 먼지까지 한 번에</li>
<li>매트 · 깨끗한 바닥에 마지막으로</li>
</ol>

<h3 {H}>견적을 받으려면</h3>
<ol {B}>
<li>현관 사진 두 장을 보내 주세요. 현관문 쪽에서 한 장, 거실 쪽에서 한 장.</li>
<li>필요한 품목을 적어 주세요. 예) 「중문 3연동 자동 · 모루 + 입주청소」</li>
<li>시공팀마다 실측 날짜를 직접 잡습니다. 다른 시공팀 금액도 나란히 받아 보실 수 있습니다.</li>
</ol>
<p {B}>문자 · 전화 <b>010-2882-8165</b> (낭만 인테리어)<br>「디에이치 방배 84A」와 필요한 품목을 남겨 주세요.</p>

<div style="border:1px solid #d6dbe6;background:#f5f7fb;padding:18px 20px;margin-top:30px;font-size:16px;line-height:1.9">
<b>함께 보시면 좋은 글</b><br>
· <a href="https://blog.naver.com/champion_chart">네이버 블로그 낭만 인테리어 · 중문 시공 사례와 견적 비교</a><br>
· <a href="https://blog.naver.com/dong_jin_kim">네이버 블로그 낭만 부동산 분석 플랫폼 · 디에이치 방배 단지 분석</a><br>
· <a href="https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_494.html">소개 글 · 남양주 중문 시공팀</a><br>
· <a href="https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_889.html">제휴 시공팀 모아 보기</a><br>
· <a href="https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_137.html">소개 글 · 입주청소 시공팀</a><br>
· <a href="https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_673.html">소개 글 · 줄눈 · 코킹 시공팀</a>
</div>
'''
bad=['자리','갈','어요','예요','고요','최고','프리미엄','가능성','헷갈','놓습니다','가정','까닭','견줘','1위','값','기준','차례로','업체는','업체가','%p','나갈','수수료','소개비','소소리']
txt=re.sub('<[^>]+>','',html+title)
print([b for b in bad if b in txt])
json.dump({'title':title,'html':html.strip()},open('/home/claude/sns/dhbb/dhbb_post.json','w'),ensure_ascii=False)
print(len(html))

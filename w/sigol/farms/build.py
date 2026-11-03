import json
data=json.load(open('all.json'))
order={'충북':0,'충남':1,'세종':1.5,'대전':1.6,'경기':2,'강원':3,'경상':4,'전라':5,'제주':6}
data.sort(key=lambda d:(order[d['reg']], -d['top'], 0 if '010' in d['tel'] else (1 if d['tel'] else 2)))
html=r'''<title>낭만 시골 농장 후보</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@700;800&family=IBM+Plex+Sans+KR:wght@400;500;600&display=swap">
<style>
/* 목록형 도구: 위 요약·필터, 아래 지역별 농장 카드. 전화번호가 제일 잘 보이게 */
:root{--bg:#f5f6f1;--card:#ffffff;--fg:#1f2a22;--mute:#66705f;--line:#dde2d6;--acc:#3f6b3a;--accsoft:#e3ecdc;--star:#a5641f;
--disp:"Nanum Myeongjo",serif;--body:"IBM Plex Sans KR",system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141a15;--card:#1c241d;--fg:#e6ebe1;--mute:#9aa592;--line:#2e3a2f;--acc:#8fbf7f;--accsoft:#25331f;--star:#e0a259;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#141a15;--card:#1c241d;--fg:#e6ebe1;--mute:#9aa592;--line:#2e3a2f;--acc:#8fbf7f;--accsoft:#25331f;--star:#e0a259;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55}
.wrap{max-width:980px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1{font-family:var(--disp);font-size:clamp(26px,5vw,36px);margin:0 0 6px;text-wrap:balance}
.lede{color:var(--mute);margin:0 0 18px;max-width:62ch}
.stats{display:flex;flex-wrap:wrap;gap:8px 20px;margin-bottom:18px;font-variant-numeric:tabular-nums;color:var(--mute)}
.stats b{color:var(--fg);font-size:18px;margin-right:4px}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:10px}
.chip{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:999px;padding:6px 13px;font:inherit;font-size:14px;cursor:pointer}
.chip[aria-pressed="true"]{background:var(--acc);border-color:var(--acc);color:var(--bg)}
.chip:focus-visible,input:focus-visible,button:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
#q{flex:1 1 220px;min-width:0;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;padding:8px 12px;font:inherit}
h2{font-family:var(--disp);font-size:21px;margin:28px 0 10px;display:flex;gap:10px;align-items:baseline}
h2 small{font-family:var(--body);font-size:13px;color:var(--mute);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:10px}
.f{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 15px;display:flex;flex-direction:column;gap:6px;min-width:0}
.f.top{border-color:var(--acc)}
.hd{display:flex;justify-content:space-between;gap:8px;align-items:flex-start}
.nm{font-weight:600;font-size:16px}
.pick{font-size:12px;color:var(--star);font-weight:600;white-space:nowrap;letter-spacing:.02em}
.loc{color:var(--mute);font-size:13px}
.tel{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.num{font-variant-numeric:tabular-nums;font-weight:600;font-size:16px;color:var(--acc);user-select:all}
.none{color:var(--mute);font-size:13px}
.cp{border:1px solid var(--line);background:transparent;color:var(--mute);border-radius:6px;font:inherit;font-size:12px;padding:2px 8px;cursor:pointer}
dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:13.5px}
dt{color:var(--mute)}dd{margin:0;min-width:0;overflow-wrap:anywhere}
.memo{font-size:13px;background:var(--accsoft);border-radius:6px;padding:6px 9px}
a{color:var(--acc)}
.foot{margin-top:30px;color:var(--mute);font-size:13px;max-width:70ch}
</style>
<div class="wrap">
<h1>낭만 시골 농장 후보</h1>
<p class="lede">꿀·약초·산양삼·산나물·표고 농가 탐방 후보입니다. 번호는 판매몰·홈페이지·지자체 안내·기사에 사업장 연락처로 공개된 것만 넣었습니다. 2026년 11월 3일 기준이니 연락 전에 한 번 확인하세요.</p>
<div class="stats" id="stats"></div>
<div class="bar" id="cats"></div>
<div class="bar" id="regs"></div>
<div class="bar"><button class="chip" id="t-top" aria-pressed="false">추천만</button><button class="chip" id="t-mob" aria-pressed="false">휴대폰 있는 곳만</button><input id="q" type="search" placeholder="농장·품목 검색 (예: 명이, 꿀, 괴산)"></div>
<div id="list"></div>
<p class="foot">「추천」은 체험·방문이 되고 자체 홍보가 약해 블로그 협업 효과가 클 곳, 또는 협업에 적극적인 곳입니다. 연도 표시가 붙은 번호는 오래된 자료라 바뀌었을 수 있습니다. 번호가 없는 곳은 괴산장터·강원더몰·인제몰 상품 페이지의 판매자 정보에서 다시 찾을 수 있습니다.</p>
</div>
<script>
const D=__DATA__;
const REG=['전체','충북','충남','세종','대전','경기','강원','경상','전라','제주'];
const CAT=['전체','꿀','약초','임산물'];
let cat='전체',reg='전체',onlyTop=false,onlyMob=false,q='';
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
$('#regs').innerHTML=REG.map(r=>`<button class="chip" data-r="${r}" aria-pressed="${r===reg}">${r}</button>`).join('');
$('#regs').onclick=e=>{const b=e.target.closest('[data-r]');if(!b)return;reg=b.dataset.r;document.querySelectorAll('#regs .chip').forEach(c=>c.setAttribute('aria-pressed',c.dataset.r===reg));draw()};
$('#cats').innerHTML=CAT.map(c=>`<button class="chip" data-c="${c}" aria-pressed="${c===cat}">${c==='임산물'?'산양삼·산나물·표고':c}</button>`).join('');
$('#cats').onclick=e=>{const b=e.target.closest('[data-c]');if(!b)return;cat=b.dataset.c;document.querySelectorAll('#cats .chip').forEach(c=>c.setAttribute('aria-pressed',c.dataset.c===cat));draw()};
$('#t-top').onclick=e=>{onlyTop=!onlyTop;e.target.setAttribute('aria-pressed',onlyTop);draw()};
$('#t-mob').onclick=e=>{onlyMob=!onlyMob;e.target.setAttribute('aria-pressed',onlyMob);draw()};
$('#q').oninput=e=>{q=e.target.value.trim();draw()};
function copy(btn,t){const done=()=>{btn.textContent='복사됨';setTimeout(()=>btn.textContent='복사',1200)};
 try{navigator.clipboard.writeText(t).then(done,()=>sel(btn))}catch(e){sel(btn)}}
function sel(btn){const n=btn.previousElementSibling;const r=document.createRange();r.selectNodeContents(n);const s=getSelection();s.removeAllRanges();s.addRange(r)}
function card(d){
 const tels=d.tel?d.tel.split(' / ').map(t=>`<span class="num">${esc(t)}</span><button class="cp" type="button" data-t="${esc(t.replace(/\(.*\)/,''))}">복사</button>`).join(''):'<span class="none">번호 못 찾음</span>';
 const rows=[['대표',d.ceo],['품목',d.item],['체험',d.exp],['SNS',d.sns]].filter(x=>x[1]).map(x=>`<dt>${x[0]}</dt><dd>${esc(x[1])}</dd>`).join('');
 return `<article class="f${d.top?' top':''}"><div class="hd"><span class="nm">${esc(d.name)}</span>${d.top?'<span class="pick">★ 추천</span>':''}</div>
 <div class="loc">${esc(d.cat==='임산물'?'임산물':d.cat)} · ${esc(d.loc)}</div><div class="tel">${tels}</div><dl>${rows}</dl>
 ${d.memo?`<div class="memo">${esc(d.memo)}</div>`:''}<a href="${esc(d.src)}" target="_blank" rel="noopener">출처 보기</a></article>`}
function draw(){
 const f=D.filter(d=>(cat==='전체'||d.cat===cat)&&(reg==='전체'||d.reg===reg)&&(!onlyTop||d.top)&&(!onlyMob||d.tel.includes('010'))&&(!q||(d.name+d.item+d.loc+d.memo+d.reg+d.ceo).includes(q)));
 $('#stats').innerHTML=`<span><b>${f.length}</b>곳</span><span><b>${f.filter(d=>d.tel).length}</b>곳 번호 있음</span><span><b>${f.filter(d=>d.tel.includes('010')).length}</b>곳 휴대폰</span><span><b>${f.filter(d=>d.top).length}</b>곳 추천</span>`;
 const g={};f.forEach(d=>(g[d.reg]=g[d.reg]||[]).push(d));
 $('#list').innerHTML=Object.keys(g).map(r=>`<h2>${r}<small>${g[r].length}곳</small></h2><div class="grid">${g[r].map(card).join('')}</div>`).join('')||'<p class="none">조건에 맞는 농장이 없습니다.</p>';
}
$('#list').onclick=e=>{const b=e.target.closest('.cp');if(b)copy(b,b.dataset.t)};
draw();
</script>'''
open('farms.html','w').write(html.replace('__DATA__',json.dumps(data,ensure_ascii=False)))

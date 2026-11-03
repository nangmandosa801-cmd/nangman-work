window.NC={};
(function(){
const CREAM='#f6ecde',CAR='#d6a062',MUT='#bea892',LINE='#5c4232',BG1='#1c120e',BG2='#342118';
const FF='"Malgun Gothic","Noto Sans KR","Apple SD Gothic Neo",sans-serif';
function cv(w,h){const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');
 const g=x.createRadialGradient(w*.78,h*.25,10,w*.78,h*.25,Math.hypot(w,h)*.75);g.addColorStop(0,BG2);g.addColorStop(1,BG1);x.fillStyle=g;x.fillRect(0,0,w,h);x.textBaseline='top';return [c,x];}
function f(x,s,w){x.font=(w||700)+' '+s+'px '+FF;}
function T(x,t,X,Y,s,c,w,al){f(x,s,w);x.fillStyle=c;x.textAlign=al||'left';x.fillText(t,X,Y);}
function rr(x,a,b,c,d,r){x.beginPath();x.roundRect(a,b,c-a,d-b,r);}
function bean(x,cx,cy,r,col,lw){x.strokeStyle=col;x.lineWidth=lw;x.beginPath();x.ellipse(cx,cy,r*.72,r,0,0,Math.PI*2);x.stroke();
 x.beginPath();for(let i=0;i<=40;i++){const t=i/40,y=cy-r*.86+t*r*1.72,X=cx+Math.sin(t*Math.PI*2)*r*.16;i?x.lineTo(X,y):x.moveTo(X,y);}x.stroke();}
function foot(x,w,h){T(x,'낭만커피',w-70,h-70,28,CAR,700,'right');}
NC.thumb=function(big,sub,chips){const [c,x]=cv(1200,800);bean(x,1030,300,200,'#6e4e38',14);bean(x,1030,300,200,'#8c6446',4);
 T(x,'낭만커피 · 원두 이야기',80,80,34,CAR);x.fillStyle=CAR;x.fillRect(80,140,100,5);
 let s=132;f(x,s,900);while(Math.max(...big.map(l=>x.measureText(l).width))>760){s-=4;f(x,s,900);}
 let y=180;big.forEach(l=>{T(x,l,76,y,s,CREAM,900);y+=Math.round(s*1.18);});
 let ss=44;f(x,ss,500);while(x.measureText(sub).width>780){ss-=2;f(x,ss,500);}T(x,sub,80,y+18,ss,MUT,500);
 let X=80;chips.forEach(t=>{f(x,34,700);const w=x.measureText(t).width+44;x.strokeStyle=CAR;x.lineWidth=3;rr(x,X,650,X+w,714,32);x.stroke();T(x,t,X+22,662,34,CREAM);X+=w+16;});return c;};
NC.profile=function(title,rows,facts,notes){const [c,x]=cv(1200,900);T(x,'한눈에 보는',70,55,36,CAR,500);T(x,title,70,100,72,CREAM,900);T(x,'맛 지도  (일반적인 경향)',70,212,32,MUT);
 let y=275;rows.forEach(([l,v])=>{T(x,l,70,y-4,38,CREAM);for(let i=0;i<5;i++){x.fillStyle=i<v?CAR:LINE;rr(x,200+i*92,y,200+i*92+82,y+36,8);x.fill();}y+=70;});
 x.strokeStyle=LINE;x.lineWidth=3;rr(x,720,270,1130,590,24);x.stroke();let yy=295;facts.forEach(([k,v])=>{T(x,k,750,yy,28,MUT,500);T(x,v,750,yy+36,36,CREAM);yy+=98;});
 T(x,'이런 향이 납니다',70,625,32,MUT);let X=70,yb=680;notes.forEach(n=>{f(x,40,700);const w=x.measureText(n).width+56;if(X+w>1130){X=70;yb+=96;}x.fillStyle='#4a3225';rr(x,X,yb,X+w,yb+76,38);x.fill();T(x,n,X+28,yb+16,40,CREAM);X+=w+18;});foot(x,1200,900);return c;};
NC.hub=function(){const [c,x]=cv(1200,1100);T(x,'한눈에 보는',70,55,36,CAR,500);T(x,'나라별 원두 맛 지도',70,100,72,CREAM,900);T(x,'산미 · 바디 (일반적인 경향)',70,212,32,MUT);
 T(x,'산미',420,285,32,MUT);T(x,'바디',800,285,32,MUT);let y=350;[['브라질',1,3],['콜롬비아',3,3],['과테말라',2,4],['만델링',1,5],['예가체프',4,2],['케냐',5,3],['게이샤',4,1]].forEach(([n,a,b])=>{T(x,n,70,y-6,42,CREAM);
 for(let i=0;i<5;i++){x.fillStyle=i<a?CAR:LINE;rr(x,420+i*70,y,478+i*70,y+36,8);x.fill();x.fillStyle=i<b?'#e8cdaa':LINE;rr(x,800+i*70,y,858+i*70,y+36,8);x.fill();}y+=95;});foot(x,1200,1100);return c;};
NC.acid=function(){const [c,x]=cv(1200,900);T(x,'한눈에 보는',70,55,36,CAR,500);T(x,'신맛이 강해지는 조건',70,100,68,CREAM,900);T(x,'신맛 ↑',520,245,40,CAR);T(x,'신맛 ↓',860,245,40,MUT);
 let y=320;[['자란 곳','높은 산','낮은 땅'],['볶은 정도','연하게','진하게'],['가루 굵기','굵게','가늘게'],['물 온도','낮게','높게']].forEach(([a,b,d])=>{x.strokeStyle=LINE;x.lineWidth=3;rr(x,70,y,1130,y+110,20);x.stroke();T(x,a,110,y+30,42,CREAM);T(x,b,520,y+30,44,CAR);T(x,d,860,y+30,44,MUT);y+=130;});return c;};
NC.roast=function(){const [c,x]=cv(1200,900);T(x,'한눈에 보는',70,55,36,CAR,500);T(x,'로스팅 8단계',70,100,72,CREAM,900);
 [['라이트','#c4a068'],['시나몬','#b07c48'],['미디엄','#966238'],['하이','#80502c'],['시티','#684024'],['풀시티','#52321e'],['프렌치','#3a2418'],['이탈리안','#261a14']].forEach(([n,col],i)=>{const X=70+i*132;x.fillStyle=col;rr(x,X,260,X+120,520,18);x.fill();x.strokeStyle='#785a46';x.lineWidth=2;x.stroke();T(x,n,X+60,545,30,CREAM,700,'center');});
 x.fillStyle=LINE;x.fillRect(70,640,1060,4);T(x,'신맛 · 과일 향',70,670,40,CAR);T(x,'쓴맛 · 그을린 향',1130,670,40,MUT,700,'right');T(x,'1차 크랙 무렵 미디엄 · 하이,  2차 크랙부터 풀시티',600,760,34,MUT,500,'center');foot(x,1200,900);return c;};
NC.D={
b00:[['원두 종류','특징'],'아라비카와 로부스타, 나라별 맛 한눈에',['7개 산지','봉투 읽는 법','맛 지도'],'hub'],
b01:[['브라질 원두'],'세계 커피의 3분의 1이 자라는 넓은 고원',['고소함','산미 적음','블렌드 바탕'],['브라질',[['산미',1],['단맛',3],['바디',3],['쓴맛',3]],[['해발','800~1,300m'],['가공','내추럴'],['등급','No.2 17/18']],['땅콩','밀크초콜릿','캐러멜']]],
b02:[['콜롬비아','수프리모'],'안데스 비탈, 한 해 두 번 수확',['균형','캐러멜','부드러운 산미'],['콜롬비아 수프리모',[['산미',3],['단맛',4],['바디',3],['쓴맛',2]],[['해발','1,200~2,000m'],['가공','워시드'],['등급','수프리모 · 엑셀소']],['캐러멜','사과','견과류']]],
b03:[['케냐 AA'],'적도 고원 붉은 흙의 진한 산미',['자몽','블랙커런트','핸드드립'],['케냐 AA',[['산미',5],['단맛',4],['바디',3],['쓴맛',1]],[['해발','1,500m 이상'],['가공','워시드 (두 번 씻음)'],['등급','AA · AB · PB']],['자몽','블랙커런트','토마토 감칠맛']]],
b04:[['만델링'],'수마트라 토바 호숫가의 묵직한 커피',['묵직함','흙내','라떼'],['만델링',[['산미',1],['단맛',2],['바디',5],['쓴맛',4]],[['산지','수마트라 북부'],['가공','길링 바사'],['등급','G1']],['다크초콜릿','삼나무','비 온 숲']]],
b05:[['과테말라','안티구아'],'세 화산이 둘러싼 골짜기',['초콜릿','스모키','균형'],['과테말라 안티구아',[['산미',2],['단맛',4],['바디',4],['쓴맛',3]],[['해발','약 1,500m'],['가공','워시드'],['등급','SHB']],['다크초콜릿','계피','은은한 연기']]],
g02:[['예가체프'],'꽃향 나는 커피가 자라는 고원 마을',['꽃향','레몬','핸드드립'],['에티오피아 예가체프',[['산미',4],['단맛',3],['바디',2],['쓴맛',1]],[['해발','1,700~2,200m'],['가공','워시드 · 내추럴'],['등급','G1 · G2']],['재스민','레몬','홍차']]],
g01:[['게이샤','커피 유래'],'에티오피아 숲에서 파나마 산비탈까지',['재스민','복숭아','가장 비싼 한 잔'],['게이샤',[['산미',4],['단맛',4],['바디',1],['쓴맛',1]],[['고향','에티오피아 게샤'],['이름난 곳','파나마 보케테'],['알려진 해','2004년']],['재스민','복숭아','베르가못']]],
g03:[['커피 산미','이유'],'커피콩은 원래 빨간 열매의 씨앗',['구연산','사과산','높은 산지'],'acid'],
g04:[['커피 로스팅','단계'],'초록 생두가 갈색 원두가 되기까지 12분',['1차 크랙','8단계','풀시티'],'roast']};
NC.files=async function(k){const d=NC.D[k];const a=NC.thumb(d[0],d[1],d[2]);const p=d[3];const b=typeof p==='string'?NC[p]():NC.profile(...p);
 const tb=c=>new Promise(r=>c.toBlob(r,'image/jpeg',0.9));return [new File([await tb(a)],'coffee_'+k+'_thumb.jpg',{type:'image/jpeg'}),new File([await tb(b)],'coffee_'+k+'_info.jpg',{type:'image/jpeg'})];};
NC.drop=async function(k){const vis=e=>e&&e.getClientRects().length>0;const fr=[...document.querySelectorAll('iframe')].filter(vis).find(x=>{try{return x.contentDocument.body.isContentEditable}catch(e){return false}});
 const fs=await NC.files(k);const dt=new DataTransfer();fs.forEach(f=>dt.items.add(f));const b=fr.contentDocument.body;
 ['dragenter','dragover','drop'].forEach(t=>b.dispatchEvent(new DragEvent(t,{bubbles:true,cancelable:true,dataTransfer:dt})));return fs.map(f=>f.size);};
})();
'render ready'

// 낭만 창고 새 글 편집 화면에서 한 번 실행: 파일 입력(cupl)에 들어간 그림을 편집기에 떨어뜨리고, 주소가 다 나올 때까지 기다려 {파일이름: 주소} JSON을 돌려준다.
(async()=>{const inp=document.getElementById('cupl');const f=[...document.querySelectorAll('iframe')].find(x=>{try{return x.contentDocument&&x.contentDocument.body.isContentEditable}catch(e){return false}});
const b=f.contentDocument.body;const dt=new DataTransfer();[...inp.files].forEach(x=>dt.items.add(x));
for(const t of ['dragenter','dragover','drop'])b.dispatchEvent(new DragEvent(t,{dataTransfer:dt,bubbles:true,cancelable:true,clientX:100,clientY:50}));
const n=inp.files.length;for(let i=0;i<40;i++){await new Promise(r=>setTimeout(r,1000));const s=[...b.querySelectorAll('img')].map(i=>i.src).filter(u=>u.includes('googleusercontent'));if(s.length>=n){const o={};s.forEach(u=>{const m=u.match(/nangman_[a-z0-9]+_([^/]+)\.png$/);if(m)o[m[1]]=u});return JSON.stringify(o)}}return 'timeout'})()

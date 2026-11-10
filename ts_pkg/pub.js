// 티스토리 발행기 (11/10) — 크롬 talk7921 관리 화면에서: (new Function('return '+await (await fetch(RAW+'pub.js')).text()))()(RAW+'<slug>.json')
async (pkgUrl) => {
  const P = await (await fetch(pkgUrl)).json();
  const tags = [];
  let html = P.html;
  for (let i = 0; i < P.imgs.length; i++) {
    const b = await (await fetch(P.imgs[i])).blob();
    const f = new FormData(); f.append('file', b, `${P.slug}_${String(i+1).padStart(2,'0')}.png`);
    const a = await (await fetch('/manage/post/attach.json', {method:'POST', body:f})).json();
    tags.push(a);
    html = html.split(`{{IMG:${i}}}`).join(`<p><img src="${a.url}" alt="${(P.alts||[])[i]||P.title}" style="max-width:100%"></p>`);
  }
  const th = tags[P.thumb||0];
  const body = {id: P.id ? String(P.id) : '0', title: P.title, content: html, slogan: P.slogan||'', visibility: 20,
    category: P.category, tag: P.tags, published: P.at ? P.at : 1, password: '', uselessMarginForEntry: 1, daumLike: '401',
    cclCommercial: 0, cclDerive: 0, thumbnail: th ? th.key : null, type: 'post', attachments: [], recaptchaValue: '', draftSequence: null};
  const r = await fetch('/manage/post.json', {method: P.id ? 'PUT' : 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
  const t = await r.text();
  let u = ''; try { u = JSON.parse(t).entryUrl || ''; } catch(e) {}
  return {status: r.status, slug: P.slug, url: u ? u.replace(/^https?:\/\/[^/]+/, '') : t.slice(0, 120).replace(/[?&=]/g,'_'), imgs: tags.length};
}

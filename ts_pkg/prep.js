async (pkgUrl) => {
  const P = await (await fetch(pkgUrl)).json();
  const up = [];
  let html = P.html;
  for (let i = 0; i < P.imgs.length; i++) {
    const b = await (await fetch(P.imgs[i])).blob();
    const f = new FormData(); f.append('file', b, `${P.slug}_${String(i+1).padStart(2,'0')}.jpg`);
    const a = await (await fetch('/manage/post/attach.json', {method:'POST', body:f})).json();
    up.push(a);
    html = html.split(`{{IMG:${i}}}`).join(`<p><img src="${a.url}" alt="${P.title}" style="max-width:100%"></p>`);
  }
  if (!html.includes(up[0].url)) html = `<p><img src="${up[0].url}" alt="${P.title}" style="max-width:100%"></p>` + html;
  const t = document.querySelector('#post-title-inp, textarea[placeholder*="제목"], input[placeholder*="제목"]');
  if (t) { const s = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(t), 'value').set; s.call(t, P.title); t.dispatchEvent(new Event('input', {bubbles:true})); }
  try { window.tinymce.activeEditor.setContent(html); window.tinymce.activeEditor.fire('change'); } catch(e) {}
  const over = {title: P.title, content: html, category: P.category, tag: P.tags, visibility: 20, thumbnail: up[0].key};
  if (P.at) over.published = P.at;
  const o = XMLHttpRequest.prototype.open, sd = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function(m, u) { this.__u = u; this.__m = m; return o.apply(this, arguments); };
  XMLHttpRequest.prototype.send = function(body) {
    if (this.__u && /\/manage\/post(\/\d+)?\.json/.test(this.__u) && typeof body === 'string') {
      try { const j = JSON.parse(body); Object.assign(j, over); j.attachments = (j.attachments||[]); body = JSON.stringify(j); window.__tsSent = true; } catch(e) {}
    }
    return sd.call(this, body);
  };
  document.title = '준비됨 · ' + P.title.slice(0, 20);
  return {ok: true, slug: P.slug, imgs: up.length, at: P.at || 0, title: !!t};
}

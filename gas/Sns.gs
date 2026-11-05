// ===== 낭만 SNS 예약 — 인스타 · 스레드 공식 API (Upload-Post 대신) =====
// 블로그 우체통2 프로젝트에 새 파일 「Sns」로 붙여 넣는다(Code.gs 아래 칸). 저장 → snsSetup ▶실행 한 번.
// 예약 글 1개 = 드라이브 「블로그/SNS예약/대기」 안 json 파일 1개. snsTick이 10분마다, snsDaily가 매일 새벽 4시에 돈다.
// 스크립트 속성(프로젝트 설정 → 스크립트 속성):
//   TOK_IG_<계정> · TOK_TH_<계정>  계정별 토큰 (예: TOK_IG_fixman, TOK_TH_nowand1969)
//   IG_APP_SECRET · TH_APP_SECRET   짧은 토큰을 60일 토큰으로 바꿀 때만 씀
//   DRY_RUN  1 = 검사만(기본) · 0 = 실제 게시
// 예약 글 모양(json):
// {"id":"fixman_EP001","when":"2026-11-10 21:00","account":"fixman","platforms":["instagram","threads"],
//  "media":[{"drive":"<드라이브 파일 id>"}, …] 또는 [{"url":"https://…jpg"}]   ← 없으면 스레드 글만
//  "caption":"인스타 캡션(해시태그 5개까지)", "threads_text":"스레드 글(없으면 caption · 500자 넘으면 답글로 이어 붙임)",
//  "first_comment":"인스타 첫 댓글", "threads_reply":"스레드 첫 답글", "topic_tag":"스레드 주제"}
// 계정별로 인스타와 스레드 아이디가 다르면 "accounts":{"instagram":"a","threads":"b"} 로 따로 적는다.

var SNS = {
  root: '블로그/SNS예약',
  ig: 'https://graph.instagram.com',
  th: 'https://graph.threads.net/v1.0',
  thRoot: 'https://graph.threads.net',
  lateMin: 360,     // 예약 시각에서 6시간 넘게 지난 글은 올리지 않고 「실패」로
  waitMin: 60,      // 영상 처리 기다리는 최대 시간(분)
  maxTry: 3
};

function snsP_(k, d) { var v = PropertiesService.getScriptProperties().getProperty(k); return (v == null || v === '') ? d : v; }
function snsSetP_(k, v) { PropertiesService.getScriptProperties().setProperty(k, String(v)); }
function snsDry_() { return snsP_('DRY_RUN', '1') !== '0'; }
function snsDir_(name) { return folder_(SNS.root + (name ? '/' + name : ''), true); }
function snsKst_(d) { return Utilities.formatDate(d || new Date(), 'Asia/Seoul', 'yyyy-MM-dd HH:mm'); }
function snsWhen_(s) {
  var m = String(s || '').match(/^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2})/);
  if (!m) throw new Error('when 형식은 YYYY-MM-DD HH:MM (한국 시간)');
  return new Date(m[1] + '-' + m[2] + '-' + m[3] + 'T' + m[4] + ':' + m[5] + ':00+09:00');
}
function snsQs_(o) { return Object.keys(o).map(function (k) { return encodeURIComponent(k) + '=' + encodeURIComponent(o[k]); }).join('&'); }
function snsFetch_(method, url, params, extra) {
  var opt = {method: method, muteHttpExceptions: true};
  if (params && method === 'get') url += (url.indexOf('?') < 0 ? '?' : '&') + snsQs_(params);
  else if (params) opt.payload = params;
  if (extra) for (var k in extra) opt[k] = extra[k];
  var r = UrlFetchApp.fetch(url, opt), c = r.getResponseCode(), t = r.getContentText(), j;
  try { j = JSON.parse(t); } catch (e) { j = {raw: t.slice(0, 300)}; }
  if (c >= 300 || j.error) throw new Error('API ' + c + ' ' + JSON.stringify(j.error || j).slice(0, 400));
  return j;
}
function snsAcct_(item, plat) { return (item.accounts && item.accounts[plat]) || item.account; }
function snsTokKey_(plat, acct) { return 'TOK_' + (plat === 'instagram' ? 'IG' : 'TH') + '_' + acct; }
function snsTok_(plat, acct) {
  var t = snsP_(snsTokKey_(plat, acct), '');
  if (!t) throw new Error('토큰 없음: ' + snsTokKey_(plat, acct));
  return t;
}
function snsUid_(plat, acct) {
  var key = 'UID_' + (plat === 'instagram' ? 'IG' : 'TH') + '_' + acct, v = snsP_(key, '');
  if (v) return v;
  var tok = snsTok_(plat, acct), me;
  if (plat === 'instagram') { me = snsFetch_('get', SNS.ig + '/me', {fields: 'user_id,username', access_token: tok}); v = me.user_id || me.id; }
  else { me = snsFetch_('get', SNS.th + '/me', {fields: 'id,username', access_token: tok}); v = me.id; }
  snsSetP_(key, v); return v;
}

// ── 사진 · 영상 ──
function snsMedia_(item) {
  return (item.media || []).map(function (m) {
    if (typeof m === 'string') m = /^https?:/.test(m) ? {url: m} : {drive: m};
    if (m.drive) {
      var f = DriveApp.getFileById(m.drive), mime = f.getMimeType();
      var video = /^video\//.test(mime) || /\.(mp4|mov)$/i.test(f.getName());
      return {kind: video ? 'video' : 'image', fileId: f.getId(), name: f.getName(), mime: mime, size: f.getSize()};
    }
    return {kind: /\.(mp4|mov)(\?|$)/i.test(m.url) ? 'video' : 'image', url: m.url};
  });
}
function snsDl_(id) { return 'https://drive.usercontent.google.com/download?id=' + id + '&export=download&confirm=t'; }
function snsPublic_(m) {   // 인스타 · 스레드가 가져갈 공개 주소. 사진은 jpg로 바꿔 「_공개」 폴더에.
  if (m.pub) return m.pub;
  if (m.url && (m.kind === 'video' || /\.jpe?g(\?|$)/i.test(m.url))) return (m.pub = m.url);
  var blob, name = 'img';
  if (m.fileId) {
    var f = DriveApp.getFileById(m.fileId);
    if (m.kind === 'video' || /jpe?g/i.test(f.getMimeType())) {
      f.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      return (m.pub = snsDl_(f.getId()));
    }
    blob = f.getBlob(); name = f.getName();
  } else { blob = UrlFetchApp.fetch(m.url).getBlob(); }
  var nf = snsDir_('_공개').createFile(blob.getAs('image/jpeg').setName(name.replace(/\.[^.]+$/, '') + '.jpg'));
  nf.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
  return (m.pub = snsDl_(nf.getId()));
}
function snsTags_(t) { return (String(t || '').match(/#[^\s#]+/g) || []).length; }
function snsSplit_(t, n) {   // 스레드 500자 넘는 글 → 여러 조각(뒤 조각은 답글로)
  t = String(t || '').trim(); var out = [];
  while (t.length > n) {
    var nl = t.lastIndexOf('\n', n), pd = t.lastIndexOf('. ', n - 1);
    var cut = Math.max(nl, pd >= 0 ? pd + 1 : -1);
    if (cut < n * 0.5) cut = n;
    out.push(t.slice(0, cut).trim()); t = t.slice(cut).trim();
  }
  if (t) out.push(t);
  return out;
}

// ── 검사 ──
function snsCheck_(item, deep) {
  var p = [], plats = item.platforms || [], ms = [];
  if (!item.account && !item.accounts) p.push('account 없음');
  try { snsWhen_(item.when); } catch (e) { p.push(String(e.message)); }
  if (!plats.length) p.push('platforms 없음');
  plats.forEach(function (x) { if (x !== 'instagram' && x !== 'threads') p.push('이 스크립트는 인스타 · 스레드만: ' + x); });
  try { ms = snsMedia_(item); } catch (e) { p.push('사진 · 영상 파일을 못 엶: ' + e.message); }
  if (plats.indexOf('instagram') >= 0) {
    if (!ms.length) p.push('인스타는 사진이나 영상이 있어야 함');
    if (ms.length > 10) p.push('인스타 캐러셀은 10장까지');
    if (snsTags_(item.caption) > 5) p.push('인스타 해시태그 5개 넘음');
    if (String(item.caption || '').length > 2200) p.push('인스타 캡션 2200자 넘음');
    ms.forEach(function (m) { if (m.kind === 'video' && m.size > 50 * 1024 * 1024) p.push('영상 50MB 넘음: ' + m.name); });
  }
  if (plats.indexOf('threads') >= 0) {
    if (!ms.length && !String(item.threads_text || item.caption || '').trim()) p.push('스레드 글이 비어 있음');
    if (ms.length > 20) p.push('스레드 캐러셀은 20장까지');
  }
  if (deep) plats.forEach(function (x) {
    if (x !== 'instagram' && x !== 'threads') return;
    var a = snsAcct_(item, x);
    try { snsUid_(x, a); } catch (e) { p.push(x + ' ' + a + ': ' + e.message); }
  });
  return p;
}

// ── 인스타 한 단계 ──
function snsIg_(item, s) {
  var acct = snsAcct_(item, 'instagram'), tok = snsTok_('instagram', acct), uid = snsUid_('instagram', acct);
  var base = SNS.ig + '/' + uid, ms = item.state._media || (item.state._media = snsMedia_(item)), cap = item.caption || '';
  if (!s.container) {
    if (ms.length === 1 && ms[0].kind === 'video') {
      if (ms[0].fileId) {   // 드라이브 영상은 직접 밀어 올림(공개 주소 문제 없음)
        var r = snsFetch_('post', base + '/media', {media_type: 'REELS', upload_type: 'resumable', caption: cap, share_to_feed: 'true', access_token: tok});
        var bytes = DriveApp.getFileById(ms[0].fileId).getBlob().getBytes();
        snsFetch_('post', r.uri, null, {headers: {Authorization: 'OAuth ' + tok, offset: '0', file_size: String(bytes.length)},
                                        payload: bytes, contentType: 'application/octet-stream'});
        s.container = r.id;
      } else {
        s.container = snsFetch_('post', base + '/media', {media_type: 'REELS', video_url: ms[0].url, caption: cap, share_to_feed: 'true', access_token: tok}).id;
      }
    } else if (ms.length === 1) {
      s.container = snsFetch_('post', base + '/media', {image_url: snsPublic_(ms[0]), caption: cap, access_token: tok}).id;
    } else {
      var kids = s.kids || (s.kids = []);
      for (var i = kids.length; i < ms.length; i++) {
        var q = {is_carousel_item: 'true', access_token: tok};
        if (ms[i].kind === 'video') { q.media_type = 'VIDEO'; q.video_url = snsPublic_(ms[i]); } else { q.image_url = snsPublic_(ms[i]); }
        kids.push(snsFetch_('post', base + '/media', q).id);
      }
      s.container = snsFetch_('post', base + '/media', {media_type: 'CAROUSEL', children: kids.join(','), caption: cap, access_token: tok}).id;
    }
    s.created = Date.now();
    Utilities.sleep(ms.length === 1 && ms[0].kind === 'video' ? 1000 : 15000);
  }
  if (!s.mediaId) {
    var st = snsFetch_('get', SNS.ig + '/' + s.container, {fields: 'status_code', access_token: tok}).status_code;
    if (st === 'ERROR' || st === 'EXPIRED') throw new Error('인스타 처리 실패: ' + st);
    if (st !== 'FINISHED' && st !== 'PUBLISHED') {
      if (Date.now() - s.created > SNS.waitMin * 60000) throw new Error('인스타 처리 시간 초과');
      return 'wait';
    }
    s.mediaId = snsFetch_('post', base + '/media_publish', {creation_id: s.container, access_token: tok}).id;
    try { s.link = snsFetch_('get', SNS.ig + '/' + s.mediaId, {fields: 'permalink', access_token: tok}).permalink; } catch (e) {}
  }
  if (item.first_comment && !s.commented) {
    snsFetch_('post', SNS.ig + '/' + s.mediaId + '/comments', {message: item.first_comment, access_token: tok});
    s.commented = true;
  }
  s.done = snsKst_();
  return 'done';
}

// ── 스레드 한 단계 ──
function snsTh_(item, s) {
  var acct = snsAcct_(item, 'threads'), tok = snsTok_('threads', acct), uid = snsUid_('threads', acct);
  var base = SNS.th + '/' + uid, ms = item.state._media || (item.state._media = snsMedia_(item));
  var parts = s.parts || (s.parts = snsSplit_(item.threads_text || item.caption || '', 500));
  if (!s.container) {
    var p = {text: parts[0] || '', access_token: tok};
    if (item.topic_tag) p.topic_tag = item.topic_tag;
    if (!ms.length) p.media_type = 'TEXT';
    else if (ms.length === 1) {
      if (ms[0].kind === 'video') { p.media_type = 'VIDEO'; p.video_url = snsPublic_(ms[0]); }
      else { p.media_type = 'IMAGE'; p.image_url = snsPublic_(ms[0]); }
    } else {
      var kids = s.kids || (s.kids = []);
      for (var i = kids.length; i < ms.length; i++) {
        var q = {is_carousel_item: 'true', access_token: tok};
        if (ms[i].kind === 'video') { q.media_type = 'VIDEO'; q.video_url = snsPublic_(ms[i]); }
        else { q.media_type = 'IMAGE'; q.image_url = snsPublic_(ms[i]); }
        kids.push(snsFetch_('post', base + '/threads', q).id);
      }
      p.media_type = 'CAROUSEL'; p.children = kids.join(',');
    }
    s.container = snsFetch_('post', base + '/threads', p).id;
    s.created = Date.now();
    Utilities.sleep(ms.some(function (m) { return m.kind === 'video'; }) ? 1000 : 20000);
  }
  if (!s.mediaId) {
    var st = snsFetch_('get', SNS.th + '/' + s.container, {fields: 'status,error_message', access_token: tok});
    if (st.status === 'ERROR' || st.status === 'EXPIRED') throw new Error('스레드 처리 실패: ' + st.status + ' ' + (st.error_message || ''));
    if (st.status !== 'FINISHED' && st.status !== 'PUBLISHED') {
      if (Date.now() - s.created > SNS.waitMin * 60000) throw new Error('스레드 처리 시간 초과');
      return 'wait';
    }
    s.mediaId = snsFetch_('post', base + '/threads_publish', {creation_id: s.container, access_token: tok}).id;
    try { s.link = snsFetch_('get', SNS.th + '/' + s.mediaId, {fields: 'permalink', access_token: tok}).permalink; } catch (e) {}
  }
  // 이어지는 조각 → 답글 줄줄이, 마지막에 threads_reply(링크 등)
  var replies = s.replies || (s.replies = parts.slice(1).concat(item.threads_reply ? [item.threads_reply] : []));
  s.ri = s.ri || 0; s.parent = s.parent || s.mediaId;
  while (s.ri < replies.length) {
    if (!s.rc) s.rc = snsFetch_('post', base + '/threads', {media_type: 'TEXT', text: replies[s.ri], reply_to_id: s.parent, access_token: tok}).id;
    Utilities.sleep(5000);
    var rid = snsFetch_('post', base + '/threads_publish', {creation_id: s.rc, access_token: tok}).id;
    s.parent = rid; s.rc = null; s.ri++;
  }
  s.done = snsKst_();
  return 'done';
}

// ── 글 하나 진행 ──
function snsStep_(f, end) {
  var item = JSON.parse(f.getBlob().getDataAsString()), st = item.state || (item.state = {}), wait = false;
  (item.platforms || []).forEach(function (p) {
    var s = st[p] || (st[p] = {});
    if (s.done || s.err || p.charAt(0) === '_') return;
    if (Date.now() > end) { wait = true; return; }
    try {
      var r = p === 'instagram' ? snsIg_(item, s) : p === 'threads' ? snsTh_(item, s) : (s.err = '모르는 채널');
      if (r === 'wait') wait = true;
    } catch (e) {
      s.tries = (s.tries || 0) + 1; s.last = String(e.message || e).slice(0, 300);
      if (s.tries >= SNS.maxTry || /토큰 없음|있어야|실패|초과/.test(s.last)) s.err = s.last; else wait = true;
    }
  });
  var res = {id: item.id || f.getName(), when: item.when, result: {}};
  (item.platforms || []).forEach(function (p) { var s = st[p] || {}; res.result[p] = s.done ? (s.link || '올림') : s.err ? '실패: ' + s.err : '진행 중'; });
  if (wait) { f.setContent(JSON.stringify(item, null, 1)); return res; }
  var bad = (item.platforms || []).some(function (p) { return (st[p] || {}).err; });
  item.finished = snsKst_();
  snsMove_(f, item, bad ? '실패' : '완료');
  return res;
}
function snsMove_(f, item, dir) { f.setContent(JSON.stringify(item, null, 1)); f.moveTo(snsDir_(dir)); }
function snsFiles_(d) {
  var out = [], it = d.getFiles();
  while (it.hasNext()) { var f = it.next(); if (/\.json$/i.test(f.getName())) out.push(f); }
  return out.sort(function (a, b) { return a.getName() < b.getName() ? -1 : 1; });
}

// ── 10분마다 ──
function snsTick() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return;
  try {
    var end = Date.now() + 4.5 * 60000, now = Date.now(), dry = snsDry_(), log = [], dryLog = {};
    snsFiles_(snsDir_('진행')).forEach(function (f) { if (Date.now() < end) log.push(snsStep_(f, end)); });
    snsFiles_(snsDir_('대기')).forEach(function (f) {
      if (Date.now() > end) return;
      var item;
      try { item = JSON.parse(f.getBlob().getDataAsString()); } catch (e) { snsMove_(f, {error: 'json 깨짐', raw: f.getBlob().getDataAsString().slice(0, 500)}, '실패'); return; }
      var t;
      try { t = snsWhen_(item.when).getTime(); } catch (e) { item.error = String(e.message); snsMove_(f, item, '실패'); log.push({id: item.id, error: item.error}); return; }
      if (t > now) return;
      var probs = snsCheck_(item, true);
      if (dry) { dryLog[f.getName()] = probs.length ? probs : ['문제 없음 · DRY_RUN이라 안 올림']; return; }
      if (now - t > (item.late_ok_min || SNS.lateMin) * 60000) probs.push('예약 시각이 너무 지남');
      if (probs.length) { item.error = probs.join(' / '); snsMove_(f, item, '실패'); log.push({id: item.id, error: item.error}); return; }
      f.moveTo(snsDir_('진행'));
      log.push(snsStep_(f, end));
    });
    snsStatus_({tick: snsKst_(), dry_run: dry, log: log, dry: dryLog});
  } finally { lock.releaseLock(); }
}

// ── 매일 새벽: 토큰 60일 연장 · 계정 확인 · 공개 사진 정리 ──
function snsDaily() {
  var props = PropertiesService.getScriptProperties().getProperties(), acc = {};
  Object.keys(props).filter(function (k) { return /^TOK_(IG|TH)_/.test(k); }).forEach(function (k) {
    var ig = k.indexOf('TOK_IG_') === 0, acct = k.slice(7), plat = ig ? 'instagram' : 'threads', tok = props[k], r = null, note = '';
    var row = (acc[acct] = acc[acct] || {})[plat] = {};
    try {
      r = ig ? snsFetch_('get', SNS.ig + '/refresh_access_token', {grant_type: 'ig_refresh_token', access_token: tok})
             : snsFetch_('get', SNS.thRoot + '/refresh_access_token', {grant_type: 'th_refresh_token', access_token: tok});
    } catch (e) {
      note = String(e.message).slice(0, 150);
      var sec = props[ig ? 'IG_APP_SECRET' : 'TH_APP_SECRET'];
      if (sec) try {
        r = ig ? snsFetch_('get', SNS.ig + '/access_token', {grant_type: 'ig_exchange_token', client_secret: sec, access_token: tok})
               : snsFetch_('get', SNS.thRoot + '/access_token', {grant_type: 'th_exchange_token', client_secret: sec, access_token: tok});
        note = '60일 토큰으로 바꿈';
      } catch (e2) { note += ' / 바꾸기 실패 ' + String(e2.message).slice(0, 100); }
    }
    if (r && r.access_token) {
      snsSetP_(k, r.access_token);
      row.expires = snsKst_(new Date(Date.now() + (r.expires_in || 5184000) * 1000));
    }
    try {
      var me = ig ? snsFetch_('get', SNS.ig + '/me', {fields: 'user_id,username', access_token: snsP_(k, tok)})
                  : snsFetch_('get', SNS.th + '/me', {fields: 'id,username', access_token: snsP_(k, tok)});
      row.ok = true; row.username = me.username;
      snsSetP_('UID_' + (ig ? 'IG' : 'TH') + '_' + acct, ig ? (me.user_id || me.id) : me.id);
    } catch (e3) { row.ok = false; row.error = String(e3.message).slice(0, 200); }
    if (note) row.note = note;
  });
  var old = Date.now() - 7 * 86400000, it = snsDir_('_공개').getFiles();
  while (it.hasNext()) { var f = it.next(); if (f.getDateCreated().getTime() < old) f.setTrashed(true); }
  snsStatus_({daily: snsKst_(), accounts: acc});
  return acc;
}

// ── 상태 파일 「블로그/SNS예약/상태.json」 ──
function snsStatusRead_() {
  var it = snsDir_().getFilesByName('상태.json');
  return it.hasNext() ? JSON.parse(it.next().getBlob().getDataAsString()) : {};
}
function snsStatus_(patch) {
  var d = snsDir_(), it = d.getFilesByName('상태.json'), f = it.hasNext() ? it.next() : null;
  var s = f ? JSON.parse(f.getBlob().getDataAsString()) : {};
  if (patch.accounts) s.accounts = patch.accounts;
  if (patch.daily) s.daily = patch.daily;
  if (patch.tick) { s.tick = patch.tick; s.dry_run = patch.dry_run; s.dry = patch.dry; }
  if (patch.log && patch.log.length) s.last = patch.log.concat(s.last || []).slice(0, 40);
  s.count = {};
  ['대기', '진행', '완료', '실패'].forEach(function (n) { s.count[n] = snsFiles_(snsDir_(n)).length; });
  var txt = JSON.stringify(s, null, 1);
  if (f) f.setContent(txt); else d.createFile('상태.json', txt, 'text/plain');
}

// ── 처음 한 번 ▶실행 ──
function snsSetup() {
  ['대기', '진행', '완료', '실패', '_공개', '미디어'].forEach(function (n) { snsDir_(n); });
  if (snsP_('DRY_RUN', '') === '') snsSetP_('DRY_RUN', '1');
  ScriptApp.getProjectTriggers().forEach(function (t) {
    var h = t.getHandlerFunction(); if (h === 'snsTick' || h === 'snsDaily') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('snsTick').timeBased().everyMinutes(10).create();
  ScriptApp.newTrigger('snsDaily').timeBased().everyDays(1).atHour(4).inTimezone('Asia/Seoul').create();
  var acc = snsDaily();
  Logger.log(JSON.stringify({dry_run: snsDry_(), accounts: acc}));
}

// ── 우체통 웹 앱으로 부르기(gas.py → action) · Code.gs 보다 아래 칸에 있어야 함 ──
if (typeof ACT === 'object') {
  ACT.sns_status = function () { return snsStatusRead_(); };
  ACT.sns_daily = function () { return snsDaily(); };
  ACT.sns_tick = function () { snsTick(); return snsStatusRead_(); };
  ACT.sns_dry = function (q) { snsSetP_('DRY_RUN', q.on ? '1' : '0'); return {dry_run: snsDry_()}; };   // 시험 뒤 Claude가 실제 게시로 바꿈
  ACT.sns_check = function (q) {   // 대기 폴더의 json 하나를 지금 검사: name
    var f = first_(snsDir_('대기').getFilesByName(q.name), q.name);
    return {problems: snsCheck_(JSON.parse(f.getBlob().getDataAsString()), true)};
  };
  ACT.sns_find = function (q) {    // 이름으로 드라이브 파일 찾기: name → [{id, name, size, folder}]
    var out = [], it = DriveApp.getFilesByName(q.name);
    while (it.hasNext() && out.length < 10) {
      var f = it.next(), ps = f.getParents();
      out.push({id: f.getId(), name: f.getName(), size: f.getSize(), folder: ps.hasNext() ? ps.next().getName() : ''});
    }
    return out;
  };
}

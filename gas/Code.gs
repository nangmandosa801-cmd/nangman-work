// 낭만 블로그 우체통 — Claude가 PC 없이 구글 블로그에 글을 올리고 그림을 올리는 통로
// 이 계정(nangmandosa801)이 글쓴이로 들어가 있는 블로그에만 씁니다.
var KEY = 'N6GT8sL5X-Ce5dQR9WHos3-7x4UbOsCJ';
var API = 'https://www.googleapis.com/blogger/v3';

function doPost(e) {
  var q;
  try { q = JSON.parse(e.postData.contents); } catch (err) { return out_({ok:false, error:'json'}); }
  if (!q || q.key !== KEY) return out_({ok:false, error:'key'});
  var f = ACT[q.action];
  if (!f) return out_({ok:false, error:'action'});
  try { return out_({ok:true, result:f(q)}); }
  catch (err) { return out_({ok:false, error:String(err)}); }
}

function doGet(e) {
  if (!e || !e.parameter || e.parameter.key !== KEY) return out_({ok:false, error:'key'});
  return out_({ok:true, result:ACT.blogs()});
}

function out_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

function call_(method, path, body) {
  var opt = {method:method, muteHttpExceptions:true, contentType:'application/json',
             headers:{Authorization:'Bearer ' + ScriptApp.getOAuthToken()}};
  if (body) opt.payload = JSON.stringify(body);
  var r = UrlFetchApp.fetch(API + path, opt);
  var c = r.getResponseCode(), t = r.getContentText();
  if (c >= 300) throw new Error(c + ' ' + t.slice(0, 400));
  return t ? JSON.parse(t) : {};
}

function slim_(p) { return {id:p.id, url:p.url, title:p.title, status:p.status, published:p.published}; }

var ACT = {
  // ChatGPT 검수(11/4): 스크립트 속성 OPENAI_KEY 필요 · system, user, model(선택)
  gpt: function (q) {
    var k = PropertiesService.getScriptProperties().getProperty('OPENAI_KEY');
    if (!k) throw new Error('OPENAI_KEY 없음 — 프로젝트 설정 → 스크립트 속성에 넣기');
    var r = UrlFetchApp.fetch('https://api.openai.com/v1/chat/completions', {method:'post', muteHttpExceptions:true,
      contentType:'application/json', headers:{Authorization:'Bearer ' + k},
      payload: JSON.stringify({model: q.model || 'gpt-4o-mini', temperature: 0.2, response_format: {type:'json_object'},
        messages: [{role:'system', content:q.system}, {role:'user', content:q.user}]})});
    var c = r.getResponseCode(), t = r.getContentText();
    if (c >= 300) throw new Error(c + ' ' + t.slice(0, 300));
    return JSON.parse(t).choices[0].message.content;
  },
  // 이 계정이 쓸 수 있는 블로그 목록
  blogs: function () {
    var r = call_('get', '/users/self/blogs');
    return (r.items || []).map(function (b) { return {id:b.id, name:b.name, url:b.url}; });
  },
  // 새 글: blogId, title, html, labels[], draft(bool), publishAt(ISO, 미래면 예약)
  post: function (q) {
    var p = call_('post', '/blogs/' + q.blogId + '/posts?isDraft=true',
                  {kind:'blogger#post', title:q.title, content:q.html, labels:q.labels || []});
    if (!q.draft) {
      var path = '/blogs/' + q.blogId + '/posts/' + p.id + '/publish';
      if (q.publishAt) path += '?publishDate=' + encodeURIComponent(q.publishAt);
      p = call_('post', path);
    }
    return slim_(p);
  },
  // 글 읽기: blogId + postId 또는 path(/2026/11/xxx.html)
  get: function (q) {
    var p = q.postId ? call_('get', '/blogs/' + q.blogId + '/posts/' + q.postId)
                     : call_('get', '/blogs/' + q.blogId + '/posts/bypath?path=' + encodeURIComponent(q.path));
    var s = slim_(p); s.html = p.content; s.labels = p.labels || []; return s;
  },
  // 찾기: blogId, q
  search: function (q) {
    var r = call_('get', '/blogs/' + q.blogId + '/posts/search?fetchBodies=false&q=' + encodeURIComponent(q.q));
    return (r.items || []).map(slim_);
  },
  // 최근 글: blogId, n
  list: function (q) {
    var r = call_('get', '/blogs/' + q.blogId + '/posts?fetchBodies=false&maxResults=' + (q.n || 20));
    return (r.items || []).map(slim_);
  },
  // 고치기: blogId, postId, (title, html, labels 중 바꿀 것만)
  patch: function (q) {
    var b = {};
    if (q.title != null) b.title = q.title;
    if (q.html != null) b.content = q.html;
    if (q.labels != null) b.labels = q.labels;
    return slim_(call_('patch', '/blogs/' + q.blogId + '/posts/' + q.postId, b));
  },
  // 본문 끝에 한 줄 더하기(입주 노트용): blogId, postId, html
  append: function (q) {
    var p = call_('get', '/blogs/' + q.blogId + '/posts/' + q.postId);
    if (q.unless && p.content.indexOf(q.unless) >= 0) return {skipped:true, url:p.url};
    return slim_(call_('patch', '/blogs/' + q.blogId + '/posts/' + q.postId, {content: p.content + q.html}));
  },
  // 그림 올리기: name, b64(png/jpg) → 드라이브 「낭만 그림」 폴더, 링크 공개, 주소 돌려줌
  image: function (q) {
    var it = DriveApp.getFoldersByName('낭만 그림');
    var folder = it.hasNext() ? it.next() : DriveApp.createFolder('낭만 그림');
    var mime = /\.jpe?g$/i.test(q.name) ? 'image/jpeg' : 'image/png';
    var f = folder.createFile(Utilities.newBlob(Utilities.base64Decode(q.b64), mime, q.name));
    f.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    return {id:f.getId(), url:'https://lh3.googleusercontent.com/d/' + f.getId()};
  },  // ── PC 폴더(C:\블로그)를 구글 드라이브로 동기화해 둔 뒤 쓰는 파일 기능 ──
  // path 예: "블로그/텍스트/낭만부동산" (첫 칸은 드라이브 어디에 있든 이름으로 찾음)
  ls: function (q) {
    var d = folder_(q.path), out = [];
    var fs = d.getFolders(); while (fs.hasNext()) { var x = fs.next(); out.push({dir:true, name:x.getName(), id:x.getId()}); }
    var it = d.getFiles(); while (it.hasNext()) { var f = it.next(); out.push({name:f.getName(), id:f.getId(), size:f.getSize(), updated:f.getLastUpdated()}); }
    return out;
  },
  // 파일 받기: id 또는 path+name → b64 (50MB 아래)
  fget: function (q) {
    var f = q.id ? DriveApp.getFileById(q.id) : first_(folder_(q.path).getFilesByName(q.name), q.name);
    return {name:f.getName(), id:f.getId(), b64:Utilities.base64Encode(f.getBlob().getBytes())};
  },
  // 파일 넣기: path, name, b64 또는 text → 같은 이름이 있으면 내용 교체
  fput: function (q) {
    var d = folder_(q.path, true);
    var blob = q.b64 != null ? Utilities.newBlob(Utilities.base64Decode(q.b64), q.mime || 'application/octet-stream', q.name)
                             : Utilities.newBlob(q.text, 'text/plain', q.name);
    var it = d.getFilesByName(q.name);
    if (it.hasNext()) return {id:repl_(it.next(), blob).getId(), replaced:true};
    return {id:d.createFile(blob).getId(), replaced:false};
  },
  // 공개 내려받기 주소(영상을 Upload-Post에 넘길 때): id
  collab: function (q) { return setupCollab(); },
  review: function (q) { return reviewInbox(); },
  flink: function (q) {
    var f = DriveApp.getFileById(q.id);
    f.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    return {url:'https://drive.google.com/uc?export=download&id=' + f.getId()};
  }
};

function first_(it, what) { if (!it.hasNext()) throw new Error('없음: ' + what); return it.next(); }

function folder_(path, make) {
  var parts = String(path || '').split('/').filter(String);
  if (!parts.length) return DriveApp.getRootFolder();
  var tops = DriveApp.getFoldersByName(parts[0]), best = null;
  while (tops.hasNext()) { var t = tops.next(); if (!best || t.getLastUpdated() > best.getLastUpdated()) best = t; }
  if (!best) { if (!make) throw new Error('폴더 없음: ' + parts[0]); best = DriveApp.createFolder(parts[0]); }
  var d = best;
  for (var i = 1; i < parts.length; i++) {
    var it = d.getFoldersByName(parts[i]);
    if (it.hasNext()) d = it.next();
    else if (make) d = d.createFolder(parts[i]);
    else throw new Error('폴더 없음: ' + parts.slice(0, i + 1).join('/'));
  }
  return d;
}

// 내용 교체: 고급 서비스 없이 — 옛 파일을 휴지통으로 보내고 같은 자리에 새로 만듦(30일 안에 되살릴 수 있음)
function repl_(f, blob) {
  var parents = f.getParents(); var d = parents.hasNext() ? parents.next() : DriveApp.getRootFolder();
  f.setTrashed(true); return d.createFile(blob);
}


// ── 협업 폴더(11/4 23시 · 사용자 「드라이브에서 파일 · 지시 주고받게, 내가 일일이 주고받지 않게」) ──
// 블로그/협업/0_지시 · 1_검수대기 · 2_검수결과 · 3_검수끝 · 4_어사이드 · 5_보고
var COLLAB = '블로그/협업';
var COLLAB_DIRS = ['0_지시', '1_검수대기', '2_검수결과', '3_검수끝', '4_어사이드', '5_보고'];
function setupCollab() {
  COLLAB_DIRS.forEach(function (d) { folder_(COLLAB + '/' + d, true); });
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() == 'reviewInbox') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('reviewInbox').timeBased().everyMinutes(10).create();
  return 'ok';
}
function readText_(dir, name) {
  var it = folder_(COLLAB + '/' + dir).getFilesByName(name);
  return it.hasNext() ? it.next().getBlob().getDataAsString('UTF-8') : '';
}
// 10분마다: 1_검수대기의 원고 → ChatGPT 검수(점검표는 0_지시/검수_점검표.txt) → 2_검수결과/<이름>.gpt.json · 원고는 3_검수끝으로
function reviewInbox() {
  var sys = readText_('0_지시', '검수_점검표.txt'); if (!sys) return 'no checklist';
  var src = folder_(COLLAB + '/1_검수대기'), out = folder_(COLLAB + '/2_검수결과'), done = folder_(COLLAB + '/3_검수끝');
  var it = src.getFiles(), n = 0, t0 = Date.now();
  while (it.hasNext() && Date.now() - t0 < 300000) {
    var f = it.next(), name = f.getName().replace(/\.(md|txt)$/, '');
    var res;
    try { res = ACT.gpt({system: sys, user: '원고:\n' + f.getBlob().getDataAsString('UTF-8').slice(0, 12000)}); }
    catch (e) { res = JSON.stringify({verdict: '오류', error: String(e)}); }
    var old = out.getFilesByName(name + '.gpt.json'); while (old.hasNext()) old.next().setTrashed(true);
    out.createFile(name + '.gpt.json', res, 'application/json');
    f.moveTo(done); n++;
  }
  return n;
}

// 처음 한 번 ▶실행: 권한 허용 창을 띄우고, 쓸 수 있는 블로그 목록을 로그에 찍습니다.
function test() {
  Logger.log(JSON.stringify(ACT.blogs()));
  DriveApp.getRootFolder();
  setupCollab();   // 협업 폴더 만들고 10분마다 검수 돌리기
}

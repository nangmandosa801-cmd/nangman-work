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
  }
};

// 처음 한 번 ▶실행: 권한 허용 창을 띄우고, 쓸 수 있는 블로그 목록을 로그에 찍습니다.
function test() {
  Logger.log(JSON.stringify(ACT.blogs()));
  DriveApp.getRootFolder();
}

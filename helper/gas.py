#!/usr/bin/env python3
"""낭만 블로그 우체통(Apps Script) 클라이언트 — PC 없이 구글 블로그 쓰기.
설정: /home/claude/gas/conf.json {"url": "<웹 앱 주소>", "key": "<키>"}
블로그 ID: budongsan 7361591188244782195 · changgo 3521924271702627135 · ipju(목록에서 확인)
사용 예:
  python3 gas.py blogs
  python3 gas.py post <blogId> "제목" body.html "라벨1,라벨2" [draft]
  python3 gas.py image <파일.png>            → 주소 출력
  python3 gas.py append <blogId> <postId> line.html
  python3 gas.py get <blogId> /2026/11/xxx.html
파이썬에서: from gas import call; call('post', blogId=..., title=..., html=..., labels=[...])
"""
import json, sys, os, base64, urllib.request
CONF = os.environ.get('GAS_CONF', '/home/claude/gas/conf.json')
BLOG = {'budongsan': '7361591188244782195', 'changgo': '3521924271702627135'}

def call(action, **kw):
    c = json.load(open(CONF))
    data = json.dumps(dict(kw, key=c['key'], action=action)).encode()
    req = urllib.request.Request(c['url'], data=data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:   # 302 → GET 은 urllib가 따라감
        res = json.loads(r.read().decode())
    if not res.get('ok'):
        raise RuntimeError(res.get('error'))
    return res['result']

def image(path):
    return call('image', name=os.path.basename(path), b64=base64.b64encode(open(path, 'rb').read()).decode())

if __name__ == '__main__':
    a = sys.argv[1:]
    bid = lambda x: BLOG.get(x, x)
    if a[0] == 'blogs': r = call('blogs')
    elif a[0] == 'post':
        r = call('post', blogId=bid(a[1]), title=a[2], html=open(a[3]).read(),
                 labels=[s for s in a[4].split(',') if s] if len(a) > 4 else [], draft=len(a) > 5)
    elif a[0] == 'image': r = image(a[1])
    elif a[0] == 'append': r = call('append', blogId=bid(a[1]), postId=a[2], html=open(a[3]).read())
    elif a[0] == 'get': r = call('get', blogId=bid(a[1]), path=a[2]) if a[2].startswith('/') else call('get', blogId=bid(a[1]), postId=a[2])
    elif a[0] == 'list': r = call('list', blogId=bid(a[1]), n=int(a[2]) if len(a) > 2 else 20)
    else: sys.exit('모르는 명령')
    print(json.dumps(r, ensure_ascii=False, indent=1))

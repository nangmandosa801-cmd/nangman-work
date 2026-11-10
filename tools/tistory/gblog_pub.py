#!/usr/bin/env python3
"""구글 블로그 「낭만 부동산」(budongsan) 실거래가 페이지 올리기 · 매달 고치기 (11/10)
사용: python3 gblog_pub.py <지역키> ["2026-11-11T09:00:00+09:00"]
  먼저 python3 pricepage.py <지역키> --gblog 로 /home/claude/w/ts_pages/<slug>/gblog.html 을 만든다.
  gblog_pages.json 에 그 지역 글이 없으면 새 글(시각을 주면 예약 · 없으면 바로 공개),
  있으면 같은 글(postId)을 patch 로 제목 · 본문만 바꾼다(주소 그대로).
기록: /home/claude/tools/tistory/gblog_pages.json  {지역키: {postId, url, title, status, published, updated}}
"""
import sys, os, json, datetime
sys.path.insert(0, '/home/claude/helper'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gas import call, BLOG
import pricepage as P
BOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gblog_pages.json')
LABELS = ['하남', '아파트 실거래가', '시세']

def main(key, when=None):
    d = os.path.join(P.OUT, P.REG[key]['slug']); meta = json.load(open(os.path.join(d, 'meta.json')))
    html = open(os.path.join(d, 'gblog.html')).read()
    book = json.load(open(BOOK)) if os.path.exists(BOOK) else {}
    bid = BLOG['budongsan']
    if key in book:
        r = call('patch', blogId=bid, postId=book[key]['postId'], title=meta['title'], html=html); mode = 'patch'
    else:
        kw = dict(blogId=bid, title=meta['title'], html=html, labels=LABELS)
        if when: kw['publishAt'] = when
        r = call('post', **kw); mode = 'post'
    book[key] = dict(book.get(key, {}), postId=r['id'], url=r.get('url'), title=r.get('title'), status=r.get('status'),
                     published=r.get('published'), updated=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                     insights=[z['title'] for z in (meta.get('gblog') or {}).get('insights', [])])
    json.dump(book, open(BOOK, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(dict(mode=mode, key=key, **{k: book[key][k] for k in ['postId', 'url', 'title', 'status', 'published']}), ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

#!/usr/bin/env python3
"""낭만 부동산 세로 클립(네이버 클립 · 블로그 본문 영상 · 유튜브 쇼츠 · 인스타 릴스 공용) 한 번에.
  python3 bd_clip.py <spec.json> [--up]
spec.json:
 {"logNo":"2244…","slug":"uidong",
  "scenes":[["hook",{"lines":["…","…"],"bub":["…","…"]}],
            ["big",{"lines":[…],"num":"11억 4천","sub1":"…","sub2":"…","c":"WARN"}],
            ["bars",{"lines":[…],"items":[["단지",18.7,"WARN","18억 7천"],…],"note":"…"}],   # 막대 5개 이하 · 핵심만 WARN
            ["vs",{"lines":[…],"L":["왼쪽","18~29%",""],"R":["오른쪽","1~7%",""],"bottom":["…"]}],
            ["end",{"lines":["검색어"],"sub":["써먹을 한 가지","…"],"sub2":"단지별 표는 블로그에"}]],
  "durs":[3.0,3.8,4.4,3.8,3.0],
  "cap":"네이버 클립 캡션 한 줄(검색어 + 숫자)", "tags5":["#…",…,"#낭만부동산"],
  "yt":"유튜브 제목", "desc":"유튜브 설명 2~3줄(네이버 원문에 있는 사실만)"}
규칙: 만화 캐릭터 없음 · 장면마다 숫자 하나 · 인테리어 문구 · 링크 없음 · 전화번호 글자 없음 · 3D 그래프 없음.
발행 전 원고와 함께 만들 때는 "logNo":"pre_<slug>" (장부 기록은 발행 뒤 scan 이 이어 줌 · 클립 칸은 손으로 set).
--up: 드라이브 「블로그/shorts/부동산」 + 「블로그/협업/4_어사이드/원고/nangman_clip_<logNo>/」(clip.mp4 · cover.jpg · caption.txt) → 장부 clip 칸 기록.
"""
import json, os, sys, subprocess
sys.path.insert(0, '/home/claude'); sys.path.insert(0, '/home/claude/helper')
import clipgen2  # noqa: bars note 등 장면 확장
from clipgen import make, NAVY, WARN, MID
from PIL import Image
C = {'NAVY': NAVY, 'WARN': WARN, 'MID': MID}
D = os.path.dirname(os.path.abspath(__file__))

def col(kw):
    for k in ('c', 'bc'):
        if isinstance(kw.get(k), str): kw[k] = C[kw[k]]
    if 'items' in kw:
        kw['items'] = [tuple(C.get(x, x) if isinstance(x, str) and x in C else x for x in it) for it in kw['items']]
    for k in ('L', 'R'):
        if k in kw: kw[k] = tuple(kw[k])
    return kw

def main(path, up):
    sp = json.load(open(path)); n = sp['logNo']; slug = sp.get('slug', n)
    out = os.path.join(D, 'out', slug)
    scenes = [(t, col(dict(kw))) for t, kw in sp['scenes']]
    info = dict(name=sp['cap'][:20], title=sp.get('title', ''), url='https://blog.naver.com/dong_jin_kim/' + n,
                cap=sp['cap'], tags5=sp['tags5'], yt=sp['yt'], desc=sp['desc'], tags10=sp.get('tags10', sp['tags5']),
                scenes=[s[0] for s in sp['scenes']], src=sp.get('src', '국토교통부 실거래'))
    mp4, cover, txt = make('nm', slug, scenes, sp['durs'], sp.get('cover', 2), info, out)[:3]
    # 소리 트랙 없는 영상은 플랫폼에서 불리 → 아주 작은 무음 트랙을 붙임
    fin = os.path.join(out, 'clip.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp4, '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
                    '-shortest', '-c:v', 'copy', '-c:a', 'aac', fin], check=True)
    Image.open(cover).convert('RGB').save(os.path.join(out, 'cover.jpg'), quality=92)
    cap = f"{sp['cap']}\n\n{' '.join(sp['tags5'])}\n\n연결할 글: https://blog.naver.com/dong_jin_kim/{n}\n"
    open(os.path.join(out, 'caption.txt'), 'w').write(cap)
    res = {'logNo': n, 'mp4': fin, 'cover': os.path.join(out, 'cover.jpg')}
    if up:
        from gas import call
        import base64
        def put(folder, f):
            r = call('fput', path=folder, name=os.path.basename(f) if folder.startswith('블로그/협업') else f'nangman_{slug}_{os.path.basename(f)}',
                     b64=base64.b64encode(open(f, 'rb').read()).decode(),
                     mime={'.mp4': 'video/mp4', '.jpg': 'image/jpeg', '.txt': 'text/plain'}[os.path.splitext(f)[1]])
            return r.get('id') if isinstance(r, dict) else r
        vid = put('블로그/shorts/부동산', fin)
        put('블로그/shorts/부동산', os.path.join(out, 'cover.jpg'))
        af = f'블로그/협업/4_어사이드/원고/nangman_clip_{n}'
        for f in ('clip.mp4', 'cover.jpg', 'caption.txt'): put(af, os.path.join(out, f))
        res.update(drive_id=vid, aside=af)
        if n.isdigit(): subprocess.run([sys.executable, os.path.join(D, 'bd_sync.py'), 'set', n, 'clip', f'drive:{vid}'], check=True,
                       stdout=subprocess.DEVNULL)
    print(json.dumps(res, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv[1], '--up' in sys.argv)

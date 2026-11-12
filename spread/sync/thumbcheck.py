"""네이버 글 대표 사진 점검 (11/12 사용자 「썸네일 없어 · 왜 요새 그런 게 빠져」).
python3 thumbcheck.py dong_jin_kim [개수=10] → 대표(og:image)가 가로로 긴 그림(카드 · 표 · 배너)이면 bad 로 JSON 한 줄씩.
썸네일 카드는 정사각형(1000x1000 · 743x743)이라 가로/세로 1.3 넘으면 대표가 틀린 것."""
import sys,re,json,subprocess,urllib.parse,html,io
from PIL import Image
b=sys.argv[1]; k=int(sys.argv[2]) if len(sys.argv)>2 else 10
c=lambda u:subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0','-e',f'https://blog.naver.com/{b}',u],capture_output=True).stdout
d=json.loads(c(f'https://blog.naver.com/PostTitleListAsync.naver?blogId={b}&currentPage=1&countPerPage={k}').decode('utf-8','replace').replace("\\'","'"))
for p in d['postList']:
    n=p['logNo']; t=html.unescape(urllib.parse.unquote_plus(p['title']))
    s=c(f'https://blog.naver.com/PostView.naver?blogId={b}&logNo={n}').decode('utf-8','replace')
    m=re.search(r'og:image" content="([^"]+)',s); r={'logNo':n,'title':t[:40]}
    try:
        w,h=Image.open(io.BytesIO(c(m.group(1)))).size; r['size']=f'{w}x{h}'; r['ok']=w/h<=1.3
    except Exception: r['ok']=False; r['size']='없음'
    print(json.dumps(r,ensure_ascii=False))

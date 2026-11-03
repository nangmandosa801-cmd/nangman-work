import sys
p,n=sys.argv[1],sys.argv[2]; s=open(p).read()
a='이 글은 본문에 그림 자리가 없습니다. 대표 그림이 필요하면 폴더의 thumb.png를 쓰세요.'
assert a in s
s=s.replace(a,f'<b>그래프 · 안내 그림 {n}장은 본문에 들어 있습니다.</b> 「본문 복사」 → 네이버에 Ctrl+V 하면 같이 들어갑니다(이 미리 보기에서는 빈칸으로 보일 수 있습니다). 따로 붙일 것은 위 0번 썸네일 한 장뿐입니다. 「썸네일 복사」를 눌러 붙이세요.')
s=s.replace('<h2><span class="n">3</span>그림 — 점선 상자 자리에 이 순서로</h2>','<h2><span class="n">3</span>그림 확인</h2>')
s=s.replace('대표 사진(썸네일) — 맨 먼저 올리고 「대표」로 지정','대표 사진(썸네일) — 「썸네일 복사」로 붙이고 「대표」로 지정')
open(p,'w').write(s); print('ok')

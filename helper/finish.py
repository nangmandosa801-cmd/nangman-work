import sys
p,n=sys.argv[1],sys.argv[2]; s=open(p).read()
s=s.replace('이 글은 본문에 그림 자리가 없습니다. 대표 그림이 필요하면 폴더의 thumb.png를 쓰세요.',f'<b>그림이 본문에 들어 있습니다.</b> 「본문 복사」 → 네이버에 Ctrl+V 하면 그림 {n}장이 같이 들어갑니다(이 미리 보기에서는 빈칸으로 보입니다).<br>붙여 넣은 그림 주소가 <b>pstatic.net</b>이면 그대로 발행, <b>googleusercontent</b>로 남으면 그 그림을 지우고 아래 폴더에서 다시 올려 주세요.')
s=s.replace('<h2><span class="n">3</span>그림 — 점선 상자 자리에 이 순서로</h2>','<h2><span class="n">3</span>그림 확인</h2>')
s=s.replace('대표 사진(썸네일) — 맨 먼저 올리고 「대표」로 지정','대표 사진(썸네일) — 본문 맨 위 그림을 「대표」로 지정')
open(p,'w').write(s)

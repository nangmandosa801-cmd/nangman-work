# 10/16 사용자 「info는 한개씩 만들때 마다 이 화면에 올려줘」 — 클립 info 파일 + 채팅용 글
import sys,json,subprocess
D='/mnt/user-data/outputs/int/clip_sigong/'
def make(slug,name,cap,link,linktitle,what,scenes,src):
    assert len(cap)<=100 and cap.count('#')==5,(len(cap),cap.count('#'))
    for w in ['값','자리','어요','예요','고요','최고','프리미엄','기준','헷갈']: assert w not in cap,w
    dur=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'nangman_interior_{slug}_clip.mp4'],capture_output=True,text=True).stdout.strip()
    ln=f"{linktitle}\n{link}" if link else "글을 올린 뒤 그 주소를 넣어 주세요"
    t=f"""{name} · 시공 클립 · 1080×1920 · {float(dur):.0f}초
파일: nangman_interior_{slug}_clip.mp4

[ 네이버 클립 ]

캡션 ({len(cap)}자)
{cap}

대표 이미지
nangman_interior_{slug}_clip_cover.jpg

연결할 글
{ln}

고정 댓글
전화 · 문자 010-2882-8165 · {what} 사진 한 장 보내 주시면 무료로 봐 드립니다

[ 장면 ]
"""+"\n".join(f"{i}  {s}" for i,s in enumerate(scenes,1))+f"\n(모든 장면 아래에 문의 010-2882-8165)\n\n[ 자료 ]\n{src}\n"
    open(D+f'nangman_interior_{slug}_clip_info.txt','w').write(t)
    m=f"**{name} · 네이버 클립 info**\n\n캡션 ({len(cap)}자)\n```\n{cap}\n```\n\n연결할 글\n"+(f"```\n{link}\n```\n({linktitle})" if link else "아직 발행 전이에요. 글을 올린 뒤 주소를 붙여 주세요.")+f"\n\n고정 댓글\n```\n전화 · 문자 010-2882-8165 · {what} 사진 한 장 보내 주시면 무료로 봐 드립니다\n```"
    open(f'/tmp/claude-0/msg_{slug}.md','w').write(m); print(m)

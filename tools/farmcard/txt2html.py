"""팜 에디터 원고 txt → 네이버 붙여넣기용 html(꾸밈 표시 포함) + 사진설명.txt
python3 txt2html.py post.txt out.html"""
import re,sys,pathlib
src,dst=sys.argv[1],sys.argv[2]
L=pathlib.Path(src).read_text(encoding='utf-8').split('\n')
B='font-size:16px;color:#55594F;line-height:1.95'
E=f'<p style="{B}">&nbsp;</p>'
note=lambda s,c='':f'<p style="font-size:12px;color:#aaa;{c}">[꾸밈: {s}]</p>'
out=[];story=0;cap=[];box=None;title='';qopen=False
def flushbox():
    global box
    if box: out.append(f'<div style="background:#F1EDE0;border-radius:12px;padding:16px 20px;{B}"><b style="color:#5E7552">{box[0]}</b><br>'+'<br>'.join(box[1:])+'</div>'+note('인용구(상자형)')); out.append(E)
    box=None
for l in L:
    s=l.strip()
    if box is not None and not s.startswith('·'): flushbox()
    if qopen and not s: continue
    if not s: continue
    if s.startswith('[제목]'): title=s[4:].strip(); out.append(f'<p style="font-size:26px;font-weight:bold;color:#3F4A36">{title}</p>'+note('제목 칸에 넣기 · 본문에는 쓰지 않음')); continue
    if s.startswith('[카테고리]'): out.append(f'<p style="font-size:13px;color:#999">카테고리: {s[6:].strip()}</p>'); continue
    if s.startswith('[태그]'): out.append(f'<p style="font-size:13px;color:#999">태그 칸: {s[4:].strip()}</p>'); continue
    m=re.match(r'▼ (사진|영상) (\S+)(?: \(대표\))? \| (.*)',s)
    if m:
        f,d=m.group(2),m.group(3); cap.append(f'{f[:2]} {d}')
        out.append(f'<p style="text-align:center"><img src="{f}" style="width:100%;max-width:640px;border-radius:14px"></p>' if m.group(1)=='사진' else f'<p style="text-align:center;background:#eee;padding:40px;border-radius:14px">▶ 영상 {f}</p>')
        out.append(f'<p style="font-size:12px;color:#999;text-align:center">▼ {m.group(1)} {f}{" (대표 · 썸네일)" if "대표" in s else ""} · 사진 설명 칸: {d}</p>'); out.append(E); continue
    if s.startswith('[인용구]'): out.append(f'<p style="font-size:17px;color:#5E7552;line-height:1.85;border-left:3px solid #B08A4A;padding:6px 18px">{s[5:].strip()}</p>'+note('인용구(라인형) · 글자색 #5E7552')); out.append(E); continue
    if s.startswith('[소제목]'):
        t=s[5:].strip(); lab=''
        if t!='자주 묻는 질문': story+=1; lab=f'<span style="display:block;font-size:13px;color:#B08A4A;letter-spacing:2px;margin-bottom:4px">STORY {story:02d}</span>'
        out.append(E); out.append(f'<p style="font-size:21px;font-weight:bold;color:#5E7552;line-height:1.5">{lab}{t}</p>'+note('소제목 · 글자색 #5E7552 · 굵게 · STORY 표시는 작은 금색 글씨')); out.append(E); continue
    if s=='[구분선]': out.append(E); out.append('<p style="text-align:center;color:#B08A4A;letter-spacing:8px">· · ·</p>'+note('구분선 · 짧은 점선','text-align:center')); out.append(E); continue
    if s.startswith('[상자]'): box=[s[4:].strip()]; continue
    if s.startswith('·') and box is not None: box.append(s); continue
    if s.startswith('Q.'): out.append(f'<div style="background:#F1EDE0;border-radius:12px;padding:14px 18px;{B}"><b style="color:#5E7552">{s}</b>'); qopen=True; continue
    if qopen: out[-1]+=f'<br>{s}</div>'+note('인용구(상자형)'); out.append(E); qopen=False; continue
    if s.startswith('(가운데'): t=s.split(')',1)[1].strip().replace(' | ','<br>'); out.append(f'<p style="font-size:15px;color:#8A8270;text-align:center;line-height:1.8">{t}</p>'+note('가운데 · 작은 글씨 · 글 맺음','text-align:center')); out.append(E); continue
    if s.startswith('(작은 글씨)'): out.append(f'<p style="font-size:13px;color:#999">{s.split(")",1)[1].strip()}</p>'); continue
    out.append(f'<p style="{B}">{s}</p>'); out.append(E)
flushbox()
head=f'<meta charset="utf-8"><title>{title}</title><body style="max-width:720px;margin:auto;background:#FAF8F1;padding:20px;font-family:\'Nanum Gothic\',sans-serif">'
pathlib.Path(dst).write_text(head+'\n'.join(out)+'</body>',encoding='utf-8')
pathlib.Path(dst).with_name('사진설명.txt').write_text('\n'.join(cap)+'\n',encoding='utf-8')
print(len(out),'blocks',len(cap),'captions')

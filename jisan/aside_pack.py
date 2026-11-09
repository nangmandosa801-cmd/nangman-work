#!/usr/bin/env python3
# 지산드림 → 어사이드 묶음: python3 aside_pack.py <slug> <폴더> <짧은이름>  → 화면 html · txt(사진 01 줄) · 드라이브 「블로그/협업/4_어사이드/원고」 + img 폴더 올리기
import sys,re,os,subprocess,json
slug,folder,short=sys.argv[1:4]
D='/mnt/user-data/outputs/jisandream/%s/'%folder; post=D+'jisandream_%s_post.html'%slug
html=open(post).read(); t=re.search(r'font-size:34px[^>]*>([^<]*)<',html).group(1)
body=html.split('<p style="font-size:17px;color:#8A8578;">자료: </p>')[0]
note=('지산드림(jisandream01) · 카테고리 그대로 · 빨간 「▼ 사진 NN.jpg」 자리에 원고/jisandream_%s/NN.jpg 를 넣고 그 줄은 지웁니다 · 01.jpg = 대표 사진(본문 맨 위) · 맨 아래 태그 줄은 태그 칸에'%slug)
wrap=('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>지산드림 원고 · %s</title>\n'
 '<style>body{background:#fff;color:#222;font-family:"Noto Sans KR",sans-serif;margin:0;padding:16px} .wrap{max-width:760px;margin:0 auto} .note{background:#FFF7E0;border:1px solid #E6C766;padding:10px 14px;font-size:15px;margin-bottom:18px}</style></head>\n'
 '<body><div class="wrap"><div class="note">%s</div>\n<p style="font-size:18px;font-weight:700;color:#C0392B;">▼ 사진 01.jpg — 대표 사진 (본문 맨 위 · 대표로 지정)</p>\n%s\n'
 '<p style="font-size:14px;color:#9AA4AE;">지산드림공인중개사사무소 · 대표 김미호 · 등록번호 41310-2022-00061 · 경기도 구리시 갈매동 540-5, 101호</p>\n</div></body></html>')%(short,note,body)
tags=re.search(r'line-height:1.9;">([^<]*)<',html); tags=tags.group(1) if tags else ''
wrap=wrap.replace('</div></body></html>','<p><br></p><p style="font-size:16px;color:#555;">태그: %s</p></div></body></html>'%tags)
hf=D+'jisandream_%s.html'%slug; open(hf,'w').write(wrap)
exec(open('/home/claude/jisan/html2txt.py').read())
txt=conv(html,t,[]).replace('\n\n[태그] ','')
txt=txt.replace('[제목] '+t+'\n','[제목] '+t+'\n[사진 01] 대표 사진 (본문 맨 위 · 대표로 지정)\n',1)
txt=re.sub(r'\n+\[태그\]\s*$','\n',txt)
tf=D+'jisandream_%s.txt'%slug; open(tf,'w').write(txt)
G='/home/claude/helper/gas.py'; up=[]
for f in [hf,tf]: subprocess.run(['python3',G,'fput','블로그/협업/4_어사이드/원고',f],capture_output=True); up.append(os.path.basename(f))
for fn in sorted(os.listdir(D+'img')): subprocess.run(['python3',G,'fput','블로그/협업/4_어사이드/원고/jisandream_%s'%slug,D+'img/'+fn],capture_output=True); up.append(fn)
print(json.dumps({'title':t,'html':hf,'txt':tf,'up':up},ensure_ascii=False))

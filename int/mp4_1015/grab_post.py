import urllib.request,re,html,sys,os
from PIL import Image,ImageDraw
no,tag=sys.argv[1],sys.argv[2]; BLOG=sys.argv[3] if len(sys.argv)>3 else 'champion_chart'; D=f'/home/claude/v2src/t1102/{tag}'; os.makedirs(D,exist_ok=True)
H={'User-Agent':'Mozilla/5.0'}
s=urllib.request.urlopen(urllib.request.Request(f'https://blog.naver.com/PostView.naver?blogId={BLOG}&logNo={no}',headers=H),timeout=20).read().decode('utf8','ignore')
title=re.search(r'<title>(.*?)</title>',s).group(1).replace(' : 네이버 블로그',''); b=s[s.find('se-main-container'):]
txt=re.sub(r'\s+',' ',re.sub(r'\{[^{}]*\}','',re.sub('<[^>]+>',' ',html.unescape(b)))).split('같이 보면 좋은 글')[0]
open(f'{D}/post.txt','w').write(title+'\n'+txt); print(title); print(txt[:2600])
imgs=[]
for x in re.findall(r'(https://(?:postfiles\.pstatic\.net|blogger\.googleusercontent\.com)/[^"\'\s<>]+)',b):
    x=x.split('?')[0] if 'pstatic' in x else x
    if x not in imgs: imgs.append(x)
th=[]; HH={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}
for i,u in enumerate(imgs):
    try:
        open(f'{D}/{i:02d}.jpg','wb').write(urllib.request.urlopen(urllib.request.Request(u+('?type=w966' if 'pstatic' in u else ''),headers=HH),timeout=20).read())
        im=Image.open(f'{D}/{i:02d}.jpg').convert('RGB'); t=im.copy(); t.thumbnail((260,260)); th.append(t)
    except Exception: th.append(Image.new('RGB',(260,260),'gray'))
W=7; S=Image.new('RGB',(W*270,max(1,(len(th)+W-1)//W)*290),'white'); d=ImageDraw.Draw(S)
for k,t in enumerate(th): S.paste(t,((k%W)*270,(k//W)*290)); d.text(((k%W)*270+4,(k//W)*290+268),str(k),fill='red')
S.save(f'/tmp/{tag}_sheet.jpg'); print(len(imgs))

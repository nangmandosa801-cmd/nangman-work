from PIL import Image, ImageDraw
from viz import kr, SANS, SANSR
def interior(out,title):
    W,H=900,330; im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,5],fill=(31,56,100)); d.line([0,H-2,W,H-2],fill=(230,230,230),width=2)
    d.text((45,38),'옆 블로그 · 낭만 인테리어',font=kr(SANSR,24),fill=(46,92,138))
    d.text((45,82),'집을 샀다면, 고칠 곳은 한 번에',font=kr(SANS,46),fill=(31,56,100))
    d.text((45,155),'중문 · 샷시 · 줄눈 · 입주청소 · 단열 · 매트',font=kr(SANSR,30),fill=(51,51,51))
    f=kr(SANS,28); d.text((45,210),'blog.naver.com/champion_chart',font=f,fill=(46,92,138))
    d.text((45+d.textlength('blog.naver.com/champion_chart',font=f)+36,210),'010-2882-8165',font=f,fill=(46,92,138))
    fs=kr(SANSR,17); t=title
    while d.textlength(t,font=fs)>800: t=t[:-2]
    if t!=title: t=t.rstrip()+' …'
    d.text((45,280),t,font=fs,fill=(200,205,215))
    im.save(out)
if __name__=='__main__':
    import sys; interior(sys.argv[1],sys.argv[2])

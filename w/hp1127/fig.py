import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image, ImageDraw, ImageFont
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
fm.fontManager.addfont(B); plt.rcParams['font.family']=fm.FontProperties(fname=B).get_name()
NAVY='#1f3a5f'; GREEN='#2e8b57'; GRAY='#b8c2cc'
# 01 썸네일 C형
im=Image.new('RGB',(1080,1080),'white');d=ImageDraw.Draw(im)
f=lambda s:ImageFont.truetype(B,s,index=0)
d.text((540,170),'하남 집값',font=f(84),fill=NAVY,anchor='mm')
d.text((540,300),'같은 84㎡ · 같은 단지 1년 비교',font=f(46),fill='#555',anchor='mm')
d.text((270,560),'31%',font=f(190),fill=GREEN,anchor='mm')
d.text((540,575),'vs',font=f(64),fill='#888',anchor='mm')
d.text((810,560),'11%',font=f(190),fill=NAVY,anchor='mm')
d.text((270,730),'미사 · 감일',font=f(52),fill=GREEN,anchor='mm')
d.text((810,730),'덕풍동',font=f(52),fill=NAVY,anchor='mm')
d.rectangle([0,960,1080,1080],fill=NAVY);d.text((540,1020),'낭만 부동산 분석 플랫폼',font=f(44),fill='white',anchor='mm')
im.save('01.jpg',quality=92)
def bar(fn,title,labels,vals,colors,fmt):
    fig,ax=plt.subplots(figsize=(10.8,8.1),dpi=100)
    b=ax.bar(labels,vals,color=colors,width=0.6)
    for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,r.get_height()*1.02,fmt(v),ha='center',fontsize=26)
    ax.set_title(title,fontsize=30,pad=24,loc='left');ax.set_yticks([]);
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.tick_params(axis='x',labelsize=22);ax.set_ylim(0,max(vals)*1.2)
    fig.text(0.99,0.01,'국토교통부 실거래 · 전용 83~86㎡ · 낭만 부동산 분석 플랫폼',ha='right',fontsize=14,color='#777')
    plt.tight_layout(rect=[0,0.03,1,1]);fig.savefig(fn,pil_kwargs={'quality':92});plt.close()
bar('02.jpg','하남 84㎡ 가운데 값, 1년 새 1억 8천만원 올랐습니다',['작년 7~10월\n714건','올해 7~10월\n377건'],[10.145,12.0],[GRAY,GREEN],lambda v:{10.145:'10억 1,450만',12.0:'12억'}[v])
bar('03.jpg','같은 단지 1년 비교, 미사·감일 31% · 덕풍동 11~14%',['미사강변\n파밀리에','감일\n센트레빌','하남풍산\n센트레빌','풍산\n아이파크5'],[31.4,31.1,13.5,11.4],[GREEN,GREEN,GRAY,GRAY],lambda v:f'{v:.0f}%')

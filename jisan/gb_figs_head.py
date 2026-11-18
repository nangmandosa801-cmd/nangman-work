# -*- coding: utf-8 -*-
# 11/16~11/22 지산드림 일주일치 그림: 01 썸네일 · 02 · 03 · 06 배너 → /mnt/user-data/outputs/jisandream/<폴더>/img/
import os,sys
exec(open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0])
exec(open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0].split("GRN=")[1].join(["GRN=",""]) if False else open('/home/claude/jisan/cafe_byop_figs.py').read().split('# 카페')[0])
sys.path.insert(0,'/home/claude/jisan/photo'); from kwphoto import thumb
cwd=os.getcwd(); os.chdir('/home/claude/jisan/choi')
exec(open('draw.py').read().split("O='/mnt/user-data/outputs/jisandream/'")[0])
os.chdir(cwd)
exec(open('/home/claude/jisan/two_figs.py').read().split("for s in ['maedo'")[0])
_head=head
def head(f,a,b): _head(f,b,a)
OUT='/mnt/user-data/outputs/jisandream/'
def P(f): d=OUT+f+'/img/'; os.makedirs(d,exist_ok=True); return d
def J(src,dst): Image.open(src).convert('RGB').save(dst,quality=92)
def ban(f,big,l1,l2):
    global H; _h=H; H='/mnt/user-data/outputs/jisandream/hwesonji/'
    d=P(f); banners(d,'tmp',big,l1,l2,'지산드림'); H=_h; J(d+'jisandream_tmp_banner.png',d+'06.jpg')
    for x in ['jisandream_tmp_banner.png','jisandream_tmp_banner_small.png']:
        try: os.remove(d+x)
        except: pass
def card(lines,title,sub,note,out):
    fig,ax=plt.subplots(figsize=(10.6,5.4)); fig.subplots_adjust(bottom=0.13,top=0.77,left=0.05,right=0.95)
    ax.set_xlim(0,10); ax.set_ylim(0,len(lines)); ax.set_axis_off()
    for i,(a,b) in enumerate(lines):
        y=len(lines)-1-i+0.5
        ax.text(0.3,y,a,fontsize=26,color=CYAN,fontproperties=FB,va='center'); ax.text(1.3,y,b,fontsize=21,color=DEEP,fontproperties=FB,va='center')
    head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
TMP='/tmp/wk_'
SANG='/mnt/user-data/outputs/jisandream/sangga/'
hanam,_=basemap(37.585,127.13,37.49,127.26,13)


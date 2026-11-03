exec(open('/home/claude/jisan/gpimfigs.py').read().split('# fig1 크기별')[0])
import numpy as np
WARN='#B5533C'
def yearly(yrs,n,py,kick,title,path,note,lab_n=None,lab_py=None,last_label="(1~8월)"):
    fig,ax=plt.subplots(figsize=(10.6,7.2)); fig.subplots_adjust(bottom=0.12,top=0.78,left=0.07,right=0.93)
    x=np.arange(len(yrs)); L=len(yrs)
    ax.bar(x,n,0.65,color=[LIGHT if i<L-1 else CYAN for i in range(L)])
    nm=max(n); pm=max(py)
    for i in (lab_n or [int(np.argmax(n)),L-1]): ax.text(x[i],n[i]+nm*0.015,f'{n[i]:,}건',ha='center',va='bottom',fontsize=13,color=DEEP,fontproperties=FB)
    ax2=ax.twinx(); ax2.plot(x,py,color=DEEP,lw=3.2,marker='o',ms=6)
    for i in (lab_py or [0,int(np.argmax(py)),L-1]): ax2.text(x[i]+(0.5 if i==0 else 0),py[i]+pm*0.03,f'{py[i]:,}만원',ha='center',va='bottom',fontsize=14,color=DEEP,fontproperties=FB)
    step=1 if L<=10 else 2
    for i,yv in enumerate(yrs):
        if i%step==0 and i<L-1: ax.text(x[i],-nm*0.03,str(yv)[2:]+"'",ha='center',va='top',fontsize=12,color=GREY,fontproperties=FR)
    ax.text(x[L-1],-nm*0.03,str(yrs[-1])[2:]+"'\n"+last_label,ha='center',va='top',fontsize=11,color=GREY,fontproperties=FR,linespacing=1.3)
    ax.set_ylim(-nm*0.07,nm*2.05); ax2.set_ylim(-pm*0.9,pm*1.25); ax.set_axis_off(); ax2.set_axis_off()
    ax.text(L-0.7,-nm*0.05-nm*0.02,'' if False else '',fontsize=1); fig.text(0.93,0.80,'막대 = 거래 건수 · 선 = 평당 중앙값(전용)',ha='right',fontsize=13,color=GREY,fontproperties=FR,va='top')
    head(fig,kick,title); finish(fig,O+path,note,brand='지산드림',allow_outside=True,strict=False)

def chgbar(rows,kick,title,path,note,xmin=-70,xmax=25,thr=-20,left=0.36):
    fig,ax=plt.subplots(figsize=(10.6,7.8)); fig.subplots_adjust(bottom=0.08,top=0.80,left=left,right=0.95)
    m=len(rows); ys=list(range(m))[::-1]
    for y,(lab,v,cnt) in zip(ys,rows):
        c=CYAN if v>0 else (WARN if v<=thr else LIGHT)
        ax.barh(y,v,color=c,height=0.6)
        ax.text(v+(0.6 if v>=0 else -0.6),y,f'{v:+.0f}%',va='center',ha='left' if v>=0 else 'right',fontsize=17,color=DEEP if v>thr else WARN,fontproperties=FB)
        ax.text(xmin,y+0.12,lab,va='center',ha='right',fontsize=16,color=DEEP,fontproperties=FB)
        if cnt: ax.text(xmin,y-0.3,cnt,va='center',ha='right',fontsize=12,color=GREY,fontproperties=FR)
    ax.axvline(0,color=LINE,lw=1.2); ax.set_xlim(xmin,xmax); ax.set_ylim(-0.7,m-0.3); ax.set_axis_off()
    head(fig,kick,title); finish(fig,O+path,note,brand='지산드림',allow_outside=True,strict=False)

def hbar2(rows,hi,kick,title,path,note,xmax,unit='만원',fmt='{:.1f}'):
    n=len(rows); fig,ax=plt.subplots(figsize=(10.6,2.6+0.62*n)); fig.subplots_adjust(bottom=0.09,top=1-1.6/(2.6+0.62*n),left=0.34,right=0.93)
    ys=list(range(n))[::-1]
    for y,(lab,v,cnt) in zip(ys,rows):
        c=CYAN if lab in hi else LIGHT
        ax.barh(y,v,color=c,height=0.6)
        ax.text(v+xmax*0.012,y,f'{fmt.format(v)}{unit}',va='center',ha='left',fontsize=18 if lab in hi else 15,color=DEEP if lab in hi else GREY,fontproperties=FB)
        ax.text(-xmax*0.02,y+(0.14 if cnt else 0),lab,va='center',ha='right',fontsize=15,color=DEEP,fontproperties=FB)
        if cnt: ax.text(-xmax*0.02,y-0.3,cnt,va='center',ha='right',fontsize=11,color=GREY,fontproperties=FR)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
    head(fig,kick,title); finish(fig,O+path,note,brand='지산드림',allow_outside=True,strict=False)

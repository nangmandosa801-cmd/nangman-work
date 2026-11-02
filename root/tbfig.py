import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_tojibosang_'

render('낭만 부동산 분석 플랫폼 · 토지보상',
       ['토지보상 이의신청,','30일보다 먼저 볼 건 이의유보'],
       '공탁금을 그냥 찾으면 승복한 것으로 볼 수 있습니다', O+'thumb.png')

def box(ax,x,y,w,h,fc,ec,title,sub=None,tc='white',fs=17,ss=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.06',
                 fc=fc,ec=ec,lw=2.0))
    if sub:
        ax.text(x+w/2,y+h*0.62,title,ha='center',va='center',fontsize=fs,fontweight='bold',color=tc)
        ax.text(x+w/2,y+h*0.26,sub,ha='center',va='center',fontsize=ss,color=tc)
    else:
        ax.text(x+w/2,y+h/2,title,ha='center',va='center',fontsize=fs,fontweight='bold',color=tc)

def arr(ax,x1,y1,x2,y2,c,label=None,lx=None,ly=None,ls=15):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),
        arrowprops=dict(arrowstyle='-|>,head_width=0.28,head_length=0.55',color=c,lw=2.4))
    if label:
        ax.text(lx,ly,label,ha='center',va='center',fontsize=ls,fontweight='bold',color=c,
                bbox=dict(boxstyle='round,pad=0.28',fc='white',ec=c,lw=1.6))

# ---- fig1 : 절차와 기한 ----
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.03,0.07,0.94,0.75])
fig.text(0.04,0.955,'토지보상 불복 절차와 기한 · 수용재결서를 받은 날부터',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'30일 · 90일 · 60일, 세는 날은 모두 서류를 받은 날입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.set_xlim(0,10); ax.set_ylim(0,6.6); ax.axis('off')

box(ax,0.1,2.55,2.05,1.5,NAVY,NAVY,'수용재결서','정본 수령')
arr(ax,2.25,3.80,4.05,5.30,MID,'90일',3.05,4.85)
arr(ax,2.25,3.10,4.05,3.10,WARN,'30일',3.15,3.55)
box(ax,4.15,4.55,2.6,1.5,MID,MID,'행정소송','이의신청 없이 바로')
box(ax,4.15,2.35,2.6,1.5,WARN,WARN,'이의신청','중앙토지수용위원회')
arr(ax,6.85,3.10,7.55,3.10,SAND)
box(ax,7.65,2.35,2.25,1.5,IVORY,SAND,'이의재결',None,tc=NAVY,fs=17)
arr(ax,8.78,2.25,8.78,1.35,MID,'60일',9.55,1.80)
box(ax,7.05,0.20,3.0,1.1,MID,MID,'행정소송',None,fs=17)

ax.text(0.1,1.55,'이의신청을 반드시 거쳐야\n소송을 낼 수 있는 것은 아닙니다',fontsize=14.5,color=SAND,
        fontweight='bold',ha='left',va='center',linespacing=1.5)
finish(fig,O+'fig1.png','토지보상법상 수용재결 불복 절차 · 기간은 모두 재결서 정본을 받은 날부터 계산',allow_outside=True,strict=False)

# ---- fig2 : 공탁금 수령 ----
fig=plt.figure(figsize=(11.2,7.4)); ax=fig.add_axes([0.04,0.07,0.92,0.74])
fig.text(0.04,0.955,'보상금이 공탁된 뒤 공탁금을 찾을 때',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'이의유보를 남겼는지에 따라 결과가 달라집니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.set_xlim(0,10); ax.set_ylim(0,6.0); ax.axis('off')

box(ax,0.15,4.45,4.5,1.25,WARN,WARN,'이의유보 없이 공탁금 수령',None,fs=18)
box(ax,5.35,4.45,4.5,1.25,MID,MID,'이의유보를 남기고 수령',None,fs=18)
arr(ax,2.40,4.35,2.40,3.35,WARN)
arr(ax,7.60,4.35,7.60,3.35,MID)
box(ax,0.15,1.85,4.5,1.4,'#F3E6E1',WARN,'재결에 승복한 것으로','볼 수 있습니다',tc=WARN,fs=18,ss=17)
box(ax,5.35,1.85,4.5,1.4,'#E4EDF6',MID,'이의신청과 소송을','계속할 수 있습니다',tc=NAVY,fs=18,ss=17)

ax.text(5.0,0.85,'이미 이의신청이나 소송을 냈다는 사실만으로는 이의유보로 보지 않을 수 있습니다',
        ha='center',va='center',fontsize=15.5,color=NAVY,fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5',fc=IVORY,ec=LINE,lw=1.5))
finish(fig,O+'fig2.png','대법원 1982. 11. 9. 선고 82누197 전원합의체 판결의 취지 · 개별 사안은 변호사·행정사에게 확인',allow_outside=True,strict=False)
print('ok')

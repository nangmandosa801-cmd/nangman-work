import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib import font_manager as fm
FP='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; fm.fontManager.addfont(FP)
plt.rcParams['font.family']=fm.FontProperties(fname=FP).get_name()
NAVY='#1F3864'; BLUE='#2E5C8A'; GOLD='#C9A227'; RED='#B5523B'; GRAY='#B8C2CE'
def foot(f): f.text(0.05,0.03,'낭만 인테리어 · 문의 010-2882-8165',fontsize=12,color='#8A8578')
# 1 위치도
f,ax=plt.subplots(figsize=(9,6),dpi=110); ax.axis('off'); ax.set_xlim(0,100); ax.set_ylim(0,70)
f.text(0.05,0.93,'3연동 중문 스토퍼는 여기 있습니다',fontsize=21,color=NAVY,weight='bold')
f.text(0.05,0.875,'현관 쪽에서 본 모습 · 위쪽 레일 양 끝에 하나씩',fontsize=13,color='#5A6675')
ax.add_patch(Rectangle((8,52),84,4,color='#7E7A70')); ax.text(50,57.5,'위쪽 레일 (상부레일)',ha='center',fontsize=13,color='#333')
ax.add_patch(Rectangle((8,8),84,1.5,color='#7E7A70')); ax.text(50,4.5,'아래 레일 · 가이드',ha='center',fontsize=12,color='#555')
for i,x in enumerate([12,38,64]):
    ax.add_patch(Rectangle((x,10),25,41,facecolor='#E6EEF7',edgecolor=BLUE,lw=2))
    ax.text(x+12.5,30,['첫째 문\n(손잡이)','둘째 문','셋째 문'][i],ha='center',va='center',fontsize=13,color=NAVY)
for x in [9.5,88]:
    ax.add_patch(Rectangle((x,52.3),2.6,3.4,color=RED))
ax.annotate('스토퍼 ①\n닫힐 때 멈추는 자리',xy=(10.8,52),xytext=(2,40),fontsize=12,color=RED,bbox=dict(fc='white',ec='none',pad=2),arrowprops=dict(arrowstyle='->',color=RED))
ax.annotate('스토퍼 ②\n열릴 때 멈추는 자리',xy=(89.3,52),xytext=(74,40),fontsize=12,color=RED,bbox=dict(fc='white',ec='none',pad=2),arrowprops=dict(arrowstyle='->',color=RED))
ax.add_patch(Rectangle((14,49.5),7,2,color=NAVY)); ax.annotate('댐퍼 · 첫째 문 위',xy=(17.5,49.5),xytext=(24,44),fontsize=12,color=NAVY,bbox=dict(fc='white',ec='none',pad=2),arrowprops=dict(arrowstyle='->',color=NAVY))
ax.text(50,62.5,'제품마다 모양과 개수가 다를 수 있습니다',ha='center',fontsize=11,color='#8A8578')
foot(f); f.savefig('img/fig_wichi.png'); plt.close(f)
# 2 교체 순서
f,ax=plt.subplots(figsize=(9,6),dpi=110); ax.axis('off'); ax.set_xlim(0,100); ax.set_ylim(0,70)
f.text(0.05,0.93,'스토퍼 교체, 이 순서로 합니다',fontsize=21,color=NAVY,weight='bold')
f.text(0.05,0.875,'걸리는 시간은 대개 짧고, 같은 부품을 구하는 게 먼저입니다',fontsize=13,color='#5A6675')
st=['문을 반대쪽 끝으로 밀어 둡니다','레일 덮개가 있으면 떼고 스토퍼를 찍습니다','고정 나사를 풀고 헌 스토퍼를 빼냅니다','같은 모델을 같은 자리에 끼웁니다','댐퍼 걸쇠와 닿는 위치를 맞추고 조입니다','열 번쯤 여닫아 보고 소리를 들어 봅니다']
for i,s in enumerate(st):
    y=56-i*9
    ax.add_patch(FancyBboxPatch((6,y-3),88,6.2,boxstyle='round,pad=0.4',facecolor='#F2F5F9' if i%2==0 else '#FFFFFF',edgecolor=GRAY))
    ax.text(10,y,str(i+1),fontsize=16,color=GOLD if i==3 else BLUE,weight='bold',va='center')
    ax.text(16,y,s,fontsize=15,color='#222',va='center')
foot(f); f.savefig('img/fig_sunseo.png'); plt.close(f)

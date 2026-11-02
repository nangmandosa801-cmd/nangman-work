import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.96,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.92,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 부품값 vs 출장 포함
R=[('호차 (2개)',0.9,20),('와이어·상부 부속',6.2,16),('도어클로저',4.0,13),('댐퍼',1.65,None),('이탈방지구',0.15,None),('모헤어 (3m)',0.6,None)]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.24,0.10,0.72,0.72])
head(fig,'공개된 부품 가격과 출장 수리 견적 사례 · 단위 만원 · 범위는 중간값','중문 수리 비용, 부품은 몇천 원인데 출장 수리는 15만~25만원입니다')
n=len(R)
for i,(nm,p,t) in enumerate(R):
    y=n-1-i
    ax.barh(y+0.17,p,0.3,color=NAVY); ax.text(p+0.3,y+0.17,f'부품 {p:g}만원',va='center',fontsize=12.5,color=NAVY,fontweight='bold')
    if t: ax.barh(y-0.17,t,0.3,color=WARN); ax.text(t+0.3,y-0.17,f'출장 수리 {t}만원 안팎',va='center',fontsize=12.5,color=WARN,fontweight='bold')
    else: ax.text(0.3,y-0.17,'셀프 가능 · 출장 사례 없음',va='center',fontsize=12,color=MID)
    ax.text(-0.3,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,30); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'gojang10_fig1.png','부품가: 문고리닷컴·중산몰·샤시마켓 · 수리 견적: 클리앙(2023)·DVD프라임(2019)·업체 글 · 출장비 3만원 별도',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 책임 매트릭스
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.04,0.06,0.92,0.74])
head(fig,'민법 제623조 · 대법원 2004다2151 · LH 임대주택 수선비 부담 기준 제3·8조·별표1','중문 고장 세입자·집주인, 노후는 집주인 파손은 세입자 직접 단 중문은 세입자입니다')
rows=[('집주인이 단 중문 · 호차 마모·처짐·노후','집주인','노후·마모·개폐불량 = 임대인'),('집주인이 단 중문 · 부딪혀 깨뜨림','세입자','파손·훼손 = 임차인'),('레일 청소 · 나사 조임 · 기름 치기','세입자','일상 유지관리 · 사소한 수선'),('유리가 혼자 깨짐 (자파)','집주인 쪽','자연적 깨짐 = 임대인 · 사진이 증거'),('세입자가 새로 단 중문 고장','세입자','별도 설치 품목 = 임차인 관리'),('세입자가 단 중문 · 이사 갈 때','철거 또는 두고 가기','두고 가도 비용 청구 못 함')]
ax.text(0.02,1.0,'상황',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold'); ax.text(0.50,1.0,'누가',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold'); ax.text(0.68,1.0,'근거',ha='left',va='bottom',fontsize=14,color=MID,fontweight='bold')
for i,(a,b,c) in enumerate(rows):
    y=0.88-i*0.17; col=WARN if '세입자' in b else NAVY
    ax.plot([0.02,0.98],[y-0.085,y-0.085],color=LINE,lw=1)
    ax.text(0.02,y,a,ha='left',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(0.50,y,b,ha='left',va='center',fontsize=15,color=col,fontweight='bold')
    ax.text(0.68,y,c,ha='left',va='center',fontsize=12.5,color=MID)
ax.set_xlim(0,1); ax.set_ylim(-0.12,1.1); clean(ax)
finish(fig,O+'gojang10_fig2.png','LH 기준은 임대주택용 · 민간 전·월세는 계약서 특약이 우선 · 세입자가 달 때는 동의와 철거·존치를 한 줄 적어 두기',brand='낭만 인테리어',allow_outside=True,strict=False)

render_interior('낭만 인테리어 · 중문 고장',['중문 고장 증상 10가지','셀프 · 수리 · 누가 내나'],'부품 몇천 원 · 출장 15만~25만원 · WD-40는 안 됩니다','노후는 집주인 · 파손은 세입자 · 유리는 사진 먼저',O+'gojang10_thumb.png')
print('ok')

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'; LINE='#D5DCE6'
def base(top,title,h):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.95,top,fontsize=19,color=BLUE,va='top'); fig.text(0.045,0.895,title,fontsize=31,color=NAVY,fontweight='bold',va='top'); return fig
def won(v):
    e=int(round(v*10000))//10000; r=int(round(v*10000))%10000
    s=(f'{r//1000}천' if r%1000==0 else f'{r:,}')+'만' if r else ''
    return (f'{e}억 '+s if e else s).strip() if (e or r) else '0'
rows=[('고덕 힐스테이트 고덕스카이시티 84㎡',2.8,2.94,3.75),('고덕 힐스테이트 고덕스카이시티 76㎡',2.5,2.625,3.5),('고덕 힐스테이트 고덕센트럴 84㎡',2.8,3.0,3.6),('칠원동 지제역 동문디이스트 5단지 84㎡',2.3,2.4125,2.55),('서정동 힐스테이트 평택 더퍼스트 84㎡',2.8,2.8,2.8),('서정동 힐스테이트 평택 더퍼스트 59㎡',2.2,2.3,2.1)]
fig=base('평택 아파트 전세 · 2024년 입주 단지 · 2026년 계약','고덕은 2년 만에 30% 넘게, 서정동은 그대로',8.6)
ax=fig.add_axes([0.42,0.13,0.55,0.64])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.tick_params(length=0)
n=len(rows)
for i,(nm,p,g,nw) in enumerate(rows):
    y=n-i; up=nw>p*1.02; c=NAVY if up else '#7A8590'
    ax.plot([p,nw],[y,y],color='#DDE3EA',lw=10,solid_capstyle='round',zorder=1)
    ax.scatter([p],[y],s=170,facecolor='white',edgecolor=GRAY,lw=3,zorder=3)
    ax.scatter([nw],[y],s=230,color=c,zorder=4)
    d=nw-p; ax.text(max(nw,p)+0.05,y,('+' if d>0 else ('−' if d<0 else '±'))+(won(abs(d)) if d else '0'),fontsize=18,color=c,fontweight='bold',va='center')
    ax.text(-0.02,y,nm,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=17,color=c,fontweight='bold')
ax.set_xlim(1.95,4.3); ax.set_ylim(0.4,n+0.9); ax.set_yticks([])
ax.set_xticks([2,2.5,3,3.5,4]); ax.set_xticklabels(['2억','2억 5천','3억','3억 5천','4억'],fontsize=16,color='#7A8590')
ax.scatter([2.05],[n+0.6],s=150,facecolor='white',edgecolor=GRAY,lw=3); ax.text(2.1,n+0.6,'2년 전 입주장',fontsize=17,va='center',color='#555')
ax.scatter([2.95],[n+0.6],s=200,color=NAVY); ax.text(3.0,n+0.6,'올해 새 세입자',fontsize=17,va='center',color=NAVY,fontweight='bold')
fig.text(0.045,0.035,'2년 전 입주장 = 갱신 계약에 적힌 종전 보증금 중앙값 · 올해 새 세입자 = 2026년 신규 전세 중앙값 · 국토교통부 전월세 실거래',fontsize=14,color='#8A8578')
fig.savefig('img/nangman_pyeongtaek_1_2024.png'); plt.close()
fig=base('평택 입주물량 · 이번 겨울 입주 시작 단지','넉 달 동안 약 9천 세대가 열쇠를 받습니다',8.4)
ax=fig.add_axes([0.40,0.1,0.52,0.7]); ax.axis('off')
R=[('2026년 11월','화양 푸르지오 센터파인',851),('2026년 11월','화양 동문 디이스트',753),('2027년 1월','지제역 쌍용 더 플래티넘',1340),('2027년 1월','브레인시티 대광로제비앙',1182),('2027년 2월','브레인시티 중흥S-클래스',1980),('2027년 2월','진위역 서희스타힐스',1659),('2027년 2월','지제역 해링턴 플레이스',1209)]
n=len(R)
for i,(m,nm,v) in enumerate(R):
    y=n-i; c=NAVY if v>=1000 else GRAY
    ax.barh(y,v,0.62,color=c); ax.text(v+30,y,f'{v:,}세대',fontsize=19,va='center',fontweight='bold',color=NAVY if v>=1000 else '#555')
    ax.text(-30,y,nm,ha='right',va='center',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(-30,y-0.33,m,ha='right',va='center',fontsize=14,color='#7A8590')
ax.set_xlim(0,2500); ax.set_ylim(0.3,n+0.6)
fig.text(0.045,0.035,'남색은 1,000세대 넘는 큰 단지 · 입주 시작 달은 청약홈 · 모집공고 기준 · 실제 입주지정기간은 단지 공지 확인',fontsize=14,color='#8A8578')
fig.savefig('img/nangman_pyeongtaek_2_ipju.png'); plt.close()

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_pyeongtaek_1_2024_v2.png', '고덕은 2년 만에 30% 넘게, 서정동은 그대로', [('고덕 힐스테이트 고덕스카이시티 84㎡|2년 전 입주장', 2.8, '2억 8,000만', False), ('고덕 힐스테이트 고덕스카이시티 84㎡|올해 새 세입자', 3.75, '3억 7,500만', True), ('서정동 힐스테이트 평택 더퍼스트 84㎡|2년 전 입주장', 2.8, '2억 8,000만', False), ('서정동 힐스테이트 평택 더퍼스트 84㎡|올해 새 세입자', 2.8, '2억 8,000만', False)], note='평택 2024년 입주 단지 전세 · 다른 단지는 본문 표')
bars('img/nangman_pyeongtaek_2_ipju_v2.png', '넉 달 동안 약 9천 세대가 열쇠를 받습니다', [('2026년 11월|2곳', 1604, '1,604세대', False), ('2027년 1월|2곳', 2522, '2,522세대', False), ('2027년 2월|3곳', 4848, '4,848세대', True)], note='평택 입주 시작 단지 7곳')
print('v2 ok')

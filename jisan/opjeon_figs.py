src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from matplotlib.patches import FancyBboxPatch
B='/mnt/user-data/outputs/jisandream/byop/'
O='/mnt/user-data/outputs/jisandream/opjeon/'
GOOD='#1B7A9E'; WARN='#C9962E'; BAD='#B5503C'
def cards(fig,ax,cols,title,sub):
    ax.set_xlim(0,10); ax.set_ylim(0,6); ax.set_axis_off()
    w=10/len(cols)
    for k,(h,c,lines) in enumerate(cols):
        x0=k*w+0.15
        ax.add_patch(FancyBboxPatch((x0,0.3),w-0.3,5.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
        ax.add_patch(FancyBboxPatch((x0,4.3),w-0.3,1.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c,lw=3))
        ax.text(x0+(w-0.3)/2,4.9,h,ha='center',va='center',fontsize=17,color='white',fontproperties=FB)
        for j,(t,big) in enumerate(lines):
            ax.text(x0+(w-0.3)/2,3.6-j*0.8,t,ha='center',va='center',fontsize=20 if big else 16,color=c if big else DEEP,fontproperties=FB if big else FR)
    head(fig,title,sub)
# fig1
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.06,top=0.8,left=0.03,right=0.97)
cards(fig,ax,[('오피스텔',GOOD,[('전입신고 됨',1),('별내자이 더 스타',0),('이그제큐티브 (전환 뒤)',0)]),
              ('생활형 숙박시설',BAD,[('전입신고 안 됨',1),('주거로 쓰면',0),('이행강제금 대상',0)]),
              ('지식산업센터 기숙사',WARN,[('주택 수 따로 봄',1),('전입하면 세금에서',0),('주택으로 볼 수 있음',0)])],
      '지산드림 · 오피스텔 전입신고','건축물대장 「주용도」 칸이 정합니다')
finish(fig,O+'jisandream_op_jeonip_fig1.png','건축물대장은 정부24에서 뗄 수 있음 · 세금은 세무사 확인',brand='지산드림',allow_outside=True,strict=False)
# fig2
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.06,top=0.8,left=0.03,right=0.97)
cards(fig,ax,[('전입신고 + 확정일자',GOOD,[('보증금 순서를 잡음',1),('집이 경매로 가도',0),('순서대로 돌려받음',0)]),
              ('전입신고 안 함',BAD,[('순서를 못 잡음',1),('경매 때 뒤로',0),('밀릴 수 있음',0)])],
      '지산드림 · 오피스텔 전입신고 안하고 살면','보증금 4억 신축 오피스텔이면 차이가 큽니다')
finish(fig,O+'jisandream_op_jeonip_fig2.png','주거로 쓰는 오피스텔은 주택임대차보호법을 받음 · 다른 길은 전세권 설정 등기',brand='지산드림',allow_outside=True,strict=False)
# fig3
fig,ax=plt.subplots(figsize=(10.6,6.4)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
for i,(a,v,c,lab) in enumerate([('분양가 (가장 낮은 호실)',6.09,DEEP,'6억 900만원'),('전세 중앙값 (10건)',4.5,CYAN,'4억 5,000만원'),('전세 끼고 사면 (취득세 포함)',1.87,'#C9962E','1억 8,700만원')]):
    y=2-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+0.08,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.1,y,a,ha='right',va='center',fontsize=15,color=DEEP,fontproperties=FB)
ax.set_xlim(0,8.6); ax.set_ylim(-0.6,2.6); ax.set_axis_off()
head(fig,'지산드림 · 생숙 오피스텔 전환','전입신고가 되니 59타입 전세가 4억 5천에 나갑니다')
finish(fig,O+'jisandream_op_jeonip_fig3.png','별내자이 더 스타 이그제큐티브 59타입 · 전세는 2026년 4~9월 국토교통부 실거래',brand='지산드림',allow_outside=True,strict=False)
# fig4
fig,ax=plt.subplots(figsize=(10.6,6.0)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
for i,(a,v,c,lab) in enumerate([('휴밸나인 복층 (월 70만원)',8.0,'#C9962E','연 8.0%'),('휴밸나인 복층 (월 65만원)',7.43,CYAN,'연 7.4%')]):
    y=1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+0.1,y,lab,va='center',fontsize=19,color=DEEP,fontproperties=FB)
    ax.text(-0.1,y,a,ha='right',va='center',fontsize=15,color=DEEP,fontproperties=FB)
ax.set_xlim(0,10.5); ax.set_ylim(-0.6,1.6); ax.set_axis_off()
head(fig,'지산드림 · 지식산업센터 기숙사 전입신고','1억 500만원 복층 원룸, 월세로 연 7~8%')
finish(fig,O+'jisandream_op_jeonip_fig4.png','세전 · 월세 × 12 ÷ 1억 500만원 · 관리비 · 공실 빼고',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
def raw(n):
    im=Image.open(B+'jisandream_byeolnaeyeok_op_photo%d.png'%n).convert('RGB'); return im.crop((40,160,im.width-40,im.height-70))
card(raw(5),'오피스텔 전입신고 · 별내자이 더 스타','생숙에서 오피스텔로 바뀐 760실, 별내역 앞',O+'jisandream_op_jeonip_photo1.png')
card(raw(6),'오피스텔 전입신고 · 59타입 평면','전환 뒤 전입신고 되는 방 둘',O+'jisandream_op_jeonip_photo2.png')
card(raw(1),'오피스텔 전입신고 · 지식산업센터 기숙사','갈매동 휴밸나인, 별내역 걸어서 7분',O+'jisandream_op_jeonip_photo3.png')
card(raw(2),'오피스텔 전입신고 · 휴밸나인 복층 25㎡','계단 위가 침실, 1억 500만원',O+'jisandream_op_jeonip_photo4.png')
thumb([raw(5)],'지산드림 · 별내역 오피스텔 두 곳','오피스텔 전입신고','용도 칸 한 줄이 정합니다','생숙 → 오피스텔 전환 · 기숙사 원룸',O+'jisandream_op_jeonip_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'오피스텔 전입신고',font=F2(52),fill=(255,226,63))
d.text((40,122),'건축물대장 용도와 전환 이력',font=F2(33),fill=(255,255,255))
d.text((40,170),'같이 떼어 봐 드립니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_op_jeonip_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='오피스텔 전입신고, 별내역 앞 생숙 전환 59타입 · 기숙사 원룸 1억 500만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_op_jeonip_banner_small.png')
print('ok')

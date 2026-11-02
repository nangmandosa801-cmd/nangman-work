import pickle,json,sys
sys.argv=['x'];exec(open('/home/claude/mg/viz.py').read().split("CONC, GAP")[0])
from build import datestr
items,by=pickle.load(open('data.pkl','rb'))
def ymd(k): y,m=k.split('-');return f'{y}년 {int(m)}월'
for k in ['2026-11','2026-12','2027-01','2027-02']:
    L=sorted(by[k],key=lambda x:-(x['세대'] or 0))[:8]
    im,d=frame(1080,'낭만 인테리어 · 입주 아파트 현황',f'{ymd(k)} 입주 아파트 {len(by[k])}곳')
    y=210
    for x in L:
        dd,ex=datestr(x);dd=dd.split(' (')[0].split(' · ')[0]
        n=x['단지'].split('(')[0].replace('울산다운2지구 ','다운2지구 ')[:17]
        d.text((60,y),n,font=f(40 if len(n)<=13 else 34,K),fill=NAVY);d.text((W-60-tw(d,dd,f(36)),y+6),dd,font=f(36),fill=RED if ex else GRY);y+=88
    center(d,W/2,y+10,'단지별 날짜 · 시공팀은 링크에서',f(38),ORG)
    im.save(f'card_{k}.png')
# 스레드 문안: 다가오는 단지 (세대 큰 순 + 글 있는 곳)
C=[]
for k in ['2026-11','2026-12','2027-01','2027-02']:
    for x in sorted(by[k],key=lambda x:(0 if x['_p'] else 1,-(x['세대'] or 0)))[:5]:
        dd,ex=datestr(x);dd=dd.split(' · ')[0]
        v=' · '.join(c for c,_ in x['_v'][:5])
        t=f"{x['단지'].split('(')[0]} 입주 {dd}.\n{x['지역']} · {x['세대']:,}세대.\n"+(f"이 단지에 가는 시공팀: {v}.\n" if v else '')+f"{ymd(k)} 입주 아파트 {len(by[k])}곳 날짜를 한 글에 모았습니다."
        C.append(dict(k=k,t=t))
json.dump(C,open('threads.json','w'),ensure_ascii=False,indent=0);print(len(C));print(C[0]['t'])

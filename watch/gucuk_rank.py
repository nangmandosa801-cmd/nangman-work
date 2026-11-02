# 거래가 많은 구축 동네 순위 (2026.10.8) — rt_fetch.py로 받은 실거래에서 가장 최근 두 달(이번 달은 빼고)의 지은 지 20년 넘은 아파트 매매를 읍면동별로 더한다
#   python3 gucuk_rank.py [YYYYMM YYYYMM]  → watch/gucuk_rank.json(순위 · 지난번과 달라진 것) · 화면에 위 20곳
import sys, json, os, datetime
sys.path.insert(0,'/home/claude/watch'); import rt_fetch
def rank(yms=None,top=40):
    today=datetime.date.today()
    if not yms:
        r=rt_fetch.recent(3,today); yms=r[:2]            # 이번 달을 뺀 두 달
    d=rt_fetch.load(yms)
    old=d[d.y<=today.year-21]
    g=old.groupby(['광역','시군','구','읍면동']).size().sort_values(ascending=False)
    out=[]
    for (a,b,c,e),n in g.head(top).items():
        x=old[(old['광역']==a)&(old['시군']==b)&(old['구']==c)&(old['읍면동']==e)]
        dj=x.groupby(['단지명','y']).size().sort_values(ascending=False).head(8)
        out.append(dict(광역=a,시군=b,구=c,동=e,n=int(n),단지=[(k[0],int(k[1]),int(v)) for k,v in dj.items()],소형=int(((x.a>=50)&(x.a<=62)).sum())))
    return dict(yms=yms,made=str(today),all=int(len(d)),old=int(len(old)),rows=out)
if __name__=='__main__':
    R=rank(sys.argv[1:] or None); f='/home/claude/watch/gucuk_rank.json'
    prev=json.load(open(f)) if os.path.exists(f) else None
    if prev:
        pk=[(r['시군'],r['구'],r['동']) for r in prev['rows'][:20]]
        R['new_in_top20']=[f"{r['시군']} {r['구']} {r['동']}".replace('  ',' ') for r in R['rows'][:20] if (r['시군'],r['구'],r['동']) not in pk]
        R['prev_yms']=prev['yms']
    json.dump(R,open(f,'w'),ensure_ascii=False,indent=1)
    print(R['yms'],'· 매매',R['all'],'· 구축',R['old'],'· 새로 20위 안에 든 곳',R.get('new_in_top20'))
    for i,r in enumerate(R['rows'][:20],1): print(i,r['광역'][:2],r['시군'],r['구'],r['동'],r['n'],'|',' · '.join(f'{a}({y}) {n}' for a,y,n in r['단지'][:4]))

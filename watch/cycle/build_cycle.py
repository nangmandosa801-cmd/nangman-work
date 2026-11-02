# 아파트 사이클 장부 — 10/22 사용자 「아파트 사이클 관리 데이터를 관리해」 · 「리모델링 · 수리는 15년 이상」
# 자료: /home/claude/w/apt_all.pkl (국토부 아파트 매매 실거래 · 서울 · 경기 · ~2026-08) + /home/claude/watch/ipju_master.json(입주예정 · 2년차)
import pandas as pd, json, datetime as dt
Y=2026
d=pd.read_pickle('/home/claude/w/apt_all.pkl')
# 10/22 더함: 부동산 채팅이 받아 둔 새 실거래 CSV(서울 · 경기 = apt_all 뒤 달 · 인천 = 전부)
import glob,io,re
def rcsv(f):
    raw=open(f,'rb').read()
    for enc in ('utf-8-sig','cp949'):
        try: s=raw.decode(enc); break
        except: pass
    lines=s.splitlines(); i=next(k for k,l in enumerate(lines) if l.startswith('"NO"'))
    x=pd.read_csv(io.StringIO('\n'.join(lines[i:])),dtype=str)
    return x
pk_last=int(d['계약년월'].max())
add=[]
for f in sorted(glob.glob('/home/claude/watch/rt/apt_*_*.csv'))+sorted(glob.glob('/mnt/user-data/uploads/블로그/실거래/아파트매매_*.csv')):
    try: x=rcsv(f)
    except Exception as e: print('skip',f,e); continue
    x['ym']=x['계약년월'].astype(int)
    inch=x['시군구'].str.startswith('인천')
    x=x[inch | (x['ym']>pk_last)]
    add.append(x)
if add:
    a=pd.concat(add).drop_duplicates(subset=['시군구','번지','단지명','전용면적(㎡)','계약년월','계약일','거래금액(만원)','층'])
    sp=a['시군구'].str.split()
    a['광역']=sp.str[0]; a['시군']=sp.str[1]
    a['구']=sp.apply(lambda v: v[2] if len(v)>3 else '')
    a['읍면동']=sp.str[-1]
    a['a']=pd.to_numeric(a['전용면적(㎡)'],errors='coerce')
    a=a[['시군구','단지명','전용면적(㎡)','거래금액(만원)','계약년월','건축년도','해제사유발생일','광역','시군','구','읍면동','a']]
    d=pd.concat([d,a],ignore_index=True)
    print('더한 거래',len(a),'인천',int(a['광역'].str.startswith('인천').sum()))
d=d[d['해제사유발생일'].astype(str).isin(['-','','nan','None'])]
d['ym']=d['계약년월'].astype(int); d['건축년도']=pd.to_numeric(d['건축년도'],errors='coerce')
d['p']=pd.to_numeric(d['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
key=['광역','시군','구','읍면동','단지명','건축년도']
for k in ['구']: d[k]=d[k].fillna('')
g=d.groupby(key,dropna=False)
last=int(d['ym'].max())
import datetime as _d
if last>=int(_d.date.today().strftime('%Y%m')): last=last-1 if last%100!=1 else last-89   # 이번 달은 덜 모였으니 지난달까지
y1=last-100   # 최근 12개월
d=d[d['ym']<=last]
rec=d[d['ym']>y1].groupby(key,dropna=False).agg(n12=('p','size'),med12=('p','median'),a84=('a',lambda s:(s.between(80,90)).sum()))
allc=g.agg(n_all=('p','size'),first=('ym','min'),lastym=('ym','max'))
t=allc.join(rec,how='left').reset_index().fillna({'n12':0})
t['연차']=Y-t['건축년도']
def stage(a):
    if a<=2: return '2년차'
    if a<=9: return '3~9년 · 부분 보수'
    if a<=14: return '10~14년 · 보일러 · 실리콘 · 줄눈'
    if a<=19: return '15~19년 · 수리 · 부분 리모델링'
    if a<=29: return '20~29년 · 올수리 · 샷시 · 배관 · 욕실'
    return '30년+ · 재건축 이주 · 전세 이사'
t['단계']=t['연차'].apply(lambda a: stage(a) if pd.notna(a) else '')
t['주소']=t['광역'].str.replace('특별시','').str.replace('광역시','').str.replace('도','')+' '+t['시군'].fillna('')+' '+t['구']+' '+t['읍면동'].fillna('')
t=t[t['lastym']>=last-300]   # 3년 안에 거래가 있는 단지만
t=t.sort_values(['n12'],ascending=False)
out=[dict(단지=r.단지명,주소=' '.join(r.주소.split()),건축=int(r.건축년도) if pd.notna(r.건축년도) else None,연차=int(r.연차) if pd.notna(r.연차) else None,단계=r.단계,
          최근12개월매매=int(r.n12),중위가_만원=int(r.med12) if pd.notna(r.med12) else None,전체거래=int(r.n_all)) for r in t.itertuples()]
meta=dict(만든때=dt.datetime.now().strftime('%Y-%m-%d %H:%M'),자료='국토부 아파트 매매 실거래(서울 · 경기 · 인천) 마지막 계약월 '+str(last),최근12개월=f'{y1+1}~{last}',단지수=len(out))
json.dump(dict(meta=meta,단지=out),open('apt_cycle.json','w'),ensure_ascii=False)
s=t.groupby('단계').agg(단지=('단지명','size'),매매12=('n12','sum')).reset_index()
print(meta); print(s.to_string())
top=t[(t['연차']>=15)].head(40)
print(top[['주소','단지명','건축년도','연차','n12','med12']].to_string())

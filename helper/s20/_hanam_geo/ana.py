import json,math,pandas as pd
op=json.load(open('op.json'))['elements']
P={}
for e in op:
    t=e['tags']
    if t.get('name'): P[t['name']]=(e.get('center',{}).get('lat',e.get('lat')),e.get('center',{}).get('lon',e.get('lon')))
ST={'하남풍산역':P['하남풍산'],'하남시청역':P['하남시청'],'하남검단산역':P['하남검단산']}
MAP={'하남풍산아이파크(1단지)':'풍산아이파크1단지','하남풍산아이파크(5단지)':'하남풍산아이파크5단지','동원베네스트':'하남풍산동원베네스트',
'하남풍산센트레빌':'하남풍산센트레빌','풍산삼부르네상스':'하남풍산삼부르네상스','진모루마을현대':'진모루마을현대아파트','더샵하남에디피스':'더샵하남에디피스',
'하남더샵센트럴뷰':'하남더샵센트럴뷰','하남한솔솔파크':'하남한솔솔파크','하남자이':'하남자이아파트','하남덕풍역파크어울림':'하남덕풍역파크어울림아파트',
'벽산블루밍':'벽산블루밍아파트','한솔리치빌(1단지)':'한솔리치빌아파트1단지','한솔리치빌(2단지)':'한솔리치빌아파트2단지','한솔리치빌(3단지)':'한솔리치빌아파트3단지',
'한솔리치빌(5단지)':'한솔리치빌아파트5단지','덕풍쌍용':'덕풍쌍용아파트','덕풍현대':'덕풍현대아파트','서해':'덕풍서해아파트','한승미메이드':'한승미메이드아파트',
'라인':'라인아파트','효천수리골마을':'효천수리골마을아파트','에코타운(A블럭)':'에코타운 1단지','에코타운(B블럭)':'신장에코타운2단지','에코타운(C블럭)':'신장에코타운3단지',
'대명강변타운':'대명강변아파트','백송한신':'백송한신아파트','백조현대':'백조현대아파트','부영':'부영아파트','꿈동산신안':'꿈동산신안아파트','창우마을':'창우마을아파트',
'하남유니온시티에일린의뜰':'하남유니온시티에일린의뜰','하남유시티대명루첸리버파크':'하남UCITY대명루첸리버파크','하남호반써밋에듀파크':'하남호반써밋에듀파크',
'현대홈타운':'하남신장현대홈타운아파트','하남석바대마을동신':'석바대마을동신아파트','해오름한국':'해오름한국아파트','하남힐즈파크푸르지오1단지':'하남힐즈파크푸르지오1단지',
'하남힐즈파크푸르지오2단지':'하남힐즈파크푸르지오2단지','하남힐즈파크푸르지오3단지':'하남힐즈파크푸르지오3단지','미사강변아란티움':'미사강변 아란티움','이편한세상미사':'e편한세상미사',
'신안인스빌':'미사강변 신안인스빌','미사강변브라운스톤엔에이치에프':'미사강변 브라운스톤 엔에이치에프','미사강변센트럴자이':'미사강변센트럴자이','미사강변더샵센트럴포레':'미사강변더샵센트럴포레',
'동일하이빌':'더우개마을동일하이빌아파트','금강KCC':'하남KCC스위첸아파트','은행한신':'은행뉴서울아파트'}
def d(a,b):
    la1,lo1=map(math.radians,a); la2,lo2=map(math.radians,b)
    return 6371000*math.hypot((lo2-lo1)*math.cos((la1+la2)/2),la2-la1)
def load(f):
    m=pd.read_pickle(f); m=m[m['시군구'].str.contains('하남시')&(m['해제사유발생일'].astype(str).str.strip()=='-')&(m['거래유형']!='직거래')]
    m['a']=m['전용면적(㎡)'].astype(float); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int)
    m['ym']=m['계약년월'].astype(int); return m[(m.a>=83)&(m.a<=86)]
m6=load('/home/claude/rtn/M2026.pkl'); m5=load('/home/claude/rtn/M2025.pkl'); m5=m5[m5.ym<=202510]
rows=[]
for k,v in MAP.items():
    if v not in P: print('miss',v); continue
    ds={s:round(d(P[v],p)) for s,p in ST.items()}; s=min(ds,key=ds.get)
    a=m6[m6['단지명']==k]; b=m5[m5['단지명']==k]
    yr=sorted(set(a['건축년도'])|set(b['건축년도']))
    rows.append(dict(cx=k,st=s,dist=ds[s],yr='/'.join(map(str,yr)),n26=len(a),med26=a.p.median() if len(a) else None,n25=len(b),med25=b.p.median() if len(b) else None))
df=pd.DataFrame(rows).sort_values(['st','dist'])
pd.set_option('display.width',200); print(df.to_string())
df.to_pickle('cx_dist.pkl'); json.dump({k:list(v) for k,v in ST.items()},open('stations.json','w'),ensure_ascii=False)

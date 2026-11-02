import pandas as pd, numpy as np
d=pd.read_parquet('/mnt/user-data/outputs/부동산DB.parquet',filters=[('자료','==','토지'),('시군','==','남양주시')])
d.to_pickle('nyj.pkl'); print(d.shape)
print(d[['지목','용도지역','도로조건','계약면적','거래금액(만원)','지분구분','해제사유발생일','계약년월','읍면동']].head(5).to_string())
for c in ['지목','용도지역','도로조건','지분구분']: print(d[c].value_counts(dropna=False).head(14))
print(d['계약년월'].min(),d['계약년월'].max(), d['계약년월'].dtype)

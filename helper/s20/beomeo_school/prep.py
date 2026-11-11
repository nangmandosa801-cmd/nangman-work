import pandas as pd, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
R='/home/claude/rtn/'
G=['27260','27290','27140']
ms=[load(R+f'rawG/MG{y}_{g}.csv') for g in G for y in [2021,2022,2023,2024]]
for f in ['M2025','M2026']:
    d=pd.read_pickle(R+f+'.pkl'); ms.append(d[d['시군구'].str.contains('^대구광역시 (?:수성구|달서구|동구) ')])
m=pd.concat(ms,ignore_index=True); m.to_pickle(R+'MD_daegu_2021_2026.pkl')
rs=[load(R+f'rawG/RG{y}_{g}.csv') for g in G for y in [2024,2025]]
d=pd.read_pickle(R+'R2026.pkl'); rs.append(d[d['시군구'].str.contains('^대구광역시 (?:수성구|달서구|동구) ')])
r=pd.concat(rs,ignore_index=True); r.to_pickle(R+'RD_daegu_2024_2026.pkl')
print(len(m),len(r)); print(m.groupby([m['시군구'].str.split().str[1],m['계약년월'].str[:4]]).size().unstack())

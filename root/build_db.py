# -*- coding: utf-8 -*-
"""실거래 CSV -> 부동산DB.parquet  (메모리 아끼며 한 파일씩 흘려 쓴다)"""
import os, io, gc, csv, re, sys
import pandas as pd, pyarrow as pa, pyarrow.parquet as pq

SRC = '/mnt/user-data/uploads/블로그/실거래'
OUT = '/mnt/user-data/outputs/부동산DB.parquet'

_판별 = [('아파트전월세', ['전월세구분','보증금(만원)'], ['아파트']),
         ('오피스텔전월세', ['전월세구분','보증금(만원)'], ['오피스텔']),
         ('아파트매매', ['단지명','거래금액(만원)','층'], ['아파트']),
         ('오피스텔매매', ['단지명','거래금액(만원)'], ['오피스텔']),
         ('토지', ['지목','용도지역'], ['토지']),
         ('상업업무용', ['건물주용도'], ['상업','업무']),
         ('공장창고', ['건축물주용도','대지면적(㎡)'], ['공장','창고'])]

def _읽기(path):
    raw = open(path,'rb').read()
    for enc in ('cp949','utf-8-sig','utf-8'):
        try: txt = raw.decode(enc); break
        except UnicodeDecodeError: continue
    else: raise RuntimeError('인코딩 실패 '+path)
    lines = txt.splitlines()
    hi = next(i for i,l in enumerate(lines) if l.startswith('"NO"'))
    return pd.read_csv(io.StringIO('\n'.join(lines[hi:])), dtype=str, low_memory=False)

def _자료명(fname, cols):
    for 이름, 필수, 힌트 in _판별:
        if all(c in cols for c in 필수) and any(h in fname for h in 힌트):
            return 이름
    for 이름, 필수, _ in _판별:
        if all(c in cols for c in 필수): return 이름
    return '기타'

def 표준화(d, 자료):
    if '시군구' in d.columns:
        s = d['시군구'].astype(str).str.split()
        d['광역'] = s.str[0]; d['시군'] = s.str[1]
        # 화성시처럼 구가 있는 시는 토큰이 4개다. 읍면동은 언제나 마지막 토큰.
        n = s.str.len()
        d['구'] = s.where(n >= 4).str[2]
        d['읍면동'] = [x[-1] if isinstance(x, list) and x else None for x in s]
    if '계약년월' in d.columns:
        ym = d['계약년월'].astype(str).str.strip()
        d['연'] = ym.str[:4]; d['월'] = ym.str[4:6]
    for c in d.columns:
        if any(k in str(c) for k in ('금액','보증금','월세','면적','층','년도','계약년월','계약일','세대수','대수','동수','연면적','대지면적')):
            d[c] = d[c].astype(str).str.strip().str.replace(',','',regex=False).replace({'nan':None,'-':None,'':None})
        elif d[c].dtype == object:
            d[c] = d[c].astype(str).str.strip().replace({'nan':None})
    d['자료'] = 자료
    return d

files = sorted(f for f in os.listdir(SRC) if f.lower().endswith('.csv'))

def _헤더(path):
    raw = open(path,'rb').read(400000)
    for enc in ('cp949','utf-8-sig','utf-8'):
        try: txt = raw.decode(enc, errors='ignore'); break
        except UnicodeDecodeError: continue
    for l in txt.splitlines():
        if l.startswith('"NO"'):
            return [c.strip().strip('"') for c in next(csv.reader([l]))]
    return []

컬럼 = []
for f in files:
    for c in _헤더(os.path.join(SRC,f)):
        if c not in 컬럼: 컬럼.append(c)
for c in ('광역','시군','구','읍면동','연','월','자료'):
    if c not in 컬럼: 컬럼.append(c)
스키마 = pa.schema([pa.field(c, pa.string()) for c in 컬럼])
print('통합 컬럼', len(컬럼), '개')
writer = None; 총 = 0; 통계 = {}
for f in files:
    d = _읽기(os.path.join(SRC,f))
    자료 = _자료명(f, set(d.columns))
    d = 표준화(d, 자료)
    for c in 컬럼:
        if c not in d.columns: d[c] = None
    d = d.reindex(columns=컬럼)
    t = pa.Table.from_pandas(d.astype(object).where(pd.notna(d), None), preserve_index=False)
    t = t.cast(스키마)
    if writer is None:
        writer = pq.ParquetWriter(OUT, 스키마, compression='zstd')
    writer.write_table(t)
    총 += len(d); 통계[자료] = 통계.get(자료,0) + len(d)
    print(f'  {자료:<10} {len(d):>9,}행  {f}', flush=True)
    del d, t; gc.collect()
writer.close()
print('\n총', f'{총:,}행', os.path.getsize(OUT)//1024//1024, 'MB')
for k,v in sorted(통계.items()): print(f'  {k:<12} {v:>10,}')

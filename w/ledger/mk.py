from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as CL
FN='맑은 고딕'; NAVY='1F3864'; GREY='F2F2F2'; YEL='FFF9DB'
f=lambda b=False,c='000000',s=10: Font(name=FN,bold=b,color=c,size=s)
thin=Side(style='thin',color='D0D0D0'); BD=Border(left=thin,right=thin,top=thin,bottom=thin)
wb=Workbook()
# ---------- 업체
V=wb.active; V.title='업체'
vh=['품목','업체','블로그','지역','수수료율','건당 수수료(원)','전화','블로그 자료','메모']
vend=[
('중문','소소리중문','rodeosky','남양주 인근 · 구리 · 의정부 · 서울 동북',0.10,None,'010-5400-8263','써도 됨',''),
('중문','인천 시흥 중문','ejn590807','경기도',0.10,None,'010-8487-1003','이 업체 블로그에서만',''),
('중문','크로바중문','clovermc2644','충청 (대전 · 청주 · 세종)',0.10,None,'1899-1627','써도 됨',''),
('중문','모던중문','pjh20712','부산 · 경남',0.10,None,'010-8851-8753','써도 됨',''),
('중문','썬중문','dbswkdrms89','경기 위주 · 전국 (경상도 제외)',0.05,None,'010-7770-8171','써도 됨',''),
('샷시','다온창호','daonsash','서울 · 경기 · 인천',0.05,None,'010-2303-6160','써도 됨','계약 1,000만원 넘으면 5% · 그 아래는 건마다 정함 → 장부의 수수료율 칸에 정한 율을 직접 적기'),
('필름','도하인테리어필름','doha_film','남양주 · 구리 · 서울 · 경기 북부',0.05,None,'010-3367-9711','써도 됨',''),
('필름','더빅필름','thebigfilm','경기 남부 (수원 · 용인 · 동탄 · 평택)',0.05,None,'010-3922-9875','써도 됨',''),
('코킹','줄남청','ssu2058','수도권',0.10,None,'010-7770-5203','써도 됨',''),
('문 수리','문수리 임반장','doors9774','수도권',0.10,None,'010-2068-9774','대표가 보내 주는 것만',''),
('방묘문','펫게이트','prore-e-','파주 · 전국이라고 적음',0.10,None,'010-9340-2000','넘긴 손님 사진만',''),
('입주 청소','솜씨종합청소','som_c24','수원',None,50000,'010-3112-2635','넘긴 손님 사진만','율이 아니라 건당 5만원'),
]
V.append(vh)
for r in vend: V.append(list(r))
for c in range(1,len(vh)+1):
    x=V.cell(1,c); x.font=f(True,'FFFFFF'); x.fill=PatternFill('solid',fgColor=NAVY); x.alignment=Alignment(horizontal='center',vertical='center'); x.border=BD
for r in range(2,len(vend)+2):
    for c in range(1,len(vh)+1):
        x=V.cell(r,c); x.font=f(); x.border=BD; x.alignment=Alignment(vertical='center',wrap_text=(c in(4,9)))
    V.cell(r,5).number_format='0%'; V.cell(r,6).number_format='#,##0'
for c,w in zip(range(1,10),[10,18,16,34,10,16,16,22,52]): V.column_dimensions[CL(c)].width=w
V.freeze_panes='A2'
V.cell(len(vend)+3,1,'업체가 늘면 맨 아래 줄에 이어서 적습니다(40줄까지 장부의 고르기 목록과 수수료 계산에 저절로 들어갑니다). 수수료율은 2026년 10월 6일까지 사용자가 업체와 정한 값입니다.').font=f(c='666666',s=9)
# ---------- 장부
S=wb.create_sheet('장부',0)
S['A1']='낭만 인테리어 · 문의 장부'; S['A1'].font=f(True,NAVY,14)
S['A2']='쓰는 법: 흰 칸만 적습니다. 회색 칸(번호 · 수수료율 · 건당 · 받을 수수료 · 못 받은 돈)은 저절로 채워집니다. 수수료율이 건마다 다르면 회색 칸 위에 그대로 적어도 됩니다. 5번 줄은 예시이니 첫 문의를 적을 때 덮어쓰세요.'
S['A2'].font=f(c='666666',s=9); S.merge_cells('A2:T2'); S['A2'].alignment=Alignment(wrap_text=True,vertical='top'); S.row_dimensions[2].height=30
H=['번호','문의 온 날','손님','지역','품목','손님이 본 글','문의 경로','넘긴 업체','넘긴 날','상태','계약 금액(원)','수수료율','건당(원)','받을 수수료(원)','받은 금액(원)','받은 날','못 받은 돈(원)','시공한 날','확인 연락','메모']
HR=4; F0=5; N=300; LAST=F0+N-1
auto={1,12,13,14,17}
for c,h in enumerate(H,1):
    x=S.cell(HR,c,h); x.font=f(True,'FFFFFF'); x.fill=PatternFill('solid',fgColor=NAVY); x.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True); x.border=BD
S.row_dimensions[HR].height=32
for r in range(F0,LAST+1):
    S.cell(r,1,f'=IF(B{r}="","",ROW()-{HR})')
    S.cell(r,12,f'=IF(H{r}="","",IFERROR(IF(INDEX(업체!$E$2:$E$41,MATCH(H{r},업체!$B$2:$B$41,0))="","",INDEX(업체!$E$2:$E$41,MATCH(H{r},업체!$B$2:$B$41,0))),""))')
    S.cell(r,13,f'=IF(H{r}="","",IFERROR(IF(INDEX(업체!$F$2:$F$41,MATCH(H{r},업체!$B$2:$B$41,0))="","",INDEX(업체!$F$2:$F$41,MATCH(H{r},업체!$B$2:$B$41,0))),""))')
    S.cell(r,14,f'=IF(J{r}="안 됨","",IF(AND(M{r}<>"",OR(J{r}="계약",J{r}="시공 끝")),M{r},IF(AND(K{r}<>"",L{r}<>""),ROUND(K{r}*L{r},0),"")))')
    S.cell(r,17,f'=IF(N{r}="","",N{r}-IF(O{r}="",0,O{r}))')
    for c in range(1,len(H)+1):
        x=S.cell(r,c); x.font=f(); x.border=BD; x.alignment=Alignment(vertical='center',horizontal='center' if c in(1,2,5,7,9,10,12,16,18,19) else None)
        if c in auto: x.fill=PatternFill('solid',fgColor=GREY)
        if c in(2,9,16,18): x.number_format='yyyy-mm-dd'
        if c in(11,13,14,15,17): x.number_format='#,##0'
        if c==12: x.number_format='0%'
# 예시 줄
import datetime as dt
ex={2:dt.date(2026,10,5),3:'(예시) 김○○ 님',4:'경기 고양',5:'방묘문',6:'방묘문, 높이보다 빠져나갈 자리를 봅니다',7:'비밀댓글',8:'펫게이트',9:dt.date(2026,10,5),10:'견적 중',20:'예시 줄입니다 · 덮어쓰세요'}
for c,v in ex.items(): S.cell(F0,c,v)
for c in range(1,len(H)+1):
    if c not in auto: S.cell(F0,c).fill=PatternFill('solid',fgColor=YEL)
for c,w in zip(range(1,21),[6,12,14,14,10,38,11,18,12,10,14,9,10,15,14,12,14,12,10,34]): S.column_dimensions[CL(c)].width=w
S.freeze_panes=S.cell(F0,4)
def dv(formula,col,allow_other=True):
    d=DataValidation(type='list',formula1=formula,allow_blank=True); d.showErrorMessage=not allow_other; S.add_data_validation(d); d.add(f'{col}{F0}:{col}{LAST}')
dv('"중문,샷시,필름,코킹,문 수리,방묘문,입주 청소,그 밖"','E')
dv('"비밀댓글,전화,문자,톡톡,쪽지,그 밖"','G')
dv('업체!$B$2:$B$41','H')
dv('"문의,넘김,견적 중,계약,시공 끝,안 됨"','J',False)
dv('"했음,아직"','S')
S.auto_filter.ref=f'A{HR}:T{LAST}'
# ---------- 요약
Q=wb.create_sheet('요약')
Q['A1']='요약 (장부에서 저절로 셉니다)'; Q['A1'].font=f(True,NAVY,14)
rows=[('문의',f'=COUNTA(장부!$B${F0}:$B${LAST})'),('업체에 넘긴 것',f'=COUNTA(장부!$I${F0}:$I${LAST})'),
      ('계약',f'=COUNTIFS(장부!$J${F0}:$J${LAST},"계약")+COUNTIFS(장부!$J${F0}:$J${LAST},"시공 끝")'),
      ('계약 금액 합(원)',f'=SUMIFS(장부!$K${F0}:$K${LAST},장부!$J${F0}:$J${LAST},"계약")+SUMIFS(장부!$K${F0}:$K${LAST},장부!$J${F0}:$J${LAST},"시공 끝")'),
      ('받을 수수료 합(원)',f'=SUM(장부!$N${F0}:$N${LAST})'),('받은 금액 합(원)',f'=SUM(장부!$O${F0}:$O${LAST})'),('못 받은 돈(원)',f'=SUM(장부!$Q${F0}:$Q${LAST})'),
      ('시공 끝났는데 확인 연락을 아직 안 한 건',f'=COUNTIFS(장부!$J${F0}:$J${LAST},"시공 끝",장부!$S${F0}:$S${LAST},"<>했음")')]
for i,(k,v) in enumerate(rows,3):
    a=Q.cell(i,1,k); b=Q.cell(i,2,v); a.font=f(True); b.font=f(); a.border=BD; b.border=BD; b.number_format='#,##0'; a.fill=PatternFill('solid',fgColor=GREY)
r0=13
for c,h in enumerate(['품목','문의','계약','받을 수수료(원)','받은 금액(원)'],1):
    x=Q.cell(r0,c,h); x.font=f(True,'FFFFFF'); x.fill=PatternFill('solid',fgColor=NAVY); x.alignment=Alignment(horizontal='center'); x.border=BD
for i,p in enumerate(['중문','샷시','필름','코킹','문 수리','방묘문','입주 청소','그 밖'],r0+1):
    Q.cell(i,1,p); E=f'장부!$E${F0}:$E${LAST}'; J=f'장부!$J${F0}:$J${LAST}'
    Q.cell(i,2,f'=COUNTIFS({E},$A{i})'); Q.cell(i,3,f'=COUNTIFS({E},$A{i},{J},"계약")+COUNTIFS({E},$A{i},{J},"시공 끝")')
    Q.cell(i,4,f'=SUMIFS(장부!$N${F0}:$N${LAST},{E},$A{i})'); Q.cell(i,5,f'=SUMIFS(장부!$O${F0}:$O${LAST},{E},$A{i})')
    for c in range(1,6): x=Q.cell(i,c); x.font=f(); x.border=BD; x.number_format='#,##0'
Q.cell(r0+10,1,'5번 예시 줄을 지우기 전에는 문의 1 · 방묘문 1로 세어집니다.').font=f(c='666666',s=9)
Q.column_dimensions['A'].width=40
for c in 'BCDE': Q.column_dimensions[c].width=18
wb.save('/mnt/user-data/outputs/int/nangman_interior_문의장부.xlsx')

import sys; sys.path.insert(0,'.')
from dosa_uikit import *
P=lambda t:f'<p style="font-size:19px;line-height:1.9;color:#222;">{t}</p>\n'
H=lambda t:f'<p style="font-size:26px;font-weight:700;color:#5C1B2A;padding-top:26px;">{t}</p>\n'
h='<html><body style="width:693px;margin:30px auto;font-family:\'Noto Sans KR\',sans-serif;">'
h+=H('FIGS 숫자 줄')+FIGS([('작은 이름','큰 글자','설명 한 줄'),('작은 이름','큰 글자','설명 한 줄'),('작은 이름','큰 글자','설명 한 줄')])
h+=H('MYEONGSIK 명식 판')+MYEONGSIK([('시주','○','십성','○','십성 · 12운성'),('일주','○','일간','○','십성 · 12운성'),('월주','○','십성','○','십성 · 12운성'),('연주','○','십성','○','십성 · 12운성')])
h+=H('PAIRS 용어와 뜻')+PAIRS([('용어','뜻을 일상어로 한두 문장'),('용어','뜻을 일상어로 한두 문장'),('용어','뜻을 일상어로 한두 문장')])
h+=H('LIST 번호 줄')+LIST([('1','굵은 글자','설명 한두 문장'),('2','굵은 글자','설명 한두 문장'),('3','굵은 글자','설명 한두 문장')])
h+=H('VS 나란히 비교')+VS([('가','작은 글자'),('나','작은 글자'),('다','작은 글자')],[('항목','값 값 값'.split()),('항목','값 값 값'.split()),('항목','값 값 값'.split())],1)
h+=H('OX 두 갈래')+OX(['해당하는 것 하나','해당하는 것 둘','해당하는 것 셋'],['아닌 것 하나','아닌 것 둘'])
h+=H('FLOW 흐름 띠')+FLOW([('1대운','몇 살~몇 살'),('2대운','몇 살~몇 살'),('3대운','몇 살~몇 살'),('4대운','몇 살~몇 살')])
h+=H('BARS 가는 막대')+BARS([('이름',5,'설명',True),('이름',3,'설명',False),('이름',2,'설명',False),('이름',1,'설명',False)],5,'개')
h+=H('VERDICT 판정 줄')+VERDICT([('해당','ok','굵은 글자','설명 한두 문장'),('조건부','cond','굵은 글자','설명 한두 문장'),('해당 없음','no','굵은 글자','설명 한두 문장')])
h+=CAPTION('부품 아래 회색 설명 한 줄')
h+='</body></html>'
open('sample.html','w',encoding='utf8').write(h)
import re
print('가장 작은 글자', min(int(x) for x in re.findall(r'font-size:(\d+)px',h) if int(x)>1), '빈 단락', h.count('<br></p>'))

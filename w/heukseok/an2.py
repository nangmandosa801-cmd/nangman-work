exec(open('an.py').read().split("print('=====')")[0].replace('print(','(lambda *a,**k:None)('))
B=all_[(all_.ym>=202604)&(all_.ym<=202609)]
for n in ['흑석리버파크자이','흑석한강센트레빌','흑석한강센트레빌Ⅱ','흑석한강푸르지오','아크로리버하임','흑석동양아파트','롯데캐슬에듀포레','청호','우리유앤미']:
    z=B[(B.단지명==n)].sort_values(['A','ym'])
    print(n, z[['A','a','p','ym','층','y']].values.tolist())
# 자이 all deals
z=all_[all_.단지명=='흑석리버파크자이'].sort_values('ym'); print(z[['A','p','ym','y']].values.tolist())

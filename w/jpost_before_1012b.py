# -*- coding: utf-8 -*-
# 지산드림 글 빌더: exec(open('/home/claude/jisan/jpost.py').read()) 뒤 build(...)
exec(open('/home/claude/jisan/gpim2_head.py').read().split("A('<p style=\"font-size:17px;color:#1B7A9E")[0])
import re, os
JU='https://blog.naver.com/jisandream01/'
def C(t): return (t,'center')
def R(*cells):
    return [c if isinstance(c,tuple) or (isinstance(c,str) and i==0) else C(c) for i,c in enumerate(cells)]
JL={
 'galmae5':('224416320137','갈매역 도보 5분 | 같은 84㎡인데 7.16억과 8.30억입니다','갈매 아파트 값이 역에서 어떻게 달라지나'),
 'byeolnae_star':('224396406790','별내자이 더 스타 이그제큐티브 | 호텔처럼 지었는데 규제는 없습니다','별내 상층부 사례입니다'),
 'guri_reg':('224404038799','구리 규제지역 지정 | 토지거래허가까지 삼중으로 묶였습니다','구리가 규제지역이 된 뒤입니다'),
 'factory_road':('224413312449','공장 창고 시세는 도로가 정합니다 | 8m 넘으면 1,357만원, 못 미치면 808만원','일반 공장 값은 도로가 정합니다'),
 'galmae_byeolnae':('224416293920','갈매동 별내동 아파트 시세 | 5년 전엔 같았는데 지금은 갈매가 덜 빠졌습니다','갈매와 별내 아파트 비교입니다'),
 'guri_land':('224394305872','구리 토지 투자 | 땅에도 종류가 넷 있습니다','용도지역을 먼저 보는 이유입니다'),
 'guri3m':('224427376695','구리 아파트 매매, 규제 뒤 한 달 415건이 79건으로 줄었고 옆 별내는 141건으로 늘었습니다','구리 규제 뒤 거래가 어디로 갔는지입니다'),
 'igok':('224427523105','가평 토지 매물, 북면 이곡리 임야 2만 평 7억, 6m 임도와 계곡이 붙은 임업용 땅입니다','가평 임야 매물입니다'),
 'igok105':(None,'가평 산 매매, 북면 이곡리 임야 13,679평 5억 4,700만원, 4.5ha라 임업인 3ha 면적 기준을 넘습니다','이곡리 산 105 · 105-1 매물입니다'),
 'dongtan_dandok_buji':('224436620846','동탄 단독주택 부지 가격, 5억 5천만원에 장지동은 75평이 팔렸고 같은 돈으로 새솔동은 113평이 팔렸습니다','같은 5억원대로 동탄 장지동과 새솔동에서 산 넓이를 비교한 글입니다'),
 'bojeonsanji':('224436607342','보전산지 확인, 가평 이곡리 산 104는 임업용산지이고 관리사 부지는 200㎡ 쉼터 부지는 100㎡ 미만입니다','임업용산지에 지을 수 있는 시설을 적은 글입니다'),
 'igok104':('224428776358','가평 토지, 북면 이곡리 임야 6,390평 2억 5,500만원, 6m 임도 붙은 산 104 한 필지입니다','이곡리 산 104 매물입니다'),
 'samhoe':('224427398219','가평 토지 매물, 청평 삼회리 임야 2,962평 2억 4천, 포장도로 붙은 계곡 앞입니다','청평 임야 매물입니다'),
 'choi':('224427504153','하남 토지, 초이동 그린벨트 밭도 도로 붙으면 평당 478만원이고 도로 없으면 170만원입니다','초이동 그린벨트 땅값과 도로'),
 'byeolnae_apt':(None,'별내 아파트 시세, 84㎡ 6억 9천으로 1년에 2.4% 올랐고 고점보다 14% 아래인데 별내자이더스타는 11억 3천입니다','별내 아파트 단지별 시세입니다'),
 'dasan_apt':(None,'다산 아파트 시세, 84㎡ 9억 2천으로 1년에 11% 올라 2021년 고점을 넘었고 힐스테이트다산은 10억 2,750만원입니다','다산 아파트 단지별 시세입니다'),
 'gambuk':('224431027068','하남 토지 매매, 감북동 그린벨트 밭은 평당 290만원이고 마을 안 집터는 1,120만원인데 팔린 땅 열에 일곱은 지분입니다','감북동 땅 종류별 평당 값입니다'),
 'homyeong':('224431148666','가평 토지 매물, 청평 호명리 임야 3만 7천 평 14억 8,500만원, 자연녹지에 포장도로와 계곡이 붙었고 감정가보다 1억 낮습니다','청평 호명리 자연녹지 산 3만 7천 평 매물입니다'),
 'hub':('224430896080','갈매동 부동산 매물, 10월에 지산드림이 내놓은 토지·오피스텔·지식산업센터·창고 열두 건입니다','지산드림이 지금 내놓은 매물 전체입니다'),
 'guri8':('224430991660','구리역 아파트 시세, 8호선 2년에 수택동은 1년 20% 올라 리버시티 84㎡ 12억이고 갈매는 5.6%입니다','구리 8호선 역별 아파트 시세입니다'),
 'topyeong2':(None,'토평2지구, 2만 2천 가구 지구지정은 됐는데 보상은 2027년 착공은 2029년이고 장자호수공원역 앞 84㎡는 11억 2천입니다','토평2지구 진행 단계입니다'),
 'sutaek_e':(None,'수택e구역 입주권, 3,022가구 착공했고 84㎡ 분양가 13억 5천인데 7월부터 조합원 지위 양도가 막혔습니다','수택E구역 재개발 현황입니다'),
 'onam_seohee':('224431540773','오남역 서희스타힐스 분양가, 84㎡ 6억 7천~7억 2천은 올해 오남에서 가장 비싸게 팔린 4억 8,400만원보다 1억 8천 넘게 높고 10월 6일 무순위 12가구를 받습니다','남양주 오남읍 무순위 공고와 분양가입니다'),
 'nm_tbi':('https://blog.naver.com/dong_jin_kim/224427576499','토지보상 이의신청, 30일보다 먼저 볼 건 이의유보입니다','보상금에 동의하지 않을 때 밟는 순서입니다'),
 'nm_jjc':('https://blog.naver.com/dong_jin_kim/224423322072','줍줍 청약 조건, 2025년 6월 10일부터 1주택자는 못 넣습니다','무순위 청약에 넣을 수 있는 사람입니다'),
 'gyosan_nm':('https://blog.naver.com/dong_jin_kim/224381460159','하남 교산신도시, 분양권은 언제부터인지 미사 4,133건으로 봤습니다','미사지구 보상 뒤 분양까지 걸린 시간입니다'),
 'galmae_apt':('224431018252','갈매 아파트 시세, 84㎡ 7억 5천으로 고점보다 7% 아래이고 갈매역아이파크는 8억 5,800만 전세 5억 8천입니다','갈매 아파트 단지별 매매·전세입니다'),
 'guri_jeonse':('224430078837','구리 아파트 전세, 2억대는 인창 주공 59㎡ 3억대는 주공1·대림한숲 4억대는 84㎡ 구축 6억대는 구리역·토평 신축입니다','구리 전세를 금액대별로 나눴습니다'),
 'sanchon_shimteo':('224434536931','산촌체류형쉼터 조건, 가평은 여섯 읍·면이 모두 산촌이고 내 산 400㎡ 이상에 33㎡까지 지을 수 있습니다','가평 임야에 짓는 쉼터 조건입니다'),
 'imeopin':('224435746917','임업인 조건, 3ha 산을 샀다고 끝이 아니고 관리사와 주택은 조건이 하나 더 붙습니다','임업인이 되는 조건과 산에 지을 수 있는 것'),
 'op_tuja':('224435753387','오피스텔 투자, 값은 7년 전보다 내렸는데 월세는 25% 올랐고 1억 원룸은 연 8%가 나옵니다','오피스텔은 월세로 돌려받는 물건입니다'),
 'byeolnae_op':(None,'별내 오피스텔 월세, 22㎡ 원룸은 500에 55만 66㎡ 투룸은 5천에 170만이고 올해 입주한 이그제큐티브 59㎡는 7,500에 175만입니다','별내 오피스텔 월세·전세·매매 실거래입니다'),
 'nyj_op':('224430674453','남양주 오피스텔 월세, 다산 원룸은 500에 65만 별내 원룸은 55만이고 투룸은 다산 130만 별내 170만입니다','남양주 오피스텔 동별·단지별 월세입니다'),
 'nyj_land':(None,'남양주 토지 매매, 1억 이하로 팔린 땅은 1,136건인데 100평 넘는 것은 171건이고 그중 104건이 임야입니다','남양주 1억 이하 땅이 실제로 어떤 땅인지입니다'),
 'gp_ipji':('224431283823','가평 부동산, 제2경춘국도가 착공하고 접경지역이 됐는데 땅 거래는 2021년의 3분의 1입니다','가평 입지와 새 도로, 거래 흐름입니다'),
 'gp_ttang':('224431287951','가평 땅값, 같은 밭도 계획관리지역은 평당 52만원 농림지역은 28만원이고 청평은 79만원 북면은 33만원입니다','가평 땅값을 땅 종류·용도지역·도로·넓이별로 나눈 글입니다'),
 'jisan199':(None,'지식산업센터 매매, 경기 199개 건물이 고점보다 7% 내렸는데 별내는 33% 하남 덕풍은 21%이고 성남 상대원만 올랐습니다','경기 전체 지식산업센터 비교입니다'),
 'galmae_jisan':('224430654385','갈매 지식산업센터 시세, 올해 27건 평당 1,319만원이고 사는 사람 열에 일곱이 개인입니다','갈매 지식산업센터 건물별 시세입니다'),
 'byeolnae_jisan':(None,'별내 지식산업센터 시세, 고점 평당 1,579만원이 1,036만원으로 34% 내렸고 2021년 건물은 39%입니다','별내 지식산업센터 건물별 시세입니다'),
 'misa_jisan':(None,'미사 지식산업센터 시세, 같은 미사대로인데 2019년 건물은 33% 2021년 건물은 38% 내렸고 조정대로 2011년 건물은 2%입니다','미사 지식산업센터 건물별 시세입니다'),
 'seongnam_jisan':(None,'성남 지식산업센터 시세, 경기에서 유일하게 고점보다 올랐고 상대원 2019년 건물은 16% 2003년 건물은 35%입니다','성남 지식산업센터 건물별 시세입니다'),
 'anyang_jisan':(None,'안양 지식산업센터 시세, 고점 평당 1,891만원이 1,592만원이고 호계동 2018년 건물은 46% 내렸습니다','안양 지식산업센터 건물별 시세입니다'),
 'jisan_vat':('224437440039','지식산업센터 매매 부가세, 건물분에만 10%가 붙어 가산 매물은 매매가의 5.1% 영등포 자이타워는 2.9%입니다','지식산업센터를 살 때 붙는 부가세와 환급입니다'),
}
def JLK(k):
    n,t,dsc=JL[k]
    if n is None: return '<p style="font-size:19px;font-weight:700;color:#0D3B5C;">「%s」<br><span style="font-size:15px;color:#7A8590;">%s · 발행 예정</span></p>'%(t,dsc)
    u=n if n.startswith('http') else JU+n
    return LK(u,t,dsc)
def JA(k):
    n,t,dsc=JL[k]
    if n is None: return '「%s」'%t
    u=n if n.startswith('http') else JU+n
    return '「<a href="%s" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">%s</a>」'%(u,t)

def build(slug,kick,title,lead,summ,body,src,links,tags):
    A('<p style="font-size:17px;color:#1B7A9E;letter-spacing:1px;">지산드림 · %s</p>'%kick); A(BR)
    A('<p style="font-size:34px;font-weight:700;color:#0D3B5C;">%s</p>'%title); A(BR)
    for t in lead: A(P(t)); A(BR)
    A(BR); A(DIV); A(BR)
    # 「30초 요약」 상자는 2026.10.3부터 넣지 않음 (사용자 지시). summ 값은 받아도 쓰지 않음
    for b in body:
        if b=='---': A(BR); A(DIV); A(BR)
        elif b=='': A(BR)
        else: A(b); A(BR)
    A(DIV); A(BR)
    A(H('같이 보면 좋은 글')); A(BR)
    for k in links: A(JLK(k)); A(BR)
    A(BR); A(CAP('자료: '+src)); A(BR)
    A('<p style="font-size:14px;color:#9AA4AE;">지산드림공인중개사사무소 · 대표 김미호 · 등록번호 41310-2022-00061 · 경기도 구리시 갈매동 540-5, 101호</p>'); A(BR)
    A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:2px solid #1B7A9E;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>'); A(BR)
    A('<p style="font-size:19px;font-weight:700;color:#0D3B5C;text-align:center;">지산드림</p>')
    A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;"><tr>')
    A('<td width="100%" style="border-left:3px solid #0D3B5C;background-color:#F4F6F8;padding:22px 24px;">')
    A('<p style="font-size:15px;color:#1B7A9E;letter-spacing:1px;">JISANDREAM</p>'); A(BR)
    A('<p style="font-size:21px;font-weight:700;color:#0D3B5C;">구리 갈매동에서 지식산업센터·창고·아파트·토지를 다룹니다</p>'); A(BR)
    A('<p style="font-size:17px;color:#333;">현장을 직접 보고 확인한 것만 씁니다.</p>')
    A('<p style="font-size:17px;color:#333;">되팔 때 걸릴 것까지 미리 말씀드립니다.</p>'); A(BR)
    A('<p style="height:1px;background-color:#DDD8CE;margin:6px 0 14px 0;"></p>')
    A('<p style="font-size:17px;font-weight:700;"><a href="https://blog.naver.com/jisandream01/224387498556" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">구리 갈매동 공인중개사 | 지산드림 지식산업센터 전문</a><br>')
    A('<span style="font-size:15px;color:#7A8590;">구리와 남양주, 하남에서 다루는 물건들입니다</span></p>')
    A('</td></tr></table>'); A(BR)
    A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
    A('<tr><td style="border-left:3px solid #1B7A9E;background-color:#F4F6F8;padding:16px 18px;">')
    A('<span style="font-size:15px;color:#8A8578;">태그</span><br>')
    A('<span style="font-size:17px;color:#555;line-height:1.9;">%s</span>'%' '.join('#'+t for t in tags))
    A('</td></tr></table>')
    x='\n'.join(A_)+'\n'
    os.makedirs('/mnt/user-data/outputs/jisandream',exist_ok=True)
    open('/mnt/user-data/outputs/jisandream/jisandream_%s_post.html'%slug,'w',encoding='utf-8').write(x)
    t=re.sub(r'<[^>]+>',' ',x)
    print(slug,'본문',len(re.sub(r'\s','',t)),'금지',re.findall(r'\S*(?:갈[라랐렸리림]|자리|고요|프리미엄|%p|어요|예요|헷갈|제자리|최고)\S*',t))
    try:
        import sys as _s; _s.path.insert(0,'/home/claude/blogkit'); import seo; seo.check(x,slug='jisandream_'+slug)   # SEO 자동완성 점검 — 글을 만들 때마다 (10/5 사용자: 무조건 반영)
    except Exception as e: print('   SEO 점검 못 함:',e)

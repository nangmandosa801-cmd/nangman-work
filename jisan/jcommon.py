# -*- coding: utf-8 -*-
# 지산드림 11/15 일주일치 공통: jpost + 상자 · 사진 표시 · 새 링크
exec(open('/home/claude/jisan/jpost.py').read())
JL['chungung']=('224472082786','하남 토지, 춘궁동 그린벨트 밭 평당 171만원','춘궁동 땅값입니다')
JL['maedo']=('224472086670','토지 매도 방법, 하남 땅 내놓을 때 필요한 것 3가지','하남 땅 내놓으실 분 안내입니다')
JL['saneunbeop']=('224472090324','하남 땅 사는법, 거래 10건 중 7건은 지분','하남 땅 사기 전 보는 순서입니다')
JL['gasan105']=('224404050862','하우스디 가산 퍼스타 상가 임대, 맞은편 건물엔 상가가 없습니다','가산 1층 105호 매물입니다')
JL['gasan_wolse']=('224441960588','가산동 상가 월세, 1층 11평을 사면 3억 7,500만원이고 빌리면 보증금 3천에 월 200만원입니다','가산동 상가 층별 가격입니다')
def BOX(title,items,tail):
    return ('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;"><tr><td width="100%" style="border-left:3px solid #0D3B5C;background-color:#F4F6F8;padding:22px 24px;">'
            '<p style="font-size:21px;font-weight:700;color:#0D3B5C;">'+title+'</p><p><br></p>'
            +''.join('<p style="font-size:19px;color:#333;">▸ '+x+'</p>' for x in items)
            +'<p><br></p><p style="font-size:19px;color:#333;">'+tail+'</p></td></tr></table>')
def PH(fn,cap): return '<p style="font-size:18px;font-weight:700;color:#C0392B;">▼ 사진 '+fn+' — '+cap+'</p>'

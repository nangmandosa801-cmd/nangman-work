import sys,re
src,out,danji,bundle,recruit=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]=='1',sys.argv[5]=='1'
s=open(src).read()
A='<a style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;" href='
def a(url,t): return f'「<a href="{url}" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a>」'
if bundle and '224451151010' not in s:
    m=re.search(r'<p style="font-size:18px;color:#8A8578;">자료:',s)
    add=f'<p style="font-size:21px;color:#333;">{danji} 열쇠를 받으면 입주청소와 새집증후군을 다른 팀에 따로 맡기지 않아도 됩니다. 34평(84㎡)을 하루 차이로 이어서 묶으면 <b style="color:#1F3864;">71만 4천원</b>입니다. 순서와 견적서에서 볼 줄은 {a("https://blog.naver.com/champion_chart/224451151010","입주청소 새집증후군, 묶어서 맡기면 이틀 연달아 잡고 받은 견적보다 낮춥니다")}에 있습니다.</p>\n<p><br></p>\n'
    s=s[:m.start()]+add+s[m.start():]
if recruit and '224449575744' not in s:
    H='<p style="font-size:27px;font-weight:700;color:#1F3864;">함께 보면 좋은 글</p>'
    box=f'''<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:5px solid #2E5C8A;background-color:#F4F6F9;padding:20px 22px;"><p style="font-size:21px;font-weight:700;color:#2E5C8A;">{danji} 앞 중개사무소 인터뷰를 받습니다</p>
<p><br></p>
<p style="font-size:20px;color:#333;line-height:1.7;">입주장 전세 분위기, 잔금 날 손님들이 묻는 것 같은 현장 이야기를 들려주시면 블로그에 무료로 소개합니다. 원고는 올리기 전에 먼저 보여 드립니다.</p>
<p style="font-size:20px;color:#333;line-height:1.7;">▸ 신청: 글 맨 위 · 맨 끝 안내 그림의 번호로 문자 주세요 (사무소 이름 · 편한 요일)</p>
<p style="font-size:19px;font-weight:700;"><a href="https://blog.naver.com/dong_jin_kim/224449575744" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">부동산 홍보방법, 입주 단지 중개사무소를 찾아가 인터뷰하고 그 단지 글마다 사무소를 무료로 소개합니다 ›</a></p>
</td></tr></table>
<p><br></p>
'''
    assert H in s
    s=s.replace(H,box+H,1)
open(out,'w').write(s)
print(src.split('/')[-1],'bundle' ,'224451151010' in s,'recruit','224449575744' in s)

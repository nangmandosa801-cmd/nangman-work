import requests,re,time,os,sys
from bs4 import BeautifulSoup
L=[('dong_jin_kim','224390827296','nm_topyeong2'),('jisandream01','224390842248','js_topyeong2_0829'),('jisandream01','224427376695','js_guri3m'),('jisandream01','224430991660','js_guri8'),('jisandream01','224401877287','js_rail'),('jisandream01','224430896080','js_hub'),('jisandream01','224404038799','js_guri_reg'),('jisandream01','224394305872','js_guri_land'),('jisandream01','224430078837','js_guri_jeonse'),('jisandream01','224413663884','js_sutaek_e'),('jisandream01','224390792285','js_guri_traffic'),('jisandream01','224388858539','js_guri_cmp')]
for b,n,s in L:
    if os.path.exists(s+'.txt'): continue
    r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
    so=BeautifulSoup(r.text,'html.parser')
    c=so.select_one('.se-main-container'); tt=so.select_one('.se-title-text'); out=[]
    if tt: out.append('TITLE: '+tt.get_text(' ',strip=True))
    if c:
        for el in c.select('.se-component'):
            cls=' '.join(el.get('class',[]))
            if 'se-image' in cls: out.append('[사진]')
            elif 'se-oglink' in cls or 'se-sticker' in cls: pass
            elif 'se-table' in cls:
                for tr in el.select('tr'): out.append(' | '.join(td.get_text(' ',strip=True) for td in tr.select('td')))
            else:
                t=el.get_text('\n',strip=True).replace('​','')
                if t.strip(): out.append(t)
    open(s+'.txt','w').write('\n'.join(out)); print(s,len('\n'.join(out)),r.status_code); time.sleep(1.2)

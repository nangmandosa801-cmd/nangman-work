import sys,pickle,time,datetime,email.utils,re
sys.argv=['x']
exec(open('scan.py').read().split("for slug in sys.argv[1:]:")[0])
REG2=['강남','서초','관악','동작','구로','금천','안양','군포','의왕','광명','남양주','구리','다산','평택','오산','부천','수원 영통','인천 연수','송도','인천 남동','부산','창원','청주']
per=['수도 동파 해빙','동파 해빙','배관 해빙','보일러 동파']
QS=[r+' '+p for r in REG2 for p in per]
R={}
for i in range(0,len(QS),4):
    with ThreadPoolExecutor(4) as ex: R.update(dict(zip(QS[i:i+4],ex.map(ranks,QS[i:i+4]))))
    time.sleep(1.3)
agg={}
for q,d in R.items():
    for b,r in d.items(): agg.setdefault(b,{})[q]=r
B=[x for x in sorted(agg,key=lambda b:-len(agg[b])) if len(agg[x])>=2 or min(agg[x].values())<=3][:220]
INFO={}
import datetime as dt
def rss2(b):
    d=rss(b)
    return d
for i in range(0,len(B),10):
    with ThreadPoolExecutor(10) as ex: INFO.update(dict(zip(B[i:i+10],ex.map(rss2,B[i:i+10]))))
    time.sleep(0.2)
pickle.dump((R,agg,INFO),open('freeze2.pkl','wb'))
print('QS',len(QS),'blogs',len(agg),'rss',len(INFO))

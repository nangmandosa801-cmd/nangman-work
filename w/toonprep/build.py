import json,os,shutil,subprocess,sys
sys.path.insert(0,'/home/claude/helper'); from gas import call
import base64
from sel import S; from desc import D
from PIL import Image
BASE='블로그/협업/인테리어툰/재료/제작준비'; OUT='/home/claude/w/toonprep/out'; res={}
def put(path,f):
    return call('fput',path=path,name=os.path.basename(f),b64=base64.b64encode(open(f,'rb').read()).decode())['id']
only=sys.argv[1:]
for folder,(src,it,url,who,rule,items,note) in S.items():
    C=folder.split('_')[0]
    if only and C not in only: continue
    d=f'{OUT}/{folder}'; shutil.rmtree(d,ignore_errors=True); os.makedirs(d); rows=[]
    for k,(n,stage,short,desc) in enumerate(items,1):
        fn=f'{k:02d}_{stage}_{short.replace(" ","").replace("·","-")}.jpg'
        im=Image.open(f'/home/claude/w/toonprep/src/{src}/{n}.jpg').convert('RGB'); im.save(f'{d}/{fn}',quality=95)
        fid=put(f'{BASE}/{folder}',f'{d}/{fn}'); rows.append((fn,fid,stage,desc,n))
        if src.startswith('flowhc'):
            w,h=im.size; cf=fn.replace('.jpg','_crop.jpg'); im.crop((0,0,int(w*.87),int(h*.89))).save(f'{d}/{cf}',quality=95)
            rows.append((cf,put(f'{BASE}/{folder}',f'{d}/{cf}'),stage,desc+' (로고 자른 사본)',n))
    x=D[C]
    lst=[f'[사진목록] {it} · {C} · {folder}',f'같은 현장 여부: {note}','','파일명 | Drive 파일 주소 | 시공 단계 | 사진 설명 | 원문 사진 번호']
    lst+=[f'{a} | https://drive.google.com/file/d/{b}/view | {c} | {e} | 원문 {n}번' for a,b,c,e,n in rows]
    open(f'{d}/사진목록.txt','w').write('\n'.join(lst)+'\n')
    ds=[f'[현장 설명] {it} · {C} · {folder.split("_",1)[1].replace("_"," ")}','',f'고객 불편: {x["불편"]}',f'확인된 원인: {x["원인"]}',f'작업 순서: {x["순서"]}',f'꼼꼼하게 처리한 부분: {x["꼼꼼"]}',f'확인 필요 · 쓰지 말 것: {x["확인필요"]}','',
        f'출처: {who} 네이버 블로그 글 {url}',f'낭만 인테리어 SNS 사용: 가능(제휴 업체 제공 자료). 사용 조건: {rule}',
        '공통: 업체 상호 · 전화 · 가격은 만화에 넣지 않기(「제휴팀」으로). 사진 속 얼굴 · 동호수가 보이면 가리기. AI 사진이나 다른 집 사진으로 바꾸지 않기.']
    open(f'{d}/현장설명.txt','w').write('\n'.join(ds)+'\n')
    put(f'{BASE}/{folder}',f'{d}/사진목록.txt'); put(f'{BASE}/{folder}',f'{d}/현장설명.txt')
    fo=[z for z in call('ls',path=BASE) if z.get('dir') and z['name']==folder][0]['id']
    res[C]=dict(it=it,folder=folder,n=len(items),url=f'https://drive.google.com/drive/folders/{fo}')
    print(json.dumps(res[C],ensure_ascii=False),flush=True)
json.dump(res,open(f'{OUT}/_res_{"_".join(only) or "all"}.json','w'),ensure_ascii=False)

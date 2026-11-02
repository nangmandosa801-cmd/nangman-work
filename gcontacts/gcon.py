import json,sys,urllib.request,urllib.parse,os
D=os.path.dirname(os.path.abspath(__file__))
def tok():
    c=json.load(open(f'{D}/client.json'));t=json.load(open(f'{D}/token.json'))
    d=urllib.parse.urlencode(dict(client_id=c['client_id'],client_secret=c['client_secret'],refresh_token=t['refresh_token'],grant_type='refresh_token')).encode()
    return json.load(urllib.request.urlopen('https://oauth2.googleapis.com/token',d))['access_token']
A=tok()
def api(path,method='GET',body=None):
    r=urllib.request.Request('https://people.googleapis.com/v1/'+path,method=method,data=json.dumps(body).encode() if body else None,headers={'Authorization':'Bearer '+A,'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r))
def allc():
    out=[];pt=''
    while True:
        r=api('people/me/connections?personFields=names,phoneNumbers,biographies&pageSize=1000'+('&pageToken='+pt if pt else ''))
        out+=r.get('connections',[]);pt=r.get('nextPageToken')
        if not pt:return out
def digits(s):return ''.join(ch for ch in s if ch.isdigit())
def find(num):
    n=digits(num)[-8:]
    return [p for p in allc() if any(digits(x.get('value',''))[-8:]==n for x in p.get('phoneNumbers',[]))]
def rename(num,name,memo=None):
    ps=find(num)
    if not ps:
        b={'names':[{'givenName':name}],'phoneNumbers':[{'value':num}]}
        if memo:b['biographies']=[{'value':memo}]
        api('people:createContact?personFields=names','POST',b);return 'created'
    p=ps[0];b={'etag':p['etag'],'names':[{'givenName':name}]};f='names'
    if memo:b['biographies']=[{'value':memo}];f+=',biographies'
    api(f"{p['resourceName']}:updateContact?updatePersonFields={f}",'PATCH',b)
    return 'renamed from '+(p.get('names',[{}])[0].get('displayName','(없음)'))
if __name__=='__main__':
    if sys.argv[1]=='list':
        for p in allc():
            nm=p.get('names',[{}])[0].get('displayName','');ph=','.join(x.get('value','') for x in p.get('phoneNumbers',[]))
            if len(sys.argv)<3 or sys.argv[2] in nm+ph: print(nm,'|',ph)
    elif sys.argv[1]=='rename': print(rename(*sys.argv[2:]))

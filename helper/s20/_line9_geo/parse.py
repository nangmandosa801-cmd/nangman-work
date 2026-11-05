import xml.etree.ElementTree as ET, json, glob, math
nodes={}; ways={}
for f in sorted(glob.glob('map*.osm')):
    root=ET.parse(f).getroot()
    for n in root.iter('node'):
        nodes[n.get('id')]=(float(n.get('lat')),float(n.get('lon')),{t.get('k'):t.get('v') for t in n.findall('tag')})
    for w in root.iter('way'):
        tags={t.get('k'):t.get('v') for t in w.findall('tag')}
        ways[w.get('id')]=([nd.get('ref') for nd in w.findall('nd')],tags)
print(len(nodes),len(ways))
def center(refs):
    pts=[nodes[r][:2] for r in refs if r in nodes]
    return (sum(p[0] for p in pts)/len(pts),sum(p[1] for p in pts)/len(pts)) if pts else None
res={'residential':{},'station':{},'school':{},'roads':{}}
for wid,(refs,t) in ways.items():
    nm=t.get('name')
    if t.get('landuse')=='residential' and nm: res['residential'][nm]=center(refs)
    if t.get('amenity')=='school' and nm: res['school'][nm]=center(refs)
    if t.get('highway') and nm: res['roads'].setdefault(nm,[]).append(refs)
    if t.get('railway')=='station' and nm: res['station'][nm]=center(refs)
for nid,(la,lo,t) in nodes.items():
    if t.get('railway')=='station' and t.get('name'): res['station'][t['name']]=(la,lo)
    if t.get('amenity')=='school' and t.get('name'): res['school'][t['name']]=(la,lo)
print('stations',res['station'])
print('schools',[k for k in res['school']])
print('residential',len(res['residential']))
for k,v in sorted(res['residential'].items()): print(' ',k,round(v[0],5),round(v[1],5))
print('roads',sorted(res['roads'].keys()))
# intersections of 미사강변대로 with other named roads
def inter(a,b):
    sa=set(r for refs in res['roads'].get(a,[]) for r in refs); sb=set(r for refs in res['roads'].get(b,[]) for r in refs)
    return [nodes[r][:2] for r in sa&sb]
for rd in res['roads']:
    if rd!='미사강변대로':
        x=inter('미사강변대로',rd)
        if x: print('X 미사강변대로 ×',rd,[(round(a,5),round(b,5)) for a,b in x][:4])
json.dump({k:(v if k!='roads' else None) for k,v in res.items()},open('feat.json','w'),ensure_ascii=False)

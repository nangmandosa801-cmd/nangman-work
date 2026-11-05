import xml.etree.ElementTree as ET, glob, json
nodes={}; ways={}
for f in sorted(glob.glob('/home/claude/helper/s20/_line9_geo/map*.osm')):
    root=ET.parse(f).getroot()
    for n in root.iter('node'): nodes[n.get('id')]=(float(n.get('lat')),float(n.get('lon')))
    for w in root.iter('way'): ways[w.get('id')]=([nd.get('ref') for nd in w.findall('nd')],{t.get('k'):t.get('v') for t in w.findall('tag')})
def pts(refs): return [nodes[r] for r in refs if r in nodes]
G={'res':{},'roads':[],'major':[],'sub5':[],'l9c':[],'river':[],'water':[]}
for wid,(refs,t) in ways.items():
    p=pts(refs)
    if len(p)<2: continue
    if t.get('landuse')=='residential' and t.get('name'): G['res'][t['name']]=p
    h=t.get('highway')
    if h in ('motorway','trunk','primary','secondary'): G['major'].append((t.get('name') or '',p))
    elif h in ('tertiary','residential','unclassified','motorway_link','trunk_link','primary_link','secondary_link'): G['roads'].append(p)
    if t.get('railway')=='subway' and t.get('name') in ('하남선','5호선'): G['sub5'].append(p)
    if t.get('railway')=='construction' and t.get('name')=='9호선': G['l9c'].append(p)
    if wid=='284168601': G['river']=p
    if t.get('natural')=='water' and t.get('water') in ('lake','pond') and len(refs)>30: G['water'].append(p)
print({k:len(v) for k,v in G.items()})
json.dump(G,open('/home/claude/helper/s20/hanam_line9_map/geo.json','w'),ensure_ascii=False)

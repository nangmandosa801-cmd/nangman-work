import json,sys
d=json.load(open(sys.argv[1]))
print('const H='+json.dumps(d['H'],ensure_ascii=False)+';const T='+json.dumps(d['T'],ensure_ascii=False)+""";const ti=document.querySelector('input[aria-label="제목"]');ti.focus();Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(ti,T);ti.dispatchEvent(new Event('input',{bubbles:true}));ti.dispatchEvent(new Event('change',{bubbles:true}));const cm=document.querySelector('.CodeMirror');if(cm)cm.CodeMirror.setValue(H);[ti.value.length,cm?cm.CodeMirror.getValue().length:-1]""")

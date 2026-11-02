import glob,subprocess,sys,re,json
out={}
for p in sorted(glob.glob('img/2244*/*.png')):
    t=subprocess.run(['tesseract',p,'-','-l','kor+eng','--psm','6'],capture_output=True,text=True).stdout
    out[p]=t
    if re.search(r'7678|9967|010[- ]?\d{4}|010',t): print('PHONE',p,re.findall(r'010[- ]?\d{3,4}[- ]?\d{4}|7678|9967',t))
json.dump(out,open('ocr.json','w'),ensure_ascii=False)
print(len(out))

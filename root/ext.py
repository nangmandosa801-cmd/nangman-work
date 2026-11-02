import zipfile, os, sys
z=zipfile.ZipFile('/mnt/user-data/uploads/Downloads/이사짐.zip')
root='/home/claude/짐/'
n=0
for i in z.infolist():
    nm=i.filename
    if not (i.flag_bits & 0x800):
        try: nm=nm.encode('cp437').decode('utf-8')
        except Exception:
            try: nm=nm.encode('cp437').decode('cp949')
            except Exception: pass
    p=os.path.join(root,nm)
    if i.is_dir():
        os.makedirs(p,exist_ok=True); continue
    os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'wb').write(z.read(i)); n+=1
print('풀린 파일',n)

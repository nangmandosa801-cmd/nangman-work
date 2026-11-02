import subprocess
def assemble(files,durs,out,xf=0.4):
    cmd=['ffmpeg','-y','-loglevel','error']
    for f,dur in zip(files,durs): cmd+=['-framerate','30','-loop','1','-t',str(dur+xf),'-i',f]
    fl=[]
    for i,dur in enumerate(durs):
        n=int((dur+xf)*30)
        fl.append(f"[{i}:v]scale=1188:2112,zoompan=z='min(zoom+0.0006,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
    prev='v0'; off=0
    for i in range(1,len(durs)):
        off+=durs[i-1]
        fl.append(f"[{prev}][v{i}]xfade=transition=fade:duration={xf}:offset={off:.2f}[x{i}]"); prev=f'x{i}'
    cmd+=['-filter_complex',';'.join(fl),'-map',f'[{prev}]','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',out]
    subprocess.run(cmd,check=True)

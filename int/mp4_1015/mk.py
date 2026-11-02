# 10/15 18:16 사용자 「mp4 사진과 메시지 중심으로 블로그 내에 올릴껄로 만들어줘」
import subprocess,sys,glob,os
sys.path.insert(0,'/home/claude'); import bgm
def make(slides,out,per=3.4,last=4.5,fade=0.5,seed=7):
    n=len(slides); durs=[per]*(n-1)+[last]
    total=sum(durs)-fade*(n-1)
    wav=out.replace('.mp4','_bgm.wav'); bgm.make(wav,total+0.5,seed)
    args=['ffmpeg','-y','-loglevel','error']
    for s,d in zip(slides,durs): args+=['-i',s]
    args+=['-i',wav]
    fc=[]
    for i,d in enumerate(durs):
        fr=int(d*30)
        fc.append(f"[{i}:v]scale=2112:1188,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1920x1080:fps=30,setsar=1,format=yuv420p[v{i}]")
    prev='v0'; off=0
    for i in range(1,n):
        off+=durs[i-1]-fade
        fc.append(f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={off:.2f}[x{i}]"); prev=f'x{i}'
    fc.append(f"[{n}:a]afade=t=out:st={total-1.2:.2f}:d=1.2,volume=0.55[a]")
    args+=['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-profile:v','main','-level','4.0','-bf','0','-g','30','-color_range','tv','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',out]
    subprocess.run(args,check=True); os.remove(wav)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','1','-i',out,'-frames:v','1',out.replace('.mp4','_cover.jpg')],check=True)
import land
O='/mnt/user-data/outputs/int/mp4_1015/'



if __name__=='__main__' and len(sys.argv)>3:
    make(land.build(sys.argv[1],sys.argv[2]),sys.argv[3],seed=int(sys.argv[4]) if len(sys.argv)>4 else 7); print('ok')

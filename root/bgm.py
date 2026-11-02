# 저작권 걱정 없는 배경음악 — 직접 합성(샘플 · 외부 음원 없음)
# make(path, dur, seed) → 밝은 우쿨렐레풍 반주 + 글로켄 멜로디 + 가벼운 드럼 wav
import numpy as np, wave
SR=44100
NOTE={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def hz(m): return 440*2**((m-69)/12)
def pluck(f,dur,bright=0.5,rng=None):
    n=int(SR*dur); p=max(2,int(SR/f)); buf=(rng.random(p)*2-1)
    out=np.zeros(n)
    for i in range(n):
        out[i]=buf[i%p]; buf[i%p]=0.996*(bright*buf[i%p]+(1-bright)*buf[(i+1)%p]) if False else 0.996*0.5*(buf[i%p]+buf[(i+1)%p])
    return out
def ks(f,dur,rng):
    # 빠른 Karplus-Strong(벡터)
    n=int(SR*dur); p=max(2,int(round(SR/f)))
    reps=n//p+2; out=np.empty(reps*p); buf=rng.random(p)*2-1
    for r in range(reps):
        out[r*p:(r+1)*p]=buf
        buf=0.994*0.5*(buf+np.roll(buf,-1))
    return out[:n]
def bell(f,dur):
    t=np.arange(int(SR*dur))/SR
    return (np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*f*2.76*t)+0.15*np.sin(2*np.pi*f*5.4*t))*np.exp(-t*4.5)
def kick(dur=0.25):
    t=np.arange(int(SR*dur))/SR; f=55+90*np.exp(-t*30)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*12)
def noise(dur,dec,rng,hp=True):
    x=rng.random(int(SR*dur))*2-1
    if hp: x=x-np.convolve(x,np.ones(8)/8,'same')
    return x*np.exp(-np.arange(len(x))/SR*dec)
def add(buf,x,at,g):
    i=int(at*SR); j=min(len(buf),i+len(x))
    if i<len(buf): buf[i:j]+=g*x[:j-i]
# 코드 진행(밝은 장조) — 근음 반음 수 · 장/단
PROGS=[[(0,'M'),(7,'M'),(9,'m'),(5,'M')],[(0,'M'),(5,'M'),(7,'M'),(5,'M')],[(0,'M'),(9,'m'),(5,'M'),(7,'M')],[(5,'M'),(7,'M'),(0,'M'),(0,'M')]]
def chord(root,q,base):
    third=4 if q=='M' else 3
    return [base+root, base+root+third, base+root+7, base+root+12]
def make(path,dur,seed=0,bpm=None,key=None):
    rng=np.random.default_rng(seed)
    bpm=bpm or [112,118,104,124][seed%4]; key=key if key is not None else [0,2,5,7][seed%4]
    beat=60/bpm; prog=PROGS[seed%4]
    L=np.zeros(int(SR*(dur+2))); R=np.zeros_like(L)
    scale=[0,2,4,7,9,12,14,16]   # 장조 펜타토닉
    t=0; bar=0
    mel_rng=np.random.default_rng(seed+99)
    while t<dur:
        root,q=prog[bar%4]; notes=chord(root,q,60+key-12)
        # 우쿨렐레 스트럼: 쿵 · 짝 · 쿵짝짝
        for k,(off,g) in enumerate([(0,1),(1,.6),(1.5,.7),(2,.9),(3,.6),(3.5,.7)]):
            at=t+off*beat
            for s,m in enumerate(notes):
                x=ks(hz(m),beat*1.6,rng); add(L,x,at+s*0.012,0.13*g); add(R,x,at+s*0.014,0.11*g)
        # 베이스
        for off in (0,2):
            x=ks(hz(36+key+root),beat*1.8,rng); x=np.convolve(x,np.ones(30)/30,'same')
            add(L,x,t+off*beat,0.5); add(R,x,t+off*beat,0.5)
        # 드럼
        for b in range(4):
            if b in (0,2): add(L,kick(),t+b*beat,0.55); add(R,kick(),t+b*beat,0.55)
            if b in (1,3): s=noise(0.18,22,rng); add(L,s,t+b*beat,0.16); add(R,s,t+b*beat,0.16)
            for h in (0,.5):
                x=noise(0.05,80,rng); add(L,x,t+(b+h)*beat,0.05); add(R,x,t+(b+h)*beat,0.07)
        # 멜로디(두 마디부터) — 화음 음을 중심으로 통통 튀게
        if bar>=1:
            pat=[0,1,1.5,2,3] if bar%2 else [0,.5,1,2,2.5,3.5]
            for off in pat:
                deg=mel_rng.choice(scale); m=72+key+deg+ (root if mel_rng.random()<.5 else 0)
                m=72+key+min(scale,key=lambda d:abs((72+key+d)-m))
                x=bell(hz(m),beat*1.5); add(L,x,t+off*beat,0.10); add(R,x,t+off*beat,0.13)
        t+=4*beat; bar+=1
    n=int(SR*dur); L=L[:n]; R=R[:n]
    env=np.ones(n); fi=int(SR*0.4); fo=int(SR*1.5); env[:fi]=np.linspace(0,1,fi); env[-fo:]=np.linspace(1,0,fo)
    st=np.stack([L*env,R*env],1); st=np.tanh(st*1.2); st=st/np.max(np.abs(st))*0.6
    with wave.open(path,'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
    return path

# synthesizes the promo soundtrack (120 BPM electro), timed to promo.html scenes. Run: uv run --with numpy python promo/gen_audio.py
import numpy as np, pathlib, subprocess
SR=44100; DUR=54; beat=.5; bar=4*beat
t=np.arange(int(SR*DUR))/SR
drums=np.zeros_like(t); music=np.zeros_like(t); fx=np.zeros_like(t)
rng=np.random.default_rng(7)
f=lambda n:440*2**((n-69)/12)
def add(bus,sig,at):
    i=int(at*SR); j=min(len(bus),i+len(sig))
    if j>i: bus[i:j]+=sig[:j-i]
X=lambda d:np.arange(int(d*SR))/SR
def saw(fr,d,h=12): x=X(d); return sum(np.sin(2*np.pi*fr*k*x)/k for k in range(1,h+1))
def noise(d): return rng.standard_normal(int(d*SR))
hp=lambda s:np.diff(s,prepend=0)
GROOVE=lambda at:(5<=at<28) or (34<=at<52)          # full drums
BREAK=lambda at:28<=at<34                            # breakdown: no kick
prog=[57,53,48,55]                                   # Am F C G, one bar each
# drums
for s in range(int(DUR/beat*4)):                     # 16th grid
    at=s*beat/4; q=s%16
    if GROOVE(at):
        if q%4==0:
            x=X(.35); add(drums,1.0*np.sin(2*np.pi*(45*x+ (110/25)*(1-np.exp(-x*25))))*np.exp(-x*7),at)  # kick
        if q in (4,12):
            x=X(.25); add(drums,.5*hp(noise(.25))*np.exp(-x*18)+.2*np.sin(2*np.pi*190*x)*np.exp(-x*25),at)  # clap/snare
        if q%4==2: x=X(.18); add(drums,.22*hp(hp(noise(.18)))*np.exp(-x*16),at)   # open hat
        else: x=X(.04); add(drums,(.12 if q%2 else .07)*hp(hp(noise(.04)))*np.exp(-x*90),at)  # closed hat
    elif BREAK(at) and q%2==0:
        x=X(.04); add(drums,.06*hp(hp(noise(.04)))*np.exp(-x*90),at)
# snare roll builds into drops
for start,end in ((3,5),(32,34),(46,48)):
    at=start
    while at<end:
        p=(at-start)/(end-start); x=X(.12)
        add(drums,(.15+.35*p)*hp(noise(.12))*np.exp(-x*30),at); at+=beat/(2 if p<.5 else 4 if p<.8 else 8)
# music: sidechained pad + offbeat saw bass + arp
for k in range(int(DUR/bar)+1):
    r=prog[k%4]; at0=k*bar
    ch=[r,r+3 if r in (57,) else r+4,r+7] if r!=57 else [57,60,64]
    x=X(bar); pad=sum(saw(f(m),bar,6)+saw(f(m)*1.006,bar,6) for m in ch)*np.minimum(1,x/.05)*np.minimum(1,(bar-x)/.05)
    add(music,.035*pad,at0)
    for e in range(8):
        at=at0+e*beat/2
        if at<3: continue
        x=X(.22); b=saw(f(r-24),.22,10)*np.exp(-x*9)                      # bass, 8ths w/ accent on offbeat
        add(music,(.16 if e%2 else .10)*b,at)
    for e in range(16):
        at=at0+e*beat/4
        if not GROOVE(at): continue
        m=ch[[0,1,2,1][e%4]]+12+(12 if e%8>=4 else 0); x=X(.15)
        add(music,.05*np.sign(np.sin(2*np.pi*f(m)*x))*np.exp(-x*22),at)
# sidechain pump on music during kick sections
duck=1-.75*np.exp(-(t%beat)/.09); music*=np.where(((t>=5)&(t<28))|((t>=34)&(t<52)),duck,1)
# intro/breakdown filter feel: thin out music
music[(t<5)]*=np.linspace(.3,1,np.sum(t<5)); music[(t>=28)&(t<34)]*=.6
# risers and impacts
for at,d in ((1.5,3.5),(31,3),(45,3)):
    x=X(d); add(fx,.25*np.convolve(noise(d),np.ones(8)/8,'same')*(x/d)**2.5,at)
    add(fx,.12*np.sin(2*np.pi*(200+1800*(x/d)**2)*x)*(x/d)**2,at)
for at in (5,19,34,48):
    x=X(2.5); add(fx,.9*np.sin(2*np.pi*(40*x+ (80/6)*(1-np.exp(-x*6))))*np.exp(-x*2.5)+.35*hp(noise(2.5))*np.exp(-x*2.2),at)  # boom + crash
for sc in (10,28,40):
    x=X(.6); add(fx,.25*np.convolve(noise(.6),np.ones(20)/20,'same')*(x/.6)**3,sc-.6)
def blip(at,m,a=.18): x=X(.12); add(fx,a*np.sin(2*np.pi*f(m)*x)*np.exp(-x*30),at)
for s,ln in ((41.0,16),(44.2,10)):
    for c in range(ln): x=X(.012); add(fx,.35*noise(.012)*np.exp(-x*400),s+c/14)
for at in (42.4,42.9,43.4,45.4): blip(at,88)
for i,at in enumerate((34.3,34.6,34.9,35.2,35.5)): blip(at,79+i*2)
for i,at in enumerate((11.0,12.2,13.4,14.6)): blip(at,76+[0,3,7,12][i],.14)
# outro: stop groove at 52, let tail ring
mix=drums+music+fx
mix*=np.minimum(1,np.minimum(t/.3,(DUR-t)/1.5))
mix=np.tanh(mix*1.6); mix/=np.abs(mix).max()/.95
here=pathlib.Path(__file__).parent; pcm=(mix*32767).astype(np.int16).tobytes()
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","-","-b:a","128k",str(here/"soundtrack.mp3")],input=pcm,check=True)
print(here/"soundtrack.mp3")

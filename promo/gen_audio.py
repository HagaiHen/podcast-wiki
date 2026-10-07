# synthesizes the promo soundtrack, timed to promo.html scenes. Run: uv run --with numpy python promo/gen_audio.py
import numpy as np, wave, pathlib
SR=44100; DUR=54; BPM=100; beat=60/BPM
t=np.arange(int(SR*DUR))/SR; mix=np.zeros_like(t)
f=lambda n:440*2**((n-69)/12)
def add(sig,at):
    i=int(at*SR); j=min(len(mix),i+len(sig))
    if j>i: mix[i:j]+=sig[:j-i]
def env(n,a=.01,r=.3):
    x=np.arange(n)/SR; return np.minimum(1,x/a)*np.exp(-x/r)
# chords: Am F C G, 2 bars each
prog=[[57,60,64],[53,57,60],[48,55,64],[55,59,62]]; bar=4*beat
for k in range(int(DUR/bar)+1):
    ch=prog[k%4]; n=int(bar*SR); x=np.arange(n)/SR
    pad=sum(np.sin(2*np.pi*f(m)*x)+.3*np.sin(2*np.pi*f(m)*1.003*x) for m in ch)
    add(.05*pad*np.minimum(1,x/.4)*np.minimum(1,(bar-x)/.4),k*bar)
    add(.18*np.sin(2*np.pi*f(ch[0]-12)*x)*np.minimum(1,(bar-x)/.1)*np.minimum(1,x/.02),k*bar)  # bass
    for s in range(8):  # pluck arpeggio, from scene 2
        at=k*bar+s*beat/2
        if at<5: continue
        m=ch[s%3]+12+(12 if s in (3,7) else 0); n2=int(.4*SR); x2=np.arange(n2)/SR
        add(.07*np.sign(np.sin(2*np.pi*f(m)*x2))*env(n2,.003,.09),at)
rng=np.random.default_rng(1)
b=0
while b*beat<DUR:  # drums from 10s
    at=b*beat
    if at>=10 and at<52:
        n=int(.25*SR); x=np.arange(n)/SR
        add(.45*np.sin(2*np.pi*(50+90*np.exp(-x*30))*x)*np.exp(-x*12),at)  # kick
        add(.05*rng.standard_normal(int(.05*SR))*env(int(.05*SR),.001,.015),at+beat/2)  # hat
    b+=1
for sc in (5,10,19,28,34,40,48):  # whoosh into each scene
    n=int(1.0*SR); x=np.arange(n)/SR; nz=np.convolve(rng.standard_normal(n),np.ones(30)/30,'same')
    add(.35*nz*(x/1.0)**3*np.where(x<.95,1,(1-x)/.05),sc-.95)
def blip(at,m,a=.12):
    n=int(.12*SR); x=np.arange(n)/SR; add(a*np.sin(2*np.pi*f(m)*x)*env(n,.002,.04),at)
for i,(s,ln) in enumerate(((41.0,16),(44.2,10))):  # typing clicks, 14 chars/s
    for c in range(ln): add(.25*rng.standard_normal(int(.01*SR))*env(int(.01*SR),.0005,.003),s+c/14)
for at in (42.4,42.9,43.4,45.4): blip(at,84)  # terminal checkmarks
for i,at in enumerate((34.3,34.6,34.9,35.2,35.5)): blip(at,76+i*2)  # stat counters
for i,at in enumerate((11.0,12.2,13.4,14.6)): blip(at,72+[0,3,7,12][i],.09)  # step cards
mix*=np.minimum(1,np.minimum(t/1.5,(DUR-t)/3))  # fade in/out
mix=np.tanh(mix*1.2); mix/=np.abs(mix).max()/.9
out=pathlib.Path(__file__).parent/"soundtrack.wav"
with wave.open(str(out),"wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes())
print(out)

# synthesizes the promo soundtrack (96 BPM swung funk/hip-hop in G), timed to promo.html scenes.
# Run: uv run --with numpy python promo/gen_audio.py
import numpy as np, pathlib, subprocess
SR=44100; DUR=54; BPM=96; beat=60/BPM; bar=4*beat; SW=.58   # SW: swing ratio for 16ths
t=np.arange(int(SR*DUR))/SR
drums,keys,bass,fx=(np.zeros_like(t) for _ in range(4))
rng=np.random.default_rng(3)
f=lambda n:440*2**((n-69)/12)
X=lambda d:np.arange(int(d*SR))/SR
noise=lambda d:rng.standard_normal(int(d*SR))
hp=lambda s:np.diff(s,prepend=0)
def add(bus,sig,at):
    i=int(at*SR); j=min(len(bus),i+len(sig))
    if j>i: bus[i:j]+=sig[:j-i]
def pos(b,q):  # time of 16th q in bar b, swung
    return b*bar+(q//2)*beat/2+(q%2)*beat/2*SW
ON=lambda at:(5<=at<28) or (34.3<=at<52)           # full groove
BRK=lambda at:28<=at<34.3                           # breakdown
def kick(at,a=1.):
    x=X(.4); add(drums,a*np.sin(2*np.pi*(48*x+(120/22)*(1-np.exp(-x*22))))*np.exp(-x*8)+a*.15*noise(.4)*np.exp(-x*200),at)
def snare(at,a=.55):
    x=X(.3); add(drums,a*(.8*hp(noise(.3))*np.exp(-x*14)+.5*np.sin(2*np.pi*185*x)*np.exp(-x*30)),at)
def hat(at,a,d=.05):
    x=X(d); add(drums,a*hp(hp(noise(d)))*np.exp(-x*(4/d)),at)
def epiano(m,d,a):   # FM electric piano
    x=X(d); fr=f(m); return a*np.sin(2*np.pi*fr*x+1.8*np.exp(-x*3)*np.sin(2*np.pi*fr*x))*np.exp(-x*1.4)*np.minimum(1,(d-x)/.05)
chords=[[55,59,62,66],[52,55,59,62],[48,52,55,59],[50,54,57,60]]   # Gmaj7 Em7 Cmaj7 D7
roots=[43,40,36,38]
KICKS=[0,7,10]; GHOST=[6,11,14]
for b in range(int(DUR/bar)+1):
    ch=chords[b%4]; r=roots[b%4]
    for q in range(16):
        at=pos(b,q)
        if ON(at):
            if q in KICKS or (b%2 and q==13): kick(at,1. if q==0 else .8)
            if q in (4,12): snare(at)
            if q in GHOST: snare(at,.08)
            hat(at,.13 if q%2==0 else .06,.12 if q==14 else .05)
        elif BRK(at) and q%2==0: hat(at,.05)
    # keys: stabs on 1, "and of 2", 4-and (swung)
    for q,d in ((0,.9),(6,.35),(13,.6)):
        at=pos(b,q)
        if at<1: continue
        for m in ch: add(keys,epiano(m,d,.09 if at>=5 else .06),at)
    # bass: syncopated root/octave/fifth line with a pickup
    if 5<=pos(b,0)<52 and not BRK(pos(b,0)):
        for q,o,d in ((0,0,.35),(3,0,.15),(7,12,.15),(8,7,.3),(10,0,.15),(14,10,.15),(15,12,.12)):
            x=X(d); fr=f(r+o); add(bass,.32*(np.sin(2*np.pi*fr*x)+.35*np.sin(4*np.pi*fr*x)+.12*np.sin(6*np.pi*fr*x))*np.minimum(1,x/.004)*np.exp(-x*5)*np.minimum(1,(d-x)/.02),pos(b,q))
# breakdown: sustained keys bed
for b in range(int(28/bar),int(34.3/bar)+1):
    for m in chords[b%4]: add(keys,epiano(m+12,bar,.05),b*bar)
# brass stabs on drops: detuned saws, fast attack, short
def brass(at,a=.16,root=55):
    x=X(.45); s=0
    for m in (root,root+4,root+7,root+12):
        for dt in (1,1.008):
            s=s+sum(np.sin(2*np.pi*f(m)*dt*k*x)/k for k in range(1,9))
    add(fx,a*s*np.minimum(1,x/.015)*np.exp(-x*5),at)
for at in (5,19,34.3,48): brass(at); brass(at+beat*1.5,.12,57 if at!=48 else 55)
# drum fills into drops + risers
for s,e in ((3.1,5),(32.4,34.3),(46.1,48)):
    at=s
    while at<e:
        p=(at-s)/(e-s); snare(at,.12+.4*p); at+=beat/(2 if p<.5 else 4)
for at,d in ((2,3),(31.3,3),(45,3)):
    x=X(d); add(fx,.18*np.convolve(noise(d),np.ones(10)/10,'same')*(x/d)**3,at)
for at in (5,34.3,48):
    x=X(2); add(fx,.5*hp(noise(2))*np.exp(-x*2.5),at); kick(at,1.1)       # crash + kick hit
for sc in (10,19,28,40):
    x=X(.5); add(fx,.2*np.convolve(noise(.5),np.ones(20)/20,'same')*(x/.5)**3,sc-.5)
def blip(at,m,a=.16): x=X(.15); add(fx,a*np.sin(2*np.pi*f(m)*x)*np.exp(-x*25),at)
for s,ln in ((41.0,16),(44.2,10)):
    for c in range(ln): x=X(.012); add(fx,.3*noise(.012)*np.exp(-x*400),s+c/14)
for at in (42.4,42.9,43.4,45.4): blip(at,86)
for i,at in enumerate((34.6,34.9,35.2,35.5,35.8)): blip(at,79+[0,2,4,7,12][i])
for i,at in enumerate((11.0,12.2,13.4,14.6)): blip(at,74+[0,4,7,12][i],.12)
# light sidechain on keys+bass
duck=1-.35*np.exp(-(t%beat)/.08); music=(keys+bass)*np.where(((t>=5)&(t<28))|((t>=34.3)&(t<52)),duck,1)
mix=drums+music+fx
mix*=np.minimum(1,np.minimum(t/.2,(DUR-t)/2))
mix=np.tanh(mix*1.5); mix/=np.abs(mix).max()/.95
here=pathlib.Path(__file__).parent; pcm=(mix*32767).astype(np.int16).tobytes()
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","-","-b:a","128k",str(here/"soundtrack.mp3")],input=pcm,check=True)
print(here/"soundtrack.mp3")

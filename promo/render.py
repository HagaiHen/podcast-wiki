# renders a promo page deterministically: seek(t) per frame -> PNG -> ffmpeg, soundtrack looped to length.
# Run: uv run --with playwright python promo/render.py [out.mp4] [page.html]
import subprocess, sys, pathlib
from playwright.sync_api import sync_playwright
here=pathlib.Path(__file__).parent; FPS=30; out=sys.argv[1] if len(sys.argv)>1 else str(here/"podcast-wiki-promo.mp4"); page=pathlib.Path(sys.argv[2]).resolve() if len(sys.argv)>2 else here/"promo.html"
with sync_playwright() as p:
    b=p.chromium.launch(channel="chrome"); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto(page.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
    w,h=pg.evaluate("[window.W||1920,window.H||1080]"); pg.set_viewport_size({"width":w,"height":h})  # the vertical demo is 1080x1920
    dur=pg.evaluate("DUR")
    ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-i","-","-stream_loop","-1","-i",str(here/"soundtrack.mp3"),"-af",f"afade=t=out:st={dur-2:.2f}:d=2","-c:a","aac","-b:a","160k","-shortest","-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-movflags","+faststart",out],stdin=subprocess.PIPE)
    for i in range(int(dur*FPS)):
        pg.evaluate(f"seek({i/FPS})"); ff.stdin.write(pg.screenshot(type="png"))
        if i%150==0: print(f"{i/FPS:.0f}s/{dur}s",flush=True)
    ff.stdin.close(); ff.wait(); b.close()

# renders social.html to social-preview.png (1280x640). Run: uv run --with playwright python promo/render_social.py
import pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome"); pg = b.new_page(viewport={"width": 1280, "height": 640})
    pg.goto((here / "social.html").as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
    pg.locator("#card").screenshot(path=str(here / "social-preview.png")); b.close()

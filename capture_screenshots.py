import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

PAGES_TO_CAPTURE = [
    ("master_portal", "http://127.0.0.1:5500/index.html", 1440, 900, False),
    ("home_page", "http://127.0.0.1:5500/home.html", 1440, 900, True),
    ("characters_page", "http://127.0.0.1:5500/characters.html", 1440, 900, True),
    ("elements_page", "http://127.0.0.1:5500/elements.html", 1440, 900, True),
    ("series_page", "http://127.0.0.1:5500/series.html", 1440, 900, True),
    ("contact_page", "http://127.0.0.1:5500/contact.html", 1440, 900, True),
    ("form_detail", "http://127.0.0.1:5500/contact.html#cadet-enlistment", 1440, 900, False),
]

def main():
    print("Capturing high-resolution screenshots for academic report...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
        page = context.new_page()

        for name, url, w, h, full_page in PAGES_TO_CAPTURE:
            print(f"  Navigating to {url}...")
            page.goto(url, wait_until="networkidle")
            time.sleep(0.5)
            out_file = SCREENSHOTS_DIR / f"{name}.png"
            if full_page:
                page.screenshot(path=str(out_file), full_page=True)
            else:
                page.screenshot(path=str(out_file))
            print(f"  [SAVED] {out_file.name} ({out_file.stat().st_size:,} bytes)")

        browser.close()
    print("All screenshots captured successfully!")

if __name__ == "__main__":
    main()

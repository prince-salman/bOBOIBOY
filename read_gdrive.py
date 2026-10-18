import time
from pathlib import Path
from playwright.sync_api import sync_playwright

url = "https://drive.google.com/drive/folders/1gdSSCNHHvDxnJOJvZTHuND17UoKkEkkN?usp=sharing"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(url, wait_until="networkidle")
    time.sleep(3)
    print("Page title:", page.title())
    
    # Take screenshot of what Google Drive is displaying
    page.screenshot(path="gdrive_view.png")
    
    # Extract visible elements
    names = page.evaluate("""() => {
        const results = [];
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let node;
        while (node = walker.nextNode()) {
            const val = node.nodeValue.trim();
            if (val.length > 2 && val.length < 150) {
                results.push(val);
            }
        }
        return Array.from(new Set(results));
    }""")
    
    print("\n--- Extracted Text Elements ---")
    for n in names[:50]:
        print("  -", n)
    browser.close()

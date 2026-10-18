import time
import json
from playwright.sync_api import sync_playwright

url = "https://drive.google.com/drive/folders/1gdSSCNHHvDxnJOJvZTHuND17UoKkEkkN?usp=sharing"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(url, wait_until="networkidle")
    time.sleep(2)
    
    files = page.evaluate("""() => {
        const rows = document.querySelectorAll('[data-id]');
        const list = [];
        for (const r of rows) {
            const id = r.getAttribute('data-id');
            const text = r.innerText;
            if (id && text) {
                list.push({id: id, text: text.split('\\n')[0]});
            }
        }
        return list;
    }""")
    print("Files found with data-id:")
    print(json.dumps(files, indent=2))
    
    # Try finding items by clicking or downloading
    browser.close()

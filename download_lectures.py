import os
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LECTURES_DIR = BASE_DIR / "lecture_materials"
LECTURES_DIR.mkdir(exist_ok=True)

FILES = [
    ("01_The_Web_and_HTML.pptx", "1ZwX5pa83uQkGD1MEocm8A2j4qNA8Io-Z"),
    ("02_HTML_Media_and_Table.pptx", "1tseALhAIRjArUrNq_qpFuB38kw2qELsJ"),
    ("03_HTML_Form_and_Frame.pptx", "1lyMQqHhaaCXp41TQVX_Bu29RxyV8vC5A"),
    ("04_CSS_Fundamentals.pptx", "1Vs0KpOc3Pi5CTIfKXAsQvOeNoMmLdjd6"),
    ("05_CSS_Advanced_Properties.docx", "1WfUgzqrVa7F8KYmyo6cMPlQ6qouRGWN4"),
    ("06_CSS_Responsive_Web_Design.pptx", "16_xtnjKAgSiCssS4xFw_E0Fz__S09OOD"),
]

def download_file(name, file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    session = requests.Session()
    response = session.get(url, stream=True)
    
    # Check for confirmation token if large file
    for k, v in response.cookies.items():
        if k.startswith('download_warning'):
            url = f"https://drive.google.com/uc?export=download&confirm={v}&id={file_id}"
            response = session.get(url, stream=True)
            break
            
    out_path = LECTURES_DIR / name
    with open(out_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:
                f.write(chunk)
    print(f"Downloaded {name}: {out_path.stat().st_size:,} bytes")

for name, fid in FILES:
    try:
        download_file(name, fid)
    except Exception as e:
        print(f"Error downloading {name}: {e}")

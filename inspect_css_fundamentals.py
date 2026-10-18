import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

filepath = Path("lecture_materials/04_CSS_Fundamentals.pptx")
with zipfile.ZipFile(filepath, 'r') as z:
    slide_files = sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')],
                         key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    for sf in slide_files:
        slide_xml = z.read(sf)
        root = ET.fromstring(slide_xml)
        texts = [node.text for node in root.iter() if node.text and node.text.strip()]
        slide_num = sf.split('/')[-1].replace('.xml', '')
        clean = [t.strip() for t in texts if len(t.strip()) > 1]
        if clean:
            print(f"--- {slide_num} ---")
            print(" | ".join(clean[:10]))

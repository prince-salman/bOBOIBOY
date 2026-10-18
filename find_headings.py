import docx

doc = docx.Document("lecture_materials/05_CSS_Advanced_Properties.docx")
headings = []
for i, p in enumerate(doc.paragraphs):
    if p.style.name.startswith("Heading") or len(p.text.strip()) < 40 and p.text.strip().isupper():
        if p.text.strip():
            headings.append((i, p.text.strip()))

print("Found headings / titles:")
for idx, text in headings[:50]:
    print(f"[{idx}] {text}")

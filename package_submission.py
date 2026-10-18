import os
import shutil
import zipfile

src_dir = r"C:\Users\Salman\.gemini\antigravity\scratch\boboiboy-universe"
dest_dir = r"C:\Users\Salman\Downloads\boboiboy-universe"
downloads_dir = r"C:\Users\Salman\Downloads"
zip_path = os.path.join(downloads_dir, "Project_1_Web_Programming_Salman.zip")

print("1. Mirroring files to Downloads/boboiboy-universe...")
# Files and dirs to exclude from clean web distribution
exclude_names = {
    ".git", "__pycache__", "node_modules", "package.json", "package-lock.json"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

# Copy files
for item in os.listdir(src_dir):
    if item in exclude_names or item.endswith(".pyc"):
        continue
    s = os.path.join(src_dir, item)
    d = os.path.join(dest_dir, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

print(f"   [DONE] Mirror complete to: {dest_dir}")

print("2. Copying report documents to Downloads root...")
docx_files = [
    "Project_1_Web_Programming_Salman_Report.docx",
    "QUICK_DEFENSE_CHEATSHEET.docx",
]
for docx in docx_files:
    s = os.path.join(src_dir, docx)
    if os.path.exists(s):
        d = os.path.join(downloads_dir, docx)
        shutil.copy2(s, d)
        print(f"   [COPIED] {docx} -> {d} ({os.path.getsize(d):,} bytes)")

print("3. Building submission ZIP archive...")
# Build zip of the website folder
core_web_items = [
    "index.html", "home.html", "characters.html", "elements.html", "series.html",
    "contact.html", "frameset.html", "nav.html", "main.html",
    "css", "images", "docs", "README.md"
]

if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for item in core_web_items:
        item_path = os.path.join(src_dir, item)
        if not os.path.exists(item_path):
            continue
        if os.path.isdir(item_path):
            for root, dirs, files in os.walk(item_path):
                for f in files:
                    if f.endswith(".pyc") or "__pycache__" in root:
                        continue
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, src_dir)
                    zf.write(full_p, rel_p)
        else:
            zf.write(item_path, item)
            
    # Also add the docx report to root of zip if desired
    report_p = os.path.join(src_dir, "Project_1_Web_Programming_Salman_Report.docx")
    if os.path.exists(report_p):
        zf.write(report_p, "Project_1_Web_Programming_Salman_Report.docx")

print(f"   [DONE] Created ZIP: {zip_path} ({os.path.getsize(zip_path):,} bytes)")
print("Packaging complete!")

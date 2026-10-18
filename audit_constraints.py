import glob
import re
import os

html_files = sorted(glob.glob('*.html'))
print(f"Auditing {len(html_files)} HTML files...\n")

total_issues = 0

for path in html_files:
    filename = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    line_count = len(lines)
    print(f"--- {filename} ---")
    
    # 1. Line count check (<= 200)
    if line_count > 200:
        print(f"  [ERROR] Line count: {line_count} (Exceeds 200!)")
        total_issues += 1
    else:
        print(f"  [OK] Line count: {line_count} lines (<= 200)")

    # 2. Comments check
    comments = re.findall(r'<!--.*?-->', content, re.DOTALL)
    if comments:
        print(f"  [ERROR] Found {len(comments)} HTML comments: {comments[:3]}")
        total_issues += 1
    else:
        print(f"  [OK] HTML comments: 0")

    # 3. Emojis check
    emojis = re.findall(r'[\U00010000-\U0010ffff]', content)
    if emojis:
        print(f"  [ERROR] Found emojis: {set(emojis)}")
        total_issues += 1
    else:
        print(f"  [OK] Emojis: 0")

    # 4. Academic / University text check
    banned = [
        "Resident University",
        "Academic Project",
        "Study Program",
        "Informatics / Information System",
    ]
    found_banned = []
    for phrase in banned:
        if phrase.lower() in content.lower():
            found_banned.append(phrase)
    if found_banned:
        print(f"  [ERROR] Found banned phrases: {found_banned}")
        total_issues += 1
    else:
        print(f"  [OK] Academic phrases: 0")

print(f"\n==========================================")
print(f"AUDIT SUMMARY: {total_issues} issues found across all HTML files.")
print(f"==========================================")

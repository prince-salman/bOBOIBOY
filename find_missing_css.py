import glob
import re

classes = set()
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    for m in re.findall(r'class="([^"]+)"', html):
        for c in m.split():
            classes.add(c)

with open('css/style.css', 'r', encoding='utf-8') as fp:
    css = fp.read()

missing = [c for c in sorted(classes) if '.' + c not in css]
print(f"Total HTML classes: {len(classes)}")
print(f"Missing in CSS: {len(missing)}")
for c in missing:
    print(f"  .{c}")

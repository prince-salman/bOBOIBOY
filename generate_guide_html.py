from pathlib import Path
import html

md_text = Path("PANDUAN_PENJELASAN_CODE.md").read_text(encoding="utf-8")

# Simple converter
lines = md_text.split("\n")
html_parts = []
in_code = False
in_table = False

for line in lines:
    if line.startswith("```"):
        if in_code:
            html_parts.append("</code></pre>")
            in_code = False
        else:
            html_parts.append("<pre><code>")
            in_code = True
        continue
    if in_code:
        html_parts.append(html.escape(line))
        continue
    
    if line.startswith("# "):
        html_parts.append(f"<h1>{html.escape(line[2:])}</h1>")
    elif line.startswith("## "):
        html_parts.append(f"<h2>{html.escape(line[3:])}</h2>")
    elif line.startswith("### "):
        html_parts.append(f"<h3>{html.escape(line[4:])}</h3>")
    elif line.startswith("> "):
        html_parts.append(f"<blockquote>{html.escape(line[2:])}</blockquote>")
    elif line.startswith("|") and "---" in line:
        continue
    elif line.startswith("|"):
        cols = [c.strip() for c in line.strip("|").split("|")]
        if not in_table:
            html_parts.append("<table><thead><tr>" + "".join(f"<th>{html.escape(c)}</th>" for c in cols) + "</tr></thead><tbody>")
            in_table = True
        else:
            html_parts.append("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in cols) + "</tr>")
    else:
        if in_table:
            html_parts.append("</tbody></table>")
            in_table = False
        if line.strip():
            # bold & code replacements
            l = html.escape(line)
            # handle bold **text**
            import re
            l = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', l)
            l = re.sub(r'`(.*?)`', r'<code>\1</code>', l)
            html_parts.append(f"<p>{l}</p>")

if in_table:
    html_parts.append("</tbody></table>")

body_content = "\n".join(html_parts)

template = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panduan Penjelasan Code - Presentasi Web Programming</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      color: #1e293b;
      background-color: #f8fafc;
      margin: 0;
      padding: 2.5rem 1rem;
    }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
      background: #ffffff;
      padding: 3rem;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      border: 1px solid #e2e8f0;
    }}
    h1 {{ color: #ff5722; font-size: 2rem; border-bottom: 2px solid #ff5722; padding-bottom: 0.5rem; }}
    h2 {{ color: #0f172a; margin-top: 2rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.3rem; }}
    h3 {{ color: #334155; margin-top: 1.5rem; }}
    blockquote {{
      background: #eff6ff;
      border-left: 4px solid #2563eb;
      margin: 1rem 0;
      padding: 0.75rem 1.25rem;
      border-radius: 0 6px 6px 0;
      font-style: italic;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
    }}
    th, td {{
      padding: 0.75rem 1rem;
      border: 1px solid #cbd5e1;
      text-align: left;
    }}
    th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }}
    code {{
      background: #f1f5f9;
      color: #ea580c;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-family: Consolas, monospace;
      font-size: 0.9em;
    }}
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 1.25rem;
      border-radius: 8px;
      overflow-x: auto;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    .back-btn {{
      display: inline-block;
      margin-bottom: 1.5rem;
      background: #ff5722;
      color: #ffffff;
      padding: 0.5rem 1.2rem;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-btn">&larr; Buka Website BoBoiBoy</a>
    {body_content}
  </div>
</body>
</html>
"""

Path("PANDUAN_PENJELASAN_CODE.html").write_text(template, encoding="utf-8")
print("PANDUAN_PENJELASAN_CODE.html generated successfully!")

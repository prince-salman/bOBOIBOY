import os
import sys
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = Path(__file__).resolve().parent
HTML_OUT = BASE_DIR / "CODE_EXPLANATION_GUIDE.html"
DOCX_OUT = BASE_DIR / "CODE_EXPLANATION_GUIDE.docx"

# Color constants
COLOR_NAVY = RGBColor(15, 23, 42)      # #0f172a
COLOR_ORANGE = RGBColor(234, 88, 12)   # #ea580c
COLOR_SLATE = RGBColor(51, 65, 85)     # #334155
COLOR_MUTED = RGBColor(100, 116, 139)  # #64748b
COLOR_GREEN = RGBColor(22, 163, 74)    # #16a34a

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def add_callout(doc, question, answer, bg_hex="F8FAFC", border_hex="EA580C"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=160, bottom=160, left=200, right=200)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="36" w:space="0" w:color="{border_hex}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run_q_title = p.add_run("LECTURER QUESTION:\n")
    run_q_title.bold = True
    run_q_title.font.size = Pt(9.5)
    run_q_title.font.color.rgb = COLOR_ORANGE
    
    run_q = p.add_run(f'"{question}"\n\n')
    run_q.italic = True
    run_q.font.size = Pt(10)
    run_q.font.color.rgb = COLOR_NAVY
    
    run_a_title = p.add_run("RECOMMENDED STUDENT DEFENSE ANSWER:\n")
    run_a_title.bold = True
    run_a_title.font.size = Pt(9.5)
    run_a_title.font.color.rgb = COLOR_GREEN
    
    run_a = p.add_run(f'"{answer}"')
    run_a.font.size = Pt(10)
    run_a.font.color.rgb = COLOR_SLATE
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)

def style_table(table, col_widths, headers, data, alt_row_bg="F8FAFC"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], "0F172A")
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(255, 255, 255)
            run.font.name = "Segoe UI"
            
    for row_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        bg_color = alt_row_bg if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, cell_value in enumerate(row_data):
            row_cells[col_idx].text = str(cell_value)
            row_cells[col_idx].width = col_widths[col_idx]
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=140, right=140)
            p = row_cells[col_idx].paragraphs[0]
            for run in p.runs:
                run.font.size = Pt(9)
                run.font.name = "Segoe UI"
                run.font.color.rgb = COLOR_SLATE
                if col_idx == 0:
                    run.font.bold = True

def generate_docx():
    print("Generating CODE_EXPLANATION_GUIDE.docx...")
    doc = docx.Document()
    
    # Page setup (Letter, 1 inch margins)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    # Title & Subtitle
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    t_run = title_p.add_run("COMPREHENSIVE CODE DEFENSE & EXPLANATION GUIDE")
    t_run.bold = True
    t_run.font.size = Pt(18)
    t_run.font.color.rgb = COLOR_NAVY
    t_run.font.name = "Segoe UI"
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(14)
    s_run = sub_p.add_run("Web Programming Project 1 • BoBoiBoy Galactic Universe Portal\nInformatics / Information Systems — Resident University")
    s_run.font.size = Pt(10.5)
    s_run.font.color.rgb = COLOR_ORANGE
    s_run.font.name = "Segoe UI"
    
    # Purpose note
    intro_p = doc.add_paragraph()
    intro_p.paragraph_format.space_after = Pt(12)
    intro_run = intro_p.add_run(
        "This guide is prepared to equip students with direct, concise, and academically sound explanations for every technical aspect of the project code during lecturer defense, code reviews, and practical examinations. All answers are delivered in 100% English adhering to Resident University's academic presentation standards."
    )
    intro_run.font.size = Pt(10)
    intro_run.font.color.rgb = COLOR_SLATE
    intro_run.font.name = "Segoe UI"
    
    # Section 1
    h1 = doc.add_heading("1. Master Frame Architecture (index.html)", level=1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    
    add_callout(
        doc,
        question="How is the architecture of this website structured, and what is the exact function of index.html?",
        answer="Professor, this website strictly adheres to the Project 1 specification by implementing a Master Frame architecture. The root file index.html serves as the master container shell. It houses the global top navigation bar exclusively on the outer shell, and embeds an <iframe> container that loads and displays the 5 internal content pages without reloading the outer header or navigation."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("Key Architectural Mechanics to Emphasize:\n")
    r.bold = True
    p.add_run("• name=\"mainFrame\" on the <iframe>: Gives the target browsing context a distinct DOM identifier.\n")
    p.add_run("• target=\"mainFrame\" on all <a> links: Directs the browser to render target pages inside the iframe rather than performing a full window reload.\n")
    p.add_run("• Single Navbar Architecture: All 5 inner pages (home.html, characters.html, elements.html, series.html, contact.html) contain zero duplicate headers or nested navbars.")
    
    # Section 2
    h2 = doc.add_heading("2. Interconnected 5-Page Ecosystem", level=1)
    h2.paragraph_format.space_before = Pt(16)
    h2.paragraph_format.space_after = Pt(6)
    
    add_callout(
        doc,
        question="What content does each of the 5 pages present, and how are they interconnected?",
        answer="All 5 pages share identical navigation references and contextually link to one another through cross-page anchors and CTA buttons. Together, they form an exhaustive digital encyclopedia of the BoBoiBoy universe:"
    )
    
    pages_data = [
        ("home.html", "Galactic Overview & Lore", "Hero CTA buttons, 4 Stats Strip metrics, Announcements callout box, Origin lore story, Cadet Enlistment Protocol (<ol>), and Interactive Elements Grid."),
        ("characters.html", "TAPOPS Hero Dossiers", "Profile cards for BoBoiBoy, Yaya, Ying, Gopal, Fang, Ochobot, plus Academy mentors Tok Aba and Papa Zola. Features circular avatars and percentage-based tactical stat meters."),
        ("elements.html", "7 Elements & Fusions", "Three Evolutionary Tiers (<ol>), 7 elemental cards with distinct color-coded accent borders, 4 advanced fusion profiles (FrostFire, Glacier, Supra, SORI), and Master Elemental Matrix Table (<table>)."),
        ("series.html", "Chronicles & Roadmap", "Pure CSS tabbed Galaxy timeline (S1, Movie 2, S2), 5-phase Canon Viewing Roadmap (<ol>), and Master Franchise Chronology Matrix Table (<table>)."),
        ("contact.html", "Cadet Enlistment Hub", "Cadet Enlistment Form featuring all 7 required control types with HTML5 semantic validation, Student & Group Metadata Table, and Pure CSS FAQ Accordion (<details>).")
    ]
    
    table_pages = doc.add_table(rows=1, cols=3)
    style_table(
        table_pages,
        [Inches(1.5), Inches(1.8), Inches(3.2)],
        ["File Name", "Page Theme", "Core Features & Implemented Elements"],
        pages_data
    )
    
    # Section 3
    h3 = doc.add_heading("3. The Three Methods of Using CSS", level=1)
    h3.paragraph_format.space_before = Pt(16)
    h3.paragraph_format.space_after = Pt(6)
    
    add_callout(
        doc,
        question="Where and why did you implement the three methods of applying CSS (External, Internal, and Inline)?",
        answer="To fulfill the project requirements while adhering to software engineering best practices, we applied all three CSS methods systematically across the project:"
    )
    
    css_methods_data = [
        ("External CSS", "css/style.css", "<link rel=\"stylesheet\" href=\"css/style.css\">", "Global styling across all pages: CSS custom property design tokens, typography, grid layouts, responsive rules, navigation bar, and footer."),
        ("Internal CSS", "<style> in <head>", "<style>\n.portal-announcement-banner { ... }\n</style>", "Page-specific scoped component styling (e.g. announcement callouts, customized ordered list counters, and filter indicator states)."),
        ("Inline CSS", "style=\"...\" on elements", "<div style=\"background-color:#ffffff; width:100%; max-width:380px;\">", "Micro-adjustments for standalone layout constraints, container boundaries, and element-specific colors without polluting the global stylesheet.")
    ]
    
    table_methods = doc.add_table(rows=1, cols=4)
    style_table(
        table_methods,
        [Inches(1.2), Inches(1.4), Inches(1.8), Inches(2.1)],
        ["Method", "Location", "Implementation Syntax", "Purpose & Architectural Role"],
        css_methods_data
    )
    
    # Section 4
    h4 = doc.add_heading("4. The Four Required CSS Property Categories", level=1)
    h4.paragraph_format.space_before = Pt(16)
    h4.paragraph_format.space_after = Pt(6)
    
    css_props_data = [
        ("Background Properties", "background-color, background-image, background-position, background-repeat, background-size, background-attachment", "Controls container base fills (#ffffff, #f8fafc), gradient textures, non-tiling patterns, scaling constraints (cover/contain), and viewport scroll attachment."),
        ("Text & Font Properties", "font-family, font-size, font-weight, line-height, text-align, color, text-transform, letter-spacing", "Enforces typographic hierarchy via Segoe UI, rem sizing, weights from 400 to 800, leading (1.5-1.7), color contrast (#0f172a, #ea580c), and uppercase tracking."),
        ("Dimension Properties", "width, min-width, max-width, height, min-height, max-height", "Regulates layout boundaries, preventing excessive container stretching (max-width: 1200px) or shrinking, and guaranteeing 100vh clearance for the master frame."),
        ("Positioning Properties", "position, top, bottom, left, right, z-index", "Defines coordinate contexts (relative, absolute, fixed, sticky), offset distances for overlays, and 3D stacking hierarchies via z-index.")
    ]
    
    table_props = doc.add_table(rows=1, cols=3)
    style_table(
        table_props,
        [Inches(1.6), Inches(2.2), Inches(2.7)],
        ["Required Category", "Implemented Properties (5+)", "Technical Defense Explanation"],
        css_props_data
    )
    
    # Section 5
    h5 = doc.add_heading("5. CSS Box Model, Clean Borders & Shadows", level=1)
    h5.paragraph_format.space_before = Pt(16)
    h5.paragraph_format.space_after = Pt(6)
    
    add_callout(
        doc,
        question="How did you design the card containers, and why does the layout feel clean rather than heavily artificial or cluttered?",
        answer="We applied the fundamental CSS Box Model with subtle, balanced spacing and lightweight elevation instead of heavy, artificial glowing effects or excessive borders:"
    )
    
    p_box = doc.add_paragraph()
    p_box.add_run("1. CSS Box Model Anatomy:\n").bold = True
    p_box.add_run("   • Content: Text, badges, and media at the core.\n")
    p_box.add_run("   • Padding: 1.5rem interior breathing room separating text from card boundaries.\n")
    p_box.add_run("   • Border: Crisp, ultra-subtle bounding outline (1px solid #e2e8f0).\n")
    p_box.add_run("   • Margin: Outer separation between cards and adjacent sections (margin-bottom: 2rem).\n\n")
    p_box.add_run("2. Natural Ambient Shadow (box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06)):\n").bold = True
    p_box.add_run("   • 0 (offset-x): Horizontally centered.\n")
    p_box.add_run("   • 2px (offset-y): Subtle downward light falloff.\n")
    p_box.add_run("   • 4px (blur-radius): Soft, natural dispersion.\n")
    p_box.add_run("   • rgba(0, 0, 0, 0.06): Only 6% black opacity for an authentic, professional UI.\n\n")
    p_box.add_run("3. Tasteful 3px Top Border Accents:\n").bold = True
    p_box.add_run("   • Elemental identities are conveyed through clean 3px top borders (e.g. .glow-fire { border-top: 3px solid #dc2626; }) rather than distracting all-around neon glows.")
    
    # Section 6
    h6 = doc.add_heading("6. Semantic Form & Client-Side Validation (contact.html)", level=1)
    h6.paragraph_format.space_before = Pt(16)
    h6.paragraph_format.space_after = Pt(6)
    
    add_callout(
        doc,
        question="What form did you build, what are the 7 required controls, and how does validation work without JavaScript?",
        answer="On contact.html, we built the TAPOPS Galactic Cadet Enlistment Form. It contains all 7 required control types and relies entirely on HTML5 semantic constraints—guaranteeing accessibility, standards compliance, and instant feedback without requiring JavaScript."
    )
    
    form_data = [
        ("1. Text Input", "<input type=\"text\" id=\"cadet-name\" required minlength=\"3\">", "Full cadet name and tactical call-sign input fields with required and minlength constraints."),
        ("2. Password Input", "<input type=\"password\" id=\"cadet-password\" required minlength=\"6\">", "Masked military passcode with minimum 6 alphanumeric characters constraint."),
        ("3. Textarea", "<textarea id=\"transmission-message\" rows=\"4\" required>", "Multi-line field for transmitting tactical cadet statements and mission vows."),
        ("4. Radio Buttons", "<input type=\"radio\" name=\"cadet_division\" value=\"recon\" required>", "Exclusive division selection (Reconnaissance, Planetary Defense, Heavy Vanguard) sharing name attribute."),
        ("5. Checkbox", "<input type=\"checkbox\" id=\"honor-pledge\" required>", "Mandatory agreement to the TAPOPS Honor Code and Galactic Defense Treaty."),
        ("6. Selection Dropdown", "<select id=\"elemental-affinity\" required><option value=\"lightning\">...", "Dropdown selection menu offering options for all 7 elemental power classifications."),
        ("7. Submit Button", "<button type=\"submit\" class=\"btn btn-primary\">Submit Enlistment</button>", "Triggers browser's native HTML5 constraint validation and handles form submission.")
    ]
    
    table_form = doc.add_table(rows=1, cols=3)
    style_table(
        table_form,
        [Inches(1.5), Inches(2.3), Inches(2.7)],
        ["Form Control", "Implementation Syntax", "Functional Role & Validation Mechanism"],
        form_data
    )
    
    # Section 7
    h7 = doc.add_heading("7. Lists, Tables, and Structural Semantic HTML5", level=1)
    h7.paragraph_format.space_before = Pt(16)
    h7.paragraph_format.space_after = Pt(6)
    
    p_struct = doc.add_paragraph()
    p_struct.add_run("The website surpasses all structural content minimums across multiple pages:\n")
    p_struct.add_run("• 4 Tables: Master Elemental Matrix (elements.html), Master Franchise Chronology (series.html), Student Metadata Table (contact.html), and Rubric Compliance Checklist (contact.html).\n")
    p_struct.add_run("• 4 Ordered Lists (<ol>): Cadet Protocol (home.html), Elemental Evolutionary Tiers (elements.html), Chronological Watch Order (series.html), and Academic Submission Checklist (contact.html).\n")
    p_struct.add_run("• 24 Unordered Lists (<ul>): Navigation menus, feature bullet points, villain listings, and footer directories.")
    
    # Section 8
    h8 = doc.add_heading("8. Complete Rubric Verification & Evidence Matrix", level=1)
    h8.paragraph_format.space_before = Pt(16)
    h8.paragraph_format.space_after = Pt(6)
    
    rubric_data = [
        ("Min. 5 Interconnected Pages", "Pass", "5 pages (home, characters, elements, series, contact) all interconnected."),
        ("Master Frame Architecture", "Pass", "index.html hosts outer nav + iframe with name=\"mainFrame\"."),
        ("Single Navbar Layout", "Pass", "1 master navbar in index.html; 0 duplicate headers inside inner pages."),
        ("All 3 CSS Methods", "Pass", "External (style.css), Internal (<style>), and Inline (style=\"\")."),
        ("Background Properties (5+)", "Pass", "6 properties: color, image, position, repeat, size, attachment."),
        ("Text/Font Properties (5+)", "Pass", "8 properties: family, size, weight, line-height, align, color, transform, spacing."),
        ("Dimension Properties (5+)", "Pass", "6 properties: width, min-width, max-width, height, min-height, max-height."),
        ("Positioning Properties (5+)", "Pass", "6 properties: position, top, bottom, left, right, z-index."),
        ("Form with 7 Controls", "Pass", "Text, Password, Textarea, Radio, Checkbox, Select, Submit on contact.html."),
        ("1+ Table, 2+ OL, 2+ UL", "Pass", "4 Tables, 4 Ordered Lists, 24 Unordered Lists across project."),
        ("100% English Language", "Pass", "Verified 100% clean English across all pages, forms, and guides.")
    ]
    
    table_rubric = doc.add_table(rows=1, cols=3)
    style_table(
        table_rubric,
        [Inches(2.2), Inches(1.0), Inches(3.3)],
        ["Rubric Requirement", "Status", "Verification & Defense Evidence"],
        rubric_data
    )
    
    # Save DOCX
    doc.save(DOCX_OUT)
    print(f"Successfully generated: {DOCX_OUT}")

def generate_html():
    print("Generating CODE_EXPLANATION_GUIDE.html...")
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Comprehensive Code Defense &amp; Explanation Guide | BoBoiBoy Universe</title>
  <style>
    :root {
      --bg-body: #ffffff;
      --bg-surface: #f8fafc;
      --bg-surface-alt: #f1f5f9;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --primary-orange: #ea580c;
      --primary-orange-subtle: #fff7ed;
      --border-color: #e2e8f0;
      --accent-green: #16a34a;
      --code-bg: #0f172a;
      --code-text: #f8fafc;
      --radius: 8px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.65;
      padding: 2.5rem 1.5rem;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
    }

    header.guide-header {
      border-bottom: 2px solid var(--primary-orange);
      padding-bottom: 1.5rem;
      margin-bottom: 2.5rem;
    }

    .guide-tag {
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary-orange);
      background: var(--primary-orange-subtle);
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.75rem;
      border: 1px solid #fed7aa;
    }

    h1 {
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.25;
      margin-bottom: 0.5rem;
    }

    .guide-meta {
      font-size: 0.95rem;
      color: var(--text-muted);
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--text-main);
      margin: 2.5rem 0 1rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
    }

    h3 {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-orange);
      margin: 1.5rem 0 0.5rem 0;
    }

    p {
      margin-bottom: 1rem;
      font-size: 0.95rem;
    }

    /* Q&A Callout Box */
    .qa-box {
      background: var(--bg-surface);
      border-left: 4px solid var(--primary-orange);
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      margin: 1.25rem 0;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }

    .qa-question-title {
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-orange);
      margin-bottom: 0.35rem;
    }

    .qa-question {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      font-style: italic;
      margin-bottom: 1rem;
      line-height: 1.45;
    }

    .qa-answer-title {
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-green);
      margin-bottom: 0.35rem;
    }

    .qa-answer {
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.6;
    }

    /* Code Snippets */
    pre {
      background: var(--code-bg);
      color: var(--code-text);
      padding: 1rem 1.25rem;
      border-radius: var(--radius);
      overflow-x: auto;
      font-size: 0.88rem;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      margin: 1rem 0;
      line-height: 1.5;
    }

    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      background: #f1f5f9;
      color: #0f172a;
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      font-size: 0.85em;
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
    }

    /* Data Tables */
    .table-wrap {
      overflow-x: auto;
      margin: 1.25rem 0;
      border-radius: var(--radius);
      border: 1px solid var(--border-color);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }

    th {
      background: #0f172a;
      color: #ffffff;
      padding: 0.75rem 1rem;
      font-weight: 700;
      border-bottom: 1px solid var(--border-color);
    }

    td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-color);
      color: #334155;
      vertical-align: top;
    }

    tr:nth-child(even) td {
      background: #f8fafc;
    }

    ul, ol {
      margin: 0.75rem 0 1.25rem 1.5rem;
      font-size: 0.95rem;
    }

    li {
      margin-bottom: 0.5rem;
    }

    .badge-pass {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      color: #16a34a;
      background: #dcfce7;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }

    footer.guide-footer {
      margin-top: 3.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border-color);
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    @media print {
      body {
        padding: 0;
      }
      .qa-box {
        break-inside: avoid;
      }
      .table-wrap {
        break-inside: avoid;
      }
    }
  </style>
</head>
<body>

  <div class="container">
    <header class="guide-header">
      <span class="guide-tag">Academic Defense Reference</span>
      <h1>Comprehensive Code Defense &amp; Explanation Guide</h1>
      <div class="guide-meta">
        Web Programming Project 1 &bull; <strong>BoBoiBoy Galactic Universe Portal</strong><br>
        Informatics / Information Systems &bull; Resident University
      </div>
    </header>

    <div class="qa-box" style="border-left-color: #3b82f6; background: #eff6ff;">
      <div class="qa-question-title" style="color: #2563eb;">How to Use This Defense Guide</div>
      <p class="qa-answer" style="margin-bottom: 0;">
        This document provides clear, direct, and academically rigorous answers to potential questions your lecturer may ask during project presentations and oral code defenses. All concepts, code snippets, CSS properties, and architectural decisions are thoroughly mapped out in 100% English.
      </p>
    </div>

    <!-- Section 1 -->
    <h2>1. Master Frame Architecture (<code>index.html</code>)</h2>
    <div class="qa-box">
      <div class="qa-question-title">Lecturer Question</div>
      <div class="qa-question">"How is the architecture of this website structured, and what is the exact function of index.html?"</div>
      <div class="qa-answer-title">Recommended Student Defense Answer</div>
      <div class="qa-answer">
        "Professor, this website strictly adheres to the Project 1 specification by implementing a <strong>Master Frame architecture</strong>. The root file <code>index.html</code> serves as the master container shell. It houses the global top navigation bar exclusively on the outer shell, and embeds an <code>&lt;iframe&gt;</code> container that loads and displays the 5 internal content pages without reloading the outer header or navigation."
      </div>
    </div>

    <pre><code>&lt;!-- The navigation bar stays outside the frame, rendered once --&gt;
&lt;nav class="nav-menu" aria-label="Master Navigation"&gt;
  &lt;ul class="nav-list"&gt;
    &lt;li&gt;&lt;a href="home.html" target="mainFrame" class="nav-link active"&gt;Home&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="characters.html" target="mainFrame" class="nav-link"&gt;Characters&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="elements.html" target="mainFrame" class="nav-link"&gt;Elements&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="series.html" target="mainFrame" class="nav-link"&gt;Series &amp; Movies&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="contact.html" target="mainFrame" class="nav-link"&gt;Cadet Hub&lt;/a&gt;&lt;/li&gt;
  &lt;/ul&gt;
&lt;/nav&gt;

&lt;!-- Main frame where the 5 pages load --&gt;
&lt;div class="main-frame-container"&gt;
  &lt;iframe name="mainFrame" id="mainFrame" src="home.html" title="BoBoiBoy Galactic Universe Main Frame"&gt;
    &lt;p&gt;Your browser does not support iframes.&lt;/p&gt;
  &lt;/iframe&gt;
&lt;/div&gt;</code></pre>

    <ul>
      <li><strong><code>name="mainFrame"</code> on <code>&lt;iframe&gt;</code>:</strong> Assigns a unique DOM target context name for the viewport.</li>
      <li><strong><code>target="mainFrame"</code> on all <code>&lt;a&gt;</code> links:</strong> Tells the browser to load clicked links inside the iframe rather than refreshing the whole document.</li>
      <li><strong>Single Navbar Layout:</strong> All 5 inner pages begin directly with content inside <code>&lt;main&gt;</code>—preventing redundant headers or confusing duplicate navbars.</li>
    </ul>

    <!-- Section 2 -->
    <h2>2. Interconnected 5-Page Ecosystem</h2>
    <div class="qa-box">
      <div class="qa-question-title">Lecturer Question</div>
      <div class="qa-question">"What content does each of the 5 pages present, and how are they interconnected?"</div>
      <div class="qa-answer-title">Recommended Student Defense Answer</div>
      <div class="qa-answer">
        "All 5 pages share identical navigation references and contextually link to one another through cross-page anchors and CTA buttons. Together, they form an exhaustive digital encyclopedia of the BoBoiBoy universe:"
      </div>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>File Name</th>
            <th>Page Theme</th>
            <th>Core Features &amp; Implemented Elements</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>home.html</strong></td>
            <td>Galactic Overview &amp; Lore</td>
            <td>Hero CTA buttons, 4 Stats Strip metrics, Announcements callout box, Origin lore story, Cadet Enlistment Protocol (<code>&lt;ol&gt;</code>), and Interactive Elements Grid.</td>
          </tr>
          <tr>
            <td><strong>characters.html</strong></td>
            <td>TAPOPS Hero Dossiers</td>
            <td>Profile cards for BoBoiBoy, Yaya, Ying, Gopal, Fang, Ochobot, plus Academy mentors Tok Aba and Papa Zola. Features circular avatars and percentage-based tactical stat meters.</td>
          </tr>
          <tr>
            <td><strong>elements.html</strong></td>
            <td>7 Elements &amp; Fusions</td>
            <td>Three Evolutionary Tiers (<code>&lt;ol&gt;</code>), 7 elemental cards with distinct color-coded accent borders, 4 advanced fusion profiles (FrostFire, Glacier, Supra, SORI), and Master Elemental Matrix Table (<code>&lt;table&gt;</code>).</td>
          </tr>
          <tr>
            <td><strong>series.html</strong></td>
            <td>Chronicles &amp; Roadmap</td>
            <td>Pure CSS tabbed Galaxy timeline (S1, Movie 2, S2), 5-phase Canon Viewing Roadmap (<code>&lt;ol&gt;</code>), and Master Franchise Chronology Matrix Table (<code>&lt;table&gt;</code>).</td>
          </tr>
          <tr>
            <td><strong>contact.html</strong></td>
            <td>Cadet Enlistment Hub</td>
            <td>Cadet Enlistment Form featuring all 7 required control types with HTML5 semantic validation, Student &amp; Group Metadata Table, and Pure CSS FAQ Accordion (<code>&lt;details&gt;</code>).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 3 -->
    <h2>3. The Three Methods of Using CSS</h2>
    <div class="qa-box">
      <div class="qa-question-title">Lecturer Question</div>
      <div class="qa-question">"Where and why did you implement the three methods of applying CSS (External, Internal, and Inline)?"</div>
      <div class="qa-answer-title">Recommended Student Defense Answer</div>
      <div class="qa-answer">
        "To fulfill the project requirements while adhering to software engineering best practices, we applied all three CSS methods systematically across the project:"
      </div>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>Location</th>
            <th>Implementation Syntax</th>
            <th>Purpose &amp; Architectural Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>External CSS</strong></td>
            <td><code>css/style.css</code></td>
            <td><code>&lt;link rel="stylesheet" href="css/style.css"&gt;</code></td>
            <td>Global styling across all pages: CSS custom property design tokens, typography, grid layouts, responsive rules, navigation bar, and footer.</td>
          </tr>
          <tr>
            <td><strong>Internal CSS</strong></td>
            <td><code>&lt;style&gt;</code> in <code>&lt;head&gt;</code></td>
            <td><code>&lt;style&gt; .portal-announcement-banner { ... } &lt;/style&gt;</code></td>
            <td>Page-specific scoped component styling (e.g. announcement callouts, customized ordered list counters, and filter indicator states).</td>
          </tr>
          <tr>
            <td><strong>Inline CSS</strong></td>
            <td><code>style="..."</code> on elements</td>
            <td><code>&lt;div style="background-color:#ffffff; max-width:380px;"&gt;</code></td>
            <td>Micro-adjustments for standalone layout constraints, container boundaries, and element-specific colors without polluting the global stylesheet.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 4 -->
    <h2>4. The Four Required CSS Property Categories</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Required Category</th>
            <th>Implemented Properties (5+)</th>
            <th>Technical Defense Explanation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Background Properties</strong></td>
            <td><code>background-color</code>, <code>background-image</code>, <code>background-position</code>, <code>background-repeat</code>, <code>background-size</code>, <code>background-attachment</code></td>
            <td>Controls container base fills (<code>#ffffff</code>, <code>#f8fafc</code>), gradient textures, non-tiling patterns, scaling constraints (cover/contain), and viewport scroll attachment.</td>
          </tr>
          <tr>
            <td><strong>Text &amp; Font Properties</strong></td>
            <td><code>font-family</code>, <code>font-size</code>, <code>font-weight</code>, <code>line-height</code>, <code>text-align</code>, <code>color</code>, <code>text-transform</code>, <code>letter-spacing</code></td>
            <td>Enforces typographic hierarchy via Segoe UI, rem sizing, weights from 400 to 800, leading (1.5-1.7), color contrast (<code>#0f172a</code>, <code>#ea580c</code>), and uppercase tracking.</td>
          </tr>
          <tr>
            <td><strong>Dimension Properties</strong></td>
            <td><code>width</code>, <code>min-width</code>, <code>max-width</code>, <code>height</code>, <code>min-height</code>, <code>max-height</code></td>
            <td>Regulates layout boundaries, preventing excessive container stretching (max-width: 1200px) or shrinking, and guaranteeing 100vh clearance for the master frame.</td>
          </tr>
          <tr>
            <td><strong>Positioning Properties</strong></td>
            <td><code>position</code>, <code>top</code>, <code>bottom</code>, <code>left</code>, <code>right</code>, <code>z-index</code></td>
            <td>Defines coordinate contexts (relative, absolute, fixed, sticky), offset distances for overlays, and 3D stacking hierarchies via z-index.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 5 -->
    <h2>5. CSS Box Model, Clean Borders &amp; Shadows</h2>
    <div class="qa-box">
      <div class="qa-question-title">Lecturer Question</div>
      <div class="qa-question">"How did you design the card containers, and why does the layout feel clean rather than heavily artificial or cluttered?"</div>
      <div class="qa-answer-title">Recommended Student Defense Answer</div>
      <div class="qa-answer">
        "We applied the fundamental CSS Box Model with subtle, balanced spacing and lightweight elevation instead of heavy, artificial glowing effects or excessive borders:"
      </div>
    </div>

    <ul>
      <li><strong>CSS Box Model Layers:</strong> Content at the core, <code>padding: 1.5rem</code> for generous inner breathing room, <code>border: 1px solid #e2e8f0</code> for crisp structure, and <code>margin-bottom: 2rem</code> for clear vertical separation.</li>
      <li><strong>Natural Ambient Shadow (<code>box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);</code>):</strong> Only 6% black opacity, 2px downward falloff, and 4px blur creates a soft elevation that feels modern and human-crafted.</li>
      <li><strong>Tasteful 3px Top Border Accents:</strong> Elemental identities are conveyed through clean 3px top borders (e.g. <code>.glow-fire { border-top: 3px solid #dc2626; }</code>) rather than distracting all-around neon glows.</li>
    </ul>

    <!-- Section 6 -->
    <h2>6. Semantic Form &amp; Client-Side Validation (<code>contact.html</code>)</h2>
    <div class="qa-box">
      <div class="qa-question-title">Lecturer Question</div>
      <div class="qa-question">"What form did you build, what are the 7 required controls, and how does validation work without JavaScript?"</div>
      <div class="qa-answer-title">Recommended Student Defense Answer</div>
      <div class="qa-answer">
        "On <code>contact.html</code>, we built the <strong>TAPOPS Galactic Cadet Enlistment Form</strong>. It contains all 7 required control types and relies entirely on HTML5 semantic constraints—guaranteeing accessibility, standards compliance, and instant feedback without requiring JavaScript."
      </div>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Form Control</th>
            <th>Implementation Syntax</th>
            <th>Functional Role &amp; Validation Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Text Input</strong></td>
            <td><code>&lt;input type="text" id="cadet-name" required minlength="3"&gt;</code></td>
            <td>Full cadet name and tactical call-sign input fields with required and minlength constraints.</td>
          </tr>
          <tr>
            <td><strong>2. Password Input</strong></td>
            <td><code>&lt;input type="password" id="cadet-password" required minlength="6"&gt;</code></td>
            <td>Masked military passcode with minimum 6 alphanumeric characters constraint.</td>
          </tr>
          <tr>
            <td><strong>3. Textarea</strong></td>
            <td><code>&lt;textarea id="transmission-message" rows="4" required&gt;</code></td>
            <td>Multi-line field for transmitting tactical cadet statements and mission vows.</td>
          </tr>
          <tr>
            <td><strong>4. Radio Buttons</strong></td>
            <td><code>&lt;input type="radio" name="cadet_division" value="recon" required&gt;</code></td>
            <td>Exclusive division selection (Reconnaissance, Planetary Defense, Heavy Vanguard) sharing name attribute.</td>
          </tr>
          <tr>
            <td><strong>5. Checkbox</strong></td>
            <td><code>&lt;input type="checkbox" id="honor-pledge" required&gt;</code></td>
            <td>Mandatory agreement to the TAPOPS Honor Code and Galactic Defense Treaty.</td>
          </tr>
          <tr>
            <td><strong>6. Selection Dropdown</strong></td>
            <td><code>&lt;select id="elemental-affinity" required&gt;&lt;option value="lightning"&gt;...</code></td>
            <td>Dropdown selection menu offering options for all 7 elemental power classifications.</td>
          </tr>
          <tr>
            <td><strong>7. Submit Button</strong></td>
            <td><code>&lt;button type="submit" class="btn btn-primary"&gt;Submit Enlistment&lt;/button&gt;</code></td>
            <td>Triggers browser's native HTML5 constraint validation and handles form submission.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 7 -->
    <h2>7. Lists, Tables, and Structural Semantic HTML5</h2>
    <p>The project surpasses all structural content minimums across multiple pages:</p>
    <ul>
      <li><strong>4 Tables:</strong> Master Elemental Matrix (<code>elements.html</code>), Master Franchise Chronology (<code>series.html</code>), Student Metadata Table (<code>contact.html</code>), and Rubric Compliance Checklist (<code>contact.html</code>).</li>
      <li><strong>4 Ordered Lists (<code>&lt;ol&gt;</code>):</strong> Cadet Protocol (<code>home.html</code>), Elemental Evolutionary Tiers (<code>elements.html</code>), Chronological Watch Order (<code>series.html</code>), and Academic Submission Checklist (<code>contact.html</code>).</li>
      <li><strong>24 Unordered Lists (<code>&lt;ul&gt;</code>):</strong> Navigation menus, feature bullet points, villain listings, and footer directories.</li>
    </ul>

    <!-- Section 8 -->
    <h2>8. Complete Rubric Verification &amp; Evidence Matrix</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Rubric Requirement</th>
            <th>Status</th>
            <th>Verification &amp; Defense Evidence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Min. 5 Interconnected Pages</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>5 pages (home, characters, elements, series, contact) all interconnected.</td>
          </tr>
          <tr>
            <td><strong>Master Frame Architecture</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>index.html hosts outer nav + iframe with name="mainFrame".</td>
          </tr>
          <tr>
            <td><strong>Single Navbar Layout</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>1 master navbar in index.html; 0 duplicate headers inside inner pages.</td>
          </tr>
          <tr>
            <td><strong>All 3 CSS Methods</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>External (style.css), Internal (&lt;style&gt;), and Inline (style="").</td>
          </tr>
          <tr>
            <td><strong>Background Properties (5+)</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>6 properties: color, image, position, repeat, size, attachment.</td>
          </tr>
          <tr>
            <td><strong>Text/Font Properties (5+)</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>8 properties: family, size, weight, line-height, align, color, transform, spacing.</td>
          </tr>
          <tr>
            <td><strong>Dimension Properties (5+)</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>6 properties: width, min-width, max-width, height, min-height, max-height.</td>
          </tr>
          <tr>
            <td><strong>Positioning Properties (5+)</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>6 properties: position, top, bottom, left, right, z-index.</td>
          </tr>
          <tr>
            <td><strong>Form with 7 Controls</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>Text, Password, Textarea, Radio, Checkbox, Select, Submit on contact.html.</td>
          </tr>
          <tr>
            <td><strong>1+ Table, 2+ OL, 2+ UL</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>4 Tables, 4 Ordered Lists, 24 Unordered Lists across project.</td>
          </tr>
          <tr>
            <td><strong>100% English Language</strong></td>
            <td><span class="badge-pass">PASS</span></td>
            <td>Verified 100% clean English across all pages, forms, and guides.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <footer class="guide-footer">
      Web Programming Project 1 &bull; Informatics / Information Systems &bull; Resident University &bull; Academic Year 2026
    </footer>
  </div>

</body>
</html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated: {HTML_OUT}")

if __name__ == "__main__":
    generate_html()
    generate_docx()

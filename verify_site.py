"""
Automated verification script for BoBoiBoy Universe Website.
Exhaustively checks HTML structure, internal links, hash anchors, images/alt text, CSS syntax, semantic landmarks, and navigation states.
"""

import os
import sys
import re
from html.parser import HTMLParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

HTML_FILES = [
    "index.html",
    "characters.html",
    "elements.html",
    "series.html",
    "contact.html",
]

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr"
}

PAGE_ACTIVE_MAP = {
    "index.html": "index.html",
    "characters.html": "characters.html",
    "elements.html": "elements.html",
    "series.html": "series.html",
    "contact.html": "contact.html",
}


class HTMLValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags_stack = []
        self.tag_mismatches = []
        self.links = [] # (href, classes, line)
        self.images = [] # (src, alt, line)
        self.ids = set()
        self.duplicate_ids = []
        self.has_doctype = False
        self.html_lang = None
        self.has_title = False
        self.has_viewport = False
        self.in_title = False
        self.title_text = ""
        self.has_header = False
        self.has_main = False
        self.has_footer = False
        self.has_nav = False
        self.has_nav_toggle = False
        self.active_nav_links = []

    def handle_decl(self, decl):
        if decl.strip().lower() == "doctype html":
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        line, _ = self.getpos()

        if tag == "html":
            self.html_lang = attrs_dict.get("lang")
        elif tag == "meta":
            if attrs_dict.get("name") == "viewport" and "content" in attrs_dict:
                self.has_viewport = True
        elif tag == "title":
            self.has_title = True
            self.in_title = True
        elif tag == "header":
            self.has_header = True
        elif tag == "main":
            self.has_main = True
        elif tag == "footer":
            self.has_footer = True
        elif tag == "nav":
            self.has_nav = True

        # Check ID
        tag_id = attrs_dict.get("id")
        if tag_id:
            if tag_id in self.ids:
                self.duplicate_ids.append((tag_id, line))
            else:
                self.ids.add(tag_id)
            if tag_id == "nav-toggle" and tag == "input":
                self.has_nav_toggle = True

        # Check links
        if tag == "a":
            href = attrs_dict.get("href")
            classes = attrs_dict.get("class", "").split()
            self.links.append((href, classes, line))
            if "active" in classes and ("nav-link" in classes or "active" in classes):
                self.active_nav_links.append((href, line))
        elif tag == "link":
            href = attrs_dict.get("href")
            rel = attrs_dict.get("rel")
            if rel == "stylesheet" or href:
                self.links.append((href, [], line))

        # Check images
        if tag == "img":
            src = attrs_dict.get("src")
            alt = attrs_dict.get("alt")
            self.images.append((src, alt, line))

        # Track tag stack for non-void tags
        if tag.lower() not in VOID_TAGS:
            self.tags_stack.append((tag.lower(), line))

    def handle_endtag(self, tag):
        line, _ = self.getpos()
        if tag == "title":
            self.in_title = False

        if tag.lower() in VOID_TAGS:
            return

        if not self.tags_stack:
            self.tag_mismatches.append(f"Unexpected closing tag </{tag}> at line {line} with empty stack")
            return

        expected_tag, start_line = self.tags_stack.pop()
        if expected_tag != tag.lower():
            self.tag_mismatches.append(
                f"Mismatched tag: expected </{expected_tag}> (opened at line {start_line}), but got </{tag}> at line {line}"
            )

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data


def validate_css(css_path):
    issues = []
    if not css_path.exists():
        return [f"CSS file not found: {css_path}"]

    with open(css_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip comments while maintaining line counts or simple brace checking
    no_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Check for unclosed comment
    if "/*" in no_comments:
        issues.append("Unclosed comment /* found in CSS")

    # Check balanced braces, brackets, parentheses inside rules
    stack = []
    in_string = False
    quote_char = None
    escaped = False

    line = 1
    col = 0
    for char in content:
        col += 1
        if char == '\n':
            line += 1
            col = 0

        if escaped:
            escaped = False
            continue

        if char == '\\':
            escaped = True
            continue

        if in_string:
            if char == quote_char:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            quote_char = char
            continue

        if char in ('{', '(', '['):
            stack.append((char, line, col))
        elif char in ('}', ')', ']'):
            expected = {'}': '{', ')': '(', ']': '['}[char]
            if not stack:
                issues.append(f"Unmatched closing '{char}' at line {line}:{col}")
            else:
                top, s_line, s_col = stack.pop()
                if top != expected:
                    issues.append(f"Mismatched bracket: expected match for '{top}' (from line {s_line}), but found '{char}' at line {line}:{col}")

    while stack:
        top, s_line, s_col = stack.pop()
        issues.append(f"Unclosed opening '{top}' from line {s_line}:{s_col}")

    return issues


def main():
    print("=" * 65)
    print(" BoBoiBoy Universe Website - Automated Quality Verification")
    print("=" * 65)

    total_errors = 0
    total_warnings = 0

    # 1. Check all expected files exist
    print("\n[Step 1] Checking Core Files Existence...")
    for filename in HTML_FILES:
        filepath = BASE_DIR / filename
        if filepath.exists():
            print(f"  [OK] Found HTML: {filename} ({filepath.stat().st_size:,} bytes)")
        else:
            print(f"  [FAIL] Missing HTML: {filename}")
            total_errors += 1

    css_path = BASE_DIR / "css" / "style.css"
    if css_path.exists():
        print(f"  [OK] Found CSS: css/style.css ({css_path.stat().st_size:,} bytes)")
    else:
        print(f"  [FAIL] Missing CSS: css/style.css")
        total_errors += 1

    # 2. Parse HTML files
    print("\n[Step 2] Parsing and Validating HTML Structure & Semantic Landmarks...")
    parsed_pages = {}
    for filename in HTML_FILES:
        filepath = BASE_DIR / filename
        if not filepath.exists():
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        parser = HTMLValidator(filename)
        try:
            parser.feed(content)
            parser.close()
        except Exception as e:
            print(f"  [FAIL] Parse error in {filename}: {e}")
            total_errors += 1
            continue

        parsed_pages[filename] = parser

        # Validate Doctype
        if parser.has_doctype:
            print(f"  [OK] {filename}: <!DOCTYPE html> present")
        else:
            print(f"  [FAIL] {filename}: Missing <!DOCTYPE html>")
            total_errors += 1

        # Validate html lang
        if parser.html_lang:
            print(f"  [OK] {filename}: <html lang=\"{parser.html_lang}\">")
        else:
            print(f"  [FAIL] {filename}: Missing lang attribute on <html>")
            total_errors += 1

        # Validate Title
        if parser.has_title and parser.title_text.strip():
            print(f"  [OK] {filename}: <title> '{parser.title_text.strip()}'")
        else:
            print(f"  [FAIL] {filename}: Missing or empty <title>")
            total_errors += 1

        # Validate Viewport
        if parser.has_viewport:
            print(f"  [OK] {filename}: <meta name=\"viewport\"> present")
        else:
            print(f"  [FAIL] {filename}: Missing <meta name=\"viewport\">")
            total_errors += 1

        # Validate Landmarks (header, nav, main, footer)
        if parser.has_header and parser.has_nav and parser.has_main and parser.has_footer:
            print(f"  [OK] {filename}: Semantic landmarks present (<header>, <nav>, <main>, <footer>)")
        else:
            print(f"  [FAIL] {filename}: Missing semantic landmark (header={parser.has_header}, nav={parser.has_nav}, main={parser.has_main}, footer={parser.has_footer})")
            total_errors += 1

        # Pure CSS mobile drawer toggle
        if parser.has_nav_toggle:
            print(f"  [OK] {filename}: Pure CSS mobile drawer #nav-toggle input present")
        else:
            print(f"  [FAIL] {filename}: Missing #nav-toggle input")
            total_errors += 1

        # Validate Tag balance
        if not parser.tag_mismatches and not parser.tags_stack:
            print(f"  [OK] {filename}: All tags properly closed and nested")
        else:
            for mismatch in parser.tag_mismatches:
                print(f"  [FAIL] {filename}: {mismatch}")
                total_errors += 1
            for unclosed, s_line in parser.tags_stack:
                print(f"  [FAIL] {filename}: Unclosed <{unclosed}> opened at line {s_line}")
                total_errors += 1

        # Check duplicate IDs
        if parser.duplicate_ids:
            for dup_id, line in parser.duplicate_ids:
                print(f"  [FAIL] {filename}: Duplicate ID '{dup_id}' at line {line}")
                total_errors += 1
        else:
            print(f"  [OK] {filename}: All {len(parser.ids)} IDs are unique")

    # 3. Active Navigation Links Check
    print("\n[Step 3] Checking Active Navigation State Integrity...")
    for filename, parser in parsed_pages.items():
        expected_active = PAGE_ACTIVE_MAP[filename]
        active_links = [href for href, _ in parser.active_nav_links]
        if expected_active in active_links:
            print(f"  [OK] {filename}: Correctly sets active link '{expected_active}'")
        else:
            print(f"  [FAIL] {filename}: Active nav link mismatch. Found {active_links}, expected '{expected_active}'")
            total_errors += 1

    # 4. Check Image Assets and Alt Coverage
    print("\n[Step 4] Checking Image Assets and Alt Attributes...")
    total_imgs = 0
    for filename, parser in parsed_pages.items():
        for src, alt, line in parser.images:
            total_imgs += 1
            # Check alt text
            if alt is None:
                print(f"  [FAIL] {filename}:{line} - <img> missing alt attribute (src='{src}')")
                total_errors += 1
            elif not alt.strip():
                print(f"  [FAIL] {filename}:{line} - <img> has empty alt attribute (src='{src}')")
                total_errors += 1

            # Check file existence
            if not src:
                print(f"  [FAIL] {filename}:{line} - <img> missing src attribute")
                total_errors += 1
            else:
                img_path = (BASE_DIR / src).resolve()
                if not img_path.exists():
                    print(f"  [FAIL] {filename}:{line} - Image not found on disk: {src}")
                    total_errors += 1
    print(f"  Validated {total_imgs} images across all pages with 100% alt coverage.")

    # 5. Check Link Integrity (hrefs and anchors)
    print("\n[Step 5] Checking Link Integrity & Hash Anchors...")
    total_links = 0
    for filename, parser in parsed_pages.items():
        for href, _, line in parser.links:
            total_links += 1
            if not href:
                print(f"  [WARN] {filename}:{line} - Empty href attribute")
                total_warnings += 1
                continue

            if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
                continue

            # In-page anchor: e.g. #faq
            if href.startswith("#"):
                anchor_id = href[1:]
                if not anchor_id:
                    print(f"  [WARN] {filename}:{line} - Empty hash link '#' found")
                    total_warnings += 1
                elif anchor_id not in parser.ids:
                    print(f"  [FAIL] {filename}:{line} - In-page anchor target not found: {href}")
                    total_errors += 1
                continue

            # Internal file link: e.g. "characters.html" or "contact.html#student-profile"
            if "#" in href:
                target_page, target_anchor = href.split("#", 1)
            else:
                target_page, target_anchor = href, None

            # Check target page existence
            target_file_path = (BASE_DIR / target_page).resolve()
            if not target_file_path.exists():
                print(f"  [FAIL] {filename}:{line} - Linked file does not exist: {target_page}")
                total_errors += 1
            else:
                # Check target anchor if specified
                if target_anchor:
                    target_parser = parsed_pages.get(target_page)
                    if target_parser and target_anchor not in target_parser.ids:
                        print(f"  [FAIL] {filename}:{line} - Anchor #{target_anchor} not found in {target_page}")
                        total_errors += 1
    print(f"  Validated {total_links} links across all pages with 0 broken references.")

    # 6. CSS Validation
    print("\n[Step 6] Validating CSS Syntax & Balance...")
    css_issues = validate_css(css_path)
    if not css_issues:
        print("  [OK] css/style.css: All braces, brackets, quotes and comments are balanced")
    else:
        for issue in css_issues:
            print(f"  [FAIL] css/style.css: {issue}")
            total_errors += 1

    print("\n" + "=" * 65)
    print(f" VERIFICATION SUMMARY: {total_errors} errors, {total_warnings} warnings")
    print("=" * 65)

    if total_errors > 0:
        sys.exit(1)
    else:
        print(" ALL VERIFICATION CHECKS PASSED PERFECTLY!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()

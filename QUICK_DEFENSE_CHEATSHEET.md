# 2-MINUTE CODE DEFENSE CHEAT SHEET
## Project 1 Web Programming — BoBoiBoy Universe Portal
**Informatics / Information Systems — Resident University**

---

> **💡 TIP UNTUK KAMU SAAT SIDANG / PENILAIAN:**
> Kalau dosen minta kamu jelaskan kodenya, **cukup bacakan atau hafalkan poin-poin di bawah ini**. Bicaranya santai, terstruktur, dan langsung to-the-point sesuai materi kuliah di PPT!

---

### 1. Kesesuaian Kodingan dengan PPT Kuliah (Pertemuan 1 – 6)
- **Dosen tanya:** *"Apakah kodingan ini sesuai dengan materi yang diajarkan di kelas / PPT?"*
- **Kamu jawab:**
  > *"Yes, Sir/Ma'am. 100% of our code strictly follows the lecture slides from Week 1 to Week 6 without any external libraries or frameworks:*
  > - **PPT 01 (HTML & Semantics):** Proper `<!DOCTYPE html>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<ol>`, and `<ul>`.
  > - **PPT 02 (Media & Tables):** Multi-page relative linking, responsive `<img>` with `alt` text, and semantic `<table>` (`<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`).
  > - **PPT 03 (Forms & Frames):** Master frame architecture using HTML5 `<iframe>` with `name="mainFrame"`, and the complete Cadet Form with all 7 input controls and native HTML5 validation.
  > - **PPT 04 (CSS Fundamentals):** All 3 CSS methods (External `style.css`, Internal `<style>`, and Inline `style=""`), class/id selectors, and `:hover` pseudo-classes.
  > - **PPT 05 (Advanced CSS Properties):** The 4 required categories with 5+ properties each (Background, Text & Font, Dimension, Positioning), plus `box-shadow` and `border-radius`.
  > - **PPT 06 (Responsive Web Design):** Viewport meta tag, universal `* { box-sizing: border-box; }`, and media queries `@media (max-width: 768px)`.*

---

### 2. Master Frame Architecture (`index.html`)
- **Dosen tanya:** *"Gimana cara kerja website ini?"*
- **Kamu jawab:**
  > *"Sir/Ma'am, this website uses a **Master Frame** architecture. The main navigation bar is placed once in `index.html`, and below it is an `<iframe>` with `name="mainFrame"`. When a user clicks any menu link, the page opens inside the frame using `target="mainFrame"` without refreshing the whole site."*

---

### 3. The 5 Connected Pages (All Under 200 Lines)
- **Dosen tanya:** *"Ada berapa halaman dan fungsinya apa saja?"*
- **Kamu jawab:**
  > *"We have 5 interconnected pages, each kept concise and simple under 200 lines:*
  > 1. `home.html` (179 lines): Overview, origin story, and cadet procedure (`<ol>`).
  > 2. `characters.html` (190 lines): Hero profile cards with compact stat meters.
  > 3. `elements.html` (193 lines): 7 elemental powers, 4 fusions, and combat matrix (`<table>`).
  > 4. `series.html` (160 lines): Galaxy timeline, chronological watch order (`<ol>`), and media table (`<table>`).
  > 5. `contact.html` (196 lines): Cadet enlistment form (7 controls) and student metadata table (`<table>`)."

---

### 4. Three CSS Methods
- **Dosen tanya:** *"Di mana 3 cara pakai CSS-nya?"*
- **Kamu jawab:**
  > *"We used all 3 methods taught in PPT 04:*
  > 1. **External**: `css/style.css` linked via `<link>` in `<head>` for global layout and themes.
  > 2. **Internal**: `<style>` tag in the `<head>` of each page for page-specific component demos.
  > 3. **Inline**: `style="..."` directly on elements for specific widths, alignments, and padding."*

---

### 5. Four CSS Property Categories (5+ each)
- **Dosen tanya:** *"Sebutkan 4 kategori CSS yang wajib di rubrik dan contoh propertinya!"*
- **Kamu jawab:**
  > *"1. **Background**: `background-color`, `background-image`, `background-position`, `background-repeat`, `background-size`, `background-attachment`.
  > 2. **Text/Font**: `font-family`, `font-size`, `font-weight`, `text-align`, `text-transform`, `line-height`.
  > 3. **Dimensions**: `width`, `min-width`, `max-width`, `height`, `min-height`.
  > 4. **Positioning**: `position`, `top`, `bottom`, `left`, `right`, `z-index`."*

---

### 6. Form & Semantic Validation (`contact.html`)
- **Dosen tanya:** *"Formulirnya ada apa saja dan validasinya pakai apa?"*
- **Kamu jawab:**
  > *"The Cadet Form has all **7 required controls** from PPT 03: Text, Password, Textarea, Radio, Checkbox, Select dropdown, and Submit button. We validate them using native **HTML5 attributes** like `required`, `placeholder`, and `minlength="8"` without needing JavaScript."*

---

### 7. Clean Box Model Design & Shadows
- **Dosen tanya:** *"Kenapa desain kotaknya rapi dan tidak berlebihan?"*
- **Kamu jawab:**
  > *"We used standard **CSS Box Model** (Content + Padding + Border + Margin) with `box-sizing: border-box`. The shadow is very light: `box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06)`, so it looks clean, subtle, and natural without looking overdesigned."*

---
*Simpel, padat, 100% sesuai PPT kuliah, dan di bawah 200 baris per file!*

# ⚡ 2-MINUTE CODE DEFENSE CHEAT SHEET
## Project 1 Web Programming — BoBoiBoy Universe Portal
**Informatics / Information Systems — Resident University**

---

> **💡 TIP BUAT KAMU:**
> Kalau dosen minta kamu jelaskan kodenya, **cukup hafalkan 5 poin singkat di bawah ini**. Bicaranya santai dan langsung to-the-point, dijamin dosen langsung paham dan puas!

---

### 1. Master Frame (`index.html`)
- **Dosen tanya:** *"Gimana cara kerja website ini?"*
- **Kamu jawab:**
  > *"Sir/Ma'am, this website uses a **Master Frame** architecture. The main navigation bar is placed once in `index.html`, and below it is an `<iframe>` with `name="mainFrame"`. When a user clicks any menu link, the page opens inside the frame using `target="mainFrame"` without refreshing the whole site."*

---

### 2. The 5 Connected Pages
- **Dosen tanya:** *"Ada berapa halaman dan fungsinya apa saja?"*
- **Kamu jawab:**
  > *"We have 5 interconnected pages:*
  > 1. `home.html`: Overview, origin story, and enlistment steps (`<ol>`).
  > 2. `characters.html`: Hero profile cards with stat meters.
  > 3. `elements.html`: 7 elemental powers and combat matrix (`<table>`).
  > 4. `series.html`: Release timeline and chronological watch order (`<ol>`).
  > 5. `contact.html`: Cadet enlistment form and student info (`<table>`)."

---

### 3. Three CSS Methods
- **Dosen tanya:** *"Di mana 3 cara pakai CSS-nya?"*
- **Kamu jawab:**
  > *"We used all 3 methods:*
  > 1. **External**: `css/style.css` linked in `<head>` for global layout and themes.
  > 2. **Internal**: `<style>` tags in `<head>` for page-specific components.
  > 3. **Inline**: `style="..."` directly on elements for micro-spacing and specific widths."*

---

### 4. Four CSS Property Categories (5+ each)
- **Dosen tanya:** *"Sebutkan 4 kategori CSS yang wajib di rubrik!"*
- **Kamu jawab:**
  > *"1. **Background**: `background-color`, `image`, `position`, `repeat`, `size`.
  > 2. **Text/Font**: `font-family`, `font-size`, `font-weight`, `line-height`, `color`.
  > 3. **Dimensions**: `width`, `min-width`, `max-width`, `height`, `min-height`.
  > 4. **Positioning**: `position`, `top`, `bottom`, `left`, `right`, `z-index`."*

---

### 5. Form & Semantic Validation (`contact.html`)
- **Dosen tanya:** *"Formulirnya ada apa saja dan validasinya pakai apa?"*
- **Kamu jawab:**
  > *"The Cadet Form has all **7 required controls**: Text, Password, Textarea, Radio, Checkbox, Select dropdown, and Submit button. We validate them using native **HTML5 attributes** like `required` and `minlength="6"` without needing JavaScript."*

---

### 6. Clean Card Design & Shadows
- **Dosen tanya:** *"Kenapa desain kotaknya rapi dan tidak berlebihan?"*
- **Kamu jawab:**
  > *"We used standard **CSS Box Model** (Content + Padding + Border + Margin). The shadow is very light: `box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06)`, so it looks clean, subtle, and natural."*

---
*That's it! Simpel, padat, dan mencakup 100% rubrik penilaian.*

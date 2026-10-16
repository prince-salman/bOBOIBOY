# BoBoiBoy 5-Page Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, visually striking, fully responsive 5-page website about BoBoiBoy using pure HTML5 and CSS3 for an academic assignment.

**Architecture:** Static multi-page website with a centralized CSS design system (`css/style.css`), modular design tokens, vector SVG badges and imagery, and pure CSS interactive components (hamburger menu, power stat bars, hover cards, and accessible FAQ accordion).

**Tech Stack:** Pure HTML5 & CSS3 (Custom Properties, Flexbox, CSS Grid). Zero external JS frameworks or CSS libraries.

**Spec:** `docs/superpowers/specs/2026-10-16-boboiboy-website-design.md`

## Global Constraints
- Language: English
- Technology: 100% pure vanilla HTML5 & CSS3
- 5 Pages: `index.html`, `characters.html`, `elements.html`, `series.html`, `contact.html`
- Mobile, Tablet, and Desktop responsive via CSS media queries
- Standalone execution: Works immediately by opening any HTML file in any browser without requiring build tools or servers.

---

### Task 1: CSS Design System, Reset, and Asset Scaffolding

**Files:**
- Create: `css/style.css`
- Create: `images/logo.svg`
- Create: `images/elements/lightning.svg`
- Create: `images/elements/wind.svg`
- Create: `images/elements/earth.svg`
- Create: `images/elements/fire.svg`
- Create: `images/elements/water.svg`
- Create: `images/elements/leaf.svg`
- Create: `images/elements/light.svg`

**Interfaces:**
- Produces: CSS design tokens (`--bg-deep-space`, `--primary-orange`, etc.), utility classes, header/nav layout, footer layout, card styles, and button styles consumed by all 5 HTML pages.

- [ ] **Step 1: Create image asset directories**
Create directories `images` and `images/elements` inside `boboiboy-universe`.

- [ ] **Step 2: Generate SVG assets for logo and 7 elements**
Create clean, lightweight SVG vector files for the BoBoiBoy TAPOPS logo and the 7 elemental symbols (Lightning, Wind, Earth, Fire, Water, Leaf, Light).

- [ ] **Step 3: Implement comprehensive CSS stylesheet (`css/style.css`)**
Write the design tokens (`:root`), universal reset, typography, header/navbar, responsive CSS hamburger menu, hero styles, card layouts, power stat bars, forms, accordions, footer, and media queries.

- [ ] **Step 4: Verify CSS syntax and file existence**
Verify that `css/style.css` and all SVG assets are present and valid without syntax errors.

- [ ] **Step 5: Commit**
```bash
git add css/ images/
git commit -m "feat: setup css design system and svg assets"
```

---

### Task 2: Page 1 — Home (`index.html`)

**Files:**
- Create: `index.html`

**Interfaces:**
- Consumes: `css/style.css`, `images/logo.svg`, `images/elements/*.svg`
- Links to: `characters.html`, `elements.html`, `series.html`, `contact.html`

- [ ] **Step 1: Write `index.html` semantic structure**
Create `index.html` with:
- Accessible `<head>` with viewport meta, title, and stylesheet link.
- Sticky `<header>` with logo, navigation links (with `.active` on Home), and mobile checkbox toggle.
- Hero `<section class="hero">` featuring headline, synopsis, and primary CTA buttons.
- Statistics counter section (`.stats-grid`) displaying 7 Elements, 5 Core Heroes, 3 Feature Films, 100+ Episodes.
- Lore & Storyline section (`.lore-section`) explaining BoBoiBoy's origin and the TAPOPS intergalactic mission.
- Featured Highlights grid showcasing BoBoiBoy and Ochobot with direct link buttons.
- Universal `<footer>` with copyright and TAPOPS branding.

- [ ] **Step 2: Verify `index.html` markup and local link integrity**
Check that all internal anchor tags (`href="index.html"`, `href="characters.html"`, etc.) point to existing or planned files.

- [ ] **Step 3: Commit**
```bash
git add index.html
git commit -m "feat: add index.html home page"
```

---

### Task 3: Page 2 — Characters (`characters.html`)

**Files:**
- Create: `characters.html`

**Interfaces:**
- Consumes: `css/style.css`, `images/logo.svg`
- Produces: 6 hero character cards with CSS stat bars and 2 mentor spotlight cards.

- [ ] **Step 1: Write `characters.html` markup**
Create `characters.html` with:
- Navigation bar with `.active` class on "Characters".
- Page header banner: *"The Galactic Heroes of TAPOPS"*.
- Character Grid (`.character-grid`):
  1. BoBoiBoy (Elemental Leader)
  2. Yaya (Gravity Manipulation)
  3. Ying (Time Acceleration)
  4. Gopal (Molecule Manipulation)
  5. Fang (Shadow Manipulation)
  6. Ochobot (Power Sphera Gen 9)
  Each card includes an avatar badge, role pill, bio, and 4 CSS progress bars (Power, Agility, Defense, Intelligence).
- Mentors & Allies section featuring Tok Aba (Kokotiam master) and Papa Zola (Justice Cadet teacher).
- Universal footer.

- [ ] **Step 2: Verify layout and styling rendering**
Verify that all character cards render cleanly and that the active navigation state points to `characters.html`.

- [ ] **Step 3: Commit**
```bash
git add characters.html
git commit -m "feat: add characters.html hero showcase page"
```

---

### Task 4: Page 3 — Elemental Powers (`elements.html`)

**Files:**
- Create: `elements.html`

**Interfaces:**
- Consumes: `css/style.css`, `images/logo.svg`, `images/elements/*.svg`
- Produces: 7 Elemental cards with tier evolutions and 4 Fusion Power cards.

- [ ] **Step 1: Write `elements.html` markup**
Create `elements.html` with:
- Navigation bar with `.active` class on "Elements".
- Page header banner: *"Mastering the 7 Elemental Powers"*.
- Overview of the 3 Elemental Tiers (Tier 1 Base, Tier 2 Advanced, Tier 3 Fusion/Mastery).
- 7 Elemental Power Cards with colored glow borders and icons:
  1. Lightning -> Thunderstorm (Halilintar)
  2. Wind -> Cyclone (Taufan)
  3. Earth -> Earthquake (Gempa)
  4. Fire -> Blaze
  5. Water -> Ice (Ais)
  6. Leaf -> Thorn (Duri)
  7. Light -> Solar
- Elemental Fusions Showcase section: FrostFire, Glacier, Supra, and SORI.
- Universal footer.

- [ ] **Step 2: Verify elements grid markup and CSS integration**
Check element card borders, glow gradients, and typography.

- [ ] **Step 3: Commit**
```bash
git add elements.html
git commit -m "feat: add elements.html power showcase page"
```

---

### Task 5: Page 4 — Series & Movies (`series.html`)

**Files:**
- Create: `series.html`

**Interfaces:**
- Consumes: `css/style.css`, `images/logo.svg`
- Produces: 5 chronicle media cards arranged in chronological release order.

- [ ] **Step 1: Write `series.html` markup**
Create `series.html` with:
- Navigation bar with `.active` class on "Series & Movies".
- Page header banner: *"The Complete BoBoiBoy Chronicles"*.
- Timeline & Media cards:
  1. *BoBoiBoy Classic (2011–2016)* — Seasons 1–3
  2. *BoBoiBoy: The Movie (2016)* — The Floating Island & Klamkabot
  3. *BoBoiBoy Galaxy Season 1 (2016–2018)* — The TAPOPS Space Odyssey
  4. *BoBoiBoy Movie 2 (2019)* — The Wrath of Retak'ka
  5. *BoBoiBoy Galaxy Season 2 (2023+)* — SORI & Windara Arcs
- Each card includes release year, episode/runtime badge, storyline summary, main villains, and rating tags.
- Universal footer.

- [ ] **Step 2: Verify timeline and media card styling**
Ensure timeline cards are visually aligned and responsive.

- [ ] **Step 3: Commit**
```bash
git add series.html
git commit -m "feat: add series.html chronicle and movie timeline page"
```

---

### Task 6: Page 5 — Fan Hub & Student Profile (`contact.html`)

**Files:**
- Create: `contact.html`

**Interfaces:**
- Consumes: `css/style.css`, `images/logo.svg`
- Produces: Interactive Cadet Enlistment form, Student Submission profile card, and pure CSS FAQ accordion.

- [ ] **Step 1: Write `contact.html` markup**
Create `contact.html` with:
- Navigation bar with `.active` class on "Contact & Fan Hub".
- Page header banner: *"TAPOPS Space Academy Hub"*.
- Two-column layout:
  - Column 1: Cadet Recruitment / Fan Feedback form (Name, Codename, Email, Favorite Element dropdown, Message, Terms checkbox, Submit button).
  - Column 2: Student Assignment Card (Student Name, Student ID/NIM, Class, Course name, Instructor name, Submission checklist).
- Pure CSS FAQ section using `<details><summary>` with questions on BoBoiBoy history, Monsta Studios, and Power Spheras.
- Universal footer.

- [ ] **Step 2: Verify form controls, states, and accordion interactions**
Ensure input focus states, button hover effects, and `<details>` toggle behaviors work seamlessly.

- [ ] **Step 3: Commit**
```bash
git add contact.html
git commit -m "feat: add contact.html fan hub and student profile page"
```

---

### Task 7: Cross-Page Navigation Verification & Automated HTML/CSS Validation

**Files:**
- Test / Verify: All 5 HTML files and `css/style.css`

- [ ] **Step 1: Run link checker script**
Execute a PowerShell command to verify that all relative links (`href`) across all 5 HTML files resolve to real files without 404s.

- [ ] **Step 2: Run semantic tag and image alt audit**
Audit all HTML files to ensure every `<img>` has an `alt` attribute and all semantic tags are properly closed.

- [ ] **Step 3: Final Commit and Documentation update**
Commit all verified files with a final summary.
```bash
git add .
git commit -m "chore: complete and verify all 5 pages of boboiboy website"
```

# Design Specification: BoBoiBoy 5-Page Website (Pure HTML & CSS)

- **Date:** 2026-10-16
- **Status:** Approved
- **Topic:** 5-Page Fan Portal & Academic Assignment Website about BoBoiBoy
- **Technology Stack:** Pure HTML5 & CSS3 (Zero external JS, Zero CSS frameworks, 100% responsive Flexbox & CSS Grid)
- **Language:** English

---

## 1. Project Overview & Objectives

The goal of this project is to build an interactive, visually stunning, multi-page website dedicated to the Malaysian animated superhero franchise **BoBoiBoy** (created by Animonsta Studios). The website is tailored for an academic school/college assignment, emphasizing:
- Semantic HTML5 markup (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`, `<figcaption>`).
- Modern CSS3 architecture using custom properties (`var(--token)`), Flexbox, CSS Grid, animations, and transitions.
- 100% responsive design across Mobile, Tablet, and Desktop screens.
- Zero dependencies: runs locally out of the box simply by opening `index.html` in any web browser.

---

## 2. Directory Structure

```
boboiboy-universe/
├── index.html                  # 1. Home / Overview
├── characters.html             # 2. Characters / TAPOPS Heroes
├── elements.html               # 3. 7 Elemental Powers & Fusions
├── series.html                 # 4. Chronicles, Series & Movies
├── contact.html                # 5. Cadet Fan Hub & Student Profile
├── css/
│   └── style.css               # Unified, modular CSS stylesheet
├── images/                     # Visual assets (SVGs and curated web images)
│   ├── logo.svg
│   ├── hero-bg.svg
│   ├── boboiboy.png
│   ├── yaya.png
│   ├── ying.png
│   ├── gopal.png
│   ├── fang.png
│   ├── ochobot.png
│   ├── tok-aba.png
│   ├── papa-zola.png
│   ├── elements/               # Element badges / SVG icons
│   │   ├── lightning.svg
│   │   ├── wind.svg
│   │   ├── earth.svg
│   │   ├── fire.svg
│   │   ├── water.svg
│   │   ├── leaf.svg
│   │   └── light.svg
│   └── series/                 # Movie/series poster images
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-10-16-boboiboy-website-design.md
```

---

## 3. Page Specifications

### Page 1: `index.html` (Home)
- **Header & Navigation:** Sticky top navigation with Logo, 5 page links with active indicator for Home, and a pure CSS mobile hamburger menu toggle.
- **Hero Section:**
  - High-impact headline: *"Defend the Galaxy with Elemental Powers"*
  - Subtitle explaining BoBoiBoy's journey from Rintis Island to the cosmic TAPOPS organization.
  - Call to Action (CTA) buttons: *"Meet The Heroes"* (links to `characters.html`) and *"Discover Elements"* (links to `elements.html`).
- **Core Statistics Strip:** 4-column responsive grid showcasing:
  - 7 Elemental Powers
  - 5 Core Heroes
  - 3 Feature Films
  - 100+ Galactic Episodes
- **Lore & Synopsis Section:**
  - Origin story: How Ochobot granted BoBoiBoy elemental superpowers.
  - The Mission: TAPOPS (Tracker and Protector of Power Spheras) safeguarding ancient artifacts from cosmic warlords like Adu Du, Borara, and Retak'ka.
- **Featured Highlights:**
  - Split cards previewing BoBoiBoy's leadership and Ochobot's teleportation abilities.
- **Footer:** Universal footer with TAPOPS branding, quick links, "Terbaik!" quote badge, and Monsta attribution.

### Page 2: `characters.html` (Heroes of TAPOPS)
- **Header Banner:** *"Meet The Galactic Heroes of TAPOPS"*
- **Character Grid:** Responsive CSS Grid displaying 6 major hero cards:
  1. **BoBoiBoy:** Elemental Hero & Leader (Powers: 7 Elements, Split Clone).
  2. **Yaya:** Gravity Manipulation & Superhuman Strength.
  3. **Ying:** Time Acceleration & Super Speed.
  4. **Gopal:** Molecular Manipulation (Food Transmutation & Shield).
  5. **Fang:** Shadow Manipulation & Combat Strategist.
  6. **Ochobot:** Generation 9 Power Sphera (Teleportation & Power Giver).
- **Card Components:**
  - Character portrait / avatar.
  - Role badge and elemental alignment.
  - Bio description.
  - CSS Power Meter bars (Power, Agility, Defense, Intelligence).
- **Mentors & Allies Section:**
  - Tok Aba (Grandfather & Cocoa Master at Tok Aba's Kokotiam).
  - Papa Zola (Heroic School Teacher & Galactic Cadet Instructor).

### Page 3: `elements.html` (The 7 Elemental Powers)
- **Header Banner:** *"Mastering The 7 Elemental Powers"*
- **Elemental Evolution Explanation:**
  - Tier 1: Base Element (e.g. Petir / Lightning).
  - Tier 2: Advanced Form (e.g. Halilintar / Thunderstorm).
  - Tier 3: Elemental Mastery & Fusion Forms.
- **7 Elemental Cards Grid:**
  - **Lightning / Thunderstorm:** Signature yellow-gold glow, rapid dual thunder blades.
  - **Wind / Cyclone:** Sky blue cyan glow, wind hoverboard and cyclone drills.
  - **Earth / Earthquake:** Amber brown glow, seismic earth fists and golem control.
  - **Fire / Blaze:** Crimson red glow, blazing chakrams and explosive combat.
  - **Water / Ice:** Deep frost blue glow, glacial bow and ice shield.
  - **Leaf / Thorn:** Vibrant emerald glow, thorn whips and rapid ivy vines.
  - **Light / Solar:** Brilliant solar gold glow, solar laser eclipse and pure light energy.
- **Elemental Fusion Showcase:**
  - FrostFire (Fire + Ice)
  - Glacier (Earth + Ice)
  - Supra (Thunderstorm + Solar)
  - SORI (Solar + Thorn)

### Page 4: `series.html` (Chronicles & Movie Releases)
- **Header Banner:** *"The Complete BoBoiBoy Chronicles"*
- **Timeline / Release Showcase:**
  1. **BoBoiBoy Classic (2011–2016):** Seasons 1–3 on Earth defending Rintis Island against Adu Du and Probe.
  2. **BoBoiBoy: The Movie (2016):** The theatrical breakthrough rescuing Klamkabot from the Tengkotak gang on floating island.
  3. **BoBoiBoy Galaxy Season 1 (2016–2018):** Space expedition arc with Commander Koko Ci and TAPOPS.
  4. **BoBoiBoy Movie 2 (2019):** Galactic war against ancient elemental master Retak'ka.
  5. **BoBoiBoy Galaxy Season 2 (2023+):** Windara, Gentar, and the search for original elemental spheres.
- **Media Card Features:** Poster image, release year tag, runtime/episodes, storyline premise, primary antagonists, and audience reception ratings.

### Page 5: `contact.html` (TAPOPS Academy Fan Hub & Student Profile)
- **Header Banner:** *"TAPOPS Space Academy Hub"*
- **Two-Column Layout:**
  - **Column 1: Cadet Recruitment & Fan Feedback Form**
    - Input: Full Name & Cadet Codename
    - Input: Email address
    - Select: Favorite Element (Lightning, Wind, Earth, Fire, Water, Leaf, Light)
    - Textarea: Message / Fan Theory / Feedback
    - Checkbox: "Agree to follow the TAPOPS Cadet Code of Honor"
    - Submit Button: *"Submit Cadet Enlistment"* (Pure CSS hover & focus states)
  - **Column 2: Student / Author Submission Profile**
    - Student Name, Student ID (NIM), Class/Group, Course Name (Web Development / Pemrograman Web), Submission Date.
    - Assignment notes & technology compliance checklist.
- **FAQ Section:**
  - Interactive pure CSS `<details><summary>` accordion covering frequently asked questions about the BoBoiBoy franchise.

---

## 4. Visual Design & CSS Architecture (`css/style.css`)

### Color Palette & Design Tokens
```css
:root {
  --bg-deep-space: #0b0f19;
  --bg-surface-dark: #131b2e;
  --bg-surface-card: #1e293b;
  --bg-surface-elevated: #283548;
  
  --primary-orange: #ff5722;
  --primary-orange-hover: #ff7043;
  --accent-amber: #f59e0b;
  
  --color-lightning: #fbbf24;
  --color-wind: #38bdf8;
  --color-earth: #d97706;
  --color-fire: #ef4444;
  --color-water: #06b6d4;
  --color-leaf: #10b981;
  --color-light: #facc15;

  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-focus: rgba(255, 87, 34, 0.6);
  
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-full: 9999px;
  
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
}
```

### Key UI Features
- **Responsive Navigation:** Fixed top navbar, brand logo with subtle glow, desktop flex menu, mobile hamburger toggle without JavaScript (CSS checkbox method).
- **Hero & Card Hover Effects:** Subtle scale transform (`transform: translateY(-5px)`), border glow matching the elemental theme.
- **Power Meters:** Custom CSS progress bars with colored gradients.
- **Pure CSS Accordion:** Custom-styled summary chevron that rotates 90 degrees when open.
- **Fully Accessible:** High contrast text ratios conforming to WCAG AA, focus-visible outlines for keyboard accessibility.

---

## 5. Verification Plan

1. **Browser Compatibility:** Check rendering across modern browsers (Chrome, Edge, Firefox, Safari).
2. **Responsive Checkpoints:**
   - Mobile: 375px & 425px
   - Tablet: 768px & 820px
   - Desktop: 1024px & 1440px
3. **HTML5 Semantic Validation:** Ensure all closing tags, alt attributes, and semantic landmarks are present and valid.
4. **Navigation Integrity:** Verify that every link in the header and footer correctly routes between all 5 pages.

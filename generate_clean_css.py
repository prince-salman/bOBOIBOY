css_content = """/* BoBoiBoy Universe - Academic Project 1 Unified Stylesheet */
:root {
  --primary-orange: #ea580c;
  --primary-orange-hover: #c2410c;
  --primary-orange-light: #fff7ed;
  --bg-main: #ffffff;
  --bg-surface: #f8fafc;
  --bg-surface-alt: #f1f5f9;
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --border-focus: #ea580c;
  --shadow-subtle: 0 2px 4px rgba(0, 0, 0, 0.05);
  --shadow-card: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
  --radius-sm: 6px;
  --radius: 10px;
  --radius-lg: 14px;
  --radius-full: 9999px;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --container-width: 1180px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 400;
  line-height: 1.6;
  color: var(--text-primary);
  background-color: var(--bg-main);
  background-image: none;
  background-repeat: no-repeat;
  background-position: center top;
  background-size: auto;
  background-attachment: scroll;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  -webkit-font-smoothing: antialiased;
}

a {
  color: var(--primary-orange);
  text-decoration: none;
  transition: color 0.15s ease;
}

a:hover {
  color: var(--primary-orange-hover);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.container {
  width: 100%;
  max-width: var(--container-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.section {
  padding-top: 3.5rem;
  padding-bottom: 3.5rem;
}

.section-alt {
  background-color: var(--bg-surface);
}

.section-header {
  text-align: center;
  max-width: 720px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2.25rem;
}

.section-title {
  font-size: 1.85rem;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.25;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.section-subtitle {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

.hero {
  padding-top: 3.5rem;
  padding-bottom: 3rem;
  background: linear-gradient(180deg, var(--bg-surface) 0%, var(--bg-main) 100%);
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 3rem;
  align-items: center;
}

.hero-content {
  display: flex;
  flex-direction: column;
}

.hero-title {
  font-size: 2.6rem;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 1rem;
  color: var(--text-primary);
  letter-spacing: -0.025em;
}

.hero-title span.highlight {
  color: var(--primary-orange);
}

.hero-subtitle {
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 1.75rem;
}

.hero-cta {
  display: flex;
  gap: 0.85rem;
  flex-wrap: wrap;
}

.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-badge-card {
  background: #ffffff;
  width: 100%;
  max-width: 320px;
  padding: 1.75rem 1.5rem;
  text-align: center;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
}

.portal-announcement-banner {
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--primary-orange);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
  box-shadow: var(--shadow-subtle);
}

.academic-topbar {
  background-color: #0f172a;
  color: #94a3b8;
  font-size: 0.75rem;
  padding: 0.45rem 0;
  border-bottom: 1px solid #1e293b;
}

.academic-topbar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.academic-topbar-left, .academic-topbar-right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.academic-pill {
  background-color: #1e293b;
  color: #f8fafc;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-weight: 700;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.site-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background-color: #ffffff;
  border-bottom: 1px solid var(--border-color);
  height: 68px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
}

.header-container, .nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.brand-link, .nav-brand {
  display: flex;
  align-items: center;
}

.brand-logo {
  height: 36px;
  width: auto;
}

.nav-menu {
  display: flex;
  align-items: center;
}

.nav-list {
  display: flex;
  list-style: none;
  gap: 0.35rem;
  align-items: center;
}

.nav-link {
  padding: 0.45rem 0.85rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-secondary);
  border-radius: var(--radius-sm);
  transition: all 0.15s ease;
}

.nav-link:hover, .nav-link.active {
  color: var(--primary-orange);
  background-color: var(--primary-orange-light);
}

.nav-toggle-input, .nav-toggle-btn {
  display: none;
}

.hamburger-bar {
  display: block;
  width: 20px;
  height: 2px;
  background-color: var(--text-primary);
  margin: 4px 0;
  border-radius: 2px;
}

.main-frame-container {
  position: relative;
  width: 100%;
  height: calc(100vh - 68px - 28px);
  min-height: 650px;
}

.master-iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.6rem 1.25rem;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-primary {
  background-color: var(--primary-orange);
  color: #ffffff;
}

.btn-primary:hover {
  background-color: var(--primary-orange-hover);
  color: #ffffff;
}

.btn-secondary {
  background-color: #ffffff;
  color: var(--text-primary);
  border-color: var(--border-color);
}

.btn-secondary:hover {
  background-color: var(--bg-surface-alt);
  color: var(--text-primary);
}

.btn-lg {
  padding: 0.75rem 1.6rem;
  font-size: 1rem;
}

.stats-strip, .stats-section {
  padding: 1.5rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.stat-card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 1.25rem 1rem;
  text-align: center;
  box-shadow: var(--shadow-subtle);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}

.stat-number {
  font-size: 2.25rem;
  font-weight: 800;
  color: var(--primary-orange);
  line-height: 1.1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow-subtle);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}

.card-title {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: var(--text-primary);
}

.glow-lightning { border-top: 3px solid #d97706; }
.glow-wind { border-top: 3px solid #0284c7; }
.glow-earth { border-top: 3px solid #b45309; }
.glow-fire { border-top: 3px solid #dc2626; }
.glow-water { border-top: 3px solid #0891b2; }
.glow-leaf { border-top: 3px solid #059669; }
.glow-light { border-top: 3px solid #ca8a04; }

.character-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.character-card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.character-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
}

.character-avatar-wrap {
  width: 84px;
  height: 84px;
  border-radius: var(--radius-full);
  margin: 0 auto 1rem auto;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.12);
  border: 3px solid #ffffff;
}

.character-avatar {
  width: 74px;
  height: 74px;
  object-fit: contain;
}

.character-header {
  text-align: center;
  margin-bottom: 0.75rem;
}

.character-name {
  font-size: 1.3rem;
  font-weight: 800;
  margin: 0.2rem 0;
  letter-spacing: -0.01em;
}

.character-alias {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
}

.character-bio {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.55;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}

.stat-group {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 0.75rem 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  margin-top: auto;
}

.stat-row {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: 0.8rem;
}

.stat-name {
  width: 46px;
  font-weight: 700;
  color: var(--text-secondary);
  text-transform: uppercase;
  font-size: 0.725rem;
  letter-spacing: 0.04em;
}

.stat-bar {
  flex: 1;
  height: 8px;
  background-color: #e2e8f0;
  border-radius: var(--radius-full);
  overflow: hidden;
}

.stat-fill {
  height: 100%;
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}

.fill-power {
  background: linear-gradient(90deg, #ea580c, #dc2626);
}

.fill-agility {
  background: linear-gradient(90deg, #0284c7, #06b6d4);
}

.stat-value {
  width: 32px;
  text-align: right;
  font-weight: 800;
  color: var(--text-primary);
  font-size: 0.75rem;
}

.elements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.25rem;
}

.element-card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 1.25rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.element-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}

.element-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.element-icon-wrap {
  width: 54px;
  height: 54px;
  border-radius: 10px;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
}

.element-name {
  font-size: 1.05rem;
  font-weight: 800;
  margin-bottom: 0.35rem;
}

.card-footer {
  margin-top: auto;
  padding-top: 0.6rem;
  border-top: 1px dashed var(--border-color);
}

.badge {
  display: inline-block;
  font-size: 0.725rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  background-color: var(--bg-surface-alt);
  color: var(--text-secondary);
}

.badge-fire { background-color: #fee2e2; color: #dc2626; }
.badge-wind { background-color: #e0f2fe; color: #0284c7; }
.badge-earth { background-color: #fef3c7; color: #b45309; }
.badge-lightning { background-color: #fef9c3; color: #ca8a04; }
.badge-water { background-color: #cffafe; color: #0891b2; }
.badge-leaf { background-color: #d1fae5; color: #059669; }
.badge-light { background-color: #fef08a; color: #a16207; }

.galaxy-radio {
  display: none;
}

.galaxy-tabs {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.galaxy-tab-btn {
  padding: 0.5rem 1.25rem;
  border-radius: var(--radius-full);
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.15s ease;
}

.galaxy-tab-btn:hover {
  background-color: var(--bg-surface-alt);
  color: var(--text-primary);
}

#tab-galaxy-all:checked ~ .galaxy-tabs label[for="tab-galaxy-all"],
#tab-galaxy-s1:checked ~ .galaxy-tabs label[for="tab-galaxy-s1"],
#tab-galaxy-movie:checked ~ .galaxy-tabs label[for="tab-galaxy-movie"],
#tab-galaxy-s2:checked ~ .galaxy-tabs label[for="tab-galaxy-s2"] {
  background-color: var(--primary-orange);
  color: #ffffff;
  border-color: var(--primary-orange);
}

#tab-galaxy-s1:checked ~ .timeline .item-galaxy-movie,
#tab-galaxy-s1:checked ~ .timeline .item-galaxy-s2,
#tab-galaxy-movie:checked ~ .timeline .item-galaxy-s1,
#tab-galaxy-movie:checked ~ .timeline .item-galaxy-s2,
#tab-galaxy-s2:checked ~ .timeline .item-galaxy-s1,
#tab-galaxy-s2:checked ~ .timeline .item-galaxy-movie {
  display: none;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.timeline-item {
  position: relative;
}

.timeline-marker {
  display: none;
}

.chronicle-card {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 1.5rem;
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  align-items: center;
  padding-right: 1.5rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.chronicle-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}

.chronicle-banner img {
  width: 100%;
  height: 100%;
  min-height: 170px;
  object-fit: cover;
}

.chronicle-meta {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.chronicle-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 0.4rem;
}

.chronicle-lead {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.55;
}

.watch-order-card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--primary-orange);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow-subtle);
}

.table-container {
  overflow-x: auto;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  background-color: #ffffff;
  margin-top: 1.25rem;
  margin-bottom: 1.25rem;
  box-shadow: var(--shadow-subtle);
}

table, .data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
  text-align: left;
}

th {
  background-color: #0f172a;
  color: #ffffff;
  padding: 0.85rem 1.15rem;
  font-weight: 700;
  font-size: 0.825rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}

td {
  padding: 0.85rem 1.15rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
}

tr:nth-child(even) td {
  background-color: var(--bg-surface);
}

tr:hover td {
  background-color: #fff7ed;
}

.cadet-form {
  margin-top: 1rem;
}

.form-group {
  margin-bottom: 1.15rem;
}

.form-label {
  display: block;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
  color: var(--text-primary);
}

.required {
  color: #dc2626;
}

.form-input, .form-textarea, .form-select {
  width: 100%;
  padding: 0.65rem 0.85rem;
  font-size: 0.9rem;
  border: 1.5px solid var(--border-color);
  border-radius: var(--radius-sm);
  background-color: #ffffff;
  color: var(--text-primary);
  font-family: inherit;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.form-input:focus, .form-textarea:focus, .form-select:focus {
  outline: none;
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(234, 88, 12, 0.15);
}

.form-radio-group {
  display: flex;
  gap: 1.25rem;
  margin-top: 0.35rem;
}

.form-radio-wrap, .form-checkbox-wrap {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--text-secondary);
  cursor: pointer;
}

.form-radio-label, .form-checkbox-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  cursor: pointer;
}

.form-radio, .form-checkbox {
  accent-color: var(--primary-orange);
  width: 1.05rem;
  height: 1.05rem;
  cursor: pointer;
}

.student-card {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  box-shadow: var(--shadow-subtle);
}

.student-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.25rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.student-avatar-badge {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ea580c, #c2410c);
  color: #ffffff;
  font-weight: 800;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(234, 88, 12, 0.25);
}

.student-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.25rem;
  font-size: 0.875rem;
}

.student-table td {
  padding: 0.55rem 0.65rem;
  border-bottom: 1px solid var(--border-color);
}

.student-table td.label {
  font-weight: 700;
  color: var(--text-muted);
  width: 36%;
}

.student-table td.value {
  color: var(--text-primary);
  font-weight: 600;
}

.checklist-list, .compliance-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.checklist-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.faq-item {
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
}

.faq-question {
  padding: 1rem 1.25rem;
  font-weight: 700;
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--text-primary);
  user-select: none;
  font-size: 0.95rem;
}

.faq-question::-webkit-details-marker {
  display: none;
}

.faq-question::after {
  content: '+';
  font-size: 1.2rem;
  color: var(--primary-orange);
  font-weight: 700;
}

details[open] .faq-question::after {
  content: '\\2013';
}

.faq-answer {
  padding: 0 1.25rem 1rem 1.25rem;
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.6;
  border-top: 1px dashed var(--border-color);
  padding-top: 0.75rem;
}

.site-footer {
  background-color: #ffffff;
  border-top: 1px solid var(--border-color);
  padding-top: 2.75rem;
  padding-bottom: 2rem;
  margin-top: auto;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.footer-col-title {
  font-size: 0.875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
  margin-bottom: 0.85rem;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}

.footer-link {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.footer-link:hover {
  color: var(--primary-orange);
}

.footer-quote {
  background-color: var(--bg-surface);
  border-left: 3px solid var(--primary-orange);
  padding: 0.85rem 1rem;
  border-radius: 4px;
}

.quote-text {
  font-style: italic;
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.25rem;
}

.quote-author {
  font-size: 0.775rem;
  font-weight: 700;
  color: var(--primary-orange);
}

.footer-bottom {
  border-top: 1px solid var(--border-color);
  padding-top: 1.25rem;
  text-align: center;
  font-size: 0.8rem;
  color: var(--text-muted);
}

.flex { display: flex; }
.flex-between { justify-content: space-between; }
.flex-center { justify-content: center; }
.items-center, .align-center { align-items: center; }
.flex-wrap { flex-wrap: wrap; }
.text-center { text-align: center; }
.text-orange { color: var(--primary-orange); }
.text-secondary { color: var(--text-secondary); }
.text-muted { color: var(--text-muted); }
.text-xs { font-size: 0.8rem; }

.text-amber { color: #d97706; }
.text-lightning { color: #ca8a04; }
.text-wind { color: #0284c7; }
.text-earth { color: #b45309; }
.text-fire { color: #dc2626; }
.text-water { color: #0891b2; }
.text-leaf { color: #059669; }
.text-light { color: #ca8a04; }

.gap-1 { gap: 0.5rem; }
.gap-2 { gap: 1rem; }
.mb-1 { margin-bottom: 0.25rem; }
.mb-2 { margin-bottom: 0.5rem; }
.mb-3 { margin-bottom: 1rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-3 { margin-top: 1rem; }

@media (max-width: 992px) {
  .hero-grid { grid-template-columns: 1fr; text-align: center; gap: 2rem; }
  .hero-cta { justify-content: center; }
  .character-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .grid-4 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: 1fr; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .chronicle-card { grid-template-columns: 1fr; padding-right: 0; }
  .chronicle-banner img { max-height: 220px; }
  .chronicle-card > div:last-child { padding: 1.25rem; }
}

@media (max-width: 768px) {
  .nav-toggle-btn {
    display: block;
    cursor: pointer;
    font-size: 1.5rem;
    color: var(--text-primary);
  }
  .nav-menu {
    display: none;
    position: absolute;
    top: 68px;
    left: 0;
    right: 0;
    background-color: #ffffff;
    border-bottom: 1px solid var(--border-color);
    padding: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }
  .nav-toggle-input:checked ~ .nav-menu {
    display: block;
  }
  .nav-list {
    flex-direction: column;
    gap: 0.25rem;
  }
  .grid-2 { grid-template-columns: 1fr; }
  .character-grid { grid-template-columns: 1fr; }
  .stats-grid { grid-template-columns: 1fr 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
  .hero-title { font-size: 2.1rem; }
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content.strip() + '\\n')

print("Wrote clean css/style.css successfully!")

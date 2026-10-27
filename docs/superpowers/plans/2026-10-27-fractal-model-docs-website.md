# TTrades Fractal Model GitHub Pages Documentation Website Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a comprehensive, light-themed GitHub Pages (`github.io`) documentation website for the TTrades Fractal Model and Pine Script indicator repository, styled identically to Material for MkDocs with instant offline search, extensive guides, and real high-resolution chart images for every entry model and indicator setup.

**Architecture:** Use Material for MkDocs (`mkdocs-material`) with a clean light palette (`scheme: default, primary: indigo, accent: indigo`), full-text client-side search plugin, rich markdown extensions (admonitions, tabs, code copy, math), automated GitHub Pages deployment workflow (`.github/workflows/deploy.yml`), and structured documentation directories with real visual charts for entry models 1-4 and TradingView indicators.

**Tech Stack:** Python 3.13, MkDocs 1.6+, Material for MkDocs 9.5+, GitHub Actions (`gh-deploy`), Pillow / SVG graphics, Pine Script v6.

**Spec:** User request specifying a light-mode documentation website like `https://metsehafe-eyasu.github.io/interview-prep/`, with search, extensive guides, plenty of examples, and real visual images illustrating the indicator and entry models.

## Global Constraints
- Light mode by default (`data-md-color-scheme="default"`).
- Offline client-side search must be fully enabled and indexed across all pages.
- Must include real visual images (charts, indicator screenshots, setup dialogs) — no plain ASCII representations.
- All Pine Script code snippets and indicators must strictly adhere to `//@version=6`.
- Clean repository structure ready for GitHub Pages hosting (`gh-pages` branch or GitHub Actions workflow).

## Review Focus
- Search functionality indexing all models, concepts (C1-C4, CISD, T-Spot, SMT), and indicators.
- Image assets correctly referenced with relative links so they render locally and on GitHub Pages.
- Visual clarity of Entry Model 1 (CISD Close), Model 2 (T-Spot Limit), Model 3 (Micro CISD), Model 4 (C4 Continuation).
- Accurate TradingView alert dialog and indicator inputs documentation with real visuals.
- Build test: `mkdocs build --strict` exits with 0 warnings/errors.

---

### Task 1: Environment Setup & MkDocs Material Configuration
**Files:**
- Create: `mkdocs.yml`
- Create: `.github/workflows/deploy.yml`
- Create: `requirements.txt`

**Interfaces:**
- Produces: Base configuration for Material for MkDocs theme, search plugin, navigation structure, and CI/CD workflow.

- [ ] **Step 1: Verify MkDocs and mkdocs-material installation**
- [ ] **Step 2: Create `requirements.txt` with mkdocs and mkdocs-material**
- [ ] **Step 3: Create `mkdocs.yml` with light mode palette, search, admonitions, and nav structure**
- [ ] **Step 4: Create `.github/workflows/deploy.yml` for automated GitHub Pages deployment**

---

### Task 2: Visual Assets & Image Architecture
**Files:**
- Create: `docs/assets/images/charts/`
- Create: `docs/assets/images/models/`
- Create: `docs/assets/images/indicator/`
- Script: `scripts/generate_model_visuals.py` (generates high-resolution annotated chart visuals for Models 1-4, C1-C4 sequence, SMT divergence)

**Interfaces:**
- Consumes: User uploaded authentic TradingView indicator screenshots and ICT fractal mechanics.
- Produces: Dedicated high-resolution chart PNGs for every model and indicator component:
  - `model1_cisd_breakout.png`
  - `model2_tspot_limit.png`
  - `model3_micro_cisd.png`
  - `model4_c4_continuation.png`
  - `fractal_c1_c4_cycle.png`
  - `tradingview_alert_setup.png`
  - `tradingview_indicator_chart.png`

- [ ] **Step 1: Copy authentic user TradingView screenshots into `docs/assets/images/`**
- [ ] **Step 2: Generate dedicated high-res chart graphics for all 4 entry models**
- [ ] **Step 3: Generate visual diagram for the C1-C2-C3-C4 fractal sequence & T-Spot**
- [ ] **Step 4: Verify all images exist and are non-corrupt**

---

### Task 3: Content Migration, Landing Page & Architecture
**Files:**
- Create: `docs/index.md`
- Create: `docs/curriculum/01_foundational_concepts.md`
- Create: `docs/curriculum/02_fractal_sequence.md`
- Create: `docs/curriculum/03_cisd_deep_dive.md`
- Create: `docs/curriculum/04_poi_and_tspot.md`
- Create: `docs/curriculum/05_timeframe_alignment.md`
- Create: `docs/curriculum/06_entry_models.md`
- Create: `docs/curriculum/07_risk_and_targets.md`
- Create: `docs/curriculum/08_indicator_guide.md`
- Create: `docs/indicators/fractal_model.md`
- Create: `docs/indicators/htf_suite.md`
- Create: `docs/cheatsheet/sessions_and_rules.md`

**Interfaces:**
- Consumes: Markdown documentation from `docs/ttrades_fractal_model/` and pine indicators from `scripts/indicators/`.
- Produces: Enriched documentation pages with Material MkDocs admonitions (`!!! note`, `!!! tip`, `!!! example`), embedded images, and deep cross-links.

- [ ] **Step 1: Create `docs/index.md` with landing page, features matrix, and quick navigation**
- [ ] **Step 2: Enrich `06_entry_models.md` with dedicated sections and real image embeds for Models 1-4**
- [ ] **Step 3: Enrich `08_indicator_guide.md` with alert setup screenshots, indicator input tables, and troubleshooting**
- [ ] **Step 4: Create indicator reference pages with copyable Pine Script v6 code blocks**
- [ ] **Step 5: Create quick-reference cheatsheet page for sessions and DST time shifts**

---

### Task 4: Local Build, Search Indexing & Verification
**Files:**
- Directory: `site/` (generated build)

**Interfaces:**
- Consumes: Complete `docs/` tree and `mkdocs.yml`.
- Produces: Production-ready static website in `site/`.

- [ ] **Step 1: Run `mkdocs build --strict` to verify zero broken links and valid search indexing**
- [ ] **Step 2: Launch `mkdocs serve` or inspect generated static HTML files**
- [ ] **Step 3: Verify search functionality with terms like "CISD", "Model 2", "T-Spot", "DST", "Alerts"**
- [ ] **Step 4: Verify image rendering on light theme**
- [ ] **Step 5: Commit changes to git**

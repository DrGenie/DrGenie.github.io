# Changelog

## Redesign pass (July 2026)

### Accuracy corrections (single source of truth)
- Corrected the University of Bologna MSc year from 2025 to **2015** in the CV page, the LaTeX CV, and recompiled the PDF; the About page and Person structured data use 2015.
- Set the current position to **Continuing Senior Lecturer in Health Economics** on the homepage, About page, CV (page and PDF), and Person structured data.
- Consolidated teaching records into one entry per course (ECON3011, ECON2112, ECON3111) with roles and periods, removing duplication.
- Created a single source of truth under `data/` (profile, service, grants, teaching, supervision, tools, talks) and `_variables.yml` for scalar facts.

### New pages
- About (canonical biography, career timeline, selected service, expertise, prospective-student guidance).
- Grants and funding (five verified records, grouped by type; institutional allocation and full programme total reported separately for MandEval; currencies flagged where unconfirmed).
- Research supervision (current and completed, no student names; principal vs co-supervision explained; supervision philosophy and prospective-student guidance).
- Talks & Media (privacy-enhanced, click-to-load webinar embed with accessible controls and a text link).
- Contact (email, collaboration areas, verified profile links).
- Tools hub and three detailed tool pages (eMANDEVAL, SOIL CRC Benefit-Cost Analysis Tool, STEPS FETP Scale-up Decision Aid) with problem, users, inputs, outputs, method, developer, and limitations.
- Behavioural economics teaching resources, with clean PDF previews and slide thumbnails for Lecture 1 (Foundations and Rational Choice under Certainty) and Lecture 6 (Advanced Choice under Risk and Uncertainty). "Uncertainty" spelling used in all site titles and metadata.
- Blog editorial calendar.

### Blog
- Added six cornerstone articles: the certainty effect; probability weighting (insurance and lottery tickets); loss aversion in health and policy; risk versus ambiguity; the Allais paradox; the Ellsberg paradox. Each gives the benchmark, then the behaviour, distinguishes description from prescription, includes a worked example where useful, links to related resources, and lists key references.

### Navigation and structure
- Rebuilt the navigation into a concise set with dropdowns: Home, About, Research (areas, grants, conferences), Publications, Tools, Teaching & Supervision (teaching, resources, supervision), Talks & Media, Blog, CV, Contact.
- Added homepage sections for the featured webinar, teaching and supervision, and latest writing, and a link to the contact page.

### Structured data
- Person structured data corrected (job title, alumni, sameAs).
- Course structured data for the three public courses.
- SoftwareApplication structured data for the three tools.
- VideoObject for the webinar deliberately omitted pending verified title, publication date, and duration (see verification list).

### Assets and hygiene
- Removed exposure of the CV LaTeX source; only the PDF is published.
- Lecture LaTeX source is not published; only compiled PDF previews and thumbnails are included.

## Phase 2 refinement (July 2026)

### Restraint and information architecture
- Reduced primary navigation to seven items; CV as utility link, Contact in footer; Grants under Research/CV; Conferences, Blog, and Talks consolidated into Writing & Talks.
- Rebuilt the homepage into seven calm sections; removed the metric strip (including "countries of appointment" and empty citation/h-index tiles), the tool card grid, the repeated publication grid, the embedded homepage video player, and the hero social row.
- Concise footer without repeated navigation.

### Credibility corrections
- Removed all public verification notes across grants, supervision, talks, and tools.
- Grants: kept only verified amounts (MandEval A$ figures); amounts with unverified currency omitted from public pages and kept in the private verification list.
- Supervision: two MPhil records moved from "Completed" to a neutral "Recorded supervision" group.
- Webinar presented as a click-out link with no fabricated title or public hedge; VideoObject withheld pending verified metadata.

### New scholarly pages
- Five project pages and six flagship publication pages (verified citations and DOIs, honest framing, ScholarlyArticle structured data, no invented findings).
- Research impact and Data & code pages.
- Writing & Talks hub.

### Blog
- Reduced to six canonical categories; retired the placeholder post.

### Structured data and accessibility
- Breadcrumbs on interior pages; ScholarlyArticle on flagship papers; Course and SoftwareApplication retained.
- Alt text verified on all images; single H1 per page; unique titles and descriptions.

### Validation
- Extended `scripts/validate.py` (alt text, verification-note detection, navigation size); **0 issues** across 43 pages.

## Build-fix and World Bank identity pass (July 2026)
- Fixed the corrupted YAML front matter in blog/posts/the-benchmark-before-bias that was failing the Quarto render, and restored the post's categories.
- Applied the World Bank visual identity: Open Sans web typeface (with system fallback), World Bank blue/cyan/gold palette (navy #002244, blue #0071BC, cyan #009FDA, gold #FDB714), heavier navy headings with an accent rule, solid-blue primary buttons, and a gold masthead ribbon.
- Verified the whole project renders cleanly: 44 pages, 0 YAML errors, 0 broken internal links, all render-list files present, all JSON-LD valid.
- Provided a stale-file cleanup list to remove leftover files from earlier versions that uploads never deleted.

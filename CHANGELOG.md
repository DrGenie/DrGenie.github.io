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

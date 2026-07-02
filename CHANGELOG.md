# Changelog

## 2026-07-02 — Minimal, credibility-first refinement

- Simplified the top navigation into seven concise groups.
- Rebuilt the homepage with fewer visual cards and a clearer reading sequence.
- Reduced the portrait size and removed decorative status elements.
- Replaced card-heavy research, teaching, tools and supervision layouts with restrained lists.
- Removed the unpublished STEPS placeholder from the live site while retaining the verified World Bank FETP project.
- Generated publication counts, recent publications and the full searchable publication list from `assets/data/publications.json`.
- Collapsed older publication years by default to reduce page length.
- Removed generic featured-publication pages that did not contain verified summaries.
- Removed the editorial calendar from the public blog and retained it as an internal report.
- Fixed malformed blog-category metadata.
- Added a validation step before every Quarto render.
- Retained all verified content, DOI links, live tools, teaching resources, supervision records, webinar, CV and structured metadata.
## 2026-07-02 — GitHub Pages render-path correction

- Corrected the Publications page include path from `assets/generated/publications-list.html` to `../assets/generated/publications-list.html`, because Quarto resolves include directives relative to the current `.qmd` file.
- Extended source validation to check every Quarto include target relative to its page, preventing this deployment error from recurring.


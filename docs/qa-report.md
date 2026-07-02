# QA report

This project was prepared in an environment **without a Quarto runtime, headless browser, or npm**. That means a live render, Lighthouse, axe/pa11y, and cross-browser testing could not be run here. To avoid reporting numbers that were not measured, this report separates checks that were actually run from checks you must run in a full environment. No performance or accessibility scores are claimed.

## Checks run here (static, from source)
Run via `python3 scripts/validate.py`. Result on the delivered source: **0 issues** across 31 pages.
- Every page has a title and meta description.
- Single H1 per page (index pages).
- No duplicate page titles.
- No "Uncertainity" typo in site source; no em or en dashes in prose.
- All internal links resolve to an existing page or asset.
- All `data/*.yml`, `_variables.yml`, `_quarto.yml`, and `assets/*.json` parse.
- All embedded JSON-LD blocks parse (Person, Course, SoftwareApplication).
- Bologna MSc year is 2015 everywhere; homepage uses "Continuing Senior Lecturer".
- `publications.json` parses; 90 DOI-like strings pass a syntax check.

Additionally verified by hand:
- CV LaTeX compiles to a 7-page PDF (xelatex); Week 1 lecture compiles to a 100-page PDF; thumbnails render real slides.

## Checks you must run in a full environment
Install Quarto (https://quarto.org) and run from the repository root:

```
quarto render
```

Then, on the built `_site/`:
- **Link check (external + DOIs):** `npx linkinator ./_site --recurse --silent` (or `lychee`).
- **Structured data:** paste each page URL into Google's Rich Results Test and validator.schema.org.
- **Accessibility:** `npx pa11y-ci` or the axe DevTools browser extension, on Home, Research, Publications, Tools, Teaching & Supervision, a tool page, a blog post, and the Talks page. Target WCAG 2.2 AA.
- **Lighthouse:** `npx lighthouse https://<preview-url>/ --preset=desktop` and a mobile run, on the pages above. Targets in the brief: Performance ≥ 95, Accessibility 100, Best Practices 100, SEO 100; LCP < 2.5 s; CLS < 0.1; INP < 200 ms.
- **Responsive + keyboard + cross-browser:** manual spot checks at mobile/tablet/laptop/wide widths and in Chrome, Firefox, Safari, Edge; keyboard-only navigation including the menus, the publication filters, and the webinar play button.
- **404 and base URL:** confirm GitHub Pages serves the custom domain and that internal links work under the deployed base URL.

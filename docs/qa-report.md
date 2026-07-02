# QA report (Phase 2)

This environment has **no Quarto runtime, headless browser, or npm**, so a live render, Lighthouse, axe/pa11y, and cross-browser tests could not be run here. No performance or accessibility scores are claimed. Checks that were actually run are separated from checks you must run in a full environment.

## Checks run here (static, from source)
`python3 scripts/validate.py` on the delivered source: **0 issues across 43 pages**.
- Every page has a title and meta description; single H1 per page; no duplicate page titles.
- No public verification notes ("to be confirmed", "pending confirmation", etc.).
- All images have non-empty alt text.
- No em or en dashes in prose; no "Uncertainity" typo.
- All internal links resolve; all `data/*.yml`, `_quarto.yml`, and JSON parse; all JSON-LD blocks parse.
- Navigation has seven primary items.
- Bologna MSc = 2015 everywhere; homepage uses "Continuing Senior Lecturer".
- `publications.json` parses; 90 DOI-like strings pass a syntax check.

Verified by hand: CV compiles to a 7-page PDF; the Week 1 lecture compiles to a 100-page PDF; thumbnails render real slides.

## Checks you must run in a full environment
From the repository root, install Quarto and run:
```
quarto render
python3 scripts/validate.py
```
Then on the built `_site/`:
- **Links + DOIs:** `npx linkinator ./_site --recurse` (or `lychee`), and confirm each flagship DOI resolves.
- **Structured data:** Google Rich Results Test and validator.schema.org for Person, ScholarlyArticle, Course, SoftwareApplication.
- **Accessibility (WCAG 2.2 AA):** `npx pa11y-ci` or axe DevTools on Home, Research, a project page, Publications, a flagship paper, Tools, a tool page, Teaching & Supervision, Writing & Talks, a blog article. Check skip link, focus visibility, keyboard access to the menu and publication filters, and contrast.
- **Lighthouse (mobile + desktop)** on the pages above. Brief targets: Performance ≥ 95, Accessibility 100, Best Practices 100, SEO 100; LCP < 2.5 s; CLS < 0.1; INP < 200 ms.
- **Responsive, keyboard-only, and cross-browser** spot checks (Chrome, Firefox, Safari, Edge); 404 and production base-URL checks on GitHub Pages.

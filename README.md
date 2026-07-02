# mesfingenie.com

Academic website for Dr Mesfin Genie, built with [Quarto](https://quarto.org) and deployed to GitHub Pages at https://mesfingenie.com.

## Single source of truth
Verified facts live in `data/` (profile, service, grants, teaching, supervision, tools, talks) and `_variables.yml` (scalars such as position and the Bologna year). Update these files first; pages are authored from them so that facts do not diverge. Metrics are held in `assets/scholar-metrics.json` with a visible "last verified" date and are never scraped at build time.

## Local preview and build
```
quarto preview      # live local preview
quarto render       # full build into _site/
python3 scripts/validate.py   # static checks (titles, links, spelling, JSON-LD, facts)
```

## How to add content
- **Publication:** edit `assets/publications.json` (the count and filters are generated from it). Use a real, verified DOI.
- **Grant:** add a record to `data/grants.yml` and mirror it on `grants/index.qmd`. Never combine an institutional allocation with a whole-programme total.
- **Course:** add to `data/teaching.yml` and `teaching/index.qmd` (one entry per course).
- **Supervision:** add to `data/supervision.yml` and `supervision/index.qmd` (no student names).
- **Tool:** add to `data/tools.yml`, create `tools/<id>/index.qmd`, and add it to the render list in `_quarto.yml`.
- **Talk / webinar:** update `data/talks.yml`; for a video, add verified VideoObject metadata.
- **Blog post:** create `blog/posts/<slug>/index.qmd` with `title`, `description`, `author`, `date`, and `categories`. The listing and RSS feed update automatically.

## Metrics
To refresh Google Scholar figures safely, update `assets/scholar-metrics.json` (or run the provided GitHub Action if configured with a `SERPAPI_KEY` secret). The update must fail safely and preserve the last verified values.

## Images
Use WebP/AVIF with explicit `width`/`height`. Lecture and CV source files are kept in the repo for regeneration but are not published.

## Deployment
Set GitHub Pages **Source** to "GitHub Actions". Commit and push to `main`; the publish workflow renders and deploys. After deploy, hard-refresh and run the runtime checks in `docs/qa-report.md`. Ensure the three interactive tool folders are present in the repository root.

## Reports
See `CHANGELOG.md`, `docs/data-consistency-report.md`, `docs/page-inventory.md`, `docs/qa-report.md`, and `docs/verification-needed.md`.

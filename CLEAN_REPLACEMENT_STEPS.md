# Clean GitHub replacement steps

The replacement should be uploaded first and obsolete files deleted only after the new site deploys successfully. This avoids unnecessary downtime.

## Preserve

Do not delete either live application folder:

- `eMANDEVA-DecisionAid-V18/`
- `farming-bca-tool-v18/`

## Expected top-level repository after cleanup

- `.github/`
- `.nojekyll`
- `about/`
- `assets/`
- `blog/`
- `conferences/`
- `contact/`
- `cv/`
- `eMANDEVA-DecisionAid-V18/`
- `farming-bca-tool-v18/`
- `publications/`
- `research/`
- `scripts/`
- `supervision/`
- `talks-media/`
- `teaching/`
- `tools/`
- `_quarto.yml`
- `CHANGELOG.md`
- `CLEAN_REPLACEMENT_STEPS.md`
- `CNAME`
- `DEPLOY.md`
- `README.md`
- `index.qmd`
- `robots.txt`
- `sitemap.xml`

Delete old items such as `news/`, `projects/`, `software/`, `STEPS-FETP-DecisionAid-V20/`, `profile.jpg.README.txt`, `.github/workflows/update-scholar-metrics.yml`, `publications/featured/`, `blog/posts/editorial-calendar/`, and old root-level page files such as `about.qmd`, `research.qmd`, `publications.qmd`, `teaching.qmd`, `contact.qmd`, `cv.qmd`, `software.qmd`, `projects.qmd`, `students.qmd`, or `news.qmd` if they remain.

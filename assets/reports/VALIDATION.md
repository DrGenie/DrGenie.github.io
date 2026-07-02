# Validation report

Date: 2 July 2026

## Passed locally

- JSON parsing for profile, publications, grants, courses, supervision, talks and tools.
- YAML front-matter parsing for all Quarto pages.
- Python syntax compilation for build and validation scripts.
- JavaScript syntax validation with Node.js.
- Publication DOI-format validation.
- Duplicate publication-title and DOI checks.
- Required-file checks.
- Duplicate-H1 source scan.
- Placeholder-status scan.
- Generated-publication HTML parsing and link-attribute checks.
- Sitemap generation.

The local source validation reports 27 Quarto pages and 44 publication records.

## Authoritative render

The package includes a GitHub Actions workflow pinned to Quarto 1.9.38. The workflow generates derived content, validates the source, performs a clean Quarto render and deploys only after every preceding step passes.

A Quarto executable was not available in the artifact container, so the authoritative Quarto render occurs in GitHub Actions after upload. No claim is made here that Lighthouse was run locally.

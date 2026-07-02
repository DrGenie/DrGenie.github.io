# Mesfin Genie academic website

Complete Quarto/GitHub Pages source for `https://mesfingenie.com/`.

## Local preview

```bash
quarto preview
```

## Render

```bash
python scripts/prepare_build.py
quarto render
```

## Add content

- Publications: edit `assets/data/publications.json`.
- Grants: edit `assets/data/grants.json`.
- Courses: edit `assets/data/courses.json`.
- Supervision: edit `assets/data/supervision.json`.
- Tools: edit `assets/data/tools.json`.
- Blog posts: create `blog/posts/post-slug/index.qmd`.

## Deployment

Upload the contents of this repository to `DrGenie/DrGenie.github.io`. Keep the real application folders `eMANDEVA-DecisionAid-V18` and `farming-bca-tool-v18` in place. GitHub Actions publishes the site automatically.

## Validation

Run:

```bash
python scripts/validate_site.py
```

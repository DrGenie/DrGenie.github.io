# Mesfin Genie academic website

A restrained Quarto academic website for `mesfingenie.com`. Repeated publication metrics and publication displays are generated from the central JSON data files in `assets/data/`.

## Local commands

```bash
python scripts/prepare_build.py
python scripts/validate_site.py
quarto preview
```

## Update workflow

- Publications: edit `assets/data/publications.json`.
- Grants: edit `assets/data/grants.json`.
- Courses: edit `assets/data/courses.json`.
- Supervision: edit `assets/data/supervision.json`.
- Tools: edit `assets/data/tools.json`.
- Talks: edit `assets/data/talks.json`.
- Blog posts: add a folder under `blog/posts/` containing `index.qmd`.

The deployment workflow generates publication HTML and the sitemap, validates the repository, renders Quarto and publishes to GitHub Pages.

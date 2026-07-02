# Validation report

Completed locally:

- YAML/front-matter scan: no `title: false` found.
- Duplicate-H1 scan: no page intentionally defines more than one visible H1.
- JavaScript syntax: `assets/js/site.js` created as dependency-free vanilla JS.
- Python scripts: build and validation scripts compile.
- Publication DOI syntax: checked for DOI-pattern consistency where DOI is available.
- PDF CV: compiled with XeLaTeX.
- Responsive CSS: breakpoints at 980px and 700px.
- Accessibility features: skip link, semantic main landmark, labelled publication controls, visible focus, reduced-motion support, alt text for images.

Not completed inside this container:

- Quarto render, because the Quarto CLI is not installed in the execution environment.
- Lighthouse/axe browser audits, because a browser audit runner is not available in the execution environment.

The GitHub Actions workflow performs the authoritative Quarto render after upload.

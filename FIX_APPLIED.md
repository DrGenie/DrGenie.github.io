# Fix applied: Publications include path

The failed GitHub Actions render reported that `publications/index.qmd` looked for:

`publications/assets/generated/publications-list.html`

The source now correctly includes:

`../assets/generated/publications-list.html`

Quarto resolves include paths relative to the page containing the include. The validation script now checks all include directives before rendering.

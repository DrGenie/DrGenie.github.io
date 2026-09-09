# mesfingenie.com

Quarto site. `quarto preview` to work on it, `quarto render` to build, push to
`main` to deploy.

## Design

Inter throughout. Body scales 15.5px to 17px with the viewport, line height 1.6.
Headings 2.05 / 1.32 / 1.04rem. Palette and spacing are the seven tokens at the
top of `custom.scss`; change them and the whole site follows.

To change the typeface: the Google Fonts link in `_includes/head.html` and
`$font-family-sans-serif` in `custom.scss`. Nothing else names a family.

## Structure

```
index.qmd              home: intro, choice task, three papers, three tools
publications/          44 papers, searchable, filterable, authors collapse
research/              three strands, five projects, impact, data and code
tools/                 one page per tool, applications vendored at repo root
blog/posts/            21 posts, each with its own social preview image
about/ teaching/ supervision/ grants/ cv/ writing/ conferences/
custom.scss            the entire visual design
_includes/head.html    fonts, social metadata, Person JSON-LD
_includes/scripts.html choice task, papers search and filter, share row
assets/social/         generated preview images, 1200x630 and 1080x1080
cv/mesfin-genie-cv.tex modern CV source, pdflatex, run twice
data/*.yml             verified record behind the pages, not read at build time
```

## Adding a post

Create `blog/posts/<slug>/index.qmd` with `title`, `description`, `image`,
`author`, `date`, `categories`, and end it with a share block:

    ```{=html}
    <div class="share" data-share></div>
    ```

Then regenerate its preview images by running the snippet in
`scripts/make-social-images.py`.

## Raw HTML in a .qmd

Always fence it:

    ```{=html}
    <ul class="rec-list">...</ul>
    ```

Unfenced indented HTML is parsed as a code block and prints as visible markup.

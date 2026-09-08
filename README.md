# mesfingenie.com

Quarto site for Mesfin Genie, Senior Lecturer in Health Economics at Newcastle
Business School, The University of Newcastle. Deployed to GitHub Pages from
`main` by `.github/workflows/publish.yml`.

## Build

```
quarto preview     # local, with live reload
quarto render      # writes _site/
```

Nothing else is required. There is no data pipeline, no generation step, and no
external service. Push to `main` and the workflow renders and deploys.

## Structure

```
index.qmd                 home: intro, choice task, recent papers, tools
publications/             all 44 papers, filterable, generated once from
                          assets/publications.json and now edited directly
research/                 three strands, five project pages, impact, data and code
tools/                    one page per tool, linking to the vendored applications
about/  teaching/  supervision/  grants/  cv/  writing/  blog/
custom.scss               the entire visual design
_includes/head.html       fonts and Person JSON-LD
_includes/scripts.html    choice-task widget and papers filter
data/*.yml                verified record of grants, appointments, supervision,
                          teaching and tools. Not read at build time; kept as the
                          source of truth for the facts on the pages.
```

The three tool applications are vendored into the repository at
`eMANDEVA-DecisionAid-V18/`, `farming-bca-tool-v18/` and
`STEPS-FETP-DecisionAid-V20/`, copied from their own repositories so that
`mesfingenie.com/<tool>/` serves them. To update a tool, replace the folder
contents from the newer tool repository.

## Design

| Token | Value | Used for |
|---|---|---|
| `$paper` | `#fbfbf9` | Page background |
| `$ink` | `#16232b` | Body text |
| `$ink-strong` | `#0d171d` | Headings |
| `$muted` | `#5b6d76` | Metadata, captions, footer |
| `$rule` | `#d7dee1` | Hairlines |
| `$tint` | `#eef2f3` | Table headers, code |
| `$accent` | `#7c2233` | Links, current page, selected option |

Spectral throughout, 19px, 1.68 line height, 68-character measure. Headings run
2.45 / 1.55 / 1.16 / 1rem. Change the tokens at the top of `custom.scss` and the
whole site follows. Section comments inside that file map to page regions.

Comparable items are set as ruled rows (`.rec-list`), not cards. The homepage
choice task is the one deliberately loud element; everything else stays quiet so
it lands.

## Adding things

**A paper.** Add an `<li class="rec" data-topic="...">` block to
`publications/index.qmd`, matching the existing entries. `data-topic` takes
`preferences`, `public-health` or `other`, and the filter reads it. Optionally add
`<p class="rec-finding">` with one sentence on what the paper found.

**A blog post.** Create `blog/posts/<slug>/index.qmd` with `title`,
`description`, `author`, `date` and `categories`. The listing and RSS pick it up.

**A tool.** Create `tools/<id>/index.qmd`, add it to `render` and `resources` in
`_quarto.yml`, and put the application folder at the repository root.

**Share row.** Any page with `<div class="share" data-share></div>` inside a
`{=html}` block gets the share controls built into it. Links are assembled from
the live URL and page title, so there is nothing to update per page.

**Changing the choice task.** `BIDS` and `BOUNDS` at the top of
`_includes/scripts.html` define the bid tree and the intervals it implies. If you
change the four-week wait difference, change `WEEKS` too or the per-week figures
will be wrong.

## Accessibility and performance

Visible keyboard focus throughout. `prefers-reduced-motion` respected. The
choice-task result is `aria-live`. The papers filter operates on a list fully
present in the HTML, so the page works without JavaScript and is indexed whole.
One web font request, no analytics, no third-party scripts, no tracking.


## Writing raw HTML in a .qmd

Always wrap it in a passthrough fence:

    ```{=html}
    <ul class="rec-list">
      <li class="rec">...</li>
    </ul>
    ```

Without the fence, Pandoc treats indented HTML lines as an indented code block
and prints your markup on the page as text instead of rendering it. Every raw
HTML block in this repository is fenced for that reason.

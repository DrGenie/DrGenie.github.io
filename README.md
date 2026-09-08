# mesfingenie.com

Quarto site for Mesfin Genie, deployed to GitHub Pages.

---

## Deploying this

1. **Back up the current repository first.** `git checkout -b old-site && git push origin old-site`, or download a zip of `main`. You will need files out of it in step 3.

2. **Clear `main` and unpack this in its place.** Delete everything in the working copy except the `.git` folder, then copy the contents of this folder in.

3. **Copy five things across from the old site.** They are not in this package because they are your files, not generated ones:

   | From the old repo | To here |
   |---|---|
   | `assets/mesfin-genie-profile-square.webp` | `assets/` |
   | `assets/og-card.png` | `assets/` |
   | `assets/favicon.png` | `assets/` |
   | `cv/mesfin-genie-cv.pdf` | `cv/` |
   | `eMANDEVA-DecisionAid-V18/`, `farming-bca-tool-v18/`, `STEPS-FETP-DecisionAid-V20/` | repository root |

4. **Uncomment the three tool lines in `_quarto.yml`** once those folders are in place (they are commented out so the site still builds without them).

5. **Preview locally**, then push.

   ```
   quarto preview
   quarto render
   ```

6. **GitHub Pages → Settings → Pages → Source: GitHub Actions.** Pushing to `main` runs `.github/workflows/publish.yml`.

---

## What changed, and why

**Navigation is four items** — Research, Papers, Tools, About, with CV as a utility link. Teaching, supervision, grants, writing and the blog are nested. Seven top-level items made the site feel like an institution rather than a person.

**No cards, no eyebrow labels, no arrow CTAs.** Those three patterns together are what made the old site legible as machine-written. Comparable items are set as ruled rows instead, which is the structure of an attribute table — a real object from your field rather than a generic UI kit.

**The homepage leads with a working choice task.** Three binary choices, bisected on the answers, returning a bracketed willingness to pay for four weeks of avoided waiting. It demonstrates the method instead of describing it, and it is the one place on the site allowed to be loud. Everything else is deliberately quiet so that it lands.

**One typeface, one accent colour.** Spectral throughout at four weights; claret used only for links, the current-page marker, and the selected option in the choice task.

**No navy bar across the top.** The header is the same paper as the page with a hairline under it.

**Publication detail pages are gone.** Six pages each holding one abstract split attention for no gain. Everything is on one filterable list, with a plain-English finding for each paper.

**The footer is two lines.** No duplicated navigation, no share widget.

**Repository scaffolding removed.** `CHANGELOG.md`, `REPLACE-AND-CLEANUP.md`, `UPDATE-DEPLOY.md` and the six files in `docs/` are not carried over. They were visible in a public repo and read as generated. The single-source-of-truth `data/*.yml` layer is also gone: it was more machinery than twenty pages of content needs, and it made small edits expensive.

---

## Content you need to complete

Everything on the site is drawn from your live pages, your University staff profile, or your Google Scholar record. Four things are deliberately incomplete because I could not verify them, and inventing them would be worse than leaving them:

1. **`publications/index.qmd` holds four papers.** Your Scholar record has more. There is a commented-out template at the top of the list showing the markup and the `data-topic` tags the filter reads. Add each paper with its real DOI, and write the one-sentence finding yourself — that sentence is the thing that makes the page better than everyone else's publication list, and it has to be yours.

2. **DOIs and PDF links are absent** from the four entries that are there. Add them inside `<p class="rec-links">`.

3. **`grants/index.qmd` names MandEval and the World Bank work.** Add the others, keeping institutional allocations and programme totals reported separately.

4. **Course codes in `teaching/index.qmd`** are copied from your old site. Check they are current for this year.

Search the repository for `TO ADD A PAPER` to find the template.

---

## Design system

Change these in `custom.scss` and everything follows.

| Token | Value | Used for |
|---|---|---|
| `$paper` | `#fbfbf9` | Page background |
| `$ink` | `#16232b` | Body text (deep petrol, not black) |
| `$ink-strong` | `#0d171d` | Headings |
| `$muted` | `#5b6d76` | Metadata, captions, footer |
| `$rule` | `#d7dee1` | Hairlines |
| `$tint` | `#eef2f3` | Table headers, code blocks |
| `$accent` | `#7c2233` | Links, current page, selected option |

Type is Spectral at 19px with a 1.68 line height and a 68-character measure. The scale is a minor third: 2.45rem, 1.55rem, 1.16rem, 1rem.

The section numbering inside `custom.scss` maps to page regions, so search for `// 5. Record lists` or `// 6. Choice task` rather than scrolling.

---

## Editing

**Add a blog post.** Create `blog/posts/<slug>/index.qmd` with `title`, `description`, `author`, `date` and `categories`. The listing and RSS feed pick it up automatically.

**Add a tool.** Create `tools/<id>/index.qmd`, add it to the `render` list in `_quarto.yml`, put the tool folder at the repository root, and add it to `resources`.

**Change the choice task.** The bid tree and the implied intervals are the `BIDS` and `BOUNDS` objects at the top of `assets/scripts.html`. They are commented. If you change the wait difference, change `WEEKS` too, or the per-week figures will be wrong.

---

## Accessibility and performance

Keyboard focus is visible everywhere. `prefers-reduced-motion` is respected. The choice task result region is `aria-live`. The papers filter operates on a list that is fully present in the HTML, so the page works without JavaScript and is indexed in full. There are no web fonts beyond one Spectral request, no analytics, no third-party scripts, and no tracking.

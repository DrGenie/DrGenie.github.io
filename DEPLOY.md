# Deploy

## Read this first: I had deleted 16 of your blog posts

My earlier rebuilds carried across one blog post and silently dropped the other
sixteen — the Allais paradox, the Ellsberg paradox, loss aversion, the power of
free, the tyranny of the default, and the rest. They are real writing, around
five hundred words each, and losing them would have been the most damaging thing
in this whole exercise.

All seventeen are back, renumbered into the new theme, each with a share row, and
the RSS feed carries all seventeen. Also restored: your conferences page, the
ECON3111 teaching resources page, `blog/editorial-calendar.qmd`, and the
`update-scholar-metrics.yml` workflow that refreshes your Scholar figures every
Monday.

Both restored pages were written in the old theme's markup, using classes like
`page-shell` and `event-card` that no longer exist. I rewrote them in the new
design language, keeping every date, title, venue and link.

## Using the web uploader

You can, but it needs two extra steps, because "Add files via upload" only adds.
It never deletes, and it will not create a file whose name begins with a dot.

**Step 1 — delete these first, in the web interface.** Open each one and use the
"..." menu, then Delete. For folders, open the folder and choose Delete directory.

    CHANGELOG.md
    REPLACE-AND-CLEANUP.md
    UPDATE-DEPLOY.md
    _variables.yml
    docs/                                    (whole folder)
    contact/                                 (whole folder)
    publications/covid-mandate-repository/   (whole folder)
    publications/feeling-lonely/             (whole folder)
    publications/fit-for-purpose/            (whole folder)
    publications/guidance-or-misdirection/   (whole folder)
    publications/no-jab-no-access/           (whole folder)
    publications/priority-for-self-or-others/ (whole folder)
    eMANDEVA-DecisionAid-V18/README.md

Nothing else needs deleting. Everything else in this zip lands on the same path
as the file it replaces, so the upload overwrites it.

**Step 2 — upload.** Unzip, then drag the *contents* of the folder onto
`github.com/DrGenie/DrGenie.github.io/upload/main`. Not the folder itself, the
files and folders inside it. Commit.

**Step 3 — check the dotfiles arrived.** In the file list, look for `.github`,
`.gitignore` and `.nojekyll`. If any is missing, use Add file → Create new file
and type the name exactly, including the leading dot, with the content from this
zip. For `.github/workflows/publish.yml`, type that whole path as the filename
and GitHub creates the folders.

Your existing `publish.yml` already works, so if it does not upload, the site
still builds. `.nojekyll` and `.gitignore` are optional with Actions deployment.

If any of that sounds fragile, it is. GitHub Desktop is easier: clone, delete
everything except the `.git` folder, copy this zip's contents in, commit, push.

Settings → Pages → Source must be **GitHub Actions**.

## The mobile problem, and what caused it

Quarto lays pages out on a CSS grid. In the version currently live, that grid gives
the content column a **500px minimum width**, so on any phone narrower than 500px
the page overflows sideways and the side margins collapse to nothing, leaving
every line of text flush against both screen edges.

I caused it twice over. I set Quarto's `$grid-sidebar-width`, `$grid-margin-width`
and `$grid-column-gutter-width` to zero to take control of the layout, which also
deleted the media queries Quarto uses to collapse that grid on small screens. And
`main.content` had vertical padding but no horizontal padding at all — invisible
on desktop, where the grid margins covered for it.

Fixed by leaving Quarto's grid alone apart from the body width, and giving the
content column, header and footer a real gutter that grows from 20px on a phone
to 36px on a laptop, all aligned to the same edge.

Four more bugs found in the same pass: a `padding` shorthand was silently zeroing
the footer gutter; the navbar gutter targeted `.container-fluid` when Quarto's
wrapper is `.navbar-container`; `table { display: block }` was destroying table
layout; and the homepage portrait, floated at 112px beside text in a 320px column,
left about four words per line, so below 560px it now sits above the name.

## Typography

Spectral throughout, one family at four weights. Body scales fluidly from 16.5px
to 19px with the viewport, line height 1.68, measure about 66 characters. To
change the typeface, edit two places: the font link in `_includes/head.html` and
`$font-family-sans-serif` at the top of `custom.scss`.

## Verified in this build

49 pages render with no warnings. All 41 site pages pass lang, viewport, image alt
text, single h1, meta description, and carry no leftover markup from the old
theme. No broken internal links. 44 papers with 43 DOIs. 17 blog posts, 17 RSS
items. Twenty behavioural assertions pass against a real DOM covering the choice
task, the papers filter and the share row. Your three tool applications are
vendored in and serve from your own domain.

## What I cannot check

I have no browser here, so layout is verified by reading compiled CSS rather than
by looking at the page. That is exactly how the missing gutter escaped me. Open
the site on your phone, and send a screenshot if anything still looks wrong.

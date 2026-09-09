# Deploy

Unzip. In your repo, delete `publications/` and `blog/` first (they have
files this version replaces or reorganises), then drag the contents of this
folder onto github.com/DrGenie/DrGenie.github.io/upload/main and commit.
Everything else lands on the same path as the file it replaces.

`.github/`, `.gitignore` and `.nojekyll`: already in your repo. Leave them.
To replace `publish.yml`, open it on GitHub, pencil icon, paste the version
from the message, commit.

## What is in this version

Papers: 47 items from Google Scholar, ResearchGate and your staff profile,
split into journal articles (41), working papers (4), chapters and datasets
(2), and 9 conference abstracts in their own collapsed section. Notes under
papers removed. Author lists collapse. Search box.

One item I could not resolve: the Social Science & Medicine paper at
sciencedirect.com/science/article/pii/S0277953626007859. ScienceDirect blocks
automated access and it is not yet on ResearchGate, Scholar snippets, PubMed
or RePEc. The entry is on the page with your link and the correct venue and
year; the title reads "New article, Social Science & Medicine (2026)". Open
publications/index.qmd, search for that string, replace it with the title.

Instagram: the button draws a square card (category, title, hook, a chart
unique to the post, "Dr Genie · Health Economics" or "· Behavioural
Economics") and hands it to your phone's share sheet as an image. Tap
Instagram, then "Add to your story". On a laptop there is no share sheet, so
the card downloads and instagram.com opens.

Nav now has Writing. Brand is Dr Genie. Inter throughout. Spacing tightened.
25 posts, 8 new, each with its own preview image. Em dashes removed. CV
recompiled.

About "Error rendering embedded code / Invalid image source" on GitHub: that
is GitHub trying to preview .qmd source files. It cannot resolve site paths or
Quarto fences. It says nothing about the site, which renders them correctly.

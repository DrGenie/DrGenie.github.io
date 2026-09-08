# Deploy

1. Download and unzip.
2. In your `DrGenie.github.io` repository, delete everything except the `.git`
   folder, then copy in everything from this zip (including the hidden
   `.github`, `.nojekyll` and `.gitignore` files).
3. `git add -A && git commit -m "Rebuild site" && git push`

Settings → Pages → Source must be set to **GitHub Actions**. That is the only
setting involved. The workflow renders and deploys on every push to `main`.

Nothing needs editing. Nothing is a placeholder.

## What is in here

31 rendered pages: 23 site pages plus your three tool applications, which are now
inside the repository. Previously the folders `eMANDEVA-DecisionAid-V18/`,
`farming-bca-tool-v18/` and `STEPS-FETP-DecisionAid-V20/` held only a README, so
all three tool links on your live site were dead. The applications have been
copied in from their own repositories and now serve at
`mesfingenie.com/eMANDEVA-DecisionAid-V18/` and the equivalent paths.

The papers page carries all 44 items from `assets/publications.json` with full
author lists, venues, citation details and 43 DOI links, filterable by area.

Facts on the grants, teaching, supervision, CV, about and tools pages were
corrected against your `data/*.yml` records: MRF2019107 with A$808,440 and
A$4,754,183.37 reported separately, the World Bank FETP business case at $416,000,
your actual coordinator role per course, four current PhD students and three
completed higher degrees, Senior Lecturer since 2026 after Lecturer 2023–2025, and
Dr Frank Wogbe Agbola credited as lead and publisher of the SOIL CRC tool.

`data/*.yml` is retained as the verified record behind those pages. It is no
longer read at build time.

## One thing I could not do

Five papers carry a one-sentence plain-English finding. The other 39 do not.

I will not write those from abstract skims. A sentence on your own site saying
what your paper found is a claim in your name, and getting one wrong is worse
than not having it. The page is complete without them — full metadata, full
author lists, working DOIs, which is what an academic publication list is. If you
add findings to your ten or fifteen most cited papers later, the markup is one
line and the README shows it.

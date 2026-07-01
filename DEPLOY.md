# Final version - what changed and how to deploy

This package contains the polished final version of your site. To avoid disturbing
your three working tool apps, it does NOT include the tool folders
(eMANDEVA-DecisionAid-V18, farming-bca-tool-v18, STEPS-FETP-DecisionAid-V20).
You keep those exactly as they are.

## What changed in this version

Content and accuracy
- Moved the two ANZJPH papers ("Community First or My Body First?" and
  "No Jab, No Access?") out of journal articles. They now appear on the
  Conferences page under "Published conference papers", each linked to CDIC 2026
  (Communicable Diseases and Immunisation Conference, cdic2026.com) and to the DOI.
- Publications count updated from 44 to 42, and the homepage tile now reads 42.
  The 2026 journal group now shows 13 articles.
- The homepage "Recent publications" now features a journal article
  (Social Science and Medicine) in place of the reclassified conference paper.
- Two 2026 Value in Health abstracts are pre-wired on the Conferences page as a
  commented block, ready for you to paste the titles and authors (see below).

Design and usability
- Fixed the duplicate "Mesfin Genie" heading: the automatic Quarto title block is
  now hidden, so your hero is the only title.
- Replaced the hand-drawn profile icons with the official brand marks for Google
  Scholar, ORCID, ResearchGate, LinkedIn, GitHub and X, plus university profile
  and email. All are crisp inline SVG (no external icon fonts, so no speed cost).
- Tightened the large white spaces: smaller hero and section padding, a smaller
  maximum heading size, and tighter section spacing.
- The Tools section and page now include the STEPS Decision Aid (World Bank FETP),
  and the tools grid reflows cleanly for three tools on any screen size.
- Consistent naming: eMANDEVAL Future is used throughout.

Publications filters
- The output-type and other dropdowns are verified against the data. "Book
  chapter", "Working papers" and "Data and research outputs" all return their
  records. The "No publications match" you saw was the older live build; this
  version is correct.

Google Scholar auto-update
- Still active: metrics refresh daily through SerpAPI and never show fabricated
  numbers. Setup is in step 5 below.

## Deploy, step by step

Pushing to the main branch auto-builds and publishes your site. Here is the safe
way to apply this update.

1. Download and unzip this package on your computer.

2. Open your website repository folder (the one with _quarto.yml, index.qmd and
   the assets folder).

3. Copy the contents of this package INTO your repository folder and choose
   "replace/overwrite" when asked. Copy these items:
   - _quarto.yml
   - index.qmd
   - the assets folder
   - the scripts folder
   - the .github folder
   - the publications, conferences, research, teaching, cv, tools folders
   - CNAME, robots.txt, sitemap.xml, .nojekyll, README.md
   Do NOT delete anything else. Leave your three tool folders
   (eMANDEVA-DecisionAid-V18, farming-bca-tool-v18, STEPS-FETP-DecisionAid-V20)
   in place. This package intentionally omits them, so copy-and-overwrite will not
   touch them.

4. Commit and push. GitHub Desktop: review the changed files, write a summary like
   "Final polish: conferences, brand icons, STEPS tool, spacing", Commit to main,
   then Push origin. Command line:
   ```
   git add -A
   git commit -m "Final polish: conferences, brand icons, STEPS tool, spacing"
   git push origin main
   ```
   The "Publish website" action runs automatically. After it finishes (1 to 2
   minutes), refresh https://mesfingenie.com with Ctrl/Cmd + Shift + R.

5. One-time, to switch on live Scholar numbers:
   - Sign up free at serpapi.com and copy your API key.
   - In your repo on GitHub: Settings, then Secrets and variables, then Actions,
     then New repository secret. Name it SERPAPI_KEY and paste the key.
   - Settings, then Actions, then General, then Workflow permissions: choose
     "Read and write permissions".
   - Actions tab, "Update Google Scholar metrics", Run workflow. The citations and
     h-index tiles then appear and refresh daily.

## The one thing I need from you

I could not read the two Value in Health 2026 abstracts because ScienceDirect
blocks automated access, so I did not guess their titles. On the Conferences page
there is a commented block with both links already in place. Send me, for each:
the exact title, the author list, and the page range. I will drop them straight in.
The two links you gave are:
- https://www.sciencedirect.com/science/article/abs/pii/S1098301526019935
- https://www.sciencedirect.com/science/article/abs/pii/S1098301526019157

## Optional quick wins to push it higher

- Turn on site search (search: true in _quarto.yml) so visitors can search across
  all pages, not only filter publications.
- Add a short plain-language research summary on the Research page.
- Add one representative figure or screenshot per tool on the Tools page.

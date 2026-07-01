# Final version - changes, the tools situation, and deployment

## What I changed this round

Home page (Selected work)
- Replaced the npj Vaccines item with the Health Economics feedback paper. The
  three featured papers are now Health Economics (Guidance or Misdirection),
  Social Science and Medicine (Fit for Purpose), and Health Policy (Feeling Lonely).

Conferences
- Fixed the two 2026 ISPOR abstract links, which were interchanged. PCR4 now points
  to its correct ScienceDirect page and PCR82 to its own.

CV (both the web page and the downloadable PDF)
- Recompiled cv/mesfin-genie-cv.pdf and updated cv/index.qmd.
- The two ANZJPH items are now listed under Published conference abstracts
  (CDIC 2026), not journal articles, matching the rest of the site.
- Added the two 2026 ISPOR abstracts (PCR4 and PCR82) to the CV.
- Added the STEPS FETP Scale-up Decision Aid to Research tools.
- Added a "Last updated July 2026" line and an outputs count.

New: Blog
- Added a modern blog at /blog/ with a grid listing, categories, an RSS feed, and
  two starter posts you can edit or delete (blog/posts/). Add a new post by
  creating blog/posts/your-post/index.qmd with a title, date and description.
- Added Blog to the navigation.

Other useful improvements
- Turned on site search across all pages.
- Tidied the title handling so blog posts show their titles while the other pages
  keep their custom headers.

## Important: your interactive tools

Every zip you have sent me contains only EMPTY placeholder folders for the three
tools (each holds a single note: "the live application files remain in this
folder"). So I have never had your actual eMANDEVA, farming or STEPS app files -
only your live site has them. Because of that:

- I did not ship empty tool folders in this package (they would overwrite your
  real tools with nothing). The tool cards and CV links still point to the correct
  URLs.
- Your live site still shows the tools only because it is serving an older build.
  Your repo does not contain the tool app files at all, which is also why the live
  site has not updated to the new design: the deployment is not building from the
  current repo.

### About STEPS specifically
You asked me to create the STEPS tool. I can't rebuild it faithfully: STEPS runs a
mixed-logit preference model estimated from your discrete choice experiment, and I
do not have those coefficients or the app's source, and I can't download it. Making
a version with invented preference weights would put fabricated numbers into a
real FETP policy tool, which I won't do. Two honest options:
1. Upload your STEPS-FETP-DecisionAid-V20 folder (the files that are live) and I
   will wire it into the repo, or
2. Send me the estimated model coefficients and cost templates and I will build a
   clean, correctly-specified STEPS tool from them.

## Deploy, step by step

1. Unzip this package and copy everything into your repository, overwriting when
   asked. New/changed: index.qmd, conferences/, cv/ (page + PDF), assets/, the new
   blog/ folder, and _quarto.yml.

2. Add your three real tool folders to the repository root (same level as
   index.qmd): eMANDEVA-DecisionAid-V18, farming-bca-tool-v18 and
   STEPS-FETP-DecisionAid-V20, each with their real application files. Without
   these, the tool links will 404 after the site rebuilds.

3. Commit and push to main:
   git add -A
   git commit -m "Selected work, ISPOR links, CV update, blog, search"
   git push origin main

4. Make it actually deploy. On GitHub: Settings, then Pages, and set Source to
   "GitHub Actions". Open the Actions tab and confirm the Publish website run is
   green. This is why your live site is still the old design.

5. Hard refresh (Ctrl/Cmd + Shift + R) and check the pages, the blog, and the three
   tool links.

## Still useful to send me
- Full author lists and page ranges for PCR4 and PCR82 (currently "et al.").
- Your STEPS folder or its model coefficients, per the options above.

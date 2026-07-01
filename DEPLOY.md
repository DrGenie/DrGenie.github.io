# Final update - deep repo check, fixes, and how to deploy

## Deep check of your repo (github.com/DrGenie/DrGenie.github.io) - findings

1. Your repo already contains the newer navy design (my previous version): brand
   icons, STEPS card, the 42-outputs tile, and the conference reclassification.
2. IMPORTANT: the three interactive tool folders were MISSING from the repo
   (eMANDEVA-DecisionAid-V18, farming-bca-tool-v18, STEPS-FETP-DecisionAid-V20).
   They only still work on the live site because the live site is an older build.
   The moment the repo rebuilds, those tools would 404. This package restores
   eMANDEVA and farming (recovered from your earlier upload). STEPS was never in
   any file you sent me, so you must add your STEPS-FETP-DecisionAid-V20 folder to
   the repo yourself (see step 3).
3. Your live site (mesfingenie.com) is still the OLD green build, which means the
   navy version in your repo has not actually deployed yet. Check that GitHub Pages
   is set to deploy from GitHub Actions and that the "Publish website" action is
   passing (see step 5).
4. Removed a stray placeholder file (profile.jpg.README.txt) from the package.

## What I changed this round

- Conferences: the two ANZJPH items ("Community First..." and "No Jab, No
  Access...") are now listed as conference ABSTRACTS (not papers), each linked to
  CDIC 2026 (cdic2026.com).
- Added the two 2026 Value in Health abstracts you sent: PCR4 (Choosing for the
  Worse-Off) and PCR82 (MASLD/MASH testing in type 2 diabetes), linked to their
  ScienceDirect pages. Author line shows "Mesfin G. Genie et al." - send me the
  full author lists and page ranges and I will complete them.
- Fixed the mislabelled CDIC entry: the 15-17 June 2026 Melbourne presentation now
  correctly reads Communicable Diseases and Immunisation Conference (CDIC 2026)
  and links to cdic2026.com (its real dates and city match exactly).
- White space reduced across every tab: shorter page headers, tighter sections,
  research blocks and section headings, and a more compact hero.
- Device optimisation: refined layouts at 900px, 520px and 380px so the hero,
  stats band, event cards, tools and icons all sit well on phones and tablets.
- Profile photo and icons: the photo is a centred square in a circular frame, so
  the crop is symmetric; the crop point was nudged for a natural head position,
  and all profile icons are sized and centred consistently.

## Deploy, step by step

1. Download and unzip this package.

2. In your website repository folder, copy in everything from this package and
   choose replace/overwrite. This includes the assets, scripts, .github and page
   folders, plus the eMANDEVA-DecisionAid-V18 and farming-bca-tool-v18 tool
   folders (restored).

3. Add your STEPS tool folder. Copy your existing STEPS-FETP-DecisionAid-V20
   folder into the repository root (the same level as index.qmd). Without it, the
   STEPS tool link will 404 after the site rebuilds.

4. Commit and push to main:
   ```
   git add -A
   git commit -m "Conferences fixes, CDIC, white space, device polish, restore tools"
   git push origin main
   ```

5. Make sure it actually deploys. On GitHub: Settings, then Pages, and confirm
   "Source" is "GitHub Actions". Then open the Actions tab and check that the
   "Publish website" run is green. If Pages was set to "Deploy from a branch",
   that is why your live site was stale - switch it to GitHub Actions and re-run.

6. After it deploys, hard refresh (Ctrl/Cmd + Shift + R) and check the three tools
   open: /eMANDEVA-DecisionAid-V18/, /farming-bca-tool-v18/, /STEPS-FETP-DecisionAid-V20/.

## Still to send me (optional, to finish)

- Full author lists and page ranges for the two Value in Health 2026 abstracts.
- If you want the interactive tool apps themselves made fully mobile-friendly,
  say so and send the tool source; that is separate from the main site styling
  and I can optimise each app's layout.

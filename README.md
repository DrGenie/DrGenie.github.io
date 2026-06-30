# Mesfin Genie academic website

## Upload through the GitHub website

1. Keep these existing repository items:
   - `.github/workflows/publish.yml`
   - `eMANDEVA-DecisionAid-V18/`
   - `farming-bca-tool-v18/`
2. Unzip this package on your computer.
3. In `DrGenie/DrGenie.github.io`, select **Add file → Upload files**.
4. Open the unzipped folder, select every item inside it, and drag the selected items onto the GitHub upload page.
5. Commit with: `Replace website with final professional design`.
6. Open **Actions** and wait for the **Publish website** workflow to show a green check.
7. Open `https://mesfingenie.com/` and hard-refresh the browser.

## Old QMD files

The `_quarto.yml` file contains an explicit `render:` list. Old QMD files that remain in the repository are therefore ignored and will not be published.

For a clean repository, old root-level pages such as `about.qmd`, `research.qmd`, `publications.qmd`, `projects.qmd`, `software.qmd`, `students.qmd`, `supervision.qmd`, `contact.qmd`, `news.qmd`, `teaching.qmd`, and `cv.qmd` can be deleted later. Do not delete the two live-tool folders or the GitHub workflow.

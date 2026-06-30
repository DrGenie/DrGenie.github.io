# Mesfin Genie academic website

## Upload through GitHub web

1. Keep these existing repository items:
   - `.github/workflows/publish.yml`
   - `eMANDEVA-DecisionAid-V18/`
   - `farming-bca-tool-v18/`
2. Unzip this package.
3. Open `DrGenie/DrGenie.github.io`.
4. Select **Add file → Upload files**.
5. Open the unzipped folder, select every item inside it, and drag the selected items onto GitHub.
6. Commit with: `Implement final academic website revisions`.
7. Open **Actions** and wait for **Publish website** to show a green check.
8. Open `https://mesfingenie.com/` and hard-refresh the browser.

## Optional repository clean-up

After the new site works, the following unused legacy files can be deleted from GitHub:

- `contact/index.qmd`
- `news/index.qmd`
- `projects/index.qmd`
- `software/index.qmd`
- `supervision/index.qmd`
- `profile.jpg.README.txt`
- `assets/styles.scss`
- `assets/publications.bib`
- `assets/publications_by_field.csv`

Do not delete the two live-tool folders, `CNAME`, `.nojekyll`, or the GitHub publishing workflow.

# Replace your repository cleanly (and remove conflicting old files)

Your repository has accumulated files from several earlier versions. GitHub's
"upload files" never deletes anything, so old and new files now sit side by side.
The build broke because one leftover file had corrupted front matter, and the site
is cluttered with duplicates. The fix is to make the repository an exact copy of
this package, while keeping your three interactive tool folders.

## Keep these three folders (do not delete)
- eMANDEVA-DecisionAid-V18/
- farming-bca-tool-v18/
- STEPS-FETP-DecisionAid-V20/

## Method A - clean replace with Git (recommended)
This makes the repo exactly match the package and removes every stale file.

```
# 1. Clone a fresh copy
git clone https://github.com/DrGenie/DrGenie.github.io.git
cd DrGenie.github.io

# 2. Delete all tracked files EXCEPT the three tool folders (and .git)
find . -type f \
  ! -path './.git/*' \
  ! -path './eMANDEVA-DecisionAid-V18/*' \
  ! -path './farming-bca-tool-v18/*' \
  ! -path './STEPS-FETP-DecisionAid-V20/*' \
  -delete
find . -type d -empty ! -path './.git/*' -delete

# 3. Unzip this package and copy its contents into the repo folder
#    (so index.qmd, _quarto.yml, assets/, etc. sit at the repo root)
cp -R /path/to/unzipped-package/. .

# 4. Commit and push
git add -A
git commit -m "Clean rebuild: World Bank identity, fixed build, no stale files"
git push origin main
```

## Method B - GitHub Desktop
1. Open the repository folder that GitHub Desktop manages.
2. In Finder/Explorer, delete everything EXCEPT the `.git` folder and the three
   tool folders listed above.
3. Unzip this package and copy its contents into that same folder.
4. In GitHub Desktop you will see deletions and additions. Commit to main, then Push.

## Method C - GitHub website only
If you must use the web UI, first delete the stale files below (open each file,
choose the trash icon, commit), then upload this package (drag the folders in).

### Stale files and folders to delete
Folders (delete the whole folder):
- talks/
- talks-media/
- publications/featured/
- research/projects/decision-tools/
- research/projects/eye-tracking-choice/
- research/projects/world-bank-fetp/
- tools/emandelval-future/
- tools/soil-crc-bca-tool/
- tools/steps-decision-aid/
- blog/posts/starting-to-write-here/
- blog/posts/editorial-calendar/
- assets/css/
- assets/js/
- assets/data/
- assets/img/
- assets/reports/

Individual files:
- DEPLOY.md
- VALIDATION.txt
- profile.jpg.README.txt
- scripts/validate_site.py
- assets/teaching/week1-foundations.webp
- assets/teaching/week6-risk-uncertainty.webp

## After you push
1. Settings, then Pages: Source must be "GitHub Actions".
2. Open the Actions tab and confirm the Publish website run is green.
3. Hard-refresh https://mesfingenie.com (Ctrl/Cmd + Shift + R) and check the pages,
   the three tools, and the new World Bank styling.

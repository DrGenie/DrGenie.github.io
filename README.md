# Mesfin Genie website — credibility-first release

## Upload through GitHub web

1. Download and unzip the package.
2. Open the unzipped `mesfin-genie-credibility-site` folder.
3. On macOS, press `Command + Shift + .` so the hidden `.github` folder is visible.
4. Open `https://github.com/DrGenie/DrGenie.github.io`.
5. Select **Add file → Upload files**.
6. Select every item inside the unzipped folder and drag the selection onto GitHub. Do not upload the ZIP or its parent folder.
7. Commit with: `Implement credibility-first website and LaTeX CV`.
8. Open **Actions** and wait for **Publish website** to finish with a green check.
9. Open `https://mesfingenie.com/` in a private window or hard-refresh with `Command + Shift + R`.

Keep the existing `eMANDEVA-DecisionAid-V18/` and `farming-bca-tool-v18/` folders. This package does not replace them.

## Google Scholar metrics

The workflow `.github/workflows/update-scholar-metrics.yml` attempts a verified update once weekly and can also be run manually. It only publishes values when the public profile name and metrics table are verified. If Google Scholar rate-limits the request, the last verified values are retained; unverified zeros are never shown.

To run it once after upload: **Actions → Update Google Scholar metrics → Run workflow**. A successful update commits `assets/scholar-metrics.json`, which triggers the website publishing workflow.

## CV

The PDF was generated from `cv/mesfin-genie-cv.tex` using XeLaTeX. Both the source and PDF are included.

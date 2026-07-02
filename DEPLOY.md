# Clean replacement deployment

The safest web-only method is to make one backup branch, clean the source tree in GitHub's web editor, upload the replacement package, and then let the validated GitHub Action deploy it.

## Files to preserve

Preserve the complete contents of these two live application folders:

- `eMANDEVA-DecisionAid-V18/`
- `farming-bca-tool-v18/`

Everything else in the repository can be replaced by this package.

## Required deployment checks

The `Publish website` workflow must pass: prepare generated content, validate source data and pages, render, upload and deploy.

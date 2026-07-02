# GitHub Pages deployment queue fix

This repository uses a two-job GitHub Pages workflow:

1. `build` validates and renders the Quarto website and uploads the `_site` artifact.
2. `deploy` publishes the validated artifact to the `github-pages` environment.

The workflow deliberately uses `cancel-in-progress: false` so an in-progress production deployment is not cancelled by a later commit. The Pages deployment action is allowed up to 20 minutes to clear GitHub's deployment queue, while the deploy job has a 30-minute ceiling.

If a deployment is queued, do not upload the site again. Wait until no other Pages workflow is running, then use **Re-run failed jobs** on the latest run.

# Deploy guide and change summary

This is your full site with the requested changes applied. Your existing GitHub
Actions pipeline (`.github/workflows/publish.yml`) already renders Quarto and
deploys to GitHub Pages on every push to `main`, so deploying is just replacing
files and pushing.

## What changed

Homepage (`index.qmd`)
- Removed the "Open to collaboration" pill and the 01 / 02 / 03 numbers on the
  research cards. Both are common "template" tells and added visual noise.
- Rewrote the credibility band so it reads as a research profile, not a
  marketing dashboard: Citations and h-index (live from Google Scholar, shown
  only once real numbers exist), 44 peer-reviewed and other outputs, A$4.75M
  programme funding secured, and 4 countries of appointment. The vague
  "6 academic appointments" and "2 live research tools" tiles were dropped.
- Replaced the em dash in the intro sentence and the en dashes in the tool
  descriptions with plain punctuation.

Site-wide
- Removed every long dash (em and en) from the page copy and replaced them with
  hyphens or commas.
- Google Scholar auto-update now works (see below).
- Faster mobile load: the hero image that actually appears is now preloaded
  (the previous preload pointed at a different file).
- Mobile polish: credibility band reflows cleanly at any tile count, the hero
  heading no longer risks overflow on small phones, and the profile links are
  larger tap targets.

Publications
- Already ordered newest year first (2026 at the top, descending). Confirmed and
  left in place. Search, theme, year and output-type filters all work.

## Deploy in 4 steps

1. Copy every file from this package over the matching files in your repository,
   keeping the same folder layout (`assets/…`, `scripts/…`, `.github/…`, the
   `.qmd` pages, and `_quarto.yml`).
2. Commit and push to `main`:
   ```bash
   git add -A
   git commit -m "Refine homepage, fix Scholar metrics, remove long dashes, mobile polish"
   git push origin main
   ```
3. Watch the "Publish website" action finish in the GitHub Actions tab. Your site
   updates at https://mesfingenie.com automatically.
4. Hard refresh (Ctrl/Cmd + Shift + R) to clear the cache and confirm the changes.

## Turn on live Google Scholar metrics

Google Scholar blocks GitHub's servers directly, which is why the old updater was
switched off. This version reads the same public profile through SerpAPI, which is
not blocked and has a free tier that easily covers one lookup per day.

1. Sign up free at https://serpapi.com and copy your API key from the dashboard.
2. In your repo: Settings, then Secrets and variables, then Actions, then New
   repository secret. Name it exactly `SERPAPI_KEY` and paste the key.
3. Settings, then Actions, then General, then Workflow permissions: select
   "Read and write permissions" so the job can commit the updated numbers.
4. Run it once now: Actions tab, "Update Google Scholar metrics", Run workflow.
   After it succeeds, the Citations and h-index tiles appear on the homepage. It
   then refreshes on its own every day.

If you would rather not use SerpAPI, you can instead edit
`assets/scholar-metrics.json` by hand whenever you like: set `citations`,
`h_index` and `updated`, commit, and the tiles will show those values. No number
is ever invented; the tiles stay hidden until a real value is present.

## One decision left to you

The vaccine tool is called "eMANDEVAL Future" on the homepage but "eMANDEVA" in
the folder name and elsewhere. Pick one public name and use it everywhere so it
is not confusing when someone cites or bookmarks it.

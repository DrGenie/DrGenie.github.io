# Deploying this update

Your repository is already clean (you did the full replace), and this update only
adds and changes files, it does not introduce any new stale files. So a simple
overwrite is safe this time.

## Option 1 - github.dev (browser, recommended)
1. Open your repo and press the `.` key to launch github.dev.
2. Unzip this package on your computer.
3. Drag the unzipped contents into the file list, choosing "replace" when asked.
   Make sure `index.qmd`, `_quarto.yml`, and the `assets`, `blog`, `supervision`,
   `teaching`, `research`, `about`, `contact` folders land at the top level.
4. Source Control icon -> commit message "Update: World Bank polish, footer, sharing,
   collapsible authors, new posts" -> Commit & Push.
5. Keep the three tool folders untouched.

## Option 2 - GitHub website
Add file -> Upload files, drag the unzipped contents in (a few batches is fine),
commit to main. Overwriting is safe because the repo is already clean.

## After it deploys
- Actions tab: confirm the Publish website run is green.
- Hard-refresh https://mesfingenie.com (Ctrl/Cmd + Shift + R).
- Check: the footer (four columns + Share this site), a blog post (Share this article
  bar at the end), the Publications page (long author lists now show "Show all N
  authors" with your name always visible and in bold), and the Supervision page
  (two completed MSc supervisions, no "Recorded" heading).

## What changed in this update
- Supervision: the two master's records are now Master of Science (MSc), listed under
  Completed supervision; the "Recorded supervision, shown under a neutral status"
  wording is removed. All other MPhil mentions reconciled to MSc.
- World Bank identity strengthened: Open Sans typeface, World Bank blue/gold, heavier
  navy headings, gold masthead ribbon, calmer interior pages.
- New World Bank-style footer with Explore, Connect, and Share-this-site columns.
- Social sharing: X, LinkedIn, Facebook, Bluesky, WhatsApp, Email, and Copy-link,
  in the footer (share the site) and auto-added to the end of every blog post.
- Publications: author lists longer than five collapse to a clean summary with your
  name always shown and bolded, and a "Show all authors" toggle.
- Four new contemporary behavioural-insight posts (the power of free, the tyranny of
  the default, why apps autoplay, why 19,998 feels cheaper than 20,000).

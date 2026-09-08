# Deploy

1. Unzip.
2. In `DrGenie.github.io`, delete everything except the `.git` folder, then copy
   in everything here, including the hidden `.github`, `.nojekyll` and
   `.gitignore`.
3. `git add -A && git commit -m "Rebuild site" && git push`

Settings → Pages → Source must be **GitHub Actions**. Nothing else to configure,
nothing to edit.

## Fixed in this version

**The papers were printing as raw code.** Pandoc treats indented HTML inside a
`.qmd` as an indented code block, so every paper on the live page appeared as
visible markup instead of a formatted entry. Every raw HTML block in the site is
now inside a `{=html}` passthrough fence. All 44 papers render as real elements,
with author lists, venues and 43 DOI links.

That bug reached you because my checks counted strings in the output, and the
markup string is present either way. The build is now tested against a real DOM:
the choice task, the papers filter and the share row are each driven through
their actual behaviour, 20 assertions, all passing.

## Sharing

Every page carries `og:image`, `twitter:image`, `og:title` and `og:description`
as absolute URLs, so a link pasted into LinkedIn, X, Bluesky, Slack, WhatsApp or
Teams unfurls with your card image and the page's own title rather than a bare
link.

Blog posts carry a share row: LinkedIn, X, Bluesky, Email and Copy link, each an
outlined control with an icon and a label. Copy link uses the clipboard API with
a fallback for older browsers and confirms with a "Copied" state. The footer and
the About page carry the same treatment for Email, Scholar, ORCID, GitHub,
ResearchGate, LinkedIn, X and your university profile.

The icons are drawn for this site rather than copied from the platforms. Brand
logos are trademarks, and a set of glyphs drawn in the site's own line weight
sits better with the rest of the page than five mismatched corporate marks.

## Devices

Type steps down at 700px and again at 400px rather than the layout changing
shape, so the page reads the same on a phone as on a desktop. Every tappable
control is at least 42–46px. Hover styles apply only where a pointer exists, so
nothing stays highlighted after a tap. Long author lists and DOI strings wrap
instead of widening the page. The choice table gets an extra step at 430px, and
landscape phones reclaim vertical space from the header. The homepage portrait is
priority-loaded; the About one is lazy.

## Papers

All 44 items from `assets/publications.json`, checked against your Google
Scholar record and your university staff profile. Every journal named on that
profile — Journal of Health Economics, Health Economics, Social Science &
Medicine, Empirical Economics, Health Policy, European Journal of Health
Economics, Journal of Health Politics Policy and Law, Value in Health, npj
Vaccines, Health Policy and Technology, BMJ Open, The Bone & Joint Journal — is
present. Filter by area; the counts partition exactly (16 preferences, 22 public
health, 6 other).

## Tools

`eMANDEVA-DecisionAid-V18/`, `farming-bca-tool-v18/` and
`STEPS-FETP-DecisionAid-V20/` are vendored in from their own repositories and
serve from your domain. Previously those folders held only a README and all
three links were dead.

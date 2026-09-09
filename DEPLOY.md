# Deploy

Unzip. Delete `publications/`, `blog/` and `assets/social/` in your repo
first, then drag this folder's contents onto
github.com/DrGenie/DrGenie.github.io/upload/main and commit. Everything else
overwrites in place. Dotfiles are already in your repo; leave them.

## Assessment of the deployed site, and what changed

Your deployed site is in good shape: Inter, five-item nav, collapsible
authors, 25 posts, working tool links, corrected workflow, and you had
already replaced the Social Science & Medicine placeholder with the real
paper. Four things needed fixing, none of them by adding anything.

**Papers were ordered by title within a year, not by date.** Every item now
carries an online-first month taken from ResearchGate and the journals, and
lists newest first. Your September paper on pull-forward and induced
vaccination is at the top. Its arXiv preprint has been removed from the
working papers, since the published version supersedes it.

**A blank band sat above the footer on every page.** Quarto gives the content
area a minimum height of the viewport so the footer sits at the bottom of
short pages. On About, Tools, Grants and most posts, that showed as empty
space. Removed; the footer now follows the content.

**Every Instagram card had the same curve.** Each post now gets a drawing of
its own subject: a parcel with a FREE tag for free shipping, an urn with
hidden balls for Ellsberg, an eye for eye tracking, four fading slices for the
second slice, a switch left ON for defaults, the 99% ring, a clapperboard for
the bad movie, three cups for the popcorn decoy, a grid of tiles for choice
overload, an hourglass reading 3 for scarcity, and so on for all 29. The
share button on a phone hands that exact card to the share sheet; on a desktop
it downloads it and opens instagram.com.

**Writing was one nav click away and nowhere on the homepage.** Three latest
posts now sit on the homepage as plain lines.

Four new posts for a general audience: the bad movie you keep watching (sunk
cost), the medium popcorn (decoy effect), not being able to pick anything to
watch (choice overload), and only three left in stock (scarcity). 29 posts
total, 8 of them everyday behavioural economics.

## Adding a post later

Create `blog/posts/<slug>/index.qmd` with title, description, image, author,
date and categories; end with the share block. Run
`python3 scripts/make-social-images.py` to draw its cards. If the slug
contains a keyword in the MOTIFS list at the top of that script, it gets that
picture; otherwise the generic curve. Add a keyword and a small drawing
function to give it its own.

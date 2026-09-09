"""Regenerate social preview images for every blog post.
    python3 scripts/make-social-images.py
Writes assets/social/<slug>-og.png (1200x630) and <slug>-sq.png (1080x1080).
Each card carries the category, title, the post's one-line hook, a preference
curve unique to the post, and the Dr Genie signature. Requires Pillow."""
from PIL import Image, ImageDraw, ImageFont
import pathlib, re, textwrap, glob, math, hashlib

F = glob.glob('/usr/share/fonts/**/DejaVuSans-Bold.ttf', recursive=True) + glob.glob('/usr/share/fonts/**/DejaVuSans.ttf', recursive=True)
bold = next((f for f in F if 'Bold' in f), None); reg = next((f for f in F if 'Bold' not in f), None)
if not bold: raise SystemExit("Install fonts-dejavu")
out = pathlib.Path('assets/social'); out.mkdir(parents=True, exist_ok=True)

def field_of(cats):
    c = cats.lower()
    return "Behavioural Economics" if re.search(r'behavio|everyday|decision', c) else "Health Economics"

def fit(d, text, font_path, max_w, start, min_size, max_lines):
    size = start
    while size > min_size:
        f = ImageFont.truetype(font_path, size)
        lines = textwrap.wrap(text, width=max(10, int(max_w / (size * 0.56))))
        if len(lines) <= max_lines and all(d.textlength(l, font=f) <= max_w for l in lines): return f, lines, size
        size -= 3
    f = ImageFont.truetype(font_path, min_size)
    return f, textwrap.wrap(text, width=max(10, int(max_w / (min_size * 0.56))))[:max_lines], min_size

for p in sorted(pathlib.Path('blog/posts').glob('*/index.qmd')):
    fm = p.read_text().split('---')[1]
    title = re.search(r'^title:\s*"(.+?)"', fm, re.M).group(1)
    desc = (re.search(r'^description:\s*"(.+?)"', fm, re.M) or [None, ""])[1]
    cats = (re.search(r'^categories:\s*\[(.*?)\]', fm, re.M) or [None, ""])[1]
    field = field_of(cats); slug = p.parent.name
    accent = "#9a1f35" if field == "Health Economics" else "#1f4e9a"
    seed = int(hashlib.md5(title.encode()).hexdigest(), 16)

    for name, W, H in (("og", 1200, 630), ("sq", 1080, 1080)):
        im = Image.new("RGB", (W, H), "#ffffff"); d = ImageDraw.Draw(im)
        pad = int(W * 0.07); d.rectangle([0, 0, W, int(H * 0.015)], fill=accent)
        d.text((pad, int(H * 0.09)), field.upper(), font=ImageFont.truetype(bold, int(W * 0.024)), fill=accent)

        tf, tl, ts = fit(d, title, bold, W - 2 * pad, int(W * 0.062), 30, 3 if name == "og" else 4)
        y = int(H * 0.19)
        for l in tl: d.text((pad, y), l, font=tf, fill="#0a0c0f"); y += int(ts * 1.18)

        y += int(H * 0.025)
        df, dl, ds = fit(d, desc, reg, W - 2 * pad, int(W * 0.028), 20, 3 if name == "og" else 5)
        for l in dl: d.text((pad, y), l, font=df, fill="#3a4149"); y += int(ds * 1.4)

        # preference curve, unique per post
        bx, bw = pad, W - 2 * pad
        by = y + int(H * 0.06)
        bh = max(int(H * 0.10), int(H * 0.815) - by)
        d.line([(bx, by + bh), (bx + bw, by + bh)], fill="#e3e5e8", width=2)
        d.line([(bx, by), (bx, by + bh)], fill="#e3e5e8", width=2)
        pts = []
        for k in range(41):
            t = k / 40; r = ((seed >> (k % 24)) & 7) / 7
            pts.append((bx + bw * t, by + bh - bh * (1 - math.exp(-(2.2 + r) * t)) * 0.92))
        d.line(pts, fill=accent, width=max(4, W // 200), joint="curve")
        ex, ey = pts[-1]; rr = max(6, W // 110)
        d.ellipse([ex - rr, ey - rr, ex + rr, ey + rr], fill=accent)

        d.text((pad, H - int(H * 0.135)), "Dr Genie", font=ImageFont.truetype(bold, int(W * 0.032)), fill="#0a0c0f")
        d.text((pad, H - int(H * 0.085)), f"{field}  \u00b7  mesfingenie.com", font=ImageFont.truetype(reg, int(W * 0.024)), fill="#6a7178")
        im.save(out / f"{slug}-{name}.png", optimize=True)
print("social images regenerated for", len(list(pathlib.Path('blog/posts').glob('*/index.qmd'))), "posts")

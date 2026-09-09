"""Regenerate social preview images for every blog post.

    python3 scripts/make-social-images.py

Writes assets/social/<slug>-og.png (1200x630, link previews) and
assets/social/<slug>-sq.png (1080x1080, Instagram). Requires Pillow.
"""
from PIL import Image, ImageDraw, ImageFont
import pathlib, re, textwrap, glob

FONTS = glob.glob('/usr/share/fonts/**/DejaVuSans-Bold.ttf', recursive=True) + \
        glob.glob('/usr/share/fonts/**/DejaVuSans.ttf', recursive=True)
bold = next((f for f in FONTS if 'Bold' in f), None)
reg = next((f for f in FONTS if 'Bold' not in f), None)
if not bold:
    raise SystemExit("No DejaVu fonts found. Install fonts-dejavu, or edit the paths above.")

out = pathlib.Path('assets/social'); out.mkdir(parents=True, exist_ok=True)
for p in sorted(pathlib.Path('blog/posts').glob('*/index.qmd')):
    title = re.search(r'^title:\s*"(.+?)"', p.read_text().split('---')[1], re.M).group(1)
    slug = p.parent.name
    for name, W, H in (("og", 1200, 630), ("sq", 1080, 1080)):
        im = Image.new("RGB", (W, H), "#ffffff"); d = ImageDraw.Draw(im)
        d.rectangle([0, 0, W, 12], fill="#9a1f35")
        pad = int(W * 0.075)
        d.text((pad, int(H*0.13)), "mesfingenie.com",
               font=ImageFont.truetype(reg, int(W*0.026)), fill="#6a7178")
        size = int(W * (0.070 if name == "og" else 0.072))
        while size > 24:
            wrap = textwrap.wrap(title, width=max(12, int((W - 2*pad) / (size*0.52))))
            if len(wrap) * size * 1.22 <= H * (0.44 if name == "og" else 0.50):
                break
            size -= 3
        y = int(H * (0.27 if name == "og" else 0.28))
        for line in wrap:
            d.text((pad, y), line, font=ImageFont.truetype(bold, size), fill="#0a0c0f")
            y += int(size * 1.22)
        d.line([(pad, H-int(H*0.17)), (W-pad, H-int(H*0.17))], fill="#e3e5e8", width=2)
        d.text((pad, H-int(H*0.125)), "Mesfin Genie",
               font=ImageFont.truetype(bold, int(W*0.030)), fill="#16191d")
        d.text((pad, H-int(H*0.075)), "Health economics, University of Newcastle",
               font=ImageFont.truetype(reg, int(W*0.024)), fill="#6a7178")
        im.save(out / f"{slug}-{name}.png", optimize=True)
print("done")

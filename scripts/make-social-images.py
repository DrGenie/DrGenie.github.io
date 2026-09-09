"""Regenerate social preview images for every blog post.

    python3 scripts/make-social-images.py

Writes assets/social/<slug>-og.png (1200x630, link previews) and
<slug>-sq.png (1080x1080, Instagram). Each card carries the category, the
title, the post's one-line hook, a motif drawn for that post's subject, and
the Dr Genie signature. Requires Pillow.

To give a new post its own picture, add a line to MOTIFS: a keyword from the
slug and a drawing function. Unmatched posts get the generic curve.
"""
from PIL import Image, ImageDraw, ImageFont
import pathlib, re, textwrap, glob, math, random

HERE = pathlib.Path(__file__).resolve().parents[1]
def _font(name, fallback_glob):
    f = HERE / "assets" / "fonts" / name
    if f.exists(): return str(f)
    g = glob.glob(fallback_glob, recursive=True)
    if not g: raise SystemExit("No fonts found: add assets/fonts/Inter-*.ttf or install fonts-dejavu")
    return g[0]
BOLD = _font("Inter-Bold.ttf", '/usr/share/fonts/**/DejaVuSans-Bold.ttf')
SEMI = _font("Inter-SemiBold.ttf", '/usr/share/fonts/**/DejaVuSans-Bold.ttf')
REG  = _font("Inter-Regular.ttf", '/usr/share/fonts/**/DejaVuSans.ttf')
HANDLE = "@DrGenie"
OUT = pathlib.Path('assets/social'); OUT.mkdir(parents=True, exist_ok=True)
INK, MUTED, RULE, SOFT, WHITE = "#0a0c0f", "#6a7178", "#e3e5e8", "#f4f5f7", "#ffffff"
def W_(s, k): return max(2, int(s * k))
def fnt(path, size): return ImageFont.truetype(path, max(8, int(size)))

# ---- motifs: draw inside the s x s box at (x, y) in colour c --------------
def m_percent(d, x, y, s, c):
    w = W_(s, .11); box = [x+w, y+w, x+s-w, y+s-w]
    d.arc(box, -90, 262, fill=c, width=w); d.arc(box, 262, 270, fill=RULE, width=w)
    f = fnt(BOLD, s*.26); t = "99%"; d.text((x+(s-d.textlength(t, font=f))/2, y+s*.37), t, font=f, fill=INK)
def m_play(d, x, y, s, c):
    w = W_(s, .07); box = [x+w, y+w, x+s-w, y+s-w]
    d.arc(box, -90, 200, fill=c, width=w); d.arc(box, 200, 270, fill=RULE, width=w)
    cx, cy, r = x+s/2, y+s/2, s*.2; d.polygon([(cx-r*.7, cy-r), (cx-r*.7, cy+r), (cx+r, cy)], fill=INK)
def m_doors(d, x, y, s, c):
    for dx, col in ((.06, INK), (.54, c)):
        bx = x+s*dx; d.rectangle([bx, y+s*.12, bx+s*.4, y+s*.92], outline=col, width=W_(s, .035))
        d.ellipse([bx+s*.3, y+s*.5, bx+s*.35, y+s*.55], fill=col)
def m_question(d, x, y, s, c):
    d.text((x+s*.16, y-s*.14), "?", font=fnt(BOLD, s*.95), fill=c); d.text((x+s*.6, y+s*.5), "?", font=fnt(BOLD, s*.36), fill=INK)
def m_shield(d, x, y, s, c):
    d.polygon([(x+s*.5, y+s*.05), (x+s*.9, y+s*.2), (x+s*.85, y+s*.6), (x+s*.5, y+s*.95), (x+s*.15, y+s*.6), (x+s*.1, y+s*.2)], outline=c, width=W_(s, .04))
    d.line([(x+s*.32, y+s*.5), (x+s*.45, y+s*.64), (x+s*.7, y+s*.36)], fill=INK, width=W_(s, .06), joint="curve")
def m_coins(d, x, y, s, c):
    for i in range(5):
        yy = y+s*.78-i*s*.11; d.ellipse([x+s*.2, yy-s*.09, x+s*.8, yy+s*.09], fill=WHITE, outline=c if i == 4 else INK, width=W_(s, .03))
    d.text((x+s*.44, y+s*.2), "$", font=fnt(BOLD, s*.16), fill=c)
def m_pizza(d, x, y, s, c):
    r0, g0, b0 = int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
    for i, a in enumerate((1.0, .62, .42, .22)):
        col = tuple(int(v*a+255*(1-a)) for v in (r0, g0, b0)); cx = x+s*(.22+i*.19)
        d.polygon([(cx, y+s*.9), (cx-s*.13, y+s*.25), (cx+s*.13, y+s*.25)], fill=col, outline=INK, width=2)
def m_dumbbell(d, x, y, s, c):
    cy = y+s*.5; d.rectangle([x+s*.3, cy-s*.04, x+s*.7, cy+s*.04], fill=INK)
    for bx in (.1, .72): d.rectangle([x+s*bx, cy-s*.2, x+s*(bx+.18), cy+s*.2], fill=c)
def m_package(d, x, y, s, c):
    d.rectangle([x+s*.12, y+s*.3, x+s*.72, y+s*.9], outline=INK, width=W_(s, .035))
    d.line([(x+s*.42, y+s*.3), (x+s*.42, y+s*.9)], fill=INK, width=W_(s, .03)); d.line([(x+s*.12, y+s*.5), (x+s*.72, y+s*.5)], fill=INK, width=W_(s, .03))
    d.polygon([(x+s*.6, y+s*.06), (x+s*.96, y+s*.06), (x+s*.96, y+s*.36), (x+s*.78, y+s*.44), (x+s*.6, y+s*.36)], fill=c)
    d.text((x+s*.65, y+s*.14), "FREE", font=fnt(BOLD, s*.1), fill=WHITE)
def m_steps(d, x, y, s, c):
    pts = [(.05, .85), (.3, .85), (.3, .55), (.55, .55), (.55, .3), (.95, .3)]
    d.line([(x+s*a, y+s*b) for a, b in pts], fill=c, width=W_(s, .06), joint="curve"); d.line([(x+s*.55, y+s*.3), (x+s*.95, y+s*.3)], fill=INK, width=W_(s, .06))
def m_dice(d, x, y, s, c):
    for bx, by, col, pips in ((.08, .25, INK, [(.5, .5)]), (.48, .08, c, [(.3, .3), (.7, .7), (.3, .7), (.7, .3), (.5, .5)])):
        sz = s*.44; d.rounded_rectangle([x+s*bx, y+s*by, x+s*bx+sz, y+s*by+sz], radius=int(s*.05), outline=col, width=W_(s, .035))
        for px, py in pips: d.ellipse([x+s*bx+sz*px-s*.035, y+s*by+sz*py-s*.035, x+s*bx+sz*px+s*.035, y+s*by+sz*py+s*.035], fill=col)
def m_urn(d, x, y, s, c):
    d.polygon([(x+s*.2, y+s*.25), (x+s*.8, y+s*.25), (x+s*.72, y+s*.92), (x+s*.28, y+s*.92)], outline=INK, width=W_(s, .035))
    for px, py, col in ((.38, .72, c), (.55, .78, INK), (.47, .58, c), (.62, .62, WHITE)):
        d.ellipse([x+s*px-s*.08, y+s*py-s*.08, x+s*px+s*.08, y+s*py+s*.08], fill=col, outline=INK, width=2)
    d.text((x+s*.4, y-s*.02), "?", font=fnt(BOLD, s*.2), fill=c)
def m_scale(d, x, y, s, c):
    d.line([(x+s*.5, y+s*.2), (x+s*.5, y+s*.9)], fill=INK, width=W_(s, .04)); d.line([(x+s*.3, y+s*.9), (x+s*.7, y+s*.9)], fill=INK, width=W_(s, .04))
    d.line([(x+s*.12, y+s*.42), (x+s*.88, y+s*.22)], fill=INK, width=W_(s, .035))
    d.ellipse([x+s*.02, y+s*.38, x+s*.28, y+s*.64], fill=c); d.ellipse([x+s*.76, y+s*.16, x+s*.92, y+s*.32], fill=INK)
def m_gift(d, x, y, s, c):
    d.rectangle([x+s*.15, y+s*.4, x+s*.85, y+s*.92], outline=INK, width=W_(s, .035))
    d.rectangle([x+s*.1, y+s*.28, x+s*.9, y+s*.42], fill=c); d.rectangle([x+s*.45, y+s*.28, x+s*.55, y+s*.92], fill=c)
    d.ellipse([x+s*.3, y+s*.1, x+s*.48, y+s*.3], outline=c, width=W_(s, .035)); d.ellipse([x+s*.52, y+s*.1, x+s*.7, y+s*.3], outline=c, width=W_(s, .035))
def m_toggle(d, x, y, s, c):
    d.rounded_rectangle([x+s*.08, y+s*.3, x+s*.92, y+s*.7], radius=int(s*.2), fill=c); d.ellipse([x+s*.12, y+s*.34, x+s*.44, y+s*.66], fill=WHITE)
    d.text((x+s*.55, y+s*.42), "ON", font=fnt(BOLD, s*.12), fill=WHITE)
def m_tag(d, x, y, s, c):
    d.polygon([(x+s*.1, y+s*.5), (x+s*.35, y+s*.2), (x+s*.92, y+s*.2), (x+s*.92, y+s*.8), (x+s*.35, y+s*.8)], fill=c)
    d.ellipse([x+s*.22, y+s*.45, x+s*.3, y+s*.55], fill=WHITE); d.text((x+s*.4, y+s*.38), "$9.99", font=fnt(BOLD, s*.18), fill=WHITE)
def m_target(d, x, y, s, c):
    for r, col in ((.46, INK), (.32, c), (.18, INK)): d.ellipse([x+s*(.5-r), y+s*(.5-r), x+s*(.5+r), y+s*(.5+r)], outline=col, width=W_(s, .04))
    d.ellipse([x+s*.44, y+s*.44, x+s*.56, y+s*.56], fill=c)
def m_scatter(d, x, y, s, c):
    rnd = random.Random(7); d.line([(x+s*.05, y+s*.5), (x+s*.95, y+s*.5)], fill=c, width=W_(s, .04))
    for i in range(14):
        px = x+s*(.08+i*.065); py = y+s*(.5+(.32 if i % 2 else -.32)+rnd.uniform(-.08, .08))
        d.ellipse([px-s*.035, py-s*.035, px+s*.035, py+s*.035], fill=INK)
def m_bubble(d, x, y, s, c):
    d.rounded_rectangle([x+s*.08, y+s*.15, x+s*.92, y+s*.72], radius=int(s*.12), outline=INK, width=W_(s, .035))
    d.polygon([(x+s*.25, y+s*.7), (x+s*.2, y+s*.9), (x+s*.42, y+s*.71)], fill=INK)
    d.line([(x+s*.33, y+s*.44), (x+s*.45, y+s*.56), (x+s*.68, y+s*.32)], fill=c, width=W_(s, .06), joint="curve")
def m_umbrella(d, x, y, s, c):
    d.pieslice([x+s*.1, y+s*.15, x+s*.9, y+s*.95], 180, 360, fill=c); d.line([(x+s*.5, y+s*.55), (x+s*.5, y+s*.92)], fill=INK, width=W_(s, .04))
    d.rectangle([x+s*.72, y+s*.62, x+s*.98, y+s*.8], outline=INK, width=W_(s, .03))
def m_clipboard(d, x, y, s, c):
    d.rectangle([x+s*.18, y+s*.12, x+s*.82, y+s*.95], outline=INK, width=W_(s, .035)); d.rectangle([x+s*.38, y+s*.05, x+s*.62, y+s*.18], fill=INK)
    for i, done in enumerate((True, True, False)):
        yy = y+s*(.35+i*.18); d.rectangle([x+s*.28, yy, x+s*.38, yy+s*.1], outline=c if done else INK, width=W_(s, .03), fill=c if done else None)
        d.line([(x+s*.45, yy+s*.05), (x+s*.72, yy+s*.05)], fill=RULE, width=W_(s, .03))
def m_grid(d, x, y, s, c):
    for r in range(4): d.line([(x+s*.05, y+s*(.12+r*.2)), (x+s*.95, y+s*(.12+r*.2))], fill=RULE, width=2)
    d.rectangle([x+s*.55, y+s*.1, x+s*.95, y+s*.92], outline=c, width=W_(s, .04))
    for r in range(4):
        yy = y+s*(.18+r*.2); d.rectangle([x+s*.12, yy, x+s*.4, yy+s*.08], fill=RULE); d.rectangle([x+s*.62, yy, x+s*.88, yy+s*.08], fill=c if r == 1 else RULE)
def m_eye(d, x, y, s, c):
    d.ellipse([x+s*.05, y+s*.22, x+s*.95, y+s*.78], outline=INK, width=W_(s, .035))
    d.ellipse([x+s*.35, y+s*.35, x+s*.65, y+s*.65], fill=c); d.ellipse([x+s*.44, y+s*.44, x+s*.56, y+s*.56], fill=INK)
    for px, py in ((.2, .5), (.8, .5), (.5, .12), (.5, .88)): d.ellipse([x+s*px-s*.03, y+s*py-s*.03, x+s*px+s*.03, y+s*py+s*.03], fill=c)
def m_sliders(d, x, y, s, c):
    for i, pos in enumerate((.3, .7, .5)):
        yy = y+s*(.25+i*.25); d.line([(x+s*.1, yy), (x+s*.9, yy)], fill=RULE, width=W_(s, .04)); d.line([(x+s*.1, yy), (x+s*pos, yy)], fill=c, width=W_(s, .04))
        d.ellipse([x+s*pos-s*.06, yy-s*.06, x+s*pos+s*.06, yy+s*.06], fill=INK)
def m_clapper(d, x, y, s, c):
    d.rectangle([x+s*.1, y+s*.4, x+s*.9, y+s*.9], outline=INK, width=W_(s, .035))
    d.polygon([(x+s*.1, y+s*.4), (x+s*.9, y+s*.4), (x+s*.9, y+s*.22), (x+s*.15, y+s*.12)], fill=c)
    d.line([(x+s*.5, y+s*.55), (x+s*.5, y+s*.76)], fill=c, width=W_(s, .05)); d.polygon([(x+s*.42, y+s*.72), (x+s*.58, y+s*.72), (x+s*.5, y+s*.84)], fill=c)
def m_cups(d, x, y, s, c):
    for i, h in enumerate((.45, .62, .8)):
        bx = x+s*(.08+i*.32); top = y+s*(.92-h); mid = (i == 1)
        d.polygon([(bx, top), (bx+s*.26, top), (bx+s*.22, y+s*.92), (bx+s*.04, y+s*.92)], outline=c if mid else INK, width=W_(s, .035), fill=c if mid else None)
def m_tiles(d, x, y, s, c):
    n = 5; g = s*.03; t = (s-g*(n+1))/n
    for r in range(n):
        for k in range(n):
            d.rounded_rectangle([x+g+k*(t+g), y+g+r*(t+g), x+g+k*(t+g)+t, y+g+r*(t+g)+t], radius=int(s*.015), fill=c if (r, k) == (2, 2) else RULE)
def m_hourglass(d, x, y, s, c):
    d.polygon([(x+s*.2, y+s*.08), (x+s*.8, y+s*.08), (x+s*.5, y+s*.5), (x+s*.8, y+s*.92), (x+s*.2, y+s*.92), (x+s*.5, y+s*.5)], outline=INK, width=W_(s, .035))
    d.polygon([(x+s*.32, y+s*.15), (x+s*.68, y+s*.15), (x+s*.5, y+s*.42)], fill=c); d.polygon([(x+s*.5, y+s*.62), (x+s*.7, y+s*.88), (x+s*.3, y+s*.88)], fill=c)
    d.text((x+s*.74, y), "3", font=fnt(BOLD, s*.16), fill=c)
def m_lanes(d, x, y, s, c):            # two queues, one moving
    for i, (col, n) in enumerate(((INK, 5), (c, 3))):
        lx = x+s*(.25+i*.5)
        d.line([(lx, y+s*.08), (lx, y+s*.95)], fill=RULE, width=W_(s, .03))
        for k in range(n): d.ellipse([lx-s*.07, y+s*(.92-k*.17)-s*.07, lx+s*.07, y+s*(.92-k*.17)+s*.07], fill=col)
    d.polygon([(x+s*.75, y+s*.02), (x+s*.68, y+s*.14), (x+s*.82, y+s*.14)], fill=c)
def m_tenk(d, x, y, s, c):              # 10,000 with a footprint
    d.text((x+s*.02, y+s*.22), "10k", font=fnt(BOLD, s*.42), fill=c)
    for i, (px, py) in enumerate(((.62, .68), (.8, .58))):
        d.ellipse([x+s*px-s*.07, y+s*py-s*.11, x+s*px+s*.07, y+s*py+s*.11], fill=INK)
        d.ellipse([x+s*px-s*.05, y+s*py+.13*s, x+s*px+s*.05, y+s*py+.2*s], fill=INK)
def m_tipscreen(d, x, y, s, c):         # card terminal with three buttons
    d.rounded_rectangle([x+s*.12, y+s*.05, x+s*.88, y+s*.95], radius=int(s*.08), outline=INK, width=W_(s, .035))
    for i, t in enumerate(("15%", "20%", "25%")):
        yy = y+s*(.2+i*.22); mid = (i == 1)
        d.rounded_rectangle([x+s*.22, yy, x+s*.78, yy+s*.16], radius=int(s*.04), fill=c if mid else RULE)
        d.text((x+s*.42, yy+s*.03), t, font=fnt(BOLD, s*.1), fill=WHITE if mid else INK)
def m_ticket(d, x, y, s, c):            # a ticket stub, torn
    d.rounded_rectangle([x+s*.08, y+s*.28, x+s*.92, y+s*.72], radius=int(s*.06), fill=c)
    for cx in (.08, .92): d.ellipse([x+s*cx-s*.07, y+s*.5-s*.07, x+s*cx+s*.07, y+s*.5+s*.07], fill=WHITE)
    for k in range(6): d.line([(x+s*.62, y+s*(.32+k*.07)), (x+s*.62, y+s*(.35+k*.07))], fill=WHITE, width=W_(s, .02))
    d.text((x+s*.18, y+s*.39), "$50", font=fnt(BOLD, s*.17), fill=WHITE)
def m_clock(d, x, y, s, c):
    d.ellipse([x+s*.08, y+s*.08, x+s*.92, y+s*.92], outline=INK, width=W_(s, .04))
    cx, cy = x+s*.5, y+s*.5
    d.line([(cx, cy), (cx, y+s*.2)], fill=INK, width=W_(s, .045)); d.line([(cx, cy), (x+s*.72, cy+s*.08)], fill=c, width=W_(s, .045))
    d.ellipse([cx-s*.04, cy-s*.04, cx+s*.04, cy+s*.04], fill=c)
    for a in range(12):
        import math as _m; r1, r2 = s*.38, s*.42; ang = a*_m.pi/6
        d.line([(cx+r1*_m.sin(ang), cy-r1*_m.cos(ang)), (cx+r2*_m.sin(ang), cy-r2*_m.cos(ang))], fill=INK, width=W_(s, .02))
def m_plate(d, x, y, s, c):             # same portion, two plates
    d.ellipse([x+s*.02, y+s*.15, x+s*.62, y+s*.75], outline=INK, width=W_(s, .03))
    d.ellipse([x+s*.22, y+s*.35, x+s*.42, y+s*.55], fill=c)
    d.ellipse([x+s*.62, y+s*.42, x+s*.98, y+s*.78], outline=INK, width=W_(s, .03))
    d.ellipse([x+s*.7, y+s*.5, x+s*.9, y+s*.7], fill=c)
def m_curve(d, x, y, s, c):
    pts = [(x+s*t/40, y+s*.9-s*.8*(1-math.exp(-2.6*t/40))) for t in range(41)]
    d.line([(x+s*.02, y+s*.92), (x+s*.98, y+s*.92)], fill=RULE, width=2); d.line(pts, fill=c, width=W_(s, .05), joint="curve")

MOTIFS = [("99", m_percent), ("autoplay", m_play), ("doctor", m_doors), ("question-behind", m_question),
    ("mandates", m_shield), ("fifty-dollar", m_coins), ("slice", m_pizza), ("gym", m_dumbbell),
    ("shipping", m_package), ("pay-rise", m_steps), ("allais", m_dice), ("ellsberg", m_urn),
    ("loss-aversion", m_scale), ("power-of-free", m_gift), ("default", m_toggle), ("risk-versus", m_dice),
    ("left-digit", m_tag), ("benchmark", m_target), ("averages", m_scatter), ("feedback", m_bubble),
    ("insurance", m_umbrella), ("preference-research", m_clipboard), ("discrete-choice", m_grid),
    ("eye-tracking", m_eye), ("decision-tools", m_sliders), ("bad-movie", m_clapper),
    ("popcorn", m_cups), ("pick-anything", m_tiles), ("left-in-stock", m_hourglass),
    ("queue", m_lanes), ("ten-thousand", m_tenk), ("tip-more", m_tipscreen), ("lost-ticket", m_ticket),
    ("waiting-rooms", m_clock), ("bigger-plate", m_plate)]
def motif_for(slug):
    return next((fn for k, fn in MOTIFS if k in slug), m_curve)
def field_of(cats):
    return "Behavioural Economics" if re.search(r'behavio|decision', cats.lower()) else "Health Economics"
def fit(d, text, path, max_w, start, min_size, max_lines):
    size = start
    while size > min_size:
        f = fnt(path, size); lines = textwrap.wrap(text, width=max(10, int(max_w/(size*.56))))
        if len(lines) <= max_lines and all(d.textlength(l, font=f) <= max_w for l in lines): return f, lines, size
        size -= 3
    return fnt(path, min_size), textwrap.wrap(text, width=max(10, int(max_w/(min_size*.56))))[:max_lines], min_size

def card(title, desc, field, motif, W, H, square):
    accent = "#9a1f35" if field == "Health Economics" else "#1f4e9a"
    chip_bg = "#fbeef0" if field == "Health Economics" else "#e9f0fb"
    im = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(im); pad = int(W*.075)
    d.rectangle([0, 0, W, int(H*.012)], fill=accent)

    # category chip
    cf = fnt(SEMI, W*.021); label = field.upper(); tw = d.textlength(label, font=cf); ch = int(W*.036)
    cy = int(H*.075)
    d.rounded_rectangle([pad, cy, pad+tw+int(W*.03), cy+ch], radius=ch//2, fill=chip_bg)
    d.text((pad+int(W*.015), cy+int(ch*.24)), label, font=cf, fill=accent)

    # motif box
    if square:
        ms = int(W*.38); mx, my = W-pad-ms, H-int(H*.2)-ms
        text_w = W-2*pad; desc_w = W-2*pad-ms-int(W*.05)
    else:
        ms = int(H*.56); mx, my = W-pad-ms, int(H*.2)
        text_w = mx-pad-int(W*.045); desc_w = text_w
    pm = int(ms*.1)
    d.rounded_rectangle([mx-pm, my-pm, mx+ms+pm, my+ms+pm], radius=int(ms*.1), fill=SOFT)

    # title
    tf, tl, ts = fit(d, title, BOLD, text_w, int(W*.064), 30, 4 if square else 3)
    y = cy+ch+int(H*.05)
    for l in tl: d.text((pad, y), l, font=tf, fill=INK); y += int(ts*1.16)

    # hook
    y += int(H*.022)
    df, dl, ds = fit(d, desc, REG, desc_w, int(W*.028), 20, 6 if square else 3)
    for l in dl: d.text((pad, y), l, font=df, fill="#3f464e"); y += int(ds*1.42)

    motif(d, mx, my, ms, accent)

    # signature row: name and field left, handle right
    by = H-int(H*.085)
    d.text((pad, by-int(W*.04)), "Dr Genie", font=fnt(BOLD, W*.03), fill=INK)
    d.text((pad, by), field + "  \u00b7  mesfingenie.com", font=fnt(REG, W*.021), fill=MUTED)
    hf = fnt(SEMI, W*.024); hw = d.textlength(HANDLE, font=hf)
    d.text((W-pad-hw, by-int(W*.005)), HANDLE, font=hf, fill=accent)
    return im

n = 0
for p in sorted(pathlib.Path('blog/posts').glob('*/index.qmd')):
    fm = p.read_text().split('---')[1]
    title = re.search(r'^title:\s*"(.+?)"', fm, re.M).group(1)
    desc = (re.search(r'^description:\s*"(.+?)"', fm, re.M) or [None, ""])[1]
    cats = (re.search(r'^categories:\s*\[(.*?)\]', fm, re.M) or [None, ""])[1]
    slug = p.parent.name; field = field_of(cats); mo = motif_for(slug)
    card(title, desc, field, mo, 1200, 630, False).save(OUT/f"{slug}-og.png", optimize=True)
    card(title, desc, field, mo, 1080, 1080, True).save(OUT/f"{slug}-sq.png", optimize=True)
    n += 1
print("cards generated for", n, "posts")

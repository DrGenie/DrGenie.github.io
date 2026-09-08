#!/usr/bin/env python3
"""Static pre-build validation for the Quarto academic website."""
import glob, re, json, sys, os
try:
    import yaml
except Exception:
    yaml=None

root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
issues=[]; ok=[]
qmds=sorted(glob.glob('**/*.qmd', recursive=True))
qmds=[q for q in qmds if 'eMANDEVA' not in q and 'farming' not in q and 'STEPS' not in q]

# Front matter, descriptions, and H1 count.
titles={}
for q in qmds:
    t=open(q,encoding='utf-8').read()
    fm=t.split('---')[1] if t.startswith('---') else ''
    if 'pagetitle:' not in fm and 'title:' not in fm: issues.append(f'{q}: missing title/pagetitle')
    if 'description:' not in fm: issues.append(f'{q}: missing meta description')
    h1=len(re.findall(r'<h1[ >]', t))
    if (q.endswith('index.qmd') or 'editorial' in q) and h1>1: issues.append(f'{q}: {h1} H1 headings (should be 1)')
    key=re.search(r'pagetitle:\s*"([^"]+)"', fm)
    if key: titles.setdefault(key.group(1),[]).append(q)
for tt,ps in titles.items():
    if len(ps)>1: issues.append(f'duplicate pagetitle "{tt}" in {ps}')

# Spelling and punctuation hygiene.
for q in qmds:
    t=open(q,encoding='utf-8').read()
    if re.search(r'uncertainity', t, re.I): issues.append(f'{q}: "Uncertainity" typo')
    if '\u2014' in t or '\u2013' in t: issues.append(f'{q}: contains em/en dash')

# Internal links.
def resolves(href):
    href=href.split('#')[0].split('?')[0]
    if not href.startswith('/'): return True
    if href.startswith('/assets/'): return os.path.exists('.'+href)
    if os.path.exists('.'+href): return True
    p=href.strip('/')
    return os.path.exists(p+'/index.qmd') or os.path.exists(p+'.qmd') or (p=='' and os.path.exists('index.qmd'))
linkbad=set()
for q in qmds:
    for href in re.findall(r'href="(/[^"]*)"', open(q,encoding='utf-8').read()):
        if not resolves(href): linkbad.add(f'{q} -> {href}')
for b in sorted(linkbad): issues.append('broken internal link: '+b)

# YAML and JSON parsing.
if yaml:
    for y in glob.glob('data/*.yml')+['_variables.yml','_quarto.yml']:
        try: yaml.safe_load(open(y,encoding='utf-8'))
        except Exception as e: issues.append(f'{y}: YAML error {e}')
for j in glob.glob('assets/*.json'):
    try: json.load(open(j,encoding='utf-8'))
    except Exception as e: issues.append(f'{j}: JSON error {e}')

# JSON-LD blocks.
for q in qmds+['assets/head.html']:
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(q,encoding='utf-8').read(), re.S):
        try: json.loads(m)
        except Exception as e: issues.append(f'{q}: invalid JSON-LD ({e})')

# Canonical public facts.
allq='\n'.join(open(q,encoding='utf-8').read() for q in qmds)
if re.search(r'Bologna[^0-9]*2025', allq): issues.append('Bologna year 2025 still present (should be 2015)')
else: ok.append('Bologna MSc year = 2015 everywhere')
home=open('index.qmd',encoding='utf-8').read()
if 'Senior Lecturer in Health Economics' not in home: issues.append('homepage missing public title "Senior Lecturer in Health Economics"')
else: ok.append('homepage public title is Senior Lecturer in Health Economics')
if 'Continuing Senior Lecturer' in home: issues.append('homepage exposes appointment classification in public title')

# Tool launch safety: standalone app folders must contain index.html before direct launch links are allowed.
app_paths=['/eMANDEVA-DecisionAid-V18/','/farming-bca-tool-v18/','/STEPS-FETP-DecisionAid-V20/']
for href in app_paths:
    folder=href.strip('/')
    has_app=os.path.exists(os.path.join(folder,'index.html'))
    references=[]
    for q in qmds:
        if f'href="{href}"' in open(q,encoding='utf-8').read(): references.append(q)
    if references and not has_app: issues.append(f'direct launch link to unavailable app {href} in {references}')
    elif has_app: ok.append(f'standalone app available: {href}')

# DOI syntax.
if os.path.exists('assets/publications.json'):
    try:
        pubs=json.load(open('assets/publications.json',encoding='utf-8'))
        dois=re.findall(r'10\.\d{4,9}/[^\s"]+', json.dumps(pubs))
        bad=[d for d in dois if not re.match(r'^10\.\d{4,9}/\S+$', d)]
        if bad: issues.append(f'publications.json: malformed DOI-like values {bad}')
        else: ok.append(f'publications.json parsed; {len(dois)} DOI-like strings, syntax OK')
    except Exception as e: issues.append(f'publications.json: {e}')

# Image alt text.
for q in qmds:
    for img in re.findall(r'<img[^>]*>', open(q,encoding='utf-8').read()):
        if 'alt=' not in img: issues.append(f'{q}: <img> without alt')
        elif re.search(r'alt=""', img): issues.append(f'{q}: empty alt text')

# No public verification placeholders.
BAD=['to be confirmed','pending confirmation','being confirmed','coming soon','to confirm','being checked']
for q in qmds:
    low=open(q,encoding='utf-8').read().lower()
    for b in BAD:
        if b in low: issues.append(f'{q}: public verification note "{b}"')

# Navigation restraint.
if yaml:
    d=yaml.safe_load(open('_quarto.yml',encoding='utf-8'))
    n=len(d['website']['navbar']['left'])
    if n>5: issues.append(f'navbar has {n} primary items (editorial target max 5)')
    else: ok.append(f'navigation has {n} primary items')

print('STATIC VALIDATION REPORT')
print('='*50)
print(f'Pages checked: {len(qmds)}')
print(f'PASSED checks: {len(ok)}')
for o in ok: print('  [ok] '+o)
print(f'ISSUES: {len(issues)}')
for i in issues: print('  [!] '+i)
sys.exit(1 if issues else 0)

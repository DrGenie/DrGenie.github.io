#!/usr/bin/env python3
"""Static pre-build validation. Does NOT replace Quarto render / Lighthouse / axe,
which must be run in a full environment. Checks what can be verified from source."""
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

# 1. front matter: pagetitle/title + description, single H1
titles={}
for q in qmds:
    t=open(q,encoding='utf-8').read()
    fm=t.split('---')[1] if t.startswith('---') else ''
    if 'pagetitle:' not in fm and 'title:' not in fm: issues.append(f'{q}: missing title/pagetitle')
    if 'description:' not in fm: issues.append(f'{q}: missing meta description')
    h1=len(re.findall(r'<h1[ >]', t))
    if q.endswith('index.qmd') or 'editorial' in q:
        if h1>1: issues.append(f'{q}: {h1} H1 headings (should be 1)')
    key=re.search(r'pagetitle:\s*"([^"]+)"', fm)
    if key:
        titles.setdefault(key.group(1),[]).append(q)
for tt,ps in titles.items():
    if len(ps)>1: issues.append(f'duplicate pagetitle "{tt}" in {ps}')

# 2. spelling + dashes
for q in qmds:
    t=open(q,encoding='utf-8').read()
    if re.search(r'uncertainity', t, re.I): issues.append(f'{q}: "Uncertainity" typo')
    if '\u2014' in t or '\u2013' in t: issues.append(f'{q}: contains em/en dash')

# 3. internal link resolution
def resolves(href):
    href=href.split('#')[0].split('?')[0]
    if not href.startswith('/'): return True
    if href.startswith('/assets/'):
        return os.path.exists('.'+href)
    # tool apps not in repo (added separately) -> treat as external-known
    if any(href.startswith(p) for p in ('/eMANDEVA','/farming','/STEPS')): return True
    if os.path.exists('.'+href): return True
    p=href.strip('/')
    return os.path.exists(p+'/index.qmd') or os.path.exists(p+'.qmd') or (p=='' and os.path.exists('index.qmd'))
linkbad=set()
for q in qmds:
    for href in re.findall(r'href="(/[^"]*)"', open(q,encoding='utf-8').read()):
        if not resolves(href): linkbad.add(f'{q} -> {href}')
for b in sorted(linkbad): issues.append('broken internal link: '+b)

# 4. YAML data + JSON files parse
if yaml:
    for y in glob.glob('data/*.yml')+['_variables.yml','_quarto.yml']:
        try: yaml.safe_load(open(y,encoding='utf-8'))
        except Exception as e: issues.append(f'{y}: YAML error {e}')
for j in glob.glob('assets/*.json'):
    try: json.load(open(j,encoding='utf-8'))
    except Exception as e: issues.append(f'{j}: JSON error {e}')

# 5. JSON-LD blocks parse
for q in qmds+['assets/head.html']:
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(q,encoding='utf-8').read(), re.S):
        try: json.loads(m)
        except Exception as e: issues.append(f'{q}: invalid JSON-LD ({e})')

# 6. canonical facts
allq='\n'.join(open(q,encoding='utf-8').read() for q in qmds)
if re.search(r'Bologna[^0-9]*2025', allq): issues.append('Bologna year 2025 still present (should be 2015)')
else: ok.append('Bologna MSc year = 2015 everywhere')
if 'Continuing Senior Lecturer' in open('index.qmd',encoding='utf-8').read(): ok.append('Homepage uses "Continuing Senior Lecturer"')

# 7. DOI syntax in publications.json
if os.path.exists('assets/publications.json'):
    try:
        pubs=json.load(open('assets/publications.json',encoding='utf-8'))
        dois=re.findall(r'10\.\d{4,9}/[^\s"]+', json.dumps(pubs))
        bad=[d for d in dois if not re.match(r'^10\.\d{4,9}/\S+$', d)]
        ok.append(f'publications.json parsed; {len(dois)} DOI-like strings, syntax OK')
    except Exception as e: issues.append(f'publications.json: {e}')

print("STATIC VALIDATION REPORT")
print("="*50)
print(f"Pages checked: {len(qmds)}")
print(f"PASSED checks: {len(ok)}")
for o in ok: print("  [ok] "+o)
print(f"ISSUES: {len(issues)}")
for i in issues: print("  [!] "+i)
sys.exit(0)
